import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.TransferChgSugSvc
// Description: The Object for Suggestions Changing for Transfer Workbench
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/$metadata", {
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
   Description: Get TransferChgSugs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransferChgSugs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TransferChgSugs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TransferChgSugs", {
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
   OperationID: NewUpdateExt_TransferChgSugs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TFOrdDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransferChgSugs(requestBody:Erp_Tablesets_TFOrdDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TransferChgSugs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TransferChgSug item
   Description: Calls GetByID to retrieve the TransferChgSug item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransferChgSug
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TransferChgSugs_Company_TFLineNum(Company:string, TFLineNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TransferChgSugs(" + Company + "," + TFLineNum + ")", {
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
   Summary: Calls UpdateExt to update TransferChgSug for the service
   Description: Calls UpdateExt to update TransferChgSug. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransferChgSug
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
export function patch_TransferChgSugs_Company_TFLineNum(Company:string, TFLineNum:string, requestBody:Erp_Tablesets_TFOrdDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TransferChgSugs(" + Company + "," + TFLineNum + ")", {
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
   Summary: Call UpdateExt to delete TransferChgSug item
   Description: Call UpdateExt to delete TransferChgSug item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransferChgSug
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TransferChgSugs_Company_TFLineNum(Company:string, TFLineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TransferChgSugs(" + Company + "," + TFLineNum + ")", {
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
   Description: Get TFOrdSugs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFOrdSugs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdSugRow
   */  
export function get_TransferChgSugs_Company_TFLineNum_TFOrdSugs(Company:string, TFLineNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdSugRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TransferChgSugs(" + Company + "," + TFLineNum + ")/TFOrdSugs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdSugRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFOrdSug item
   Description: Calls GetByID to retrieve the TFOrdSug item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdSug1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdSugRow
   */  
export function get_TransferChgSugs_Company_TFLineNum_TFOrdSugs_Company_TFLineNum(Company:string, TFLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdSugRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TransferChgSugs(" + Company + "," + TFLineNum + ")/TFOrdSugs(" + Company + "," + TFLineNum + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdSugRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TFOrdSugs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFOrdSugs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdSugRow
   */  
export function get_TFOrdSugs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdSugRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TFOrdSugs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdSugRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFOrdSugs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdSugRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TFOrdSugRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFOrdSugs(requestBody:Erp_Tablesets_TFOrdSugRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TFOrdSugs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TFOrdSug item
   Description: Calls GetByID to retrieve the TFOrdSug item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdSug
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdSugRow
   */  
export function get_TFOrdSugs_Company_TFLineNum(Company:string, TFLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdSugRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TFOrdSugs(" + Company + "," + TFLineNum + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdSugRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFOrdSug for the service
   Description: Calls UpdateExt to update TFOrdSug. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFOrdSug
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdSugRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFOrdSugs_Company_TFLineNum(Company:string, TFLineNum:string, requestBody:Erp_Tablesets_TFOrdSugRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TFOrdSugs(" + Company + "," + TFLineNum + ")", {
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
   Summary: Call UpdateExt to delete TFOrdSug item
   Description: Call UpdateExt to delete TFOrdSug item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFOrdSug
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFOrdSugs_Company_TFLineNum(Company:string, TFLineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/TFOrdSugs(" + Company + "," + TFLineNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlListRow)
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
export function get_GetRows(whereClauseTFOrdDtl:string, whereClauseTFOrdSug:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTFOrdDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdDtl=" + whereClauseTFOrdDtl
   }
   if(typeof whereClauseTFOrdSug!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdSug=" + whereClauseTFOrdSug
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetRows" + params, {
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
export function get_GetByID(tfLineNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tfLineNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tfLineNum=" + tfLineNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetList" + params, {
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
   Summary: Invoke method ChangeReqValue
   Description: This method is called when the required quantity or required UOM changes to convert quantities.
   OperationID: ChangeReqValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeReqValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReqValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeReqValue(requestBody:ChangeReqValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeReqValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/ChangeReqValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeReqValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForLandingPage
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRowsForLandingPage
      @param inTFLineList Desc: RowType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsForLandingPage(inTFLineList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof inTFLineList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inTFLineList=" + inTFLineList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForLandingPage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetRowsForLandingPage" + params, {
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
         resolve(data as GetRowsForLandingPage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ProcessChgSuggestions
   Description: This method updates existing transfer lines with the suggested changes from MRP.
Suggested where statement for Search clause:
(TFOrdDtl where) TFOrdDtl.Plant = ipPlant and TFOrdDtl.ToPlant = cur-plant
and TFOrdDtl.Shipped = no
and TFOrdDTl.NeedByDate less or = horizonDate
   OperationID: ProcessChgSuggestions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessChgSuggestions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessChgSuggestions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessChgSuggestions(requestBody:ProcessChgSuggestions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessChgSuggestions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/ProcessChgSuggestions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ProcessChgSuggestions_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetNewTFOrdDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewTFOrdSug
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdSug
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdSug_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdSug_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFOrdSug(requestBody:GetNewTFOrdSug_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTFOrdSug_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetNewTFOrdSug", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTFOrdSug_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferChgSugSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdSugRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdSugRow,
}

export interface Erp_Tablesets_TFOrdDtlListRow{
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
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "ToPlantDesc":string,
   "FromPlantDesc":string,
   "Selected":boolean,
   "RequiredQty":number,
   "CreateOrder":boolean,
      /**  Descriptive Text of OpenLine Field  */  
   "LineStatus":string,
   "LotNum":string,
   "DimCode":string,
   "Weight":number,
   "TotNetWeight":number,
   "BinNum":string,
   "PkgClass":string,
   "PkgCode":string,
   "Packages":number,
   "AvailSerialNumbers":boolean,
   "DimConvFactor":number,
   "DUM":string,
      /**  DimCodeDimCodeDescription  */  
   "DimCodeDimCodeDescription":string,
      /**  PkgClassDescription  */  
   "PkgClassDescription":string,
      /**  PkgCodeDescription  */  
   "PkgCodeDescription":string,
      /**  OurStockQty * DimConvFactor  */  
   "DisplayShipQty":number,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   "InvtyUOM":string,
      /**  This order inventory quantity  */  
   "ThisOrderInvtyQty":number,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartDescIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartDescSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartDescTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartDescPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartDescSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartDescTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartDescPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartDescTrackDimension":boolean,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Description.  */  
   "StageWhseCodeDescription":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
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

export interface Erp_Tablesets_TFOrdSugRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, R = Reduce Qty. This field is a 8 char. field it could contain "IP' increase and postpone.  */  
   "SuggestionCode":string,
      /**  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  */  
   "RequireDate":string,
      /**  Human formatted string that contains the original source document of this entry.  */  
   "SourceName":string,
      /**  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  */  
   "SurplusQty":number,
      /**   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  */  
   "CancelReason":string,
      /**  Comment  */  
   "Comment":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   "OrderFirm":boolean,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Date and time when this record was created.  */  
   "CreatedOn":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "CancelSug":boolean,
   "ExpediteSug":boolean,
   "IncreaseSug":boolean,
      /**  ThisOrderInvtyQty Unit of measure  */  
   "InvtyUOM":string,
   "PostponeSug":boolean,
   "ReduceSug":boolean,
   "RequiredQty":number,
      /**  Required quantity unit of measure  */  
   "RequiredUOM":string,
   "Selected":boolean,
      /**  SurplusQty UOM  */  
   "SurplusQtyUOM":string,
      /**  This field will show the value in the Required Qty field converted to the InvtyUOM  */  
   "ThisOrderInvtyQty":number,
   "BitFlag":number,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "PartNumPricePerCode":string,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumAttrClassID":string,
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
export interface ChangeReqValue_input{
   ds:Erp_Tablesets_TransferChgSugTableset[],
}

export interface ChangeReqValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferChgSugTableset,
}
}

   /** Required : 
      @param tfLineNum
   */  
export interface DeleteByID_input{
   tfLineNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TFOrdDtlListRow{
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
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   ToPlantDesc:string,
   FromPlantDesc:string,
   Selected:boolean,
   RequiredQty:number,
   CreateOrder:boolean,
      /**  Descriptive Text of OpenLine Field  */  
   LineStatus:string,
   LotNum:string,
   DimCode:string,
   Weight:number,
   TotNetWeight:number,
   BinNum:string,
   PkgClass:string,
   PkgCode:string,
   Packages:number,
   AvailSerialNumbers:boolean,
   DimConvFactor:number,
   DUM:string,
      /**  DimCodeDimCodeDescription  */  
   DimCodeDimCodeDescription:string,
      /**  PkgClassDescription  */  
   PkgClassDescription:string,
      /**  PkgCodeDescription  */  
   PkgCodeDescription:string,
      /**  OurStockQty * DimConvFactor  */  
   DisplayShipQty:number,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   InvtyUOM:string,
      /**  This order inventory quantity  */  
   ThisOrderInvtyQty:number,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartDescIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartDescSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartDescTrackLots:boolean,
      /**  Describes the Part.  */  
   PartDescPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartDescSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartDescTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartDescPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartDescTrackDimension:boolean,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Description.  */  
   StageWhseCodeDescription:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFOrdDtlListTableset{
   TFOrdDtlList:Erp_Tablesets_TFOrdDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_TFOrdSugRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, R = Reduce Qty. This field is a 8 char. field it could contain "IP' increase and postpone.  */  
   SuggestionCode:string,
      /**  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  */  
   RequireDate:string,
      /**  Human formatted string that contains the original source document of this entry.  */  
   SourceName:string,
      /**  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  */  
   SurplusQty:number,
      /**   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  */  
   CancelReason:string,
      /**  Comment  */  
   Comment:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   OrderFirm:boolean,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Date and time when this record was created.  */  
   CreatedOn:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   CancelSug:boolean,
   ExpediteSug:boolean,
   IncreaseSug:boolean,
      /**  ThisOrderInvtyQty Unit of measure  */  
   InvtyUOM:string,
   PostponeSug:boolean,
   ReduceSug:boolean,
   RequiredQty:number,
      /**  Required quantity unit of measure  */  
   RequiredUOM:string,
   Selected:boolean,
      /**  SurplusQty UOM  */  
   SurplusQtyUOM:string,
      /**  This field will show the value in the Required Qty field converted to the InvtyUOM  */  
   ThisOrderInvtyQty:number,
   BitFlag:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumAttrClassID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TransferChgSugTableset{
   TFOrdDtl:Erp_Tablesets_TFOrdDtlRow[],
   TFOrdSug:Erp_Tablesets_TFOrdSugRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTransferChgSugTableset{
   TFOrdDtl:Erp_Tablesets_TFOrdDtlRow[],
   TFOrdSug:Erp_Tablesets_TFOrdSugRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param tfLineNum
   */  
export interface GetByID_input{
   tfLineNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TransferChgSugTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TransferChgSugTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TransferChgSugTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name  */  
   tableName:string,
      /**  The field name.  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
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
   returnObj:Erp_Tablesets_TFOrdDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTFOrdDtl_input{
   ds:Erp_Tablesets_TransferChgSugTableset[],
}

export interface GetNewTFOrdDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferChgSugTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTFOrdSug_input{
   ds:Erp_Tablesets_TransferChgSugTableset[],
}

export interface GetNewTFOrdSug_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferChgSugTableset,
}
}

   /** Required : 
      @param inTFLineList
   */  
export interface GetRowsForLandingPage_input{
      /**  RowType  */  
   inTFLineList:string,
}

export interface GetRowsForLandingPage_output{
   returnObj:Erp_Tablesets_TransferChgSugTableset[],
}

   /** Required : 
      @param whereClauseTFOrdDtl
      @param whereClauseTFOrdSug
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTFOrdDtl:string,
   whereClauseTFOrdSug:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TransferChgSugTableset[],
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
   */  
export interface ProcessChgSuggestions_input{
   ds:Erp_Tablesets_TransferChgSugTableset[],
}

export interface ProcessChgSuggestions_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferChgSugTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTransferChgSugTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTransferChgSugTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TransferChgSugTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferChgSugTableset,
}
}

