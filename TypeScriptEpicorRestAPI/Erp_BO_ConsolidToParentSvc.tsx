import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ConsolidToParentSvc
// Description: bo/ConsolidToParent/ConsolidToParent
Consolidate to Parent Business Object
SCR 40420 (Opr. 320)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/$metadata", {
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
   Description: Get ConsolidToParents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsolidToParents
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenRow
   */  
export function get_ConsolidToParents(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsolidToParents
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ConsTgtGenRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsolidToParents(requestBody:Erp_Tablesets_ConsTgtGenRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ConsolidToParent item
   Description: Calls GetByID to retrieve the ConsolidToParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsolidToParent
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsTgtGenRow
   */  
export function get_ConsolidToParents_Company_GenID(Company:string, GenID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtGenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")", {
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
         resolve(data as Erp_Tablesets_ConsTgtGenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsolidToParent for the service
   Description: Calls UpdateExt to update ConsolidToParent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsolidToParent
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsolidToParents_Company_GenID(Company:string, GenID:string, requestBody:Erp_Tablesets_ConsTgtGenRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")", {
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
   Summary: Call UpdateExt to delete ConsolidToParent item
   Description: Call UpdateExt to delete ConsolidToParent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsolidToParent
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsolidToParents_Company_GenID(Company:string, GenID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")", {
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
   Description: Get ConsSrcCtrls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsSrcCtrls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsolidToParents_Company_GenID_ConsSrcCtrls(Company:string, GenID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")/ConsSrcCtrls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsSrcCtrl item
   Description: Calls GetByID to retrieve the ConsSrcCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcCtrl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsolidToParents_Company_GenID_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
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
         resolve(data as Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsSrcCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsSrcCtrls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsSrcCtrls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsSrcCtrls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsSrcCtrls(requestBody:Erp_Tablesets_ConsSrcCtrlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ConsSrcCtrl item
   Description: Calls GetByID to retrieve the ConsSrcCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
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
         resolve(data as Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsSrcCtrl for the service
   Description: Calls UpdateExt to update ConsSrcCtrl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsSrcCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, requestBody:Erp_Tablesets_ConsSrcCtrlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
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
   Summary: Call UpdateExt to delete ConsSrcCtrl item
   Description: Call UpdateExt to delete ConsSrcCtrl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsSrcCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
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
   Description: Get ConsSrcRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsSrcRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcCtrls_Company_GenID_SourceBook_ConsSrcRates(Company:string, GenID:string, SourceBook:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsSrcRate item
   Description: Calls GetByID to retrieve the ConsSrcRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcCtrls_Company_GenID_SourceBook_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
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
         resolve(data as Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsSrcRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsSrcRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsSrcRates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ConsSrcRatesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsSrcRates(requestBody:Erp_Tablesets_ConsSrcRatesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ConsSrcRate item
   Description: Calls GetByID to retrieve the ConsSrcRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
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
         resolve(data as Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsSrcRate for the service
   Description: Calls UpdateExt to update ConsSrcRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsSrcRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, requestBody:Erp_Tablesets_ConsSrcRatesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
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
   Summary: Call UpdateExt to delete ConsSrcRate item
   Description: Call UpdateExt to delete ConsSrcRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsSrcRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseConsTgtGen:string, whereClauseConsSrcCtrl:string, whereClauseConsSrcRates:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseConsTgtGen!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsTgtGen=" + whereClauseConsTgtGen
   }
   if(typeof whereClauseConsSrcCtrl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsSrcCtrl=" + whereClauseConsSrcCtrl
   }
   if(typeof whereClauseConsSrcRates!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsSrcRates=" + whereClauseConsSrcRates
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetRows" + params, {
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
export function get_GetByID(genID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof genID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "genID=" + genID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetList" + params, {
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
   Summary: Invoke method GetConsDefIDData
   Description: Gets information from the Consolidation Definition
   OperationID: GetConsDefIDData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetConsDefIDData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConsDefIDData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConsDefIDData(requestBody:GetConsDefIDData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetConsDefIDData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetConsDefIDData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetConsDefIDData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaults
   Description: Method to call to get the default consolidation types and currency exchange rates.
   OperationID: GetDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaults(requestBody:GetDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalculateRates
   Description: This method checks if the consolidation rates may need recalculation, and warn user about it.
   OperationID: RecalculateRates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RecalculateRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalculateRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalculateRates(requestBody:RecalculateRates_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RecalculateRates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/RecalculateRates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RecalculateRates_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConsTgtGenEntryMode
   Description: Gets a new Consolidation to Parent record for the specified Entry Type
   OperationID: GetNewConsTgtGenEntryMode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtGenEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtGenEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsTgtGenEntryMode(requestBody:GetNewConsTgtGenEntryMode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewConsTgtGenEntryMode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetNewConsTgtGenEntryMode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewConsTgtGenEntryMode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateExchangeRate
   Description: Checks if the user modified the exchange rate
   OperationID: ValidateExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateExchangeRate(requestBody:ValidateExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSrcAdjustFromFiscalPeriod
   Description: Called when Adjust From Fiscal Period is changed
   OperationID: ValidateSrcAdjustFromFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSrcAdjustFromFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSrcAdjustFromFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSrcAdjustFromFiscalPeriod(requestBody:ValidateSrcAdjustFromFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSrcAdjustFromFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateSrcAdjustFromFiscalPeriod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSrcAdjustFromFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSrcFiscalPeriod
   Description: Validates the source control fiscal period
   OperationID: ValidateSrcFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSrcFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSrcFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSrcFiscalPeriod(requestBody:ValidateSrcFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSrcFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateSrcFiscalPeriod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSrcFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePrevRecords
   Description: Validates if previous consolidations have been processed
   OperationID: ValidatePrevRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePrevRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrevRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePrevRecords(requestBody:ValidatePrevRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePrevRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidatePrevRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePrevRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckConsReadyToPost
   Description: Checks if the consoliation is ready to post
   OperationID: CheckConsReadyToPost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckConsReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConsReadyToPost(requestBody:CheckConsReadyToPost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckConsReadyToPost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/CheckConsReadyToPost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckConsReadyToPost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SendErrorMsg
   Description: Sends the error message
   OperationID: SendErrorMsg
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SendErrorMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendErrorMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SendErrorMsg(requestBody:SendErrorMsg_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SendErrorMsg_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/SendErrorMsg", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SendErrorMsg_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateClosingPeriods
   Description: Validates closing periods
   OperationID: ValidateClosingPeriods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateClosingPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateClosingPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateClosingPeriods(requestBody:ValidateClosingPeriods_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateClosingPeriods_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateClosingPeriods", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateClosingPeriods_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalPeriod
   Description: Validates the fiscal period
   OperationID: ValidateFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalPeriod(requestBody:ValidateFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateFiscalPeriod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalYearandGetPeriods
   Description: Validates the fiscal year and selects the fiscal periods
   OperationID: ValidateFiscalYearandGetPeriods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYearandGetPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYearandGetPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalYearandGetPeriods(requestBody:ValidateFiscalYearandGetPeriods_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFiscalYearandGetPeriods_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateFiscalYearandGetPeriods", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateFiscalYearandGetPeriods_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalYear
   Description: Validates the fiscal year
   OperationID: ValidateFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalYear(requestBody:ValidateFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateFiscalYear", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateGenID
   Description: Validate the Consolidation ID
   OperationID: ValidateGenID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateGenID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGenID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGenID(requestBody:ValidateGenID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateGenID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateGenID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateGenID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRateGroupStatus
   Description: Validate the Rate Group Status
   OperationID: ValidateRateGroupStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateGroupStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRateGroupStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRateGroupStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateRateGroupStatus", {
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
         resolve(data as ValidateRateGroupStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateLastConsol
   Description: Checks if it is the Last Consolidation depending on SourceBook and Consolidation Definition
   OperationID: ValidateLastConsol
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateLastConsol_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLastConsol_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateLastConsol(requestBody:ValidateLastConsol_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateLastConsol_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ValidateLastConsol", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateLastConsol_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConsTgtGen
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtGen
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsTgtGen(requestBody:GetNewConsTgtGen_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewConsTgtGen_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetNewConsTgtGen", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewConsTgtGen_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConsSrcCtrl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsSrcCtrl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewConsSrcCtrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsSrcCtrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsSrcCtrl(requestBody:GetNewConsSrcCtrl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewConsSrcCtrl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetNewConsSrcCtrl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewConsSrcCtrl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConsSrcRates
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsSrcRates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewConsSrcRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsSrcRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsSrcRates(requestBody:GetNewConsSrcRates_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewConsSrcRates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetNewConsSrcRates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewConsSrcRates_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsSrcCtrlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsSrcRatesRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtGenListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtGenRow,
}

export interface Erp_Tablesets_ConsSrcCtrlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SourceBook":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Posted Date  */  
   "PostedDate":string,
      /**  (secounds since midnight)  */  
   "PostedTime":number,
      /**  User ID of person that posted this period.  */  
   "PostedBy":string,
      /**  Account Number where rounding differences will be posted  */  
   "DiffOnExchangeAcct":string,
      /**  Indicates the current status of the generation.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   "GenStatus":string,
      /**  Indicates if consolidation was bypassed  */  
   "Bypassed":boolean,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "DiffExSegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  */  
   "DiffExSegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "DiffExSegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "DiffExSegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "DiffExSegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "DiffExSegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "DiffExSegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "DiffExSegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "DiffExSegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "DiffExSegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "DiffExSegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "DiffExSegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "DiffExSegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "DiffExSegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "DiffExSegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "DiffExSegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "DiffExSegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "DiffExSegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "DiffExSegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "DiffExSegValue20":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**  The related ConsType ID  */  
   "BalanceSheetDefType":string,
      /**  The related ConsType ID  */  
   "IncomeStmtDefType":string,
      /**  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  */  
   "ClosingPeriods":number,
      /**  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  */  
   "ExcludeOpenPrds":boolean,
      /**  The journal code to use when posting the consolidation records in the target company book.  */  
   "TgtJrnlCode":string,
      /**  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  */  
   "ReverseDBCR":boolean,
      /**  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  */  
   "COAMapUID":number,
      /**  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  */  
   "IntermediateJrnlCode":string,
      /**  Retransfer  */  
   "Retransfer":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The fiscal period to start adjusting from  */  
   "AdjustFromFiscalPeriod":number,
      /**  PeriodEndDate  */  
   "PeriodEndDate":string,
      /**  AdjPeriodEndDate  */  
   "AdjPeriodEndDate":string,
      /**  When posting, the last fiscal period that was processed without error, particulary for consolidations that span multiple periods.  */  
   "ProcessedFiscalPeriod":number,
      /**   Indicates the status of the consolidation for display purposes.  Is set programatically.

F - First consolidation
R - Retrospective
L - Last Period Delta
O - Overriding Period  */  
   "ConsolidationStatus":string,
      /**  Indicates if previous periods have not been consolidated  */  
   "PeriodsMissed":boolean,
      /**  Source COA code  */  
   "SourceCOA":string,
      /**  TargetCOA for DiffExtAccount  */  
   "TargetCOA":string,
      /**  Flag indicating that next period consolidation has been performed  */  
   "NextPeriodConsolidation":boolean,
   "BitFlag":number,
   "FiscalCalDescription":string,
   "SourceBookDescription":string,
   "SourceBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsSrcRatesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SourceBook":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  Rate Type id of related RateType.  */  
   "RateTypeID":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Exchange Rate that will be used for this Rate Type.  */  
   "ExchangeRate":number,
      /**  Internal field used to indicate whether or not the user modified the rates.  */  
   "UserModified":boolean,
      /**  Internal field used to indicate if the system was unable to calcuate the rates.  If yes, the rates are in error.  If no, the rates are okay.  */  
   "RateError":boolean,
      /**  Calculation Date  */  
   "CalcDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Daily Average, Period End or None  */  
   "DefaultMethod":string,
      /**  Indicates if the record is selected for retrieval of default values  */  
   "Selected":boolean,
   "Description":string,
   "BitFlag":number,
   "RateTypeIDDescription":string,
   "SourceBookCurrencyCode":string,
   "SourceBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtGenListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Generation Description  */  
   "Description":string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   "GenStatus":string,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   "TgtBook":string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   "TargetCOA":string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   "IntermediateBookID":string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   "ImmediateTrans":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   "RemoteParent":boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   "VantageDB":boolean,
      /**  Import/Export file name.  */  
   "OutputFile":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   "ConsolidationType":string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   "AdjustMode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   "ConsDefIDDescription":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  Indicates the base currency for the book  */  
   "IntermediateBookIDCurrencyCode":string,
      /**  Descripiton of Book  */  
   "IntermediateBookIDDescription":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "TargetCOADescription":string,
      /**  Indicates the base currency for the book  */  
   "TgtBookCurrencyCode":string,
      /**  Descripiton of Book  */  
   "TgtBookDescription":string,
      /**  Company Name  */  
   "TgtCompanyName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtGenRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Generation Description  */  
   "Description":string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   "GenStatus":string,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   "TgtBook":string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   "TargetCOA":string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   "IntermediateBookID":string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   "ImmediateTrans":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   "RemoteParent":boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   "VantageDB":boolean,
      /**  Import/Export file name.  */  
   "OutputFile":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   "ConsolidationType":string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   "AdjustMode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  */  
   "EntryMode":string,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
      /**  LatestConsolidation  */  
   "LatestConsolidation":boolean,
      /**  Closing periods parameter defined in Consolidation definition.  */  
   "ClosingPeriods":number,
   "BitFlag":number,
   "ConsDefIDDescription":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "IntermediateBookIDDescription":string,
   "IntermediateBookIDCurrencyCode":string,
   "TargetCOADescription":string,
   "TgtBookCurrencyCode":string,
   "TgtBookDescription":string,
   "TgtCompanyName":string,
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
      @param intGenID
      @param txtSourceBook
      @param txtFiscalCalendarID
      @param intFiscalYear
      @param txtFiscalYearSuffix
      @param intFiscalPeriod
   */  
export interface CheckConsReadyToPost_input{
      /**  The Consolidation ID  */  
   intGenID:number,
      /**  The Source Book  */  
   txtSourceBook:string,
      /**  The Fiscal Calendar ID  */  
   txtFiscalCalendarID:string,
      /**  The Fiscal Year  */  
   intFiscalYear:number,
      /**  The Fiscal Year Suffix  */  
   txtFiscalYearSuffix:string,
      /**  The Fiscal Period  */  
   intFiscalPeriod:number,
}

export interface CheckConsReadyToPost_output{
parameters : {
      /**  output parameters  */  
   txtpriorPeriodNotPostedMsg:string,
   txtperiodAlreadyPostedMsg:string,
   txtperiodAlreadyGeneratedMsg:string,
   txtfileAlreadyExistsMsg:string,
}
}

   /** Required : 
      @param genID
   */  
export interface DeleteByID_input{
   genID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ConsSrcCtrlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SourceBook:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Posted Date  */  
   PostedDate:string,
      /**  (secounds since midnight)  */  
   PostedTime:number,
      /**  User ID of person that posted this period.  */  
   PostedBy:string,
      /**  Account Number where rounding differences will be posted  */  
   DiffOnExchangeAcct:string,
      /**  Indicates the current status of the generation.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   GenStatus:string,
      /**  Indicates if consolidation was bypassed  */  
   Bypassed:boolean,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   DiffExSegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  */  
   DiffExSegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   DiffExSegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   DiffExSegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   DiffExSegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   DiffExSegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   DiffExSegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   DiffExSegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   DiffExSegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   DiffExSegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   DiffExSegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   DiffExSegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   DiffExSegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   DiffExSegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   DiffExSegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   DiffExSegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   DiffExSegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   DiffExSegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   DiffExSegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   DiffExSegValue20:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**  The related ConsType ID  */  
   BalanceSheetDefType:string,
      /**  The related ConsType ID  */  
   IncomeStmtDefType:string,
      /**  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  */  
   ClosingPeriods:number,
      /**  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  */  
   ExcludeOpenPrds:boolean,
      /**  The journal code to use when posting the consolidation records in the target company book.  */  
   TgtJrnlCode:string,
      /**  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  */  
   ReverseDBCR:boolean,
      /**  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  */  
   COAMapUID:number,
      /**  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  */  
   IntermediateJrnlCode:string,
      /**  Retransfer  */  
   Retransfer:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The fiscal period to start adjusting from  */  
   AdjustFromFiscalPeriod:number,
      /**  PeriodEndDate  */  
   PeriodEndDate:string,
      /**  AdjPeriodEndDate  */  
   AdjPeriodEndDate:string,
      /**  When posting, the last fiscal period that was processed without error, particulary for consolidations that span multiple periods.  */  
   ProcessedFiscalPeriod:number,
      /**   Indicates the status of the consolidation for display purposes.  Is set programatically.

F - First consolidation
R - Retrospective
L - Last Period Delta
O - Overriding Period  */  
   ConsolidationStatus:string,
      /**  Indicates if previous periods have not been consolidated  */  
   PeriodsMissed:boolean,
      /**  Source COA code  */  
   SourceCOA:string,
      /**  TargetCOA for DiffExtAccount  */  
   TargetCOA:string,
      /**  Flag indicating that next period consolidation has been performed  */  
   NextPeriodConsolidation:boolean,
   BitFlag:number,
   FiscalCalDescription:string,
   SourceBookDescription:string,
   SourceBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsSrcRatesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SourceBook:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  Rate Type id of related RateType.  */  
   RateTypeID:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Exchange Rate that will be used for this Rate Type.  */  
   ExchangeRate:number,
      /**  Internal field used to indicate whether or not the user modified the rates.  */  
   UserModified:boolean,
      /**  Internal field used to indicate if the system was unable to calcuate the rates.  If yes, the rates are in error.  If no, the rates are okay.  */  
   RateError:boolean,
      /**  Calculation Date  */  
   CalcDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Daily Average, Period End or None  */  
   DefaultMethod:string,
      /**  Indicates if the record is selected for retrieval of default values  */  
   Selected:boolean,
   Description:string,
   BitFlag:number,
   RateTypeIDDescription:string,
   SourceBookCurrencyCode:string,
   SourceBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtGenListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Generation Description  */  
   Description:string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   GenStatus:string,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   TgtBook:string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   TargetCOA:string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   IntermediateBookID:string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   ImmediateTrans:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   RemoteParent:boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   VantageDB:boolean,
      /**  Import/Export file name.  */  
   OutputFile:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   ConsolidationType:string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   AdjustMode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   ConsDefIDDescription:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  Indicates the base currency for the book  */  
   IntermediateBookIDCurrencyCode:string,
      /**  Descripiton of Book  */  
   IntermediateBookIDDescription:string,
      /**  The description or Name of this Chart of Accounts.  */  
   TargetCOADescription:string,
      /**  Indicates the base currency for the book  */  
   TgtBookCurrencyCode:string,
      /**  Descripiton of Book  */  
   TgtBookDescription:string,
      /**  Company Name  */  
   TgtCompanyName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtGenListTableset{
   ConsTgtGenList:Erp_Tablesets_ConsTgtGenListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConsTgtGenRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Generation Description  */  
   Description:string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   GenStatus:string,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   TgtBook:string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   TargetCOA:string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   IntermediateBookID:string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   ImmediateTrans:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   RemoteParent:boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   VantageDB:boolean,
      /**  Import/Export file name.  */  
   OutputFile:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   ConsolidationType:string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   AdjustMode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  */  
   EntryMode:string,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
      /**  LatestConsolidation  */  
   LatestConsolidation:boolean,
      /**  Closing periods parameter defined in Consolidation definition.  */  
   ClosingPeriods:number,
   BitFlag:number,
   ConsDefIDDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   IntermediateBookIDDescription:string,
   IntermediateBookIDCurrencyCode:string,
   TargetCOADescription:string,
   TgtBookCurrencyCode:string,
   TgtBookDescription:string,
   TgtCompanyName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsolidToParentTableset{
   ConsTgtGen:Erp_Tablesets_ConsTgtGenRow[],
   ConsSrcCtrl:Erp_Tablesets_ConsSrcCtrlRow[],
   ConsSrcRates:Erp_Tablesets_ConsSrcRatesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtConsolidToParentTableset{
   ConsTgtGen:Erp_Tablesets_ConsTgtGenRow[],
   ConsSrcCtrl:Erp_Tablesets_ConsSrcCtrlRow[],
   ConsSrcRates:Erp_Tablesets_ConsSrcRatesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param genID
   */  
export interface GetByID_input{
   genID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConsolidToParentTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConsolidToParentTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConsolidToParentTableset[],
}

   /** Required : 
      @param proposedConsDefID
      @param ds
   */  
export interface GetConsDefIDData_input{
      /**  The proposed Consolidation Definition ID  */  
   proposedConsDefID:string,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface GetConsDefIDData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param ipGenID
      @param ipSourceBook
      @param ipGetDefaultType
      @param ds
   */  
export interface GetDefaults_input{
      /**  The Generation ID  */  
   ipGenID:number,
      /**  The Source Book  */  
   ipSourceBook:string,
      /**  GetDefault Type. 1 - All, 2 - Just record in screen.  */  
   ipGetDefaultType:number,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface GetDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
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
   returnObj:Erp_Tablesets_ConsTgtGenListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param genID
   */  
export interface GetNewConsSrcCtrl_input{
   ds:Erp_Tablesets_ConsolidToParentTableset[],
   genID:number,
}

export interface GetNewConsSrcCtrl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param ds
      @param genID
      @param sourceBook
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
   */  
export interface GetNewConsSrcRates_input{
   ds:Erp_Tablesets_ConsolidToParentTableset[],
   genID:number,
   sourceBook:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
}

export interface GetNewConsSrcRates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param EntryMode
      @param ds
   */  
export interface GetNewConsTgtGenEntryMode_input{
      /**  The Entry Mode  */  
   EntryMode:string,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface GetNewConsTgtGenEntryMode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewConsTgtGen_input{
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface GetNewConsTgtGen_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param whereClauseConsTgtGen
      @param whereClauseConsSrcCtrl
      @param whereClauseConsSrcRates
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseConsTgtGen:string,
   whereClauseConsSrcCtrl:string,
   whereClauseConsSrcRates:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConsolidToParentTableset[],
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
      @param GenID
      @param SourceBook
      @param Option
      @param ds
   */  
export interface RecalculateRates_input{
   GenID:number,
   SourceBook:string,
   Option:number,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface RecalculateRates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param ipcMethod
      @param ipcGenId
      @param ipcSourceBook
      @param ipcMsg
   */  
export interface SendErrorMsg_input{
      /**  The Generation Method  */  
   ipcMethod:string,
      /**  The Consolidation ID  */  
   ipcGenId:string,
      /**  The Source Book  */  
   ipcSourceBook:string,
      /**  The message to send  */  
   ipcMsg:string,
}

export interface SendErrorMsg_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConsolidToParentTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConsolidToParentTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param proposedClosingPeriods
      @param ipCalledFromUI
   */  
export interface ValidateClosingPeriods_input{
   ipFiscalCalendarID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
   proposedClosingPeriods:number,
   ipCalledFromUI:boolean,
}

export interface ValidateClosingPeriods_output{
parameters : {
      /**  output parameters  */  
   opcMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateExchangeRate_input{
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface ValidateExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param ipcompany
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param proposedFiscalPeriod
      @param ipCalledFromUI
   */  
export interface ValidateFiscalPeriod_input{
      /**  The Company ID  */  
   ipcompany:string,
      /**  The Fiscal Calendar ID  */  
   ipFiscalCalendarID:string,
      /**  The Fiscal Year  */  
   ipFiscalYear:number,
      /**  The Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  The FIscal Period  */  
   proposedFiscalPeriod:number,
      /**  Indicates if this method was called from the UI  */  
   ipCalledFromUI:boolean,
}

export interface ValidateFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   opcMsg:string,
}
}

   /** Required : 
      @param ipFiscalCalendarID
      @param proposedFiscalYear
      @param ipCalledFromUI
   */  
export interface ValidateFiscalYear_input{
      /**  The Fiscal Calendar ID  */  
   ipFiscalCalendarID:string,
      /**  The Fiscal Year  */  
   proposedFiscalYear:number,
      /**  Indicates if this method was called from the UI  */  
   ipCalledFromUI:boolean,
}

export interface ValidateFiscalYear_output{
parameters : {
      /**  output parameters  */  
   opFiscalYearSuffix:string,
   opcMsg:string,
}
}

   /** Required : 
      @param proposedFiscalYear
      @param ds
      @param ipCalledFromUI
      @param entryMode
   */  
export interface ValidateFiscalYearandGetPeriods_input{
      /**  The Fiscal Year  */  
   proposedFiscalYear:number,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
      /**  Indicates if this method was called from the UI  */  
   ipCalledFromUI:boolean,
      /**  Consolidation Entry Mode  */  
   entryMode:string,
}

export interface ValidateFiscalYearandGetPeriods_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
   opcMsg:string,
}
}

   /** Required : 
      @param intGenID
   */  
export interface ValidateGenID_input{
   intGenID:number,
}

export interface ValidateGenID_output{
parameters : {
      /**  output parameters  */  
   Recalculate:boolean,
}
}

   /** Required : 
      @param genID
      @param sourceBook
      @param consDefID
   */  
export interface ValidateLastConsol_input{
      /**  Consolidation ID  */  
   genID:number,
      /**  Source Book  */  
   sourceBook:string,
      /**  Consolidation Definition ID  */  
   consDefID:string,
}

export interface ValidateLastConsol_output{
   returnObj:boolean,
}

   /** Required : 
      @param intYear
      @param txtFiscalYearSuffix
      @param intPeriod
      @param ds
   */  
export interface ValidatePrevRecords_input{
      /**  Fiscal Year  */  
   intYear:number,
      /**  Fiscal Year Suffix  */  
   txtFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   intPeriod:number,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface ValidatePrevRecords_output{
parameters : {
      /**  output parameters  */  
   txtPriorPeriodNotPostedMsg:string,
   txtPeriodAlreadyPostedMsg:string,
   txtPeriodAlreadyGeneratedMsg:string,
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

export interface ValidateRateGroupStatus_output{
parameters : {
      /**  output parameters  */  
   strInactiveRateType:string,
}
}

   /** Required : 
      @param proposedAdjustFromFiscalPeriod
      @param ds
   */  
export interface ValidateSrcAdjustFromFiscalPeriod_input{
      /**  The proposed Adjust From Fiscal Year  */  
   proposedAdjustFromFiscalPeriod:number,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface ValidateSrcAdjustFromFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
}
}

   /** Required : 
      @param proposedFiscalPeriod
      @param ds
   */  
export interface ValidateSrcFiscalPeriod_input{
      /**  The proposed fiscal period  */  
   proposedFiscalPeriod:number,
   ds:Erp_Tablesets_ConsolidToParentTableset[],
}

export interface ValidateSrcFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsolidToParentTableset,
   opcMsg:string,
   opClosingPeriod:number,
}
}

