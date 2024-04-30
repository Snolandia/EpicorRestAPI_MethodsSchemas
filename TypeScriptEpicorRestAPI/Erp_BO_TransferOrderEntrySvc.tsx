import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.TransferOrderEntrySvc
// Description: Creates Transfer Orders
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/$metadata", {
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
   Description: Get TransferOrderEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransferOrderEntries
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedRow
   */  
export function get_TransferOrderEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransferOrderEntries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TFOrdHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransferOrderEntries(requestBody:Erp_Tablesets_TFOrdHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TransferOrderEntry item
   Description: Calls GetByID to retrieve the TransferOrderEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransferOrderEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdHedRow
   */  
export function get_TransferOrderEntries_Company_TFOrdNum(Company:string, TFOrdNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TransferOrderEntry for the service
   Description: Calls UpdateExt to update TransferOrderEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransferOrderEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TransferOrderEntries_Company_TFOrdNum(Company:string, TFOrdNum:string, requestBody:Erp_Tablesets_TFOrdHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")", {
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
   Summary: Call UpdateExt to delete TransferOrderEntry item
   Description: Call UpdateExt to delete TransferOrderEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransferOrderEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TransferOrderEntries_Company_TFOrdNum(Company:string, TFOrdNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")", {
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
   Description: Get TFOrdDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFOrdDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TransferOrderEntries_Company_TFOrdNum_TFOrdDtls(Company:string, TFOrdNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFOrdDtl item
   Description: Calls GetByID to retrieve the TFOrdDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TransferOrderEntries_Company_TFOrdNum_TFOrdDtls_Company_TFLineNum(Company:string, TFOrdNum:string, TFLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdDtls(" + Company + "," + TFLineNum + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TFOrdHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFOrdHedAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedAttchRow
   */  
export function get_TransferOrderEntries_Company_TFOrdNum_TFOrdHedAttches(Company:string, TFOrdNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFOrdHedAttch item
   Description: Calls GetByID to retrieve the TFOrdHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdHedAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   */  
export function get_TransferOrderEntries_Company_TFOrdNum_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company:string, TFOrdNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TFOrdDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFOrdDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TFOrdDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFOrdDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TFOrdDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFOrdDtls(requestBody:Erp_Tablesets_TFOrdDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TFOrdDtl item
   Description: Calls GetByID to retrieve the TFOrdDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TFOrdDtls_Company_TFLineNum(Company:string, TFLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls(" + Company + "," + TFLineNum + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFOrdDtl for the service
   Description: Calls UpdateExt to update TFOrdDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFOrdDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFOrdDtls_Company_TFLineNum(Company:string, TFLineNum:string, requestBody:Erp_Tablesets_TFOrdDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls(" + Company + "," + TFLineNum + ")", {
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
   Summary: Call UpdateExt to delete TFOrdDtl item
   Description: Call UpdateExt to delete TFOrdDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFOrdDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFOrdDtls_Company_TFLineNum(Company:string, TFLineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls(" + Company + "," + TFLineNum + ")", {
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
   Description: Get TFOrdHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFOrdHedAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedAttchRow
   */  
export function get_TFOrdHedAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFOrdHedAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFOrdHedAttches(requestBody:Erp_Tablesets_TFOrdHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TFOrdHedAttch item
   Description: Calls GetByID to retrieve the TFOrdHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   */  
export function get_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company:string, TFOrdNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFOrdHedAttch for the service
   Description: Calls UpdateExt to update TFOrdHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFOrdHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company:string, TFOrdNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_TFOrdHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete TFOrdHedAttch item
   Description: Call UpdateExt to delete TFOrdHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFOrdHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company:string, TFOrdNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedListRow)
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
export function get_GetRows(whereClauseTFOrdHed:string, whereClauseTFOrdHedAttch:string, whereClauseTFOrdDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTFOrdHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdHed=" + whereClauseTFOrdHed
   }
   if(typeof whereClauseTFOrdHedAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdHedAttch=" + whereClauseTFOrdHedAttch
   }
   if(typeof whereClauseTFOrdDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdDtl=" + whereClauseTFOrdDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetRows" + params, {
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
export function get_GetByID(tfOrdNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tfOrdNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tfOrdNum=" + tfOrdNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetList" + params, {
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
   Summary: Invoke method FindPart
   OperationID: FindPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:FindPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/FindPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as FindPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:GetPartFromRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartFromRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetPartFromRowID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPartFromRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFromPlant
   Description: Sets the transfer ship via code base on fromplant
   OperationID: ChangeFromPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFromPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromPlant(requestBody:ChangeFromPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFromPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/ChangeFromPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFromPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipVia
   Description: Sets the transfer degtail ship via code from the header
   OperationID: ChangeShipVia
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeShipVia_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipVia_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipVia(requestBody:ChangeShipVia_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeShipVia_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/ChangeShipVia", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeShipVia_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTransferContractID
   Description: Sets warehouse defaults when transfer Planning Contract or transfer link to contract are changed
   OperationID: ChangeTransferContractID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTransferContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTransferContractID(requestBody:ChangeTransferContractID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTransferContractID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/ChangeTransferContractID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTransferContractID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSellingQty
   Description: This method is to be called when the Selling Quantity field changes
   OperationID: ChangeSellingQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSellingQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSellingQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSellingQty(requestBody:ChangeSellingQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSellingQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/ChangeSellingQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSellingQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSellingQtyUOM
   Description: This method is to be called when the Selling Quantity UOM field changes
   OperationID: ChangeSellingQtyUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSellingQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSellingQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSellingQtyUOM(requestBody:ChangeSellingQtyUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSellingQtyUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/ChangeSellingQtyUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSellingQtyUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/OnChangingNumberOfPieces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:OnChangingAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/OnChangingAttributeSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/OnChangingRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetListCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:GetListCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetListCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFOrdDtlOrdNum
   Description: This method is to override the standard GetNewTFOrdDtl method since TFOrdDtl needs to
be passed in and that is no longer the primary key.
   OperationID: GetNewTFOrdDtlOrdNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdDtlOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdDtlOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFOrdDtlOrdNum(requestBody:GetNewTFOrdDtlOrdNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTFOrdDtlOrdNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetNewTFOrdDtlOrdNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTFOrdDtlOrdNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetRowsCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustom(requestBody:GetRowsCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetRowsCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomPlantsWC
   Description: Calls the GetRowsCustomPlants method, but this method allow the use of whereClauses for each DataView
<param name="whereClauseTFOrdHed">TFOrdHed WhereClause </param><param name="whereClauseTFOrdHedAttch">TFOrdHedAttch WhereClause </param><param name="whereClauseTFOrdDtl">TFOrdDtl WhereClause </param><param name="pageSize">The pageSize </param><param name="absolutePage">The absolutePage </param><param name="morePages">The morePages</param>
   OperationID: Get_GetRowsCustomPlantsWC
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomPlantsWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsCustomPlantsWC(whereClauseTFOrdHed:string, whereClauseTFOrdHedAttch:string, whereClauseTFOrdDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTFOrdHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdHed=" + whereClauseTFOrdHed
   }
   if(typeof whereClauseTFOrdHedAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdHedAttch=" + whereClauseTFOrdHedAttch
   }
   if(typeof whereClauseTFOrdDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdDtl=" + whereClauseTFOrdDtl
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

   return (new Promise<GetRowsCustomPlantsWC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetRowsCustomPlantsWC" + params, {
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
         resolve(data as GetRowsCustomPlantsWC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomPlants
   Description: Custom GetRows method. Retrieves records based on user
authorized plants.
   OperationID: GetRowsCustomPlants
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCustomPlants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomPlants_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomPlants(requestBody:GetRowsCustomPlants_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustomPlants_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetRowsCustomPlants", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsCustomPlants_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransferShipDate
   Description: Sets the transfer ship date base on fromplant, toplant, and needbydate.
It's calculated using the needby date and subtracting the transfers days
held in the PltTranDef Table.
   OperationID: GetTransferShipDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransferShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransferShipDate(requestBody:GetTransferShipDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransferShipDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetTransferShipDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTransferShipDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: This method is to be called when the Part Number field changes
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/OnChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePartAllocQueue
   Description: Update the fulfillment queue with the lines on this transfer order.
   OperationID: UpdatePartAllocQueue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdatePartAllocQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePartAllocQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePartAllocQueue(requestBody:UpdatePartAllocQueue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdatePartAllocQueue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/UpdatePartAllocQueue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdatePartAllocQueue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBeforeUpdate
   Description: Checks before performing the transfer order update
   OperationID: CheckBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBeforeUpdate(requestBody:CheckBeforeUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/CheckBeforeUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckBeforeUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFOrdHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFOrdHed(requestBody:GetNewTFOrdHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTFOrdHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetNewTFOrdHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTFOrdHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFOrdHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdHedAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFOrdHedAttch(requestBody:GetNewTFOrdHedAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTFOrdHedAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetNewTFOrdHedAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTFOrdHedAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFOrdDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFOrdDtl(requestBody:GetNewTFOrdDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTFOrdDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetNewTFOrdDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTFOrdDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdHedAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdHedRow,
}

export interface Erp_Tablesets_TFOrdDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  */  
   "TFOrdNum":string,
      /**  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   "OpenLine":boolean,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "OurStockQty":number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   "WarehouseCode":string,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   "OurStockShippedQty":number,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   "OrderFirm":boolean,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   "RequestDate":string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   "NeedByDate":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  */  
   "ManualOrder":boolean,
      /**  Job number of the job supplying the parts for this record (FromSite)  */  
   "SupplyJobNum":string,
      /**  Job number of the job demand for the parts on this record (ToSite)  */  
   "DemandJobNum":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  Received Quantity  */  
   "ReceivedQty":number,
      /**  Additional quantity beyond the initial requirement to be transferred  */  
   "AdditionalQty":number,
      /**  Date transfer suggestion went firm  */  
   "FirmDate":string,
      /**  User who made the transfer suggestion firm  */  
   "FirmUser":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "DemandAsmSeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "DemandMtlSeq":number,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "SupplyAsmSeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "SupplyMtlSeq":number,
      /**  Indicates if this requirement/receipt affects stock.  */  
   "StockTrans":boolean,
      /**   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "OurStockQtyUOM":string,
      /**   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "SellingQtyUOM":string,
      /**  Selling Quantity  */  
   "SellingQty":number,
      /**  Selling Shipped Quantity  */  
   "SellingShippedQty":number,
      /**  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  */  
   "StagingWarehouseCode":string,
      /**  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  */  
   "TransferContractID":string,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  */  
   "TransferLinkToContract":boolean,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Indicates if the transfer order line should be added or removed from the fulfillment queue.  */  
   "PartAllocQueueAction":string,
      /**  This flag indicates if the transfer order line is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
   "AvailSerialNumbers":boolean,
   "BinNum":string,
   "DimCode":string,
      /**  DimCodeDimCodeDescription  */  
   "DimCodeDimCodeDescription":string,
   "DimConvFactor":number,
      /**  OurStockQty * DimConvFactor  */  
   "DisplayShipQty":number,
   "DUM":string,
   "FromPlantDesc":string,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   "InvtyUOM":string,
      /**  Descriptive Text of OpenLine Field  */  
   "LineStatus":string,
   "LotNum":string,
   "Packages":number,
   "PCID":string,
   "PkgClass":string,
      /**  PkgClassDescription  */  
   "PkgClassDescription":string,
   "PkgCode":string,
      /**  PkgCodeDescription  */  
   "PkgCodeDescription":string,
   "RequiredQty":number,
   "Selected":boolean,
   "StagingBinDesc":string,
      /**  This order inventory quantity  */  
   "ThisOrderInvtyQty":number,
   "ToPlantDesc":string,
   "TotNetWeight":number,
   "Weight":number,
   "CreateOrder":boolean,
   "EnableAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
      /**  Error Status Display  */  
   "ErrorStatusDisplay":string,
      /**  True if this release is in the fulfillment queue.  */  
   "InPartAllocQueue":boolean,
      /**  Show Fulfillment Queue Actions  */  
   "ShowFulfillmentQueueActions":boolean,
   "BitFlag":number,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "PartDescTrackInventoryAttributes":boolean,
   "PartDescAttrClassID":string,
   "PartDescPricePerCode":string,
   "PartDescTrackSerialNum":boolean,
   "PartDescPartDescription":string,
   "PartDescTrackDimension":boolean,
   "PartDescSalesUM":string,
   "PartDescIUM":string,
   "PartDescSellingFactor":number,
   "PartDescTrackLots":boolean,
   "PartDescTrackInventoryByRevision":boolean,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "StageWhseCodeDescription":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFOrdHedAttchRow{
   "Company":string,
   "TFOrdNum":string,
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

export interface Erp_Tablesets_TFOrdHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   "OpenOrder":boolean,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   "OrderDate":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   "ShipComment":string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   "PickListComment":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   "WarehouseCode":string,
      /**  Indicates that the One Time ShipTo information defined for this release should be used.  */  
   "UseOTS":boolean,
      /**  One Time ShipTo Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time ShipTo first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time ShipTo second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time ShipTo third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portionof the One Time ShipTo address.  */  
   "OTSCity":string,
      /**  The state or provine portion of the One Time ShipTo address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo address.  */  
   "OTSZip":string,
      /**  One Time ShipTo contact name.  */  
   "OTSContact":string,
   "OTSCountryNum":number,
      /**  Phone number for the One Time ShipTo.  */  
   "OTSPhoneNum":string,
      /**  Fax Number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ToPlantDesc":string,
   "FromPlantDesc":string,
   "NeedByDate":string,
   "RequestDate":string,
      /**  User Name  */  
   "EntryPersonName":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFOrdHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   "OpenOrder":boolean,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   "OrderDate":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   "ShipComment":string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   "PickListComment":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   "WarehouseCode":string,
      /**  Indicates that the One Time ShipTo information defined for this release should be used.  */  
   "UseOTS":boolean,
      /**  One Time ShipTo Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time ShipTo first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time ShipTo second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time ShipTo third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portionof the One Time ShipTo address.  */  
   "OTSCity":string,
      /**  The state or provine portion of the One Time ShipTo address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo address.  */  
   "OTSZip":string,
      /**  One Time ShipTo contact name.  */  
   "OTSContact":string,
   "OTSCountryNum":number,
      /**  Phone number for the One Time ShipTo.  */  
   "OTSPhoneNum":string,
      /**  Fax Number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This flag indicates if the transfer order is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
   "ToPlantDesc":string,
   "FromPlantDesc":string,
   "NeedByDate":string,
   "RequestDate":string,
      /**  Show Fulfillment Queue Actions  */  
   "ShowFulfillmentQueueActions":boolean,
      /**  Flag to indicate if details need to be refreshed after changing the header.  */  
   "UpdateDtlRecords":boolean,
   "BitFlag":number,
   "EntryPersonName":string,
   "ShipViaDescription":string,
   "ShipViaWebDesc":string,
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
export interface ChangeFromPlant_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface ChangeFromPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSellingQtyUOM_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface ChangeSellingQtyUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSellingQty_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface ChangeSellingQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeShipVia_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface ChangeShipVia_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTransferContractID_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface ChangeTransferContractID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param viewName
      @param ds
   */  
export interface CheckBeforeUpdate_input{
      /**  View name  */  
   viewName:string,
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface CheckBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   tfOrdHedChangedMsgText:string,
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param tfOrdNum
   */  
export interface DeleteByID_input{
   tfOrdNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TFOrdDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  */  
   TFOrdNum:string,
      /**  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   OrderFirm:boolean,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  */  
   ManualOrder:boolean,
      /**  Job number of the job supplying the parts for this record (FromSite)  */  
   SupplyJobNum:string,
      /**  Job number of the job demand for the parts on this record (ToSite)  */  
   DemandJobNum:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Received Quantity  */  
   ReceivedQty:number,
      /**  Additional quantity beyond the initial requirement to be transferred  */  
   AdditionalQty:number,
      /**  Date transfer suggestion went firm  */  
   FirmDate:string,
      /**  User who made the transfer suggestion firm  */  
   FirmUser:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   DemandAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   DemandMtlSeq:number,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   SupplyAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   SupplyMtlSeq:number,
      /**  Indicates if this requirement/receipt affects stock.  */  
   StockTrans:boolean,
      /**   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   OurStockQtyUOM:string,
      /**   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   SellingQtyUOM:string,
      /**  Selling Quantity  */  
   SellingQty:number,
      /**  Selling Shipped Quantity  */  
   SellingShippedQty:number,
      /**  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ContractID  */  
   ContractID:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  */  
   TransferContractID:string,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  */  
   TransferLinkToContract:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Indicates if the transfer order line should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  This flag indicates if the transfer order line is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
   AvailSerialNumbers:boolean,
   BinNum:string,
   DimCode:string,
      /**  DimCodeDimCodeDescription  */  
   DimCodeDimCodeDescription:string,
   DimConvFactor:number,
      /**  OurStockQty * DimConvFactor  */  
   DisplayShipQty:number,
   DUM:string,
   FromPlantDesc:string,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   InvtyUOM:string,
      /**  Descriptive Text of OpenLine Field  */  
   LineStatus:string,
   LotNum:string,
   Packages:number,
   PCID:string,
   PkgClass:string,
      /**  PkgClassDescription  */  
   PkgClassDescription:string,
   PkgCode:string,
      /**  PkgCodeDescription  */  
   PkgCodeDescription:string,
   RequiredQty:number,
   Selected:boolean,
   StagingBinDesc:string,
      /**  This order inventory quantity  */  
   ThisOrderInvtyQty:number,
   ToPlantDesc:string,
   TotNetWeight:number,
   Weight:number,
   CreateOrder:boolean,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this release is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   PartDescTrackInventoryAttributes:boolean,
   PartDescAttrClassID:string,
   PartDescPricePerCode:string,
   PartDescTrackSerialNum:boolean,
   PartDescPartDescription:string,
   PartDescTrackDimension:boolean,
   PartDescSalesUM:string,
   PartDescIUM:string,
   PartDescSellingFactor:number,
   PartDescTrackLots:boolean,
   PartDescTrackInventoryByRevision:boolean,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   StageWhseCodeDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFOrdHedAttchRow{
   Company:string,
   TFOrdNum:string,
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

export interface Erp_Tablesets_TFOrdHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   ShipComment:string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   PickListComment:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   WarehouseCode:string,
      /**  Indicates that the One Time ShipTo information defined for this release should be used.  */  
   UseOTS:boolean,
      /**  One Time ShipTo Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time ShipTo first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time ShipTo second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time ShipTo third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portionof the One Time ShipTo address.  */  
   OTSCity:string,
      /**  The state or provine portion of the One Time ShipTo address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo address.  */  
   OTSZip:string,
      /**  One Time ShipTo contact name.  */  
   OTSContact:string,
   OTSCountryNum:number,
      /**  Phone number for the One Time ShipTo.  */  
   OTSPhoneNum:string,
      /**  Fax Number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ToPlantDesc:string,
   FromPlantDesc:string,
   NeedByDate:string,
   RequestDate:string,
      /**  User Name  */  
   EntryPersonName:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFOrdHedListTableset{
   TFOrdHedList:Erp_Tablesets_TFOrdHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TFOrdHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   ShipComment:string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   PickListComment:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   WarehouseCode:string,
      /**  Indicates that the One Time ShipTo information defined for this release should be used.  */  
   UseOTS:boolean,
      /**  One Time ShipTo Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time ShipTo first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time ShipTo second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time ShipTo third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portionof the One Time ShipTo address.  */  
   OTSCity:string,
      /**  The state or provine portion of the One Time ShipTo address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo address.  */  
   OTSZip:string,
      /**  One Time ShipTo contact name.  */  
   OTSContact:string,
   OTSCountryNum:number,
      /**  Phone number for the One Time ShipTo.  */  
   OTSPhoneNum:string,
      /**  Fax Number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This flag indicates if the transfer order is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
   ToPlantDesc:string,
   FromPlantDesc:string,
   NeedByDate:string,
   RequestDate:string,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
      /**  Flag to indicate if details need to be refreshed after changing the header.  */  
   UpdateDtlRecords:boolean,
   BitFlag:number,
   EntryPersonName:string,
   ShipViaDescription:string,
   ShipViaWebDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TransferOrderEntryTableset{
   TFOrdHed:Erp_Tablesets_TFOrdHedRow[],
   TFOrdHedAttch:Erp_Tablesets_TFOrdHedAttchRow[],
   TFOrdDtl:Erp_Tablesets_TFOrdDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTransferOrderEntryTableset{
   TFOrdHed:Erp_Tablesets_TFOrdHedRow[],
   TFOrdHedAttch:Erp_Tablesets_TFOrdHedAttchRow[],
   TFOrdDtl:Erp_Tablesets_TFOrdDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param tfOrdNum
   */  
export interface GetByID_input{
   tfOrdNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
}

   /** Required : 
      @param TransferOrderList
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  The Transfer Order List  */  
   TransferOrderList:string,
      /**  The pageSize  */  
   pageSize:number,
      /**  The absolutePage  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_TFOrdHedListTableset[],
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
   returnObj:Erp_Tablesets_TFOrdHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param TFOrdNum
   */  
export interface GetNewTFOrdDtlOrdNum_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
      /**  Transfer Order Number  */  
   TFOrdNum:string,
}

export interface GetNewTFOrdDtlOrdNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTFOrdDtl_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface GetNewTFOrdDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
      @param tfOrdNum
   */  
export interface GetNewTFOrdHedAttch_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
   tfOrdNum:string,
}

export interface GetNewTFOrdHedAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTFOrdHed_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface GetNewTFOrdHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
   ipRowType:string,
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param whereClauseTFOrdHed
      @param whereClauseTFOrdHedAttch
      @param whereClauseTFOrdDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomPlantsWC_input{
   whereClauseTFOrdHed:string,
   whereClauseTFOrdHedAttch:string,
   whereClauseTFOrdDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsCustomPlantsWC_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param TransferOrderList
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomPlants_input{
      /**  The Transfer Order number list  */  
   TransferOrderList:string,
      /**  The pageSize  */  
   pageSize:number,
      /**  The absolutePage  */  
   absolutePage:number,
}

export interface GetRowsCustomPlants_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param TransferOrderList
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  The Transfer Order number list  */  
   TransferOrderList:string,
      /**  The pageSize  */  
   pageSize:number,
      /**  The absolutePage  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseTFOrdHed
      @param whereClauseTFOrdHedAttch
      @param whereClauseTFOrdDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTFOrdHed:string,
   whereClauseTFOrdHedAttch:string,
   whereClauseTFOrdDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetTransferShipDate_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface GetTransferShipDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
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
      @param partNum
      @param ds
      @param SysRowID
      @param rowType
   */  
export interface OnChangePartNum_input{
      /**  Part Number  */  
   partNum:string,
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   ds:Erp_Tablesets_TransferOrderEntryTableset,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTransferOrderEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTransferOrderEntryTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param tfOrdNum
      @param action
   */  
export interface UpdatePartAllocQueue_input{
      /**  The transfer order number  */  
   tfOrdNum:string,
      /**  The fulfillment queue action to take ("SEND" or "REMOVE")  */  
   action:string,
}

export interface UpdatePartAllocQueue_output{
   returnObj:Erp_Tablesets_TransferOrderEntryTableset[],
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TransferOrderEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferOrderEntryTableset,
}
}

