import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ConsTgtDefSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/$metadata", {
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
   Description: Get ConsTgtDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtDefs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefRow
   */  
export function get_ConsTgtDefs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtDefs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ConsTgtDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsTgtDefs(requestBody:Erp_Tablesets_ConsTgtDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ConsTgtDef item
   Description: Calls GetByID to retrieve the ConsTgtDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsTgtDefRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID(Company:string, ConsDefID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", {
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
         resolve(data as Erp_Tablesets_ConsTgtDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsTgtDef for the service
   Description: Calls UpdateExt to update ConsTgtDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsTgtDefs_Company_ConsDefID(Company:string, ConsDefID:string, requestBody:Erp_Tablesets_ConsTgtDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", {
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
   Summary: Call UpdateExt to delete ConsTgtDef item
   Description: Call UpdateExt to delete ConsTgtDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsTgtDefs_Company_ConsDefID(Company:string, ConsDefID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", {
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
   Description: Get ConsTgtSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtSrcs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs(Company:string, ConsDefID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
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
         resolve(data as Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtSrcs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtSrcs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtSrcs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ConsTgtSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsTgtSrcs(requestBody:Erp_Tablesets_ConsTgtSrcRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
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
         resolve(data as Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsTgtSrc for the service
   Description: Calls UpdateExt to update ConsTgtSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, requestBody:Erp_Tablesets_ConsTgtSrcRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
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
   Summary: Call UpdateExt to delete ConsTgtSrc item
   Description: Call UpdateExt to delete ConsTgtSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefListRow)
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
export function get_GetRows(whereClauseConsTgtDef:string, whereClauseConsTgtSrc:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseConsTgtDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsTgtDef=" + whereClauseConsTgtDef
   }
   if(typeof whereClauseConsTgtSrc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsTgtSrc=" + whereClauseConsTgtSrc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetRows" + params, {
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
export function get_GetByID(consDefID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof consDefID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "consDefID=" + consDefID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetList" + params, {
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
   Summary: Invoke method CheckCOAMap
   Description: Purpose:
Parameters:
<param name="ipCOAMapUID">COA Map ID to validate</param><param name="ipSourceCOA">COA for the Source Book</param><param name="ipTargetCOA">COA for the Intermediate Book if any</param>
Notes:
   OperationID: CheckCOAMap
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCOAMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOAMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCOAMap(requestBody:CheckCOAMap_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCOAMap_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckCOAMap", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckCOAMap_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckConsolidationType
   Description: Purpose:
Parameters:
<param name="ipConsolidationType">proposed consolidation type (Periodic/Continuous)</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckConsolidationType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckConsolidationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsolidationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConsolidationType(requestBody:CheckConsolidationType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckConsolidationType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckConsolidationType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckConsolidationType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckConsType
   Description: Purpose:
Parameters:
<param name="ipConsType">ConsType to edit</param><param name="ipConsTypeText">text that identifies the constype being validated</param>
Notes:
   OperationID: CheckConsType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckConsType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConsType(requestBody:CheckConsType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckConsType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckConsType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckConsType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCurrencyCode
   Description: Purpose:
Parameters:
<param name="ipCurrencyCode">currency code to validate</param>
Notes:
   OperationID: CheckCurrencyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrencyCode(requestBody:CheckCurrencyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCurrencyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckCurrencyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckCurrencyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckIfResetTgtBook
   Description: Purpose:
Parameters:
<param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckIfResetTgtBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckIfResetTgtBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfResetTgtBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfResetTgtBook(requestBody:CheckIfResetTgtBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckIfResetTgtBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckIfResetTgtBook", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckIfResetTgtBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckIntermediateBook
   Description: Purpose:
Parameters:
<param name="ipIntermediateBook">IntermediateBookID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckIntermediateBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckIntermediateBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIntermediateBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIntermediateBook(requestBody:CheckIntermediateBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckIntermediateBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckIntermediateBook", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckIntermediateBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckJournalCode
   Description: Purpose:
Parameters:
<param name="ipJrnlCode">Journal code to edit</param><param name="ipJrnlCodeType">Identifies which journal code to edit: target or intermediate</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckJournalCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckJournalCode(requestBody:CheckJournalCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckJournalCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckJournalCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckJournalCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOutputFile
   Description: Purpose:  Verify the outputfile is unqique
Parameters:
<param name="ipOutputFile">output file</param>
Notes:
   OperationID: CheckOutputFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckOutputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOutputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOutputFile(requestBody:CheckOutputFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckOutputFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckOutputFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckOutputFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRemoteParent
   Description: Purpose:
Parameters:
<param name="ipRemoteParent">remote parent value</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckRemoteParent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRemoteParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRemoteParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRemoteParent(requestBody:CheckRemoteParent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRemoteParent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckRemoteParent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRemoteParent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTargetBook
   Description: Purpose:
Parameters:
<param name="ipTargetBook">target book ID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckTargetBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTargetBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTargetBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTargetBook(requestBody:CheckTargetBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTargetBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckTargetBook", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckTargetBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTargetCompany
   Description: Purpose:
Parameters:
<param name="ipTargetCompany">target Company ID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckTargetCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTargetCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTargetCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTargetCompany(requestBody:CheckTargetCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTargetCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/CheckTargetCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckTargetCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSourceCOA
   Description: Purpose:  Updates the Source COA when the Source Book changes
Parameters:
<param name="ipSourceBook">Source GL Book ID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: GetSourceCOA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSourceCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSourceCOA(requestBody:GetSourceCOA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSourceCOA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetSourceCOA", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSourceCOA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsSourceBookDefined
   Description: Purpose:  Checks to see if the source book is already defined for this ConsDefID
Parameters:
<param name="ipConsDefID">Consolidation Definition ID</param><param name="ipSourceBook">Source GL Book ID</param>
Notes:
   OperationID: IsSourceBookDefined
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsSourceBookDefined_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsSourceBookDefined_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsSourceBookDefined(requestBody:IsSourceBookDefined_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsSourceBookDefined_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/IsSourceBookDefined", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsSourceBookDefined_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getCompaniesList
   Description: To get external companies configured for current company.
   OperationID: getCompaniesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/getCompaniesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getCompaniesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getCompaniesList(requestBody:getCompaniesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<getCompaniesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/getCompaniesList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as getCompaniesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultsOnAdd
   Description: Check if account is valid and set description for it
   OperationID: DefaultsOnAdd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultsOnAdd(requestBody:DefaultsOnAdd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultsOnAdd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/DefaultsOnAdd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultsOnAdd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForTargetBookCmb
   Description: Generates list of available target books in string format.
   OperationID: GetListForTargetBookCmb
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListForTargetBookCmb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTargetBookCmb_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForTargetBookCmb(requestBody:GetListForTargetBookCmb_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListForTargetBookCmb_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetListForTargetBookCmb", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListForTargetBookCmb_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForTargetJrnlCmb
   Description: Generates list of available target journals in string format.
   OperationID: GetListForTargetJrnlCmb
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListForTargetJrnlCmb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTargetJrnlCmb_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForTargetJrnlCmb(requestBody:GetListForTargetJrnlCmb_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListForTargetJrnlCmb_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetListForTargetJrnlCmb", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListForTargetJrnlCmb_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForCOAMapUIDCmb
   Description: Returns list of available COA Mappings
   OperationID: GetListForCOAMapUIDCmb
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListForCOAMapUIDCmb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForCOAMapUIDCmb_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForCOAMapUIDCmb(requestBody:GetListForCOAMapUIDCmb_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListForCOAMapUIDCmb_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetListForCOAMapUIDCmb", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListForCOAMapUIDCmb_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConsolidationTypeOnChanging
   Description: ConsolidationType Column changing.
   OperationID: ConsolidationTypeOnChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConsolidationTypeOnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConsolidationTypeOnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsolidationTypeOnChanging(requestBody:ConsolidationTypeOnChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConsolidationTypeOnChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsolidationTypeOnChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ConsolidationTypeOnChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConsTgtDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsTgtDef(requestBody:GetNewConsTgtDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewConsTgtDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetNewConsTgtDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewConsTgtDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConsTgtSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtSrc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsTgtSrc(requestBody:GetNewConsTgtSrc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewConsTgtSrc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetNewConsTgtSrc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewConsTgtSrc_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtDefListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtDefRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtSrcRow,
}

export interface Erp_Tablesets_ConsTgtDefListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   "Description":string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   "RemoteParent":boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   "VantageDB":boolean,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   "TgtBook":string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   "TargetCOA":string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   "ConsolidationType":string,
      /**  Import/Export file name.  */  
   "OutputFile":string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   "IntermediateBookID":string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   "ImmediateTrans":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   "AdjustMode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Target Book Fiscal Calendar  */  
   "TgtBookCal":string,
      /**  Intermediate book fiscal calendar  */  
   "IterBookFiscalCal":string,
      /**  Target Book fiscal Calendar  */  
   "TgtBookFiscalCal":string,
      /**  Target Book Description  */  
   "TgtBookDesc":string,
      /**  Intermediate COA Code  */  
   "IntermediateCOA":string,
      /**  Descripiton of Book  */  
   "InterBookDescription":string,
      /**  Indicates the base currency for the book  */  
   "InterBookCurrencyCode":string,
      /**  Company Name  */  
   "TargetCOName":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "TgtCOADescription":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "TgtCurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "TgtCurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "TgtCurrencyCurrName":string,
      /**  Description of the currency  */  
   "TgtCurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "TgtCurrencyCurrSymbol":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtDefRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   "Description":string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   "RemoteParent":boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   "VantageDB":boolean,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   "TgtBook":string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   "TargetCOA":string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   "ConsolidationType":string,
      /**  Import/Export file name.  */  
   "OutputFile":string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   "IntermediateBookID":string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   "ImmediateTrans":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   "AdjustMode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Target Book Fiscal Calendar  */  
   "TgtBookCal":string,
      /**  Intermediate book fiscal calendar  */  
   "IterBookFiscalCal":string,
      /**  Target Book fiscal Calendar  */  
   "TgtBookFiscalCal":string,
      /**  Target Book Description  */  
   "TgtBookDesc":string,
      /**  Intermediate COA Code  */  
   "IntermediateCOA":string,
      /**  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  */  
   "AdjustModeInput":boolean,
      /**  Source Company  */  
   "SrcCompany":string,
      /**  Source Company Name  */  
   "SrcCompanyName":string,
      /**  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  */  
   "HasConsolitation":boolean,
      /**  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  */  
   "LastGenStatus":string,
      /**  Intermediate book fiscal calendar ID.  */  
   "IterBookFiscalCalID":string,
      /**  Target Book fiscal Calendar ID.  */  
   "TgtBookFiscalCalID":string,
   "BitFlag":number,
   "InterBookCurrencyCode":string,
   "InterBookDescription":string,
   "TargetCOName":string,
   "TgtCOADescription":string,
   "TgtCurrencyCurrName":string,
   "TgtCurrencyCurrSymbol":string,
   "TgtCurrencyCurrencyID":string,
   "TgtCurrencyDocumentDesc":string,
   "TgtCurrencyCurrDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtSrcRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SourceBook":string,
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
      /**  Account Number where rounding differences will be posted  */  
   "DiffOnExchangeAcct":string,
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Target COA - this field is intended for internal use  */  
   "TargetCOA":string,
      /**  Target Company ID - intended for internal use  */  
   "TargetCompany":string,
      /**  Source COA code  */  
   "SourceCOA":string,
      /**  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   "InterJrnlDesc":string,
      /**  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   "TgtJrnlCodeDesc":string,
      /**  Currency code description from either the Currency or GLBCurrency table.  */  
   "CurrencyDesc":string,
      /**  Source book fiscal calendar.  */  
   "SrcFiscalCalendar":string,
      /**  Holds GLAccount description temporarily to provide extra information to the user.  */  
   "DiffOnExchangeDesc":string,
      /**  Intermediate COA Code  */  
   "IntermediateCOA":string,
   "BitFlag":number,
   "BalanceConsTypeDescription":string,
   "BalanceRateDescription":string,
   "COAMapDisplayName":string,
   "IncomeConsTypeDescription":string,
   "IncomeRateDescription":string,
   "SrcBookDescription":string,
   "SrcBookCurrencyCode":string,
   "SrcCompanyName":string,
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
      @param ipCOAMapUID
      @param ipSourceCOA
      @param ipTargetCOA
   */  
export interface CheckCOAMap_input{
   ipCOAMapUID:number,
   ipSourceCOA:string,
   ipTargetCOA:string,
}

export interface CheckCOAMap_output{
}

   /** Required : 
      @param ipConsType
      @param ipConsTypeText
   */  
export interface CheckConsType_input{
   ipConsType:string,
   ipConsTypeText:string,
}

export interface CheckConsType_output{
}

   /** Required : 
      @param ipConsolidationType
      @param ds
   */  
export interface CheckConsolidationType_input{
   ipConsolidationType:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface CheckConsolidationType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ipCurrencyCode
   */  
export interface CheckCurrencyCode_input{
   ipCurrencyCode:string,
}

export interface CheckCurrencyCode_output{
}

   /** Required : 
      @param ds
   */  
export interface CheckIfResetTgtBook_input{
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface CheckIfResetTgtBook_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ipIntermediateBook
      @param ds
   */  
export interface CheckIntermediateBook_input{
   ipIntermediateBook:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface CheckIntermediateBook_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ipJrnlCode
      @param ipJrnlCodeType
      @param ds
   */  
export interface CheckJournalCode_input{
   ipJrnlCode:string,
   ipJrnlCodeType:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface CheckJournalCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ipOutputFile
   */  
export interface CheckOutputFile_input{
   ipOutputFile:string,
}

export interface CheckOutputFile_output{
}

   /** Required : 
      @param ipRemoteParent
      @param ds
   */  
export interface CheckRemoteParent_input{
   ipRemoteParent:boolean,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface CheckRemoteParent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ipTargetBook
      @param ds
   */  
export interface CheckTargetBook_input{
   ipTargetBook:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface CheckTargetBook_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ipTargetCompany
      @param ds
   */  
export interface CheckTargetCompany_input{
   ipTargetCompany:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface CheckTargetCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ipConsolidationType
      @param ds
   */  
export interface ConsolidationTypeOnChanging_input{
   ipConsolidationType:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface ConsolidationTypeOnChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param glAccount
      @param ds
   */  
export interface DefaultsOnAdd_input{
      /**  GL Account being processed  */  
   glAccount:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface DefaultsOnAdd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param consDefID
   */  
export interface DeleteByID_input{
   consDefID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ConsTgtDefListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   Description:string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   RemoteParent:boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   VantageDB:boolean,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   TgtBook:string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   TargetCOA:string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   ConsolidationType:string,
      /**  Import/Export file name.  */  
   OutputFile:string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   IntermediateBookID:string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   ImmediateTrans:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   AdjustMode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Target Book Fiscal Calendar  */  
   TgtBookCal:string,
      /**  Intermediate book fiscal calendar  */  
   IterBookFiscalCal:string,
      /**  Target Book fiscal Calendar  */  
   TgtBookFiscalCal:string,
      /**  Target Book Description  */  
   TgtBookDesc:string,
      /**  Intermediate COA Code  */  
   IntermediateCOA:string,
      /**  Descripiton of Book  */  
   InterBookDescription:string,
      /**  Indicates the base currency for the book  */  
   InterBookCurrencyCode:string,
      /**  Company Name  */  
   TargetCOName:string,
      /**  The description or Name of this Chart of Accounts.  */  
   TgtCOADescription:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   TgtCurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   TgtCurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   TgtCurrencyCurrName:string,
      /**  Description of the currency  */  
   TgtCurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   TgtCurrencyCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtDefListTableset{
   ConsTgtDefList:Erp_Tablesets_ConsTgtDefListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConsTgtDefRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   Description:string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   RemoteParent:boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   VantageDB:boolean,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   TgtBook:string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   TargetCOA:string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   ConsolidationType:string,
      /**  Import/Export file name.  */  
   OutputFile:string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   IntermediateBookID:string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   ImmediateTrans:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   AdjustMode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Target Book Fiscal Calendar  */  
   TgtBookCal:string,
      /**  Intermediate book fiscal calendar  */  
   IterBookFiscalCal:string,
      /**  Target Book fiscal Calendar  */  
   TgtBookFiscalCal:string,
      /**  Target Book Description  */  
   TgtBookDesc:string,
      /**  Intermediate COA Code  */  
   IntermediateCOA:string,
      /**  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  */  
   AdjustModeInput:boolean,
      /**  Source Company  */  
   SrcCompany:string,
      /**  Source Company Name  */  
   SrcCompanyName:string,
      /**  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  */  
   HasConsolitation:boolean,
      /**  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  */  
   LastGenStatus:string,
      /**  Intermediate book fiscal calendar ID.  */  
   IterBookFiscalCalID:string,
      /**  Target Book fiscal Calendar ID.  */  
   TgtBookFiscalCalID:string,
   BitFlag:number,
   InterBookCurrencyCode:string,
   InterBookDescription:string,
   TargetCOName:string,
   TgtCOADescription:string,
   TgtCurrencyCurrName:string,
   TgtCurrencyCurrSymbol:string,
   TgtCurrencyCurrencyID:string,
   TgtCurrencyDocumentDesc:string,
   TgtCurrencyCurrDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtDefTableset{
   ConsTgtDef:Erp_Tablesets_ConsTgtDefRow[],
   ConsTgtSrc:Erp_Tablesets_ConsTgtSrcRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConsTgtSrcRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SourceBook:string,
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
      /**  Account Number where rounding differences will be posted  */  
   DiffOnExchangeAcct:string,
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Target COA - this field is intended for internal use  */  
   TargetCOA:string,
      /**  Target Company ID - intended for internal use  */  
   TargetCompany:string,
      /**  Source COA code  */  
   SourceCOA:string,
      /**  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   InterJrnlDesc:string,
      /**  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   TgtJrnlCodeDesc:string,
      /**  Currency code description from either the Currency or GLBCurrency table.  */  
   CurrencyDesc:string,
      /**  Source book fiscal calendar.  */  
   SrcFiscalCalendar:string,
      /**  Holds GLAccount description temporarily to provide extra information to the user.  */  
   DiffOnExchangeDesc:string,
      /**  Intermediate COA Code  */  
   IntermediateCOA:string,
   BitFlag:number,
   BalanceConsTypeDescription:string,
   BalanceRateDescription:string,
   COAMapDisplayName:string,
   IncomeConsTypeDescription:string,
   IncomeRateDescription:string,
   SrcBookDescription:string,
   SrcBookCurrencyCode:string,
   SrcCompanyName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtConsTgtDefTableset{
   ConsTgtDef:Erp_Tablesets_ConsTgtDefRow[],
   ConsTgtSrc:Erp_Tablesets_ConsTgtSrcRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param consDefID
   */  
export interface GetByID_input{
   consDefID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConsTgtDefTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConsTgtDefTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConsTgtDefTableset[],
}

   /** Required : 
      @param ipConsDefID
      @param ipSourceCOA
   */  
export interface GetListForCOAMapUIDCmb_input{
   ipConsDefID:string,
   ipSourceCOA:string,
}

export interface GetListForCOAMapUIDCmb_output{
   returnObj:string,
}

   /** Required : 
      @param ipCompany
      @param ipTgtCompany
      @param ipExtCompany
   */  
export interface GetListForTargetBookCmb_input{
   ipCompany:string,
   ipTgtCompany:string,
   ipExtCompany:string,
}

export interface GetListForTargetBookCmb_output{
   returnObj:string,
}

   /** Required : 
      @param ipCompany
      @param ipTgtCompany
      @param ipExtCompany
   */  
export interface GetListForTargetJrnlCmb_input{
   ipCompany:string,
   ipTgtCompany:string,
   ipExtCompany:string,
}

export interface GetListForTargetJrnlCmb_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_ConsTgtDefListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewConsTgtDef_input{
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface GetNewConsTgtDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param ds
      @param consDefID
   */  
export interface GetNewConsTgtSrc_input{
   ds:Erp_Tablesets_ConsTgtDefTableset[],
   consDefID:string,
}

export interface GetNewConsTgtSrc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param whereClauseConsTgtDef
      @param whereClauseConsTgtSrc
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseConsTgtDef:string,
   whereClauseConsTgtSrc:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConsTgtDefTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipSourceBook
      @param ds
   */  
export interface GetSourceCOA_input{
   ipSourceBook:string,
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface GetSourceCOA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
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
      @param ipConsDefID
      @param ipSourceBook
   */  
export interface IsSourceBookDefined_input{
   ipConsDefID:string,
   ipSourceBook:string,
}

export interface IsSourceBookDefined_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConsTgtDefTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConsTgtDefTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConsTgtDefTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsTgtDefTableset,
}
}

   /** Required : 
      @param consTypeSelected
   */  
export interface getCompaniesList_input{
   consTypeSelected:string,
}

export interface getCompaniesList_output{
      /**  String  */  
   returnObj:string,
}

