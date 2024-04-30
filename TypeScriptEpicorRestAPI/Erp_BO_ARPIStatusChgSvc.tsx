import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ARPIStatusChgSvc
// Description: AR Payment Instrument Status Change Service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/$metadata", {
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
   Description: Get ARPIStatusChgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPIStatusChgs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadRow
   */  
export function get_ARPIStatusChgs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPIStatusChgs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ARPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPIStatusChgs(requestBody:Erp_Tablesets_ARPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ARPIStatusChg item
   Description: Calls GetByID to retrieve the ARPIStatusChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPIStatusChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNHeadRow
   */  
export function get_ARPIStatusChgs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_ARPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPIStatusChg for the service
   Description: Calls UpdateExt to update ARPIStatusChg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPIStatusChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPIStatusChgs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:Erp_Tablesets_ARPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete ARPIStatusChg item
   Description: Call UpdateExt to delete ARPIStatusChg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPIStatusChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPIStatusChgs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Description: Get ARPNDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPIStatusChgs_Company_GroupID_HeadNum_ARPNDtls(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPIStatusChgs_Company_GroupID_HeadNum_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPIStatusChgs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
         resolve(data as Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ARPNDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPNDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ARPNDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNDtls(requestBody:Erp_Tablesets_ARPNDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNDtlRow
   */  
export function get_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
         resolve(data as Erp_Tablesets_ARPNDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNDtl for the service
   Description: Calls UpdateExt to update ARPNDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, requestBody:Erp_Tablesets_ARPNDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Summary: Call UpdateExt to delete ARPNDtl item
   Description: Call UpdateExt to delete ARPNDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow)
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
export function get_GetRows(whereClauseARPNHead:string, whereClauseARPNDtl:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseARPNHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNHead=" + whereClauseARPNHead
   }
   if(typeof whereClauseARPNDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNDtl=" + whereClauseARPNDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetList" + params, {
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
   Summary: Invoke method AddSinglePI
   Description: Add a single PI to the group
   OperationID: AddSinglePI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddSinglePI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSinglePI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddSinglePI(requestBody:AddSinglePI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddSinglePI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/AddSinglePI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddSinglePI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BankExportToProcessFolder
   OperationID: BankExportToProcessFolder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BankExportToProcessFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankExportToProcessFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankExportToProcessFolder(requestBody:BankExportToProcessFolder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BankExportToProcessFolder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/BankExportToProcessFolder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BankExportToProcessFolder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BankExport
   Description: Create Bank Export output file
   OperationID: BankExport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BankExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankExport(requestBody:BankExport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BankExport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/BankExport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BankExport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteExportServerFile
   Description: Delete server file.
   OperationID: DeleteExportServerFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteExportServerFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteExportServerFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteExportServerFile(requestBody:DeleteExportServerFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteExportServerFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/DeleteExportServerFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteExportServerFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteLastARPNMove
   OperationID: DeleteLastARPNMove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteLastARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLastARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteLastARPNMove(requestBody:DeleteLastARPNMove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteLastARPNMove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/DeleteLastARPNMove", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteLastARPNMove_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupPIs
   Description: Get Current ARPNHead records for the group
   OperationID: GetGroupPIs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGroupPIs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupPIs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupPIs(requestBody:GetGroupPIs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGroupPIs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetGroupPIs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetGroupPIs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByGroup
   Description: Get Current ARPNHead records by group
   OperationID: GetByGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByGroup(requestBody:GetByGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetByGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByGroupHeadNum
   Description: Get Current ARPNHead records by group
   OperationID: GetByGroupHeadNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByGroupHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByGroupHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByGroupHeadNum(requestBody:GetByGroupHeadNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByGroupHeadNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetByGroupHeadNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByGroupHeadNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UndoCancelOnAccount
   Description: Undo credit Memo changes
   OperationID: UndoCancelOnAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UndoCancelOnAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoCancelOnAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UndoCancelOnAccount(requestBody:UndoCancelOnAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UndoCancelOnAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/UndoCancelOnAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UndoCancelOnAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessCancelOnAccount
   Description: Processes credit Memo
   OperationID: ProcessCancelOnAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessCancelOnAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessCancelOnAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessCancelOnAccount(requestBody:ProcessCancelOnAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessCancelOnAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ProcessCancelOnAccount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ProcessCancelOnAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveFromGroup
   Description: Removes AR PN records from the current group
   OperationID: RemoveFromGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveFromGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveFromGroup(requestBody:RemoveFromGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveFromGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/RemoveFromGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RemoveFromGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectPI
   Description: Search Payment Instruments to add to group
   OperationID: SelectPI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectPI(requestBody:SelectPI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectPI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/SelectPI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectPI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectPIData
   Description: Select Payment Instruments to add to group
   OperationID: SelectPIData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectPIData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectPIData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectPIData(requestBody:SelectPIData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectPIData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/SelectPIData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectPIData_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method ChangeStatusFromABR
   Description: Change ARPN status from ABR
   OperationID: ChangeStatusFromABR
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeStatusFromABR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatusFromABR_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStatusFromABR(requestBody:ChangeStatusFromABR_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeStatusFromABR_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/ChangeStatusFromABR", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeStatusFromABR_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnDiscountingCashDateChange
   Description: This method should be called on Discounting Cash Date changing.
   OperationID: OnDiscountingCashDateChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnDiscountingCashDateChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnDiscountingCashDateChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnDiscountingCashDateChange(requestBody:OnDiscountingCashDateChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnDiscountingCashDateChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/OnDiscountingCashDateChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnDiscountingCashDateChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnDiscountingChargeChange
   Description: This method should be called on Discounting Change changing.
   OperationID: OnDiscountingChargeChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnDiscountingChargeChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnDiscountingChargeChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnDiscountingChargeChange(requestBody:OnDiscountingChargeChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnDiscountingChargeChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/OnDiscountingChargeChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnDiscountingChargeChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnDiscountedAmountChange
   Description: This method should be called on Discounted amount changing.
   OperationID: OnDiscountedAmountChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnDiscountedAmountChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnDiscountedAmountChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnDiscountedAmountChange(requestBody:OnDiscountedAmountChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnDiscountedAmountChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/OnDiscountedAmountChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnDiscountedAmountChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the status change.
   OperationID: AssignLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLegalNumber(requestBody:AssignLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AssignLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumGenOpts(requestBody:GetLegalNumGenOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegalNumGenOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLegalNumGenOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumGenOptsFromABR
   Description: Returns the legal number generation options when called from ABR.
   OperationID: GetLegalNumGenOptsFromABR
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOptsFromABR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOptsFromABR_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumGenOptsFromABR(requestBody:GetLegalNumGenOptsFromABR_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegalNumGenOptsFromABR_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetLegalNumGenOptsFromABR", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLegalNumGenOptsFromABR_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumber(requestBody:VoidLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VoidLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePost
   Description: Ensure all data is ready to be posted.
   OperationID: PrePost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrePost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePost(requestBody:PrePost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrePost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/PrePost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PrePost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHead(requestBody:GetNewARPNHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewARPNHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetNewARPNHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewARPNHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewARPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNDtl(requestBody:GetNewARPNDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewARPNDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetNewARPNDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewARPNDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIStatusChgSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Erp_Tablesets_ARPNDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Discount Amount. Document Currency.  */  
   "DocDiscountAmount":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Rounding Difference  */  
   "RoundDiff":number,
      /**  Discount Amount. Report Currency 1.  */  
   "Rpt1DiscountAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Discount Amount. Report Currency 2.  */  
   "Rpt2DiscountAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Discount Amount. Report Currency 3.  */  
   "Rpt3DiscountAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Transaction Date  */  
   "TranDate":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  */  
   "HeadNum":number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   "InvoiceRef":number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DNAmount":number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DocDnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DnAmount":number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   "TranType":string,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   "FiscalPeriod":number,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal Year Suffix.  */  
   "FiscalYearSuffix":string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   "Reference":string,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  PI Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency PI Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "InvoiceDate":string,
   "DocInvoiceAmt":number,
   "CurrencyCode":string,
   "CurrencyDescription":string,
   "BaseCurrDesc":string,
   "BaseCurrSymbol":string,
   "DocInvoiceBal":number,
   "InvTermsCode":string,
   "InvDiscountDate":string,
   "InvDueDate":string,
   "DocNetCash":number,
   "DocNewBalance":number,
   "InvLockRate":boolean,
   "InvoiceBal":number,
   "NewBalance":number,
   "NetCash":number,
   "GainLossAmt":number,
   "ApplyDate":string,
   "BillConNumber":number,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
   "DispGLAcct":string,
   "DispTranAmt":number,
   "DocDispTranAmt":number,
   "DocSelfAssessTax":number,
   "DocWithholdTax":number,
   "FullyPaid":boolean,
   "InvExchRate":number,
   "InvLegalNumber":string,
   "InvoiceAmt":number,
   "InvXRateLabel":string,
   "LegalNumMessage":string,
   "LegalNumStyle":string,
   "OldGainLoss":number,
   "PostToGL":boolean,
   "SelfAssessTax":number,
   "SoldToCustID":string,
   "SoldToCustNum":number,
   "SoldToCustomerName":string,
   "WithholdTax":number,
   "XRateLabel":string,
   "Rpt1NewBalance":number,
   "Rpt3NewBalance":number,
   "Rpt1DispTranAmt":number,
   "Rpt2DispTranAmt":number,
   "Rpt3DispTranAmt":number,
   "Rpt1OldGainLoss":number,
   "Rpt2OldGainLoss":number,
   "Rpt3OldGainLoss":number,
   "Rpt1GainLossAmt":number,
   "Rpt2GainLossAmt":number,
   "Rpt3GainLossAmt":number,
   "Rpt1InvoiceAmt":number,
   "Rpt2InvoiceAmt":number,
   "Rpt3InvoiceAmt":number,
   "Rpt1InvoiceBal":number,
   "Rpt2InvoiceBal":number,
   "Rpt3InvoiceBal":number,
   "Rpt2NewBalance":number,
   "Rpt1NetCash":number,
   "Rpt2NetCash":number,
   "Rpt3NetCash":number,
   "InvoicePosted":boolean,
   "CurGroupID":string,
   "BitFlag":number,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "TaxRgnDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Applied Amount  */  
   "AppliedAmt":number,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  Company Bank Account ID  */  
   "CompBankAcctID":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Customer Bank Account ID  */  
   "CustBankAcctID":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Description  */  
   "Description":string,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Applied Amount. Document Currency.  */  
   "DocAppliedAmt":number,
      /**  Unapplied Amount. Document Currency.  */  
   "DocUnAppliedAmt":number,
      /**  Tax Amount. Document Currency.  */  
   "DocTaxAmt":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Withholding Amount. Document Currency.  */  
   "DocWithholdAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Paid flag  */  
   "Paid":boolean,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Process Card  */  
   "ProcessCard":string,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Recalculated before posting.  */  
   "RecalcBeforePost":boolean,
      /**  Applied Amount. Report Currency 1.  */  
   "Rpt1AppliedAmt":number,
      /**  Tax Amount. Report Currency 1.  */  
   "Rpt1TaxAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Unapplied Amount. Report Currency 1.  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 1.  */  
   "Rpt1WithholdAmt":number,
      /**  Applied Amount. Report Currency 2.  */  
   "Rpt2AppliedAmt":number,
      /**  Tax Amount. Report Currency 2.  */  
   "Rpt2TaxAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Unapplied Amount. Report Currency 2.  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 2.  */  
   "Rpt2WithholdAmt":number,
      /**  Applied Amount. Report Currency 3.  */  
   "Rpt3AppliedAmt":number,
      /**  Tax Amount. Report Currency 3.  */  
   "Rpt3TaxAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Unapplied Amount. Report Currency 3.  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 3.  */  
   "Rpt3WithholdAmt":number,
      /**  Signed flag  */  
   "Signed":boolean,
      /**  Tax Amount. Base Currency.  */  
   "TaxAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Total AR Amount  */  
   "TotalARAmt":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Unapplied Amount. Base Currency.  */  
   "UnappliedAmt":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  Withholding Amount. Base Currency.  */  
   "WithholdAmt":number,
      /**  Company Name  */  
   "CompanyName":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CustomerName":string,
      /**  First customer address line.  */  
   "CustomerAddr1":string,
      /**  Second customer address line.  */  
   "CustomerAddr2":string,
      /**  Third customer address line.  */  
   "CustomerAddr3":string,
      /**  Customer Stateportion of the address.  */  
   "CustomerState":string,
      /**  Customer City portion of the address.  */  
   "CustomerPostalCode":string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   "CustomerCity":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  AR Payment Instrument ID  */  
   "ARPromNoteID":string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Sent Flag  */  
   "Sent":boolean,
      /**  Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  IBANCode for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   "AutoGenerated":boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   "DirectDeposit":boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Customer's country code  */  
   "CustCountryCode":number,
      /**  Customer country portion of the address.  */  
   "CustomerCountry":string,
      /**  Promissory Note Status  */  
   "PIStatus":string,
      /**  Current Group  */  
   "CurGroupID":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Reason to change Company or Customer information  */  
   "ChgComment":string,
      /**  Hold from Application reason  */  
   "HoldReason":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Reference to reversed PI  */  
   "ReferseRef":number,
      /**  Reverse Date  */  
   "ReverseDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  DiscountCashDate  */  
   "DiscountCashDate":string,
   "BaseCurrSymbol":string,
   "BaseCurrencyCode":string,
   "BaseCurrencyDesc":string,
   "TermsDesc":string,
   "CurrencyDesc":string,
   "TotalCashReceived":number,
   "CompanyBankName":string,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CustomerBankName":string,
   "CustomerBankAcct":string,
   "CustomerBankIdentifier":string,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   "calcRate":boolean,
   "ApplyDate":string,
   "BankCurrencyCode":string,
   "BankCurrSymbol":string,
   "BillToName":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
   "CurrencySwitch":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocDiscount":number,
   "DocReceipt":number,
   "FullyPaid":boolean,
   "LegalNumMessage":string,
   "TotalRoundDiff":number,
   "TranTaxAmt":number,
   "XRateLabel":string,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
   "Rpt1TranTaxAmt":number,
   "Rpt2TranTaxAmt":number,
   "Rpt3TranTaxAmt":number,
   "CompBankBranchCodeDesc":string,
   "CustBankBranchCodeDesc":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
   "PIStatusDesc":string,
      /**  like PIType.Initiation  */  
   "PITypeInitiation":string,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
   "GainLossReal":number,
   "GainLossUnreal":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
   "RevalueDate":string,
   "DocDiscountAmt":number,
   "Rpt1DiscountAmt":number,
   "Rpt2DiscountAmt":number,
   "Rpt3DiscountAmt":number,
   "Receipt":number,
   "Rpt1Receipt":number,
   "Rpt2Receipt":number,
   "Rpt3Receipt":number,
      /**  The Bank's full name.  */  
   "BankAcctBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctDescription":string,
      /**  Description  */  
   "CashbookLineDescription":string,
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
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Status Description  */  
   "PIStatusStatusDesc":string,
      /**  Type Description  */  
   "PITypeDescription":string,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
   "BankRecGainLoss":number,
   "DocBankRecGainLoss":number,
   "Rpt1BankRecGainLoss":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt3BankRecGainLoss":number,
   "BankTotalAmount":number,
   "StatusChgTranDocType":string,
   "StatusChgLegalNum":string,
      /**  for kinetic purposes  */  
   "ARPNDtlExists":boolean,
      /**  for kinetic purposes  */  
   "ARPNDtlInvoicePosted":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Applied Amount  */  
   "AppliedAmt":number,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  Company Bank Account ID  */  
   "CompBankAcctID":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Customer Bank Account ID  */  
   "CustBankAcctID":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Description  */  
   "Description":string,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Applied Amount. Document Currency.  */  
   "DocAppliedAmt":number,
      /**  Unapplied Amount. Document Currency.  */  
   "DocUnAppliedAmt":number,
      /**  Tax Amount. Document Currency.  */  
   "DocTaxAmt":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Withholding Amount. Document Currency.  */  
   "DocWithholdAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Paid flag  */  
   "Paid":boolean,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Process Card  */  
   "ProcessCard":string,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Recalculated before posting.  */  
   "RecalcBeforePost":boolean,
      /**  Applied Amount. Report Currency 1.  */  
   "Rpt1AppliedAmt":number,
      /**  Tax Amount. Report Currency 1.  */  
   "Rpt1TaxAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Unapplied Amount. Report Currency 1.  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 1.  */  
   "Rpt1WithholdAmt":number,
      /**  Applied Amount. Report Currency 2.  */  
   "Rpt2AppliedAmt":number,
      /**  Tax Amount. Report Currency 2.  */  
   "Rpt2TaxAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Unapplied Amount. Report Currency 2.  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 2.  */  
   "Rpt2WithholdAmt":number,
      /**  Applied Amount. Report Currency 3.  */  
   "Rpt3AppliedAmt":number,
      /**  Tax Amount. Report Currency 3.  */  
   "Rpt3TaxAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Unapplied Amount. Report Currency 3.  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 3.  */  
   "Rpt3WithholdAmt":number,
      /**  Signed flag  */  
   "Signed":boolean,
      /**  Tax Amount. Base Currency.  */  
   "TaxAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Total AR Amount  */  
   "TotalARAmt":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Unapplied Amount. Base Currency.  */  
   "UnappliedAmt":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  Withholding Amount. Base Currency.  */  
   "WithholdAmt":number,
      /**  Company Name  */  
   "CompanyName":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CustomerName":string,
      /**  First customer address line.  */  
   "CustomerAddr1":string,
      /**  Second customer address line.  */  
   "CustomerAddr2":string,
      /**  Third customer address line.  */  
   "CustomerAddr3":string,
      /**  Customer Stateportion of the address.  */  
   "CustomerState":string,
      /**  Customer City portion of the address.  */  
   "CustomerPostalCode":string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   "CustomerCity":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  AR Payment Instrument ID  */  
   "ARPromNoteID":string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Sent Flag  */  
   "Sent":boolean,
      /**  Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  IBANCode for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   "AutoGenerated":boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   "DirectDeposit":boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Customer's country code  */  
   "CustCountryCode":number,
      /**  Customer country portion of the address.  */  
   "CustomerCountry":string,
      /**  Promissory Note Status  */  
   "PIStatus":string,
      /**  Current Group  */  
   "CurGroupID":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Reason to change Company or Customer information  */  
   "ChgComment":string,
      /**  Hold from Application reason  */  
   "HoldReason":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Reference to reversed PI  */  
   "ReferseRef":number,
      /**  Reverse Date  */  
   "ReverseDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  TotalBankFee  */  
   "TotalBankFee":number,
      /**  DocTotalBankFee  */  
   "DocTotalBankFee":number,
      /**  Rpt1TotalBankFee  */  
   "Rpt1TotalBankFee":number,
      /**  Rpt2TotalBankFee  */  
   "Rpt2TotalBankFee":number,
      /**  Rpt3TotalBankFee  */  
   "Rpt3TotalBankFee":number,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  Issuer Name  */  
   "IssuerName":string,
      /**  Signed By  */  
   "SignedBy":string,
      /**  Signed Date  */  
   "SignedDate":string,
      /**  Signee Address 1  */  
   "SigneeAddr1":string,
      /**  Signee Address 2  */  
   "SigneeAddr2":string,
      /**  Signee Address 3  */  
   "SigneeAddr3":string,
      /**  Signee City  */  
   "SigneeCity":string,
      /**  Signee State  */  
   "SigneeState":string,
      /**  Signee Postal Code  */  
   "SigneeZip":string,
      /**  Signee Country Number  */  
   "SigneeCountryNum":number,
      /**  Signee Phone  */  
   "SigneePhoneNum":string,
      /**  Signee Email Address  */  
   "SigneeEMailAddress":string,
      /**  Signee Comment  */  
   "SigneeComment":string,
      /**  DiscountChargeAmt  */  
   "DiscountChargeAmt":number,
      /**  DocDiscountChargeAmt  */  
   "DocDiscountChargeAmt":number,
      /**  Rpt1DiscountChargeAmt  */  
   "Rpt1DiscountChargeAmt":number,
      /**  Rpt2DiscountChargeAmt  */  
   "Rpt2DiscountChargeAmt":number,
      /**  Rpt3DiscountChargeAmt  */  
   "Rpt3DiscountChargeAmt":number,
      /**  Signee Bank Name  */  
   "SigneeBankName":string,
      /**  Signee Bank Account Number  */  
   "SigneeBankAcct":string,
      /**  Signee Bank Identifier  */  
   "SigneeBankIdentifier":string,
      /**  Signee IBAN Code  */  
   "SigneeIBANCode":string,
      /**  Signee Bank BranchCode  */  
   "SigneeBankBranchCode":string,
      /**  DiscountCashDate  */  
   "DiscountCashDate":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
   "ApplyDate":string,
   "BankCurrencyCode":string,
   "BankCurrSymbol":string,
   "BankRecGainLoss":number,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   "calcRate":boolean,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CompanyBankName":string,
   "CompBankBranchCodeDesc":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
   "CurrencyDesc":string,
   "CurrencySwitch":boolean,
   "CustBankBranchCodeDesc":string,
   "CustomerBankAcct":string,
   "CustomerBankIdentifier":string,
   "CustomerBankName":string,
   "DisableBankAcctIDPI":boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocBankRecGainLoss":number,
   "DocDiscount":number,
   "DocDiscountAmt":number,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
   "FullyPaid":boolean,
   "GainLossReal":number,
   "GainLossUnreal":number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PIStatusDesc":string,
      /**  like PIType.Initiation  */  
   "PITypeInitiation":string,
   "Receipt":number,
   "RevalueDate":string,
   "Rpt1BankRecGainLoss":number,
   "Rpt1DiscountAmt":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt1Receipt":number,
   "Rpt1TranTaxAmt":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt2DiscountAmt":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt2Receipt":number,
   "Rpt2TranTaxAmt":number,
   "Rpt3BankRecGainLoss":number,
   "Rpt3DiscountAmt":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
   "Rpt3Receipt":number,
   "Rpt3TranTaxAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "StatusChgLegalNum":string,
   "StatusChgTranDocType":string,
   "TermsDesc":string,
   "TotalCashReceived":number,
   "TotalRoundDiff":number,
   "TranTaxAmt":number,
   "TypeDesc":string,
   "XRateLabel":string,
   "BankTotalAmount":number,
   "BaseCurrencyCode":string,
   "BaseCurrencyDesc":string,
   "BaseCurrSymbol":string,
   "BillToName":string,
   "DocDiscountedAmt":number,
      /**  for kinetic purposes  */  
   "ARPNDtlExists":boolean,
      /**  for kinetic purposes  */  
   "ARPNDtlInvoicePosted":boolean,
   "BitFlag":number,
   "BankAcctDescription":string,
   "BankAcctBankName":string,
   "CashbookLineDescription":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CustNumInactive":boolean,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "PIStatusStatusDesc":string,
   "PITypeDescription":string,
   "RateGrpDescription":string,
   "TaxRegionCodeDescription":string,
   "TranDocTypeDescription":string,
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
      @param piGroup
      @param piHeadNum
      @param piNewGroup
      @param piGrpStatus
   */  
export interface AddSinglePI_input{
      /**  Header Group ID  */  
   piGroup:string,
      /**  Header Number  */  
   piHeadNum:number,
      /**  New Group ID  */  
   piNewGroup:string,
      /**  Group Status  */  
   piGrpStatus:string,
}

export interface AddSinglePI_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
}

   /** Required : 
      @param ds
      @param ipGroupID
      @param ipHeadNum
   */  
export interface AssignLegalNumber_input{
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
      /**  Group ID  */  
   ipGroupID:string,
      /**  Payment Instrument Head Number  */  
   ipHeadNum:number,
}

export interface AssignLegalNumber_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
parameters : {
      /**  output parameters  */  
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipFileFormat
   */  
export interface BankExportToProcessFolder_input{
   ipGroupID:string,
   ipFileFormat:number,
}

export interface BankExportToProcessFolder_output{
parameters : {
      /**  output parameters  */  
   ipOutRelativeFileName:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipFileFormat
      @param ipOutFileName
   */  
export interface BankExport_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Output File Format  */  
   ipFileFormat:number,
      /**  Output Filename  */  
   ipOutFileName:string,
}

export interface BankExport_output{
parameters : {
      /**  output parameters  */  
   ipOutFileName:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipCurGroupID
      @param ipHeadNum
      @param ipPIStatus
      @param ipTranDate
      @param ipLegalNumGenOpts
      @param ipTranDocTypeID
   */  
export interface ChangeStatusFromABR_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Current Group ID  */  
   ipCurGroupID:string,
      /**  HeadNum  */  
   ipHeadNum:number,
      /**  PIStatus  */  
   ipPIStatus:string,
      /**  TranDate  */  
   ipTranDate:string,
      /**  Legal Number defaults  */  
   ipLegalNumGenOpts:string,
      /**  TranDocType  */  
   ipTranDocTypeID:string,
}

export interface ChangeStatusFromABR_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
parameters : {
      /**  output parameters  */  
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface DeleteByID_input{
   groupID:string,
   headNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param serverFile
   */  
export interface DeleteExportServerFile_input{
      /**  Server file path  */  
   serverFile:string,
}

export interface DeleteExportServerFile_output{
}

   /** Required : 
      @param ipGroupID
   */  
export interface DeleteLastARPNMove_input{
      /**  ipGroupID  */  
   ipGroupID:string,
}

export interface DeleteLastARPNMove_output{
}

export interface Erp_Tablesets_ARPIStatusChgTableset{
   ARPNHead:Erp_Tablesets_ARPNHeadRow[],
   ARPNDtl:Erp_Tablesets_ARPNDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPNDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Discount Amount. Document Currency.  */  
   DocDiscountAmount:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Rounding Difference  */  
   RoundDiff:number,
      /**  Discount Amount. Report Currency 1.  */  
   Rpt1DiscountAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Discount Amount. Report Currency 2.  */  
   Rpt2DiscountAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Discount Amount. Report Currency 3.  */  
   Rpt3DiscountAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  */  
   HeadNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DNAmount:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DocDnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3DnAmount:number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   TranType:string,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   FiscalPeriod:number,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal Year Suffix.  */  
   FiscalYearSuffix:string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   Reference:string,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  PI Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency PI Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency PI Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   InvoiceDate:string,
   DocInvoiceAmt:number,
   CurrencyCode:string,
   CurrencyDescription:string,
   BaseCurrDesc:string,
   BaseCurrSymbol:string,
   DocInvoiceBal:number,
   InvTermsCode:string,
   InvDiscountDate:string,
   InvDueDate:string,
   DocNetCash:number,
   DocNewBalance:number,
   InvLockRate:boolean,
   InvoiceBal:number,
   NewBalance:number,
   NetCash:number,
   GainLossAmt:number,
   ApplyDate:string,
   BillConNumber:number,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DispGLAcct:string,
   DispTranAmt:number,
   DocDispTranAmt:number,
   DocSelfAssessTax:number,
   DocWithholdTax:number,
   FullyPaid:boolean,
   InvExchRate:number,
   InvLegalNumber:string,
   InvoiceAmt:number,
   InvXRateLabel:string,
   LegalNumMessage:string,
   LegalNumStyle:string,
   OldGainLoss:number,
   PostToGL:boolean,
   SelfAssessTax:number,
   SoldToCustID:string,
   SoldToCustNum:number,
   SoldToCustomerName:string,
   WithholdTax:number,
   XRateLabel:string,
   Rpt1NewBalance:number,
   Rpt3NewBalance:number,
   Rpt1DispTranAmt:number,
   Rpt2DispTranAmt:number,
   Rpt3DispTranAmt:number,
   Rpt1OldGainLoss:number,
   Rpt2OldGainLoss:number,
   Rpt3OldGainLoss:number,
   Rpt1GainLossAmt:number,
   Rpt2GainLossAmt:number,
   Rpt3GainLossAmt:number,
   Rpt1InvoiceAmt:number,
   Rpt2InvoiceAmt:number,
   Rpt3InvoiceAmt:number,
   Rpt1InvoiceBal:number,
   Rpt2InvoiceBal:number,
   Rpt3InvoiceBal:number,
   Rpt2NewBalance:number,
   Rpt1NetCash:number,
   Rpt2NetCash:number,
   Rpt3NetCash:number,
   InvoicePosted:boolean,
   CurGroupID:string,
   BitFlag:number,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Applied Amount  */  
   AppliedAmt:number,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Company Bank Account ID  */  
   CompBankAcctID:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Customer Bank Account ID  */  
   CustBankAcctID:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Description  */  
   Description:string,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Applied Amount. Document Currency.  */  
   DocAppliedAmt:number,
      /**  Unapplied Amount. Document Currency.  */  
   DocUnAppliedAmt:number,
      /**  Tax Amount. Document Currency.  */  
   DocTaxAmt:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Withholding Amount. Document Currency.  */  
   DocWithholdAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Paid flag  */  
   Paid:boolean,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Process Card  */  
   ProcessCard:string,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Recalculated before posting.  */  
   RecalcBeforePost:boolean,
      /**  Applied Amount. Report Currency 1.  */  
   Rpt1AppliedAmt:number,
      /**  Tax Amount. Report Currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Unapplied Amount. Report Currency 1.  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 1.  */  
   Rpt1WithholdAmt:number,
      /**  Applied Amount. Report Currency 2.  */  
   Rpt2AppliedAmt:number,
      /**  Tax Amount. Report Currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Unapplied Amount. Report Currency 2.  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 2.  */  
   Rpt2WithholdAmt:number,
      /**  Applied Amount. Report Currency 3.  */  
   Rpt3AppliedAmt:number,
      /**  Tax Amount. Report Currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Unapplied Amount. Report Currency 3.  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 3.  */  
   Rpt3WithholdAmt:number,
      /**  Signed flag  */  
   Signed:boolean,
      /**  Tax Amount. Base Currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Total AR Amount  */  
   TotalARAmt:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Unapplied Amount. Base Currency.  */  
   UnappliedAmt:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  Withholding Amount. Base Currency.  */  
   WithholdAmt:number,
      /**  Company Name  */  
   CompanyName:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CustomerName:string,
      /**  First customer address line.  */  
   CustomerAddr1:string,
      /**  Second customer address line.  */  
   CustomerAddr2:string,
      /**  Third customer address line.  */  
   CustomerAddr3:string,
      /**  Customer Stateportion of the address.  */  
   CustomerState:string,
      /**  Customer City portion of the address.  */  
   CustomerPostalCode:string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   CustomerCity:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  AR Payment Instrument ID  */  
   ARPromNoteID:string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Transaction Type  */  
   TranType:string,
      /**  Sent Flag  */  
   Sent:boolean,
      /**  Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  IBANCode for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   AutoGenerated:boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   DirectDeposit:boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Customer's country code  */  
   CustCountryCode:number,
      /**  Customer country portion of the address.  */  
   CustomerCountry:string,
      /**  Promissory Note Status  */  
   PIStatus:string,
      /**  Current Group  */  
   CurGroupID:string,
      /**  Stage  */  
   PIStage:string,
      /**  Reason to change Company or Customer information  */  
   ChgComment:string,
      /**  Hold from Application reason  */  
   HoldReason:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Reference to reversed PI  */  
   ReferseRef:number,
      /**  Reverse Date  */  
   ReverseDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  DiscountCashDate  */  
   DiscountCashDate:string,
   BaseCurrSymbol:string,
   BaseCurrencyCode:string,
   BaseCurrencyDesc:string,
   TermsDesc:string,
   CurrencyDesc:string,
   TotalCashReceived:number,
   CompanyBankName:string,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CustomerBankName:string,
   CustomerBankAcct:string,
   CustomerBankIdentifier:string,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   calcRate:boolean,
   ApplyDate:string,
   BankCurrencyCode:string,
   BankCurrSymbol:string,
   BillToName:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
   CurrencySwitch:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocDiscount:number,
   DocReceipt:number,
   FullyPaid:boolean,
   LegalNumMessage:string,
   TotalRoundDiff:number,
   TranTaxAmt:number,
   XRateLabel:string,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
   Rpt1TranTaxAmt:number,
   Rpt2TranTaxAmt:number,
   Rpt3TranTaxAmt:number,
   CompBankBranchCodeDesc:string,
   CustBankBranchCodeDesc:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
   PIStatusDesc:string,
      /**  like PIType.Initiation  */  
   PITypeInitiation:string,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
   GainLossReal:number,
   GainLossUnreal:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
   RevalueDate:string,
   DocDiscountAmt:number,
   Rpt1DiscountAmt:number,
   Rpt2DiscountAmt:number,
   Rpt3DiscountAmt:number,
   Receipt:number,
   Rpt1Receipt:number,
   Rpt2Receipt:number,
   Rpt3Receipt:number,
      /**  The Bank's full name.  */  
   BankAcctBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctDescription:string,
      /**  Description  */  
   CashbookLineDescription:string,
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
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Status Description  */  
   PIStatusStatusDesc:string,
      /**  Type Description  */  
   PITypeDescription:string,
      /**  Description  */  
   RateGrpDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  Description  */  
   TranDocTypeDescription:string,
   BankRecGainLoss:number,
   DocBankRecGainLoss:number,
   Rpt1BankRecGainLoss:number,
   Rpt2BankRecGainLoss:number,
   Rpt3BankRecGainLoss:number,
   BankTotalAmount:number,
   StatusChgTranDocType:string,
   StatusChgLegalNum:string,
      /**  for kinetic purposes  */  
   ARPNDtlExists:boolean,
      /**  for kinetic purposes  */  
   ARPNDtlInvoicePosted:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNHeadListTableset{
   ARPNHeadList:Erp_Tablesets_ARPNHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPNHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Applied Amount  */  
   AppliedAmt:number,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Company Bank Account ID  */  
   CompBankAcctID:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Customer Bank Account ID  */  
   CustBankAcctID:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Description  */  
   Description:string,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Applied Amount. Document Currency.  */  
   DocAppliedAmt:number,
      /**  Unapplied Amount. Document Currency.  */  
   DocUnAppliedAmt:number,
      /**  Tax Amount. Document Currency.  */  
   DocTaxAmt:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Withholding Amount. Document Currency.  */  
   DocWithholdAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Paid flag  */  
   Paid:boolean,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Process Card  */  
   ProcessCard:string,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Recalculated before posting.  */  
   RecalcBeforePost:boolean,
      /**  Applied Amount. Report Currency 1.  */  
   Rpt1AppliedAmt:number,
      /**  Tax Amount. Report Currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Unapplied Amount. Report Currency 1.  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 1.  */  
   Rpt1WithholdAmt:number,
      /**  Applied Amount. Report Currency 2.  */  
   Rpt2AppliedAmt:number,
      /**  Tax Amount. Report Currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Unapplied Amount. Report Currency 2.  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 2.  */  
   Rpt2WithholdAmt:number,
      /**  Applied Amount. Report Currency 3.  */  
   Rpt3AppliedAmt:number,
      /**  Tax Amount. Report Currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Unapplied Amount. Report Currency 3.  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 3.  */  
   Rpt3WithholdAmt:number,
      /**  Signed flag  */  
   Signed:boolean,
      /**  Tax Amount. Base Currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Total AR Amount  */  
   TotalARAmt:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Unapplied Amount. Base Currency.  */  
   UnappliedAmt:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  Withholding Amount. Base Currency.  */  
   WithholdAmt:number,
      /**  Company Name  */  
   CompanyName:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CustomerName:string,
      /**  First customer address line.  */  
   CustomerAddr1:string,
      /**  Second customer address line.  */  
   CustomerAddr2:string,
      /**  Third customer address line.  */  
   CustomerAddr3:string,
      /**  Customer Stateportion of the address.  */  
   CustomerState:string,
      /**  Customer City portion of the address.  */  
   CustomerPostalCode:string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   CustomerCity:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  AR Payment Instrument ID  */  
   ARPromNoteID:string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Transaction Type  */  
   TranType:string,
      /**  Sent Flag  */  
   Sent:boolean,
      /**  Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  IBANCode for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   AutoGenerated:boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   DirectDeposit:boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Customer's country code  */  
   CustCountryCode:number,
      /**  Customer country portion of the address.  */  
   CustomerCountry:string,
      /**  Promissory Note Status  */  
   PIStatus:string,
      /**  Current Group  */  
   CurGroupID:string,
      /**  Stage  */  
   PIStage:string,
      /**  Reason to change Company or Customer information  */  
   ChgComment:string,
      /**  Hold from Application reason  */  
   HoldReason:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Reference to reversed PI  */  
   ReferseRef:number,
      /**  Reverse Date  */  
   ReverseDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  TotalBankFee  */  
   TotalBankFee:number,
      /**  DocTotalBankFee  */  
   DocTotalBankFee:number,
      /**  Rpt1TotalBankFee  */  
   Rpt1TotalBankFee:number,
      /**  Rpt2TotalBankFee  */  
   Rpt2TotalBankFee:number,
      /**  Rpt3TotalBankFee  */  
   Rpt3TotalBankFee:number,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  Issuer Name  */  
   IssuerName:string,
      /**  Signed By  */  
   SignedBy:string,
      /**  Signed Date  */  
   SignedDate:string,
      /**  Signee Address 1  */  
   SigneeAddr1:string,
      /**  Signee Address 2  */  
   SigneeAddr2:string,
      /**  Signee Address 3  */  
   SigneeAddr3:string,
      /**  Signee City  */  
   SigneeCity:string,
      /**  Signee State  */  
   SigneeState:string,
      /**  Signee Postal Code  */  
   SigneeZip:string,
      /**  Signee Country Number  */  
   SigneeCountryNum:number,
      /**  Signee Phone  */  
   SigneePhoneNum:string,
      /**  Signee Email Address  */  
   SigneeEMailAddress:string,
      /**  Signee Comment  */  
   SigneeComment:string,
      /**  DiscountChargeAmt  */  
   DiscountChargeAmt:number,
      /**  DocDiscountChargeAmt  */  
   DocDiscountChargeAmt:number,
      /**  Rpt1DiscountChargeAmt  */  
   Rpt1DiscountChargeAmt:number,
      /**  Rpt2DiscountChargeAmt  */  
   Rpt2DiscountChargeAmt:number,
      /**  Rpt3DiscountChargeAmt  */  
   Rpt3DiscountChargeAmt:number,
      /**  Signee Bank Name  */  
   SigneeBankName:string,
      /**  Signee Bank Account Number  */  
   SigneeBankAcct:string,
      /**  Signee Bank Identifier  */  
   SigneeBankIdentifier:string,
      /**  Signee IBAN Code  */  
   SigneeIBANCode:string,
      /**  Signee Bank BranchCode  */  
   SigneeBankBranchCode:string,
      /**  DiscountCashDate  */  
   DiscountCashDate:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
   ApplyDate:string,
   BankCurrencyCode:string,
   BankCurrSymbol:string,
   BankRecGainLoss:number,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   calcRate:boolean,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
   CompBankBranchCodeDesc:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
   CurrencyDesc:string,
   CurrencySwitch:boolean,
   CustBankBranchCodeDesc:string,
   CustomerBankAcct:string,
   CustomerBankIdentifier:string,
   CustomerBankName:string,
   DisableBankAcctIDPI:boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocBankRecGainLoss:number,
   DocDiscount:number,
   DocDiscountAmt:number,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
   FullyPaid:boolean,
   GainLossReal:number,
   GainLossUnreal:number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PIStatusDesc:string,
      /**  like PIType.Initiation  */  
   PITypeInitiation:string,
   Receipt:number,
   RevalueDate:string,
   Rpt1BankRecGainLoss:number,
   Rpt1DiscountAmt:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt1Receipt:number,
   Rpt1TranTaxAmt:number,
   Rpt2BankRecGainLoss:number,
   Rpt2DiscountAmt:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt2Receipt:number,
   Rpt2TranTaxAmt:number,
   Rpt3BankRecGainLoss:number,
   Rpt3DiscountAmt:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
   Rpt3Receipt:number,
   Rpt3TranTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   StatusChgLegalNum:string,
   StatusChgTranDocType:string,
   TermsDesc:string,
   TotalCashReceived:number,
   TotalRoundDiff:number,
   TranTaxAmt:number,
   TypeDesc:string,
   XRateLabel:string,
   BankTotalAmount:number,
   BaseCurrencyCode:string,
   BaseCurrencyDesc:string,
   BaseCurrSymbol:string,
   BillToName:string,
   DocDiscountedAmt:number,
      /**  for kinetic purposes  */  
   ARPNDtlExists:boolean,
      /**  for kinetic purposes  */  
   ARPNDtlInvoicePosted:boolean,
   BitFlag:number,
   BankAcctDescription:string,
   BankAcctBankName:string,
   CashbookLineDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CustNumInactive:boolean,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   PIStatusStatusDesc:string,
   PITypeDescription:string,
   RateGrpDescription:string,
   TaxRegionCodeDescription:string,
   TranDocTypeDescription:string,
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

export interface Erp_Tablesets_LegalNumGenOptsTableset{
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtARPIStatusChgTableset{
   ARPNHead:Erp_Tablesets_ARPNHeadRow[],
   ARPNDtl:Erp_Tablesets_ARPNDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param ipGroup
      @param ipHeadNum
   */  
export interface GetByGroupHeadNum_input{
      /**  Group ID  */  
   ipGroup:string,
      /**  HeadNum  */  
   ipHeadNum:number,
}

export interface GetByGroupHeadNum_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param piGroup
   */  
export interface GetByGroup_input{
      /**  Group ID  */  
   piGroup:string,
}

export interface GetByGroup_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetByID_input{
   groupID:string,
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
}

   /** Required : 
      @param piGroup
      @param piAutoBankRec
      @param piHeadNum
      @param pageSize
      @param absolutePage
   */  
export interface GetGroupPIs_input{
      /**  Group ID  */  
   piGroup:string,
      /**  The flag shows the PIs should be retrieved in AutoBankRec mode  */  
   piAutoBankRec:boolean,
      /**  HeadNum  */  
   piHeadNum:number,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface GetGroupPIs_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipStatusChgTranDocType
      @param ipTranDate
   */  
export interface GetLegalNumGenOptsFromABR_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Payment Instrument Head Number  */  
   ipHeadNum:number,
      /**  Document Type for the status change  */  
   ipStatusChgTranDocType:string,
      /**  Transaction Date  */  
   ipTranDate:string,
}

export interface GetLegalNumGenOptsFromABR_output{
   returnObj:Erp_Tablesets_LegalNumGenOptsTableset[],
parameters : {
      /**  output parameters  */  
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipStatusChgTranDocType
   */  
export interface GetLegalNumGenOpts_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Payment Instrument Head Number  */  
   ipHeadNum:number,
      /**  Document Type for the status change  */  
   ipStatusChgTranDocType:string,
}

export interface GetLegalNumGenOpts_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
parameters : {
      /**  output parameters  */  
   opPromptForNum:boolean,
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
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param headNum
      @param invoiceNum
   */  
export interface GetNewARPNDtl_input{
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
   headNum:number,
   invoiceNum:number,
}

export interface GetNewARPNDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewARPNHead_input{
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
   groupID:string,
}

export interface GetNewARPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
}
}

   /** Required : 
      @param whereClauseARPNHead
      @param whereClauseARPNDtl
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseARPNHead:string,
   whereClauseARPNDtl:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
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
      @param discountedAmount
      @param ds
   */  
export interface OnDiscountedAmountChange_input{
      /**  Discounted Amount  */  
   discountedAmount:number,
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
}

export interface OnDiscountedAmountChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
}
}

   /** Required : 
      @param discountingCashDate
      @param ds
   */  
export interface OnDiscountingCashDateChange_input{
      /**  Discounting Cash Date  */  
   discountingCashDate:string,
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
}

export interface OnDiscountingCashDateChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
}
}

   /** Required : 
      @param discountingCharge
      @param ds
   */  
export interface OnDiscountingChargeChange_input{
      /**  Discounting Charge  */  
   discountingCharge:number,
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
}

export interface OnDiscountingChargeChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
}
}

   /** Required : 
      @param piGroup
   */  
export interface PrePost_input{
      /**  Group ID  */  
   piGroup:string,
}

export interface PrePost_output{
parameters : {
      /**  output parameters  */  
   poRunGL:string,
   legalNumberMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ipFiscalInfo
      @param inARPNHeadKey
   */  
export interface ProcessCancelOnAccount_input{
      /**  Fiscal Info  */  
   ipFiscalInfo:string,
      /**  AR PI  */  
   inARPNHeadKey:string,
}

export interface ProcessCancelOnAccount_output{
}

   /** Required : 
      @param ds
      @param bClearDiscountingCharge
   */  
export interface RemoveFromGroup_input{
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
      /**  If true then system should try to clear discounting charge data  */  
   bClearDiscountingCharge:boolean,
}

export interface RemoveFromGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
}
}

   /** Required : 
      @param piGroup
      @param piGrpStatus
      @param piPIList
      @param ds
   */  
export interface SelectPIData_input{
      /**  Group ID  */  
   piGroup:string,
      /**  Group Status  */  
   piGrpStatus:string,
      /**  PI List  */  
   piPIList:string,
   ds:Erp_Tablesets_ARPNHeadListTableset[],
}

export interface SelectPIData_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
}

   /** Required : 
      @param targetBankAcctID
      @param piGroup
      @param piGrpStatus
      @param piFromDate
      @param piToDate
      @param piType
      @param piCustFilter
      @param piCurrencyFilter
      @param piStatusFilter
      @param ipCashBookNum
   */  
export interface SelectPI_input{
      /**  Target BankID  */  
   targetBankAcctID:string,
      /**  Group ID  */  
   piGroup:string,
      /**  Group Status  */  
   piGrpStatus:string,
      /**  From DueDate  */  
   piFromDate:string,
      /**  To DueDate  */  
   piToDate:string,
      /**  PI Type  */  
   piType:string,
      /**  Customer Filter  */  
   piCustFilter:string,
      /**  Currency Filter  */  
   piCurrencyFilter:string,
      /**  StatusFilter  */  
   piStatusFilter:string,
      /**  CashBook  */  
   ipCashBookNum:number,
}

export interface SelectPI_output{
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
}

   /** Required : 
      @param inARPNHeadKey
   */  
export interface UndoCancelOnAccount_input{
      /**  AR PI  */  
   inARPNHeadKey:string,
}

export interface UndoCancelOnAccount_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtARPIStatusChgTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARPIStatusChgTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARPIStatusChgTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIStatusChgTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  Group identifier.  */  
   ipGroupID:string,
      /**  Payment Instrument Head Number.  */  
   ipHeadNum:number,
      /**  Indicates reason why legal number should be voided.  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_ARPIStatusChgTableset[],
}

