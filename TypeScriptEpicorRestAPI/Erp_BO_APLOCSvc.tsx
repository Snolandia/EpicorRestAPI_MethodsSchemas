import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APLOCSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/$metadata", {
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
   Description: Get APLOCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APLOCs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCRow
   */  
export function get_APLOCs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APLOCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APLOCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APLOCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APLOCs(requestBody:Erp_Tablesets_APLOCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APLOC item
   Description: Calls GetByID to retrieve the APLOC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APLOC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APLOCRow
   */  
export function get_APLOCs_Company_LCID(Company:string, LCID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APLOCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")", {
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
         resolve(data as Erp_Tablesets_APLOCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APLOC for the service
   Description: Calls UpdateExt to update APLOC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APLOC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APLOCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APLOCs_Company_LCID(Company:string, LCID:string, requestBody:Erp_Tablesets_APLOCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")", {
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
   Summary: Call UpdateExt to delete APLOC item
   Description: Call UpdateExt to delete APLOC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APLOC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APLOCs_Company_LCID(Company:string, LCID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")", {
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
   Description: Get APLOCAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APLOCAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCAttchRow
   */  
export function get_APLOCs_Company_LCID_APLOCAttches(Company:string, LCID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")/APLOCAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APLOCAttch item
   Description: Calls GetByID to retrieve the APLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APLOCAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APLOCAttchRow
   */  
export function get_APLOCs_Company_LCID_APLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_APLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APLOCAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APLOCAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCAttchRow
   */  
export function get_APLOCAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APLOCAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APLOCAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APLOCAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APLOCAttches(requestBody:Erp_Tablesets_APLOCAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APLOCAttch item
   Description: Calls GetByID to retrieve the APLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APLOCAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APLOCAttchRow
   */  
export function get_APLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_APLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APLOCAttch for the service
   Description: Calls UpdateExt to update APLOCAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APLOCAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APLOCAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, requestBody:Erp_Tablesets_APLOCAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete APLOCAttch item
   Description: Call UpdateExt to delete APLOCAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APLOCAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCListRow)
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
export function get_GetRows(whereClauseAPLOC:string, whereClauseAPLOCAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPLOC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPLOC=" + whereClauseAPLOC
   }
   if(typeof whereClauseAPLOCAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPLOCAttch=" + whereClauseAPLOCAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetRows" + params, {
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
export function get_GetByID(lcID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof lcID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lcID=" + lcID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetList" + params, {
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
   Summary: Invoke method ChangeCurrencyCode
   Description: Called when the CurrencyCode field has been changed.
   OperationID: ChangeCurrencyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyCode(requestBody:ChangeCurrencyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCurrencyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/ChangeCurrencyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCurrencyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeIssueDate
   Description: Called when the IssueDate field has been changed.
   OperationID: ChangeIssueDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeIssueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIssueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeIssueDate(requestBody:ChangeIssueDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeIssueDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/ChangeIssueDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeIssueDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDocLCValue
   Description: Called when the DocLCValue field has been changed.
   OperationID: ChangeDocLCValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDocLCValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDocLCValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDocLCValue(requestBody:ChangeDocLCValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDocLCValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/ChangeDocLCValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDocLCValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeExchangeRate
   Description: Called when the ExchangeRate field has been changed.
   OperationID: ChangeExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeExchangeRate(requestBody:ChangeExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/ChangeExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUseExchangeRate
   Description: Called when the Use ExchangeRate field has been changed.
   OperationID: ChangeUseExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUseExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUseExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUseExchangeRate(requestBody:ChangeUseExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUseExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/ChangeUseExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeUseExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPLOCInvc
   Description: This method will retrieve all the information related to AP Invoices
   OperationID: GetAPLOCInvc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAPLOCInvc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCInvc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPLOCInvc(requestBody:GetAPLOCInvc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPLOCInvc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetAPLOCInvc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetAPLOCInvc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPLOCPO
   Description: This method will retrieve all the information related to Purchase Orders.
   OperationID: GetAPLOCPO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAPLOCPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPLOCPO(requestBody:GetAPLOCPO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPLOCPO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetAPLOCPO", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetAPLOCPO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfCurrencyCode
   Description: Called when the CurrencyCode field is changing.
   OperationID: OnChangeOfCurrencyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfCurrencyCode(requestBody:OnChangeOfCurrencyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfCurrencyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/OnChangeOfCurrencyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfCurrencyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfFromDate
   Description: Called when changing the FromDate field.
   OperationID: OnChangeOfFromDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfFromDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFromDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfFromDate(requestBody:OnChangeOfFromDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfFromDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/OnChangeOfFromDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfFromDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfUseExchangeRate
   Description: Called when changing the FromDate field.
   OperationID: OnChangeOfUseExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfUseExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfUseExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfUseExchangeRate(requestBody:OnChangeOfUseExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfUseExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/OnChangeOfUseExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfUseExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfLCValue
   Description: Called when changing the LCValue field.
   OperationID: OnChangeOfLCValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfLCValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLCValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLCValue(requestBody:OnChangeOfLCValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfLCValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/OnChangeOfLCValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfLCValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfToDate
   Description: Called when changing the ToDate field.
   OperationID: OnChangeOfToDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfToDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfToDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfToDate(requestBody:OnChangeOfToDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfToDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/OnChangeOfToDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfToDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankAcctID
   Description: Called when changing the BankAcctId field.
   OperationID: OnChangeBankAcctID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankAcctID(requestBody:OnChangeBankAcctID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankAcctID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/OnChangeBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankAcctID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPLOC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPLOC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPLOC(requestBody:GetNewAPLOC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPLOC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetNewAPLOC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPLOC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPLOCAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPLOCAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPLOCAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPLOCAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPLOCAttch(requestBody:GetNewAPLOCAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPLOCAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetNewAPLOCAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPLOCAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APLOCAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APLOCListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APLOCRow,
}

export interface Erp_Tablesets_APLOCAttchRow{
   "Company":string,
   "LCID":string,
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

export interface Erp_Tablesets_APLOCListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Letter of Credit ID.  */  
   "LCID":string,
      /**  BankAcct ID.  */  
   "BankAcctID":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Monetary value of the Letter of Credit.  */  
   "LCValue":number,
      /**  Letter of Credit Value for report currency 1.  */  
   "Rpt1LCValue":number,
      /**  Letter of Credit Value for report currency 2.  */  
   "Rpt2LCValue":number,
      /**  Letter of Credit Value for report currency 3.  */  
   "Rpt3LCValue":number,
      /**  Letter of Credit Currency code  */  
   "CurrencyCode":string,
      /**  Exchange Rate.  */  
   "ExchangeRate":number,
      /**  Indicates a locked exchange rate.  */  
   "RateLocked":boolean,
      /**  Date that Letter of Credit was issued.  */  
   "IssueDate":string,
      /**  Valid From date.  */  
   "FromDate":string,
      /**  Valid To date.  */  
   "ToDate":string,
      /**  Letter of Credit Description.  */  
   "Description":string,
      /**  Bill to customer.  */  
   "BTCustNum":number,
      /**  Letter of Credit Terms.  */  
   "TermsCode":string,
      /**  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  */  
   "ShipComplete":boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   "Inactive":boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   "InactiveReason":string,
      /**  If true, Letter of Credit is closed.  */  
   "Closed":boolean,
      /**  Optional.  */  
   "FOB":string,
      /**  Free form text.  */  
   "IssuanceType":string,
      /**  Free form text.  */  
   "PackListCopies":string,
      /**  Free form text.  */  
   "PlaceOfLoading":string,
      /**  Free form text comments.  */  
   "Comment":string,
      /**  Unique identifier.  */  
   "RateGrpCode":string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   "DocLCValue":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BaseCurrencyID":string,
   "CurrencySwitch":boolean,
   "VendorID":string,
   "BaseCurrSymbol":string,
   "InUse":boolean,
      /**  Cumulative Invoice Value  */  
   "CumInValue":number,
      /**  Outstanding PO Value  */  
   "OutPOValue":number,
      /**  Remaining LC Value  */  
   "RemLCValue":number,
      /**  Invoice Balance  */  
   "InvoiceBal":number,
   "DocCumInValue":number,
   "Rpt1CumInValue":number,
   "Rpt2CumInValue":number,
   "Rpt3CumInValue":number,
   "DocRemLCValue":number,
   "Rpt1RemLCValue":number,
   "Rpt2RemLCValue":number,
   "Rpt3RemLCValue":number,
   "DocOutPOValue":number,
   "Rpt1OutPOValue":number,
   "Rpt2OutPOValue":number,
   "Rpt3OutPOValue":number,
   "DocInvoiceBal":number,
   "Rpt1InvoiceBal":number,
   "Rpt2InvoiceBal":number,
   "Rpt3InvoiceBal":number,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   "APTermsDescription":string,
      /**  Full description of the bank account.  */  
   "BankAcctDescription":string,
      /**  The Bank's full name.  */  
   "BankAcctBankName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrCurrSymbol":string,
      /**  Description of the currency  */  
   "BaseCurrCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrCurrName":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APLOCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Letter of Credit ID.  */  
   "LCID":string,
      /**  BankAcct ID.  */  
   "BankAcctID":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Monetary value of the Letter of Credit.  */  
   "LCValue":number,
      /**  Letter of Credit Value for report currency 1.  */  
   "Rpt1LCValue":number,
      /**  Letter of Credit Value for report currency 2.  */  
   "Rpt2LCValue":number,
      /**  Letter of Credit Value for report currency 3.  */  
   "Rpt3LCValue":number,
      /**  Letter of Credit Currency code  */  
   "CurrencyCode":string,
      /**  Exchange Rate.  */  
   "ExchangeRate":number,
      /**  Indicates a locked exchange rate.  */  
   "RateLocked":boolean,
      /**  Date that Letter of Credit was issued.  */  
   "IssueDate":string,
      /**  Valid From date.  */  
   "FromDate":string,
      /**  Valid To date.  */  
   "ToDate":string,
      /**  Letter of Credit Description.  */  
   "Description":string,
      /**  Bill to customer.  */  
   "BTCustNum":number,
      /**  Letter of Credit Terms.  */  
   "TermsCode":string,
      /**  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  */  
   "ShipComplete":boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   "Inactive":boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   "InactiveReason":string,
      /**  If true, Letter of Credit is closed.  */  
   "Closed":boolean,
      /**  Optional.  */  
   "FOB":string,
      /**  Free form text.  */  
   "IssuanceType":string,
      /**  Free form text.  */  
   "PackListCopies":string,
      /**  Free form text.  */  
   "PlaceOfLoading":string,
      /**  Free form text comments.  */  
   "Comment":string,
      /**  Unique identifier.  */  
   "RateGrpCode":string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   "DocLCValue":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BaseCurrencyID":string,
   "CurrencySwitch":boolean,
   "VendorID":string,
   "BaseCurrSymbol":string,
   "InUse":boolean,
      /**  Cumulative Invoice Value  */  
   "CumInValue":number,
      /**  Outstanding PO Value  */  
   "OutPOValue":number,
      /**  Remaining LC Value  */  
   "RemLCValue":number,
      /**  Invoice Balance  */  
   "InvoiceBal":number,
   "DocCumInValue":number,
   "Rpt1CumInValue":number,
   "Rpt2CumInValue":number,
   "Rpt3CumInValue":number,
   "DocRemLCValue":number,
   "Rpt1RemLCValue":number,
   "Rpt2RemLCValue":number,
   "Rpt3RemLCValue":number,
   "DocOutPOValue":number,
   "Rpt1OutPOValue":number,
   "Rpt2OutPOValue":number,
   "Rpt3OutPOValue":number,
   "DocInvoiceBal":number,
   "Rpt1InvoiceBal":number,
   "Rpt2InvoiceBal":number,
   "Rpt3InvoiceBal":number,
      /**  Use to choose which Exchange Rate will be use either Letter of Credit's or current.  */  
   "UseExchangeRate":string,
   "BitFlag":number,
   "APTermsDescription":string,
   "BankAcctBankName":string,
   "BankAcctDescription":string,
   "BaseCurrDocumentDesc":string,
   "BaseCurrCurrencyID":string,
   "BaseCurrCurrDesc":string,
   "BaseCurrCurrName":string,
   "BaseCurrCurrSymbol":string,
   "CurrencyCodeBaseCurr":boolean,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "ReasonDescription":string,
   "VendorVendorID":string,
   "VendorName":string,
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
export interface ChangeCurrencyCode_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface ChangeCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDocLCValue_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface ChangeDocLCValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeExchangeRate_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface ChangeExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeIssueDate_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface ChangeIssueDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUseExchangeRate_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface ChangeUseExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param lcID
   */  
export interface DeleteByID_input{
   lcID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APLOCAttchRow{
   Company:string,
   LCID:string,
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

export interface Erp_Tablesets_APLOCInvcRow{
   InvoiceAmt:number,
   InvoiceBal:number,
      /**  Field required for the grid of APLOCTracker Invoices.  */  
   InvoiceNum:string,
   LegalNumber:string,
   OpenPayable:boolean,
   DocInvoiceAmt:number,
   Rpt1InvoiceAmt:number,
   Rpt2InvoiceAmt:number,
   Rpt3InvoiceAmt:number,
   DocInvoiceBal:number,
   Rpt1InvoiceBal:number,
   Rpt2InvoiceBal:number,
   Rpt3InvoiceBal:number,
   CurrencyCode:string,
   CurrencyName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APLOCListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Letter of Credit ID.  */  
   LCID:string,
      /**  BankAcct ID.  */  
   BankAcctID:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Monetary value of the Letter of Credit.  */  
   LCValue:number,
      /**  Letter of Credit Value for report currency 1.  */  
   Rpt1LCValue:number,
      /**  Letter of Credit Value for report currency 2.  */  
   Rpt2LCValue:number,
      /**  Letter of Credit Value for report currency 3.  */  
   Rpt3LCValue:number,
      /**  Letter of Credit Currency code  */  
   CurrencyCode:string,
      /**  Exchange Rate.  */  
   ExchangeRate:number,
      /**  Indicates a locked exchange rate.  */  
   RateLocked:boolean,
      /**  Date that Letter of Credit was issued.  */  
   IssueDate:string,
      /**  Valid From date.  */  
   FromDate:string,
      /**  Valid To date.  */  
   ToDate:string,
      /**  Letter of Credit Description.  */  
   Description:string,
      /**  Bill to customer.  */  
   BTCustNum:number,
      /**  Letter of Credit Terms.  */  
   TermsCode:string,
      /**  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  */  
   ShipComplete:boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   Inactive:boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   InactiveReason:string,
      /**  If true, Letter of Credit is closed.  */  
   Closed:boolean,
      /**  Optional.  */  
   FOB:string,
      /**  Free form text.  */  
   IssuanceType:string,
      /**  Free form text.  */  
   PackListCopies:string,
      /**  Free form text.  */  
   PlaceOfLoading:string,
      /**  Free form text comments.  */  
   Comment:string,
      /**  Unique identifier.  */  
   RateGrpCode:string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   DocLCValue:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrencyID:string,
   CurrencySwitch:boolean,
   VendorID:string,
   BaseCurrSymbol:string,
   InUse:boolean,
      /**  Cumulative Invoice Value  */  
   CumInValue:number,
      /**  Outstanding PO Value  */  
   OutPOValue:number,
      /**  Remaining LC Value  */  
   RemLCValue:number,
      /**  Invoice Balance  */  
   InvoiceBal:number,
   DocCumInValue:number,
   Rpt1CumInValue:number,
   Rpt2CumInValue:number,
   Rpt3CumInValue:number,
   DocRemLCValue:number,
   Rpt1RemLCValue:number,
   Rpt2RemLCValue:number,
   Rpt3RemLCValue:number,
   DocOutPOValue:number,
   Rpt1OutPOValue:number,
   Rpt2OutPOValue:number,
   Rpt3OutPOValue:number,
   DocInvoiceBal:number,
   Rpt1InvoiceBal:number,
   Rpt2InvoiceBal:number,
   Rpt3InvoiceBal:number,
      /**  Full description of terms....this is printed on purchase orders. Can't be blank.  */  
   APTermsDescription:string,
      /**  Full description of the bank account.  */  
   BankAcctDescription:string,
      /**  The Bank's full name.  */  
   BankAcctBankName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrCurrSymbol:string,
      /**  Description of the currency  */  
   BaseCurrCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrCurrName:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APLOCListTableset{
   APLOCList:Erp_Tablesets_APLOCListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APLOCPORow{
   OpenOrder:boolean,
      /**  Temp Table required by the APLOCTracker Dataset  */  
   PONum:number,
      /**  the value of open unreceived goods + value of received but unmatched to invoice goods.  */  
   OutstdValue:number,
   CurrencyCode:string,
      /**  Currency Name  */  
   CurrencyName:string,
   DocOutstdValue:number,
   Rpt1OutstdValue:number,
   Rpt2OutstdValue:number,
   Rpt3OutstdValue:number,
      /**  Total Order form PO  */  
   TotalOrder:number,
   DocTotalOrder:number,
      /**  Total Order form PO  */  
   Rpt1TotalOrder:number,
      /**  Total Order form PO  */  
   Rpt2TotalOrder:number,
      /**  Total Order form PO  */  
   Rpt3TotalOrder:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APLOCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Letter of Credit ID.  */  
   LCID:string,
      /**  BankAcct ID.  */  
   BankAcctID:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Monetary value of the Letter of Credit.  */  
   LCValue:number,
      /**  Letter of Credit Value for report currency 1.  */  
   Rpt1LCValue:number,
      /**  Letter of Credit Value for report currency 2.  */  
   Rpt2LCValue:number,
      /**  Letter of Credit Value for report currency 3.  */  
   Rpt3LCValue:number,
      /**  Letter of Credit Currency code  */  
   CurrencyCode:string,
      /**  Exchange Rate.  */  
   ExchangeRate:number,
      /**  Indicates a locked exchange rate.  */  
   RateLocked:boolean,
      /**  Date that Letter of Credit was issued.  */  
   IssueDate:string,
      /**  Valid From date.  */  
   FromDate:string,
      /**  Valid To date.  */  
   ToDate:string,
      /**  Letter of Credit Description.  */  
   Description:string,
      /**  Bill to customer.  */  
   BTCustNum:number,
      /**  Letter of Credit Terms.  */  
   TermsCode:string,
      /**  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  */  
   ShipComplete:boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   Inactive:boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   InactiveReason:string,
      /**  If true, Letter of Credit is closed.  */  
   Closed:boolean,
      /**  Optional.  */  
   FOB:string,
      /**  Free form text.  */  
   IssuanceType:string,
      /**  Free form text.  */  
   PackListCopies:string,
      /**  Free form text.  */  
   PlaceOfLoading:string,
      /**  Free form text comments.  */  
   Comment:string,
      /**  Unique identifier.  */  
   RateGrpCode:string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   DocLCValue:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrencyID:string,
   CurrencySwitch:boolean,
   VendorID:string,
   BaseCurrSymbol:string,
   InUse:boolean,
      /**  Cumulative Invoice Value  */  
   CumInValue:number,
      /**  Outstanding PO Value  */  
   OutPOValue:number,
      /**  Remaining LC Value  */  
   RemLCValue:number,
      /**  Invoice Balance  */  
   InvoiceBal:number,
   DocCumInValue:number,
   Rpt1CumInValue:number,
   Rpt2CumInValue:number,
   Rpt3CumInValue:number,
   DocRemLCValue:number,
   Rpt1RemLCValue:number,
   Rpt2RemLCValue:number,
   Rpt3RemLCValue:number,
   DocOutPOValue:number,
   Rpt1OutPOValue:number,
   Rpt2OutPOValue:number,
   Rpt3OutPOValue:number,
   DocInvoiceBal:number,
   Rpt1InvoiceBal:number,
   Rpt2InvoiceBal:number,
   Rpt3InvoiceBal:number,
      /**  Use to choose which Exchange Rate will be use either Letter of Credit's or current.  */  
   UseExchangeRate:string,
   BitFlag:number,
   APTermsDescription:string,
   BankAcctBankName:string,
   BankAcctDescription:string,
   BaseCurrDocumentDesc:string,
   BaseCurrCurrencyID:string,
   BaseCurrCurrDesc:string,
   BaseCurrCurrName:string,
   BaseCurrCurrSymbol:string,
   CurrencyCodeBaseCurr:boolean,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   ReasonDescription:string,
   VendorVendorID:string,
   VendorName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APLOCTableset{
   APLOC:Erp_Tablesets_APLOCRow[],
   APLOCAttch:Erp_Tablesets_APLOCAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APLOCTrackerTableset{
   APLOCInvc:Erp_Tablesets_APLOCInvcRow[],
   APLOCPO:Erp_Tablesets_APLOCPORow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtAPLOCTableset{
   APLOC:Erp_Tablesets_APLOCRow[],
   APLOCAttch:Erp_Tablesets_APLOCAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param aplocid
      @param ds
   */  
export interface GetAPLOCInvc_input{
      /**  AP Letters Of Credit ID  */  
   aplocid:string,
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface GetAPLOCInvc_output{
   returnObj:Erp_Tablesets_APLOCTrackerTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param aplocid
      @param ds
   */  
export interface GetAPLOCPO_input{
      /**  AP Letters Of Credit ID  */  
   aplocid:string,
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface GetAPLOCPO_output{
   returnObj:Erp_Tablesets_APLOCTrackerTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param lcID
   */  
export interface GetByID_input{
   lcID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APLOCTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APLOCTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APLOCTableset[],
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
   returnObj:Erp_Tablesets_APLOCListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param lcID
   */  
export interface GetNewAPLOCAttch_input{
   ds:Erp_Tablesets_APLOCTableset[],
   lcID:string,
}

export interface GetNewAPLOCAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAPLOC_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface GetNewAPLOC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param whereClauseAPLOC
      @param whereClauseAPLOCAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPLOC:string,
   whereClauseAPLOCAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APLOCTableset[],
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
      @param pcBankAcctID
      @param ds
   */  
export interface OnChangeBankAcctID_input{
      /**  The proposed value of BankAcctID.  */  
   pcBankAcctID:string,
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface OnChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfCurrencyCode_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface OnChangeOfCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param proposedFromDate
      @param ds
   */  
export interface OnChangeOfFromDate_input{
      /**  Proposed From Date  */  
   proposedFromDate:string,
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface OnChangeOfFromDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param proposedLCValue
      @param ds
   */  
export interface OnChangeOfLCValue_input{
      /**  Proposed LCValue  */  
   proposedLCValue:number,
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface OnChangeOfLCValue_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param proposedToDate
      @param ds
   */  
export interface OnChangeOfToDate_input{
      /**  Proposed To Date  */  
   proposedToDate:string,
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface OnChangeOfToDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param proposedFromUseExchangeRate
      @param ds
   */  
export interface OnChangeOfUseExchangeRate_input{
      /**  Proposed From Date  */  
   proposedFromUseExchangeRate:string,
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface OnChangeOfUseExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAPLOCTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPLOCTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APLOCTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APLOCTableset,
}
}

