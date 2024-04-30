import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RebateSvc
// Description: This is the maintenance object for Rebates
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get Rebates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Rebates
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrRow
   */  
export function get_Rebates(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Rebates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RebateHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Rebates(requestBody:Erp_Tablesets_RebateHdrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Rebate item
   Description: Calls GetByID to retrieve the Rebate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Rebate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateHdrRow
   */  
export function get_Rebates_Company_RebateID(Company:string, RebateID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Rebate for the service
   Description: Calls UpdateExt to update Rebate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Rebate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Rebates_Company_RebateID(Company:string, RebateID:string, requestBody:Erp_Tablesets_RebateHdrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")", {
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
   Summary: Call UpdateExt to delete Rebate item
   Description: Call UpdateExt to delete Rebate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Rebate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Rebates_Company_RebateID(Company:string, RebateID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")", {
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
   Description: Get RebateCusts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateCusts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustRow
   */  
export function get_Rebates_Company_RebateID_RebateCusts(Company:string, RebateID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateCusts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RebateCust item
   Description: Calls GetByID to retrieve the RebateCust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCust1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateCustRow
   */  
export function get_Rebates_Company_RebateID_RebateCusts_Company_RebateID_CustNum(Company:string, RebateID:string, CustNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateCustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateCustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RebateDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateDtlRow
   */  
export function get_Rebates_Company_RebateID_RebateDtls(Company:string, RebateID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RebateDtl item
   Description: Calls GetByID to retrieve the RebateDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateDtlRow
   */  
export function get_Rebates_Company_RebateID_RebateDtls_Company_RebateID_LineNum(Company:string, RebateID:string, LineNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RebatePymts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebatePymts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebatePymtRow
   */  
export function get_Rebates_Company_RebateID_RebatePymts(Company:string, RebateID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebatePymtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebatePymts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebatePymtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RebatePymt item
   Description: Calls GetByID to retrieve the RebatePymt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebatePymt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param PymtDate Desc: PymtDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebatePymtRow
   */  
export function get_Rebates_Company_RebateID_RebatePymts_Company_RebateID_PymtDate(Company:string, RebateID:string, PymtDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebatePymtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebatePymtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RebateHdrAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateHdrAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrAttchRow
   */  
export function get_Rebates_Company_RebateID_RebateHdrAttches(Company:string, RebateID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateHdrAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RebateHdrAttch item
   Description: Calls GetByID to retrieve the RebateHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateHdrAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   */  
export function get_Rebates_Company_RebateID_RebateHdrAttches_Company_RebateID_DrawingSeq(Company:string, RebateID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RebateCusts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateCusts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustRow
   */  
export function get_RebateCusts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateCusts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateCustRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RebateCustRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebateCusts(requestBody:Erp_Tablesets_RebateCustRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RebateCust item
   Description: Calls GetByID to retrieve the RebateCust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCust
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateCustRow
   */  
export function get_RebateCusts_Company_RebateID_CustNum(Company:string, RebateID:string, CustNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateCustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateCustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RebateCust for the service
   Description: Calls UpdateExt to update RebateCust. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateCust
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateCustRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RebateCusts_Company_RebateID_CustNum(Company:string, RebateID:string, CustNum:string, requestBody:Erp_Tablesets_RebateCustRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")", {
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
   Summary: Call UpdateExt to delete RebateCust item
   Description: Call UpdateExt to delete RebateCust item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateCust
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RebateCusts_Company_RebateID_CustNum(Company:string, RebateID:string, CustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")", {
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
   Description: Get RebateCustDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateCustDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustDtlRow
   */  
export function get_RebateCusts_Company_RebateID_CustNum_RebateCustDtls(Company:string, RebateID:string, CustNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")/RebateCustDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RebateCustDtl item
   Description: Calls GetByID to retrieve the RebateCustDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCustDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateCustDtlRow
   */  
export function get_RebateCusts_Company_RebateID_CustNum_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company:string, RebateID:string, CustNum:string, LineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateCustDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateCustDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RebateCustDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateCustDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustDtlRow
   */  
export function get_RebateCustDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateCustDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateCustDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RebateCustDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebateCustDtls(requestBody:Erp_Tablesets_RebateCustDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RebateCustDtl item
   Description: Calls GetByID to retrieve the RebateCustDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCustDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateCustDtlRow
   */  
export function get_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company:string, RebateID:string, LineNum:string, CustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateCustDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateCustDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RebateCustDtl for the service
   Description: Calls UpdateExt to update RebateCustDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateCustDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateCustDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company:string, RebateID:string, LineNum:string, CustNum:string, requestBody:Erp_Tablesets_RebateCustDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")", {
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
   Summary: Call UpdateExt to delete RebateCustDtl item
   Description: Call UpdateExt to delete RebateCustDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateCustDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company:string, RebateID:string, LineNum:string, CustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")", {
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
   Description: Get RebateDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateDtlRow
   */  
export function get_RebateDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RebateDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebateDtls(requestBody:Erp_Tablesets_RebateDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RebateDtl item
   Description: Calls GetByID to retrieve the RebateDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateDtlRow
   */  
export function get_RebateDtls_Company_RebateID_LineNum(Company:string, RebateID:string, LineNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RebateDtl for the service
   Description: Calls UpdateExt to update RebateDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RebateDtls_Company_RebateID_LineNum(Company:string, RebateID:string, LineNum:string, requestBody:Erp_Tablesets_RebateDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")", {
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
   Summary: Call UpdateExt to delete RebateDtl item
   Description: Call UpdateExt to delete RebateDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RebateDtls_Company_RebateID_LineNum(Company:string, RebateID:string, LineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")", {
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
   Description: Get RebateBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateBrks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateBrkRow
   */  
export function get_RebateDtls_Company_RebateID_LineNum_RebateBrks(Company:string, RebateID:string, LineNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")/RebateBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RebateBrk item
   Description: Calls GetByID to retrieve the RebateBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateBrk1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param BreakMin Desc: BreakMin   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateBrkRow
   */  
export function get_RebateDtls_Company_RebateID_LineNum_RebateBrks_Company_RebateID_LineNum_BreakMin(Company:string, RebateID:string, LineNum:string, BreakMin:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RebateBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateBrks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateBrkRow
   */  
export function get_RebateBrks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateBrks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RebateBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebateBrks(requestBody:Erp_Tablesets_RebateBrkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RebateBrk item
   Description: Calls GetByID to retrieve the RebateBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param BreakMin Desc: BreakMin   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateBrkRow
   */  
export function get_RebateBrks_Company_RebateID_LineNum_BreakMin(Company:string, RebateID:string, LineNum:string, BreakMin:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RebateBrk for the service
   Description: Calls UpdateExt to update RebateBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param BreakMin Desc: BreakMin   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RebateBrks_Company_RebateID_LineNum_BreakMin(Company:string, RebateID:string, LineNum:string, BreakMin:string, requestBody:Erp_Tablesets_RebateBrkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")", {
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
   Summary: Call UpdateExt to delete RebateBrk item
   Description: Call UpdateExt to delete RebateBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param BreakMin Desc: BreakMin   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RebateBrks_Company_RebateID_LineNum_BreakMin(Company:string, RebateID:string, LineNum:string, BreakMin:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")", {
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
   Description: Get RebatePymts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebatePymts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebatePymtRow
   */  
export function get_RebatePymts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebatePymtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebatePymtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebatePymts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebatePymtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RebatePymtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebatePymts(requestBody:Erp_Tablesets_RebatePymtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RebatePymt item
   Description: Calls GetByID to retrieve the RebatePymt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebatePymt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param PymtDate Desc: PymtDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebatePymtRow
   */  
export function get_RebatePymts_Company_RebateID_PymtDate(Company:string, RebateID:string, PymtDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebatePymtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebatePymtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RebatePymt for the service
   Description: Calls UpdateExt to update RebatePymt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebatePymt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param PymtDate Desc: PymtDate   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebatePymtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RebatePymts_Company_RebateID_PymtDate(Company:string, RebateID:string, PymtDate:string, requestBody:Erp_Tablesets_RebatePymtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")", {
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
   Summary: Call UpdateExt to delete RebatePymt item
   Description: Call UpdateExt to delete RebatePymt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebatePymt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param PymtDate Desc: PymtDate   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RebatePymts_Company_RebateID_PymtDate(Company:string, RebateID:string, PymtDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")", {
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
   Description: Get RebateHdrAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateHdrAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrAttchRow
   */  
export function get_RebateHdrAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateHdrAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RebateHdrAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebateHdrAttches(requestBody:Erp_Tablesets_RebateHdrAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RebateHdrAttch item
   Description: Calls GetByID to retrieve the RebateHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateHdrAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   */  
export function get_RebateHdrAttches_Company_RebateID_DrawingSeq(Company:string, RebateID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RebateHdrAttch for the service
   Description: Calls UpdateExt to update RebateHdrAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateHdrAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RebateHdrAttches_Company_RebateID_DrawingSeq(Company:string, RebateID:string, DrawingSeq:string, requestBody:Erp_Tablesets_RebateHdrAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete RebateHdrAttch item
   Description: Call UpdateExt to delete RebateHdrAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateHdrAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RebateHdrAttches_Company_RebateID_DrawingSeq(Company:string, RebateID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrListRow)
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
export function get_GetRows(whereClauseRebateHdr:string, whereClauseRebateHdrAttch:string, whereClauseRebateCust:string, whereClauseRebateCustDtl:string, whereClauseRebateDtl:string, whereClauseRebateBrk:string, whereClauseRebatePymt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRebateHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebateHdr=" + whereClauseRebateHdr
   }
   if(typeof whereClauseRebateHdrAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebateHdrAttch=" + whereClauseRebateHdrAttch
   }
   if(typeof whereClauseRebateCust!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebateCust=" + whereClauseRebateCust
   }
   if(typeof whereClauseRebateCustDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebateCustDtl=" + whereClauseRebateCustDtl
   }
   if(typeof whereClauseRebateDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebateDtl=" + whereClauseRebateDtl
   }
   if(typeof whereClauseRebateBrk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebateBrk=" + whereClauseRebateBrk
   }
   if(typeof whereClauseRebatePymt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebatePymt=" + whereClauseRebatePymt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(rebateID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rebateID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rebateID=" + rebateID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ChangeDetailPartNum
   Description: This method validates and populates the Part related fields when the
RebateDtl.PartNum changes
   OperationID: ChangeDetailPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailPartNum(requestBody:ChangeDetailPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDetailPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/ChangeDetailPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDetailPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeHdrCustID
   Description: This method validates and populates the Customer fields when the
ttRebateHdr.CustomerCustID changes
   OperationID: ChangeHdrCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeHdrCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrCustID(requestBody:ChangeHdrCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeHdrCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/ChangeHdrCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeHdrCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePymtDate
   Description: This method should run before changing the RebatePymt.PymtDate.
   OperationID: ChangePymtDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePymtDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePymtDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePymtDate(requestBody:ChangePymtDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePymtDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/ChangePymtDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePymtDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePymtDate
   Description: This method validates the proposed value of the PymtDate field.
   OperationID: OnChangePymtDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePymtDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePymtDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePymtDate(requestBody:OnChangePymtDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePymtDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/OnChangePymtDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePymtDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRCCustomer
   Description: This method validates and populates the Customer fields when the
RebateCust.CustID changes
   OperationID: ChangeRCCustomer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRCCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRCCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRCCustomer(requestBody:ChangeRCCustomer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRCCustomer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/ChangeRCCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRCCustomer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyRebate
   Description: This method copies one rebate to a new rebate.  The user can change either
the dates of the rebate or the customers for the rebate.
If changing the dates, then custNum and groupCode fields will be ignored
If date fields are null, then either custID or groupCode must be populated
   OperationID: CopyRebate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyRebate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyRebate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyRebate(requestBody:CopyRebate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyRebate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/CopyRebate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyRebate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustGroup
   Description: This method generates RebateCust records for the specified Rebate and Customer Group.
   OperationID: GetCustGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCustGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustGroup(requestBody:GetCustGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCustGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetCustGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCustGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRebateHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateHdr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRebateHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebateHdr(requestBody:GetNewRebateHdr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRebateHdr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetNewRebateHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRebateHdr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRebateHdrAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateHdrAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRebateHdrAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateHdrAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebateHdrAttch(requestBody:GetNewRebateHdrAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRebateHdrAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetNewRebateHdrAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRebateHdrAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRebateCust
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateCust
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRebateCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebateCust(requestBody:GetNewRebateCust_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRebateCust_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetNewRebateCust", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRebateCust_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRebateCustDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateCustDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRebateCustDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateCustDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebateCustDtl(requestBody:GetNewRebateCustDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRebateCustDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetNewRebateCustDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRebateCustDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRebateDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRebateDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebateDtl(requestBody:GetNewRebateDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRebateDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetNewRebateDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRebateDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRebateBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateBrk
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRebateBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebateBrk(requestBody:GetNewRebateBrk_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRebateBrk_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetNewRebateBrk", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRebateBrk_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRebatePymt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebatePymt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRebatePymt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebatePymt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebatePymt(requestBody:GetNewRebatePymt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRebatePymt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetNewRebatePymt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRebatePymt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateBrkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateBrkRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateCustDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateCustRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateHdrAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateHdrListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateHdrRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebatePymtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebatePymtRow,
}

export interface Erp_Tablesets_RebateBrkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Internal unique identifier for the RebateDtl table  */  
   "LineNum":number,
      /**  The miniumum quantity or amount needed to meet this level  */  
   "BreakMin":number,
      /**  The Rebate Percent that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   "RebatePercent":number,
      /**  The Rebate Amount that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   "RebateAmount":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RebateCustDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Internal unique identifier for the RebateDtl table  */  
   "LineNum":number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  Indicates if the customer is no longer participating in the Rebate  */  
   "Void":boolean,
      /**  Total amount of rebate paid to date  */  
   "PaidAmount":number,
      /**  Amount of rebate that has been earned  */  
   "AccruedAmount":number,
      /**  Total Invoice Quantity Accrued toward Rebate  */  
   "AccruedQty":number,
      /**  AccuredQty Unit of Measure  */  
   "UOMCode":string,
      /**  Total Invoice Amount accrued towards rebate  */  
   "AccruedTot":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AccruedAmount less PaidAmount  */  
   "BalanceAmount":number,
   "ProdCodeDesc":string,
   "BitFlag":number,
   "RebateDtlProdCode":string,
   "RebateDtlPartNum":string,
   "RebateDtlUOMCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RebateCustRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  Populated from the Customer's Terms code.  Discount to reduce invoice amount by before applying the rebate discount  */  
   "FixedDisc":number,
      /**  Indicates if the customer is no longer participating in the Rebate  */  
   "Void":boolean,
      /**  Total amount of rebate paid to date  */  
   "PaidAmount":number,
      /**  Amount of rebate that has been earned  */  
   "AccruedAmount":number,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   "RebateForm":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Amount remaining between Accrued amount and paid amount  */  
   "BalanceAmount":number,
   "GroupCode":string,
      /**  Rebate Supplier ID  */  
   "RebateSuppID":string,
      /**  Rebate Supplier Name  */  
   "VendorName":string,
   "BitFlag":number,
   "CustomerCustID":string,
   "CustomerName":string,
   "CustomerBTName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RebateDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Internal unique identifier for the RebateDtl table  */  
   "LineNum":number,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   "ProdCode":string,
      /**  Part/PartClass is no longer a part of the Rebate  */  
   "Void":boolean,
      /**  Total amount of rebate paid to date  */  
   "PaidAmount":number,
      /**  Amount of rebate that has been earned  */  
   "AccruedAmount":number,
      /**  Indicates whether the BreakMin for the levels is a quantity or Amount.  */  
   "BreakType":string,
      /**  Unit of Measure  */  
   "UOMCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Accrued Amount less Paid Amount  */  
   "BalanceAmount":number,
   "BitFlag":number,
   "PartPartDescription":string,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartPricePerCode":string,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "ProdGrupDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RebateHdrAttchRow{
   "Company":string,
   "RebateID":string,
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

export interface Erp_Tablesets_RebateHdrListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Rebate Description  */  
   "RebateDesc":string,
      /**  Starting Date of the Rebate  */  
   "StartDate":string,
      /**  End Date of the Rebate  */  
   "EndDate":string,
      /**  Number of days after the end date before a rebate check can be processed  */  
   "GraceDays":number,
      /**  Indicates if the Rebate is active or not  */  
   "Active":boolean,
      /**  Total amount of rebate paid to date  */  
   "PaidAmount":number,
      /**  Amount of rebate that has been earned  */  
   "AccruedAmount":number,
      /**  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  */  
   "CustNum":number,
      /**  Generate Rebate Transactions based on Invoices or Payments  */  
   "AccrualType":string,
      /**  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  */  
   "BillToFlag":boolean,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   "RebateForm":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Accrued Amount less Paid Amount  */  
   "BalanceAmount":number,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RebateHdrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Rebate Description  */  
   "RebateDesc":string,
      /**  Starting Date of the Rebate  */  
   "StartDate":string,
      /**  End Date of the Rebate  */  
   "EndDate":string,
      /**  Number of days after the end date before a rebate check can be processed  */  
   "GraceDays":number,
      /**  Indicates if the Rebate is active or not  */  
   "Active":boolean,
      /**  Total amount of rebate paid to date  */  
   "PaidAmount":number,
      /**  Amount of rebate that has been earned  */  
   "AccruedAmount":number,
      /**  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  */  
   "CustNum":number,
      /**  Generate Rebate Transactions based on Invoices or Payments  */  
   "AccrualType":string,
      /**  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  */  
   "BillToFlag":boolean,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   "RebateForm":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Accrued Amount less Paid Amount  */  
   "BalanceAmount":number,
   "BitFlag":number,
   "CustomerName":string,
   "CustomerBTName":string,
   "CustomerCustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RebatePymtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Date to generate the rebate on  */  
   "PymtDate":string,
      /**  Flag to indicate if the rebates have been generated  */  
   "Generated":boolean,
      /**  Indicates that the transactions for the rebate have been approved and the check/credit memo can be created  */  
   "Approved":boolean,
      /**  Indicates if the Rebate has been pulled into AR.  If yes, the next pull will ignore the group.  */  
   "Pulled":boolean,
      /**  Indicates if the Rebate has been pulled into AP.  If yes, the next pull will ignore the group.  */  
   "APPulled":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
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
      @param inPartNum
      @param ds
   */  
export interface ChangeDetailPartNum_input{
      /**  The proposed Part Num  */  
   inPartNum:string,
   ds:Erp_Tablesets_RebateTableset[],
}

export interface ChangeDetailPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param inCustID
      @param ds
   */  
export interface ChangeHdrCustID_input{
      /**  The proposed Customer ID  */  
   inCustID:string,
   ds:Erp_Tablesets_RebateTableset[],
}

export interface ChangeHdrCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ipProposedPymtDate
      @param ds
   */  
export interface ChangePymtDate_input{
      /**  The new proposed RebatePymt.PymtDate value  */  
   ipProposedPymtDate:string,
   ds:Erp_Tablesets_RebateTableset[],
}

export interface ChangePymtDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param inCustID
      @param ds
   */  
export interface ChangeRCCustomer_input{
      /**  The proposed Customer ID  */  
   inCustID:string,
   ds:Erp_Tablesets_RebateTableset[],
}

export interface ChangeRCCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param fromRebateID
      @param newRebateID
      @param newRebateDesc
      @param newDate
      @param newCustomer
      @param newSchedule
      @param startDate
      @param endDate
      @param custID
      @param groupCode
      @param pRebateForm
   */  
export interface CopyRebate_input{
      /**  RebateID to copy from  */  
   fromRebateID:string,
      /**  RebateID to create  */  
   newRebateID:string,
      /**  New description for rebate  */  
   newRebateDesc:string,
      /**  Flag to indicate if a new Date will be added  */  
   newDate:boolean,
      /**  Flag to indicate if Customers are going to be replaced  */  
   newCustomer:boolean,
      /**  Flag to indicate if Schedule will be copied or defaulted  */  
   newSchedule:boolean,
      /**  Rebate Start date  */  
   startDate:string,
      /**  Rebate End date  */  
   endDate:string,
      /**  Customer to be used for rebate  */  
   custID:string,
      /**  Customer Group Code to be used for rebate  */  
   groupCode:string,
      /**  Rebate Form when Rebate Supplier is empty  */  
   pRebateForm:string,
}

export interface CopyRebate_output{
   returnObj:Erp_Tablesets_RebateTableset[],
}

   /** Required : 
      @param rebateID
   */  
export interface DeleteByID_input{
   rebateID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_RebateBrkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Internal unique identifier for the RebateDtl table  */  
   LineNum:number,
      /**  The miniumum quantity or amount needed to meet this level  */  
   BreakMin:number,
      /**  The Rebate Percent that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   RebatePercent:number,
      /**  The Rebate Amount that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   RebateAmount:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateCustDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Internal unique identifier for the RebateDtl table  */  
   LineNum:number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  Indicates if the customer is no longer participating in the Rebate  */  
   Void:boolean,
      /**  Total amount of rebate paid to date  */  
   PaidAmount:number,
      /**  Amount of rebate that has been earned  */  
   AccruedAmount:number,
      /**  Total Invoice Quantity Accrued toward Rebate  */  
   AccruedQty:number,
      /**  AccuredQty Unit of Measure  */  
   UOMCode:string,
      /**  Total Invoice Amount accrued towards rebate  */  
   AccruedTot:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AccruedAmount less PaidAmount  */  
   BalanceAmount:number,
   ProdCodeDesc:string,
   BitFlag:number,
   RebateDtlProdCode:string,
   RebateDtlPartNum:string,
   RebateDtlUOMCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateCustRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  Populated from the Customer's Terms code.  Discount to reduce invoice amount by before applying the rebate discount  */  
   FixedDisc:number,
      /**  Indicates if the customer is no longer participating in the Rebate  */  
   Void:boolean,
      /**  Total amount of rebate paid to date  */  
   PaidAmount:number,
      /**  Amount of rebate that has been earned  */  
   AccruedAmount:number,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   RebateForm:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Amount remaining between Accrued amount and paid amount  */  
   BalanceAmount:number,
   GroupCode:string,
      /**  Rebate Supplier ID  */  
   RebateSuppID:string,
      /**  Rebate Supplier Name  */  
   VendorName:string,
   BitFlag:number,
   CustomerCustID:string,
   CustomerName:string,
   CustomerBTName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Internal unique identifier for the RebateDtl table  */  
   LineNum:number,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   ProdCode:string,
      /**  Part/PartClass is no longer a part of the Rebate  */  
   Void:boolean,
      /**  Total amount of rebate paid to date  */  
   PaidAmount:number,
      /**  Amount of rebate that has been earned  */  
   AccruedAmount:number,
      /**  Indicates whether the BreakMin for the levels is a quantity or Amount.  */  
   BreakType:string,
      /**  Unit of Measure  */  
   UOMCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Accrued Amount less Paid Amount  */  
   BalanceAmount:number,
   BitFlag:number,
   PartPartDescription:string,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   ProdGrupDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateHdrAttchRow{
   Company:string,
   RebateID:string,
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

export interface Erp_Tablesets_RebateHdrListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Rebate Description  */  
   RebateDesc:string,
      /**  Starting Date of the Rebate  */  
   StartDate:string,
      /**  End Date of the Rebate  */  
   EndDate:string,
      /**  Number of days after the end date before a rebate check can be processed  */  
   GraceDays:number,
      /**  Indicates if the Rebate is active or not  */  
   Active:boolean,
      /**  Total amount of rebate paid to date  */  
   PaidAmount:number,
      /**  Amount of rebate that has been earned  */  
   AccruedAmount:number,
      /**  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  */  
   CustNum:number,
      /**  Generate Rebate Transactions based on Invoices or Payments  */  
   AccrualType:string,
      /**  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  */  
   BillToFlag:boolean,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   RebateForm:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Accrued Amount less Paid Amount  */  
   BalanceAmount:number,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateHdrListTableset{
   RebateHdrList:Erp_Tablesets_RebateHdrListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RebateHdrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Rebate Description  */  
   RebateDesc:string,
      /**  Starting Date of the Rebate  */  
   StartDate:string,
      /**  End Date of the Rebate  */  
   EndDate:string,
      /**  Number of days after the end date before a rebate check can be processed  */  
   GraceDays:number,
      /**  Indicates if the Rebate is active or not  */  
   Active:boolean,
      /**  Total amount of rebate paid to date  */  
   PaidAmount:number,
      /**  Amount of rebate that has been earned  */  
   AccruedAmount:number,
      /**  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  */  
   CustNum:number,
      /**  Generate Rebate Transactions based on Invoices or Payments  */  
   AccrualType:string,
      /**  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  */  
   BillToFlag:boolean,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   RebateForm:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Accrued Amount less Paid Amount  */  
   BalanceAmount:number,
   BitFlag:number,
   CustomerName:string,
   CustomerBTName:string,
   CustomerCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebatePymtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Date to generate the rebate on  */  
   PymtDate:string,
      /**  Flag to indicate if the rebates have been generated  */  
   Generated:boolean,
      /**  Indicates that the transactions for the rebate have been approved and the check/credit memo can be created  */  
   Approved:boolean,
      /**  Indicates if the Rebate has been pulled into AR.  If yes, the next pull will ignore the group.  */  
   Pulled:boolean,
      /**  Indicates if the Rebate has been pulled into AP.  If yes, the next pull will ignore the group.  */  
   APPulled:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateTableset{
   RebateHdr:Erp_Tablesets_RebateHdrRow[],
   RebateHdrAttch:Erp_Tablesets_RebateHdrAttchRow[],
   RebateCust:Erp_Tablesets_RebateCustRow[],
   RebateCustDtl:Erp_Tablesets_RebateCustDtlRow[],
   RebateDtl:Erp_Tablesets_RebateDtlRow[],
   RebateBrk:Erp_Tablesets_RebateBrkRow[],
   RebatePymt:Erp_Tablesets_RebatePymtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRebateTableset{
   RebateHdr:Erp_Tablesets_RebateHdrRow[],
   RebateHdrAttch:Erp_Tablesets_RebateHdrAttchRow[],
   RebateCust:Erp_Tablesets_RebateCustRow[],
   RebateCustDtl:Erp_Tablesets_RebateCustDtlRow[],
   RebateDtl:Erp_Tablesets_RebateDtlRow[],
   RebateBrk:Erp_Tablesets_RebateBrkRow[],
   RebatePymt:Erp_Tablesets_RebatePymtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param rebateID
   */  
export interface GetByID_input{
   rebateID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RebateTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RebateTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RebateTableset[],
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
      @param rebateID
      @param groupCode
      @param pRebateForm
   */  
export interface GetCustGroup_input{
      /**  Rebate ID  */  
   rebateID:string,
      /**  Customer Group Code  */  
   groupCode:string,
      /**  Rebate Form when Rebate Supplier is empty  */  
   pRebateForm:string,
}

export interface GetCustGroup_output{
   returnObj:Erp_Tablesets_RebateTableset[],
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
   returnObj:Erp_Tablesets_RebateHdrListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rebateID
      @param lineNum
   */  
export interface GetNewRebateBrk_input{
   ds:Erp_Tablesets_RebateTableset[],
   rebateID:string,
   lineNum:number,
}

export interface GetNewRebateBrk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ds
      @param rebateID
      @param lineNum
   */  
export interface GetNewRebateCustDtl_input{
   ds:Erp_Tablesets_RebateTableset[],
   rebateID:string,
   lineNum:number,
}

export interface GetNewRebateCustDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ds
      @param rebateID
   */  
export interface GetNewRebateCust_input{
   ds:Erp_Tablesets_RebateTableset[],
   rebateID:string,
}

export interface GetNewRebateCust_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ds
      @param rebateID
   */  
export interface GetNewRebateDtl_input{
   ds:Erp_Tablesets_RebateTableset[],
   rebateID:string,
}

export interface GetNewRebateDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ds
      @param rebateID
   */  
export interface GetNewRebateHdrAttch_input{
   ds:Erp_Tablesets_RebateTableset[],
   rebateID:string,
}

export interface GetNewRebateHdrAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRebateHdr_input{
   ds:Erp_Tablesets_RebateTableset[],
}

export interface GetNewRebateHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ds
      @param rebateID
   */  
export interface GetNewRebatePymt_input{
   ds:Erp_Tablesets_RebateTableset[],
   rebateID:string,
}

export interface GetNewRebatePymt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param whereClauseRebateHdr
      @param whereClauseRebateHdrAttch
      @param whereClauseRebateCust
      @param whereClauseRebateCustDtl
      @param whereClauseRebateDtl
      @param whereClauseRebateBrk
      @param whereClauseRebatePymt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRebateHdr:string,
   whereClauseRebateHdrAttch:string,
   whereClauseRebateCust:string,
   whereClauseRebateCustDtl:string,
   whereClauseRebateDtl:string,
   whereClauseRebateBrk:string,
   whereClauseRebatePymt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RebateTableset[],
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
      @param ipProposedPymtDate
      @param ds
   */  
export interface OnChangePymtDate_input{
      /**  The new proposed RebatePymt.PymtDate value  */  
   ipProposedPymtDate:string,
   ds:Erp_Tablesets_RebateTableset[],
}

export interface OnChangePymtDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtRebateTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRebateTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RebateTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTableset,
}
}

