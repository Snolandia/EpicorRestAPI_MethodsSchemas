import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.BankBatchSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/$metadata", {
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
   Description: Get BankBatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankBatches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankBatchRow
   */  
export function get_BankBatches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankBatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/BankBatches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankBatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankBatches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankBatchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BankBatchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankBatches(requestBody:Erp_Tablesets_BankBatchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/BankBatches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the BankBatch item
   Description: Calls GetByID to retrieve the BankBatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankBatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceType Desc: SourceType   Required: True
      @param BankBatchID Desc: BankBatchID   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BankBatchRow
   */  
export function get_BankBatches_Company_SourceType_BankBatchID_BankAcctID(Company:string, SourceType:string, BankBatchID:string, BankAcctID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankBatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/BankBatches(" + Company + "," + SourceType + "," + BankBatchID + "," + BankAcctID + ")", {
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
         resolve(data as Erp_Tablesets_BankBatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankBatch for the service
   Description: Calls UpdateExt to update BankBatch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankBatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceType Desc: SourceType   Required: True
      @param BankBatchID Desc: BankBatchID   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankBatchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankBatches_Company_SourceType_BankBatchID_BankAcctID(Company:string, SourceType:string, BankBatchID:string, BankAcctID:string, requestBody:Erp_Tablesets_BankBatchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/BankBatches(" + Company + "," + SourceType + "," + BankBatchID + "," + BankAcctID + ")", {
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
   Summary: Call UpdateExt to delete BankBatch item
   Description: Call UpdateExt to delete BankBatch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankBatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceType Desc: SourceType   Required: True
      @param BankBatchID Desc: BankBatchID   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankBatches_Company_SourceType_BankBatchID_BankAcctID(Company:string, SourceType:string, BankBatchID:string, BankAcctID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/BankBatches(" + Company + "," + SourceType + "," + BankBatchID + "," + BankAcctID + ")", {
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
   Description: Get CashHeadSels items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashHeadSels
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadSelRow
   */  
export function get_CashHeadSels(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadSelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CashHeadSels", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadSelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashHeadSels
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadSelRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashHeadSelRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashHeadSels(requestBody:Erp_Tablesets_CashHeadSelRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CashHeadSels", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CashHeadSel item
   Description: Calls GetByID to retrieve the CashHeadSel item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadSel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashHeadSelRow
   */  
export function get_CashHeadSels_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadSelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CashHeadSels(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_CashHeadSelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashHeadSel for the service
   Description: Calls UpdateExt to update CashHeadSel. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashHeadSel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadSelRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashHeadSels_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:Erp_Tablesets_CashHeadSelRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CashHeadSels(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete CashHeadSel item
   Description: Call UpdateExt to delete CashHeadSel item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashHeadSel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashHeadSels_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CashHeadSels(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Description: Get CheckHedSels items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckHedSels
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedSelRow
   */  
export function get_CheckHedSels(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedSelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CheckHedSels", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedSelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckHedSels
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedSelRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CheckHedSelRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckHedSels(requestBody:Erp_Tablesets_CheckHedSelRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CheckHedSels", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CheckHedSel item
   Description: Calls GetByID to retrieve the CheckHedSel item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedSel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedSelRow
   */  
export function get_CheckHedSels_Company_HeadNum(Company:string, HeadNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedSelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CheckHedSels(" + Company + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedSelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CheckHedSel for the service
   Description: Calls UpdateExt to update CheckHedSel. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckHedSel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedSelRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CheckHedSels_Company_HeadNum(Company:string, HeadNum:string, requestBody:Erp_Tablesets_CheckHedSelRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CheckHedSels(" + Company + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete CheckHedSel item
   Description: Call UpdateExt to delete CheckHedSel item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckHedSel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CheckHedSels_Company_HeadNum(Company:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CheckHedSels(" + Company + "," + HeadNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankBatchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankBatchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankBatchListRow)
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
export function get_GetRows(whereClauseBankBatch:string, whereClauseCashHeadSel:string, whereClauseCheckHedSel:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseBankBatch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankBatch=" + whereClauseBankBatch
   }
   if(typeof whereClauseCashHeadSel!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashHeadSel=" + whereClauseCashHeadSel
   }
   if(typeof whereClauseCheckHedSel!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCheckHedSel=" + whereClauseCheckHedSel
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sourceType:string, bankBatchID:string, bankAcctID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sourceType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sourceType=" + sourceType
   }
   if(typeof bankBatchID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bankBatchID=" + bankBatchID
   }
   if(typeof bankAcctID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bankAcctID=" + bankAcctID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetList" + params, {
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
   Summary: Invoke method GetNextBankBatchID
   Description: Get next Bank Batch ID
   OperationID: GetNextBankBatchID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextBankBatchID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextBankBatchID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNextBankBatchID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetNextBankBatchID", {
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
         resolve(data as GetNextBankBatchID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ModifyBankBatch
   Description: Create new bank Batch/ get existing batch
   OperationID: ModifyBankBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ModifyBankBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyBankBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifyBankBatch(requestBody:ModifyBankBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ModifyBankBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/ModifyBankBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ModifyBankBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankBatch
   Description: Create new bank Batch/ get existing batch
   OperationID: GetBankBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBankBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankBatch(requestBody:GetBankBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBankBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetBankBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBankBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExpandBatch
   Description: Expand bank Batch.
   OperationID: ExpandBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExpandBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpandBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpandBatch(requestBody:ExpandBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExpandBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/ExpandBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExpandBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CollapseBatch
   Description: Collapse bank Batch, if possible.
   OperationID: CollapseBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CollapseBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollapseBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CollapseBatch(requestBody:CollapseBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CollapseBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/CollapseBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CollapseBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnBatchCheckHed
   Description: Unbatch AP Payment from batch.
   OperationID: UnBatchCheckHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnBatchCheckHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnBatchCheckHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnBatchCheckHed(requestBody:UnBatchCheckHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnBatchCheckHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/UnBatchCheckHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnBatchCheckHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnBatchCashHead
   Description: Unbatch AR Receipt from batch.
   OperationID: UnBatchCashHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnBatchCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnBatchCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnBatchCashHead(requestBody:UnBatchCashHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnBatchCashHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/UnBatchCashHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnBatchCashHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReBatchCheckHed
   Description: Rebatch AP Payment to batch.
   OperationID: ReBatchCheckHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReBatchCheckHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReBatchCheckHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReBatchCheckHed(requestBody:ReBatchCheckHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReBatchCheckHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/ReBatchCheckHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReBatchCheckHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReBatchCashHead
   Description: Rebatch AR Receipt to batch.
   OperationID: ReBatchCashHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReBatchCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReBatchCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReBatchCashHead(requestBody:ReBatchCashHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReBatchCashHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/ReBatchCashHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReBatchCashHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReBatchBankBatch
   Description: Rebatch Bank Batch.
   OperationID: ReBatchBankBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReBatchBankBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReBatchBankBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReBatchBankBatch(requestBody:ReBatchBankBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReBatchBankBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/ReBatchBankBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReBatchBankBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBatchStatus
   Description: Returns BankBatch status.
   OperationID: GetBatchStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBatchStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBatchStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBatchStatus(requestBody:GetBatchStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBatchStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetBatchStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBatchStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReCalcBatchAmountInCurrency
   Description: Recalculate Batch BankAmount in given currency.
   OperationID: ReCalcBatchAmountInCurrency
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReCalcBatchAmountInCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReCalcBatchAmountInCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReCalcBatchAmountInCurrency(requestBody:ReCalcBatchAmountInCurrency_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReCalcBatchAmountInCurrency_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/ReCalcBatchAmountInCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReCalcBatchAmountInCurrency_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankBatchType
   Description: Returns integer representing Batch tyep:
0 - for AP batches
1 - for AR batches
-1 - error
   OperationID: GetBankBatchType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBankBatchType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankBatchType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankBatchType(requestBody:GetBankBatchType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBankBatchType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetBankBatchType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBankBatchType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankAcctID
   Description: Call this method when the user changes the Bank Account.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/OnChangeBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method SelectPayments
   OperationID: SelectPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectPayments(requestBody:SelectPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/SelectPayments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPayments
   OperationID: GetPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPayments(requestBody:GetPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetPayments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddPaymentsToBatch
   OperationID: AddPaymentsToBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddPaymentsToBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPaymentsToBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddPaymentsToBatch(requestBody:AddPaymentsToBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddPaymentsToBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/AddPaymentsToBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddPaymentsToBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemovePaymentsFromBatch
   OperationID: RemovePaymentsFromBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemovePaymentsFromBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePaymentsFromBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemovePaymentsFromBatch(requestBody:RemovePaymentsFromBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemovePaymentsFromBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/RemovePaymentsFromBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RemovePaymentsFromBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MovePaymentsToAnotherBatch
   OperationID: MovePaymentsToAnotherBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MovePaymentsToAnotherBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MovePaymentsToAnotherBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MovePaymentsToAnotherBatch(requestBody:MovePaymentsToAnotherBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MovePaymentsToAnotherBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/MovePaymentsToAnotherBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MovePaymentsToAnotherBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectReceipts
   OperationID: SelectReceipts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectReceipts(requestBody:SelectReceipts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectReceipts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/SelectReceipts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SelectReceipts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReceipts
   OperationID: GetReceipts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReceipts(requestBody:GetReceipts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReceipts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetReceipts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetReceipts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddReceiptsToBatch
   OperationID: AddReceiptsToBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddReceiptsToBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddReceiptsToBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddReceiptsToBatch(requestBody:AddReceiptsToBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddReceiptsToBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/AddReceiptsToBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddReceiptsToBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveReceiptsFromBatch
   OperationID: RemoveReceiptsFromBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveReceiptsFromBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveReceiptsFromBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveReceiptsFromBatch(requestBody:RemoveReceiptsFromBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveReceiptsFromBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/RemoveReceiptsFromBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RemoveReceiptsFromBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveReceiptsToAnotherBatch
   OperationID: MoveReceiptsToAnotherBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveReceiptsToAnotherBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveReceiptsToAnotherBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveReceiptsToAnotherBatch(requestBody:MoveReceiptsToAnotherBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveReceiptsToAnotherBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/MoveReceiptsToAnotherBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MoveReceiptsToAnotherBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockAPBatch
   OperationID: LockAPBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockAPBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockAPBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockAPBatch(requestBody:LockAPBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockAPBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/LockAPBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LockAPBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockARBatch
   OperationID: LockARBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockARBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockARBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockARBatch(requestBody:LockARBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockARBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/LockARBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LockARBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockBatch
   OperationID: LockBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockBatch(requestBody:LockBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/LockBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LockBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnLockBatch
   OperationID: UnLockBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnLockBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLockBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnLockBatch(requestBody:UnLockBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnLockBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/UnLockBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnLockBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBankBatch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankBatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBankBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankBatch(requestBody:GetNewBankBatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBankBatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetNewBankBatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewBankBatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHeadSel
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHeadSel
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashHeadSel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHeadSel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHeadSel(requestBody:GetNewCashHeadSel_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashHeadSel_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetNewCashHeadSel", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCashHeadSel_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCheckHedSel
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckHedSel
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCheckHedSel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHedSel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCheckHedSel(requestBody:GetNewCheckHedSel_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCheckHedSel_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetNewCheckHedSel", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCheckHedSel_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankBatchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankBatchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankBatchListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankBatchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankBatchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadSelRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadSelRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedSelRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedSelRow,
}

export interface Erp_Tablesets_BankBatchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Source Type  */  
   "SourceType":number,
      /**  Displays the ID of the batch.  */  
   "BankBatchID":string,
      /**  Displays the bank account where the data is reconciled.  */  
   "BankAcctID":string,
      /**  Created By  */  
   "CreatedBy":string,
      /**  Displays the total amount of the batch.  */  
   "BankAmount":number,
      /**  Displays the bank currency.  */  
   "BankCurrency":string,
      /**  Displays the date of the batch.  */  
   "BatchDate":string,
      /**  Reconciled  */  
   "Reconciled":boolean,
      /**  Displays the batch status.  */  
   "BatchStatus":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankBatchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Source Type  */  
   "SourceType":number,
      /**  Displays the ID of the batch.  */  
   "BankBatchID":string,
      /**  Displays the bank account where the data is reconciled.  */  
   "BankAcctID":string,
      /**  Created By  */  
   "CreatedBy":string,
      /**  Displays the total amount of the batch.  */  
   "BankAmount":number,
      /**  Displays the bank currency.  */  
   "BankCurrency":string,
      /**  Displays the date of the batch.  */  
   "BatchDate":string,
      /**  Reconciled  */  
   "Reconciled":boolean,
      /**  Displays the batch status.  */  
   "BatchStatus":number,
      /**  Reconcile Pending  */  
   "ReconcilePending":boolean,
      /**  Displays the date of reconciliation.  */  
   "ReconciledDate":string,
      /**  Reconciled Time  */  
   "ReconciledTime":string,
      /**  Reconciled Person  */  
   "ReconciledPerson":string,
      /**  Cash Book Number.  */  
   "CashBookNum":number,
      /**  Cash Book Line Number.  */  
   "CashBookLine":number,
      /**  Reconciled Bank Amt  */  
   "ReconciledBankAmt":number,
      /**  Displays the number of the statement to which this batch is matched.  */  
   "BankSlip":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Active User ID  */  
   "ActiveUserID":string,
      /**  Indicates whether Batch was generated by Electronic Interface or not.  */  
   "EIGenerated":boolean,
      /**  Represents user friendly status of Batch.  */  
   "BatchStatusDsp":number,
   "DspBankBatchID":string,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadSelRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   "GroupID":string,
      /**  Displays the receipt header number used for internal reference.  */  
   "HeadNum":number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Displays the transaction type.  */  
   "TranType":string,
      /**  Displays the number of the check.  */  
   "CheckRef":string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   "OrderNum":number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   "InvoiceNum":number,
      /**  Displays the transaction amount.  */  
   "TranAmt":number,
      /**  Displays the transaction amount in customer currency.  */  
   "DocTranAmt":number,
      /**  Displays the customer ID.  */  
   "CustID":string,
      /**  Displays the date of the transaction.  */  
   "TranDate":string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**  Displays the unapplied amount.  */  
   "UnAppliedAmt":number,
      /**  Displays the unapplied amount in base currency.  */  
   "DocUnAppliedAmt":number,
      /**  Displays the amount applied to invoices.  */  
   "AppliedAmt":number,
      /**  Displays the amount in document currency applied to invoices.  */  
   "DocAppliedAmt":number,
      /**  Displays the fiscal year that the check is posted to.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period that the check is posted to.  */  
   "FiscalPeriod":number,
      /**  Displays any reference.  */  
   "Reference":string,
      /**  Indicates if this transaction has been posted.  */  
   "GLPosted":boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   "CreditMemoNum":number,
      /**  Displays the customer currency.  */  
   "CurrencyCode":string,
      /**  Displays the exchange rate that is used for this check.  */  
   "ExchangeRate":number,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Displays the tax amount.  */  
   "DocTaxAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Displays the legal number of the check.  */  
   "LegalNumber":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   "DebNoteOnly":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnAppliedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
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
      /**  The unique code of Receipt Currency.  */  
   "ReceiptCurrencyCode":string,
      /**  Amount of Receipt in Receipt Currency.  */  
   "ReceiptAmt":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   "BankRcptExchangeRate":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   "SettlementExchangeRate":number,
      /**  The unique Currency code for Credit Memo.  */  
   "CMCurrencyCode":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "CMAmount":number,
      /**  Reference to cash receipt which had been reversed.  */  
   "ReverseRef":number,
      /**  Date when cash receipt had been reversed  */  
   "ReverseDate":string,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Withhold Tax  */  
   "TaxWhld":number,
      /**  Dsicount Date  */  
   "DiscountDate":string,
      /**  Calculate Withhold Tax  */  
   "TaxWhldCalc":number,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   "UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   "DocUnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   "Rpt1UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   "Rpt2UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   "Rpt3UnallocatedAmt":number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   "ApplyHeadNum":number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   "AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   "DocAllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   "Rpt1AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   "Rpt2AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   "Rpt3AllocatedAmt":number,
      /**  Comments related to the cash receipt.  */  
   "Comment":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
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
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  MandateReference  */  
   "MandateReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SEPADDExportDate  */  
   "SEPADDExportDate":string,
      /**  BOE Invoice Number  */  
   "BOEInvoiceNum":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  DocumentType  */  
   "DocumentType":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  BankRcptExchangeRate10D  */  
   "BankRcptExchangeRate10D":number,
      /**  SettlementExchangeRate10D  */  
   "SettlementExchangeRate10D":number,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
   "BankSlip":number,
   "ReverseFlag":boolean,
   "Selected":boolean,
   "BankBatchIDDsp":string,
   "BankBatchSourceTypeExt":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CheckHedSelRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   "Posted":boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   "CheckSrc":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  employee # for payroll checks  */  
   "EmployeeNum":string,
      /**  Check Amount. Base Currency.  */  
   "CheckAmt":number,
      /**  Check Amount. Document Currency.  */  
   "DocCheckAmt":number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   "ManualPrint":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Vendors name.  */  
   "Name":string,
      /**  First Address line  */  
   "Address1":string,
      /**  Second Address Line  */  
   "Address2":string,
      /**  Third Address Line  */  
   "Address3":string,
      /**  City portion of address  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Zip code or Postal code portion of address  */  
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's bank.  */  
   "VendorBankID":string,
      /**  Supplier Bank Name  */  
   "VendorBankName":string,
      /**  Name on the Bank Account.  */  
   "VendorBankNameOnAccount":string,
      /**  First address line of supplier bank.  */  
   "VendorBankAddress1":string,
      /**  Second address line of supplier bank.  */  
   "VendorBankAddress2":string,
      /**  Third address line of supplier bank.  */  
   "VendorBankAddress3":string,
      /**  City portion of address of supplier bank.  */  
   "VendorBankCity":string,
      /**  Can be blank.  */  
   "VendorBankState":string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   "VendorBankPostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "VendorBankCountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "VendorBankAcctNumber":string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   "VendorBankSwiftNum":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefCheckNum":string,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  Total amount in Bank currency  */  
   "BankTotalAmt":number,
      /**  Total entered flag  */  
   "IsEnterTotal":boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   "LockRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   "UsePendAcct":boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Reference to first checkhed  */  
   "FirstHeadNum":number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   "ApplyingPayment":boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   "InvoiceNum":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  VendorBankIBANCode  */  
   "VendorBankIBANCode":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  NOPaymentStatus  */  
   "NOPaymentStatus":number,
      /**  NOPaymentDirection  */  
   "NOPaymentDirection":string,
      /**  NOPaymentType  */  
   "NOPaymentType":string,
      /**  Norway CSF: The name of created payment file.  */  
   "NOTransferFileName":string,
      /**  Norway CSF: Transaction Reference Number assigned by bank.  */  
   "NOBankTransRef":string,
      /**  BalanceUpdate  */  
   "BalanceUpdate":number,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  BankRecGainLoss  */  
   "BankRecGainLoss":number,
      /**  Bill of Exchange Invoice num this was generated from  */  
   "BOEInvoiceNum":string,
      /**  DocBankRecGainLoss  */  
   "DocBankRecGainLoss":number,
      /**  MsgId  */  
   "MsgId":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  PayLegalNumber  */  
   "PayLegalNumber":string,
      /**  PayTranDocTypeID  */  
   "PayTranDocTypeID":string,
      /**  Rpt1BankRecGainLoss  */  
   "Rpt1BankRecGainLoss":number,
      /**  Rpt2BankRecGainLoss  */  
   "Rpt2BankRecGainLoss":number,
      /**  Rpt3BankRecGainLoss  */  
   "Rpt3BankRecGainLoss":number,
      /**  TaxPaymInfo  */  
   "TaxPaymInfo":string,
      /**  VoidLegalNumber  */  
   "VoidLegalNumber":string,
      /**  VoidTranDocTypeID  */  
   "VoidTranDocTypeID":string,
      /**  SEGrpNum  */  
   "SEGrpNum":number,
      /**  SEReference  */  
   "SEReference":string,
      /**  SEISGroupedPO3  */  
   "SEISGroupedPO3":boolean,
      /**  SEISExported  */  
   "SEISExported":boolean,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  MXBankAcctNumber  */  
   "MXBankAcctNumber":string,
      /**  MXBankIdentifier  */  
   "MXBankIdentifier":string,
      /**  MXRFC  */  
   "MXRFC":string,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
   "Selected":boolean,
   "BankBatchIDDsp":string,
   "BankBatchSourceTypeExt":number,
      /**  Bank Account currency code.  */  
   "BankCurrencyCode":string,
   "BitFlag":number,
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
      @param bankAcctID
      @param bankBatchSysRowID
      @param ds
   */  
export interface AddPaymentsToBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
   ds:Erp_Tablesets_CheckHedSelTableset[],
}

export interface AddPaymentsToBatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CheckHedSelTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
      @param ds
   */  
export interface AddReceiptsToBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
   ds:Erp_Tablesets_CashHeadSelTableset[],
}

export interface AddReceiptsToBatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashHeadSelTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
   */  
export interface CollapseBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
}

export interface CollapseBatch_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param sourceType
      @param bankBatchID
      @param bankAcctID
   */  
export interface DeleteByID_input{
   sourceType:number,
   bankBatchID:string,
   bankAcctID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_BankBatchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Source Type  */  
   SourceType:number,
      /**  Displays the ID of the batch.  */  
   BankBatchID:string,
      /**  Displays the bank account where the data is reconciled.  */  
   BankAcctID:string,
      /**  Created By  */  
   CreatedBy:string,
      /**  Displays the total amount of the batch.  */  
   BankAmount:number,
      /**  Displays the bank currency.  */  
   BankCurrency:string,
      /**  Displays the date of the batch.  */  
   BatchDate:string,
      /**  Reconciled  */  
   Reconciled:boolean,
      /**  Displays the batch status.  */  
   BatchStatus:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankBatchListTableset{
   BankBatchList:Erp_Tablesets_BankBatchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankBatchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Source Type  */  
   SourceType:number,
      /**  Displays the ID of the batch.  */  
   BankBatchID:string,
      /**  Displays the bank account where the data is reconciled.  */  
   BankAcctID:string,
      /**  Created By  */  
   CreatedBy:string,
      /**  Displays the total amount of the batch.  */  
   BankAmount:number,
      /**  Displays the bank currency.  */  
   BankCurrency:string,
      /**  Displays the date of the batch.  */  
   BatchDate:string,
      /**  Reconciled  */  
   Reconciled:boolean,
      /**  Displays the batch status.  */  
   BatchStatus:number,
      /**  Reconcile Pending  */  
   ReconcilePending:boolean,
      /**  Displays the date of reconciliation.  */  
   ReconciledDate:string,
      /**  Reconciled Time  */  
   ReconciledTime:string,
      /**  Reconciled Person  */  
   ReconciledPerson:string,
      /**  Cash Book Number.  */  
   CashBookNum:number,
      /**  Cash Book Line Number.  */  
   CashBookLine:number,
      /**  Reconciled Bank Amt  */  
   ReconciledBankAmt:number,
      /**  Displays the number of the statement to which this batch is matched.  */  
   BankSlip:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Active User ID  */  
   ActiveUserID:string,
      /**  Indicates whether Batch was generated by Electronic Interface or not.  */  
   EIGenerated:boolean,
      /**  Represents user friendly status of Batch.  */  
   BatchStatusDsp:number,
   DspBankBatchID:string,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankBatchTableset{
   BankBatch:Erp_Tablesets_BankBatchRow[],
   CashHeadSel:Erp_Tablesets_CashHeadSelRow[],
   CheckHedSel:Erp_Tablesets_CheckHedSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashHeadSelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
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
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
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
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
   BankSlip:number,
   ReverseFlag:boolean,
   Selected:boolean,
   BankBatchIDDsp:string,
   BankBatchSourceTypeExt:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadSelTableset{
   CashHeadSel:Erp_Tablesets_CashHeadSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CheckHedSelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   Posted:boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   CheckSrc:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  employee # for payroll checks  */  
   EmployeeNum:string,
      /**  Check Amount. Base Currency.  */  
   CheckAmt:number,
      /**  Check Amount. Document Currency.  */  
   DocCheckAmt:number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   ManualPrint:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Vendors name.  */  
   Name:string,
      /**  First Address line  */  
   Address1:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  Third Address Line  */  
   Address3:string,
      /**  City portion of address  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Zip code or Postal code portion of address  */  
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's bank.  */  
   VendorBankID:string,
      /**  Supplier Bank Name  */  
   VendorBankName:string,
      /**  Name on the Bank Account.  */  
   VendorBankNameOnAccount:string,
      /**  First address line of supplier bank.  */  
   VendorBankAddress1:string,
      /**  Second address line of supplier bank.  */  
   VendorBankAddress2:string,
      /**  Third address line of supplier bank.  */  
   VendorBankAddress3:string,
      /**  City portion of address of supplier bank.  */  
   VendorBankCity:string,
      /**  Can be blank.  */  
   VendorBankState:string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   VendorBankPostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   VendorBankCountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   VendorBankAcctNumber:string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   VendorBankSwiftNum:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefCheckNum:string,
      /**  Reporting currency value of this field  */  
   Rpt1CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  Total amount in Bank currency  */  
   BankTotalAmt:number,
      /**  Total entered flag  */  
   IsEnterTotal:boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   LockRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   UsePendAcct:boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Reference to first checkhed  */  
   FirstHeadNum:number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   ApplyingPayment:boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   InvoiceNum:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  VendorBankIBANCode  */  
   VendorBankIBANCode:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  NOPaymentStatus  */  
   NOPaymentStatus:number,
      /**  NOPaymentDirection  */  
   NOPaymentDirection:string,
      /**  NOPaymentType  */  
   NOPaymentType:string,
      /**  Norway CSF: The name of created payment file.  */  
   NOTransferFileName:string,
      /**  Norway CSF: Transaction Reference Number assigned by bank.  */  
   NOBankTransRef:string,
      /**  BalanceUpdate  */  
   BalanceUpdate:number,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  BankRecGainLoss  */  
   BankRecGainLoss:number,
      /**  Bill of Exchange Invoice num this was generated from  */  
   BOEInvoiceNum:string,
      /**  DocBankRecGainLoss  */  
   DocBankRecGainLoss:number,
      /**  MsgId  */  
   MsgId:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  PayLegalNumber  */  
   PayLegalNumber:string,
      /**  PayTranDocTypeID  */  
   PayTranDocTypeID:string,
      /**  Rpt1BankRecGainLoss  */  
   Rpt1BankRecGainLoss:number,
      /**  Rpt2BankRecGainLoss  */  
   Rpt2BankRecGainLoss:number,
      /**  Rpt3BankRecGainLoss  */  
   Rpt3BankRecGainLoss:number,
      /**  TaxPaymInfo  */  
   TaxPaymInfo:string,
      /**  VoidLegalNumber  */  
   VoidLegalNumber:string,
      /**  VoidTranDocTypeID  */  
   VoidTranDocTypeID:string,
      /**  SEGrpNum  */  
   SEGrpNum:number,
      /**  SEReference  */  
   SEReference:string,
      /**  SEISGroupedPO3  */  
   SEISGroupedPO3:boolean,
      /**  SEISExported  */  
   SEISExported:boolean,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  MXBankAcctNumber  */  
   MXBankAcctNumber:string,
      /**  MXBankIdentifier  */  
   MXBankIdentifier:string,
      /**  MXRFC  */  
   MXRFC:string,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
   Selected:boolean,
   BankBatchIDDsp:string,
   BankBatchSourceTypeExt:number,
      /**  Bank Account currency code.  */  
   BankCurrencyCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CheckHedSelTableset{
   CheckHedSel:Erp_Tablesets_CheckHedSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtBankBatchTableset{
   BankBatch:Erp_Tablesets_BankBatchRow[],
   CashHeadSel:Erp_Tablesets_CashHeadSelRow[],
   CheckHedSel:Erp_Tablesets_CheckHedSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
   */  
export interface ExpandBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
}

export interface ExpandBatch_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
   */  
export interface GetBankBatchType_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
}

export interface GetBankBatchType_output{
   returnObj:number,
}

   /** Required : 
      @param bankAcctID
      @param payMethodID
      @param bankBatchID
      @param oldBankBatchSysRowID
      @param sourceType
      @param createdBy
      @param batchDate
      @param mode
      @param batchHolder
   */  
export interface GetBankBatch_input{
      /**  Bank Account  */  
   bankAcctID:string,
      /**  Payment Method  */  
   payMethodID:number,
      /**  Batch ID  */  
   bankBatchID:string,
      /**  Old Batch ID  */  
   oldBankBatchSysRowID:string,
      /**  Source Type  */  
   sourceType:number,
      /**  User ID  */  
   createdBy:string,
      /**  Batch Date  */  
   batchDate:string,
      /**  Batch Mode  */  
   mode:number,
      /**  Batch holder  */  
   batchHolder:string,
}

export interface GetBankBatch_output{
parameters : {
      /**  output parameters  */  
   bankBatchSysRowID:string,
   message:string,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
   */  
export interface GetBatchStatus_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
}

export interface GetBatchStatus_output{
   returnObj:number,
}

   /** Required : 
      @param sourceType
      @param bankBatchID
      @param bankAcctID
   */  
export interface GetByID_input{
   sourceType:number,
   bankBatchID:string,
   bankAcctID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_BankBatchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_BankBatchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_BankBatchTableset[],
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
   returnObj:Erp_Tablesets_BankBatchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param sourceType
      @param bankBatchID
   */  
export interface GetNewBankBatch_input{
   ds:Erp_Tablesets_BankBatchTableset[],
   sourceType:number,
   bankBatchID:string,
}

export interface GetNewBankBatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewCashHeadSel_input{
   ds:Erp_Tablesets_BankBatchTableset[],
   groupID:string,
}

export interface GetNewCashHeadSel_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCheckHedSel_input{
   ds:Erp_Tablesets_BankBatchTableset[],
}

export interface GetNewCheckHedSel_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

export interface GetNextBankBatchID_output{
parameters : {
      /**  output parameters  */  
   opBankBatchID:string,
}
}

   /** Required : 
      @param bankAcctID
      @param fromDate
      @param toDate
      @param checkNumStartsWith
      @param vendNumList
      @param pageSize
   */  
export interface GetPayments_input{
   bankAcctID:string,
   fromDate:string,
   toDate:string,
   checkNumStartsWith:string,
   vendNumList:string,
   pageSize:number,
}

export interface GetPayments_output{
   returnObj:Erp_Tablesets_CheckHedSelTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param bankAcctID
      @param fromDate
      @param toDate
      @param checkRefStartsWith
      @param custNumList
      @param pageSize
   */  
export interface GetReceipts_input{
   bankAcctID:string,
   fromDate:string,
   toDate:string,
   checkRefStartsWith:string,
   custNumList:string,
   pageSize:number,
}

export interface GetReceipts_output{
   returnObj:Erp_Tablesets_CashHeadSelTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseBankBatch
      @param whereClauseCashHeadSel
      @param whereClauseCheckHedSel
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseBankBatch:string,
   whereClauseCashHeadSel:string,
   whereClauseCheckHedSel:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_BankBatchTableset[],
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
      @param groupID
      @param programName
   */  
export interface LockAPBatch_input{
   groupID:string,
   programName:string,
}

export interface LockAPBatch_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

   /** Required : 
      @param groupID
      @param programName
   */  
export interface LockARBatch_input{
   groupID:string,
   programName:string,
}

export interface LockARBatch_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
      @param programName
   */  
export interface LockBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
   programName:string,
}

export interface LockBatch_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

   /** Required : 
      @param bankAcctID
      @param payMethodID
      @param bankBatchSysRowID
      @param groupID
      @param mode
      @param newGroupBankBatchSysRowID
   */  
export interface ModifyBankBatch_input{
      /**  Bank Account  */  
   bankAcctID:string,
      /**  Payment Method  */  
   payMethodID:number,
      /**  Batch ID  */  
   bankBatchSysRowID:string,
      /**  Group ID  */  
   groupID:string,
      /**  Mode  */  
   mode:number,
      /**  New Group Batch ID  */  
   newGroupBankBatchSysRowID:string,
}

export interface ModifyBankBatch_output{
}

   /** Required : 
      @param bankAcctID
      @param oldBankBatchSysRowID
      @param newBankBatchSysRowID
      @param ds
      @param programName
   */  
export interface MovePaymentsToAnotherBatch_input{
   bankAcctID:string,
   oldBankBatchSysRowID:string,
   newBankBatchSysRowID:string,
   ds:Erp_Tablesets_BankBatchTableset[],
   programName:string,
}

export interface MovePaymentsToAnotherBatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param oldBankBatchSysRowID
      @param newBankBatchSysRowID
      @param ds
      @param ipProgramName
   */  
export interface MoveReceiptsToAnotherBatch_input{
   bankAcctID:string,
   oldBankBatchSysRowID:string,
   newBankBatchSysRowID:string,
   ds:Erp_Tablesets_BankBatchTableset[],
   ipProgramName:string,
}

export interface MoveReceiptsToAnotherBatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param ds
   */  
export interface OnChangeBankAcctID_input{
      /**  Bank Account ID  */  
   bankAcctID:string,
   ds:Erp_Tablesets_BankBatchTableset[],
}

export interface OnChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
   */  
export interface ReBatchBankBatch_input{
      /**  Bank Account ID  */  
   bankAcctID:string,
      /**  Bank Batch ID  */  
   bankBatchSysRowID:string,
}

export interface ReBatchBankBatch_output{
      /**  Success True/False  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param bankAcctID
      @param headNum
   */  
export interface ReBatchCashHead_input{
   bankAcctID:string,
   headNum:number,
}

export interface ReBatchCashHead_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param bankAcctID
      @param headNum
   */  
export interface ReBatchCheckHed_input{
      /**  Bank Account ID  */  
   bankAcctID:string,
      /**  Head Num  */  
   headNum:number,
}

export interface ReBatchCheckHed_output{
      /**  Success True/False  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param toCurrency
      @param rateGrpCode
      @param exchangeDate
      @param bankAcctID
      @param bankBatchSysRowID
   */  
export interface ReCalcBatchAmountInCurrency_input{
      /**  Target currency  */  
   toCurrency:string,
      /**  Rate Group Code  */  
   rateGrpCode:string,
      /**  Exchange Date  */  
   exchangeDate:string,
      /**  Bank Account ID  */  
   bankAcctID:string,
   bankBatchSysRowID:string,
}

export interface ReCalcBatchAmountInCurrency_output{
      /**  Success True/False  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   amount:number,
   message:string,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
      @param ds
   */  
export interface RemovePaymentsFromBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
   ds:Erp_Tablesets_BankBatchTableset[],
}

export interface RemovePaymentsFromBatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
      @param ds
   */  
export interface RemoveReceiptsFromBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
   ds:Erp_Tablesets_BankBatchTableset[],
}

export interface RemoveReceiptsFromBatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

   /** Required : 
      @param ipBankAcctID
   */  
export interface SelectPayments_input{
   ipBankAcctID:string,
}

export interface SelectPayments_output{
   returnObj:Erp_Tablesets_CheckHedSelTableset[],
}

   /** Required : 
      @param ipBankAcctID
   */  
export interface SelectReceipts_input{
   ipBankAcctID:string,
}

export interface SelectReceipts_output{
   returnObj:Erp_Tablesets_CashHeadSelTableset[],
}

   /** Required : 
      @param bankAcctID
      @param headNum
   */  
export interface UnBatchCashHead_input{
   bankAcctID:string,
   headNum:number,
}

export interface UnBatchCashHead_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param bankAcctID
      @param headNum
   */  
export interface UnBatchCheckHed_input{
      /**  Bank Account ID  */  
   bankAcctID:string,
      /**  Head Num  */  
   headNum:number,
}

export interface UnBatchCheckHed_output{
      /**  Success True/False  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param bankAcctID
      @param bankBatchSysRowID
      @param programName
   */  
export interface UnLockBatch_input{
   bankAcctID:string,
   bankBatchSysRowID:string,
   programName:string,
}

export interface UnLockBatch_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtBankBatchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtBankBatchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_BankBatchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankBatchTableset,
}
}

