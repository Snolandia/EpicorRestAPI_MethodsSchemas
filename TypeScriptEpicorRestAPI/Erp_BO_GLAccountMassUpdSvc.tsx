import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLAccountMassUpdSvc
// Description: General Ledger Accounts Massive Update Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/$metadata", {
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
   Description: Get GLAccountMassUpds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAccountMassUpds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COARow
   */  
export function get_GLAccountMassUpds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAccountMassUpds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.COARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLAccountMassUpds(requestBody:Erp_Tablesets_COARow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds", {
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
   Summary: Calls GetByID to retrieve the GLAccountMassUpd item
   Description: Calls GetByID to retrieve the GLAccountMassUpd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccountMassUpd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.COARow
   */  
export function get_GLAccountMassUpds_Company_COACode(Company:string, COACode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds(" + Company + "," + COACode + ")", {
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
         resolve(data as Erp_Tablesets_COARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLAccountMassUpd for the service
   Description: Calls UpdateExt to update GLAccountMassUpd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAccountMassUpd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLAccountMassUpds_Company_COACode(Company:string, COACode:string, requestBody:Erp_Tablesets_COARow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds(" + Company + "," + COACode + ")", {
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
   Summary: Call UpdateExt to delete GLAccountMassUpd item
   Description: Call UpdateExt to delete GLAccountMassUpd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAccountMassUpd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLAccountMassUpds_Company_COACode(Company:string, COACode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds(" + Company + "," + COACode + ")", {
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
   Description: Get SegAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegAccts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegAcctRow
   */  
export function get_SegAccts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegAccts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SegAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SegAccts(requestBody:Erp_Tablesets_SegAcctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts", {
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
   Summary: Calls GetByID to retrieve the SegAcct item
   Description: Calls GetByID to retrieve the SegAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SegAcctRow
   */  
export function get_SegAccts_Company_COACode_CurrencyCode(Company:string, COACode:string, CurrencyCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts(" + Company + "," + COACode + "," + CurrencyCode + ")", {
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
         resolve(data as Erp_Tablesets_SegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SegAcct for the service
   Description: Calls UpdateExt to update SegAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SegAccts_Company_COACode_CurrencyCode(Company:string, COACode:string, CurrencyCode:string, requestBody:Erp_Tablesets_SegAcctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts(" + Company + "," + COACode + "," + CurrencyCode + ")", {
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
   Summary: Call UpdateExt to delete SegAcct item
   Description: Call UpdateExt to delete SegAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SegAccts_Company_COACode_CurrencyCode(Company:string, COACode:string, CurrencyCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts(" + Company + "," + COACode + "," + CurrencyCode + ")", {
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
   Description: Get SegOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegOptRow
   */  
export function get_SegOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegOptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SegOptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SegOpts(requestBody:Erp_Tablesets_SegOptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts", {
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
   Summary: Calls GetByID to retrieve the SegOpt item
   Description: Calls GetByID to retrieve the SegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegOpt
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SegOptRow
   */  
export function get_SegOpts_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_SegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SegOpt for the service
   Description: Calls UpdateExt to update SegOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegOpt
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegOptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SegOpts_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_SegOptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete SegOpt item
   Description: Call UpdateExt to delete SegOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegOpt
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SegOpts_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts(" + SysRowID + ")", {
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
   Description: Get SegRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegRanges
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegRangeRow
   */  
export function get_SegRanges(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegRanges
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SegRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SegRanges(requestBody:Erp_Tablesets_SegRangeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges", {
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
   Summary: Calls GetByID to retrieve the SegRange item
   Description: Calls GetByID to retrieve the SegRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegRange
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SegRangeRow
   */  
export function get_SegRanges_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SegRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_SegRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SegRange for the service
   Description: Calls UpdateExt to update SegRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegRange
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SegRanges_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_SegRangeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete SegRange item
   Description: Call UpdateExt to delete SegRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegRange
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SegRanges_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges(" + SysRowID + ")", {
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
   Description: Get SegRes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegRes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegResRow
   */  
export function get_SegRes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegResRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegResRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegRes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegResRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SegResRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SegRes(requestBody:Erp_Tablesets_SegResRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes", {
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
   Summary: Calls GetByID to retrieve the SegRe item
   Description: Calls GetByID to retrieve the SegRe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegRe
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SegResRow
   */  
export function get_SegRes_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SegResRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_SegResRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SegRe for the service
   Description: Calls UpdateExt to update SegRe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegRe
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegResRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SegRes_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_SegResRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete SegRe item
   Description: Call UpdateExt to delete SegRe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegRe
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SegRes_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCOA:string, whereClauseSegAcct:string, whereClauseSegOpt:string, whereClauseSegRange:string, whereClauseSegRes:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCOA!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOA=" + whereClauseCOA
   }
   if(typeof whereClauseSegAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSegAcct=" + whereClauseSegAcct
   }
   if(typeof whereClauseSegOpt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSegOpt=" + whereClauseSegOpt
   }
   if(typeof whereClauseSegRange!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSegRange=" + whereClauseSegRange
   }
   if(typeof whereClauseSegRes!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSegRes=" + whereClauseSegRes
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetRows" + params, {
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
export function get_GetByID(coACode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof coACode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "coACode=" + coACode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetList" + params, {
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
   Summary: Invoke method ChangeCurrencyAccount
   Description: Change currency account and load currencies data according selection.
   OperationID: ChangeCurrencyAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyAccount(requestBody:ChangeCurrencyAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCurrencyAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/ChangeCurrencyAccount", {
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
         resolve(data as ChangeCurrencyAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteCurrencyAccount
   Description: Delete currency account.
   OperationID: DeleteCurrencyAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCurrencyAccount(requestBody:DeleteCurrencyAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteCurrencyAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/DeleteCurrencyAccount", {
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
         resolve(data as DeleteCurrencyAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeAllowed
   Description: Change Currency Allowed
   OperationID: ChangeAllowed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAllowed(requestBody:ChangeAllowed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAllowed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/ChangeAllowed", {
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
         resolve(data as ChangeAllowed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRevalue
   Description: Change Revalue Option
   OperationID: ChangeRevalue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRevalue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevalue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevalue(requestBody:ChangeRevalue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRevalue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/ChangeRevalue", {
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
         resolve(data as ChangeRevalue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSegRange
   Description: Add a row to datatable SegRange
   OperationID: GetNewSegRange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSegRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSegRange(requestBody:GetNewSegRange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSegRange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetNewSegRange", {
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
         resolve(data as GetNewSegRange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSegOpt
   Description: Add a row to datatable SegOpt
   OperationID: GetNewSegOpt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSegOpt(requestBody:GetNewSegOpt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSegOpt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetNewSegOpt", {
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
         resolve(data as GetNewSegOpt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSegRes
   Description: Add a row to datatable SegRes
   OperationID: GetNewSegRes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSegRes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegRes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSegRes(requestBody:GetNewSegRes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSegRes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetNewSegRes", {
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
         resolve(data as GetNewSegRes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListsForProcess
   Description: Builds list for ranges, options, restrictions, and currency accounts for the Natural Account Mass Update process
   OperationID: GetListsForProcess
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListsForProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListsForProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListsForProcess(requestBody:GetListsForProcess_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListsForProcess_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetListsForProcess", {
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
         resolve(data as GetListsForProcess_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCOACategoriesFromList
   Description: Create Natural Account COA Categories datatable for selection
   OperationID: GetCOACategoriesFromList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCOACategoriesFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOACategoriesFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOACategoriesFromList(requestBody:GetCOACategoriesFromList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCOACategoriesFromList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetCOACategoriesFromList", {
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
         resolve(data as GetCOACategoriesFromList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultsOnAddSegAcct
   Description: Check if account is valid and set description for it
   OperationID: DefaultsOnAddSegAcct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultsOnAddSegAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAddSegAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultsOnAddSegAcct(requestBody:DefaultsOnAddSegAcct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultsOnAddSegAcct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/DefaultsOnAddSegAcct", {
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
         resolve(data as DefaultsOnAddSegAcct_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCOA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOA(requestBody:GetNewCOA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCOA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetNewCOA", {
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
         resolve(data as GetNewCOA_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COAListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow{
   "odatametadata":string,
   "value":Erp_Tablesets_COARow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SegAcctRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegOptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SegOptRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegRangeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SegRangeRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegResRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SegResRow,
}

export interface Erp_Tablesets_COAListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "Description":string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   "SeparatorChar":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgDate":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgTime":number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   "CtrlSegList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Marks the COA as Global  */  
   "GlobalCOA":boolean,
      /**  Disables this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   "RebuildGLAccts":boolean,
      /**  Logical indicating if the chart has been used  */  
   "ChartInUse":boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   "ChartLength":number,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
      /**  Total number of segments defined for this COA  */  
   "NbrSegments":number,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   "HasRefSegment":boolean,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   "ConsInUse":boolean,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   "RebuildBalances":boolean,
      /**  Logical indicating if default categories are to be created  */  
   "CreateDefCat":boolean,
   "GlbFlag":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "Description":string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   "SeparatorChar":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgDate":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgTime":number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   "CtrlSegList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Marks the COA as Global  */  
   "GlobalCOA":boolean,
      /**  Disables this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   "RebuildGLAccts":boolean,
      /**  Peru CSF: SUNAT Chart of Accounts Code  */  
   "PESunatCOA":string,
      /**  Logical indicating if the chart has been used  */  
   "ChartInUse":boolean,
      /**  Logical indicating if default categories are to be created  */  
   "CreateDefCat":boolean,
   "EnableGlobalCOA":boolean,
   "EnableGlobalLock":boolean,
   "GlbFlag":boolean,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   "HasRefSegment":boolean,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
      /**  Total number of segments defined for this COA  */  
   "NbrSegments":number,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   "RebuildBalances":boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   "ChartLength":number,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   "ConsInUse":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SegAcctRow{
      /**  The natural account used as the accrual account.  */  
   "AccrualAccount":string,
      /**  Accrual GL Account description  */  
   "AccrualGLDesc":string,
      /**  AccrualSegVal1  */  
   "AccrualSegVal1":string,
      /**  AccrualSegVal10  */  
   "AccrualSegVal10":string,
      /**  AccrualSegVal11  */  
   "AccrualSegVal11":string,
      /**  AccrualSegVal12  */  
   "AccrualSegVal12":string,
      /**  AccrualSegVal13  */  
   "AccrualSegVal13":string,
      /**  AccrualSegVal14  */  
   "AccrualSegVal14":string,
      /**  AccrualSegVal15  */  
   "AccrualSegVal15":string,
      /**  AccrualSegVal16  */  
   "AccrualSegVal16":string,
      /**  AccrualSegVal17  */  
   "AccrualSegVal17":string,
      /**  AccrualSegVal18  */  
   "AccrualSegVal18":string,
      /**  AccrualSegVal19  */  
   "AccrualSegVal19":string,
      /**  AccrualSegVal2  */  
   "AccrualSegVal2":string,
      /**  AccrualSegVal20  */  
   "AccrualSegVal20":string,
      /**  AccrualSegVal3  */  
   "AccrualSegVal3":string,
      /**  AccrualSegVal4  */  
   "AccrualSegVal4":string,
      /**  AccrualSegVal5  */  
   "AccrualSegVal5":string,
      /**  AccrualSegVal6  */  
   "AccrualSegVal6":string,
      /**  AccrualSegVal7  */  
   "AccrualSegVal7":string,
      /**  AccrualSegVal8  */  
   "AccrualSegVal8":string,
      /**  AccrualSegVal9  */  
   "AccrualSegVal9":string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   "Allowed":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Description of the currency  */  
   "CurrDesc":string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   "CurrencyCode":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "DocumentDesc":string,
      /**  The natural account used for booking currency gains.  */  
   "GainAccount":string,
      /**  Gain GL Account Description  */  
   "GainGLDesc":string,
      /**  GainSegVal1  */  
   "GainSegVal1":string,
      /**  GainSegVal10  */  
   "GainSegVal10":string,
      /**  GainSegVal11  */  
   "GainSegVal11":string,
      /**  GainSegVal12  */  
   "GainSegVal12":string,
      /**  GainSegVal13  */  
   "GainSegVal13":string,
      /**  GainSegVal14  */  
   "GainSegVal14":string,
      /**  GainSegVal15  */  
   "GainSegVal15":string,
      /**  GainSegVal16  */  
   "GainSegVal16":string,
      /**  GainSegVal17  */  
   "GainSegVal17":string,
      /**  GainSegVal18  */  
   "GainSegVal18":string,
      /**  GainSegVal19  */  
   "GainSegVal19":string,
      /**  GainSegVal2  */  
   "GainSegVal2":string,
      /**  GainSegVal20  */  
   "GainSegVal20":string,
      /**  GainSegVal3  */  
   "GainSegVal3":string,
      /**  GainSegVal4  */  
   "GainSegVal4":string,
      /**  GainSegVal5  */  
   "GainSegVal5":string,
      /**  GainSegVal6  */  
   "GainSegVal6":string,
      /**  GainSegVal7  */  
   "GainSegVal7":string,
      /**  GainSegVal8  */  
   "GainSegVal8":string,
      /**  GainSegVal9  */  
   "GainSegVal9":string,
      /**  The natural account used for booking currency losses.  */  
   "LossAccount":string,
      /**  Loss GL Account Description  */  
   "LossGLDesc":string,
      /**  LossSegVal1  */  
   "LossSegVal1":string,
      /**  LossSegVal10  */  
   "LossSegVal10":string,
      /**  LossSegVal11  */  
   "LossSegVal11":string,
      /**  LossSegVal12  */  
   "LossSegVal12":string,
      /**  LossSegVal13  */  
   "LossSegVal13":string,
      /**  LossSegVal14  */  
   "LossSegVal14":string,
      /**  LossSegVal15  */  
   "LossSegVal15":string,
      /**  LossSegVal16  */  
   "LossSegVal16":string,
      /**  LossSegVal17  */  
   "LossSegVal17":string,
      /**  LossSegVal18  */  
   "LossSegVal18":string,
      /**  LossSegVal19  */  
   "LossSegVal19":string,
      /**  LossSegVal2  */  
   "LossSegVal2":string,
      /**  LossSegVal20  */  
   "LossSegVal20":string,
      /**  LossSegVal3  */  
   "LossSegVal3":string,
      /**  LossSegVal4  */  
   "LossSegVal4":string,
      /**  LossSegVal5  */  
   "LossSegVal5":string,
      /**  LossSegVal6  */  
   "LossSegVal6":string,
      /**  LossSegVal7  */  
   "LossSegVal7":string,
      /**  LossSegVal8  */  
   "LossSegVal8":string,
      /**  LossSegVal9  */  
   "LossSegVal9":string,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   "Revalue":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SegOptRow{
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates the default segment value to be used for this natural account.  */  
   "DefaultSegment":string,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   "ValOption":string,
   "SegmentName":string,
   "SegmentNbr":number,
   "SubSegmentNbr":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SegRangeRow{
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Company Identifier.  */  
   "Company":string,
   "EndVal":string,
      /**  From code to code  */  
   "RangeID":string,
   "SegmentNbr":number,
   "StartVal":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SegResRow{
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if GL Account entry is prohibited  */  
   "FctBlocked":boolean,
      /**  Application DLL name  */  
   "RestrictID":string,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
   "SegmentNbr":number,
   "RestrictDesc":string,
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
      @param currencyAcctType
      @param revalueOpt
      @param currencyCode
      @param allowed
      @param ds
   */  
export interface ChangeAllowed_input{
      /**  Currency Account Type  */  
   currencyAcctType:string,
      /**  Revalue Option  */  
   revalueOpt:number,
      /**  Currency Code  */  
   currencyCode:string,
      /**  Allowed  */  
   allowed:boolean,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface ChangeAllowed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param coaCode
      @param revalueOpt
      @param ipValue
      @param ds
   */  
export interface ChangeCurrencyAccount_input{
      /**  Chart of account  */  
   coaCode:string,
      /**  Revalue option  */  
   revalueOpt:number,
      /**  Input value  */  
   ipValue:string,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface ChangeCurrencyAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param revalueOpt
      @param currencyCode
      @param ds
   */  
export interface ChangeRevalue_input{
      /**  Revalue Option  */  
   revalueOpt:number,
      /**  Currency Code  */  
   currencyCode:string,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface ChangeRevalue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param glAccount
      @param accountDescField
      @param ds
   */  
export interface DefaultsOnAddSegAcct_input{
      /**  GL Account being processed  */  
   glAccount:string,
      /**  GL Account description field being updated  */  
   accountDescField:string,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface DefaultsOnAddSegAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param coACode
   */  
export interface DeleteByID_input{
   coACode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param coaCode
      @param currencyCode
      @param ds
   */  
export interface DeleteCurrencyAccount_input{
      /**  Chart of account  */  
   coaCode:string,
      /**  Currency code to delete  */  
   currencyCode:string,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface DeleteCurrencyAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

export interface Erp_Tablesets_COAListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The description or Name of this Chart of Accounts.  */  
   Description:string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   SeparatorChar:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgDate:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgTime:number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   CtrlSegList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Marks the COA as Global  */  
   GlobalCOA:boolean,
      /**  Disables this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   RebuildGLAccts:boolean,
      /**  Logical indicating if the chart has been used  */  
   ChartInUse:boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   ChartLength:number,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
      /**  Total number of segments defined for this COA  */  
   NbrSegments:number,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   HasRefSegment:boolean,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   ConsInUse:boolean,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   RebuildBalances:boolean,
      /**  Logical indicating if default categories are to be created  */  
   CreateDefCat:boolean,
   GlbFlag:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The description or Name of this Chart of Accounts.  */  
   Description:string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   SeparatorChar:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgDate:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgTime:number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   CtrlSegList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Marks the COA as Global  */  
   GlobalCOA:boolean,
      /**  Disables this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   RebuildGLAccts:boolean,
      /**  Peru CSF: SUNAT Chart of Accounts Code  */  
   PESunatCOA:string,
      /**  Logical indicating if the chart has been used  */  
   ChartInUse:boolean,
      /**  Logical indicating if default categories are to be created  */  
   CreateDefCat:boolean,
   EnableGlobalCOA:boolean,
   EnableGlobalLock:boolean,
   GlbFlag:boolean,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   HasRefSegment:boolean,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
      /**  Total number of segments defined for this COA  */  
   NbrSegments:number,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   RebuildBalances:boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   ChartLength:number,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   ConsInUse:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLAccountMassUpdListTableset{
   COAList:Erp_Tablesets_COAListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLAccountMassUpdTableset{
   COA:Erp_Tablesets_COARow[],
   SegAcct:Erp_Tablesets_SegAcctRow[],
   SegOpt:Erp_Tablesets_SegOptRow[],
   SegRange:Erp_Tablesets_SegRangeRow[],
   SegRes:Erp_Tablesets_SegResRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_NatAcctUpdCOACategoryRow{
   Company:string,
   CategoryID:string,
   Description:string,
   Type:string,
   ParentCategory:string,
   CatNumber:string,
   NumberOfParents:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NatAcctUpdCOACategoryTableset{
   NatAcctUpdCOACategory:Erp_Tablesets_NatAcctUpdCOACategoryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SegAcctRow{
      /**  The natural account used as the accrual account.  */  
   AccrualAccount:string,
      /**  Accrual GL Account description  */  
   AccrualGLDesc:string,
      /**  AccrualSegVal1  */  
   AccrualSegVal1:string,
      /**  AccrualSegVal10  */  
   AccrualSegVal10:string,
      /**  AccrualSegVal11  */  
   AccrualSegVal11:string,
      /**  AccrualSegVal12  */  
   AccrualSegVal12:string,
      /**  AccrualSegVal13  */  
   AccrualSegVal13:string,
      /**  AccrualSegVal14  */  
   AccrualSegVal14:string,
      /**  AccrualSegVal15  */  
   AccrualSegVal15:string,
      /**  AccrualSegVal16  */  
   AccrualSegVal16:string,
      /**  AccrualSegVal17  */  
   AccrualSegVal17:string,
      /**  AccrualSegVal18  */  
   AccrualSegVal18:string,
      /**  AccrualSegVal19  */  
   AccrualSegVal19:string,
      /**  AccrualSegVal2  */  
   AccrualSegVal2:string,
      /**  AccrualSegVal20  */  
   AccrualSegVal20:string,
      /**  AccrualSegVal3  */  
   AccrualSegVal3:string,
      /**  AccrualSegVal4  */  
   AccrualSegVal4:string,
      /**  AccrualSegVal5  */  
   AccrualSegVal5:string,
      /**  AccrualSegVal6  */  
   AccrualSegVal6:string,
      /**  AccrualSegVal7  */  
   AccrualSegVal7:string,
      /**  AccrualSegVal8  */  
   AccrualSegVal8:string,
      /**  AccrualSegVal9  */  
   AccrualSegVal9:string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   Allowed:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   CurrencyCode:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   DocumentDesc:string,
      /**  The natural account used for booking currency gains.  */  
   GainAccount:string,
      /**  Gain GL Account Description  */  
   GainGLDesc:string,
      /**  GainSegVal1  */  
   GainSegVal1:string,
      /**  GainSegVal10  */  
   GainSegVal10:string,
      /**  GainSegVal11  */  
   GainSegVal11:string,
      /**  GainSegVal12  */  
   GainSegVal12:string,
      /**  GainSegVal13  */  
   GainSegVal13:string,
      /**  GainSegVal14  */  
   GainSegVal14:string,
      /**  GainSegVal15  */  
   GainSegVal15:string,
      /**  GainSegVal16  */  
   GainSegVal16:string,
      /**  GainSegVal17  */  
   GainSegVal17:string,
      /**  GainSegVal18  */  
   GainSegVal18:string,
      /**  GainSegVal19  */  
   GainSegVal19:string,
      /**  GainSegVal2  */  
   GainSegVal2:string,
      /**  GainSegVal20  */  
   GainSegVal20:string,
      /**  GainSegVal3  */  
   GainSegVal3:string,
      /**  GainSegVal4  */  
   GainSegVal4:string,
      /**  GainSegVal5  */  
   GainSegVal5:string,
      /**  GainSegVal6  */  
   GainSegVal6:string,
      /**  GainSegVal7  */  
   GainSegVal7:string,
      /**  GainSegVal8  */  
   GainSegVal8:string,
      /**  GainSegVal9  */  
   GainSegVal9:string,
      /**  The natural account used for booking currency losses.  */  
   LossAccount:string,
      /**  Loss GL Account Description  */  
   LossGLDesc:string,
      /**  LossSegVal1  */  
   LossSegVal1:string,
      /**  LossSegVal10  */  
   LossSegVal10:string,
      /**  LossSegVal11  */  
   LossSegVal11:string,
      /**  LossSegVal12  */  
   LossSegVal12:string,
      /**  LossSegVal13  */  
   LossSegVal13:string,
      /**  LossSegVal14  */  
   LossSegVal14:string,
      /**  LossSegVal15  */  
   LossSegVal15:string,
      /**  LossSegVal16  */  
   LossSegVal16:string,
      /**  LossSegVal17  */  
   LossSegVal17:string,
      /**  LossSegVal18  */  
   LossSegVal18:string,
      /**  LossSegVal19  */  
   LossSegVal19:string,
      /**  LossSegVal2  */  
   LossSegVal2:string,
      /**  LossSegVal20  */  
   LossSegVal20:string,
      /**  LossSegVal3  */  
   LossSegVal3:string,
      /**  LossSegVal4  */  
   LossSegVal4:string,
      /**  LossSegVal5  */  
   LossSegVal5:string,
      /**  LossSegVal6  */  
   LossSegVal6:string,
      /**  LossSegVal7  */  
   LossSegVal7:string,
      /**  LossSegVal8  */  
   LossSegVal8:string,
      /**  LossSegVal9  */  
   LossSegVal9:string,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   Revalue:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SegOptRow{
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates the default segment value to be used for this natural account.  */  
   DefaultSegment:string,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   ValOption:string,
   SegmentName:string,
   SegmentNbr:number,
   SubSegmentNbr:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SegRangeRow{
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Company Identifier.  */  
   Company:string,
   EndVal:string,
      /**  From code to code  */  
   RangeID:string,
   SegmentNbr:number,
   StartVal:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SegResRow{
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if GL Account entry is prohibited  */  
   FctBlocked:boolean,
      /**  Application DLL name  */  
   RestrictID:string,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
   SegmentNbr:number,
   RestrictDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtGLAccountMassUpdTableset{
   COA:Erp_Tablesets_COARow[],
   SegAcct:Erp_Tablesets_SegAcctRow[],
   SegOpt:Erp_Tablesets_SegOptRow[],
   SegRange:Erp_Tablesets_SegRangeRow[],
   SegRes:Erp_Tablesets_SegResRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param coACode
   */  
export interface GetByID_input{
   coACode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLAccountMassUpdTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLAccountMassUpdTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLAccountMassUpdTableset[],
}

   /** Required : 
      @param categoryList
   */  
export interface GetCOACategoriesFromList_input{
      /**  Category list  */  
   categoryList:string,
}

export interface GetCOACategoriesFromList_output{
   returnObj:Erp_Tablesets_NatAcctUpdCOACategoryTableset[],
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
   returnObj:Erp_Tablesets_GLAccountMassUpdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetListsForProcess_input{
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface GetListsForProcess_output{
parameters : {
      /**  output parameters  */  
   segRangesList:string,
   segOptsList:string,
   restrictionsList:string,
   coaSegAcctList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCOA_input{
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface GetNewCOA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param coaCode
      @param ds
   */  
export interface GetNewSegOpt_input{
      /**  COA Code  */  
   coaCode:string,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface GetNewSegOpt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param coaCode
      @param ds
   */  
export interface GetNewSegRange_input{
      /**  COA Code  */  
   coaCode:string,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface GetNewSegRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param coaCode
      @param ds
   */  
export interface GetNewSegRes_input{
      /**  COA Code  */  
   coaCode:string,
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface GetNewSegRes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

   /** Required : 
      @param whereClauseCOA
      @param whereClauseSegAcct
      @param whereClauseSegOpt
      @param whereClauseSegRange
      @param whereClauseSegRes
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCOA:string,
   whereClauseSegAcct:string,
   whereClauseSegOpt:string,
   whereClauseSegRange:string,
   whereClauseSegRes:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLAccountMassUpdTableset[],
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
   ds:Erp_Tablesets_UpdExtGLAccountMassUpdTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLAccountMassUpdTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLAccountMassUpdTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountMassUpdTableset,
}
}

