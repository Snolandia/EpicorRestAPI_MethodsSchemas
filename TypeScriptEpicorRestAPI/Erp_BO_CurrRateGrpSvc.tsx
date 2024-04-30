import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CurrRateGrpSvc
// Description: Currency Rates Group Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get CurrRateGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateGrps
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpRow
   */  
export function get_CurrRateGrps(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateGrps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CurrRateGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrRateGrps(requestBody:Erp_Tablesets_CurrRateGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CurrRateGrp item
   Description: Calls GetByID to retrieve the CurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrRateGrpRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode(Company:string, RateGrpCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CurrRateGrp for the service
   Description: Calls UpdateExt to update CurrRateGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CurrRateGrps_Company_RateGrpCode(Company:string, RateGrpCode:string, requestBody:Erp_Tablesets_CurrRateGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", {
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
   Summary: Call UpdateExt to delete CurrRateGrp item
   Description: Call UpdateExt to delete CurrRateGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CurrRateGrps_Company_RateGrpCode(Company:string, RateGrpCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", {
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
   Description: Get CurrConvRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrConvRules1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrConvRuleRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode_CurrConvRules(Company:string, RateGrpCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrConvRules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CurrConvRule item
   Description: Calls GetByID to retrieve the CurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrConvRule1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param SourceCurrCode Desc: SourceCurrCode   Required: True   Allow empty value : True
      @param TargetCurrCode Desc: TargetCurrCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrConvRuleRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company:string, RateGrpCode:string, SourceCurrCode:string, TargetCurrCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CurrRateDisps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrRateDisps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateDispRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode_CurrRateDisps(Company:string, RateGrpCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateDisps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CurrRateDisp item
   Description: Calls GetByID to retrieve the CurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateDisp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrRateDispRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode_CurrRateDisps_Company_RateGrpCode_Seq(Company:string, RateGrpCode:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CurrRateGrpAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrRateGrpAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpAttchRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode_CurrRateGrpAttches(Company:string, RateGrpCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateGrpAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CurrRateGrpAttch item
   Description: Calls GetByID to retrieve the CurrRateGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrpAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company:string, RateGrpCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrRateGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrRateGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CurrConvRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrConvRules
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrConvRuleRow
   */  
export function get_CurrConvRules(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrConvRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrConvRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CurrConvRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrConvRules(requestBody:Erp_Tablesets_CurrConvRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CurrConvRule item
   Description: Calls GetByID to retrieve the CurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrConvRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param SourceCurrCode Desc: SourceCurrCode   Required: True   Allow empty value : True
      @param TargetCurrCode Desc: TargetCurrCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrConvRuleRow
   */  
export function get_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company:string, RateGrpCode:string, SourceCurrCode:string, TargetCurrCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CurrConvRule for the service
   Description: Calls UpdateExt to update CurrConvRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrConvRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param SourceCurrCode Desc: SourceCurrCode   Required: True   Allow empty value : True
      @param TargetCurrCode Desc: TargetCurrCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrConvRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company:string, RateGrpCode:string, SourceCurrCode:string, TargetCurrCode:string, requestBody:Erp_Tablesets_CurrConvRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")", {
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
   Summary: Call UpdateExt to delete CurrConvRule item
   Description: Call UpdateExt to delete CurrConvRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrConvRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param SourceCurrCode Desc: SourceCurrCode   Required: True   Allow empty value : True
      @param TargetCurrCode Desc: TargetCurrCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company:string, RateGrpCode:string, SourceCurrCode:string, TargetCurrCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")", {
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
   Description: Get CurrRateDisps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateDisps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateDispRow
   */  
export function get_CurrRateDisps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateDisps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateDispRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CurrRateDispRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrRateDisps(requestBody:Erp_Tablesets_CurrRateDispRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CurrRateDisp item
   Description: Calls GetByID to retrieve the CurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateDisp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrRateDispRow
   */  
export function get_CurrRateDisps_Company_RateGrpCode_Seq(Company:string, RateGrpCode:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CurrRateDisp for the service
   Description: Calls UpdateExt to update CurrRateDisp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateDisp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateDispRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CurrRateDisps_Company_RateGrpCode_Seq(Company:string, RateGrpCode:string, Seq:string, requestBody:Erp_Tablesets_CurrRateDispRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete CurrRateDisp item
   Description: Call UpdateExt to delete CurrRateDisp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateDisp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CurrRateDisps_Company_RateGrpCode_Seq(Company:string, RateGrpCode:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")", {
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
   Description: Get CurrRateGrpAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateGrpAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpAttchRow
   */  
export function get_CurrRateGrpAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateGrpAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrRateGrpAttches(requestBody:Erp_Tablesets_CurrRateGrpAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CurrRateGrpAttch item
   Description: Calls GetByID to retrieve the CurrRateGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   */  
export function get_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company:string, RateGrpCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrRateGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrRateGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CurrRateGrpAttch for the service
   Description: Calls UpdateExt to update CurrRateGrpAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company:string, RateGrpCode:string, DrawingSeq:string, requestBody:Erp_Tablesets_CurrRateGrpAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CurrRateGrpAttch item
   Description: Call UpdateExt to delete CurrRateGrpAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company:string, RateGrpCode:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCurrRateGrp:string, whereClauseCurrRateGrpAttch:string, whereClauseCurrConvRule:string, whereClauseCurrRateDisp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCurrRateGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrRateGrp=" + whereClauseCurrRateGrp
   }
   if(typeof whereClauseCurrRateGrpAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrRateGrpAttch=" + whereClauseCurrRateGrpAttch
   }
   if(typeof whereClauseCurrConvRule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrConvRule=" + whereClauseCurrConvRule
   }
   if(typeof whereClauseCurrRateDisp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrRateDisp=" + whereClauseCurrRateDisp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(rateGrpCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rateGrpCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rateGrpCode=" + rateGrpCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method DefaultFieldsCurrConvRule
   OperationID: DefaultFieldsCurrConvRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultFieldsCurrConvRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultFieldsCurrConvRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultFieldsCurrConvRule(requestBody:DefaultFieldsCurrConvRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultFieldsCurrConvRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/DefaultFieldsCurrConvRule", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultFieldsCurrConvRule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultFieldsCurrGrp
   OperationID: DefaultFieldsCurrGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultFieldsCurrGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultFieldsCurrGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultFieldsCurrGrp(requestBody:DefaultFieldsCurrGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultFieldsCurrGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/DefaultFieldsCurrGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultFieldsCurrGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrRateGrpForLink
   Description: This returns the CurrRateGrp dataset for linking.
   OperationID: GetCurrRateGrpForLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCurrRateGrpForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrRateGrpForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrRateGrpForLink(requestBody:GetCurrRateGrpForLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrRateGrpForLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetCurrRateGrpForLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCurrRateGrpForLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGlbCurrRateGrpList
   Description: This method returns the GlbCurrRateGrp dataset based on a delimited list of
GlbRateGrpCode values passed in.
   OperationID: GetGlbCurrRateGrpList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGlbCurrRateGrpList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCurrRateGrpList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlbCurrRateGrpList(requestBody:GetGlbCurrRateGrpList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGlbCurrRateGrpList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetGlbCurrRateGrpList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetGlbCurrRateGrpList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkSelected
   OperationID: LinkSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkSelected(requestBody:LinkSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/LinkSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LinkSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildGlbCurrRateGrpList
   OperationID: BuildGlbCurrRateGrpList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildGlbCurrRateGrpList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildGlbCurrRateGrpList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildGlbCurrRateGrpList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/BuildGlbCurrRateGrpList", {
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
         resolve(data as BuildGlbCurrRateGrpList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GlbCurrRateGrpsExist
   Description: This method checks if GlbCurrRateGrp records exist or not.  Can be used
to determine if the option to link/unlink customers is available.
   OperationID: GlbCurrRateGrpsExist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlbCurrRateGrpsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCurrRateGrpsExist(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GlbCurrRateGrpsExist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GlbCurrRateGrpsExist", {
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
         resolve(data as GlbCurrRateGrpsExist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CurrExRateExist
   Description: This method checks if CurrExRate records exist or not.
   OperationID: CurrExRateExist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CurrExRateExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CurrExRateExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrExRateExist(requestBody:CurrExRateExist_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CurrExRateExist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrExRateExist", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CurrExRateExist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbCurrRateGrp
   Description: This method performs the actual logic behind linking a Currency Rate Group.  It is run after
the PreLinkGlbCurrRateGrp method which determines the Currency Rate Group Code to link to.
If the Currency Rate Group Code is for a Rate Group that already exists, the GlbCurrRateGrp information is
translated and then copied to the CurrRateGrpDataSet as an update.
If the Rate Group Code is for a new Rate Group, the GlbCurrRateGrp information is translated and then
copied to the CurrRateGrpDataSet as an Add.  Until the update method is run on CurrRateGrp record
the Link process is not completed.
   OperationID: LinkGlbCurrRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbCurrRateGrp(requestBody:LinkGlbCurrRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkGlbCurrRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/LinkGlbCurrRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LinkGlbCurrRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreLinkGlbCurrRateGrp
   Description: Linking a GlbCurrRateGrp record ties a global record to a new or existing CurrRateGrp record so
that any changes made to the GlbCurrRateGrp record in another company are automatically copied
to any linked Rate Groups.
This method performs the pre link logic to check of okay to link or get the new RateGrpCode
to create/link to.  Will be run before LinkGlbCurrRateGrp which actually creates/updates a
CurrRateGrp record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkRateGrpCode will be defaulted to the GlbRateGrpCode field.  It will then
check to see if this RateGrpCode is available for Use.  If available for use the system will return a
question asking the user if they want to use this code.  If the answer is no, then the user
either needs to select an existing rate group's code to link to or enter a brand new ID.  You will
run this method until the user answer is yes.  Then the LinkGlbCurrRateGrp method is called.
   OperationID: PreLinkGlbCurrRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreLinkGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreLinkGlbCurrRateGrp(requestBody:PreLinkGlbCurrRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreLinkGlbCurrRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/PreLinkGlbCurrRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreLinkGlbCurrRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipGlbCurrRateGrp
   Description: This method performs the logic behind the skip option for GlbCurrRateGrp
Skip - sets the Skipped flag to true.
If the CurrRateGrpCode field is not blank will error out
   OperationID: SkipGlbCurrRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipGlbCurrRateGrp(requestBody:SkipGlbCurrRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipGlbCurrRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/SkipGlbCurrRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkipGlbCurrRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlinkGlbCurrRateGrp
   Description: This method performs the logic behind the unlink option for GlbCurrRateGrp
Unlink - clears the RateGrpCode field in GlbCurrRateGrp.  Returns the CurrRateGrp DataSet
   OperationID: UnlinkGlbCurrRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlinkGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlinkGlbCurrRateGrp(requestBody:UnlinkGlbCurrRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlinkGlbCurrRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/UnlinkGlbCurrRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnlinkGlbCurrRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateAltCrossCurrCode
   Description: This method validates AltCrossCurrCode.
If exist at least one record on CurrConvRule with Rulecode value equal to  5 or 6
AltCrossCurrCode cannot be changed if exist at least one record on CurrConvRule with Rulecode value equal to 5 or 6
   OperationID: ValidateAltCrossCurrCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateAltCrossCurrCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAltCrossCurrCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAltCrossCurrCode(requestBody:ValidateAltCrossCurrCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateAltCrossCurrCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateAltCrossCurrCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateAltCrossCurrCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBaseRateGrp
   Description: This method validates that:
(1) BaseRate must be a valid, active CurrRateGrp
(2) If this CurrRateGrp is used as a BaseRateGrp on any other CurrRateGrp then it's own BaseRateGrp cannot be populate.
(3) If choosing a BaseRateGrp, cannot choose a CurrRateGrp that has a BaseRateGrp defined.
(4) If any Conversion Rule (currConvRule) have their UseBaseRate set to true, cannot clear BaseRateGrp field.
   OperationID: ValidateBaseRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateBaseRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBaseRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBaseRateGrp(requestBody:ValidateBaseRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateBaseRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateBaseRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateBaseRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCrossCurrCode
   Description: This method validates if exist at least one record on CurrConvRule with Rulecode value equal to 3, 4, 5 or 6
CrossCurrCode cannot be changed if exist at least one record on CurrConvRule with Rulecode value equal to 3, 4, 5 or 6
   OperationID: ValidateCrossCurrCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCrossCurrCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCrossCurrCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCrossCurrCode(requestBody:ValidateCrossCurrCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCrossCurrCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateCrossCurrCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateCrossCurrCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCurrencies
   Description: Validate that when changing the cross rate currencies on a RateGrp
if BaseRateGrp is defined must validate against the BaseRateGrp's currencies
if it is used as a BaseRateGrp on other RateGrps (could be more than one) must validate against the RateGrps' currencies
   OperationID: ValidateCurrencies
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCurrencies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCurrencies(requestBody:ValidateCurrencies_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCurrencies_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateCurrencies", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateCurrencies_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateInactive
   Description: This method validate , that  CurrRateGrp.Inactive cannot be marked as true
if the rate group is assigned to a Company Default.
   OperationID: ValidateInactive
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateInactive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInactive(requestBody:ValidateInactive_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateInactive_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateInactive", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateInactive_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRateGrpCode
   Description: This method validate , that  RateGrpCode is unique
   OperationID: ValidateRateGrpCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRateGrpCode(requestBody:ValidateRateGrpCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRateGrpCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateRateGrpCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateRateGrpCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRateGrpDescription
   Description: This method validate , that  Description is unique
   OperationID: ValidateRateGrpDescription
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRateGrpDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateGrpDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRateGrpDescription(requestBody:ValidateRateGrpDescription_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRateGrpDescription_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateRateGrpDescription", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateRateGrpDescription_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRateNumDec
   Description: This method validate , that  RateNumDec not exceed 6 decimal places
   OperationID: ValidateRateNumDec
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRateNumDec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateNumDec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRateNumDec(requestBody:ValidateRateNumDec_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRateNumDec_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateRateNumDec", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateRateNumDec_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRuleCode
   OperationID: ValidateRuleCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRuleCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRuleCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRuleCode(requestBody:ValidateRuleCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRuleCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateRuleCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateRuleCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateUseBaseRate
   OperationID: ValidateUseBaseRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateUseBaseRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUseBaseRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUseBaseRate(requestBody:ValidateUseBaseRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateUseBaseRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/ValidateUseBaseRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateUseBaseRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method validateExCurrStatusForRateType
   Description: This method validates the current status for the Rate Group that will be linked to a global Rate Type
   OperationID: validateExCurrStatusForRateType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/validateExCurrStatusForRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateExCurrStatusForRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_validateExCurrStatusForRateType(requestBody:validateExCurrStatusForRateType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<validateExCurrStatusForRateType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/validateExCurrStatusForRateType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as validateExCurrStatusForRateType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCurrRateGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrRateGrp(requestBody:GetNewCurrRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCurrRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetNewCurrRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCurrRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCurrRateGrpAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateGrpAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateGrpAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateGrpAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrRateGrpAttch(requestBody:GetNewCurrRateGrpAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCurrRateGrpAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetNewCurrRateGrpAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCurrRateGrpAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCurrConvRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrConvRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCurrConvRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrConvRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrConvRule(requestBody:GetNewCurrConvRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCurrConvRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetNewCurrConvRule", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCurrConvRule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCurrRateDisp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateDisp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrRateDisp(requestBody:GetNewCurrRateDisp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCurrRateDisp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetNewCurrRateDisp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCurrRateDisp_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrConvRuleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrConvRuleRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateDispRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrRateDispRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrRateGrpAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrRateGrpListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrRateGrpRow,
}

export interface Erp_Tablesets_CurrConvRuleRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the source currency.  */  
   "SourceCurrCode":string,
      /**  A unique code that identifies the target currency.  */  
   "TargetCurrCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Determine if the user should use the base rate group defined in CurrRateGrp  */  
   "UseBaseRate":boolean,
      /**  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  */  
   "RuleCode":number,
      /**  Indiates if the exchange rate is fixed and cannot be updated  */  
   "FixedRate":boolean,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   "DisplayMode":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This field is used as display on the Three Node. Is compose by the source and target code separated by an hyphen (-) . i.e. XXXX-XXX  */  
   "SourceTargetCode":string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Souce Currency ID with Scale Factor  */  
   "SouceCurrDspID":string,
      /**  Target Currency ID wiht Scale Factor  */  
   "TargetCurrDspID":string,
   "DisplayModeText":string,
   "RuleCodeText":string,
   "BitFlag":number,
   "SourceCurrCurrName":string,
   "SourceCurrCurrDesc":string,
   "SourceCurrDocumentDesc":string,
   "SourceCurrCurrSymbol":string,
   "SourceCurrCurrencyID":string,
   "TargetCurrCurrDesc":string,
   "TargetCurrDocumentDesc":string,
   "TargetCurrCurrName":string,
   "TargetCurrCurrencyID":string,
   "TargetCurrCurrSymbol":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CurrRateDispRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Order in which the currencies should be displayed in the matrix grids  */  
   "Seq":number,
      /**  Currency code to be displayed  */  
   "CurrencyCode":string,
      /**  Display factor for exchange rates  */  
   "ScaleFactor":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   "GlbFlag":boolean,
   "BitFlag":number,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CurrRateGrpAttchRow{
   "Company":string,
   "RateGrpCode":string,
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

export interface Erp_Tablesets_CurrRateGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Description  */  
   "Description":string,
      /**  Determines if the record is inactive  */  
   "Inactive":boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   "BaseRateGrpCode":string,
      /**  Currency to use during single or double currency conversions  */  
   "CrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "CrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "CrossRoundDec":number,
      /**  Currency used for double currency conversions  */  
   "AltCrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "AltCrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "AltCrossRoundDec":number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   "GlobalGrp":boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Number of decimals for the exchange rates  */  
   "RateNumDec":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  control when the GlobalGrp field should be enabled.  */  
   "EnableGlobalGrp":boolean,
      /**  Control when the GlobalLock field should be enabled.  */  
   "EnableGlobalLock":boolean,
      /**  Indicates if the Currency is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  */  
   "GlbLink":string,
      /**  Description of the currency  */  
   "AltCrossCurrCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "AltCrossCurrCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "AltCrossCurrCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "AltCrossCurrDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "AltCrossCurrCurrName":string,
      /**  Description  */  
   "BaseRateGrpDescDescription":string,
      /**  Description of the currency  */  
   "CrossCurrCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CrossCurrCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CrossCurrCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CrossCurrDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CrossCurrCurrName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CurrRateGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Description  */  
   "Description":string,
      /**  Determines if the record is inactive  */  
   "Inactive":boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   "BaseRateGrpCode":string,
      /**  Currency to use during single or double currency conversions  */  
   "CrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "CrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "CrossRoundDec":number,
      /**  Currency used for double currency conversions  */  
   "AltCrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "AltCrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "AltCrossRoundDec":number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   "GlobalGrp":boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Number of decimals for the exchange rates  */  
   "RateNumDec":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  control when the GlobalGrp field should be enabled.  */  
   "EnableGlobalGrp":boolean,
      /**  Control when the GlobalLock field should be enabled.  */  
   "EnableGlobalLock":boolean,
      /**  Indicates if the Currency is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  */  
   "GlbLink":string,
      /**  Company Name from linked global rate group.  */  
   "GlbCompanyName":string,
      /**  Rate group Code from linked global rate group.  */  
   "GlbRateGrpCode":string,
      /**  Description from linked global rate group.  */  
   "GlbRateGrpDesc":string,
      /**  Company ID from linked global rate group.  */  
   "GlbCompanyID":string,
   "BitFlag":number,
   "AltCrossCurrCurrName":string,
   "AltCrossCurrCurrDesc":string,
   "AltCrossCurrCurrencyID":string,
   "AltCrossCurrDocumentDesc":string,
   "AltCrossCurrCurrSymbol":string,
   "BaseRateGrpDescDescription":string,
   "CrossCurrCurrDesc":string,
   "CrossCurrCurrName":string,
   "CrossCurrCurrencyID":string,
   "CrossCurrDocumentDesc":string,
   "CrossCurrCurrSymbol":string,
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
export interface BuildGlbCurrRateGrpList_output{
   returnObj:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

   /** Required : 
      @param pRateGrpCode
   */  
export interface CurrExRateExist_input{
      /**  Rate Group code.  */  
   pRateGrpCode:string,
}

export interface CurrExRateExist_output{
parameters : {
      /**  output parameters  */  
   pCurrExRateExist:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultFieldsCurrConvRule_input{
   ds:Erp_Tablesets_CurrRateGrpTableset[],
}

export interface DefaultFieldsCurrConvRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultFieldsCurrGrp_input{
   ds:Erp_Tablesets_CurrRateGrpTableset[],
}

export interface DefaultFieldsCurrGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param rateGrpCode
   */  
export interface DeleteByID_input{
   rateGrpCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CurrConvRuleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the source currency.  */  
   SourceCurrCode:string,
      /**  A unique code that identifies the target currency.  */  
   TargetCurrCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Determine if the user should use the base rate group defined in CurrRateGrp  */  
   UseBaseRate:boolean,
      /**  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  */  
   RuleCode:number,
      /**  Indiates if the exchange rate is fixed and cannot be updated  */  
   FixedRate:boolean,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   DisplayMode:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This field is used as display on the Three Node. Is compose by the source and target code separated by an hyphen (-) . i.e. XXXX-XXX  */  
   SourceTargetCode:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Souce Currency ID with Scale Factor  */  
   SouceCurrDspID:string,
      /**  Target Currency ID wiht Scale Factor  */  
   TargetCurrDspID:string,
   DisplayModeText:string,
   RuleCodeText:string,
   BitFlag:number,
   SourceCurrCurrName:string,
   SourceCurrCurrDesc:string,
   SourceCurrDocumentDesc:string,
   SourceCurrCurrSymbol:string,
   SourceCurrCurrencyID:string,
   TargetCurrCurrDesc:string,
   TargetCurrDocumentDesc:string,
   TargetCurrCurrName:string,
   TargetCurrCurrencyID:string,
   TargetCurrCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrRateDispRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Order in which the currencies should be displayed in the matrix grids  */  
   Seq:number,
      /**  Currency code to be displayed  */  
   CurrencyCode:string,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   BitFlag:number,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrRateGrpAttchRow{
   Company:string,
   RateGrpCode:string,
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

export interface Erp_Tablesets_CurrRateGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Description  */  
   Description:string,
      /**  Determines if the record is inactive  */  
   Inactive:boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   BaseRateGrpCode:string,
      /**  Currency to use during single or double currency conversions  */  
   CrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   CrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   CrossRoundDec:number,
      /**  Currency used for double currency conversions  */  
   AltCrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   AltCrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   AltCrossRoundDec:number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   GlobalGrp:boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Number of decimals for the exchange rates  */  
   RateNumDec:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  control when the GlobalGrp field should be enabled.  */  
   EnableGlobalGrp:boolean,
      /**  Control when the GlobalLock field should be enabled.  */  
   EnableGlobalLock:boolean,
      /**  Indicates if the Currency is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  */  
   GlbLink:string,
      /**  Description of the currency  */  
   AltCrossCurrCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   AltCrossCurrCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   AltCrossCurrCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   AltCrossCurrDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   AltCrossCurrCurrName:string,
      /**  Description  */  
   BaseRateGrpDescDescription:string,
      /**  Description of the currency  */  
   CrossCurrCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CrossCurrCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CrossCurrCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CrossCurrDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CrossCurrCurrName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrRateGrpListTableset{
   CurrRateGrpList:Erp_Tablesets_CurrRateGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CurrRateGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Description  */  
   Description:string,
      /**  Determines if the record is inactive  */  
   Inactive:boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   BaseRateGrpCode:string,
      /**  Currency to use during single or double currency conversions  */  
   CrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   CrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   CrossRoundDec:number,
      /**  Currency used for double currency conversions  */  
   AltCrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   AltCrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   AltCrossRoundDec:number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   GlobalGrp:boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Number of decimals for the exchange rates  */  
   RateNumDec:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  control when the GlobalGrp field should be enabled.  */  
   EnableGlobalGrp:boolean,
      /**  Control when the GlobalLock field should be enabled.  */  
   EnableGlobalLock:boolean,
      /**  Indicates if the Currency is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  */  
   GlbLink:string,
      /**  Company Name from linked global rate group.  */  
   GlbCompanyName:string,
      /**  Rate group Code from linked global rate group.  */  
   GlbRateGrpCode:string,
      /**  Description from linked global rate group.  */  
   GlbRateGrpDesc:string,
      /**  Company ID from linked global rate group.  */  
   GlbCompanyID:string,
   BitFlag:number,
   AltCrossCurrCurrName:string,
   AltCrossCurrCurrDesc:string,
   AltCrossCurrCurrencyID:string,
   AltCrossCurrDocumentDesc:string,
   AltCrossCurrCurrSymbol:string,
   BaseRateGrpDescDescription:string,
   CrossCurrCurrDesc:string,
   CrossCurrCurrName:string,
   CrossCurrCurrencyID:string,
   CrossCurrDocumentDesc:string,
   CrossCurrCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrRateGrpTableset{
   CurrRateGrp:Erp_Tablesets_CurrRateGrpRow[],
   CurrRateGrpAttch:Erp_Tablesets_CurrRateGrpAttchRow[],
   CurrConvRule:Erp_Tablesets_CurrConvRuleRow[],
   CurrRateDisp:Erp_Tablesets_CurrRateDispRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbCurrConvRuleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the source currency.  */  
   SourceCurrCode:string,
      /**  A unique code that identifies the target currency.  */  
   TargetCurrCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Determine if the user should use the base rate group defined in CurrRateGrp  */  
   UseBaseRate:boolean,
      /**  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  */  
   RuleCode:number,
      /**  Indiates if the exchange rate is fixed and cannot be updated  */  
   FixedRate:boolean,
      /**  Currency Rate Group Code from Source Company  */  
   GlbRateGrpCode:string,
      /**  Source Currency from Source Company  */  
   GlbSourceCurrCode:string,
      /**  Target Currency from Source Company  */  
   GlbTargetCurrCode:string,
      /**  Source Company  */  
   GlbCompany:string,
   DisplayMode:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrExRateRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the source currency.  */  
   SourceCurrCode:string,
      /**  This rate is effective as of this date.  */  
   EffectiveDate:string,
      /**   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   CurrentRate:number,
      /**  System date at time that record was modified.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was modified.  */  
   SysTime:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   Reference:string,
      /**  A unique code that identifies the target currency.  */  
   TargetCurrCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Currency Rate Group Code from Source Company  */  
   GlbRateGrpCode:string,
      /**  Source Currency from Source Company  */  
   GlbSourceCurrCode:string,
      /**  Target Currency from Source Company  */  
   GlbTargetCurrCode:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Effective Date from Source Company  */  
   GlbEffectiveDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrRateDispRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Order in which the currencies should be displayed in the matrix grids  */  
   Seq:number,
      /**  Currency code to be displayed  */  
   CurrencyCode:string,
      /**  Currency Rate Group Code from source company  */  
   GlbRateGrpCode:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Sequence from Source Company  */  
   GlbSeq:number,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrRateGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Currency Rate Group Code from source company  */  
   GlbRateGrpCode:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   Skipped:boolean,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Description  */  
   Description:string,
      /**  Determines if the record is inactive  */  
   Inactive:boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   BaseRateGrpCode:string,
      /**  Currency to use during single or double currency conversions  */  
   CrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   CrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   CrossRoundDec:number,
      /**  Currency used for double currency conversions  */  
   AltCrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   AltCrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   AltCrossRoundDec:number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   GlobalGrp:boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   DisplayMode:number,
   RateNumDec:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CurrRateGrp.RateGrpCode to link to (new or existing)  */  
   LinkRateGrpCode:string,
      /**  holds description of currency rate group from local rate group linked.  */  
   LocalDesc:string,
   Select:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrRateGrpTableset{
   GlbCurrRateGrp:Erp_Tablesets_GlbCurrRateGrpRow[],
   GlbCurrConvRule:Erp_Tablesets_GlbCurrConvRuleRow[],
   GlbCurrExRate:Erp_Tablesets_GlbCurrExRateRow[],
   GlbCurrRateDisp:Erp_Tablesets_GlbCurrRateDispRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCurrRateGrpTableset{
   CurrRateGrp:Erp_Tablesets_CurrRateGrpRow[],
   CurrRateGrpAttch:Erp_Tablesets_CurrRateGrpAttchRow[],
   CurrConvRule:Erp_Tablesets_CurrConvRuleRow[],
   CurrRateDisp:Erp_Tablesets_CurrRateDispRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param rateGrpCode
   */  
export interface GetByID_input{
   rateGrpCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CurrRateGrpTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CurrRateGrpTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CurrRateGrpTableset[],
}

   /** Required : 
      @param currRateGrpCode
   */  
export interface GetCurrRateGrpForLink_input{
      /**  Global Rate Group Code GLBCurrRateGrp record to link  */  
   currRateGrpCode:string,
}

export interface GetCurrRateGrpForLink_output{
   returnObj:Erp_Tablesets_CurrRateGrpTableset[],
}

   /** Required : 
      @param glbRateGrpCodeList
   */  
export interface GetGlbCurrRateGrpList_input{
      /**  Delimited list of glbRateGrpCode values  */  
   glbRateGrpCodeList:string,
}

export interface GetGlbCurrRateGrpList_output{
   returnObj:Erp_Tablesets_GlbCurrRateGrpTableset[],
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
   returnObj:Erp_Tablesets_CurrRateGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rateGrpCode
      @param sourceCurrCode
   */  
export interface GetNewCurrConvRule_input{
   ds:Erp_Tablesets_CurrRateGrpTableset[],
   rateGrpCode:string,
   sourceCurrCode:string,
}

export interface GetNewCurrConvRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param ds
      @param rateGrpCode
   */  
export interface GetNewCurrRateDisp_input{
   ds:Erp_Tablesets_CurrRateGrpTableset[],
   rateGrpCode:string,
}

export interface GetNewCurrRateDisp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param ds
      @param rateGrpCode
   */  
export interface GetNewCurrRateGrpAttch_input{
   ds:Erp_Tablesets_CurrRateGrpTableset[],
   rateGrpCode:string,
}

export interface GetNewCurrRateGrpAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCurrRateGrp_input{
   ds:Erp_Tablesets_CurrRateGrpTableset[],
}

export interface GetNewCurrRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param whereClauseCurrRateGrp
      @param whereClauseCurrRateGrpAttch
      @param whereClauseCurrConvRule
      @param whereClauseCurrRateDisp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCurrRateGrp:string,
   whereClauseCurrRateGrpAttch:string,
   whereClauseCurrConvRule:string,
   whereClauseCurrRateDisp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CurrRateGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GlbCurrRateGrpsExist_output{
parameters : {
      /**  output parameters  */  
   GlbCurrRateGrpsExist:boolean,
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
      @param glbRateGrpCode
      @param ds
      @param ds1
   */  
export interface LinkGlbCurrRateGrp_input{
      /**  Global Company field on the GlbCurrRateGrp record to link  */  
   glbCompany:string,
      /**  Global CurrRateGrp Code field on the GlbCurrRateGrp record to link  */  
   glbRateGrpCode:string,
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
   ds1:Erp_Tablesets_CurrRateGrpTableset[],
}

export interface LinkGlbCurrRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset,
   ds1:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface LinkSelected_input{
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

export interface LinkSelected_output{
parameters : {
      /**  output parameters  */  
   linkEnable:boolean,
   unLinlkEnable:boolean,
   ds:Erp_Tablesets_GlbCurrRateGrpTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbRateGrpCode
      @param ds
   */  
export interface PreLinkGlbCurrRateGrp_input{
      /**  Global Company field on the GlbCurrRateGrp record to link  */  
   glbCompany:string,
      /**  Global Rate Group Code field on the GlbCurrRateGrp record to link  */  
   glbRateGrpCode:string,
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

export interface PreLinkGlbCurrRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset,
   vMessage:string,
}
}

   /** Required : 
      @param glbCompany
      @param glbRateGrpCode
      @param ds
   */  
export interface SkipGlbCurrRateGrp_input{
      /**  Global Company field on the GlbCurrRateGrp record to skip  */  
   glbCompany:string,
      /**  Global Rate Group Code field on the GlbCurrRateGrp record to skip  */  
   glbRateGrpCode:string,
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

export interface SkipGlbCurrRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbRateGrpCode
      @param ds
   */  
export interface UnlinkGlbCurrRateGrp_input{
      /**  Global Company field on the GlbCurrency record to unlink  */  
   glbCompany:string,
      /**  Global Rate Group Code field on the GlbCurrRateGrp record to unlink  */  
   glbRateGrpCode:string,
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

export interface UnlinkGlbCurrRateGrp_output{
   returnObj:Erp_Tablesets_CurrRateGrpTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCurrRateGrpTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCurrRateGrpTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CurrRateGrpTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrRateGrpTableset,
}
}

   /** Required : 
      @param plRateGrpCode
      @param plCrossRate
      @param proposedAltCrossRate
   */  
export interface ValidateAltCrossCurrCode_input{
      /**  The RateGrpCode selected by the user  */  
   plRateGrpCode:string,
      /**  The CrossCurrCode selected by the user  */  
   plCrossRate:string,
      /**  The AltCrossCurrCode selected by the user  */  
   proposedAltCrossRate:string,
}

export interface ValidateAltCrossCurrCode_output{
}

   /** Required : 
      @param plRateGrpCode
      @param proposedBaseRateGrp
      @param plCrossCurrCode
      @param plAltCrossCurrCode
   */  
export interface ValidateBaseRateGrp_input{
      /**  The proposed value for Rate Grp  */  
   plRateGrpCode:string,
      /**  The proposed value for Base Rate Grp field  */  
   proposedBaseRateGrp:string,
      /**  The proposed value for CrossCurrCode field  */  
   plCrossCurrCode:string,
      /**  The proposed value for AltCrossCurrCode field  */  
   plAltCrossCurrCode:string,
}

export interface ValidateBaseRateGrp_output{
}

   /** Required : 
      @param plRateGrpCode
      @param proposedCrossRate
      @param plAltCrossRate
   */  
export interface ValidateCrossCurrCode_input{
      /**  The RateGrpCode selected by the user  */  
   plRateGrpCode:string,
      /**  The CrossCurrCode selected by the user  */  
   proposedCrossRate:string,
      /**  The AltCrossCurrCode selected by the user  */  
   plAltCrossRate:string,
}

export interface ValidateCrossCurrCode_output{
}

   /** Required : 
      @param plRateGrpCode
      @param plBaseRateGrp
      @param proposedCrossRate
      @param proposedAltCrossRate
   */  
export interface ValidateCurrencies_input{
      /**  The RateGrpCode  */  
   plRateGrpCode:string,
      /**  The Base Rate Group  */  
   plBaseRateGrp:string,
      /**  The AltCrossCurrCode selected by the user  */  
   proposedCrossRate:string,
      /**  The AltCrossCurrCode selected by the user  */  
   proposedAltCrossRate:string,
}

export interface ValidateCurrencies_output{
}

   /** Required : 
      @param plRateGrpCode
      @param proposedInactive
      @param plCrossCurrCode
      @param plAltCrossCurrCode
      @param plBaseRateGrpCode
   */  
export interface ValidateInactive_input{
      /**  The RateGrpCode selected by the user  */  
   plRateGrpCode:string,
      /**  The proposed value for Inactive field  */  
   proposedInactive:boolean,
      /**  The current Cross Rate Currency  */  
   plCrossCurrCode:string,
      /**  The current Alternative Cross Rate Currency  */  
   plAltCrossCurrCode:string,
      /**  The current Base Rate Group  */  
   plBaseRateGrpCode:string,
}

export interface ValidateInactive_output{
}

   /** Required : 
      @param proposedRateGrpCode
   */  
export interface ValidateRateGrpCode_input{
      /**  The RateGrpCode selected by the user  */  
   proposedRateGrpCode:string,
}

export interface ValidateRateGrpCode_output{
}

   /** Required : 
      @param plRateGrpCode
      @param proposedDescription
   */  
export interface ValidateRateGrpDescription_input{
      /**  RateGrpCode value  */  
   plRateGrpCode:string,
      /**  The Rate group description  */  
   proposedDescription:string,
}

export interface ValidateRateGrpDescription_output{
}

   /** Required : 
      @param plRateGrpCode
      @param proposedRateNumDec
   */  
export interface ValidateRateNumDec_input{
      /**  The RateGrpCode selected by the user  */  
   plRateGrpCode:string,
      /**  The RateNumDec  */  
   proposedRateNumDec:number,
}

export interface ValidateRateNumDec_output{
}

   /** Required : 
      @param plRateGrpCode
      @param plUseBaseRate
      @param plSourceCurrCode
      @param plTargetCurrCode
      @param proposedRuleCode
   */  
export interface ValidateRuleCode_input{
   plRateGrpCode:string,
   plUseBaseRate:boolean,
   plSourceCurrCode:string,
   plTargetCurrCode:string,
   proposedRuleCode:number,
}

export interface ValidateRuleCode_output{
}

   /** Required : 
      @param plRateGrpCode
      @param proposedUseBaseRate
   */  
export interface ValidateUseBaseRate_input{
   plRateGrpCode:string,
   proposedUseBaseRate:boolean,
}

export interface ValidateUseBaseRate_output{
}

   /** Required : 
      @param linkGlbCurrRateGrp
      @param glbRateGrpCode
   */  
export interface validateExCurrStatusForRateType_input{
      /**  Link Rate Group Code  */  
   linkGlbCurrRateGrp:string,
      /**  Global Rate Group Code  */  
   glbRateGrpCode:string,
}

export interface validateExCurrStatusForRateType_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

