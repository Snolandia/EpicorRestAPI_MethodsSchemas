import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.POSuggSvc
// Description: This object Generates PO Suggestions.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get POSuggs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POSuggs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoDtlRow
   */  
export function get_POSuggs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POSuggs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SugPoDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SugPoDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POSuggs(requestBody:Erp_Tablesets_SugPoDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the POSugg item
   Description: Calls GetByID to retrieve the POSugg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POSugg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SugPoDtlRow
   */  
export function get_POSuggs_Company_SugNum(Company:string, SugNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SugPoDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_SugPoDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POSugg for the service
   Description: Calls UpdateExt to update POSugg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POSugg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SugPoDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POSuggs_Company_SugNum(Company:string, SugNum:string, requestBody:Erp_Tablesets_SugPoDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")", {
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
   Summary: Call UpdateExt to delete POSugg item
   Description: Call UpdateExt to delete POSugg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POSugg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POSuggs_Company_SugNum(Company:string, SugNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")", {
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
   Description: Get SugPoMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SugPoMscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoMscRow
   */  
export function get_POSuggs_Company_SugNum_SugPoMscs(Company:string, SugNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")/SugPoMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SugPoMsc item
   Description: Calls GetByID to retrieve the SugPoMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SugPoMsc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SugPoMscRow
   */  
export function get_POSuggs_Company_SugNum_SugPoMscs_Company_SugNum_SeqNum(Company:string, SugNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SugPoMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_SugPoMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SugPoMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SugPoMscs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoMscRow
   */  
export function get_SugPoMscs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SugPoMscs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SugPoMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SugPoMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SugPoMscs(requestBody:Erp_Tablesets_SugPoMscRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the SugPoMsc item
   Description: Calls GetByID to retrieve the SugPoMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SugPoMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SugPoMscRow
   */  
export function get_SugPoMscs_Company_SugNum_SeqNum(Company:string, SugNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SugPoMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_SugPoMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SugPoMsc for the service
   Description: Calls UpdateExt to update SugPoMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SugPoMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SugPoMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SugPoMscs_Company_SugNum_SeqNum(Company:string, SugNum:string, SeqNum:string, requestBody:Erp_Tablesets_SugPoMscRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete SugPoMsc item
   Description: Call UpdateExt to delete SugPoMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SugPoMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SugPoMscs_Company_SugNum_SeqNum(Company:string, SugNum:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlListRow)
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
export function get_GetRows(whereClauseSugPoDtl:string, whereClauseSugPoMsc:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSugPoDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSugPoDtl=" + whereClauseSugPoDtl
   }
   if(typeof whereClauseSugPoMsc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSugPoMsc=" + whereClauseSugPoMsc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(sugNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sugNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sugNum=" + sugNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method Autoselect
   Description: This method will automatically change the Buy specification to Yes for any suggestion
for the currently selected buyer that spicifies a vendor, a unit price a quantity , a purchasing factor
and a unit of measure .
            
The UI must mark the selected ttSugPoDtl records are "dirty" before calling this
method.  This is to allow auto select to only run on the records selected
            
This is a danger that there will be some records selected that will not show up in this dataset.
These records may have been updated using a previous filter ( or lack of filter ) or by another user.
This is consistant with Vantage 6.1.
The result is more records may be marked as buy then expected....
   OperationID: Autoselect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Autoselect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Autoselect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Autoselect(requestBody:Autoselect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Autoselect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/Autoselect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Autoselect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcQtys
   Description: This method recalculates RelQty, XRelQty
   OperationID: CalcQtys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalcQtys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcQtys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcQtys(requestBody:CalcQtys_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalcQtys_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/CalcQtys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CalcQtys_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CapableToPromiseGenerate
   Description: Purpose: Called from bo/CapPromise/CapPromise.p to generate POs
Parameters:  none
Notes:
   OperationID: CapableToPromiseGenerate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CapableToPromiseGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CapableToPromiseGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CapableToPromiseGenerate(requestBody:CapableToPromiseGenerate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CapableToPromiseGenerate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/CapableToPromiseGenerate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CapableToPromiseGenerate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCurrencySwitch
   Description: Returns the currency display symbol base on currencyswitch.
   OperationID: ChangeCurrencySwitch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCurrencySwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencySwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencySwitch(requestBody:ChangeCurrencySwitch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCurrencySwitch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeCurrencySwitch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCurrencySwitch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDetailOverridePriceList
   Description: Run this method when the override pricelist is unchecked
   OperationID: ChangeDetailOverridePriceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDetailOverridePriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOverridePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailOverridePriceList(requestBody:ChangeDetailOverridePriceList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDetailOverridePriceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeDetailOverridePriceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDetailOverridePriceList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMfgNum
   Description: Called when MfgNum is changed. Updates MfgNumName.
   OperationID: ChangeMfgNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMfgNum(requestBody:ChangeMfgNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMfgNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeMfgNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeMfgNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMfgPartNum
   Description: Called when MfgNumPart is changed and need to retrieve Supplier Part
   OperationID: ChangeMfgPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMfgPartNum(requestBody:ChangeMfgPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMfgPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeMfgPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeMfgPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePoLine
   Description: Obsolete method which calls overloaded ChangePoLine
   OperationID: ChangePoLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePoLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePoLine(requestBody:ChangePoLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePoLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangePoLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePoLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePoLineWithWarning
   Description: This is called when a PO Line is entered.  An error will return if invalid PO Line, Line is closed, or Part or Configuration is different.
Suggestions fields will be updated with values from PO Line if warnIfDifferences is false, or there are no differences.  Otherwise list of different
fields will be returned in differenceMsg
   OperationID: ChangePoLineWithWarning
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePoLineWithWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoLineWithWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePoLineWithWarning(requestBody:ChangePoLineWithWarning_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePoLineWithWarning_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangePoLineWithWarning", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePoLineWithWarning_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePoNum
   Description: This method will change the PoNum and pull in the values associated with the PO Header.
The default fields are; PONum, VendorNum, PurPoint, BuyerID, ShipViaCode, FOB, TermsCode, Name
   OperationID: ChangePoNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePoNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePoNum(requestBody:ChangePoNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePoNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangePoNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePoNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSugPoMscAmt
   Description: Run this method when the amount changes on the ttSugPoMsc .
   OperationID: ChangeSugPoMscAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSugPoMscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSugPoMscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSugPoMscAmt(requestBody:ChangeSugPoMscAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSugPoMscAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeSugPoMscAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSugPoMscAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSugPoMscCharge
   Description: Run this method when the poMsc charge changes to default in a description.
   OperationID: ChangeSugPoMscCharge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSugPoMscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSugPoMscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSugPoMscCharge(requestBody:ChangeSugPoMscCharge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSugPoMscCharge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeSugPoMscCharge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSugPoMscCharge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSugPoMscPercent
   Description: Run this method when the percentage changes on the ttSugPoMsc .
   OperationID: ChangeSugPoMscPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSugPoMscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSugPoMscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSugPoMscPercent(requestBody:ChangeSugPoMscPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSugPoMscPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeSugPoMscPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSugPoMscPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSupplierPart
   Description: Validate that the Supplier part entered exists.
   OperationID: ChangeSupplierPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSupplierPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupplierPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSupplierPart(requestBody:ChangeSupplierPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSupplierPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeSupplierPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSupplierPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUnitPriceConfirmOverride
   Description: Checks if the source of the unit price is from a supplier price list, if so
will prompt for confirmation of overriding if flag is set against purchase configuration.
   OperationID: ChangeUnitPriceConfirmOverride
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUnitPriceConfirmOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPriceConfirmOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUnitPriceConfirmOverride(requestBody:ChangeUnitPriceConfirmOverride_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUnitPriceConfirmOverride_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeUnitPriceConfirmOverride", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeUnitPriceConfirmOverride_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendor
   Description: This method returns the default information for a vendor. Such as FOB,Terms, purchase point
and currency . This method must be run after changing the VendorID and before invoking the
update method, otherwise all related vendor information on the screen will not be updated.
   OperationID: ChangeVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendor(requestBody:ChangeVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangeVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: ChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangingNumberOfPieces(requestBody:ChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/ChangingNumberOfPieces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBuyers
   Description: Need to be run before generating po's, the Generate() method.
            
This method will check to see if generating PO from the currently tagged suggestions will generate
po's for other buyers.
            
Running the Generate method will assume that all tagged suggestion records will generate PO's,
regardless of the buyer.
   OperationID: CheckBuyers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBuyers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBuyers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBuyers(requestBody:CheckBuyers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBuyers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/CheckBuyers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckBuyers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRelQty
   Description: Purpose: Called to calculate the RelQty if needed
Parameters:  calcField
Notes:
   OperationID: CheckRelQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRelQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRelQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRelQty(requestBody:CheckRelQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRelQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/CheckRelQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRelQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSugPoDtlCount
   Description: This methods will return a count of NEW PO Suggestions for the selected Buyer
   OperationID: GetSugPoDtlCount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSugPoDtlCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPoDtlCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSugPoDtlCount(requestBody:GetSugPoDtlCount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSugPoDtlCount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetSugPoDtlCount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSugPoDtlCount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckGenerate
   Description: This method will check for run out parts and if compliant.
   OperationID: CheckGenerate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGenerate(requestBody:CheckGenerate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckGenerate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/CheckGenerate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckGenerate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateShowCreated
   Description: This method processes all suggestion records where buy has been set to true within
the passed parameters.
            
This will also return a list of all the purchase order numbers that were generated as part of this run.
            
Note: This is doing a getrows and passing back a new dataset minus the records that
were processed. The dataset at the client will still have the processed records, in
order to removed these records we may have to somehow tag the processed records with
a "D":U or, have the UI replace their dataset with this new one.
   OperationID: GenerateShowCreated
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateShowCreated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateShowCreated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateShowCreated(requestBody:GenerateShowCreated_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateShowCreated_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GenerateShowCreated", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenerateShowCreated_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Generate
   Description: This method processes all suggestion records where buy has been set to true within
the passed parameters.
Note: This is doing a getrows and passing back a new dataset minus the records that
were processed. The dataset at the client will still have the processed records, in
order to removed these records we may have to somehow tag the processed records with
a "D":U or, have the UI replace their dataset with this new one.
   OperationID: Generate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Generate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Generate(requestBody:Generate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Generate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/Generate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Generate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAuthorizedAgentList
   Description: Returns a list of Buyers, authorized for the Current User.
   OperationID: GetAuthorizedAgentList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAuthorizedAgentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAuthorizedAgentList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAuthorizedAgentList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetAuthorizedAgentList", {
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
         resolve(data as GetAuthorizedAgentList_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetDefaultBuyer
   Description: Purpose:  RETURNS THE DEFAULT BUYER FOR CURRENT COMPANY
Parameters:  out buyerId, out buyerIdName
Notes:
   OperationID: GetDefaultBuyer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultBuyer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultBuyer(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultBuyer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetDefaultBuyer", {
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
         resolve(data as GetDefaultBuyer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetForecastVendors
   Description: This method returns a list of inter-company trading partners. Use to populate the
grid to select inter-company partners.
   OperationID: GetForecastVendors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForecastVendors_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetForecastVendors(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetForecastVendors_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetForecastVendors", {
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
         resolve(data as GetForecastVendors_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListPlant
   Description: Returns a list of rows that satisfy the where clause. Use in place of GetList
   OperationID: GetListPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListPlant(requestBody:GetListPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetListPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsPlant
   Description: Returns a dataset containing all rows that satisfy the where clauses. use in place of GetRows
   OperationID: GetRowsPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsPlant(requestBody:GetRowsPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetRowsPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartIsRunOut
   Description: The method chekcs status of the current Part and if this Part is Active and not onHold
or it`s HoldDay later then today, but it is flagged as Run Out then it sets
value of isRunOut parament in true..
   OperationID: PartIsRunOut
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartIsRunOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartIsRunOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartIsRunOut(requestBody:PartIsRunOut_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartIsRunOut_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/PartIsRunOut", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PartIsRunOut_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SendForecast
   Description: This method will process the selected forecast vendor records and send a forecast.
   OperationID: SendForecast
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SendForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SendForecast(requestBody:SendForecast_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SendForecast_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SendForecast", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SendForecast_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSugPoDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSugPoDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSugPoDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSugPoDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSugPoDtl(requestBody:GetNewSugPoDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSugPoDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetNewSugPoDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewSugPoDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSugPoMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSugPoMsc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSugPoMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSugPoMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSugPoMsc(requestBody:GetNewSugPoMsc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSugPoMsc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetNewSugPoMsc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewSugPoMsc_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SugPoDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SugPoDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoMscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SugPoMscRow,
}

export interface Erp_Tablesets_SugPoDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   "SugNum":number,
      /**  Type of requirement - "M" - Material "S" - Subcontract.  */  
   "SugType":string,
      /**  The Id that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  Due date of the requirement. Not maintainable.  */  
   "DueDate":string,
      /**  Order quantity for this release in our unit of measure.  */  
   "XRelQty":number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  */  
   "PurchasingFactor":number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   "RelQty":number,
      /**  Job Number of the requirement.  Not maintainable.  */  
   "JobNum":string,
      /**  Job assembly of the requirement.  Not maintainable.  */  
   "AssemblySeq":number,
      /**  Job Seq of the requirement. Not maintainable.  */  
   "JobSeq":number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   "WarehouseCode":string,
      /**  Incoterms  */  
   "FOB":string,
      /**  Defaults from the XASyst.ShipViaCode.  */  
   "ShipViaCode":string,
      /**  Defaults from the Vendor.  */  
   "TermsCode":string,
      /**  VendorNum that ties back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Ties back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   "LineDesc":string,
      /**  Issue(Our) Unit Of Measure.  */  
   "IUM":string,
      /**  The unit price in the vendors unit of measure.  */  
   "UnitPrice":number,
      /**  The unit price in the vendors unit of measure and currency.  */  
   "DocUnitPrice":number,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Purchase UOM  */  
   "PUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "CostPerCode":string,
      /**  OUR internal Part number for this item.  */  
   "PartNum":string,
      /**  Supplier Part Number  */  
   "VenPartNum":string,
      /**  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  */  
   "ClassID":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Duplicate of Vendor.VendorID. Used for sorting.  */  
   "VendorID":string,
      /**  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  */  
   "Name":string,
      /**  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  */  
   "Buy":boolean,
      /**  Purchase order number that this POSugDtl record should be added to.  */  
   "PONUM":number,
      /**  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  */  
   "POLine":number,
      /**  Operation Master Code - Duplicated from the Subcontract JobOper.  */  
   "OpCode":string,
      /**  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  */  
   "OrderByDate":string,
      /**  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  */  
   "LeadTime":number,
      /**  Requisition which generated this POSugDtl record.  */  
   "ReqNum":number,
      /**  Requisition line which generated this POSugDtl record.  */  
   "ReqLine":number,
      /**  Site Identifier. This field can not be blank.  */  
   "Plant":string,
      /**  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  */  
   "CreateRFQ":boolean,
      /**  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  */  
   "SourceRFQ":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  */  
   "GlbSugNum":number,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   "GlbSuggestion":boolean,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   "OrderNum":number,
      /**  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   "OrderLine":number,
      /**  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   "OrderRelNum":number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  */  
   "DropShip":boolean,
      /**  MfgNum  */  
   "MfgNum":number,
      /**  MfgPartNum  */  
   "MfgPartNum":string,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   "ShipToNum":string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   "SoldToNum":number,
      /**  Contains the key value for the shipping contact.  */  
   "ShpConNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  */  
   "ShipToCustNum":number,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Open Purchase Order Release flag  */  
   "PORelOpen":boolean,
      /**  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  */  
   "SugReason":string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   "ABCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Code of the related Req (if specified) or Supplier  */  
   "CurrencyCode":string,
      /**  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandContractNum":number,
      /**  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandHeadSeq":number,
      /**  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandDtlSeq":number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandScheduleSeq":number,
   "calcCurrencySwitch":boolean,
   "calcDisplaySymbol":string,
   "calcDocDisplaySymbol":string,
   "DisablePoFields":boolean,
   "PriceBrkChevron":boolean,
   "DisableCurrencySwitch":boolean,
   "DisablePriceBrkBtn":boolean,
   "calcDueDate":string,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
   "DisableSRMFields":boolean,
      /**  Name of Manufacturer  */  
   "MfgNumName":string,
   "PartNumTrackDim":boolean,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   "NotCompliant":boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   "BuyerIDName":string,
      /**  Full description of the part class.  */  
   "ClassDescription":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpCodeOpDesc":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  defaults from the company file.  */  
   "PONUMShipName":string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "PONUMShipToConName":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   "ReqLineLineDesc":string,
      /**  defaults from the company file.  */  
   "ReqNumShipName":string,
      /**  Ship to contact name.  */  
   "ReqNumShipToConName":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   "TermsCodeDescription":string,
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
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SugPoDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   "SugNum":number,
      /**  Type of requirement - "M" - Material "S" - Subcontract.  */  
   "SugType":string,
      /**  The Id that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  Due date of the requirement. Not maintainable.  */  
   "DueDate":string,
      /**  Order quantity for this release in our unit of measure.  */  
   "XRelQty":number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  */  
   "PurchasingFactor":number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   "RelQty":number,
      /**  Job Number of the requirement.  Not maintainable.  */  
   "JobNum":string,
      /**  Job assembly of the requirement.  Not maintainable.  */  
   "AssemblySeq":number,
      /**  Job Seq of the requirement. Not maintainable.  */  
   "JobSeq":number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   "WarehouseCode":string,
      /**  Incoterms  */  
   "FOB":string,
      /**  Defaults from the XASyst.ShipViaCode.  */  
   "ShipViaCode":string,
      /**  Defaults from the Vendor.  */  
   "TermsCode":string,
      /**  VendorNum that ties back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Ties back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   "LineDesc":string,
      /**  Issue(Our) Unit Of Measure.  */  
   "IUM":string,
      /**  The unit price in the vendors unit of measure.  */  
   "UnitPrice":number,
      /**  The unit price in the vendors unit of measure and currency.  */  
   "DocUnitPrice":number,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Purchase UOM  */  
   "PUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "CostPerCode":string,
      /**  OUR internal Part number for this item.  */  
   "PartNum":string,
      /**  Supplier Part Number  */  
   "VenPartNum":string,
      /**  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  */  
   "ClassID":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Duplicate of Vendor.VendorID. Used for sorting.  */  
   "VendorID":string,
      /**  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  */  
   "Name":string,
      /**  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  */  
   "Buy":boolean,
      /**  Purchase order number that this POSugDtl record should be added to.  */  
   "PONUM":number,
      /**  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  */  
   "POLine":number,
      /**  Operation Master Code - Duplicated from the Subcontract JobOper.  */  
   "OpCode":string,
      /**  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  */  
   "OrderByDate":string,
      /**  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  */  
   "LeadTime":number,
      /**  Requisition which generated this POSugDtl record.  */  
   "ReqNum":number,
      /**  Requisition line which generated this POSugDtl record.  */  
   "ReqLine":number,
      /**  Site Identifier. This field can not be blank.  */  
   "Plant":string,
      /**  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  */  
   "CreateRFQ":boolean,
      /**  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  */  
   "SourceRFQ":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  */  
   "GlbSugNum":number,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   "GlbSuggestion":boolean,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   "OrderNum":number,
      /**  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   "OrderLine":number,
      /**  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   "OrderRelNum":number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  */  
   "DropShip":boolean,
      /**  MfgNum  */  
   "MfgNum":number,
      /**  MfgPartNum  */  
   "MfgPartNum":string,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   "ShipToNum":string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   "SoldToNum":number,
      /**  Contains the key value for the shipping contact.  */  
   "ShpConNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  */  
   "ShipToCustNum":number,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Open Purchase Order Release flag  */  
   "PORelOpen":boolean,
      /**  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  */  
   "SugReason":string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   "ABCCode":string,
      /**  Direction  */  
   "Direction":string,
      /**  Per  */  
   "Per":string,
      /**  ManualFactor  */  
   "ManualFactor":boolean,
      /**  Factor  */  
   "Factor":number,
      /**  PricingQty  */  
   "PricingQty":number,
      /**  PricingUnitPrice  */  
   "PricingUnitPrice":number,
      /**  UOM  */  
   "UOM":string,
      /**  UrgentPlanning  */  
   "UrgentPlanning":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MaintainPricingUnits  */  
   "MaintainPricingUnits":boolean,
      /**  Currency Code of the related Req (if specified) or Supplier  */  
   "CurrencyCode":string,
      /**  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  */  
   "Review":boolean,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   "OverridePriceList":boolean,
      /**  ContractID  */  
   "ContractID":string,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandContractNum":number,
      /**  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandHeadSeq":number,
      /**  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandDtlSeq":number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   "DemandScheduleSeq":number,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Date and time when this record was created.  */  
   "CreatedOn":string,
      /**  If True indicates the Currency matches the Base Currency  */  
   "calcCurrencySwitch":boolean,
      /**  Currency symbol in for Document Currency  */  
   "calcDocDisplaySymbol":string,
   "calcDueDate":string,
      /**  Flag to indicate whether the calcCurrencySwitch field should be disabled.  */  
   "DisableCurrencySwitch":boolean,
   "DisablePoFields":boolean,
   "DisablePriceBrkBtn":boolean,
   "DisableSRMFields":boolean,
      /**  Name of Manufacturer  */  
   "MfgNumName":string,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   "NotCompliant":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
   "PartNumTrackDim":boolean,
   "PriceBrkChevron":boolean,
      /**  Currency symbol in for Base Currency  */  
   "calcDisplaySymbol":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BuyerIDName":string,
   "ClassDescription":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetAttrClassID":string,
   "DynAttrValueSetShortDescription":string,
   "FOBDescription":string,
   "JobNumPartDescription":string,
   "ManufacturerName":string,
   "OpCodeOpDesc":string,
   "PartPartDescription":string,
   "PartTrackInventoryByRevision":boolean,
   "PartTrackInventoryAttributes":boolean,
   "PartTrackDimension":boolean,
   "PlantName":string,
   "POLinePartNum":string,
   "POLineVenPartNum":string,
   "POLineLineDesc":string,
   "PONUMShipToConName":string,
   "PONUMShipName":string,
   "ReqLineLineDesc":string,
   "ReqNumShipName":string,
   "ReqNumShipToConName":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TermsCodeDescription":string,
   "VendorNumEDISupplier":boolean,
   "VendorNumName":string,
   "VendorNumZIP":string,
   "VendorNumState":string,
   "VendorNumVendorID":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress2":string,
   "VendorNumAddress1":string,
   "VendorNumTermsCode":string,
   "VendorNumCity":string,
   "VendorNumCountry":string,
   "VendorNumDefaultFOB":string,
   "WarehouseCodeDescription":string,
   "XbSystDisableOverridePriceListOption":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SugPoMscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   "SugNum":number,
      /**  Sequence Number  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overrideable by the user. This can't be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "MiscAmt":number,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "DocMiscAmt":number,
      /**  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  */  
   "Taxable":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   "GlbSuggestion":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  If True indicates the Currency matches the Base Currency  */  
   "CurrencySwitch":boolean,
      /**  Currency symbol in for Base Currency  */  
   "DisplaySymbol":string,
      /**  Flag to indicate whether the CurrencySwitch field should be disabled.  */  
   "DisableCurrencySwitch":boolean,
      /**  Currency symbol in for Document Currency  */  
   "DocDisplaySymbol":string,
   "DisableSRMFields":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "BitFlag":number,
   "MiscCodeLCAmount":number,
   "MiscCodeDescription":string,
   "MiscCodeLCCurrencyCode":string,
   "MiscCodeLCDisburseMethod":string,
   "SugNumVendorID":string,
   "SugNumName":string,
   "SugNumLineDesc":string,
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
      @param ipPlantKey
      @param ipCurBuyer
      @param ipCutOffDate
   */  
export interface Autoselect_input{
   ds:Erp_Tablesets_POSuggTableset[],
      /**  Plant or blank for all  */  
   ipPlantKey:string,
      /**  BuyerId or blank for all buyers  */  
   ipCurBuyer:string,
      /**  Cut off date for suggestions  */  
   ipCutOffDate:string,
}

export interface Autoselect_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param calcField
      @param ds
   */  
export interface CalcQtys_input{
      /**  calcField  */  
   calcField:string,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface CalcQtys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param ipOrderNum
      @param ipSugNumList
   */  
export interface CapableToPromiseGenerate_input{
   ipOrderNum:number,
   ipSugNumList:number,
}

export interface CapableToPromiseGenerate_output{
parameters : {
      /**  output parameters  */  
   opError:string,
}
}

   /** Required : 
      @param currencySwitch
      @param vendorNum
      @param currencyCode
   */  
export interface ChangeCurrencySwitch_input{
      /**  Logical indicating if the currency toggle is checked  */  
   currencySwitch:boolean,
      /**  SugPoDtl.VendorNum  */  
   vendorNum:number,
      /**  SugPoDtl.CurrencyCode  */  
   currencyCode:string,
}

export interface ChangeCurrencySwitch_output{
parameters : {
      /**  output parameters  */  
   displaySymbol:string,
}
}

   /** Required : 
      @param overridePriceList
      @param ds
   */  
export interface ChangeDetailOverridePriceList_input{
      /**  True is override pricelist has been checked  */  
   overridePriceList:boolean,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeDetailOverridePriceList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param ipMfgNum
      @param ds
   */  
export interface ChangeMfgNum_input{
      /**  Manufacturer Number  */  
   ipMfgNum:number,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeMfgNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param ipMfgPartNum
      @param ds
   */  
export interface ChangeMfgPartNum_input{
      /**  Manufacturer Number  */  
   ipMfgPartNum:string,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeMfgPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param newPoLine
      @param warnIfDifferences
      @param ds
   */  
export interface ChangePoLineWithWarning_input{
      /**  New PO Line to use  */  
   newPoLine:number,
      /**  If True return list of fields that differ between Suggestion and PO Line  */  
   warnIfDifferences:boolean,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangePoLineWithWarning_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
   differenceMsg:string,
}
}

   /** Required : 
      @param newPoLine
      @param ds
   */  
export interface ChangePoLine_input{
      /**  New Po Line  */  
   newPoLine:number,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangePoLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param newPoNum
      @param ds
   */  
export interface ChangePoNum_input{
      /**  Indicates the Po to retrieve  */  
   newPoNum:number,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangePoNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSugPoMscAmt_input{
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeSugPoMscAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param newMiscCode
      @param ds
   */  
export interface ChangeSugPoMscCharge_input{
      /**  New Misc Code  */  
   newMiscCode:string,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeSugPoMscCharge_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSugPoMscPercent_input{
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeSugPoMscPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param newVenPartNum
      @param ds
   */  
export interface ChangeSupplierPart_input{
      /**  The Supplier Part Number proposed value  */  
   newVenPartNum:string,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeSupplierPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUnitPriceConfirmOverride_input{
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeUnitPriceConfirmOverride_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
   sConfirmMsg:string,
}
}

   /** Required : 
      @param newVendID
      @param ds
   */  
export interface ChangeVendor_input{
      /**  New Vendor ID  */  
   newVendID:string,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface ChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface ChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param opCurBuyer
   */  
export interface CheckBuyers_input{
      /**  Current BuyerID  */  
   opCurBuyer:string,
}

export interface CheckBuyers_output{
parameters : {
      /**  output parameters  */  
   poForOtherBuyer:boolean,
   suggList:string,
   opCurBuyer:string,
   opBuyerName:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckGenerate_input{
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface CheckGenerate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
   opPartRunOutMessage:string,
   opComplianceFlag:boolean,
}
}

   /** Required : 
      @param calcField
   */  
export interface CheckRelQty_input{
   calcField:string,
}

export interface CheckRelQty_output{
}

   /** Required : 
      @param sugNum
   */  
export interface DeleteByID_input{
   sugNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ForecastVendorsRow{
   Send:boolean,
   VendorNum:number,
   VendorId:string,
   VendorName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ForecastVendorsTableset{
   ForecastVendors:Erp_Tablesets_ForecastVendorsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_POSuggTableset{
   SugPoDtl:Erp_Tablesets_SugPoDtlRow[],
   SugPoMsc:Erp_Tablesets_SugPoMscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SugPoCreatedListRow{
   Company:string,
   PONum:number,
   VendorID:string,
   CreatedDateTime:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SugPoCreatedListTableset{
   SugPoCreatedList:Erp_Tablesets_SugPoCreatedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SugPoDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**  Type of requirement - "M" - Material "S" - Subcontract.  */  
   SugType:string,
      /**  The Id that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  Due date of the requirement. Not maintainable.  */  
   DueDate:string,
      /**  Order quantity for this release in our unit of measure.  */  
   XRelQty:number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  */  
   PurchasingFactor:number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   RelQty:number,
      /**  Job Number of the requirement.  Not maintainable.  */  
   JobNum:string,
      /**  Job assembly of the requirement.  Not maintainable.  */  
   AssemblySeq:number,
      /**  Job Seq of the requirement. Not maintainable.  */  
   JobSeq:number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   WarehouseCode:string,
      /**  Incoterms  */  
   FOB:string,
      /**  Defaults from the XASyst.ShipViaCode.  */  
   ShipViaCode:string,
      /**  Defaults from the Vendor.  */  
   TermsCode:string,
      /**  VendorNum that ties back to the Vendor master file.  */  
   VendorNum:number,
      /**  Ties back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   LineDesc:string,
      /**  Issue(Our) Unit Of Measure.  */  
   IUM:string,
      /**  The unit price in the vendors unit of measure.  */  
   UnitPrice:number,
      /**  The unit price in the vendors unit of measure and currency.  */  
   DocUnitPrice:number,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Purchase UOM  */  
   PUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  OUR internal Part number for this item.  */  
   PartNum:string,
      /**  Supplier Part Number  */  
   VenPartNum:string,
      /**  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  */  
   ClassID:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Duplicate of Vendor.VendorID. Used for sorting.  */  
   VendorID:string,
      /**  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  */  
   Name:string,
      /**  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  */  
   Buy:boolean,
      /**  Purchase order number that this POSugDtl record should be added to.  */  
   PONUM:number,
      /**  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  */  
   POLine:number,
      /**  Operation Master Code - Duplicated from the Subcontract JobOper.  */  
   OpCode:string,
      /**  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  */  
   OrderByDate:string,
      /**  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  */  
   LeadTime:number,
      /**  Requisition which generated this POSugDtl record.  */  
   ReqNum:number,
      /**  Requisition line which generated this POSugDtl record.  */  
   ReqLine:number,
      /**  Site Identifier. This field can not be blank.  */  
   Plant:string,
      /**  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  */  
   CreateRFQ:boolean,
      /**  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  */  
   SourceRFQ:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  */  
   GlbSugNum:number,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   GlbSuggestion:boolean,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   OrderNum:number,
      /**  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   OrderLine:number,
      /**  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   OrderRelNum:number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  */  
   DropShip:boolean,
      /**  MfgNum  */  
   MfgNum:number,
      /**  MfgPartNum  */  
   MfgPartNum:string,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   ShipToNum:string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   SoldToNum:number,
      /**  Contains the key value for the shipping contact.  */  
   ShpConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  */  
   ShipToCustNum:number,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Open Purchase Order Release flag  */  
   PORelOpen:boolean,
      /**  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  */  
   SugReason:string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   ABCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Code of the related Req (if specified) or Supplier  */  
   CurrencyCode:string,
      /**  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandContractNum:number,
      /**  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandDtlSeq:number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandScheduleSeq:number,
   calcCurrencySwitch:boolean,
   calcDisplaySymbol:string,
   calcDocDisplaySymbol:string,
   DisablePoFields:boolean,
   PriceBrkChevron:boolean,
   DisableCurrencySwitch:boolean,
   DisablePriceBrkBtn:boolean,
   calcDueDate:string,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
   DisableSRMFields:boolean,
      /**  Name of Manufacturer  */  
   MfgNumName:string,
   PartNumTrackDim:boolean,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   NotCompliant:boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   BuyerIDName:string,
      /**  Full description of the part class.  */  
   ClassDescription:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpCodeOpDesc:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  defaults from the company file.  */  
   PONUMShipName:string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   PONUMShipToConName:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   ReqLineLineDesc:string,
      /**  defaults from the company file.  */  
   ReqNumShipName:string,
      /**  Ship to contact name.  */  
   ReqNumShipToConName:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   TermsCodeDescription:string,
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
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SugPoDtlListTableset{
   SugPoDtlList:Erp_Tablesets_SugPoDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SugPoDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**  Type of requirement - "M" - Material "S" - Subcontract.  */  
   SugType:string,
      /**  The Id that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  Due date of the requirement. Not maintainable.  */  
   DueDate:string,
      /**  Order quantity for this release in our unit of measure.  */  
   XRelQty:number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  */  
   PurchasingFactor:number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   RelQty:number,
      /**  Job Number of the requirement.  Not maintainable.  */  
   JobNum:string,
      /**  Job assembly of the requirement.  Not maintainable.  */  
   AssemblySeq:number,
      /**  Job Seq of the requirement. Not maintainable.  */  
   JobSeq:number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   WarehouseCode:string,
      /**  Incoterms  */  
   FOB:string,
      /**  Defaults from the XASyst.ShipViaCode.  */  
   ShipViaCode:string,
      /**  Defaults from the Vendor.  */  
   TermsCode:string,
      /**  VendorNum that ties back to the Vendor master file.  */  
   VendorNum:number,
      /**  Ties back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   LineDesc:string,
      /**  Issue(Our) Unit Of Measure.  */  
   IUM:string,
      /**  The unit price in the vendors unit of measure.  */  
   UnitPrice:number,
      /**  The unit price in the vendors unit of measure and currency.  */  
   DocUnitPrice:number,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Purchase UOM  */  
   PUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  OUR internal Part number for this item.  */  
   PartNum:string,
      /**  Supplier Part Number  */  
   VenPartNum:string,
      /**  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  */  
   ClassID:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Duplicate of Vendor.VendorID. Used for sorting.  */  
   VendorID:string,
      /**  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  */  
   Name:string,
      /**  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  */  
   Buy:boolean,
      /**  Purchase order number that this POSugDtl record should be added to.  */  
   PONUM:number,
      /**  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  */  
   POLine:number,
      /**  Operation Master Code - Duplicated from the Subcontract JobOper.  */  
   OpCode:string,
      /**  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  */  
   OrderByDate:string,
      /**  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  */  
   LeadTime:number,
      /**  Requisition which generated this POSugDtl record.  */  
   ReqNum:number,
      /**  Requisition line which generated this POSugDtl record.  */  
   ReqLine:number,
      /**  Site Identifier. This field can not be blank.  */  
   Plant:string,
      /**  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  */  
   CreateRFQ:boolean,
      /**  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  */  
   SourceRFQ:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  */  
   GlbSugNum:number,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   GlbSuggestion:boolean,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   OrderNum:number,
      /**  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   OrderLine:number,
      /**  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  */  
   OrderRelNum:number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  */  
   DropShip:boolean,
      /**  MfgNum  */  
   MfgNum:number,
      /**  MfgPartNum  */  
   MfgPartNum:string,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   ShipToNum:string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  */  
   SoldToNum:number,
      /**  Contains the key value for the shipping contact.  */  
   ShpConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  */  
   ShipToCustNum:number,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Open Purchase Order Release flag  */  
   PORelOpen:boolean,
      /**  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  */  
   SugReason:string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   ABCCode:string,
      /**  Direction  */  
   Direction:string,
      /**  Per  */  
   Per:string,
      /**  ManualFactor  */  
   ManualFactor:boolean,
      /**  Factor  */  
   Factor:number,
      /**  PricingQty  */  
   PricingQty:number,
      /**  PricingUnitPrice  */  
   PricingUnitPrice:number,
      /**  UOM  */  
   UOM:string,
      /**  UrgentPlanning  */  
   UrgentPlanning:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MaintainPricingUnits  */  
   MaintainPricingUnits:boolean,
      /**  Currency Code of the related Req (if specified) or Supplier  */  
   CurrencyCode:string,
      /**  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  */  
   Review:boolean,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   OverridePriceList:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandContractNum:number,
      /**  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandDtlSeq:number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  */  
   DemandScheduleSeq:number,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Date and time when this record was created.  */  
   CreatedOn:string,
      /**  If True indicates the Currency matches the Base Currency  */  
   calcCurrencySwitch:boolean,
      /**  Currency symbol in for Document Currency  */  
   calcDocDisplaySymbol:string,
   calcDueDate:string,
      /**  Flag to indicate whether the calcCurrencySwitch field should be disabled.  */  
   DisableCurrencySwitch:boolean,
   DisablePoFields:boolean,
   DisablePriceBrkBtn:boolean,
   DisableSRMFields:boolean,
      /**  Name of Manufacturer  */  
   MfgNumName:string,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   NotCompliant:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
   PartNumTrackDim:boolean,
   PriceBrkChevron:boolean,
      /**  Currency symbol in for Base Currency  */  
   calcDisplaySymbol:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   BuyerIDName:string,
   ClassDescription:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetAttrClassID:string,
   DynAttrValueSetShortDescription:string,
   FOBDescription:string,
   JobNumPartDescription:string,
   ManufacturerName:string,
   OpCodeOpDesc:string,
   PartPartDescription:string,
   PartTrackInventoryByRevision:boolean,
   PartTrackInventoryAttributes:boolean,
   PartTrackDimension:boolean,
   PlantName:string,
   POLinePartNum:string,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   PONUMShipToConName:string,
   PONUMShipName:string,
   ReqLineLineDesc:string,
   ReqNumShipName:string,
   ReqNumShipToConName:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TermsCodeDescription:string,
   VendorNumEDISupplier:boolean,
   VendorNumName:string,
   VendorNumZIP:string,
   VendorNumState:string,
   VendorNumVendorID:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumTermsCode:string,
   VendorNumCity:string,
   VendorNumCountry:string,
   VendorNumDefaultFOB:string,
   WarehouseCodeDescription:string,
   XbSystDisableOverridePriceListOption:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SugPoMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overrideable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   DocMiscAmt:number,
      /**  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  */  
   Taxable:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   GlbSuggestion:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If True indicates the Currency matches the Base Currency  */  
   CurrencySwitch:boolean,
      /**  Currency symbol in for Base Currency  */  
   DisplaySymbol:string,
      /**  Flag to indicate whether the CurrencySwitch field should be disabled.  */  
   DisableCurrencySwitch:boolean,
      /**  Currency symbol in for Document Currency  */  
   DocDisplaySymbol:string,
   DisableSRMFields:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   BitFlag:number,
   MiscCodeLCAmount:number,
   MiscCodeDescription:string,
   MiscCodeLCCurrencyCode:string,
   MiscCodeLCDisburseMethod:string,
   SugNumVendorID:string,
   SugNumName:string,
   SugNumLineDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPOSuggTableset{
   SugPoDtl:Erp_Tablesets_SugPoDtlRow[],
   SugPoMsc:Erp_Tablesets_SugPoMscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param ipPlantKey
      @param ipCurBuyer
      @param ipCutOffDate
      @param sugPoCreatedListDS
   */  
export interface GenerateShowCreated_input{
   ds:Erp_Tablesets_POSuggTableset[],
      /**  Plant or blank for all  */  
   ipPlantKey:string,
      /**  BuyerId or blank for all buyers  */  
   ipCurBuyer:string,
      /**  Cut off date for suggestions  */  
   ipCutOffDate:string,
   sugPoCreatedListDS:Erp_Tablesets_SugPoCreatedListTableset[],
}

export interface GenerateShowCreated_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
   sugPoCreatedListDS:Erp_Tablesets_SugPoCreatedListTableset,
}
}

   /** Required : 
      @param ds
      @param ipPlantKey
      @param ipCurBuyer
      @param ipCutOffDate
   */  
export interface Generate_input{
   ds:Erp_Tablesets_POSuggTableset[],
      /**  Plant or blank for all  */  
   ipPlantKey:string,
      /**  BuyerId or blank for all buyers  */  
   ipCurBuyer:string,
      /**  Cut off date for suggestions  */  
   ipCutOffDate:string,
}

export interface Generate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

export interface GetAuthorizedAgentList_output{
parameters : {
      /**  output parameters  */  
   opBuyerName:string,
}
}

   /** Required : 
      @param sugNum
   */  
export interface GetByID_input{
   sugNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_POSuggTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_POSuggTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_POSuggTableset[],
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

export interface GetDefaultBuyer_output{
parameters : {
      /**  output parameters  */  
   buyerId:string,
   buyerIdName:string,
}
}

export interface GetForecastVendors_output{
   returnObj:Erp_Tablesets_ForecastVendorsTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListPlant_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetListPlant_output{
   returnObj:Erp_Tablesets_SugPoDtlListTableset[],
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
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_SugPoDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewSugPoDtl_input{
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface GetNewSugPoDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param ds
      @param sugNum
   */  
export interface GetNewSugPoMsc_input{
   ds:Erp_Tablesets_POSuggTableset[],
   sugNum:number,
}

export interface GetNewSugPoMsc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

   /** Required : 
      @param whereClauseSugPoDtl
      @param whereClauseSugPoMsc
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsPlant_input{
      /**  whereClause for SugPoDtl table  */  
   whereClauseSugPoDtl:string,
      /**  whereClause for SugPoMsc table  */  
   whereClauseSugPoMsc:string,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface GetRowsPlant_output{
   returnObj:Erp_Tablesets_POSuggTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSugPoDtl
      @param whereClauseSugPoMsc
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSugPoDtl:string,
   whereClauseSugPoMsc:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_POSuggTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param buyerID
   */  
export interface GetSugPoDtlCount_input{
      /**  buyerID  */  
   buyerID:string,
}

export interface GetSugPoDtlCount_output{
      /**  Count  */  
   returnObj:number,
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
      @param valpartnum
   */  
export interface PartIsRunOut_input{
      /**  The PartNum, whose status need to check  */  
   valpartnum:string,
}

export interface PartIsRunOut_output{
parameters : {
      /**  output parameters  */  
   msg:string,
}
}

   /** Required : 
      @param ds
      @param ds1
   */  
export interface SendForecast_input{
   ds:Erp_Tablesets_ForecastVendorsTableset[],
   ds1:Erp_Tablesets_POSuggTableset[],
}

export interface SendForecast_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastVendorsTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPOSuggTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPOSuggTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_POSuggTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggTableset,
}
}

