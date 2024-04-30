import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLCostTransSvc
// Description: Cost transaction details for Chart Tracker.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/$metadata", {
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
   Description: Get GLCostTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCostTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranRow
   */  
export function get_GLCostTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCostTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLCostTrans(requestBody:Erp_Tablesets_PartTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GLCostTran item
   Description: Calls GetByID to retrieve the GLCostTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCostTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartTranRow
   */  
export function get_GLCostTrans_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
         resolve(data as Erp_Tablesets_PartTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLCostTran for the service
   Description: Calls UpdateExt to update GLCostTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCostTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLCostTrans_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, requestBody:Erp_Tablesets_PartTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete GLCostTran item
   Description: Call UpdateExt to delete GLCostTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCostTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLCostTrans_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
   Description: Get InvcDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   */  
export function get_InvcDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.InvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvcDtls(requestBody:Erp_Tablesets_InvcDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the InvcDtl item
   Description: Calls GetByID to retrieve the InvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.InvcDtlRow
   */  
export function get_InvcDtls_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
         resolve(data as Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InvcDtl for the service
   Description: Calls UpdateExt to update InvcDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InvcDtls_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, requestBody:Erp_Tablesets_InvcDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
   Summary: Call UpdateExt to delete InvcDtl item
   Description: Call UpdateExt to delete InvcDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InvcDtls_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
   Description: Get LaborDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   */  
export function get_LaborDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtls(requestBody:Erp_Tablesets_LaborDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LaborDtl item
   Description: Calls GetByID to retrieve the LaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborDtlRow
   */  
export function get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborDtl for the service
   Description: Calls UpdateExt to update LaborDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, requestBody:Erp_Tablesets_LaborDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete LaborDtl item
   Description: Call UpdateExt to delete LaborDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow)
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
export function get_GetRows(whereClausePartTran:string, whereClauseInvcDtl:string, whereClauseLaborDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartTran=" + whereClausePartTran
   }
   if(typeof whereClauseInvcDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcDtl=" + whereClauseInvcDtl
   }
   if(typeof whereClauseLaborDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtl=" + whereClauseLaborDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sysDate:string, sysTime:string, tranNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sysDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysDate=" + sysDate
   }
   if(typeof sysTime!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysTime=" + sysTime
   }
   if(typeof tranNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranNum=" + tranNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsCustom
   Description: Custom GetRows method.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetRowsCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewPartTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartTran(requestBody:GetNewPartTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetNewPartTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPartTran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcDtl(requestBody:GetNewInvcDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewInvcDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetNewInvcDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewInvcDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtl(requestBody:GetNewLaborDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetNewLaborDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLaborDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartTranListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartTranRow,
}

export interface Erp_Tablesets_InvcDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   "XRevisionNum":string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   "PartNum":string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   "LineDesc":string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   "IUM":string,
      /**  Our Current Revision Number for this Part.  */  
   "RevisionNum":string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   "POLine":string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   "TaxExempt":string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   "TaxCatID":string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   "Commissionable":boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   "DiscountPercent":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "UnitPrice":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocUnitPrice":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   "OurOrderQty":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocExtPrice":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "Discount":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "DocTotalMiscChrg":number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   "ProdCode":string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "OurShipQty":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  The packing slip line number that is being invoiced.  */  
   "PackLine":number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   "OrderNum":number,
      /**  The associated sales order line number.  */  
   "OrderLine":number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   "OrderRelNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   "ShipToNum":string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   "ShipDate":string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   "ShipViaCode":string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "AdvanceBillCredit":number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "DocAdvanceBillCredit":number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   "CustNum":number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   "InvoiceComment":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   "ShpConNum":number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlBurUnitCost":number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   "COSPostingReqd":boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPosted":boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   "CallNum":number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   "CallCode":string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   "RMANum":number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   "RMALine":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   "JournalCode":string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   "SellingOrderQty":number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "SellingShipQty":number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   "ProjectID":string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   "MilestoneID":string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   "ListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   "OrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   "DocOrdBasedPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "AdvGainLoss":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Sales representative commission rate.  */  
   "RepRate1":number,
      /**  Sales representative commission rate.  */  
   "RepRate2":number,
      /**  Sales representative commission rate.  */  
   "RepRate3":number,
      /**  Sales representative commission rate.  */  
   "RepRate4":number,
      /**  Sales representative commission rate.  */  
   "RepRate5":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit1":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit2":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit3":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit4":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit5":number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   "BTCustNum":number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlUnitCost":number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCLbrUnitCost":number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCBurUnitCost":number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCSubUnitCost":number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlBurUnitCost":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   "RevChargeMethod":string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   "OverrideReverseCharge":boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   "RevChargeApplied":boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3AdvGainLoss":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping adress country Number.  */  
   "OTSCountryNum":number,
      /**  Value is copied from PartTran for PE  */  
   "Plant":string,
      /**  value is copied from PartTran for PE  */  
   "WarehouseCode":string,
      /**  value is copied from PartTran for PE  */  
   "CallLine":number,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  FK to the Finance Charges table  */  
   "FinChargeCode":string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   "ABTUID":string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "InUnitPrice":number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocInUnitPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "InExtPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocInExtPrice":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "InDiscount":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocInDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "InTotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "DocInTotalMiscChrg":number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   "InListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   "DocInListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   "InOrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   "DocInOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitPrice":number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   "AssetNum":string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   "DisposalNum":number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   "PBLineType":string,
      /**  Invoice line reference  */  
   "InvoiceLineRef":number,
      /**  Invoice Number Reference  */  
   "InvoiceRef":number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   "LotNum":string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   "PBInvoiceLine":number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   "RAID":number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   "RADtlID":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   "ChargeDefRev":boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DefRevPosted  */  
   "DefRevPosted":boolean,
      /**  Unit price of Invoice linked to Bill of Exchange in original currency.  */  
   "LinkedInvcUnitPrice":number,
      /**  Withholding Tax Amount in reporting currency  */  
   "DspWithholdAmt":number,
      /**  Withholding Tax Amount in document currency  */  
   "DocDspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt1DspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt2DspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt3DspWithholdAmt":number,
      /**  Currency code from linked Invoice Header  */  
   "LinkedCurrencyCode":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  PEBOEHeadNum  */  
   "PEBOEHeadNum":number,
      /**  MXSellingShipQty  */  
   "MXSellingShipQty":number,
      /**  MXUnitPrice  */  
   "MXUnitPrice":number,
      /**  DocMXUnitPrice  */  
   "DocMXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MXUnitPrice":number,
      /**  CustCostCenter  */  
   "CustCostCenter":string,
      /**  DEIsServices  */  
   "DEIsServices":boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   "DEIsSecurityFinancialDerivative":boolean,
      /**  DEInternationalSecuritiesID  */  
   "DEInternationalSecuritiesID":string,
      /**  DEIsInvestment  */  
   "DEIsInvestment":boolean,
      /**  DEPayStatCode  */  
   "DEPayStatCode":string,
      /**  DefRevEndDate  */  
   "DefRevEndDate":string,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  Indicates tha this invoice Line was reclassified.  */  
   "Reclassified":boolean,
      /**  Enables the user the ability to override the Percent or Amount of revenue to be deferred  */  
   "PartiallyDefer":boolean,
      /**  Percentage of revenue to be deferred for this line item  */  
   "DeferredPercent":number,
      /**  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  */  
   "Reclass":boolean,
      /**  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  */  
   "DeferredOnly":boolean,
      /**  Reclassification Code. This field will be required if Reclass is checked.  */  
   "ReclassCodeID":string,
      /**  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  */  
   "ReclassReasonCode":string,
      /**  Internal comments for reclassification entered by the user.  */  
   "ReclassComments":string,
      /**  Deferred Revenue Amount in base currency  */  
   "DeferredRevAmt":number,
      /**  Deferred Revenue Amount in document currency  */  
   "DocDeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt1DeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt2DeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt3DeferredRevAmt":number,
      /**  ChargeReclass  */  
   "ChargeReclass":boolean,
      /**  DEDenomination  */  
   "DEDenomination":string,
      /**  DropShipPONum  */  
   "DropShipPONum":number,
      /**  DocInAdvanceBillCredit  */  
   "DocInAdvanceBillCredit":number,
      /**  InAdvanceBillCredit  */  
   "InAdvanceBillCredit":number,
      /**  Rpt1InAdvanceBillCredit  */  
   "Rpt1InAdvanceBillCredit":number,
      /**  Rpt2InAdvanceBillCredit  */  
   "Rpt2InAdvanceBillCredit":number,
      /**  Rpt3InAdvanceBillCredit  */  
   "Rpt3InAdvanceBillCredit":number,
      /**  MYIndustryCode  */  
   "MYIndustryCode":string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  ConsolidateLines  */  
   "ConsolidateLines":boolean,
      /**  MXCustomsDuty  */  
   "MXCustomsDuty":string,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  MXProdServCode  */  
   "MXProdServCode":string,
      /**  Quote number to which this line item detail record is associated with.  */  
   "QuoteNum":number,
      /**  Quote Line number from which this invoice line was created from.  */  
   "QuoteLine":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  MXCustomsUMFrom  */  
   "MXCustomsUMFrom":string,
      /**  PE Detraction good or service code  */  
   "PEDetrGoodServiceCode":string,
      /**  PETaxExempt  */  
   "PETaxExempt":string,
      /**  Order number on the Invoicing Company.  */  
   "CColOrderNum":number,
      /**  Order number line the Invoicing Company.  */  
   "CColOrderLine":number,
      /**  Order number release the Invoicing Company.  */  
   "CColOrderRel":number,
      /**  Invoice Line reference on the Invoicing Company.  */  
   "CColInvoiceLineRef":number,
      /**  Packing slip number on the Invoicing Company.  */  
   "CColPackNum":number,
      /**  Packing slip line number on the Invoicing Company.  */  
   "CColPackLine":number,
      /**  Drop shipment packing slip number on the Invoicing Company.  */  
   "CColDropShipPackSlip":string,
      /**  Drop shipment packing slip line number on the Invoicing Company.  */  
   "CColDropShipPackSlipLine":number,
      /**  Ship To Customer ID from the Invoice Line in the subsidiary company.  */  
   "CColShipToCustID":string,
      /**  Ship To from the Invoice Line in the subsidiary company.  */  
   "CColShipToNum":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Exempt Reason Code  */  
   "ExemptReasonCode":string,
      /**  Associates the Call Line record back its linked jobnum  */  
   "JobNum":string,
      /**  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  */  
   "ServiceSource":string,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  */  
   "AssemblySeq":number,
      /**  Job Mtl seq used to create invoice line from service call job  */  
   "MtlSeq":number,
      /**  Job subcontract oper seq used to create invoice line from service call job  */  
   "OprSeq":number,
      /**  Indicates the labor type of the LaborDtl used to create invoice from service call job.  */  
   "LaborType":string,
      /**  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  */  
   "BillableLaborHrs":number,
      /**  Billable rate used to create invoice line from labor related to service call job. In base currency.  */  
   "BillableLaborRate":number,
      /**  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  */  
   "ServiceSourceType":string,
      /**  TotalCovenantDiscount  */  
   "TotalCovenantDiscount":number,
      /**  DocCovenantDiscount  */  
   "DocCovenantDiscount":number,
      /**  Rpt1CovenantDiscount  */  
   "Rpt1CovenantDiscount":number,
      /**  Rpt2CovenantDiscount  */  
   "Rpt2CovenantDiscount":number,
      /**  Rpt3CovenantDiscount  */  
   "Rpt3CovenantDiscount":number,
      /**  TotalInCovenantDiscount  */  
   "TotalInCovenantDiscount":number,
      /**  DocInCovenantDiscount  */  
   "DocInCovenantDiscount":number,
      /**  Rpt1InCovenantDiscount  */  
   "Rpt1InCovenantDiscount":number,
      /**  Rpt2InCovenantDiscount  */  
   "Rpt2InCovenantDiscount":number,
      /**  Rpt3InCovenantDiscount  */  
   "Rpt3InCovenantDiscount":number,
      /**  Adv bill enabled flag  */  
   "AdvBillEnabled":boolean,
   "AllowTaxCodeUpd":boolean,
      /**  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  */  
   "AllowUpdPartDefer":boolean,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   "BillToCustID":string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   "BTCustName":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   "CheckAmortAmounts":boolean,
   "CNGTIDescription1":string,
   "CNGTIDescription2":string,
   "CNGTIDescription3":string,
      /**  CSF China, discount tax amount  */  
   "CNGTIDiscountTaxAmount":number,
   "CNGTIIUM":string,
   "CNGTINetAmount":number,
   "CNGTIPartDescription":string,
   "CNGTISpecification":string,
   "CNGTITaxAmount":number,
   "CNGTITaxCode":string,
   "CNGTITaxPercent":number,
   "CNGTITotalAmount":number,
      /**  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  */  
   "CNGTIUnitPrice":number,
   "ContractSuspended":boolean,
      /**  Currency code from InvcHead.  */  
   "CurrencyCode":string,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "CustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "CustName":string,
      /**  Invoice Detail Customer Name  */  
   "CustomerName":string,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   "DeleteRASchedule":boolean,
   "DispGLAcct":string,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  PO number for display.  */  
   "DispPONum":string,
      /**  Ship to display address  */  
   "DispShipToAddr":string,
      /**  Document display symbol.  */  
   "DocDisplaySymbol":string,
   "DocDspUnitPrice":number,
      /**  Document discount amount  */  
   "DocLessDiscount":number,
      /**  Doc line tax  */  
   "DocLineTax":number,
      /**  ExtPrice-disc+misc charges.  */  
   "DocLineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "DocPEDetAmt":number,
      /**  Drop Shipment  */  
   "DropShipment":boolean,
      /**  Display advance bill credit  */  
   "DspAdvanceBillCredit":number,
      /**  Display discount  */  
   "DspDiscount":number,
      /**  Display documents advance bill credit  */  
   "DspDocAdvanceBillCredit":number,
      /**  Display document discount  */  
   "DspDocDiscount":number,
      /**  Display document ext price  */  
   "DspDocExtPrice":number,
      /**  Display document less discount  */  
   "DspDocLessDiscount":number,
      /**  Display document line tax  */  
   "DspDocLineTax":number,
      /**  Display document line total  */  
   "DspDocLineTotal":number,
      /**  Display document total misc. charge  */  
   "DspDocTotalMiscChrg":number,
      /**  Display ext price  */  
   "DspExtPrice":number,
      /**  Display Invoice Reference  */  
   "DspInvoiceRef":number,
      /**  Display less discount  */  
   "DspLessDiscount":number,
      /**  Display line tax  */  
   "DspLineTax":number,
      /**  Display line total  */  
   "DspLineTotal":number,
      /**  Display our ship qty  */  
   "DspOurShipQty":number,
      /**  Display selling ship qty  */  
   "DspSellingShipQty":number,
   "DspTaxExempt":string,
      /**  Display total misc. charges  */  
   "DspTotalMiscChrg":number,
   "DspUnitPrice":number,
      /**  Invoice head due date.  */  
   "DueDate":string,
      /**  FSA Technician  */  
   "EmpID":string,
   "EnableDspWithholdAmt":boolean,
   "EnableRMADelete":boolean,
   "EnableRMAUpdate":boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "FSACallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "FSAContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "FSAContractNum":number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   "FSAEmpID":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   "FSAWarrantyCode":string,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Group associated to the invoice  */  
   "GroupID":string,
   "InPrice":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Invoice Header Legal Number  */  
   "InvLegalNum":string,
      /**  Invoice Date from InvcHead.  */  
   "InvoiceDate":string,
      /**  Invoice header type  */  
   "InvoiceType":string,
      /**  Is commission button sensitive  */  
   "IsCommisBtnSensitive":boolean,
      /**  Set to true if intrastat is enabled.  */  
   "IsIntrastatSensitive":boolean,
      /**  Tax buton sensitive or not.  */  
   "IsTaxBtnSensitive":boolean,
      /**  display discount  */  
   "LessDiscount":number,
      /**  Line tax amount  */  
   "LineTax":number,
      /**  ExtPrice-disc+misc charges.  */  
   "LineTotal":number,
   "LinkedCurrencySymbol":string,
      /**  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  */  
   "NoShipTaxRgnInfo":boolean,
      /**  Open invoice flag from InvcHead.  */  
   "OpenInvoice":boolean,
      /**  OrderUM display  */  
   "OrderUM":string,
      /**  original tax category  */  
   "OrigTaxCat":string,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "PEDetAmt":number,
      /**  PE Detraction good or service code description  */  
   "PEDetrGoodServiceCodeDesc":string,
   "PEDspCurrencySymbol":string,
      /**  PE VAT Exemption Reason  */  
   "PEVATExemptionReason":string,
      /**  Posted flag from the InvcHead.  */  
   "Posted":boolean,
   "RADesc":string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   "RASchedExists":boolean,
      /**  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  */  
   "RemoveManAdTax":boolean,
   "Rpt1DspAdvanceBillCredit":number,
   "Rpt1DspDiscount":number,
   "Rpt1DspExtPrice":number,
   "Rpt1DspLessDiscount":number,
   "Rpt1DspLineTax":number,
   "Rpt1DspLineTotal":number,
   "Rpt1DspTotalMiscChrg":number,
   "Rpt1DspUnitPrice":number,
   "Rpt1LineTax":number,
   "Rpt1LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt1PEDetAmt":number,
   "Rpt2DspAdvanceBillCredit":number,
   "Rpt2DspDiscount":number,
   "Rpt2DspExtPrice":number,
   "Rpt2DspLessDiscount":number,
   "Rpt2DspLineTax":number,
   "Rpt2DspLineTotal":number,
   "Rpt2DspTotalMiscChrg":number,
   "Rpt2DspUnitPrice":number,
   "Rpt2LineTax":number,
   "Rpt2LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt2PEDetAmt":number,
   "Rpt3DspAdvanceBillCredit":number,
   "Rpt3DspDiscount":number,
   "Rpt3DspExtPrice":number,
   "Rpt3DspLessDiscount":number,
   "Rpt3DspLineTax":number,
   "Rpt3DspLineTotal":number,
   "Rpt3DspTotalMiscChrg":number,
   "Rpt3DspUnitPrice":number,
   "Rpt3LineTax":number,
   "Rpt3LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt3PEDetAmt":number,
      /**  1st sales rep of the invoice.  */  
   "SalesRepCode1":string,
      /**  2nd sales rep of the invoice header.  */  
   "SalesRepCode2":string,
      /**  3rd sales rep code of the invoice header.  */  
   "SalesRepCode3":string,
      /**  4th sales rep code of the invoice header.  */  
   "SalesRepCode4":string,
      /**  5th salesrep code of the invoice header.  */  
   "SalesRepCode5":string,
      /**  1st sales rep name  */  
   "SalesRepName1":string,
      /**  2nd sales rep name  */  
   "SalesRepName2":string,
      /**  3rd sales rep name  */  
   "SalesRepName3":string,
      /**  4th sales rep name  */  
   "SalesRepName4":string,
      /**  5th sales rep name  */  
   "SalesRepName5":string,
   "ShipToContactEMailAddress":string,
   "ShipToContactFaxNum":string,
   "ShipToContactName":string,
   "ShipToContactPhoneNum":string,
      /**  Ship Head Legal Number  */  
   "ShpLegalNum":string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "SoldToCustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "SoldToCustName":string,
      /**  Terms code from InvcHead.  */  
   "TermsCode":string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
      /**  This flag allow updating Reclassification data.  */  
   "AllowReclassify":boolean,
      /**  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  */  
   "LineAmtRecalcd":boolean,
      /**  Set to true if extra trade statistics is enabled.  */  
   "IsExtrastatSensitive":boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   "TrackInventoryByRevision":boolean,
   "BitFlag":number,
   "CallCodeCallDescription":string,
   "CommodityCodeDescription":string,
   "ContractCodeContractDescription":string,
   "ContractNumSuspended":boolean,
   "CustCntName":string,
   "CustCntMiddleName":string,
   "CustCntFirstName":string,
   "CustCntFaxNum":string,
   "CustCntCorpName":string,
   "CustCntPhoneNum":string,
   "CustCntLastName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumAllowShipTo3":boolean,
   "CustNumBTName":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "JournalCodeJrnlDescription":string,
   "MilestoneIDDescription":string,
   "MXProdServCodeDesc":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "OTSCntryEUMember":boolean,
   "OTSCntryISOCode":string,
   "OTSCntryDescription":string,
   "PackLineLineDesc":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
   "ReclassCodeDescription":string,
   "ReclassReasonDescription":string,
   "RMALineLineDesc":string,
   "SalesCatIDDescription":string,
   "ShipToCustCustID":string,
   "ShipToCustName":string,
   "ShipToCustBTName":string,
   "ShipToNumInactive":boolean,
   "ShipToNumName":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TaxCatIDDescription":string,
   "TaxRegionDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   "EmployeeNum":string,
      /**  Used as the foreign key to the LaborHed record.  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborType":string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborTypePseudo":string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   "ReWork":boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   "ReworkReasonCode":string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   "AssemblySeq":number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   "OprSeq":number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   "JCDept":string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   "ResourceGrpID":string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   "OpCode":string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   "LaborHrs":number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   "BurdenHrs":number,
      /**  The Total production quantity reported.  */  
   "LaborQty":number,
      /**  The reported scrap quantity.  */  
   "ScrapQty":number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   "ScrapReasonCode":string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   "SetupPctComplete":number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   "Complete":boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   "IndirectCode":string,
      /**  A short note that the user can make about the labor transaction.  */  
   "LaborNote":string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   "ExpenseCode":string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   "LaborCollection":boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   "AppliedToSchedule":boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   "ClockInMInute":number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   "ClockOutMinute":number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   "ClockInDate":string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   "ClockinTime":number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   "ClockOutTime":number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   "ActiveTrans":boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   "OverRidePayRate":number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   "LaborRate":number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   "BurdenRate":number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockInTime":string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockOutTime":string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "ResourceID":string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   "OpComplete":boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   "EarnedHrs":number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   "AddedOper":boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   "PayrollDate":string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   "GLTrans":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   "InspectionPending":boolean,
      /**  The service call that this service record belongs to.  */  
   "CallNum":number,
      /**  The line number of the service call this labor detail is for.  */  
   "CallLine":number,
      /**  the service that is being performed on this line.  */  
   "ServNum":number,
      /**  A unique code that identifies the Service  */  
   "ServCode":string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   "WipPosted":boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   "DiscrepQty":number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   "DiscrpRsnCode":string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   "ParentLaborDtlSeq":number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   "LaborEntryMethod":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   "BFLaborReq":boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   "ABTUID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Project Role Code  */  
   "RoleCd":string,
      /**  Time Type Code  */  
   "TimeTypCd":string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   "PBInvNum":number,
      /**  The payment method of the time.  */  
   "PMUID":number,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**  The date the time received final approval.  */  
   "ApprovedDate":string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   "ClaimRef":string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   "QuickEntryCode":string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   "TimeStatus":string,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   "CreatedViaTEWeekView":boolean,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  The User ID of the submitter.  */  
   "SubmittedBy":string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   "PBRateFrom":string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   "PBCurrencyCode":string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   "PBHours":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   "PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   "PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   "DocPBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt1PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt2PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt3PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   "DocPBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt1PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt2PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt3PBChargeAmt":number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   "Shift":number,
      /**  Links to PActDtl.ActID  */  
   "ActID":number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   "DtailID":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used By Project Analysis Process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process.  */  
   "AsOfSeq":number,
      /**  JDFInputFiles  */  
   "JDFInputFiles":string,
      /**  JDFNumberOfPages  */  
   "JDFNumberOfPages":string,
      /**  BatchWasSaved  */  
   "BatchWasSaved":string,
      /**  AssignToBatch  */  
   "AssignToBatch":boolean,
      /**  BatchComplete  */  
   "BatchComplete":boolean,
      /**  BatchRequestMove  */  
   "BatchRequestMove":boolean,
      /**  BatchPrint  */  
   "BatchPrint":boolean,
      /**  BatchLaborHrs  */  
   "BatchLaborHrs":number,
      /**  BatchPctOfTotHrs  */  
   "BatchPctOfTotHrs":number,
      /**  BatchQty  */  
   "BatchQty":number,
      /**  BatchTotalExpectedHrs  */  
   "BatchTotalExpectedHrs":number,
      /**  JDFOpCompleted  */  
   "JDFOpCompleted":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Downtime  */  
   "Downtime":boolean,
      /**  RefJobNum  */  
   "RefJobNum":string,
      /**  RefAssemblySeq  */  
   "RefAssemblySeq":number,
      /**  RefOprSeq  */  
   "RefOprSeq":number,
      /**  Imported  */  
   "Imported":boolean,
      /**  ImportDate  */  
   "ImportDate":string,
      /**   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   "TimeAutoSubmit":boolean,
      /**  BatchMode  */  
   "BatchMode":boolean,
      /**  BillServiceRate  */  
   "BillServiceRate":number,
      /**  Pay Hours used for HCM  */  
   "HCMPayHours":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   "DiscrepAttributeSetID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  */  
   "LaborAttributeSetID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   "ScrapAttributeSetID":number,
      /**  PCID  */  
   "PCID":string,
      /**  NonConfPCID  */  
   "NonConfPCID":string,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   "AllowDirLbr":boolean,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseID":string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectID":string,
   "ApprovedBy":string,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   "ApprvrHasOpenTask":boolean,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   "BaseCurrCodeDesc":string,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   "BurdenCost":number,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "CallCode":string,
   "CapabilityDescription":string,
   "CapabilityID":string,
      /**  Charge rate calculated for Time and Expense approval  */  
   "ChargeRate":number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   "ChargeRateSRC":string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   "ChgRateCurrDesc":string,
   "CompleteFlag":boolean,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "ContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "ContractNum":number,
      /**  Unit of Measure used for DiscrepQty  */  
   "DiscrepUOM":string,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   "DisLaborType":boolean,
   "DisplayJob":string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   "DisPrjRoleCd":boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   "DisTimeTypCd":boolean,
   "DowntimeTotal":number,
   "DspChangeTime":string,
   "DspCreateTime":string,
   "DspTotHours":string,
   "DtClockIn":string,
   "DtClockOut":string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   "EfficiencyPercentage":number,
      /**  Labor Detail Employee Name  */  
   "EmployeeName":string,
   "EnableComplete":boolean,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
   "EnableDiscrepQty":boolean,
   "EnableInspection":boolean,
   "EnableLaborQty":boolean,
   "EnableNextOprSeq":boolean,
   "EnablePrintTagsList":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if recall is available for an approver  */  
   "EnableRecallAprv":boolean,
   "EnableRequestMove":boolean,
   "EnableResourceGrpID":boolean,
   "EnableScrapQty":boolean,
      /**  Enable the SN Button?  */  
   "EnableSN":boolean,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
   "EndActivity":boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   "EnteredOnCurPlant":boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "FSACallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "FSAContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "FSAContractNum":number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   "FSAEmpID":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   "FSAWarrantyCode":string,
   "FSComplete":boolean,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Indicates if the user has access to the row  */  
   "HasAccessToRow":boolean,
      /**  Indicates if the labor detail has comments  */  
   "HasComments":boolean,
      /**  To tell the bo that this transaction was being modified from HH.  */  
   "HH":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Indicates if the job operation is marked as fixed hours and quantity only.  */  
   "ISFixHourAndQtyOnly":boolean,
   "JCSystReworkReasons":boolean,
   "JCSystScrapReasons":boolean,
   "JobOperComplete":boolean,
   "JobType":string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   "JobTypeCode":string,
      /**  calculated field: LaborHrs * LaborRate  */  
   "LaborCost":number,
      /**  Unit of Measure used for LaborQty  */  
   "LaborUOM":string,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   "LbrDay":string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   "LbrMonth":string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   "LbrWeek":string,
   "MES":boolean,
   "MultipleEmployeesText":string,
   "NewDifDateFlag":number,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   "NewPrjRoleCd":string,
      /**  Holds the description for NewPrjRoleCd  */  
   "NewRoleCdDesc":string,
   "NextAssemblySeq":number,
   "NextOperDesc":string,
   "NextOprSeq":number,
   "NextResourceDesc":string,
      /**  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  */  
   "NonConfProcessed":boolean,
   "NotSubmitted":boolean,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   "OkToChangeResourceGrpID":boolean,
   "PartDescription":string,
   "PartNum":string,
   "PBAllowModify":boolean,
   "PendingApprovalBy":string,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   "PhaseJobNum":string,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   "PhaseOprSeq":number,
   "PrintNCTag":boolean,
   "PrjUsedTran":string,
   "ProdDesc":string,
   "ProjPhaseID":string,
   "RequestMove":boolean,
   "ResourceDesc":string,
   "RoleCdDisplayAll":boolean,
      /**  Unit of Measure used for ScrapQty.  */  
   "ScrapUOM":string,
      /**  Flag field to identify if the row is being sent from MES  */  
   "SentFromMES":boolean,
   "StartActivity":boolean,
   "TimeDisableDelete":boolean,
   "TimeDisableUpdate":boolean,
   "TreeNodeImageName":string,
   "UnapprovedFirstArt":boolean,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
   "WeekDisplayText":string,
      /**  EnablePCID  */  
   "EnablePCID":boolean,
      /**  The output bin from the resource  */  
   "OutputBin":string,
      /**  The output warehouse from the resource  */  
   "OutputWarehouse":string,
      /**  Internal flag used for the row rules to control whether the Lot columns should be enabled.  */  
   "EnableLot":boolean,
      /**  Lot number that is to be added to the PCID  */  
   "LotNum":string,
      /**  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  */  
   "PrintPCIDContents":boolean,
      /**  Indicates if the labor detail has attachments  */  
   "HasAttachments":boolean,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set for LaborQty  */  
   "LaborAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for LaborQty  */  
   "LaborAttributeSetShortDescription":string,
      /**  Indicates if recall and delete should be disabled  */  
   "DisableRecallAndDelete":boolean,
      /**  List of available role codes  */  
   "RoleCdList":string,
      /**  Indicates if the row is selected for submit, recall, or copy  */  
   "RowSelected":boolean,
      /**  Start date/time for calendar appoinment  */  
   "AppointmentStart":string,
      /**  End date/time for calendar appoinment  */  
   "AppointmentEnd":string,
      /**  Title to display for the calendar appointment  */  
   "AppointmentTitle":string,
      /**  PDF Form Template linked to the Job Operation  */  
   "TemplateID":string,
      /**  Flag to validate if the transaction includes WIP  */  
   "WIPTransaction":boolean,
      /**  Revision for DiscrepQty  */  
   "DiscrepRevision":string,
      /**  Revision for LaborQty  */  
   "LaborRevision":string,
      /**  Revision for ScrapQty  */  
   "ScrapRevision":string,
   "TrackInventoryByRevision":boolean,
      /**  Indicates whether co-parts can be entered  */  
   "ReportPartQtyAllowed":boolean,
   "BitFlag":number,
   "DiscrpRsnDescription":string,
   "EmpBasicLastName":string,
   "EmpBasicFirstName":string,
   "EmpBasicName":string,
   "ExpenseCodeDescription":string,
   "HCMIntregationHCMEnabled":boolean,
   "HCMStatusStatus":string,
   "IndirectDescription":string,
   "JCDeptDescription":string,
   "JobAsmblPartNum":string,
   "JobAsmblDescription":string,
   "MachineDescription":string,
   "OpCodeOpDesc":string,
   "OpDescOpDesc":string,
   "PayMethodType":number,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "PhaseIDDescription":string,
   "ProjectDescription":string,
   "ResourceGrpDescription":string,
   "ResReasonDescription":string,
   "ReWorkReasonDescription":string,
   "RoleCdRoleDescription":string,
   "ScrapReasonDescription":string,
   "ShiftDescription":string,
   "TimeTypCdDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartTranListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   "TranClass":string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  date of transaction.  */  
   "TranDate":string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   "CostMethod":string,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Assembly Sequence #  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   "PackType":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   "PackLine":number,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**  The line # of detail record on the purchase order.  */  
   "POLine":number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   "PORelNum":number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   "WareHouse2":string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   "BinNum2":string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**  The sales order line that this transaction is associated with.  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   "OrderRelNum":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   "RevisionNum":string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   "VendorNum":number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   "PurPoint":string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "POReceiptQty":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   "POUnitCost":number,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   "InvoiceNum":string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   "InvoiceLine":number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   "InvAdjSrc":string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   "InvAdjReason":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Transfer "From/To" lot number.  */  
   "LotNum2":string,
      /**  Transfer "From/To" Part Dimension  */  
   "DimCode2":string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   "DUM2":string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   "DimConvFactor2":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   "GLTrans":boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   "Costed":boolean,
      /**  DMR number used to identify the related DMR record.  */  
   "DMRNum":number,
      /**  DMR action number  */  
   "ActionNum":number,
      /**  RMA Number  */  
   "RMANum":number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPostingReqd":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Site Identifier.  */  
   "Plant2":string,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   "CallLine":number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   "MatNum":number,
      /**  Job Number of transfer source/target.  */  
   "JobNum2":string,
      /**  Assembly Sequence  of transfer source/target.  */  
   "AssemblySeq2":number,
      /**  Seq # of transfer source/target.  */  
   "JobSeq2":number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   "CustNum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMA Receipt  */  
   "RMAReceipt":number,
      /**  RMA Disposition  */  
   "RMADisp":number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   "OtherDivValue":number,
      /**  Site Transaction Number  */  
   "PlantTranNum":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfID":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   "BeginQty":number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   "AfterQty":number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   "BegBurUnitCost":number,
      /**  Labor Unit cost before the costing calculation was run  */  
   "BegLbrUnitCost":number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   "BegMtlBurUnitCost":number,
      /**  Material Unit Cost before the costing calculation was run  */  
   "BegMtlUnitCost":number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   "BegSubUnitCost":number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   "AfterBurUnitCost":number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   "AfterLbrUnitCost":number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   "AfterMtlBurUnitCost":number,
      /**  Material Unit Cost after the costing calculation was run  */  
   "AfterMtlUnitCost":number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   "AfterSubUnitCost":number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   "PlantCostValue":number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   "EmpID":string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   "ReconcileNum":number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   "CostID":string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   "FIFODate":string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   "FIFOSeq":number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM":string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM2":string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   "FIFOAction":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CCYear":number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   "CCMonth":number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CycleSeq":number,
      /**  GUID - reference on PE ABT.  */  
   "ABTUID":string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   "BaseCostMethod":string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   "RevertStatus":number,
      /**  Reference on revert line  by SySRowID.  */  
   "RevertID":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   "VarTarget":string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   "FIFOSubSeq":number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlUnitCost":number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltLbrUnitCost":number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltBurUnitCost":number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltSubUnitCost":number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlBurUnitCost":number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltExtCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlMtlUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlLabUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlSubUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlBurdenUnitCost":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   "PBInvNum":number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   "LoanFlag":string,
      /**  Unique identifier of the Asset.  */  
   "AssetNum":string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   "AdditionNum":number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   "DisposalNum":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used by Project Analysis process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process  */  
   "AsOfSeq":number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   "MscNum":number,
      /**  ODC Unit Cost  */  
   "ODCUnitCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TranRefType  */  
   "TranRefType":number,
      /**  PCID  */  
   "PCID":string,
      /**  PCIDCollapseCounter  */  
   "PCIDCollapseCounter":number,
      /**  PCID2  */  
   "PCID2":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  ExtMtlCost  */  
   "ExtMtlCost":number,
      /**  ExtLbrCost  */  
   "ExtLbrCost":number,
      /**  ExtBurCost  */  
   "ExtBurCost":number,
      /**  ExtSubCost  */  
   "ExtSubCost":number,
      /**  ExtMtlBurCost  */  
   "ExtMtlBurCost":number,
      /**  ExtMtlMtlCost  */  
   "ExtMtlMtlCost":number,
      /**  ExtMtlLabCost  */  
   "ExtMtlLabCost":number,
      /**  ExtMtlSubCost  */  
   "ExtMtlSubCost":number,
      /**  ExtMtlBurdenCost  */  
   "ExtMtlBurdenCost":number,
      /**  MYImportNum  */  
   "MYImportNum":string,
      /**  AutoReverse  */  
   "AutoReverse":boolean,
      /**  RevTranNum  */  
   "RevTranNum":number,
      /**  RevSysDate  */  
   "RevSysDate":string,
      /**  RevSysTime  */  
   "RevSysTime":number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   "ExtNonRecoverableCost":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  WIPPCID  */  
   "WIPPCID":string,
      /**  WIPPCID2  */  
   "WIPPCID2":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
   "JobSubUnitCost":number,
   "LegalNumberNumber":string,
   "LegalNumberPrefix":string,
   "LegalNumberPrefixList":string,
   "LegalNumberReadOnlyFields":string,
   "LegalNumberYear":number,
   "MtlLbrUnitCost":number,
   "MtlQueueRowId":string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   "MultiEndParts":boolean,
   "OnHandQty":number,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   "OverRideCosts":boolean,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "PackNumName":string,
   "PartDescriptionAsm":string,
   "PartDescriptionJH":string,
   "PartDescriptionMS":string,
   "PartDescriptionSP":string,
      /**  Optional lot number description.  */  
   "PartLotPartLotDescription":string,
   "PartNumAsm":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
   "PartNumJH":string,
   "PartNumMS":string,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
   "PartNumSP":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
   "QtyAvailToComplete":number,
   "QtyBearing":boolean,
      /**  Quantity Completed  */  
   "QtyCompleted":number,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "SalvageQtyToDate":number,
   "SerialNoTempTranID":number,
   "ThisTranQty":number,
   "TreeDisplay":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line  */  
   "VendorPPNumAddress1":string,
      /**  Second address line  */  
   "VendorPPNumAddress2":string,
      /**  Third address line  */  
   "VendorPPNumAddress3":string,
      /**  City portion of the address  */  
   "VendorPPNumCity":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "VendorPPNumCountry":string,
      /**  Purchase Point Name...can't be blank.  */  
   "VendorPPNumName":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "VendorPPNumPrimPCon":number,
      /**  State portion of the address  */  
   "VendorPPNumState":string,
      /**  Postal Code or Zip code portion of the address  */  
   "VendorPPNumZip":string,
      /**  Description.  */  
   "WarehouseDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
   "CostMethodDisplay":string,
      /**  Description for the dimension code.  */  
   "DimCodeDimCodeDescription":string,
   "DIMDescription":string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   "DisableFieldPart":boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   "DispSysTime":string,
   "DispUOM":string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   "DMRNumPartDescription":string,
   "dummyKeyField":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "FromBinDescription":string,
      /**  The Plant name. Used on shipping reports.  */  
   "FromPlantName":string,
      /**  Description.  */  
   "FromWareHouseDescription":string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   "FullPhysical":boolean,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Inventory subcontract unit cost  */  
   "InvBurUnitCost":number,
      /**  Inventory Labor unit cost.  */  
   "InvLbrUnitCost":number,
      /**  Inventory burden unit cost  */  
   "InvMtlBurUnitCost":number,
      /**  Inventory material unit cost  */  
   "InvMtlUnitCost":number,
      /**  Inventory subcontract unit cost.  */  
   "InvSubUnitCost":number,
   "IssuedComplete":boolean,
   "JobBurUnitCost":number,
   "JobLbrUnitCost":number,
   "JobMtlBurUnitCost":number,
   "JobMtlUnitCost":number,
   "Selected":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   "TranClass":string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  date of transaction.  */  
   "TranDate":string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   "CostMethod":string,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Assembly Sequence #  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   "PackType":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   "PackLine":number,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**  The line # of detail record on the purchase order.  */  
   "POLine":number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   "PORelNum":number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   "WareHouse2":string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   "BinNum2":string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**  The sales order line that this transaction is associated with.  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   "OrderRelNum":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   "RevisionNum":string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   "VendorNum":number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   "PurPoint":string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "POReceiptQty":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   "POUnitCost":number,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   "InvoiceNum":string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   "InvoiceLine":number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   "InvAdjSrc":string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   "InvAdjReason":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Transfer "From/To" lot number.  */  
   "LotNum2":string,
      /**  Transfer "From/To" Part Dimension  */  
   "DimCode2":string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   "DUM2":string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   "DimConvFactor2":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   "GLTrans":boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   "Costed":boolean,
      /**  DMR number used to identify the related DMR record.  */  
   "DMRNum":number,
      /**  DMR action number  */  
   "ActionNum":number,
      /**  RMA Number  */  
   "RMANum":number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPostingReqd":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Site Identifier.  */  
   "Plant2":string,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   "CallLine":number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   "MatNum":number,
      /**  Job Number of transfer source/target.  */  
   "JobNum2":string,
      /**  Assembly Sequence  of transfer source/target.  */  
   "AssemblySeq2":number,
      /**  Seq # of transfer source/target.  */  
   "JobSeq2":number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   "CustNum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMA Receipt  */  
   "RMAReceipt":number,
      /**  RMA Disposition  */  
   "RMADisp":number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   "OtherDivValue":number,
      /**  Site Transaction Number  */  
   "PlantTranNum":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfID":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   "BeginQty":number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   "AfterQty":number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   "BegBurUnitCost":number,
      /**  Labor Unit cost before the costing calculation was run  */  
   "BegLbrUnitCost":number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   "BegMtlBurUnitCost":number,
      /**  Material Unit Cost before the costing calculation was run  */  
   "BegMtlUnitCost":number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   "BegSubUnitCost":number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   "AfterBurUnitCost":number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   "AfterLbrUnitCost":number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   "AfterMtlBurUnitCost":number,
      /**  Material Unit Cost after the costing calculation was run  */  
   "AfterMtlUnitCost":number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   "AfterSubUnitCost":number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   "PlantCostValue":number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   "EmpID":string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   "ReconcileNum":number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   "CostID":string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   "FIFODate":string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   "FIFOSeq":number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM":string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM2":string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   "FIFOAction":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CCYear":number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   "CCMonth":number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CycleSeq":number,
      /**  GUID - reference on PE ABT.  */  
   "ABTUID":string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   "BaseCostMethod":string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   "RevertStatus":number,
      /**  Reference on revert line  by SySRowID.  */  
   "RevertID":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   "VarTarget":string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   "FIFOSubSeq":number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlUnitCost":number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltLbrUnitCost":number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltBurUnitCost":number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltSubUnitCost":number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlBurUnitCost":number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltExtCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlMtlUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlLabUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlSubUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlBurdenUnitCost":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   "PBInvNum":number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   "LoanFlag":string,
      /**  Unique identifier of the Asset.  */  
   "AssetNum":string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   "AdditionNum":number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   "DisposalNum":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used by Project Analysis process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process  */  
   "AsOfSeq":number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   "MscNum":number,
      /**  ODC Unit Cost  */  
   "ODCUnitCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TranRefType  */  
   "TranRefType":number,
      /**  PCID  */  
   "PCID":string,
      /**  PCIDCollapseCounter  */  
   "PCIDCollapseCounter":number,
      /**  PCID2  */  
   "PCID2":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  ExtMtlCost  */  
   "ExtMtlCost":number,
      /**  ExtLbrCost  */  
   "ExtLbrCost":number,
      /**  ExtBurCost  */  
   "ExtBurCost":number,
      /**  ExtSubCost  */  
   "ExtSubCost":number,
      /**  ExtMtlBurCost  */  
   "ExtMtlBurCost":number,
      /**  ExtMtlMtlCost  */  
   "ExtMtlMtlCost":number,
      /**  ExtMtlLabCost  */  
   "ExtMtlLabCost":number,
      /**  ExtMtlSubCost  */  
   "ExtMtlSubCost":number,
      /**  ExtMtlBurdenCost  */  
   "ExtMtlBurdenCost":number,
      /**  MYImportNum  */  
   "MYImportNum":string,
      /**  AutoReverse  */  
   "AutoReverse":boolean,
      /**  RevTranNum  */  
   "RevTranNum":number,
      /**  RevSysDate  */  
   "RevSysDate":string,
      /**  RevSysTime  */  
   "RevSysTime":number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   "ExtNonRecoverableCost":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  WIPPCID  */  
   "WIPPCID":string,
      /**  WIPPCID2  */  
   "WIPPCID2":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "CallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "ContractCode":string,
   "DIMDescription":string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   "DisableFieldPart":boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   "DispSysTime":string,
   "DispUOM":string,
   "dummyKeyField":string,
   "EnableSerialNumbers":boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "FSACallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "FSAContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "FSAContractNum":number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   "FSAEmpID":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   "FSAWarrantyCode":string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   "FullPhysical":boolean,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Inventory subcontract unit cost  */  
   "InvBurUnitCost":number,
      /**  Inventory Labor unit cost.  */  
   "InvLbrUnitCost":number,
      /**  Inventory burden unit cost  */  
   "InvMtlBurUnitCost":number,
      /**  Inventory material unit cost  */  
   "InvMtlUnitCost":number,
      /**  Inventory subcontract unit cost.  */  
   "InvSubUnitCost":number,
   "IssuedComplete":boolean,
   "JobBurUnitCost":number,
   "JobLbrUnitCost":number,
   "JobMtlBurUnitCost":number,
   "JobMtlUnitCost":number,
   "JobSubUnitCost":number,
   "LegalNumberNumber":string,
   "LegalNumberPrefix":string,
   "LegalNumberPrefixList":string,
   "LegalNumberReadOnlyFields":string,
   "LegalNumberYear":number,
   "MtlLbrUnitCost":number,
   "MtlQueueRowId":string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   "MultiEndParts":boolean,
   "OnHandQty":number,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   "OverRideCosts":boolean,
   "PartDescriptionAsm":string,
   "PartDescriptionJH":string,
   "PartDescriptionMS":string,
   "PartDescriptionSP":string,
   "PartNumAsm":string,
   "PartNumJH":string,
   "PartNumMS":string,
   "PartNumSP":string,
   "QtyAvailToComplete":number,
   "QtyBearing":boolean,
      /**  Quantity Completed  */  
   "QtyCompleted":number,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "SalvageQtyToDate":number,
   "SerialNoTempTranID":number,
   "ThisTranQty":number,
      /**  Transaction Amount  */  
   "TranAmount":number,
   "TreeDisplay":string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
      /**  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "ContractNum":number,
   "CostMethodDisplay":string,
      /**  Number of pieces for inventory attribute tracked parts  */  
   "DispNumberOfPieces":number,
   "RevisionNumAsm":string,
   "RevisionNumMS":string,
   "RevisionNumSP":string,
   "PlantConfCtrlEnablePackageControl":boolean,
      /**  Description for AttributeSetID associated with PartNumMS  */  
   "AttributeSetDescriptionMS":string,
      /**  AttributeSetID associated with PartNumMS  */  
   "AttributeSetIDMS":number,
      /**  AttributeSetShortDescription associated with PartNumMS  */  
   "AttributeSetShortDescriptionMS":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CallLineLineDesc":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "CustNumName":string,
   "DimCodeDimCodeDescription":string,
   "DMRNumPartDescription":string,
   "FromBinDescription":string,
   "FromPlantName":string,
   "FromWareHouseDescription":string,
   "InvoiceNumDescription":string,
   "JobNumPartDescription":string,
   "MatNumLineDesc":string,
   "OrderLineLineDesc":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PackLineLineDesc":string,
   "PackNumName":string,
   "PartLotPartLotDescription":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PlantName":string,
   "POLineVenPartNum":string,
   "POLinePartNum":string,
   "POLineLineDesc":string,
   "RMALineLineDesc":string,
   "VendorNumName":string,
   "VendorNumAddress3":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumAddress2":string,
   "VendorNumVendorID":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorPPNumAddress1":string,
   "VendorPPNumAddress2":string,
   "VendorPPNumPrimPCon":number,
   "VendorPPNumAddress3":string,
   "VendorPPNumCountry":string,
   "VendorPPNumState":string,
   "VendorPPNumZip":string,
   "VendorPPNumCity":string,
   "VendorPPNumName":string,
   "WarehouseDescription":string,
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
      @param sysDate
      @param sysTime
      @param tranNum
   */  
export interface DeleteByID_input{
   sysDate:string,
   sysTime:number,
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLCostTransTableset{
   PartTran:Erp_Tablesets_PartTranRow[],
   InvcDtl:Erp_Tablesets_InvcDtlRow[],
   LaborDtl:Erp_Tablesets_LaborDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   XRevisionNum:string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   PartNum:string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   LineDesc:string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   IUM:string,
      /**  Our Current Revision Number for this Part.  */  
   RevisionNum:string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   POLine:string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   TaxCatID:string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   Commissionable:boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   DiscountPercent:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   OurOrderQty:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   ProdCode:string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   OurShipQty:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  The packing slip line number that is being invoiced.  */  
   PackLine:number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   OrderNum:number,
      /**  The associated sales order line number.  */  
   OrderLine:number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   ShipToNum:string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   ShipDate:string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   ShipViaCode:string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   AdvanceBillCredit:number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   DocAdvanceBillCredit:number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   CustNum:number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   InvoiceComment:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   ShpConNum:number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlBurUnitCost:number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   COSPostingReqd:boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPosted:boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   CallCode:string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   RMALine:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   JournalCode:string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   SellingOrderQty:number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   SellingShipQty:number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   ProjectID:string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   MilestoneID:string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   ListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   OrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   DocOrdBasedPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Sales representative commission rate.  */  
   RepRate1:number,
      /**  Sales representative commission rate.  */  
   RepRate2:number,
      /**  Sales representative commission rate.  */  
   RepRate3:number,
      /**  Sales representative commission rate.  */  
   RepRate4:number,
      /**  Sales representative commission rate.  */  
   RepRate5:number,
      /**  Sales representative commission percentage.  */  
   RepSplit1:number,
      /**  Sales representative commission percentage.  */  
   RepSplit2:number,
      /**  Sales representative commission percentage.  */  
   RepSplit3:number,
      /**  Sales representative commission percentage.  */  
   RepSplit4:number,
      /**  Sales representative commission percentage.  */  
   RepSplit5:number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   BTCustNum:number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlUnitCost:number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCLbrUnitCost:number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCBurUnitCost:number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCSubUnitCost:number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlBurUnitCost:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   RevChargeMethod:string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   OverrideReverseCharge:boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   RevChargeApplied:boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3AdvGainLoss:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping adress country Number.  */  
   OTSCountryNum:number,
      /**  Value is copied from PartTran for PE  */  
   Plant:string,
      /**  value is copied from PartTran for PE  */  
   WarehouseCode:string,
      /**  value is copied from PartTran for PE  */  
   CallLine:number,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  FK to the Finance Charges table  */  
   FinChargeCode:string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   ABTUID:string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocInUnitPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocInExtPrice:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   InDiscount:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocInDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   InTotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   DocInTotalMiscChrg:number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   InListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   InOrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   DocInOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   AssetNum:string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   DisposalNum:number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   PBLineType:string,
      /**  Invoice line reference  */  
   InvoiceLineRef:number,
      /**  Invoice Number Reference  */  
   InvoiceRef:number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   LotNum:string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   PBInvoiceLine:number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   RAID:number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   RADtlID:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   ChargeDefRev:boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DefRevPosted  */  
   DefRevPosted:boolean,
      /**  Unit price of Invoice linked to Bill of Exchange in original currency.  */  
   LinkedInvcUnitPrice:number,
      /**  Withholding Tax Amount in reporting currency  */  
   DspWithholdAmt:number,
      /**  Withholding Tax Amount in document currency  */  
   DocDspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt1DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt2DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt3DspWithholdAmt:number,
      /**  Currency code from linked Invoice Header  */  
   LinkedCurrencyCode:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  PEBOEHeadNum  */  
   PEBOEHeadNum:number,
      /**  MXSellingShipQty  */  
   MXSellingShipQty:number,
      /**  MXUnitPrice  */  
   MXUnitPrice:number,
      /**  DocMXUnitPrice  */  
   DocMXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3MXUnitPrice:number,
      /**  CustCostCenter  */  
   CustCostCenter:string,
      /**  DEIsServices  */  
   DEIsServices:boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   DEIsSecurityFinancialDerivative:boolean,
      /**  DEInternationalSecuritiesID  */  
   DEInternationalSecuritiesID:string,
      /**  DEIsInvestment  */  
   DEIsInvestment:boolean,
      /**  DEPayStatCode  */  
   DEPayStatCode:string,
      /**  DefRevEndDate  */  
   DefRevEndDate:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  Indicates tha this invoice Line was reclassified.  */  
   Reclassified:boolean,
      /**  Enables the user the ability to override the Percent or Amount of revenue to be deferred  */  
   PartiallyDefer:boolean,
      /**  Percentage of revenue to be deferred for this line item  */  
   DeferredPercent:number,
      /**  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  */  
   Reclass:boolean,
      /**  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  */  
   DeferredOnly:boolean,
      /**  Reclassification Code. This field will be required if Reclass is checked.  */  
   ReclassCodeID:string,
      /**  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  */  
   ReclassReasonCode:string,
      /**  Internal comments for reclassification entered by the user.  */  
   ReclassComments:string,
      /**  Deferred Revenue Amount in base currency  */  
   DeferredRevAmt:number,
      /**  Deferred Revenue Amount in document currency  */  
   DocDeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt1DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt2DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt3DeferredRevAmt:number,
      /**  ChargeReclass  */  
   ChargeReclass:boolean,
      /**  DEDenomination  */  
   DEDenomination:string,
      /**  DropShipPONum  */  
   DropShipPONum:number,
      /**  DocInAdvanceBillCredit  */  
   DocInAdvanceBillCredit:number,
      /**  InAdvanceBillCredit  */  
   InAdvanceBillCredit:number,
      /**  Rpt1InAdvanceBillCredit  */  
   Rpt1InAdvanceBillCredit:number,
      /**  Rpt2InAdvanceBillCredit  */  
   Rpt2InAdvanceBillCredit:number,
      /**  Rpt3InAdvanceBillCredit  */  
   Rpt3InAdvanceBillCredit:number,
      /**  MYIndustryCode  */  
   MYIndustryCode:string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  ConsolidateLines  */  
   ConsolidateLines:boolean,
      /**  MXCustomsDuty  */  
   MXCustomsDuty:string,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  MXProdServCode  */  
   MXProdServCode:string,
      /**  Quote number to which this line item detail record is associated with.  */  
   QuoteNum:number,
      /**  Quote Line number from which this invoice line was created from.  */  
   QuoteLine:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  MXCustomsUMFrom  */  
   MXCustomsUMFrom:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PETaxExempt  */  
   PETaxExempt:string,
      /**  Order number on the Invoicing Company.  */  
   CColOrderNum:number,
      /**  Order number line the Invoicing Company.  */  
   CColOrderLine:number,
      /**  Order number release the Invoicing Company.  */  
   CColOrderRel:number,
      /**  Invoice Line reference on the Invoicing Company.  */  
   CColInvoiceLineRef:number,
      /**  Packing slip number on the Invoicing Company.  */  
   CColPackNum:number,
      /**  Packing slip line number on the Invoicing Company.  */  
   CColPackLine:number,
      /**  Drop shipment packing slip number on the Invoicing Company.  */  
   CColDropShipPackSlip:string,
      /**  Drop shipment packing slip line number on the Invoicing Company.  */  
   CColDropShipPackSlipLine:number,
      /**  Ship To Customer ID from the Invoice Line in the subsidiary company.  */  
   CColShipToCustID:string,
      /**  Ship To from the Invoice Line in the subsidiary company.  */  
   CColShipToNum:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  */  
   ServiceSource:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  */  
   AssemblySeq:number,
      /**  Job Mtl seq used to create invoice line from service call job  */  
   MtlSeq:number,
      /**  Job subcontract oper seq used to create invoice line from service call job  */  
   OprSeq:number,
      /**  Indicates the labor type of the LaborDtl used to create invoice from service call job.  */  
   LaborType:string,
      /**  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  */  
   BillableLaborHrs:number,
      /**  Billable rate used to create invoice line from labor related to service call job. In base currency.  */  
   BillableLaborRate:number,
      /**  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  */  
   ServiceSourceType:string,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  Adv bill enabled flag  */  
   AdvBillEnabled:boolean,
   AllowTaxCodeUpd:boolean,
      /**  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  */  
   AllowUpdPartDefer:boolean,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   BillToCustID:string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   BTCustName:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   CheckAmortAmounts:boolean,
   CNGTIDescription1:string,
   CNGTIDescription2:string,
   CNGTIDescription3:string,
      /**  CSF China, discount tax amount  */  
   CNGTIDiscountTaxAmount:number,
   CNGTIIUM:string,
   CNGTINetAmount:number,
   CNGTIPartDescription:string,
   CNGTISpecification:string,
   CNGTITaxAmount:number,
   CNGTITaxCode:string,
   CNGTITaxPercent:number,
   CNGTITotalAmount:number,
      /**  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  */  
   CNGTIUnitPrice:number,
   ContractSuspended:boolean,
      /**  Currency code from InvcHead.  */  
   CurrencyCode:string,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   CustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   CustName:string,
      /**  Invoice Detail Customer Name  */  
   CustomerName:string,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   DeleteRASchedule:boolean,
   DispGLAcct:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  PO number for display.  */  
   DispPONum:string,
      /**  Ship to display address  */  
   DispShipToAddr:string,
      /**  Document display symbol.  */  
   DocDisplaySymbol:string,
   DocDspUnitPrice:number,
      /**  Document discount amount  */  
   DocLessDiscount:number,
      /**  Doc line tax  */  
   DocLineTax:number,
      /**  ExtPrice-disc+misc charges.  */  
   DocLineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   DocPEDetAmt:number,
      /**  Drop Shipment  */  
   DropShipment:boolean,
      /**  Display advance bill credit  */  
   DspAdvanceBillCredit:number,
      /**  Display discount  */  
   DspDiscount:number,
      /**  Display documents advance bill credit  */  
   DspDocAdvanceBillCredit:number,
      /**  Display document discount  */  
   DspDocDiscount:number,
      /**  Display document ext price  */  
   DspDocExtPrice:number,
      /**  Display document less discount  */  
   DspDocLessDiscount:number,
      /**  Display document line tax  */  
   DspDocLineTax:number,
      /**  Display document line total  */  
   DspDocLineTotal:number,
      /**  Display document total misc. charge  */  
   DspDocTotalMiscChrg:number,
      /**  Display ext price  */  
   DspExtPrice:number,
      /**  Display Invoice Reference  */  
   DspInvoiceRef:number,
      /**  Display less discount  */  
   DspLessDiscount:number,
      /**  Display line tax  */  
   DspLineTax:number,
      /**  Display line total  */  
   DspLineTotal:number,
      /**  Display our ship qty  */  
   DspOurShipQty:number,
      /**  Display selling ship qty  */  
   DspSellingShipQty:number,
   DspTaxExempt:string,
      /**  Display total misc. charges  */  
   DspTotalMiscChrg:number,
   DspUnitPrice:number,
      /**  Invoice head due date.  */  
   DueDate:string,
      /**  FSA Technician  */  
   EmpID:string,
   EnableDspWithholdAmt:boolean,
   EnableRMADelete:boolean,
   EnableRMAUpdate:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Group associated to the invoice  */  
   GroupID:string,
   InPrice:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Invoice Header Legal Number  */  
   InvLegalNum:string,
      /**  Invoice Date from InvcHead.  */  
   InvoiceDate:string,
      /**  Invoice header type  */  
   InvoiceType:string,
      /**  Is commission button sensitive  */  
   IsCommisBtnSensitive:boolean,
      /**  Set to true if intrastat is enabled.  */  
   IsIntrastatSensitive:boolean,
      /**  Tax buton sensitive or not.  */  
   IsTaxBtnSensitive:boolean,
      /**  display discount  */  
   LessDiscount:number,
      /**  Line tax amount  */  
   LineTax:number,
      /**  ExtPrice-disc+misc charges.  */  
   LineTotal:number,
   LinkedCurrencySymbol:string,
      /**  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  */  
   NoShipTaxRgnInfo:boolean,
      /**  Open invoice flag from InvcHead.  */  
   OpenInvoice:boolean,
      /**  OrderUM display  */  
   OrderUM:string,
      /**  original tax category  */  
   OrigTaxCat:string,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   PEDetAmt:number,
      /**  PE Detraction good or service code description  */  
   PEDetrGoodServiceCodeDesc:string,
   PEDspCurrencySymbol:string,
      /**  PE VAT Exemption Reason  */  
   PEVATExemptionReason:string,
      /**  Posted flag from the InvcHead.  */  
   Posted:boolean,
   RADesc:string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   RASchedExists:boolean,
      /**  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  */  
   RemoveManAdTax:boolean,
   Rpt1DspAdvanceBillCredit:number,
   Rpt1DspDiscount:number,
   Rpt1DspExtPrice:number,
   Rpt1DspLessDiscount:number,
   Rpt1DspLineTax:number,
   Rpt1DspLineTotal:number,
   Rpt1DspTotalMiscChrg:number,
   Rpt1DspUnitPrice:number,
   Rpt1LineTax:number,
   Rpt1LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt1PEDetAmt:number,
   Rpt2DspAdvanceBillCredit:number,
   Rpt2DspDiscount:number,
   Rpt2DspExtPrice:number,
   Rpt2DspLessDiscount:number,
   Rpt2DspLineTax:number,
   Rpt2DspLineTotal:number,
   Rpt2DspTotalMiscChrg:number,
   Rpt2DspUnitPrice:number,
   Rpt2LineTax:number,
   Rpt2LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt2PEDetAmt:number,
   Rpt3DspAdvanceBillCredit:number,
   Rpt3DspDiscount:number,
   Rpt3DspExtPrice:number,
   Rpt3DspLessDiscount:number,
   Rpt3DspLineTax:number,
   Rpt3DspLineTotal:number,
   Rpt3DspTotalMiscChrg:number,
   Rpt3DspUnitPrice:number,
   Rpt3LineTax:number,
   Rpt3LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt3PEDetAmt:number,
      /**  1st sales rep of the invoice.  */  
   SalesRepCode1:string,
      /**  2nd sales rep of the invoice header.  */  
   SalesRepCode2:string,
      /**  3rd sales rep code of the invoice header.  */  
   SalesRepCode3:string,
      /**  4th sales rep code of the invoice header.  */  
   SalesRepCode4:string,
      /**  5th salesrep code of the invoice header.  */  
   SalesRepCode5:string,
      /**  1st sales rep name  */  
   SalesRepName1:string,
      /**  2nd sales rep name  */  
   SalesRepName2:string,
      /**  3rd sales rep name  */  
   SalesRepName3:string,
      /**  4th sales rep name  */  
   SalesRepName4:string,
      /**  5th sales rep name  */  
   SalesRepName5:string,
   ShipToContactEMailAddress:string,
   ShipToContactFaxNum:string,
   ShipToContactName:string,
   ShipToContactPhoneNum:string,
      /**  Ship Head Legal Number  */  
   ShpLegalNum:string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   SoldToCustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   SoldToCustName:string,
      /**  Terms code from InvcHead.  */  
   TermsCode:string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
      /**  This flag allow updating Reclassification data.  */  
   AllowReclassify:boolean,
      /**  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  */  
   LineAmtRecalcd:boolean,
      /**  Set to true if extra trade statistics is enabled.  */  
   IsExtrastatSensitive:boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
   BitFlag:number,
   CallCodeCallDescription:string,
   CommodityCodeDescription:string,
   ContractCodeContractDescription:string,
   ContractNumSuspended:boolean,
   CustCntName:string,
   CustCntMiddleName:string,
   CustCntFirstName:string,
   CustCntFaxNum:string,
   CustCntCorpName:string,
   CustCntPhoneNum:string,
   CustCntLastName:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumAllowShipTo3:boolean,
   CustNumBTName:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   JournalCodeJrnlDescription:string,
   MilestoneIDDescription:string,
   MXProdServCodeDesc:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OTSCntryEUMember:boolean,
   OTSCntryISOCode:string,
   OTSCntryDescription:string,
   PackLineLineDesc:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   ReclassCodeDescription:string,
   ReclassReasonDescription:string,
   RMALineLineDesc:string,
   SalesCatIDDescription:string,
   ShipToCustCustID:string,
   ShipToCustName:string,
   ShipToCustBTName:string,
   ShipToNumInactive:boolean,
   ShipToNumName:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TaxCatIDDescription:string,
   TaxRegionDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborType:string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborTypePseudo:string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   ReWork:boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   ReworkReasonCode:string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   AssemblySeq:number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   OprSeq:number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   JCDept:string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   ResourceGrpID:string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   OpCode:string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   LaborHrs:number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   BurdenHrs:number,
      /**  The Total production quantity reported.  */  
   LaborQty:number,
      /**  The reported scrap quantity.  */  
   ScrapQty:number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   ScrapReasonCode:string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   SetupPctComplete:number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   Complete:boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   IndirectCode:string,
      /**  A short note that the user can make about the labor transaction.  */  
   LaborNote:string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   ExpenseCode:string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   AppliedToSchedule:boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   ClockInMInute:number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   ClockOutMinute:number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   ClockInDate:string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   ClockinTime:number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   ClockOutTime:number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   ActiveTrans:boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   OverRidePayRate:number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   LaborRate:number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   BurdenRate:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   ResourceID:string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   OpComplete:boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   EarnedHrs:number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   AddedOper:boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   PayrollDate:string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   GLTrans:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   InspectionPending:boolean,
      /**  The service call that this service record belongs to.  */  
   CallNum:number,
      /**  The line number of the service call this labor detail is for.  */  
   CallLine:number,
      /**  the service that is being performed on this line.  */  
   ServNum:number,
      /**  A unique code that identifies the Service  */  
   ServCode:string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   WipPosted:boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   DiscrepQty:number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   DiscrpRsnCode:string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   ParentLaborDtlSeq:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   LaborEntryMethod:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   BFLaborReq:boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   ABTUID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Project Role Code  */  
   RoleCd:string,
      /**  Time Type Code  */  
   TimeTypCd:string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   PBInvNum:number,
      /**  The payment method of the time.  */  
   PMUID:number,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**  The date the time received final approval.  */  
   ApprovedDate:string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   QuickEntryCode:string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   TimeStatus:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   CreatedViaTEWeekView:boolean,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  The User ID of the submitter.  */  
   SubmittedBy:string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   PBRateFrom:string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   PBCurrencyCode:string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   PBHours:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   DocPBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt1PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt2PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt3PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   DocPBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt1PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt2PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt3PBChargeAmt:number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  Links to PActDtl.ActID  */  
   ActID:number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   DtailID:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used By Project Analysis Process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process.  */  
   AsOfSeq:number,
      /**  JDFInputFiles  */  
   JDFInputFiles:string,
      /**  JDFNumberOfPages  */  
   JDFNumberOfPages:string,
      /**  BatchWasSaved  */  
   BatchWasSaved:string,
      /**  AssignToBatch  */  
   AssignToBatch:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchRequestMove  */  
   BatchRequestMove:boolean,
      /**  BatchPrint  */  
   BatchPrint:boolean,
      /**  BatchLaborHrs  */  
   BatchLaborHrs:number,
      /**  BatchPctOfTotHrs  */  
   BatchPctOfTotHrs:number,
      /**  BatchQty  */  
   BatchQty:number,
      /**  BatchTotalExpectedHrs  */  
   BatchTotalExpectedHrs:number,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Downtime  */  
   Downtime:boolean,
      /**  RefJobNum  */  
   RefJobNum:string,
      /**  RefAssemblySeq  */  
   RefAssemblySeq:number,
      /**  RefOprSeq  */  
   RefOprSeq:number,
      /**  Imported  */  
   Imported:boolean,
      /**  ImportDate  */  
   ImportDate:string,
      /**   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   TimeAutoSubmit:boolean,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  BillServiceRate  */  
   BillServiceRate:number,
      /**  Pay Hours used for HCM  */  
   HCMPayHours:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   DiscrepAttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  */  
   LaborAttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   ScrapAttributeSetID:number,
      /**  PCID  */  
   PCID:string,
      /**  NonConfPCID  */  
   NonConfPCID:string,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   AllowDirLbr:boolean,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseID:string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectID:string,
   ApprovedBy:string,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   ApprvrHasOpenTask:boolean,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   BaseCurrCodeDesc:string,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   BurdenCost:number,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   CallCode:string,
   CapabilityDescription:string,
   CapabilityID:string,
      /**  Charge rate calculated for Time and Expense approval  */  
   ChargeRate:number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   ChargeRateSRC:string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   ChgRateCurrDesc:string,
   CompleteFlag:boolean,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   ContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   ContractNum:number,
      /**  Unit of Measure used for DiscrepQty  */  
   DiscrepUOM:string,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   DisLaborType:boolean,
   DisplayJob:string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   DisPrjRoleCd:boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   DisTimeTypCd:boolean,
   DowntimeTotal:number,
   DspChangeTime:string,
   DspCreateTime:string,
   DspTotHours:string,
   DtClockIn:string,
   DtClockOut:string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   EfficiencyPercentage:number,
      /**  Labor Detail Employee Name  */  
   EmployeeName:string,
   EnableComplete:boolean,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
   EnableDiscrepQty:boolean,
   EnableInspection:boolean,
   EnableLaborQty:boolean,
   EnableNextOprSeq:boolean,
   EnablePrintTagsList:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if recall is available for an approver  */  
   EnableRecallAprv:boolean,
   EnableRequestMove:boolean,
   EnableResourceGrpID:boolean,
   EnableScrapQty:boolean,
      /**  Enable the SN Button?  */  
   EnableSN:boolean,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
   EndActivity:boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   EnteredOnCurPlant:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
   FSComplete:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Indicates if the user has access to the row  */  
   HasAccessToRow:boolean,
      /**  Indicates if the labor detail has comments  */  
   HasComments:boolean,
      /**  To tell the bo that this transaction was being modified from HH.  */  
   HH:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Indicates if the job operation is marked as fixed hours and quantity only.  */  
   ISFixHourAndQtyOnly:boolean,
   JCSystReworkReasons:boolean,
   JCSystScrapReasons:boolean,
   JobOperComplete:boolean,
   JobType:string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   JobTypeCode:string,
      /**  calculated field: LaborHrs * LaborRate  */  
   LaborCost:number,
      /**  Unit of Measure used for LaborQty  */  
   LaborUOM:string,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   LbrDay:string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   LbrMonth:string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   LbrWeek:string,
   MES:boolean,
   MultipleEmployeesText:string,
   NewDifDateFlag:number,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   NewPrjRoleCd:string,
      /**  Holds the description for NewPrjRoleCd  */  
   NewRoleCdDesc:string,
   NextAssemblySeq:number,
   NextOperDesc:string,
   NextOprSeq:number,
   NextResourceDesc:string,
      /**  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  */  
   NonConfProcessed:boolean,
   NotSubmitted:boolean,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   OkToChangeResourceGrpID:boolean,
   PartDescription:string,
   PartNum:string,
   PBAllowModify:boolean,
   PendingApprovalBy:string,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   PhaseJobNum:string,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   PhaseOprSeq:number,
   PrintNCTag:boolean,
   PrjUsedTran:string,
   ProdDesc:string,
   ProjPhaseID:string,
   RequestMove:boolean,
   ResourceDesc:string,
   RoleCdDisplayAll:boolean,
      /**  Unit of Measure used for ScrapQty.  */  
   ScrapUOM:string,
      /**  Flag field to identify if the row is being sent from MES  */  
   SentFromMES:boolean,
   StartActivity:boolean,
   TimeDisableDelete:boolean,
   TimeDisableUpdate:boolean,
   TreeNodeImageName:string,
   UnapprovedFirstArt:boolean,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
   WeekDisplayText:string,
      /**  EnablePCID  */  
   EnablePCID:boolean,
      /**  The output bin from the resource  */  
   OutputBin:string,
      /**  The output warehouse from the resource  */  
   OutputWarehouse:string,
      /**  Internal flag used for the row rules to control whether the Lot columns should be enabled.  */  
   EnableLot:boolean,
      /**  Lot number that is to be added to the PCID  */  
   LotNum:string,
      /**  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  */  
   PrintPCIDContents:boolean,
      /**  Indicates if the labor detail has attachments  */  
   HasAttachments:boolean,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set for LaborQty  */  
   LaborAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for LaborQty  */  
   LaborAttributeSetShortDescription:string,
      /**  Indicates if recall and delete should be disabled  */  
   DisableRecallAndDelete:boolean,
      /**  List of available role codes  */  
   RoleCdList:string,
      /**  Indicates if the row is selected for submit, recall, or copy  */  
   RowSelected:boolean,
      /**  Start date/time for calendar appoinment  */  
   AppointmentStart:string,
      /**  End date/time for calendar appoinment  */  
   AppointmentEnd:string,
      /**  Title to display for the calendar appointment  */  
   AppointmentTitle:string,
      /**  PDF Form Template linked to the Job Operation  */  
   TemplateID:string,
      /**  Flag to validate if the transaction includes WIP  */  
   WIPTransaction:boolean,
      /**  Revision for DiscrepQty  */  
   DiscrepRevision:string,
      /**  Revision for LaborQty  */  
   LaborRevision:string,
      /**  Revision for ScrapQty  */  
   ScrapRevision:string,
   TrackInventoryByRevision:boolean,
      /**  Indicates whether co-parts can be entered  */  
   ReportPartQtyAllowed:boolean,
   BitFlag:number,
   DiscrpRsnDescription:string,
   EmpBasicLastName:string,
   EmpBasicFirstName:string,
   EmpBasicName:string,
   ExpenseCodeDescription:string,
   HCMIntregationHCMEnabled:boolean,
   HCMStatusStatus:string,
   IndirectDescription:string,
   JCDeptDescription:string,
   JobAsmblPartNum:string,
   JobAsmblDescription:string,
   MachineDescription:string,
   OpCodeOpDesc:string,
   OpDescOpDesc:string,
   PayMethodType:number,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   PhaseIDDescription:string,
   ProjectDescription:string,
   ResourceGrpDescription:string,
   ResReasonDescription:string,
   ReWorkReasonDescription:string,
   RoleCdRoleDescription:string,
   ScrapReasonDescription:string,
   ShiftDescription:string,
   TimeTypCdDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   TranClass:string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   CostMethod:string,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Assembly Sequence #  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   PackType:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   PackLine:number,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**  The line # of detail record on the purchase order.  */  
   POLine:number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   PORelNum:number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   WareHouse2:string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   BinNum2:string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this transaction is associated with.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   RevisionNum:string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   VendorNum:number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   PurPoint:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   POReceiptQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   POUnitCost:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   InvoiceNum:string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   InvoiceLine:number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   InvAdjSrc:string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   InvAdjReason:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Transfer "From/To" lot number.  */  
   LotNum2:string,
      /**  Transfer "From/To" Part Dimension  */  
   DimCode2:string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   DUM2:string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   DimConvFactor2:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   GLTrans:boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   Costed:boolean,
      /**  DMR number used to identify the related DMR record.  */  
   DMRNum:number,
      /**  DMR action number  */  
   ActionNum:number,
      /**  RMA Number  */  
   RMANum:number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPostingReqd:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Site Identifier.  */  
   Plant2:string,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   CallLine:number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   MatNum:number,
      /**  Job Number of transfer source/target.  */  
   JobNum2:string,
      /**  Assembly Sequence  of transfer source/target.  */  
   AssemblySeq2:number,
      /**  Seq # of transfer source/target.  */  
   JobSeq2:number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   CustNum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA Receipt  */  
   RMAReceipt:number,
      /**  RMA Disposition  */  
   RMADisp:number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   OtherDivValue:number,
      /**  Site Transaction Number  */  
   PlantTranNum:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfID:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   BeginQty:number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   AfterQty:number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   BegBurUnitCost:number,
      /**  Labor Unit cost before the costing calculation was run  */  
   BegLbrUnitCost:number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   BegMtlBurUnitCost:number,
      /**  Material Unit Cost before the costing calculation was run  */  
   BegMtlUnitCost:number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   BegSubUnitCost:number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   AfterBurUnitCost:number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   AfterLbrUnitCost:number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   AfterMtlBurUnitCost:number,
      /**  Material Unit Cost after the costing calculation was run  */  
   AfterMtlUnitCost:number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   AfterSubUnitCost:number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   PlantCostValue:number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   EmpID:string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   ReconcileNum:number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   CostID:string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   FIFODate:string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   FIFOSeq:number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM:string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM2:string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   FIFOAction:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CCYear:number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   CCMonth:number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CycleSeq:number,
      /**  GUID - reference on PE ABT.  */  
   ABTUID:string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   BaseCostMethod:string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   RevertStatus:number,
      /**  Reference on revert line  by SySRowID.  */  
   RevertID:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   VarTarget:string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   FIFOSubSeq:number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltExtCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   PBInvNum:number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   LoanFlag:string,
      /**  Unique identifier of the Asset.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   AdditionNum:number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   DisposalNum:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used by Project Analysis process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process  */  
   AsOfSeq:number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   MscNum:number,
      /**  ODC Unit Cost  */  
   ODCUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TranRefType  */  
   TranRefType:number,
      /**  PCID  */  
   PCID:string,
      /**  PCIDCollapseCounter  */  
   PCIDCollapseCounter:number,
      /**  PCID2  */  
   PCID2:string,
      /**  ContractID  */  
   ContractID:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  ExtMtlCost  */  
   ExtMtlCost:number,
      /**  ExtLbrCost  */  
   ExtLbrCost:number,
      /**  ExtBurCost  */  
   ExtBurCost:number,
      /**  ExtSubCost  */  
   ExtSubCost:number,
      /**  ExtMtlBurCost  */  
   ExtMtlBurCost:number,
      /**  ExtMtlMtlCost  */  
   ExtMtlMtlCost:number,
      /**  ExtMtlLabCost  */  
   ExtMtlLabCost:number,
      /**  ExtMtlSubCost  */  
   ExtMtlSubCost:number,
      /**  ExtMtlBurdenCost  */  
   ExtMtlBurdenCost:number,
      /**  MYImportNum  */  
   MYImportNum:string,
      /**  AutoReverse  */  
   AutoReverse:boolean,
      /**  RevTranNum  */  
   RevTranNum:number,
      /**  RevSysDate  */  
   RevSysDate:string,
      /**  RevSysTime  */  
   RevSysTime:number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   ExtNonRecoverableCost:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  WIPPCID  */  
   WIPPCID:string,
      /**  WIPPCID2  */  
   WIPPCID2:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
   JobSubUnitCost:number,
   LegalNumberNumber:string,
   LegalNumberPrefix:string,
   LegalNumberPrefixList:string,
   LegalNumberReadOnlyFields:string,
   LegalNumberYear:number,
   MtlLbrUnitCost:number,
   MtlQueueRowId:string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   MultiEndParts:boolean,
   OnHandQty:number,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   OverRideCosts:boolean,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   PackNumName:string,
   PartDescriptionAsm:string,
   PartDescriptionJH:string,
   PartDescriptionMS:string,
   PartDescriptionSP:string,
      /**  Optional lot number description.  */  
   PartLotPartLotDescription:string,
   PartNumAsm:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
   PartNumJH:string,
   PartNumMS:string,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
   PartNumSP:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
   QtyAvailToComplete:number,
   QtyBearing:boolean,
      /**  Quantity Completed  */  
   QtyCompleted:number,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   SalvageQtyToDate:number,
   SerialNoTempTranID:number,
   ThisTranQty:number,
   TreeDisplay:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line  */  
   VendorPPNumAddress1:string,
      /**  Second address line  */  
   VendorPPNumAddress2:string,
      /**  Third address line  */  
   VendorPPNumAddress3:string,
      /**  City portion of the address  */  
   VendorPPNumCity:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   VendorPPNumCountry:string,
      /**  Purchase Point Name...can't be blank.  */  
   VendorPPNumName:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   VendorPPNumPrimPCon:number,
      /**  State portion of the address  */  
   VendorPPNumState:string,
      /**  Postal Code or Zip code portion of the address  */  
   VendorPPNumZip:string,
      /**  Description.  */  
   WarehouseDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
   CostMethodDisplay:string,
      /**  Description for the dimension code.  */  
   DimCodeDimCodeDescription:string,
   DIMDescription:string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   DisableFieldPart:boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   DispSysTime:string,
   DispUOM:string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   DMRNumPartDescription:string,
   dummyKeyField:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   FromBinDescription:string,
      /**  The Plant name. Used on shipping reports.  */  
   FromPlantName:string,
      /**  Description.  */  
   FromWareHouseDescription:string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   FullPhysical:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Inventory subcontract unit cost  */  
   InvBurUnitCost:number,
      /**  Inventory Labor unit cost.  */  
   InvLbrUnitCost:number,
      /**  Inventory burden unit cost  */  
   InvMtlBurUnitCost:number,
      /**  Inventory material unit cost  */  
   InvMtlUnitCost:number,
      /**  Inventory subcontract unit cost.  */  
   InvSubUnitCost:number,
   IssuedComplete:boolean,
   JobBurUnitCost:number,
   JobLbrUnitCost:number,
   JobMtlBurUnitCost:number,
   JobMtlUnitCost:number,
   Selected:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranListTableset{
   PartTranList:Erp_Tablesets_PartTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   TranClass:string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   CostMethod:string,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Assembly Sequence #  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   PackType:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   PackLine:number,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**  The line # of detail record on the purchase order.  */  
   POLine:number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   PORelNum:number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   WareHouse2:string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   BinNum2:string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this transaction is associated with.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   RevisionNum:string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   VendorNum:number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   PurPoint:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   POReceiptQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   POUnitCost:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   InvoiceNum:string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   InvoiceLine:number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   InvAdjSrc:string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   InvAdjReason:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Transfer "From/To" lot number.  */  
   LotNum2:string,
      /**  Transfer "From/To" Part Dimension  */  
   DimCode2:string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   DUM2:string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   DimConvFactor2:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   GLTrans:boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   Costed:boolean,
      /**  DMR number used to identify the related DMR record.  */  
   DMRNum:number,
      /**  DMR action number  */  
   ActionNum:number,
      /**  RMA Number  */  
   RMANum:number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPostingReqd:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Site Identifier.  */  
   Plant2:string,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   CallLine:number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   MatNum:number,
      /**  Job Number of transfer source/target.  */  
   JobNum2:string,
      /**  Assembly Sequence  of transfer source/target.  */  
   AssemblySeq2:number,
      /**  Seq # of transfer source/target.  */  
   JobSeq2:number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   CustNum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA Receipt  */  
   RMAReceipt:number,
      /**  RMA Disposition  */  
   RMADisp:number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   OtherDivValue:number,
      /**  Site Transaction Number  */  
   PlantTranNum:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfID:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   BeginQty:number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   AfterQty:number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   BegBurUnitCost:number,
      /**  Labor Unit cost before the costing calculation was run  */  
   BegLbrUnitCost:number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   BegMtlBurUnitCost:number,
      /**  Material Unit Cost before the costing calculation was run  */  
   BegMtlUnitCost:number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   BegSubUnitCost:number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   AfterBurUnitCost:number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   AfterLbrUnitCost:number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   AfterMtlBurUnitCost:number,
      /**  Material Unit Cost after the costing calculation was run  */  
   AfterMtlUnitCost:number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   AfterSubUnitCost:number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   PlantCostValue:number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   EmpID:string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   ReconcileNum:number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   CostID:string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   FIFODate:string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   FIFOSeq:number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM:string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM2:string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   FIFOAction:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CCYear:number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   CCMonth:number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CycleSeq:number,
      /**  GUID - reference on PE ABT.  */  
   ABTUID:string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   BaseCostMethod:string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   RevertStatus:number,
      /**  Reference on revert line  by SySRowID.  */  
   RevertID:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   VarTarget:string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   FIFOSubSeq:number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltExtCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   PBInvNum:number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   LoanFlag:string,
      /**  Unique identifier of the Asset.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   AdditionNum:number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   DisposalNum:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used by Project Analysis process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process  */  
   AsOfSeq:number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   MscNum:number,
      /**  ODC Unit Cost  */  
   ODCUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TranRefType  */  
   TranRefType:number,
      /**  PCID  */  
   PCID:string,
      /**  PCIDCollapseCounter  */  
   PCIDCollapseCounter:number,
      /**  PCID2  */  
   PCID2:string,
      /**  ContractID  */  
   ContractID:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  ExtMtlCost  */  
   ExtMtlCost:number,
      /**  ExtLbrCost  */  
   ExtLbrCost:number,
      /**  ExtBurCost  */  
   ExtBurCost:number,
      /**  ExtSubCost  */  
   ExtSubCost:number,
      /**  ExtMtlBurCost  */  
   ExtMtlBurCost:number,
      /**  ExtMtlMtlCost  */  
   ExtMtlMtlCost:number,
      /**  ExtMtlLabCost  */  
   ExtMtlLabCost:number,
      /**  ExtMtlSubCost  */  
   ExtMtlSubCost:number,
      /**  ExtMtlBurdenCost  */  
   ExtMtlBurdenCost:number,
      /**  MYImportNum  */  
   MYImportNum:string,
      /**  AutoReverse  */  
   AutoReverse:boolean,
      /**  RevTranNum  */  
   RevTranNum:number,
      /**  RevSysDate  */  
   RevSysDate:string,
      /**  RevSysTime  */  
   RevSysTime:number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   ExtNonRecoverableCost:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  WIPPCID  */  
   WIPPCID:string,
      /**  WIPPCID2  */  
   WIPPCID2:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   CallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   ContractCode:string,
   DIMDescription:string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   DisableFieldPart:boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   DispSysTime:string,
   DispUOM:string,
   dummyKeyField:string,
   EnableSerialNumbers:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   FullPhysical:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Inventory subcontract unit cost  */  
   InvBurUnitCost:number,
      /**  Inventory Labor unit cost.  */  
   InvLbrUnitCost:number,
      /**  Inventory burden unit cost  */  
   InvMtlBurUnitCost:number,
      /**  Inventory material unit cost  */  
   InvMtlUnitCost:number,
      /**  Inventory subcontract unit cost.  */  
   InvSubUnitCost:number,
   IssuedComplete:boolean,
   JobBurUnitCost:number,
   JobLbrUnitCost:number,
   JobMtlBurUnitCost:number,
   JobMtlUnitCost:number,
   JobSubUnitCost:number,
   LegalNumberNumber:string,
   LegalNumberPrefix:string,
   LegalNumberPrefixList:string,
   LegalNumberReadOnlyFields:string,
   LegalNumberYear:number,
   MtlLbrUnitCost:number,
   MtlQueueRowId:string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   MultiEndParts:boolean,
   OnHandQty:number,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   OverRideCosts:boolean,
   PartDescriptionAsm:string,
   PartDescriptionJH:string,
   PartDescriptionMS:string,
   PartDescriptionSP:string,
   PartNumAsm:string,
   PartNumJH:string,
   PartNumMS:string,
   PartNumSP:string,
   QtyAvailToComplete:number,
   QtyBearing:boolean,
      /**  Quantity Completed  */  
   QtyCompleted:number,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   SalvageQtyToDate:number,
   SerialNoTempTranID:number,
   ThisTranQty:number,
      /**  Transaction Amount  */  
   TranAmount:number,
   TreeDisplay:string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
      /**  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   ContractNum:number,
   CostMethodDisplay:string,
      /**  Number of pieces for inventory attribute tracked parts  */  
   DispNumberOfPieces:number,
   RevisionNumAsm:string,
   RevisionNumMS:string,
   RevisionNumSP:string,
   PlantConfCtrlEnablePackageControl:boolean,
      /**  Description for AttributeSetID associated with PartNumMS  */  
   AttributeSetDescriptionMS:string,
      /**  AttributeSetID associated with PartNumMS  */  
   AttributeSetIDMS:number,
      /**  AttributeSetShortDescription associated with PartNumMS  */  
   AttributeSetShortDescriptionMS:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CallLineLineDesc:string,
   CustNumCustID:string,
   CustNumBTName:string,
   CustNumName:string,
   DimCodeDimCodeDescription:string,
   DMRNumPartDescription:string,
   FromBinDescription:string,
   FromPlantName:string,
   FromWareHouseDescription:string,
   InvoiceNumDescription:string,
   JobNumPartDescription:string,
   MatNumLineDesc:string,
   OrderLineLineDesc:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PackLineLineDesc:string,
   PackNumName:string,
   PartLotPartLotDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PlantName:string,
   POLineVenPartNum:string,
   POLinePartNum:string,
   POLineLineDesc:string,
   RMALineLineDesc:string,
   VendorNumName:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumAddress2:string,
   VendorNumVendorID:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorPPNumAddress1:string,
   VendorPPNumAddress2:string,
   VendorPPNumPrimPCon:number,
   VendorPPNumAddress3:string,
   VendorPPNumCountry:string,
   VendorPPNumState:string,
   VendorPPNumZip:string,
   VendorPPNumCity:string,
   VendorPPNumName:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtGLCostTransTableset{
   PartTran:Erp_Tablesets_PartTranRow[],
   InvcDtl:Erp_Tablesets_InvcDtlRow[],
   LaborDtl:Erp_Tablesets_LaborDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sysDate
      @param sysTime
      @param tranNum
   */  
export interface GetByID_input{
   sysDate:string,
   sysTime:number,
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLCostTransTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLCostTransTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLCostTransTableset[],
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
   returnObj:Erp_Tablesets_PartTranListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param invoiceNum
   */  
export interface GetNewInvcDtl_input{
   ds:Erp_Tablesets_GLCostTransTableset[],
   invoiceNum:number,
}

export interface GetNewInvcDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLCostTransTableset,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
   */  
export interface GetNewLaborDtl_input{
   ds:Erp_Tablesets_GLCostTransTableset[],
   laborHedSeq:number,
}

export interface GetNewLaborDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLCostTransTableset,
}
}

   /** Required : 
      @param ds
      @param sysDate
      @param sysTime
   */  
export interface GetNewPartTran_input{
   ds:Erp_Tablesets_GLCostTransTableset[],
   sysDate:string,
   sysTime:number,
}

export interface GetNewPartTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLCostTransTableset,
}
}

   /** Required : 
      @param GLJrnDtlRowid
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  The GLJrnDtl Rowid  */  
   GLJrnDtlRowid:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_GLCostTransTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePartTran
      @param whereClauseInvcDtl
      @param whereClauseLaborDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartTran:string,
   whereClauseInvcDtl:string,
   whereClauseLaborDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLCostTransTableset[],
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
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGLCostTransTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLCostTransTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLCostTransTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLCostTransTableset,
}
}

