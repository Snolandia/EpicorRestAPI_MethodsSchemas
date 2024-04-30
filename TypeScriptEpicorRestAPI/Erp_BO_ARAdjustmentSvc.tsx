import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ARAdjustmentSvc
// Description: bo/ARAdjustment/ARAdjustment.p
           A/R Invoice Adjustment Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/$metadata", {
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
   Description: Get ARAdjustments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARAdjustments
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcHeadAdjRow
   */  
export function get_ARAdjustments(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadAdjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ARAdjustments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadAdjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARAdjustments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcHeadAdjRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.InvcHeadAdjRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARAdjustments(requestBody:Erp_Tablesets_InvcHeadAdjRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ARAdjustments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ARAdjustment item
   Description: Calls GetByID to retrieve the ARAdjustment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARAdjustment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.InvcHeadAdjRow
   */  
export function get_ARAdjustments_Company_InvoiceNum(Company:string, InvoiceNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcHeadAdjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ARAdjustments(" + Company + "," + InvoiceNum + ")", {
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
         resolve(data as Erp_Tablesets_InvcHeadAdjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARAdjustment for the service
   Description: Calls UpdateExt to update ARAdjustment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARAdjustment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcHeadAdjRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARAdjustments_Company_InvoiceNum(Company:string, InvoiceNum:string, requestBody:Erp_Tablesets_InvcHeadAdjRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ARAdjustments(" + Company + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete ARAdjustment item
   Description: Call UpdateExt to delete ARAdjustment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARAdjustment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARAdjustments_Company_InvoiceNum(Company:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ARAdjustments(" + Company + "," + InvoiceNum + ")", {
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
   Description: Get CashDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   */  
export function get_ARAdjustments_Company_InvoiceNum_CashDtls(Company:string, InvoiceNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ARAdjustments(" + Company + "," + InvoiceNum + ")/CashDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashDtlRow
   */  
export function get_ARAdjustments_Company_InvoiceNum_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, InvoiceNum:string, GroupID:string, HeadNum:string, InvoiceRef:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ARAdjustments(" + Company + "," + InvoiceNum + ")/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
         resolve(data as Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CashDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   */  
export function get_CashDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashDtls(requestBody:Erp_Tablesets_CashDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashDtlRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
         resolve(data as Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashDtl for the service
   Description: Calls UpdateExt to update CashDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, requestBody:Erp_Tablesets_CashDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Summary: Call UpdateExt to delete CashDtl item
   Description: Call UpdateExt to delete CashDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Description: Get CashDtlTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtlTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef_CashDtlTGLCs(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")/CashDtlTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtlTGLC item
   Description: Calls GetByID to retrieve the CashDtlTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef_CashDtlTGLCs_SysRowID(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")/CashDtlTGLCs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CashDtlTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtlTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtlTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtlTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtlTGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashDtlTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashDtlTGLCs(requestBody:Erp_Tablesets_CashDtlTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtlTGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CashDtlTGLC item
   Description: Calls GetByID to retrieve the CashDtlTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlTGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   */  
export function get_CashDtlTGLCs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtlTGLCs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_CashDtlTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashDtlTGLC for the service
   Description: Calls UpdateExt to update CashDtlTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtlTGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashDtlTGLCs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_CashDtlTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtlTGLCs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CashDtlTGLC item
   Description: Call UpdateExt to delete CashDtlTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtlTGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashDtlTGLCs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CashDtlTGLCs(" + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcHeadAdjListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadAdjListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadAdjListRow)
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
export function get_GetRows(whereClauseInvcHeadAdj:string, whereClauseCashDtl:string, whereClauseCashDtlTGLC:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseInvcHeadAdj!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcHeadAdj=" + whereClauseInvcHeadAdj
   }
   if(typeof whereClauseCashDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashDtl=" + whereClauseCashDtl
   }
   if(typeof whereClauseCashDtlTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashDtlTGLC=" + whereClauseCashDtlTGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetRows" + params, {
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
export function get_GetByID(invoiceNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetList" + params, {
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
   Summary: Invoke method ChangeGLAcctDisp
   Description: This method updates the GLAcctDisp when the transaction
G/L Account changes.
   OperationID: ChangeGLAcctDisp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLAcctDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLAcctDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLAcctDisp(requestBody:ChangeGLAcctDisp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLAcctDisp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ChangeGLAcctDisp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeGLAcctDisp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeAdjAmount
   Description: This method updates the CashDtl details when the adjustment amount changes or
the currency switch toggles.  Use the external fields CashDtl.DispTranAmt and
CashDtl.DocDispTranAmt to accept the user entered adjustment amount.
   OperationID: ChangeAdjAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAdjAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAdjAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAdjAmount(requestBody:ChangeAdjAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAdjAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ChangeAdjAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeAdjAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCopyRate
   Description: This method updates exchange rate for the transaction and update currency gain/loss
date changes.
   OperationID: ChangeCopyRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCopyRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCopyRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCopyRate(requestBody:ChangeCopyRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCopyRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ChangeCopyRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCopyRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRateGroupCode
   Description: This method updates the CashDtl details when Rate Group code is changed
   OperationID: ChangeRateGroupCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRateGroupCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateGroupCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRateGroupCode(requestBody:ChangeRateGroupCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRateGroupCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ChangeRateGroupCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRateGroupCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranDate
   Description: This method updates the CashDtl fiscal period and year when the transaction
date changes.
   OperationID: ChangeTranDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranDate(requestBody:ChangeTranDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTranDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ChangeTranDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTranDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentIsLocked(requestBody:CheckDocumentIsLocked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDocumentIsLocked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckDocumentIsLocked_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckGLInterface
   Description: Call this method once to validate the G/L Interface.  This method checks for
GLSyst availability and if G/L is interfaced with A/R. If A/R is not interfaced
with G/L then user should be asked if okay to continue without posting to G/L.
This method will return a Message for the user if not interfaced else the Message
is blank. If the user do not wish to continue then exit this object. This method
also returns a logical flag to indicate if Posting to G/L.  This value should be
passed on to each new A/R Adjustment (CashDtl) record to process.
   OperationID: CheckGLInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGLInterface(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckGLInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/CheckGLInterface", {
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
         resolve(data as CheckGLInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateLegalNumber
   Description: This method generates a legal number if necessary
date changes.
   OperationID: GenerateLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateLegalNumber(requestBody:GenerateLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GenerateLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenerateLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashDtl1
   Description: This method is to be used in place of GetNewCashDtl.  This method asks for
invoice number to link the A/R Invoice Header (InvcHead) to A/R Invoice
Adjustment (CashDtl).
   OperationID: GetNewCashDtl1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashDtl1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtl1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashDtl1(requestBody:GetNewCashDtl1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashDtl1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetNewCashDtl1", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashDtl1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTrandocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: OnChangeTrandocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTrandocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTrandocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTrandocTypeID(requestBody:OnChangeTrandocTypeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTrandocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/OnChangeTrandocTypeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTrandocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateTransaction
   Description: This method checks that all necessary data are entered, that should be done before adjustment.
   OperationID: ValidateTransaction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTransaction(requestBody:ValidateTransaction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateTransaction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/ValidateTransaction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateTransaction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNum
   Description: Void legal number is AR Adjust is not posted
   OperationID: VoidLegalNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidLegalNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNum(requestBody:VoidLegalNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidLegalNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/VoidLegalNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VoidLegalNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewInvcHeadAdj
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcHeadAdj
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewInvcHeadAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcHeadAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcHeadAdj(requestBody:GetNewInvcHeadAdj_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewInvcHeadAdj_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetNewInvcHeadAdj", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewInvcHeadAdj_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashDtl(requestBody:GetNewCashDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetNewCashDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashDtlTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtlTGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashDtlTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtlTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashDtlTGLC(requestBody:GetNewCashDtlTGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashDtlTGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetNewCashDtlTGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashDtlTGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAdjustmentSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashDtlTGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadAdjListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcHeadAdjListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadAdjRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcHeadAdjRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Erp_Tablesets_CashDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  */  
   "GroupID":string,
      /**  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  */  
   "HeadNum":number,
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   "InvoiceNum":number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   "InvoiceRef":number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   "TranType":string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger Module.  */  
   "GLPosted":boolean,
      /**  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  */  
   "TranDate":string,
      /**   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   "CheckRef":string,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  */  
   "TranAmt":number,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  */  
   "DocTranAmt":number,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   "Discount":number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   "DocDiscount":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  */  
   "Comment":string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   "Reference":string,
      /**   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  */  
   "DebitNote":boolean,
      /**  Debit Note Detail Comments.  */  
   "DNComments":string,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DNAmount":number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DocDnAmount":number,
      /**  The Debit Note Number assigned by the customer.  */  
   "DNCustNbr":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal Year Suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt No. (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date  (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate No. (Thailand Localization)  */  
   "WHTCertificateNo":string,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  Invoice Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  SEPADDMsgID  */  
   "SEPADDMsgID":string,
      /**  SEPADDPmtID  */  
   "SEPADDPmtID":string,
      /**  PmtDueDate  */  
   "PmtDueDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  MX Payment Number for AR Invoice  */  
   "MXPaymentNum":number,
      /**  Reference to HeadNum of main CashHead record.  */  
   "WriteOffHeadNumRef":number,
      /**  EpicorFSA  */  
   "EpicorFSA":boolean,
      /**  Taxable Adjustment  */  
   "TaxableAdjustment":boolean,
   "ApplyDate":string,
      /**  Adjustment amount in Base Currency  */  
   "BaseAdjAmt":number,
   "BaseCurrDesc":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  */  
   "BillConNum":number,
      /**  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  */  
   "CopyRate":boolean,
      /**  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  */  
   "CorrectionInv":boolean,
   "CreditMemo":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyDescription":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol  */  
   "CurrSymbol":string,
      /**  This field displays all Debit Note customer defined numbers applied.  */  
   "DebitNotesApplied":string,
   "DispDocSelfAssessAmt":number,
   "DispDocWithholdAmt":number,
      /**  Display gl account  */  
   "DispGLAcct":string,
   "DispSelfAssessAmt":number,
   "DispTranAmt":number,
   "DispWithholdAmt":number,
   "DocDispTranAmt":number,
      /**  Doc Invoice Amount  */  
   "DocInvoiceAmt":number,
      /**  Doc Invoice Balance  */  
   "DocInvoiceBal":number,
   "DocNetCash":number,
      /**  Doc New Invoice Balance  */  
   "DocNewBalance":number,
      /**  Write Off Amount  */  
   "DocWriteOffAmount":number,
      /**  If this flag is true then CopyRate checkbox is Read Only  */  
   "DsblCopyRate":boolean,
      /**  Legal Number Field  */  
   "EnableAssignLegNum":boolean,
   "EnableTranDocType":boolean,
      /**  Legal Number Field  */  
   "EnableVoidLegNum":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   "FullyPaid":boolean,
   "GainLossAmt":number,
      /**  G/L Reference Code Description  */  
   "GLRefCodeDesc":string,
      /**  Legal Number Field  */  
   "HasLegNumCnfg":boolean,
   "InvDiscountDate":string,
   "InvDueDate":string,
      /**  Invoice Exchange Rate  */  
   "InvExchRate":number,
   "InvLegalNumber":string,
   "InvLockRate":boolean,
      /**  Invoice Amount  */  
   "InvoiceAmt":number,
      /**  Invoice Balance  */  
   "InvoiceBal":number,
   "InvTermsCode":string,
   "InvXRateLabel":string,
      /**  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  */  
   "IsCreditPayment":boolean,
   "IsDiscountforCreditM":boolean,
   "LegalNumMessage":string,
   "LegalNumStyle":string,
   "NetCash":number,
      /**  New Invoice Balance  */  
   "NewBalance":number,
   "OldGainLoss":number,
      /**  The related order number (InvcHead.OrderNum)  */  
   "OrderNum":number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   "PNRef":string,
      /**  Indicates if posting GL transactions  */  
   "PostToGL":boolean,
      /**  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  */  
   "RecalcTranAmt":boolean,
   "RedStornoOpt":string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   "RefCodeStatus":string,
      /**  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  */  
   "RemoveForAdjustment":boolean,
   "Rpt1DispTranAmt":number,
   "Rpt1GainLossAmt":number,
   "Rpt1InvoiceAmt":number,
   "Rpt1InvoiceBal":number,
   "Rpt1NetCash":number,
   "Rpt1NewBalance":number,
   "Rpt1OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt1WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt1WriteOffGainLossAmt":number,
   "Rpt2DispTranAmt":number,
   "Rpt2GainLossAmt":number,
   "Rpt2InvoiceAmt":number,
   "Rpt2InvoiceBal":number,
   "Rpt2NetCash":number,
   "Rpt2NewBalance":number,
   "Rpt2OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt2WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt2WriteOffGainLossAmt":number,
   "Rpt3DispTranAmt":number,
   "Rpt3GainLossAmt":number,
   "Rpt3InvoiceAmt":number,
   "Rpt3InvoiceBal":number,
   "Rpt3NetCash":number,
   "Rpt3NewBalance":number,
   "Rpt3OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt3WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt3WriteOffGainLossAmt":number,
      /**  CustID associated with CashDtl.SoldToCustNum  */  
   "SoldToCustID":string,
      /**  Populated from InvcHead.SoldToCustNum.  */  
   "SoldToCustNum":number,
      /**  CustName associated with CashDtl.SoldToCustNum  */  
   "SoldToCustomerName":string,
      /**  Legal Number Field  */  
   "SystemTranType":string,
      /**  Description of the Tran Type  */  
   "TranTypeDesc":string,
      /**  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  */  
   "Type":string,
      /**  Write Off  */  
   "WriteOff":boolean,
      /**  Write Off Account  */  
   "WriteOffAccount":string,
      /**  Write Off Account Description  */  
   "WriteOffAccountDesc":string,
      /**  Write Off Amount  */  
   "WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "WriteOffGainLossAmt":number,
   "XRateLabel":string,
      /**  Legal Number Field  */  
   "AllowChgAfterPrint":boolean,
      /**  Write Off Amount  */  
   "OldWriteOffAmount":number,
   "WriteOffAccountDisp":string,
   "TaxableWriteOff":boolean,
      /**  Total Gain Loss Amount  */  
   "TotalGainLossAmt":number,
      /**  Write Off Amount  */  
   "OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt1OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt2OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt3OldWriteOffGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt1TotalGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt2TotalGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt3TotalGainLossAmt":number,
      /**  Write Off Amount  */  
   "DocOldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt1OldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt2OldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt3OldWriteOffAmount":number,
      /**  Allows uset to enter comment for Write Off.  */  
   "WriteOffComment":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
   "ReferenceTranDate":string,
   "ReferenceTranNum":number,
   "ReferenceTranTime":number,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   "EnableManualWHTax":boolean,
      /**  Indicates if the withholding amount tax was manually modified.  */  
   "WHTaxManualChange":boolean,
   "BitFlag":number,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "InvoiceNumInvoiceType":string,
   "InvoiceNumCardMemberName":string,
   "InvoiceNumTermsCode":string,
   "RateGrpDescription":string,
   "TaxRgnDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashDtlTGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
      /**  HeadNum of CashDtl  */  
   "HeadNum":number,
      /**  InvoiceNum of CashDtl  */  
   "InvoiceNum":number,
      /**  InvoiceRef of CashDtl  */  
   "InvoiceRef":number,
      /**  GroupID of CashDtl  */  
   "GroupID":string,
   "CDSeqNum":number,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountGLShortAcct":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountAccountDesc":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InvcHeadAdjListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if invoice is "open".  */  
   "OpenInvoice":boolean,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   "CreditMemo":boolean,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   "InvoiceType":string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   "CustNum":number,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   "InvoiceDate":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "InvoiceBal":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "DocInvoiceBal":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceBal":number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Switch  */  
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "BaseCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InvcHeadAdjRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if invoice is "open".  */  
   "OpenInvoice":boolean,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   "CreditMemo":boolean,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   "InvoiceType":string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   "CustNum":number,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   "InvoiceDate":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "InvoiceBal":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "DocInvoiceBal":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceBal":number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Switch  */  
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "BaseCurrencyID":string,
      /**  Indictes if this invoice is Correction Invoice with negative amount  */  
   "CorrectionInvNeg":boolean,
   "BitFlag":number,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrName":string,
   "CurrencyCurrencyID":string,
   "CurrencyDocumentDesc":string,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "CustomerName":string,
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




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
export interface ChangeAdjAmount_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface ChangeAdjAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
   reload:boolean,
}
}

   /** Required : 
      @param proposedCopyRate
      @param ds
   */  
export interface ChangeCopyRate_input{
      /**  The proposed flag to copy or not to copy the exchange rates of the invoice  */  
   proposedCopyRate:boolean,
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface ChangeCopyRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ipCompany
      @param ipCOACode
      @param ipGLAccount
   */  
export interface ChangeGLAcctDisp_input{
      /**  TranGLC Company for G/L Account  */  
   ipCompany:string,
      /**  TranGLC COA Code for G/L Account  */  
   ipCOACode:string,
      /**  TranGLC G/L Account  */  
   ipGLAccount:string,
}

export interface ChangeGLAcctDisp_output{
}

   /** Required : 
      @param ipRateGrpCode
      @param ds
   */  
export interface ChangeRateGroupCode_input{
      /**  Proposed input value of Income Tax Code  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface ChangeRateGroupCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTranDate_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface ChangeTranDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param keyValue
   */  
export interface CheckDocumentIsLocked_input{
      /**  InvoiceNum  */  
   keyValue:string,
}

export interface CheckDocumentIsLocked_output{
}

export interface CheckGLInterface_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opPostToGL:boolean,
}
}

   /** Required : 
      @param invoiceNum
   */  
export interface DeleteByID_input{
   invoiceNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ARAdjustmentTableset{
   InvcHeadAdj:Erp_Tablesets_InvcHeadAdjRow[],
   CashDtl:Erp_Tablesets_CashDtlRow[],
   CashDtlTGLC:Erp_Tablesets_CashDtlTGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  */  
   GroupID:string,
      /**  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  */  
   HeadNum:number,
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   InvoiceNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   TranType:string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger Module.  */  
   GLPosted:boolean,
      /**  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  */  
   TranDate:string,
      /**   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  */  
   TranAmt:number,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  */  
   DocTranAmt:number,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   Discount:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   DocDiscount:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  */  
   Comment:string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   Reference:string,
      /**   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  */  
   DebitNote:boolean,
      /**  Debit Note Detail Comments.  */  
   DNComments:string,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DNAmount:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DocDnAmount:number,
      /**  The Debit Note Number assigned by the customer.  */  
   DNCustNbr:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal Year Suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt No. (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date  (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate No. (Thailand Localization)  */  
   WHTCertificateNo:string,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  SEPADDMsgID  */  
   SEPADDMsgID:string,
      /**  SEPADDPmtID  */  
   SEPADDPmtID:string,
      /**  PmtDueDate  */  
   PmtDueDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  MX Payment Number for AR Invoice  */  
   MXPaymentNum:number,
      /**  Reference to HeadNum of main CashHead record.  */  
   WriteOffHeadNumRef:number,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  Taxable Adjustment  */  
   TaxableAdjustment:boolean,
   ApplyDate:string,
      /**  Adjustment amount in Base Currency  */  
   BaseAdjAmt:number,
   BaseCurrDesc:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  */  
   BillConNum:number,
      /**  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  */  
   CopyRate:boolean,
      /**  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  */  
   CorrectionInv:boolean,
   CreditMemo:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyDescription:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol  */  
   CurrSymbol:string,
      /**  This field displays all Debit Note customer defined numbers applied.  */  
   DebitNotesApplied:string,
   DispDocSelfAssessAmt:number,
   DispDocWithholdAmt:number,
      /**  Display gl account  */  
   DispGLAcct:string,
   DispSelfAssessAmt:number,
   DispTranAmt:number,
   DispWithholdAmt:number,
   DocDispTranAmt:number,
      /**  Doc Invoice Amount  */  
   DocInvoiceAmt:number,
      /**  Doc Invoice Balance  */  
   DocInvoiceBal:number,
   DocNetCash:number,
      /**  Doc New Invoice Balance  */  
   DocNewBalance:number,
      /**  Write Off Amount  */  
   DocWriteOffAmount:number,
      /**  If this flag is true then CopyRate checkbox is Read Only  */  
   DsblCopyRate:boolean,
      /**  Legal Number Field  */  
   EnableAssignLegNum:boolean,
   EnableTranDocType:boolean,
      /**  Legal Number Field  */  
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
   GainLossAmt:number,
      /**  G/L Reference Code Description  */  
   GLRefCodeDesc:string,
      /**  Legal Number Field  */  
   HasLegNumCnfg:boolean,
   InvDiscountDate:string,
   InvDueDate:string,
      /**  Invoice Exchange Rate  */  
   InvExchRate:number,
   InvLegalNumber:string,
   InvLockRate:boolean,
      /**  Invoice Amount  */  
   InvoiceAmt:number,
      /**  Invoice Balance  */  
   InvoiceBal:number,
   InvTermsCode:string,
   InvXRateLabel:string,
      /**  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  */  
   IsCreditPayment:boolean,
   IsDiscountforCreditM:boolean,
   LegalNumMessage:string,
   LegalNumStyle:string,
   NetCash:number,
      /**  New Invoice Balance  */  
   NewBalance:number,
   OldGainLoss:number,
      /**  The related order number (InvcHead.OrderNum)  */  
   OrderNum:number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   PNRef:string,
      /**  Indicates if posting GL transactions  */  
   PostToGL:boolean,
      /**  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  */  
   RecalcTranAmt:boolean,
   RedStornoOpt:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
      /**  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  */  
   RemoveForAdjustment:boolean,
   Rpt1DispTranAmt:number,
   Rpt1GainLossAmt:number,
   Rpt1InvoiceAmt:number,
   Rpt1InvoiceBal:number,
   Rpt1NetCash:number,
   Rpt1NewBalance:number,
   Rpt1OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt1WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt1WriteOffGainLossAmt:number,
   Rpt2DispTranAmt:number,
   Rpt2GainLossAmt:number,
   Rpt2InvoiceAmt:number,
   Rpt2InvoiceBal:number,
   Rpt2NetCash:number,
   Rpt2NewBalance:number,
   Rpt2OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt2WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt2WriteOffGainLossAmt:number,
   Rpt3DispTranAmt:number,
   Rpt3GainLossAmt:number,
   Rpt3InvoiceAmt:number,
   Rpt3InvoiceBal:number,
   Rpt3NetCash:number,
   Rpt3NewBalance:number,
   Rpt3OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt3WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt3WriteOffGainLossAmt:number,
      /**  CustID associated with CashDtl.SoldToCustNum  */  
   SoldToCustID:string,
      /**  Populated from InvcHead.SoldToCustNum.  */  
   SoldToCustNum:number,
      /**  CustName associated with CashDtl.SoldToCustNum  */  
   SoldToCustomerName:string,
      /**  Legal Number Field  */  
   SystemTranType:string,
      /**  Description of the Tran Type  */  
   TranTypeDesc:string,
      /**  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  */  
   Type:string,
      /**  Write Off  */  
   WriteOff:boolean,
      /**  Write Off Account  */  
   WriteOffAccount:string,
      /**  Write Off Account Description  */  
   WriteOffAccountDesc:string,
      /**  Write Off Amount  */  
   WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   WriteOffGainLossAmt:number,
   XRateLabel:string,
      /**  Legal Number Field  */  
   AllowChgAfterPrint:boolean,
      /**  Write Off Amount  */  
   OldWriteOffAmount:number,
   WriteOffAccountDisp:string,
   TaxableWriteOff:boolean,
      /**  Total Gain Loss Amount  */  
   TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt1TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt2TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt3TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   DocOldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffAmount:number,
      /**  Allows uset to enter comment for Write Off.  */  
   WriteOffComment:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding amount tax was manually modified.  */  
   WHTaxManualChange:boolean,
   BitFlag:number,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   InvoiceNumInvoiceType:string,
   InvoiceNumCardMemberName:string,
   InvoiceNumTermsCode:string,
   RateGrpDescription:string,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashDtlTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  HeadNum of CashDtl  */  
   HeadNum:number,
      /**  InvoiceNum of CashDtl  */  
   InvoiceNum:number,
      /**  InvoiceRef of CashDtl  */  
   InvoiceRef:number,
      /**  GroupID of CashDtl  */  
   GroupID:string,
   CDSeqNum:number,
   BitFlag:number,
   COADescription:string,
   GLAccountGLShortAcct:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadAdjListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceBal:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Switch  */  
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   BaseCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadAdjListTableset{
   InvcHeadAdjList:Erp_Tablesets_InvcHeadAdjListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcHeadAdjRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceBal:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Switch  */  
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   BaseCurrencyID:string,
      /**  Indictes if this invoice is Correction Invoice with negative amount  */  
   CorrectionInvNeg:boolean,
   BitFlag:number,
   CurrencyCurrSymbol:string,
   CurrencyCurrDesc:string,
   CurrencyCurrName:string,
   CurrencyCurrencyID:string,
   CurrencyDocumentDesc:string,
   CustomerBTName:string,
   CustomerCustID:string,
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_UpdExtARAdjustmentTableset{
   InvcHeadAdj:Erp_Tablesets_InvcHeadAdjRow[],
   CashDtl:Erp_Tablesets_CashDtlRow[],
   CashDtlTGLC:Erp_Tablesets_CashDtlTGLCRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateLegalNumber_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface GenerateLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param invoiceNum
   */  
export interface GetByID_input{
   invoiceNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARAdjustmentTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARAdjustmentTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARAdjustmentTableset[],
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
   returnObj:Erp_Tablesets_InvcHeadAdjListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param ipInvoiceNum
   */  
export interface GetNewCashDtl1_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
      /**  The A/R Invoice Number to adjust  */  
   ipInvoiceNum:number,
}

export interface GetNewCashDtl1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashDtlTGLC_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface GetNewCashDtlTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
      @param invoiceNum
   */  
export interface GetNewCashDtl_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
   groupID:string,
   headNum:number,
   invoiceNum:number,
}

export interface GetNewCashDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewInvcHeadAdj_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface GetNewInvcHeadAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param whereClauseInvcHeadAdj
      @param whereClauseCashDtl
      @param whereClauseCashDtlTGLC
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseInvcHeadAdj:string,
   whereClauseCashDtl:string,
   whereClauseCashDtlTGLC:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARAdjustmentTableset[],
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
      @param ipTranDocTypeID
      @param ds
   */  
export interface OnChangeTrandocTypeID_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface OnChangeTrandocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtARAdjustmentTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARAdjustmentTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateTransaction_input{
   ds:Erp_Tablesets_ARAdjustmentTableset[],
}

export interface ValidateTransaction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARAdjustmentTableset,
}
}

   /** Required : 
      @param ipHeadNum
      @param ipInvoiceNum
      @param ipLegalNumber
   */  
export interface VoidLegalNum_input{
      /**  CashDtl HeadNum  */  
   ipHeadNum:number,
      /**  Invoice Num  */  
   ipInvoiceNum:number,
      /**  Legal Number  */  
   ipLegalNumber:string,
}

export interface VoidLegalNum_output{
}

