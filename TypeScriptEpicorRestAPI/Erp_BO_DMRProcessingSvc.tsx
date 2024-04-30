import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.DMRProcessingSvc
// Description: DMR Processing Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/$metadata", {
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
   Description: Get DMRProcessings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRProcessings
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadRow
   */  
export function get_DMRProcessings(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRProcessings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DMRHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DMRProcessings(requestBody:Erp_Tablesets_DMRHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DMRProcessing item
   Description: Calls GetByID to retrieve the DMRProcessing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRProcessing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DMRHeadRow
   */  
export function get_DMRProcessings_Company_DMRNum(Company:string, DMRNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DMRHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")", {
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
         resolve(data as Erp_Tablesets_DMRHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DMRProcessing for the service
   Description: Calls UpdateExt to update DMRProcessing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRProcessing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DMRProcessings_Company_DMRNum(Company:string, DMRNum:string, requestBody:Erp_Tablesets_DMRHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")", {
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
   Summary: Call UpdateExt to delete DMRProcessing item
   Description: Call UpdateExt to delete DMRProcessing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRProcessing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DMRProcessings_Company_DMRNum(Company:string, DMRNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")", {
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
   Description: Get DMRActns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DMRActns1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnRow
   */  
export function get_DMRProcessings_Company_DMRNum_DMRActns(Company:string, DMRNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRActns", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DMRActn item
   Description: Calls GetByID to retrieve the DMRActn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRActn1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param ActionNum Desc: ActionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DMRActnRow
   */  
export function get_DMRProcessings_Company_DMRNum_DMRActns_Company_DMRNum_ActionNum(Company:string, DMRNum:string, ActionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DMRActnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")", {
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
         resolve(data as Erp_Tablesets_DMRActnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DMRHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DMRHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadAttchRow
   */  
export function get_DMRProcessings_Company_DMRNum_DMRHeadAttches(Company:string, DMRNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DMRHeadAttch item
   Description: Calls GetByID to retrieve the DMRHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   */  
export function get_DMRProcessings_Company_DMRNum_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company:string, DMRNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DMRHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_DMRHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DMRActns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRActns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnRow
   */  
export function get_DMRActns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRActns
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DMRActnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DMRActns(requestBody:Erp_Tablesets_DMRActnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DMRActn item
   Description: Calls GetByID to retrieve the DMRActn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRActn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param ActionNum Desc: ActionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DMRActnRow
   */  
export function get_DMRActns_Company_DMRNum_ActionNum(Company:string, DMRNum:string, ActionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DMRActnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")", {
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
         resolve(data as Erp_Tablesets_DMRActnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DMRActn for the service
   Description: Calls UpdateExt to update DMRActn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRActn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param ActionNum Desc: ActionNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DMRActns_Company_DMRNum_ActionNum(Company:string, DMRNum:string, ActionNum:string, requestBody:Erp_Tablesets_DMRActnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")", {
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
   Summary: Call UpdateExt to delete DMRActn item
   Description: Call UpdateExt to delete DMRActn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRActn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param ActionNum Desc: ActionNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DMRActns_Company_DMRNum_ActionNum(Company:string, DMRNum:string, ActionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")", {
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
   Description: Get DMRHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadAttchRow
   */  
export function get_DMRHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRHeadAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DMRHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DMRHeadAttches(requestBody:Erp_Tablesets_DMRHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DMRHeadAttch item
   Description: Calls GetByID to retrieve the DMRHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   */  
export function get_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company:string, DMRNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DMRHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_DMRHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DMRHeadAttch for the service
   Description: Calls UpdateExt to update DMRHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company:string, DMRNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_DMRHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete DMRHeadAttch item
   Description: Call UpdateExt to delete DMRHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company:string, DMRNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDMRHead:string, whereClauseDMRHeadAttch:string, whereClauseDMRActn:string, whereClauseLegalNumGenOpts:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDMRHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDMRHead=" + whereClauseDMRHead
   }
   if(typeof whereClauseDMRHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDMRHeadAttch=" + whereClauseDMRHeadAttch
   }
   if(typeof whereClauseDMRActn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDMRActn=" + whereClauseDMRActn
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetRows" + params, {
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
export function get_GetByID(dmRNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof dmRNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dmRNum=" + dmRNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetList" + params, {
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
   Description: This method recalculates the exchange rate and base price when the currency code changes.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeCurrencyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ChangeExchangeRate
   Description: This method recalculates the base price when the exchange rate changes.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ChangeJobAsmSeq
   Description: This method initializes the job material sequence and accepted quantity
when the Job Assembly Sequence changes.
   OperationID: ChangeJobAsmSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobAsmSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobAsmSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobAsmSeq(requestBody:ChangeJobAsmSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobAsmSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeJobAsmSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeJobAsmSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobMtlSeq
   Description: This method initializes the IssuedComplete check box and defaults Warehouse
and Bin (if necessary) when the Job Material Sequence changes.
   OperationID: ChangeJobMtlSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobMtlSeq(requestBody:ChangeJobMtlSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobMtlSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeJobMtlSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeJobMtlSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobNum
   Description: This method initializes the job assembly/material sequences, accepted quantity
and the comment text when the Job Number changes.
   OperationID: ChangeJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobNum(requestBody:ChangeJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePackingSlip
   Description: This method retrieves information related to the packing slip where this material was originally received.
   OperationID: ChangePackingSlip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePackingSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackingSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePackingSlip(requestBody:ChangePackingSlip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePackingSlip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangePackingSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePackingSlip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePackingSlipLine
   Description: This method retrieves information related to the packing slip where this material was originally received.
   OperationID: ChangePackingSlipLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePackingSlipLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackingSlipLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePackingSlipLine(requestBody:ChangePackingSlipLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePackingSlipLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangePackingSlipLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePackingSlipLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRefInvoiceNum
   Description: This method validates Ref Invoice Number.
   OperationID: ChangeRefInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRefInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRefInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRefInvoiceNum(requestBody:ChangeRefInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRefInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeRefInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRefInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCID
   Description: Validates that PCID exists
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/OnChangePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method OnChangeResolution
   Description: This method check if there is an Invoice for the PONum/line.
   OperationID: OnChangeResolution
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeResolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeResolution(requestBody:OnChangeResolution_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeResolution_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/OnChangeResolution", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeResolution_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeStkWhs
   Description: This method initializes the serial tracking data when the Accept to Stock
warehoues changes, because a warehouse change might mean a "to" plant change
which can affect serial process under some circumstances.
Updates values of warehouse and primary bin (if any)
   OperationID: ChangeStkWhs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeStkWhs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStkWhs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStkWhs(requestBody:ChangeStkWhs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeStkWhs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeStkWhs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeStkWhs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUnitCredit
   Description: This method recalculates the base price when the doc price changes or recalculates
the doc price when the base price changes.  The CurrencySwitch flag in DMRActn is used to
determine which value to calculate.
   OperationID: ChangeUnitCredit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUnitCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUnitCredit(requestBody:ChangeUnitCredit_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUnitCredit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeUnitCredit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeUnitCredit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeWarehouse
   Description: This method will load the bin number only if one bin exists for the selected warehouse.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ChangeWarehouse", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method CheckIssueComplete
   Description: This method returns text of a message to be asked of the user when changing the
issue complete flag for Accepting to Job Materials.  The purpose of the question
is to verify the user wants to continue with the change.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckIssueComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckIssueComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIssueComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIssueComplete(requestBody:CheckIssueComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckIssueComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/CheckIssueComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckIssueComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckJobMtlSeq
   Description: This method returns a message for the user if the job material selected is already issued
complete. The user would then have the option to continue with the selected
job material or change the material sequence.
   OperationID: CheckJobMtlSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckJobMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJobMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckJobMtlSeq(requestBody:CheckJobMtlSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckJobMtlSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/CheckJobMtlSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckJobMtlSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPlanningContractBin
   Description: Method to check Contract bin.
   OperationID: CheckPlanningContractBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPlanningContractBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlanningContractBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPlanningContractBin(requestBody:CheckPlanningContractBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPlanningContractBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/CheckPlanningContractBin", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckPlanningContractBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOperationComplete
   Description: This method returns text of a message to be asked of the user when changing the
operation complete flag for Accepting to Job Operations.  The purpose of the question
is to verify the user wants to continue with the change.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckOperationComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckOperationComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOperationComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOperationComplete(requestBody:CheckOperationComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckOperationComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/CheckOperationComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckOperationComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRejectDisabled
   Description: This method returns the DMR Action Debit Memo created by this rejection.
   OperationID: CheckRejectDisabled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRejectDisabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRejectDisabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRejectDisabled(requestBody:CheckRejectDisabled_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRejectDisabled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/CheckRejectDisabled", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRejectDisabled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateDebitMemoNum
   Description: This method fills the DebitMemoNum from database.
   OperationID: UpdateDebitMemoNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateDebitMemoNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDebitMemoNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDebitMemoNum(requestBody:UpdateDebitMemoNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateDebitMemoNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/UpdateDebitMemoNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateDebitMemoNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CustomUpdate
   OperationID: CustomUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomUpdate(requestBody:CustomUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/CustomUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CustomUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultIssueComplete
   Description: This method defaults the appropriate value for the Issue Complete check box
whenever the quantity to be accepted to Job Material changes. Also defaults
the appropiate value for the Operation Complete check box whenever the quantity
to be accepted to Job Operation changes.
   OperationID: DefaultIssueComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultIssueComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultIssueComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultIssueComplete(requestBody:DefaultIssueComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultIssueComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DefaultIssueComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultIssueComplete_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/CheckCNCustomsDeclarationBillLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetContactInfo
   Description: This method updates the default Contact information when the ConNum field changes.
   OperationID: GetContactInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContactInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContactInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContactInfo(requestBody:GetContactInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContactInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetContactInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetContactInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrencyBase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetCurrencyBase", {
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
         resolve(data as GetCurrencyBase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDMRHistory
   Description: Get DMR history
   OperationID: GetDMRHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDMRHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDMRHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDMRHistory(requestBody:GetDMRHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDMRHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetDMRHistory", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDMRHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRActnAcceptMTL
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Material to Job Material) is created.  This method requires the DMR Number
as input parameter.  In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptMTL
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptMTL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptMTL_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActnAcceptMTL(requestBody:GetNewDMRActnAcceptMTL_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRActnAcceptMTL_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRActnAcceptMTL", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRActnAcceptMTL_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRActnAcceptOPR
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Material to Job Operation) is created.  This method requires the DMR Number
as input parameter.  In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptOPR
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptOPR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptOPR_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActnAcceptOPR(requestBody:GetNewDMRActnAcceptOPR_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRActnAcceptOPR_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRActnAcceptOPR", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRActnAcceptOPR_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRActnAcceptSTK
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Material to Stock) is created. This method requires the DMR Number as
the input parameter. In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptSTK
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptSTK_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptSTK_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActnAcceptSTK(requestBody:GetNewDMRActnAcceptSTK_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRActnAcceptSTK_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRActnAcceptSTK", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRActnAcceptSTK_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRActnAcceptCUST
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Return to Customer) is created. This method requires the DMR Number as
the input parameter. In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptCUST
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptCUST_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptCUST_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActnAcceptCUST(requestBody:GetNewDMRActnAcceptCUST_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRActnAcceptCUST_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRActnAcceptCUST", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRActnAcceptCUST_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRActnDebitMemo
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Requesting Debit Memo) is created.  This method requires the DMR Number as input
parameter. In addition, this method sets the external fields to indicate whether
certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnDebitMemo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnDebitMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnDebitMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActnDebitMemo(requestBody:GetNewDMRActnDebitMemo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRActnDebitMemo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRActnDebitMemo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRActnDebitMemo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRActnReject
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Rejecting Material) is created.  This method requires the DMR Number as input
parameter. In addition, this method sets the external fields to indicate whether
certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnReject
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActnReject(requestBody:GetNewDMRActnReject_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRActnReject_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRActnReject", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRActnReject_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPurPointInfo
   Description: This method updates Purchase Point default information when the PurPoint
field changes.
   OperationID: GetPurPointInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPurPointInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurPointInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPurPointInfo(requestBody:GetPurPointInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPurPointInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetPurPointInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPurPointInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetSelectSerialNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetVendorInfo
   Description: This method updates the default Vendor information when the VendorNumVendorID
field changes.
   OperationID: GetVendorInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorInfo(requestBody:GetVendorInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetVendorInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: This method does one thing.
1 . This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The requiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ReasonCodeWhereClause
   Description: This method returns the reason code where clause for searching for Reason codes
for DMR Rejections or Request of Debit Memos.
   OperationID: ReasonCodeWhereClause
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReasonCodeWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReasonCodeWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReasonCodeWhereClause(requestBody:ReasonCodeWhereClause_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReasonCodeWhereClause_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ReasonCodeWhereClause", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReasonCodeWhereClause_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/ValidateSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method GetNewDMRHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRHead(requestBody:GetNewDMRHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRHeadAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRHeadAttch(requestBody:GetNewDMRHeadAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRHeadAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRHeadAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDMRActn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRActn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDMRActn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActn(requestBody:GetNewDMRActn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDMRActn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetNewDMRActn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDMRActn_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DMRActnRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DMRHeadAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DMRHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DMRHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow,
}

export interface Erp_Tablesets_DMRActnRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  */  
   "ActionNum":number,
      /**  DMR Action Date.  */  
   "ActionDate":string,
      /**  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  */  
   "ActionType":string,
      /**  DMR Action quantity in base unit of measure.  Must be > ZERO.  */  
   "Quantity":number,
      /**  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  */  
   "DestinationType":string,
      /**  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "WarehouseCode":string,
      /**  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  */  
   "BinNum":string,
      /**  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  */  
   "JobNum":string,
      /**  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "DMRSeqNum":number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "UnitCredit":number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "DocUnitCredit":number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "CreditUM":string,
      /**  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  */  
   "DebitMemoNum":string,
      /**  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  */  
   "DebitMemoLine":number,
      /**  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  */  
   "VendRMANum":string,
      /**  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  */  
   "ActionUserID":string,
      /**  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  */  
   "SysTime":number,
      /**  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  */  
   "CommentText":string,
      /**  DMRs use Reason type "D".  Required for all actions.  */  
   "ReasonCode":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   "FldWarehouseCode":string,
      /**  The user defined bin number within the warehouse.  */  
   "FldBinNum":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCredit":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  */  
   "Resolution":string,
      /**  Flag indicating that the part will be returned to the supplier.  */  
   "ReturnToSupplier":boolean,
      /**  This is the supplier's packing slip number for the original receipt of the part.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackLine":number,
      /**  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  */  
   "DisableRejection":boolean,
      /**  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  */  
   "DisableRejectionChar":string,
      /**  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  */  
   "RefInvoiceNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IssuedComplete  */  
   "IssuedComplete":boolean,
      /**  PCID  */  
   "PCID":string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   "AcceptIUM":string,
   "ActionTypeDesc":string,
   "BaseCurrSymbol":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
      /**  External field for handling unit of measure conversions in the UI.  */  
   "DispQuantity":number,
      /**  Indicates if the Bin field should be enabled for input.  */  
   "EnableBin":boolean,
      /**  Indicates if the Reason field should be enabled for input.  */  
   "EnableReason":boolean,
      /**  Indicates if the RequestMove field should be enabled for input.  */  
   "EnableReqMove":boolean,
      /**  Indicates if the Warehouse field should be enabled for input.  */  
   "EnableWarehouse":boolean,
   "LegalNumberMessage":string,
   "OpenDMR":boolean,
      /**  Job Operation Complete  */  
   "OperationComplete":boolean,
      /**  PartNum  */  
   "PartNum":string,
      /**  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  */  
   "PartTrackSerialNum":boolean,
      /**  Plant  */  
   "Plant":string,
      /**  PO Currency Code.  */  
   "POCurrencyCode":string,
   "POLine":number,
   "PONum":number,
      /**  DMR item's unit cost in the POs currency.  */  
   "POUnitCost":number,
   "ReasonDescription":string,
   "RejectType":string,
      /**  Request to Move  */  
   "RequestMove":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1POUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2POUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3POUnitCost":number,
      /**  The plant id of the plant that is controlling the serial processing for this transaction record  */  
   "SerialControlPlant":string,
      /**  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  */  
   "SerialControlPlant2":string,
      /**  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  */  
   "SerialControlPlantIsFromPlt":boolean,
   "TotRemainQty":number,
      /**  TranQty  */  
   "TranQty":number,
      /**  TranUOM  */  
   "TranUOM":string,
      /**  Displays the customer name for the Ship To contact related to the RMA.  */  
   "ShipToCustID":string,
      /**  Displays the customer Ship To name related to the RMA.  */  
   "ShipToName":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  Customer that is returning parts on related RMA.  */  
   "CustomerCustID":string,
      /**  The RMA Number that the Return detail is related to.  */  
   "RMANum":number,
      /**  The RMA line that the Return detail is related to.  */  
   "RMALine":number,
      /**  Specifies the ID of the Ship To contact related to the RMA.  */  
   "ShipToID":string,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "DMRNumPartDescription":string,
   "JobNumPartDescription":string,
   "RateGrpDescription":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DMRHeadAttchRow{
   "Company":string,
   "DMRNum":number,
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

export interface Erp_Tablesets_DMRHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  */  
   "OpenDMR":boolean,
      /**  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  */  
   "VendorNum":number,
      /**  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  */  
   "PurPoint":string,
      /**  Contact Person Number  */  
   "ConNum":number,
      /**  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  */  
   "TotDiscrepantQty":number,
      /**  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  */  
   "TotRejectedQty":number,
      /**  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  */  
   "TotAcceptedQty":number,
      /**  Average Material Unit Cost.  */  
   "AvgMtlUnitCost":number,
      /**  Average Labor Unit cost.  */  
   "AvgLbrUnitCost":number,
      /**  Average Burden unit cost.  */  
   "AvgBurUnitCost":number,
      /**  Average Subcontract unit cost  */  
   "AvgSubUnitCost":number,
      /**  Average Mtl Burden unit cost  */  
   "AvgMtlBurUnitCost":number,
      /**  Parrt Number  */  
   "PartNum":string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   "PartDescription":string,
      /**  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  */  
   "DimCode":string,
      /**  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  */  
   "LotNum":string,
      /**  Base Inventory Unit of Measure.  System maintained, not user modifiable.  */  
   "IUM":string,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "ResourceID":string,
      /**  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "BinNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Total Mtl Mtl unit cost to date.  */  
   "MaterialMtlCost":number,
      /**  Total Mtl Lab unit cost to date  */  
   "MaterialLabCost":number,
      /**  Total Mtl Sub unit cost to date  */  
   "MaterialSubCost":number,
      /**  Total Material  Bur unit component cost to date  */  
   "MaterialBurCost":number,
      /**  Indicates this requires a Vendor RMA number  */  
   "ReqDMR":boolean,
      /**  Vendors RMA number.  Defaults to DMR Number.  */  
   "VendRMANum":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
   "DispTotAcceptedQty":number,
   "DispTotRejectedQty":number,
   "DispTotRemainQty":number,
   "DispTotDiscrepantQty":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DMRHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  */  
   "OpenDMR":boolean,
      /**  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  */  
   "VendorNum":number,
      /**  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  */  
   "PurPoint":string,
      /**  Contact Person Number  */  
   "ConNum":number,
      /**  Contains comments about the detail DMR line item. These will be printed on the DMR Status Report.  */  
   "CommentText":string,
      /**  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  */  
   "TotDiscrepantQty":number,
      /**  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  */  
   "TotRejectedQty":number,
      /**  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  */  
   "TotAcceptedQty":number,
      /**  Average Material Unit Cost.  */  
   "AvgMtlUnitCost":number,
      /**  Average Labor Unit cost.  */  
   "AvgLbrUnitCost":number,
      /**  Average Burden unit cost.  */  
   "AvgBurUnitCost":number,
      /**  Average Subcontract unit cost  */  
   "AvgSubUnitCost":number,
      /**  Average Mtl Burden unit cost  */  
   "AvgMtlBurUnitCost":number,
      /**  Parrt Number  */  
   "PartNum":string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   "PartDescription":string,
      /**  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  */  
   "DimCode":string,
      /**  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  */  
   "LotNum":string,
      /**  Base Inventory Unit of Measure.  System maintained, not user modifiable.  */  
   "IUM":string,
      /**   Optional DMR check off # 1. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   "CheckOff1":boolean,
      /**   Optional DMR check off # 2. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   "CheckOff2":boolean,
      /**   Optional DMR check off # 3. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   "CheckOff3":boolean,
      /**   Optional DMR check off # 4. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   "CheckOff4":boolean,
      /**   Optional DMR check off # 5. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   "CheckOff5":boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "ResourceID":string,
      /**  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "BinNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Total Mtl Mtl unit cost to date.  */  
   "MaterialMtlCost":number,
      /**  Total Mtl Lab unit cost to date  */  
   "MaterialLabCost":number,
      /**  Total Mtl Sub unit cost to date  */  
   "MaterialSubCost":number,
      /**  Total Material  Bur unit component cost to date  */  
   "MaterialBurCost":number,
      /**  Indicates this requires a Vendor RMA number  */  
   "ReqDMR":boolean,
      /**  Vendors RMA number.  Defaults to DMR Number.  */  
   "VendRMANum":string,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Plant  */  
   "Plant":string,
      /**  PONum  */  
   "PONum":number,
      /**  EpicorFSA  */  
   "EpicorFSA":boolean,
      /**  RMANum  */  
   "RMANum":number,
      /**  RMALine  */  
   "RMALine":number,
      /**  Declaration Bill  */  
   "CNDeclarationBill":string,
      /**  Return Date  */  
   "CNReturnDate":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  CNBonded  */  
   "CNBonded":boolean,
      /**  PCID  */  
   "PCID":string,
      /**  CNDeclarationBillLine  */  
   "CNDeclarationBillLine":number,
   "AllowAcceptToMtl":boolean,
   "AllowAcceptToOpr":boolean,
   "AllowAcceptToStock":boolean,
   "CheckOffLabel1":string,
   "CheckOffLabel2":string,
   "CheckOffLabel3":string,
   "CheckOffLabel4":string,
   "CheckOffLabel5":string,
   "DiscrepantUM":string,
   "DispTotAcceptedQty":number,
   "DispTotDiscrepantQty":number,
   "DispTotRejectedQty":number,
   "DispTotRemainQty":number,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
   "NonConfID":number,
      /**  Indicates the panel view for this record (S)tock, (M)aterial, (O)peration  */  
   "PanelView":string,
      /**  PlantName of the Plant  */  
   "PlantName":string,
      /**  Remaining Quantity is the Total Discrepant Qty except the sum of the totals of the  AcceptedQty and RejectedQty  */  
   "QtyRemaining":number,
   "RejectedUM":string,
   "RemainUM":string,
   "AcceptedUM":string,
      /**  Flag in PlantConfCtrl that enables Package Control functionality  */  
   "PlantConfCtrlEnablePackageControl":boolean,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "ConNumName":string,
   "ConNumPhoneNum":string,
   "ConNumEmailAddress":string,
   "ConNumFaxNum":string,
   "DimCodeDimCodeDescription":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "JobNumPartDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "ResourceIDDescription":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress1":string,
   "VendorNumAddress2":string,
   "VendorNumName":string,
   "VendorNumCurrencyCode":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "WarehouseCodeDescription":string,
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




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface ChangeCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeExchangeRate_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface ChangeExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param iProposedAssemblySeq
   */  
export interface ChangeJobAsmSeq_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The proposed AssmeblySeq value  */  
   iProposedAssemblySeq:number,
}

export interface ChangeJobAsmSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param iProposedDMRSeqNum
   */  
export interface ChangeJobMtlSeq_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The proposed material sequence number  */  
   iProposedDMRSeqNum:number,
}

export interface ChangeJobMtlSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param cProposedJobNum
   */  
export interface ChangeJobNum_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The proposed Job Number  */  
   cProposedJobNum:string,
}

export interface ChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param iDMRNum
      @param cProposedPackLine
   */  
export interface ChangePackingSlipLine_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number  */  
   iDMRNum:number,
      /**  The proposed PackLine  */  
   cProposedPackLine:number,
}

export interface ChangePackingSlipLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param iDMRNum
      @param cProposedPackSlip
   */  
export interface ChangePackingSlip_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number  */  
   iDMRNum:number,
      /**  The proposed PackSlip  */  
   cProposedPackSlip:string,
}

export interface ChangePackingSlip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param cProposedRefInvoiceNum
   */  
export interface ChangeRefInvoiceNum_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The proposed Ref Invoice Number  */  
   cProposedRefInvoiceNum:string,
}

export interface ChangeRefInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param cProposedWarehouseCode
   */  
export interface ChangeStkWhs_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The proposed Accept to Stock warehouse  */  
   cProposedWarehouseCode:string,
}

export interface ChangeStkWhs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUnitCredit_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface ChangeUnitCredit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeWarehouse_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface ChangeWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param bBeforeUpdate
      @param ds
   */  
export interface CheckCNCustomsDeclarationBillLine_input{
   bBeforeUpdate:boolean,
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface CheckCNCustomsDeclarationBillLine_output{
parameters : {
      /**  output parameters  */  
   sMessage:string,
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param iDMRNum
      @param cJobNum
      @param iAssemblySeq
      @param iDMRSeqNum
      @param dQuantity
      @param cUOM
      @param lProposedIssueComplete
   */  
export interface CheckIssueComplete_input{
      /**  The DMR Number  */  
   iDMRNum:number,
      /**  The Job Number  */  
   cJobNum:string,
      /**  The Assembly Sequence Number  */  
   iAssemblySeq:number,
      /**  The DMR Action Sequence Number (Material Sequence)  */  
   iDMRSeqNum:number,
      /**  The DMRActn Quantity  */  
   dQuantity:number,
      /**  The DMRActn UOM  */  
   cUOM:string,
      /**  The proposed value for the Issue Complete flag  */  
   lProposedIssueComplete:boolean,
}

export interface CheckIssueComplete_output{
parameters : {
      /**  output parameters  */  
   cMessageText:string,
}
}

   /** Required : 
      @param cJobNum
      @param iAssemblySeq
      @param iDMRSeqNum
   */  
export interface CheckJobMtlSeq_input{
      /**  The job number  */  
   cJobNum:string,
      /**  The assembly sequence  */  
   iAssemblySeq:number,
      /**  The DMR sequequence number  */  
   iDMRSeqNum:number,
}

export interface CheckJobMtlSeq_output{
parameters : {
      /**  output parameters  */  
   cMessage:string,
}
}

   /** Required : 
      @param cJobNum
      @param iAssemblySeq
      @param iDMRSeqNum
      @param lProposedOperationComplete
   */  
export interface CheckOperationComplete_input{
      /**  The Job Number  */  
   cJobNum:string,
      /**  The Assembly Sequence Number  */  
   iAssemblySeq:number,
      /**  The DMR Action Sequence Number (Operation Sequence)  */  
   iDMRSeqNum:number,
      /**  The proposed value for the Operation Complete flag  */  
   lProposedOperationComplete:boolean,
}

export interface CheckOperationComplete_output{
parameters : {
      /**  output parameters  */  
   cMessageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckPlanningContractBin_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface CheckPlanningContractBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
   pcPCBinAction:string,
   pcPCBinMessage:string,
}
}

   /** Required : 
      @param iDMRNum
      @param iDMRAction
   */  
export interface CheckRejectDisabled_input{
      /**  Actual dmr num.  */  
   iDMRNum:number,
      /**  Actual dmr action.  */  
   iDMRAction:number,
}

export interface CheckRejectDisabled_output{
parameters : {
      /**  output parameters  */  
   DebitMemo:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CustomUpdate_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface CustomUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
   opLegalNumberMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultIssueComplete_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface DefaultIssueComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param dmRNum
   */  
export interface DeleteByID_input{
   dmRNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DMRActnRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  */  
   ActionNum:number,
      /**  DMR Action Date.  */  
   ActionDate:string,
      /**  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  */  
   ActionType:string,
      /**  DMR Action quantity in base unit of measure.  Must be > ZERO.  */  
   Quantity:number,
      /**  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  */  
   DestinationType:string,
      /**  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   WarehouseCode:string,
      /**  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  */  
   BinNum:string,
      /**  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  */  
   JobNum:string,
      /**  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   DMRSeqNum:number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   UnitCredit:number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   DocUnitCredit:number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  */  
   CreditUM:string,
      /**  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  */  
   DebitMemoNum:string,
      /**  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  */  
   DebitMemoLine:number,
      /**  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  */  
   VendRMANum:string,
      /**  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  */  
   ActionUserID:string,
      /**  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  */  
   SysTime:number,
      /**  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  */  
   CommentText:string,
      /**  DMRs use Reason type "D".  Required for all actions.  */  
   ReasonCode:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   FldWarehouseCode:string,
      /**  The user defined bin number within the warehouse.  */  
   FldBinNum:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCredit:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  */  
   Resolution:string,
      /**  Flag indicating that the part will be returned to the supplier.  */  
   ReturnToSupplier:boolean,
      /**  This is the supplier's packing slip number for the original receipt of the part.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackLine:number,
      /**  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  */  
   DisableRejection:boolean,
      /**  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  */  
   DisableRejectionChar:string,
      /**  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  */  
   RefInvoiceNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IssuedComplete  */  
   IssuedComplete:boolean,
      /**  PCID  */  
   PCID:string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   AcceptIUM:string,
   ActionTypeDesc:string,
   BaseCurrSymbol:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  External field for handling unit of measure conversions in the UI.  */  
   DispQuantity:number,
      /**  Indicates if the Bin field should be enabled for input.  */  
   EnableBin:boolean,
      /**  Indicates if the Reason field should be enabled for input.  */  
   EnableReason:boolean,
      /**  Indicates if the RequestMove field should be enabled for input.  */  
   EnableReqMove:boolean,
      /**  Indicates if the Warehouse field should be enabled for input.  */  
   EnableWarehouse:boolean,
   LegalNumberMessage:string,
   OpenDMR:boolean,
      /**  Job Operation Complete  */  
   OperationComplete:boolean,
      /**  PartNum  */  
   PartNum:string,
      /**  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  */  
   PartTrackSerialNum:boolean,
      /**  Plant  */  
   Plant:string,
      /**  PO Currency Code.  */  
   POCurrencyCode:string,
   POLine:number,
   PONum:number,
      /**  DMR item's unit cost in the POs currency.  */  
   POUnitCost:number,
   ReasonDescription:string,
   RejectType:string,
      /**  Request to Move  */  
   RequestMove:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1POUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2POUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3POUnitCost:number,
      /**  The plant id of the plant that is controlling the serial processing for this transaction record  */  
   SerialControlPlant:string,
      /**  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  */  
   SerialControlPlant2:string,
      /**  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  */  
   SerialControlPlantIsFromPlt:boolean,
   TotRemainQty:number,
      /**  TranQty  */  
   TranQty:number,
      /**  TranUOM  */  
   TranUOM:string,
      /**  Displays the customer name for the Ship To contact related to the RMA.  */  
   ShipToCustID:string,
      /**  Displays the customer Ship To name related to the RMA.  */  
   ShipToName:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  Customer that is returning parts on related RMA.  */  
   CustomerCustID:string,
      /**  The RMA Number that the Return detail is related to.  */  
   RMANum:number,
      /**  The RMA line that the Return detail is related to.  */  
   RMALine:number,
      /**  Specifies the ID of the Ship To contact related to the RMA.  */  
   ShipToID:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   DMRNumPartDescription:string,
   JobNumPartDescription:string,
   RateGrpDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DMRHeadAttchRow{
   Company:string,
   DMRNum:number,
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

export interface Erp_Tablesets_DMRHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  */  
   OpenDMR:boolean,
      /**  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  */  
   VendorNum:number,
      /**  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  */  
   PurPoint:string,
      /**  Contact Person Number  */  
   ConNum:number,
      /**  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  */  
   TotDiscrepantQty:number,
      /**  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  */  
   TotRejectedQty:number,
      /**  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  */  
   TotAcceptedQty:number,
      /**  Average Material Unit Cost.  */  
   AvgMtlUnitCost:number,
      /**  Average Labor Unit cost.  */  
   AvgLbrUnitCost:number,
      /**  Average Burden unit cost.  */  
   AvgBurUnitCost:number,
      /**  Average Subcontract unit cost  */  
   AvgSubUnitCost:number,
      /**  Average Mtl Burden unit cost  */  
   AvgMtlBurUnitCost:number,
      /**  Parrt Number  */  
   PartNum:string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   PartDescription:string,
      /**  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  */  
   DimCode:string,
      /**  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  */  
   LotNum:string,
      /**  Base Inventory Unit of Measure.  System maintained, not user modifiable.  */  
   IUM:string,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   ResourceID:string,
      /**  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Total Mtl Mtl unit cost to date.  */  
   MaterialMtlCost:number,
      /**  Total Mtl Lab unit cost to date  */  
   MaterialLabCost:number,
      /**  Total Mtl Sub unit cost to date  */  
   MaterialSubCost:number,
      /**  Total Material  Bur unit component cost to date  */  
   MaterialBurCost:number,
      /**  Indicates this requires a Vendor RMA number  */  
   ReqDMR:boolean,
      /**  Vendors RMA number.  Defaults to DMR Number.  */  
   VendRMANum:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
   DispTotAcceptedQty:number,
   DispTotRejectedQty:number,
   DispTotRemainQty:number,
   DispTotDiscrepantQty:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DMRHeadListTableset{
   DMRHeadList:Erp_Tablesets_DMRHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DMRHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  */  
   OpenDMR:boolean,
      /**  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  */  
   VendorNum:number,
      /**  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  */  
   PurPoint:string,
      /**  Contact Person Number  */  
   ConNum:number,
      /**  Contains comments about the detail DMR line item. These will be printed on the DMR Status Report.  */  
   CommentText:string,
      /**  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  */  
   TotDiscrepantQty:number,
      /**  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  */  
   TotRejectedQty:number,
      /**  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  */  
   TotAcceptedQty:number,
      /**  Average Material Unit Cost.  */  
   AvgMtlUnitCost:number,
      /**  Average Labor Unit cost.  */  
   AvgLbrUnitCost:number,
      /**  Average Burden unit cost.  */  
   AvgBurUnitCost:number,
      /**  Average Subcontract unit cost  */  
   AvgSubUnitCost:number,
      /**  Average Mtl Burden unit cost  */  
   AvgMtlBurUnitCost:number,
      /**  Parrt Number  */  
   PartNum:string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   PartDescription:string,
      /**  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  */  
   DimCode:string,
      /**  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  */  
   LotNum:string,
      /**  Base Inventory Unit of Measure.  System maintained, not user modifiable.  */  
   IUM:string,
      /**   Optional DMR check off # 1. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   CheckOff1:boolean,
      /**   Optional DMR check off # 2. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   CheckOff2:boolean,
      /**   Optional DMR check off # 3. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   CheckOff3:boolean,
      /**   Optional DMR check off # 4. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   CheckOff4:boolean,
      /**   Optional DMR check off # 5. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  */  
   CheckOff5:boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   ResourceID:string,
      /**  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Total Mtl Mtl unit cost to date.  */  
   MaterialMtlCost:number,
      /**  Total Mtl Lab unit cost to date  */  
   MaterialLabCost:number,
      /**  Total Mtl Sub unit cost to date  */  
   MaterialSubCost:number,
      /**  Total Material  Bur unit component cost to date  */  
   MaterialBurCost:number,
      /**  Indicates this requires a Vendor RMA number  */  
   ReqDMR:boolean,
      /**  Vendors RMA number.  Defaults to DMR Number.  */  
   VendRMANum:string,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Plant  */  
   Plant:string,
      /**  PONum  */  
   PONum:number,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  RMANum  */  
   RMANum:number,
      /**  RMALine  */  
   RMALine:number,
      /**  Declaration Bill  */  
   CNDeclarationBill:string,
      /**  Return Date  */  
   CNReturnDate:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  CNBonded  */  
   CNBonded:boolean,
      /**  PCID  */  
   PCID:string,
      /**  CNDeclarationBillLine  */  
   CNDeclarationBillLine:number,
   AllowAcceptToMtl:boolean,
   AllowAcceptToOpr:boolean,
   AllowAcceptToStock:boolean,
   CheckOffLabel1:string,
   CheckOffLabel2:string,
   CheckOffLabel3:string,
   CheckOffLabel4:string,
   CheckOffLabel5:string,
   DiscrepantUM:string,
   DispTotAcceptedQty:number,
   DispTotDiscrepantQty:number,
   DispTotRejectedQty:number,
   DispTotRemainQty:number,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
   NonConfID:number,
      /**  Indicates the panel view for this record (S)tock, (M)aterial, (O)peration  */  
   PanelView:string,
      /**  PlantName of the Plant  */  
   PlantName:string,
      /**  Remaining Quantity is the Total Discrepant Qty except the sum of the totals of the  AcceptedQty and RejectedQty  */  
   QtyRemaining:number,
   RejectedUM:string,
   RemainUM:string,
   AcceptedUM:string,
      /**  Flag in PlantConfCtrl that enables Package Control functionality  */  
   PlantConfCtrlEnablePackageControl:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   ConNumName:string,
   ConNumPhoneNum:string,
   ConNumEmailAddress:string,
   ConNumFaxNum:string,
   DimCodeDimCodeDescription:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackInventoryByRevision:boolean,
   ResourceIDDescription:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   VendorNumAddress2:string,
   VendorNumName:string,
   VendorNumCurrencyCode:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DMRHistoryRow{
   TranDate:string,
   TranType:string,
   InvAdjReason:string,
   JobNum:string,
   Quantity:number,
   AssemblySeq:number,
   JobSeq:number,
   WarehouseCode:string,
   BinNum:string,
   ExtCost:number,
   LotNum:string,
   EntryPerson:string,
   BurUnitCost:number,
   ActionNum:number,
   LbrUnitCost:number,
   MtlUnitCost:number,
   SubUnitCost:number,
   MtlBurUnitCost:number,
   NonConfID:number,
   TranReference:string,
   WhseDesc:string,
   BinDesc:string,
   ReasonDesc:string,
   UOM:string,
      /**  Primary key of PartTran.  */  
   PrimKeyStr:string,
   PCID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DMRHistoryTableset{
   DMRHistory:Erp_Tablesets_DMRHistoryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DMRProcessingTableset{
   DMRHead:Erp_Tablesets_DMRHeadRow[],
   DMRHeadAttch:Erp_Tablesets_DMRHeadAttchRow[],
   DMRActn:Erp_Tablesets_DMRActnRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_UpdExtDMRProcessingTableset{
   DMRHead:Erp_Tablesets_DMRHeadRow[],
   DMRHeadAttch:Erp_Tablesets_DMRHeadAttchRow[],
   DMRActn:Erp_Tablesets_DMRActnRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
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
      @param dmRNum
   */  
export interface GetByID_input{
   dmRNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DMRProcessingTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DMRProcessingTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DMRProcessingTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetContactInfo_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface GetContactInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
}
}

   /** Required : 
      @param ipDMRNum
   */  
export interface GetDMRHistory_input{
      /**  DMR Number  */  
   ipDMRNum:number,
}

export interface GetDMRHistory_output{
   returnObj:Erp_Tablesets_DMRHistoryTableset[],
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
   returnObj:Erp_Tablesets_DMRHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param ipDMRNum
   */  
export interface GetNewDMRActnAcceptCUST_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number being processed.  */  
   ipDMRNum:number,
}

export interface GetNewDMRActnAcceptCUST_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param ipDMRNum
   */  
export interface GetNewDMRActnAcceptMTL_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number being processed.  */  
   ipDMRNum:number,
}

export interface GetNewDMRActnAcceptMTL_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param ipDMRNum
   */  
export interface GetNewDMRActnAcceptOPR_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number being processed.  */  
   ipDMRNum:number,
}

export interface GetNewDMRActnAcceptOPR_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param ipDMRNum
   */  
export interface GetNewDMRActnAcceptSTK_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number being processed.  */  
   ipDMRNum:number,
}

export interface GetNewDMRActnAcceptSTK_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param ipDMRNum
   */  
export interface GetNewDMRActnDebitMemo_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number being processed.  */  
   ipDMRNum:number,
}

export interface GetNewDMRActnDebitMemo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param ipDMRNum
   */  
export interface GetNewDMRActnReject_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  The DMR Number being processed.  */  
   ipDMRNum:number,
}

export interface GetNewDMRActnReject_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param dmRNum
   */  
export interface GetNewDMRActn_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
   dmRNum:number,
}

export interface GetNewDMRActn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param dmRNum
   */  
export interface GetNewDMRHeadAttch_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
   dmRNum:number,
}

export interface GetNewDMRHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDMRHead_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface GetNewDMRHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetPurPointInfo_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface GetPurPointInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param whereClauseDMRHead
      @param whereClauseDMRHeadAttch
      @param whereClauseDMRActn
      @param whereClauseLegalNumGenOpts
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDMRHead:string,
   whereClauseDMRHeadAttch:string,
   whereClauseDMRActn:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DMRProcessingTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPartNum
      @param ipAttributeSetID
      @param ipQuantity
      @param ipDestinationType
      @param ipActionType
      @param ipSerialControlPlant
      @param ipSerialControlPlantIsFromPlt
      @param ipDMRNum
      @param ipJobNum
      @param ipPartTrackSerialNum
      @param ipActionNum
      @param ipQtyIUM
      @param ipPCID
   */  
export interface GetSelectSerialNumbersParams_input{
      /**  DMRActn Part Number  */  
   ipPartNum:string,
      /**  The part's attribute set  */  
   ipAttributeSetID:number,
      /**  Serial Number quantity required  */  
   ipQuantity:number,
      /**  DMR Action destination  */  
   ipDestinationType:string,
      /**  DMR Action action type  */  
   ipActionType:string,
      /**  Plant that is controlling serial entry rules  */  
   ipSerialControlPlant:string,
      /**  Indicates if the from plant is the controllin plant for serial entry  */  
   ipSerialControlPlantIsFromPlt:boolean,
      /**  DMR Number  */  
   ipDMRNum:number,
      /**  DMR Action Job Number  */  
   ipJobNum:string,
      /**  Indicates if Serial Numbers required on this DMR Action  */  
   ipPartTrackSerialNum:boolean,
      /**  DMR Action Number  */  
   ipActionNum:number,
      /**  UOM for the DMR quantity  */  
   ipQtyIUM:string,
      /**  PCID  */  
   ipPCID:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetVendorInfo_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface GetVendorInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
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
      @param pcid
      @param pCallProcess
      @param ds
   */  
export interface OnChangePCID_input{
   pcid:string,
   pCallProcess:string,
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface OnChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeResolution_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface OnChangeResolution_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
   requiresUserInput:boolean,
   serialTrackPartMessage:string,
}
}

   /** Required : 
      @param cAction
      @param iDMRNum
   */  
export interface ReasonCodeWhereClause_input{
      /**  The reason the where clause is being built.  Values are "REJ" for reject
            or "DM" for debit memo  */  
   cAction:string,
      /**  The DMR number.  This is needed when cAction is "REJ".  For
           cAction = "DM" the value can be 0 (zero)  */  
   iDMRNum:number,
}

export interface ReasonCodeWhereClause_output{
parameters : {
      /**  output parameters  */  
   cReasonWhereClause:string,
}
}

   /** Required : 
      @param iDMRNum
      @param iDMRAction
   */  
export interface UpdateDebitMemoNum_input{
      /**  Actual dmr num.  */  
   iDMRNum:number,
      /**  Actual dmr action.  */  
   iDMRAction:number,
}

export interface UpdateDebitMemoNum_output{
parameters : {
      /**  output parameters  */  
   DebitMemo:string,
   DebitMemoLine:number,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDMRProcessingTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDMRProcessingTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_DMRProcessingTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRProcessingTableset,
   isVoided:boolean,
}
}

