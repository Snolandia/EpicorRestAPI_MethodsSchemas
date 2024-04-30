import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ConfiguratorRuleSvc
// Description: This Business Object allows the modification of configurator method and structure rules
            The configurator is the design portion that is run during a configuration.
           
            Business Object for the configurator rule designer
            Brock Mulqueen
            07/12/12
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/$metadata", {
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
   Description: Get ConfiguratorRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfiguratorRules
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevRow
   */  
export function get_ConfiguratorRules(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfiguratorRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartRevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfiguratorRules(requestBody:Erp_Tablesets_PartRevRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules", {
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
   Summary: Calls GetByID to retrieve the ConfiguratorRule item
   Description: Calls GetByID to retrieve the ConfiguratorRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfiguratorRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartRevRow
   */  
export function get_ConfiguratorRules_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartRevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
         resolve(data as Erp_Tablesets_PartRevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConfiguratorRule for the service
   Description: Calls UpdateExt to update ConfiguratorRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfiguratorRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConfiguratorRules_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, requestBody:Erp_Tablesets_PartRevRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
   Summary: Call UpdateExt to delete ConfiguratorRule item
   Description: Call UpdateExt to delete ConfiguratorRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfiguratorRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConfiguratorRules_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
   Description: Get PcMethodVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcMethodVars
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcMethodVarRow
   */  
export function get_PcMethodVars(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcMethodVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcMethodVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcMethodVars
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcMethodVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PcMethodVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcMethodVars(requestBody:Erp_Tablesets_PcMethodVarRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars", {
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
   Summary: Calls GetByID to retrieve the PcMethodVar item
   Description: Calls GetByID to retrieve the PcMethodVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcMethodVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param VarNum Desc: VarNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcMethodVarRow
   */  
export function get_PcMethodVars_Company_ConfigID_PartNum_RevisionNum_AltMethod_VarNum(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, VarNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcMethodVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + VarNum + ")", {
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
         resolve(data as Erp_Tablesets_PcMethodVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcMethodVar for the service
   Description: Calls UpdateExt to update PcMethodVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcMethodVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param VarNum Desc: VarNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcMethodVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcMethodVars_Company_ConfigID_PartNum_RevisionNum_AltMethod_VarNum(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, VarNum:string, requestBody:Erp_Tablesets_PcMethodVarRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + VarNum + ")", {
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
   Summary: Call UpdateExt to delete PcMethodVar item
   Description: Call UpdateExt to delete PcMethodVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcMethodVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param VarNum Desc: VarNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcMethodVars_Company_ConfigID_PartNum_RevisionNum_AltMethod_VarNum(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, VarNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + VarNum + ")", {
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
   Description: Get PcRuleSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcRuleSets
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRuleSetRow
   */  
export function get_PcRuleSets(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRuleSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRuleSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcRuleSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcRuleSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PcRuleSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcRuleSets(requestBody:Erp_Tablesets_PcRuleSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets", {
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
   Summary: Calls GetByID to retrieve the PcRuleSet item
   Description: Calls GetByID to retrieve the PcRuleSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRuleSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param BOMElementTableName Desc: BOMElementTableName   Required: True   Allow empty value : True
      @param BOMElementSysRowID Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      @param RuleTag Desc: RuleTag   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcRuleSetRow
   */  
export function get_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, BOMElementTableName:string, BOMElementSysRowID:string, RuleTag:string, RuleSetID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcRuleSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")", {
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
         resolve(data as Erp_Tablesets_PcRuleSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcRuleSet for the service
   Description: Calls UpdateExt to update PcRuleSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcRuleSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param BOMElementTableName Desc: BOMElementTableName   Required: True   Allow empty value : True
      @param BOMElementSysRowID Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      @param RuleTag Desc: RuleTag   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcRuleSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, BOMElementTableName:string, BOMElementSysRowID:string, RuleTag:string, RuleSetID:string, requestBody:Erp_Tablesets_PcRuleSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")", {
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
   Summary: Call UpdateExt to delete PcRuleSet item
   Description: Call UpdateExt to delete PcRuleSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcRuleSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param BOMElementTableName Desc: BOMElementTableName   Required: True   Allow empty value : True
      @param BOMElementSysRowID Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      @param RuleTag Desc: RuleTag   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, BOMElementTableName:string, BOMElementSysRowID:string, RuleTag:string, RuleSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")", {
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
   Description: Get PcRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcRules1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param BOMElementTableName Desc: BOMElementTableName   Required: True   Allow empty value : True
      @param BOMElementSysRowID Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      @param RuleTag Desc: RuleTag   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesRow
   */  
export function get_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID_PcRules(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, BOMElementTableName:string, BOMElementSysRowID:string, RuleTag:string, RuleSetID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")/PcRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcRule item
   Description: Calls GetByID to retrieve the PcRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRule1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param BOMElementTableName Desc: BOMElementTableName   Required: True   Allow empty value : True
      @param BOMElementSysRowID Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      @param RuleTag Desc: RuleTag   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcRulesRow
   */  
export function get_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, BOMElementTableName:string, BOMElementSysRowID:string, RuleTag:string, RuleSetID:string, RuleSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcRulesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")", {
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
         resolve(data as Erp_Tablesets_PcRulesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcRules
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesRow
   */  
export function get_PcRules(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcRulesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PcRulesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcRules(requestBody:Erp_Tablesets_PcRulesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules", {
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
   Summary: Calls GetByID to retrieve the PcRule item
   Description: Calls GetByID to retrieve the PcRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcRulesRow
   */  
export function get_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcRulesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")", {
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
         resolve(data as Erp_Tablesets_PcRulesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcRule for the service
   Description: Calls UpdateExt to update PcRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcRulesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, requestBody:Erp_Tablesets_PcRulesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")", {
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
   Summary: Call UpdateExt to delete PcRule item
   Description: Call UpdateExt to delete PcRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")", {
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
   Description: Get PcRulesExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcRulesExprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesExprRow
   */  
export function get_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_PcRulesExprs(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")/PcRulesExprs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcRulesExpr item
   Description: Calls GetByID to retrieve the PcRulesExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRulesExpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcRulesExprRow
   */  
export function get_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcRulesExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_PcRulesExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcRulesExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcRulesExprs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesExprRow
   */  
export function get_PcRulesExprs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcRulesExprs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcRulesExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PcRulesExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcRulesExprs(requestBody:Erp_Tablesets_PcRulesExprRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs", {
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
   Summary: Calls GetByID to retrieve the PcRulesExpr item
   Description: Calls GetByID to retrieve the PcRulesExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRulesExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcRulesExprRow
   */  
export function get_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcRulesExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_PcRulesExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcRulesExpr for the service
   Description: Calls UpdateExt to update PcRulesExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcRulesExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcRulesExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, TypeCode:string, SeqNum:string, requestBody:Erp_Tablesets_PcRulesExprRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete PcRulesExpr item
   Description: Call UpdateExt to delete PcRulesExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcRulesExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param RuleSetID Desc: RuleSetID   Required: True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PartNum:string, RevisionNum:string, AltMethod:string, RuleSetID:string, RuleSeq:string, TypeCode:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow)
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
export function get_GetRows(whereClausePartRev:string, whereClausePcMethodVar:string, whereClausePcRuleSet:string, whereClausePcRules:string, whereClausePcRulesExpr:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartRev!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartRev=" + whereClausePartRev
   }
   if(typeof whereClausePcMethodVar!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcMethodVar=" + whereClausePcMethodVar
   }
   if(typeof whereClausePcRuleSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcRuleSet=" + whereClausePcRuleSet
   }
   if(typeof whereClausePcRules!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcRules=" + whereClausePcRules
   }
   if(typeof whereClausePcRulesExpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcRulesExpr=" + whereClausePcRulesExpr
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, revisionNum:string, altMethod:string, processMfgID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof revisionNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "revisionNum=" + revisionNum
   }
   if(typeof altMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "altMethod=" + altMethod
   }
   if(typeof processMfgID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "processMfgID=" + processMfgID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetCodeDescList", {
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
   Summary: Invoke method SalesKitConfiguration
   Description: If a partplant record is available for the current plant then check the SourceType
If not partplant available then check the typecode on the part record.
   OperationID: SalesKitConfiguration
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SalesKitConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesKitConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesKitConfiguration(requestBody:SalesKitConfiguration_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SalesKitConfiguration_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/SalesKitConfiguration", {
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
         resolve(data as SalesKitConfiguration_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckIsConfigured
   Description: This methods is called prior to expanding a tree node on the Rules tab.  If the
part is a configureable part, the node will not be expanded
   OperationID: CheckIsConfigured
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckIsConfigured_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIsConfigured_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIsConfigured(requestBody:CheckIsConfigured_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckIsConfigured_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/CheckIsConfigured", {
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
         resolve(data as CheckIsConfigured_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RulesMoveDown
   Description: Move a rule down in the order of configuration rules.
   OperationID: RulesMoveDown
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RulesMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RulesMoveDown(requestBody:RulesMoveDown_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RulesMoveDown_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/RulesMoveDown", {
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
         resolve(data as RulesMoveDown_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RulesMoveUp
   Description: Move a rule up in the order of configuration rules.
   OperationID: RulesMoveUp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RulesMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RulesMoveUp(requestBody:RulesMoveUp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RulesMoveUp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/RulesMoveUp", {
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
         resolve(data as RulesMoveUp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters but only for the main revision the alternate methods will only will be add the ParRev record
This method will also allow you to return the whole dataset or allow the user to specify how
the revision to return possible "part" records for.
   OperationID: GetDatasetForTree
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTree(requestBody:GetDatasetForTree_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDatasetForTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetDatasetForTree", {
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
         resolve(data as GetDatasetForTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllAlternateTrees
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
ALL ALTERNATES OF THE PARTREVISION WILL BE RETURNED if ipcomplete is true
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
Vdavila - To allow keep the position of the current element in tree view when refresh we are going to use the
lastNodeKey to continue building the BOM for non-configure subassemblies
   OperationID: GetAllAlternateTrees
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllAlternateTrees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllAlternateTrees_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllAlternateTrees(requestBody:GetAllAlternateTrees_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllAlternateTrees_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetAllAlternateTrees", {
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
         resolve(data as GetAllAlternateTrees_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PromptForPassword
   Description: This method checks the BMSyst record to see if a password should prompted for and then
validated by the ValidatePassword method in UserFile BO.  Run this before SyncRevision method is called.
   OperationID: PromptForPassword
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PromptForPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptForPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PromptForPassword(requestBody:PromptForPassword_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PromptForPassword_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PromptForPassword", {
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
         resolve(data as PromptForPassword_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SyncRevision
   Description: This method synchronizes the part revision approval flag when the PcStatus.Approved
flag changes
   OperationID: SyncRevision
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SyncRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyncRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SyncRevision(requestBody:SyncRevision_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SyncRevision_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/SyncRevision", {
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
         resolve(data as SyncRevision_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangingEntConf
   Description: This methods checks to see if any enterprise configurator specific settings
have been created.  If so then a message should be displayed prior to unchecking
the enterprise configurator checkbox
   OperationID: ChangingEntConf
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangingEntConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingEntConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangingEntConf(requestBody:ChangingEntConf_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangingEntConf_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ChangingEntConf", {
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
         resolve(data as ChangingEntConf_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcRulesExprExprType
   Description: This method is executed when changing the ExprType column of PcRulesExpr, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcRulesExprExprType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedPcRulesExprExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcRulesExprExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcRulesExprExprType(requestBody:OnChangedPcRulesExprExprType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedPcRulesExprExprType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangedPcRulesExprExprType", {
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
         resolve(data as OnChangedPcRulesExprExprType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcRulesRuleType
   Description: This method is executed when changing the RuleType column of PcRules, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcRulesRuleType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedPcRulesRuleType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcRulesRuleType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcRulesRuleType(requestBody:OnChangedPcRulesRuleType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedPcRulesRuleType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangedPcRulesRuleType", {
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
         resolve(data as OnChangedPcRulesRuleType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePcRulesExprLValue
   Description: This method is executed when changing the LValue column of PcRulesExpr, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcRulesExprLValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePcRulesExprLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcRulesExprLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePcRulesExprLValue(requestBody:OnChangePcRulesExprLValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePcRulesExprLValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangePcRulesExprLValue", {
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
         resolve(data as OnChangePcRulesExprLValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePcRulesLValue
   Description: This method is executed when changing the LValue column of PcRules, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcRulesLValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePcRulesLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcRulesLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePcRulesLValue(requestBody:OnChangePcRulesLValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePcRulesLValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangePcRulesLValue", {
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
         resolve(data as OnChangePcRulesLValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Validate if exists PartNum and returns the partnum
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangePartNum", {
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
   Summary: Invoke method OnChangedRuleSetCompany
   Description: Change Company when click check boxes for Multi-Company or Local company
Must clear the list of companies in case already selected in picker list
   OperationID: OnChangedRuleSetCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedRuleSetCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedRuleSetCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedRuleSetCompany(requestBody:OnChangedRuleSetCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedRuleSetCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangedRuleSetCompany", {
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
         resolve(data as OnChangedRuleSetCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePcRulesDelete
   Description: Validate if exist child record when try to delete
   OperationID: ValidatePcRulesDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePcRulesDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcRulesDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePcRulesDelete(requestBody:ValidatePcRulesDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePcRulesDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ValidatePcRulesDelete", {
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
         resolve(data as ValidatePcRulesDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EditorFilter
   Description: Return filter for editor
   OperationID: EditorFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EditorFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EditorFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EditorFilter(requestBody:EditorFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EditorFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/EditorFilter", {
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
         resolve(data as EditorFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetValidTargetEntitiesAndInputs
   Description: Gathers valid target entities
   OperationID: GetValidTargetEntitiesAndInputs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetValidTargetEntitiesAndInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidTargetEntitiesAndInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetValidTargetEntitiesAndInputs(requestBody:GetValidTargetEntitiesAndInputs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetValidTargetEntitiesAndInputs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetValidTargetEntitiesAndInputs", {
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
         resolve(data as GetValidTargetEntitiesAndInputs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingPcMethodVarDataType
   Description: Validate variable is not being used.
   OperationID: OnChangingPcMethodVarDataType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingPcMethodVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcMethodVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingPcMethodVarDataType(requestBody:OnChangingPcMethodVarDataType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingPcMethodVarDataType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangingPcMethodVarDataType", {
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
         resolve(data as OnChangingPcMethodVarDataType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcMethodVarDataType
   Description: Clean DataType when dataType is changed
   OperationID: OnChangedPcMethodVarDataType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedPcMethodVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcMethodVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcMethodVarDataType(requestBody:OnChangedPcMethodVarDataType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedPcMethodVarDataType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangedPcMethodVarDataType", {
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
         resolve(data as OnChangedPcMethodVarDataType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingPcMethodVarVarName
   Description: Validate Changing VarName
   OperationID: OnChangingPcMethodVarVarName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingPcMethodVarVarName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcMethodVarVarName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingPcMethodVarVarName(requestBody:OnChangingPcMethodVarVarName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingPcMethodVarVarName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangingPcMethodVarVarName", {
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
         resolve(data as OnChangingPcMethodVarVarName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcMethodVarExprType
   Description: This method is executed when changing the ExprType column of PcMethod, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcMethodVarExprType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedPcMethodVarExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcMethodVarExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcMethodVarExprType(requestBody:OnChangedPcMethodVarExprType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedPcMethodVarExprType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangedPcMethodVarExprType", {
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
         resolve(data as OnChangedPcMethodVarExprType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MethodVarMoveDown
   Description: Move a Variable down in the order of method variables.
   OperationID: MethodVarMoveDown
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MethodVarMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MethodVarMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MethodVarMoveDown(requestBody:MethodVarMoveDown_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MethodVarMoveDown_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/MethodVarMoveDown", {
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
         resolve(data as MethodVarMoveDown_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MethodVarMoveUp
   Description: Move a Variable up in the order of method variables.
   OperationID: MethodVarMoveUp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MethodVarMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MethodVarMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MethodVarMoveUp(requestBody:MethodVarMoveUp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MethodVarMoveUp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/MethodVarMoveUp", {
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
         resolve(data as MethodVarMoveUp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailMethodVariables
   Description: Get the available method variables that may be used in code editor.
   OperationID: GetAvailMethodVariables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailMethodVariables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailMethodVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailMethodVariables(requestBody:GetAvailMethodVariables_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailMethodVariables_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetAvailMethodVariables", {
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
         resolve(data as GetAvailMethodVariables_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRevisionNum
   Description: When type a revision in revision combo it validates if revision exists
   OperationID: ValidateRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRevisionNum(requestBody:ValidateRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ValidateRevisionNum", {
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
         resolve(data as ValidateRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedConfigID
   Description: Assign the configurator id to alt methods
   OperationID: OnChangedConfigID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedConfigID(requestBody:OnChangedConfigID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedConfigID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/OnChangedConfigID", {
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
         resolve(data as OnChangedConfigID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BeforeStartTestRules
   Description: Generates the configuration sequence and validate if non of the configurators has rules then throw exception and will not open Test Rules window,
and build the message that will send when there are configurators not approved
   OperationID: BeforeStartTestRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BeforeStartTestRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeStartTestRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BeforeStartTestRules(requestBody:BeforeStartTestRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BeforeStartTestRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/BeforeStartTestRules", {
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
         resolve(data as BeforeStartTestRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyMethodRules
   Description: Copy rules from the Source part to the part selected in Copy Rules Form
-CopyActions:
-Replace: Will delete the existing rules from target part
-Append:  Will search if already exists a rule set using rule tag if exists will not copy anything neither rule set, rules or rulesexpr
Create results data to display it in a grid.
-Copied: rules copied successfully
-Not Copied: rules not copied because already exists rule set or does not exists element in target BOM
-Exception: will not display anything when element does not exists in target BOM and source BOM
-
   OperationID: CopyMethodRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyMethodRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyMethodRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyMethodRules(requestBody:CopyMethodRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyMethodRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/CopyMethodRules", {
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
         resolve(data as CopyMethodRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPrimaryPartNum
   Description: Find the Primary Part Number for a Configuration ID
   OperationID: GetPrimaryPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPrimaryPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPrimaryPartNum(requestBody:GetPrimaryPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPrimaryPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetPrimaryPartNum", {
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
         resolve(data as GetPrimaryPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartRev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartRev
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartRev(requestBody:GetNewPartRev_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartRev_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetNewPartRev", {
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
         resolve(data as GetNewPartRev_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcMethodVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcMethodVar
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPcMethodVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcMethodVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcMethodVar(requestBody:GetNewPcMethodVar_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPcMethodVar_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetNewPcMethodVar", {
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
         resolve(data as GetNewPcMethodVar_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcRuleSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcRuleSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPcRuleSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcRuleSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcRuleSet(requestBody:GetNewPcRuleSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPcRuleSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetNewPcRuleSet", {
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
         resolve(data as GetNewPcRuleSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcRules
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPcRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcRules(requestBody:GetNewPcRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPcRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetNewPcRules", {
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
         resolve(data as GetNewPcRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcRulesExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcRulesExpr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPcRulesExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcRulesExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcRulesExpr(requestBody:GetNewPcRulesExpr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPcRulesExpr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetNewPcRulesExpr", {
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
         resolve(data as GetNewPcRulesExpr_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartRevListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartRevRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcMethodVarRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcMethodVarRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRuleSetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcRuleSetRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesExprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcRulesExprRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcRulesRow,
}

export interface Erp_Tablesets_PartRevListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   "RevShortDesc":string,
      /**  Used to enter a full description of the revision.  */  
   "RevDescription":string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   "Approved":boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   "EffectiveDate":string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRSetupBurdenCost":number,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   "ECO":string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   "Configured":boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   "WebConfigured":boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   "ShowInputPrice":boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  The description of the alternate method.  */  
   "AltMethodDesc":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The alternate method of the parent this method inherits from.  */  
   "ParentAltMethod":string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   "UseStaging":boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   "UseAltRevForParts":boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  External Configurator  */  
   "ExtConfig":boolean,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Is the part for this revision a global part  */  
   "PcGlobalPart":boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   "PcEntprsConf":boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   "GlobalRev":boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   "RoughCutCode":string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   "RMAInspPlan":string,
      /**  The specification ID to use for RMA processing for this part.  */  
   "RMASpecID":string,
      /**  The default sample size to use for RMA processing for this part  */  
   "RMASampleSize":number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   "RMASampleSizePct":number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   "BaseRevisionNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   "vDate":string,
   "vQty":number,
   "ProdCode":string,
   "NonStock":boolean,
   "Class":string,
   "ParentAltMethodDesc":string,
      /**  Name of ECO Group that this part is checked out to  */  
   "ECOGroup":string,
   "DisableApproved":boolean,
   "SpecHedDescription":string,
      /**  The description of the inspection plan  */  
   "InspPlanDescription":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartDescriptionPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartDescriptionTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartDescriptionIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartDescriptionSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartDescriptionTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartDescriptionPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartDescriptionSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartDescriptionTrackSerialNum":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Full description of the rough cut parameter set.  */  
   "RoughCutParamDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartRevRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   "RevShortDesc":string,
      /**  Used to enter a full description of the revision.  */  
   "RevDescription":string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   "Approved":boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   "EffectiveDate":string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRSetupBurdenCost":number,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   "ECO":string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   "Configured":boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   "WebConfigured":boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   "ShowInputPrice":boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  The description of the alternate method.  */  
   "AltMethodDesc":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The alternate method of the parent this method inherits from.  */  
   "ParentAltMethod":string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   "UseStaging":boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   "UseAltRevForParts":boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  External Configurator  */  
   "ExtConfig":boolean,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Is the part for this revision a global part  */  
   "PcGlobalPart":boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   "PcEntprsConf":boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   "GlobalRev":boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   "RoughCutCode":string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   "RMAInspPlan":string,
      /**  The specification ID to use for RMA processing for this part.  */  
   "RMASpecID":string,
      /**  The default sample size to use for RMA processing for this part  */  
   "RMASampleSize":number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   "RMASampleSizePct":number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   "BaseRevisionNum":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  RegenConfig  */  
   "RegenConfig":boolean,
      /**  SIValuesGroupSeq  */  
   "SIValuesGroupSeq":number,
      /**  SIValuesHeadNum  */  
   "SIValuesHeadNum":number,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   "ProcessMode":string,
      /**  DefaultConfigPart  */  
   "DefaultConfigPart":boolean,
      /**  Number of COPart required in the Revision  */  
   "CoPartsReqQty":number,
      /**  Material Cost Factor  */  
   "MtlCostPct":number,
      /**  Labor Cost Factor  */  
   "LaborCostPct":number,
      /**  Number of COParts per Operation  */  
   "CoPartsPerOp":number,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Customs BOM  */  
   "CNCustomsBOM":boolean,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Type of Process Manufacturing this revision is for: General, Site, Master.  */  
   "ProcessMfgType":string,
      /**  Description of Process Manufacturing revision.  */  
   "ProcessMfgDescription":string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   "UseAdvancedStaging":boolean,
      /**  The last Group to modify this Revision for Recipe Authoring.  */  
   "ProcessMfgLastGroupID":string,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   "ECPCEnabled":boolean,
   "DisableApproved":boolean,
      /**  Name of ECO Group that this part is checked out to  */  
   "ECOGroup":string,
      /**  This field will be set to true if two or more ECOCoParts records exist for the revision.  */  
   "HasCoParts":boolean,
   "ParentAltMethodDesc":string,
      /**  Part Number of the Parent Part  */  
   "ParentPartNum":string,
      /**  Revision number  of Parent Part.  */  
   "ParentRevisionNum":string,
   "ProdCode":string,
      /**   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  */  
   "RevStatusAsOfDate":number,
   "SpecHedDescription":string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   "vDate":string,
   "vQty":number,
   "Class":string,
   "NonStock":boolean,
      /**  Indicates that the PartRev is the root node in the tree  */  
   "IsRootNode":boolean,
      /**  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  */  
   "EngineeringApproved":boolean,
   "BitFlag":number,
   "InspPlanDescription":string,
   "PartDescriptionTrackDimension":boolean,
   "PartDescriptionSellingFactor":number,
   "PartDescriptionPartDescription":string,
   "PartDescriptionIUM":string,
   "PartDescriptionTrackLots":boolean,
   "PartDescriptionPricePerCode":string,
   "PartDescriptionSalesUM":string,
   "PartDescriptionTrackSerialNum":boolean,
   "PartDescriptionTypeCode":string,
   "PcStatusConfigType":string,
   "PlantName":string,
   "RoughCutParamDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcMethodVarRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  PartNum  */  
   "PartNum":string,
      /**  RevisionNum  */  
   "RevisionNum":string,
      /**  AltMethod  */  
   "AltMethod":string,
      /**  VarNum  */  
   "VarNum":number,
      /**  VarName  */  
   "VarName":string,
      /**  DataType  */  
   "DataType":string,
      /**  Expression  */  
   "Expression":string,
      /**  ExprType  */  
   "ExprType":string,
      /**  VarSeq  */  
   "VarSeq":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Temporal column to show link phrase  */  
   "DispLinkString":string,
   "Format":string,
   "CanUpdate":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcRuleSetRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  PartNum  */  
   "PartNum":string,
      /**  RevisionNum  */  
   "RevisionNum":string,
      /**  AltMethod  */  
   "AltMethod":string,
      /**  RuleSetID  */  
   "RuleSetID":number,
      /**  BOMElementSysRowID  */  
   "BOMElementSysRowID":string,
      /**  BOMElementTableName  */  
   "BOMElementTableName":string,
      /**  BOMElementType  */  
   "BOMElementType":string,
      /**  RuleTag  */  
   "RuleTag":string,
      /**  MtlSeq  */  
   "MtlSeq":number,
      /**  OprSeq  */  
   "OprSeq":number,
      /**  OpDtlSeq  */  
   "OpDtlSeq":number,
      /**  UseKeepWhen  */  
   "UseKeepWhen":boolean,
      /**  KeepWhenExpr  */  
   "KeepWhenExpr":string,
      /**  KeepWhenLValue  */  
   "KeepWhenLValue":string,
      /**  KeepWhenCompareOpr  */  
   "KeepWhenCompareOpr":string,
      /**  KeepWhenRValue  */  
   "KeepWhenRValue":string,
      /**  KeepWhenRValueType  */  
   "KeepWhenRValueType":string,
      /**  KeepWhenType  */  
   "KeepWhenType":string,
      /**  ExtCompanyList  */  
   "ExtCompanyList":string,
      /**  Comments  */  
   "Comments":string,
      /**  Expression  */  
   "Expression":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Indicates if is allowed Enterprise Configuration  */  
   "EntprsConf":boolean,
   "KeepWhenField":string,
   "KeepWhenTable":string,
      /**  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  */  
   "MultiCompany":boolean,
   "AsmPartNum":string,
      /**  If is Enterprise configuration allowed it will update if is Local Company or MultiCompany  */  
   "CompanyName":string,
   "CanUpdate":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcRulesExprRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number of the associated configurator  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  The sequence the rule is going to be applied.  */  
   "RuleSeq":number,
      /**  Operation Sequence Number  */  
   "OprSeq":number,
      /**  Material Sequence Number  */  
   "MtlSeq":number,
      /**  Stores the parent part number within the multi-level BOM for which the rule is related.  */  
   "ParPartNum":string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   "AsmPartNum":string,
      /**  Alternate Routing method to be used for this rule.  */  
   "AltMethod":string,
      /**  Uniquely identifies an OpDtl  */  
   "OpDtlSeq":number,
      /**  Sequence Number.  */  
   "SeqNum":number,
      /**  Method Rule Expression  */  
   "Expression":string,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  ProcessOrder  */  
   "ProcessOrder":number,
      /**  RuleSetID  */  
   "RuleSetID":number,
      /**  ExprType  */  
   "ExprType":string,
      /**  LValue  */  
   "LValue":string,
      /**  CompareOpr  */  
   "CompareOpr":string,
      /**  RValue  */  
   "RValue":string,
      /**  RValueType  */  
   "RValueType":string,
      /**  ExprXMLItem  */  
   "ExprXMLItem":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DispActionString":string,
   "BOMElementSysRowID":string,
   "BOMElementTableName":string,
   "RuleTag":string,
      /**  Assing the default format for the constant editor  */  
   "Format":string,
   "dbField":string,
   "dbTable":string,
   "CanUpdate":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcRulesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Part Number of the associated configurator  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  The sequence the rule is going to be applied.  */  
   "RuleSeq":number,
      /**  Method Rule String  */  
   "RuleString":string,
      /**  Method Rule Type  */  
   "RuleType":string,
      /**  Method Rule Expression  */  
   "RuleExpr":string,
      /**  Name for the calculated field  */  
   "CalcName":string,
      /**  Calculated field data type  */  
   "CalcDataType":string,
      /**  Database Field  */  
   "dbField":string,
      /**  Database Table  */  
   "dbTable":string,
      /**  Operation Sequence Number  */  
   "OprSeq":number,
      /**  Material Sequence Number  */  
   "MtlSeq":number,
      /**  Stores the parent part number within the multi-level BOM for which the rule is related.  */  
   "ParPartNum":string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   "AsmPartNum":string,
      /**  Defines what the rule is related to.  Valid values include Par, Opr, Mtl, Asm.  This is used in Gencode.p when creating the compiled code.  */  
   "ElementType":string,
      /**  Alternate Routing method to be used for this rule.  */  
   "AltMethod":string,
      /**  A unique identifier for the rule.  This will be generated in the database trigger.  */  
   "RuleID":number,
      /**  Uniquely identifies an OpDtl  */  
   "OpDtlSeq":number,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  Comments  */  
   "Comments":string,
      /**  Rule Tag  */  
   "RuleTag":string,
      /**  Process Sequence  */  
   "ProcessSeq":number,
      /**  LValue  */  
   "LValue":string,
      /**  CompareOpr  */  
   "CompareOpr":string,
      /**  RValue  */  
   "RValue":string,
      /**  RValueType  */  
   "RValueType":string,
      /**  RuleSetID  */  
   "RuleSetID":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CanUpdate":boolean,
      /**  The node that is currently selected in the tree.  */  
   "CurrentNode":string,
   "CurrentRuleLineage":string,
      /**  The parent node of the current node that is selected in the tree  */  
   "ParentNode":string,
   "BOMElementTableName":string,
   "BOMElementSysRowID":string,
      /**  Assing the default format for the constant editor  */  
   "Format":string,
      /**  Temporal column to show link phrase  */  
   "DispLinkString":string,
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
      @param configID
      @param partNum
      @param revisionNum
   */  
export interface BeforeStartTestRules_input{
   configID:string,
   partNum:string,
   revisionNum:string,
}

export interface BeforeStartTestRules_output{
   returnObj:string,
}

   /** Required : 
      @param ipConfigID
   */  
export interface ChangingEntConf_input{
      /**  Current Configuration ID  */  
   ipConfigID:string,
}

export interface ChangingEntConf_output{
parameters : {
      /**  output parameters  */  
   settingsExist:boolean,
}
}

   /** Required : 
      @param ipPartNum
   */  
export interface CheckIsConfigured_input{
      /**  The proposed part number  */  
   ipPartNum:string,
}

export interface CheckIsConfigured_output{
parameters : {
      /**  output parameters  */  
   isConfigured:boolean,
}
}

   /** Required : 
      @param ds
      @param CopyAction
      @param UpdateComments
      @param SourceConfigID
      @param SourcePartNum
      @param SourceRevisionNum
      @param SourceAltMethod
      @param TargetPartNum
      @param TargetRevisionNum
      @param TargetAltMethod
   */  
export interface CopyMethodRules_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
      /**  Append or Replace  */  
   CopyAction:string,
      /**  Update comments  */  
   UpdateComments:boolean,
      /**  Source ConfigID  */  
   SourceConfigID:string,
      /**  Source Part Num  */  
   SourcePartNum:string,
      /**  Source Revision Num  */  
   SourceRevisionNum:string,
      /**  Source Alternate Method  */  
   SourceAltMethod:string,
      /**  Source Part Num  */  
   TargetPartNum:string,
      /**  Source Revision Num  */  
   TargetRevisionNum:string,
      /**  Source Alternate Method  */  
   TargetAltMethod:string,
}

export interface CopyMethodRules_output{
   returnObj:Erp_Tablesets_CopyRulesResultsTableset[],
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface DeleteByID_input{
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param type
      @param configID
      @param partNum
      @param revisionNum
      @param altMethod
      @param ruleSetID
   */  
export interface EditorFilter_input{
      /**  Indicates if will be for session filter or for ColumnFilter  */  
   type:string,
      /**  ConfigID  */  
   configID:string,
      /**  Part Num  */  
   partNum:string,
      /**  Revision Num  */  
   revisionNum:string,
      /**  AltMethod  */  
   altMethod:string,
      /**  RuleSetID  */  
   ruleSetID:number,
}

export interface EditorFilter_output{
   returnObj:string,
}

export interface Erp_Tablesets_CodeEditorPCDatasetTableset{
   CodeEditorPCTargets:Erp_Tablesets_CodeEditorPCTargetsRow[],
   CodeEditorPCDocVars:Erp_Tablesets_CodeEditorPCDocVarsRow[],
   CodeEditorPCInputs:Erp_Tablesets_CodeEditorPCInputsRow[],
   CodeEditorPCMethodVars:Erp_Tablesets_CodeEditorPCMethodVarsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CodeEditorPCDocVarsRow{
   VarName:string,
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCInputsRow{
   InputName:string,
   InputType:string,
   DataType:string,
   PcDynLstCount:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCMethodVarsRow{
   VarName:string,
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCTargetsRow{
   Company:string,
   TableName:string,
   ColumnName:string,
      /**  Reserved for future development  */  
   ColumnFormat:string,
   ColumnSyntax:string,
      /**  Indicates if the column is from the UD table  */  
   UDColumn:boolean,
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfiguratorRuleListTableset{
   PartRevList:Erp_Tablesets_PartRevListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfiguratorRuleTableset{
   PartRev:Erp_Tablesets_PartRevRow[],
   PcMethodVar:Erp_Tablesets_PcMethodVarRow[],
   PcRuleSet:Erp_Tablesets_PcRuleSetRow[],
   PcRules:Erp_Tablesets_PcRulesRow[],
   PcRulesExpr:Erp_Tablesets_PcRulesExprRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CopyPcRuleSetRow{
   Description:string,
   Copied:boolean,
   BOMElementType:string,
   OprSeq:number,
   OpDtlSeq:number,
   MtlSeq:number,
   TotalRules:number,
   TotalActions:number,
   ID:string,
   Assembly:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CopyRulesResultsTableset{
   CopyPcRuleSet:Erp_Tablesets_CopyPcRuleSetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCRulesBOMTableset{
   PCRulesMtl:Erp_Tablesets_PCRulesMtlRow[],
   PcRulesOpDtl:Erp_Tablesets_PcRulesOpDtlRow[],
   PcRulesOpr:Erp_Tablesets_PcRulesOprRow[],
   PCRulesRev:Erp_Tablesets_PCRulesRevRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCRulesMtlRow{
   Company:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   MtlSeq:number,
   RelatedOperation:number,
   MtlPartNum:string,
   RuleTag:string,
   GeneratedRuleTag:string,
   OpDesc:string,
   MtlRevisionNum:string,
   PullAsAsm:boolean,
   ViewAsAsm:boolean,
   ParentRuleTag:string,
   AssemblySeq:number,
   HasRuleSet:boolean,
   KitComponent:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCRulesRevRow{
   Company:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   EffectiveDate:string,
   AltMethodDesc:string,
   RuleTag:string,
   ParentRuleTag:string,
   CurrentRevision:boolean,
   DispAltMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRevListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   RevShortDesc:string,
      /**  Used to enter a full description of the revision.  */  
   RevDescription:string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   Approved:boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   EffectiveDate:string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRSetupBurdenCost:number,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   ECO:string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   Configured:boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   WebConfigured:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  The description of the alternate method.  */  
   AltMethodDesc:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  External Configurator  */  
   ExtConfig:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Is the part for this revision a global part  */  
   PcGlobalPart:boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   PcEntprsConf:boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   GlobalRev:boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   RoughCutCode:string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   RMAInspPlan:string,
      /**  The specification ID to use for RMA processing for this part.  */  
   RMASpecID:string,
      /**  The default sample size to use for RMA processing for this part  */  
   RMASampleSize:number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   RMASampleSizePct:number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   BaseRevisionNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   vDate:string,
   vQty:number,
   ProdCode:string,
   NonStock:boolean,
   Class:string,
   ParentAltMethodDesc:string,
      /**  Name of ECO Group that this part is checked out to  */  
   ECOGroup:string,
   DisableApproved:boolean,
   SpecHedDescription:string,
      /**  The description of the inspection plan  */  
   InspPlanDescription:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartDescriptionPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartDescriptionTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartDescriptionIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartDescriptionSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartDescriptionTrackLots:boolean,
      /**  Describes the Part.  */  
   PartDescriptionPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartDescriptionSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartDescriptionTrackSerialNum:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Full description of the rough cut parameter set.  */  
   RoughCutParamDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRevRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   RevShortDesc:string,
      /**  Used to enter a full description of the revision.  */  
   RevDescription:string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   Approved:boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   EffectiveDate:string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRSetupBurdenCost:number,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   ECO:string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   Configured:boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   WebConfigured:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  The description of the alternate method.  */  
   AltMethodDesc:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  External Configurator  */  
   ExtConfig:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Is the part for this revision a global part  */  
   PcGlobalPart:boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   PcEntprsConf:boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   GlobalRev:boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   RoughCutCode:string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   RMAInspPlan:string,
      /**  The specification ID to use for RMA processing for this part.  */  
   RMASpecID:string,
      /**  The default sample size to use for RMA processing for this part  */  
   RMASampleSize:number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   RMASampleSizePct:number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   BaseRevisionNum:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  RegenConfig  */  
   RegenConfig:boolean,
      /**  SIValuesGroupSeq  */  
   SIValuesGroupSeq:number,
      /**  SIValuesHeadNum  */  
   SIValuesHeadNum:number,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   ProcessMode:string,
      /**  DefaultConfigPart  */  
   DefaultConfigPart:boolean,
      /**  Number of COPart required in the Revision  */  
   CoPartsReqQty:number,
      /**  Material Cost Factor  */  
   MtlCostPct:number,
      /**  Labor Cost Factor  */  
   LaborCostPct:number,
      /**  Number of COParts per Operation  */  
   CoPartsPerOp:number,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Customs BOM  */  
   CNCustomsBOM:boolean,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Type of Process Manufacturing this revision is for: General, Site, Master.  */  
   ProcessMfgType:string,
      /**  Description of Process Manufacturing revision.  */  
   ProcessMfgDescription:string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  The last Group to modify this Revision for Recipe Authoring.  */  
   ProcessMfgLastGroupID:string,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   ECPCEnabled:boolean,
   DisableApproved:boolean,
      /**  Name of ECO Group that this part is checked out to  */  
   ECOGroup:string,
      /**  This field will be set to true if two or more ECOCoParts records exist for the revision.  */  
   HasCoParts:boolean,
   ParentAltMethodDesc:string,
      /**  Part Number of the Parent Part  */  
   ParentPartNum:string,
      /**  Revision number  of Parent Part.  */  
   ParentRevisionNum:string,
   ProdCode:string,
      /**   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  */  
   RevStatusAsOfDate:number,
   SpecHedDescription:string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   vDate:string,
   vQty:number,
   Class:string,
   NonStock:boolean,
      /**  Indicates that the PartRev is the root node in the tree  */  
   IsRootNode:boolean,
      /**  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  */  
   EngineeringApproved:boolean,
   BitFlag:number,
   InspPlanDescription:string,
   PartDescriptionTrackDimension:boolean,
   PartDescriptionSellingFactor:number,
   PartDescriptionPartDescription:string,
   PartDescriptionIUM:string,
   PartDescriptionTrackLots:boolean,
   PartDescriptionPricePerCode:string,
   PartDescriptionSalesUM:string,
   PartDescriptionTrackSerialNum:boolean,
   PartDescriptionTypeCode:string,
   PcStatusConfigType:string,
   PlantName:string,
   RoughCutParamDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcMethodVarRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  PartNum  */  
   PartNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  AltMethod  */  
   AltMethod:string,
      /**  VarNum  */  
   VarNum:number,
      /**  VarName  */  
   VarName:string,
      /**  DataType  */  
   DataType:string,
      /**  Expression  */  
   Expression:string,
      /**  ExprType  */  
   ExprType:string,
      /**  VarSeq  */  
   VarSeq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Temporal column to show link phrase  */  
   DispLinkString:string,
   Format:string,
   CanUpdate:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRuleSetRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  PartNum  */  
   PartNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  AltMethod  */  
   AltMethod:string,
      /**  RuleSetID  */  
   RuleSetID:number,
      /**  BOMElementSysRowID  */  
   BOMElementSysRowID:string,
      /**  BOMElementTableName  */  
   BOMElementTableName:string,
      /**  BOMElementType  */  
   BOMElementType:string,
      /**  RuleTag  */  
   RuleTag:string,
      /**  MtlSeq  */  
   MtlSeq:number,
      /**  OprSeq  */  
   OprSeq:number,
      /**  OpDtlSeq  */  
   OpDtlSeq:number,
      /**  UseKeepWhen  */  
   UseKeepWhen:boolean,
      /**  KeepWhenExpr  */  
   KeepWhenExpr:string,
      /**  KeepWhenLValue  */  
   KeepWhenLValue:string,
      /**  KeepWhenCompareOpr  */  
   KeepWhenCompareOpr:string,
      /**  KeepWhenRValue  */  
   KeepWhenRValue:string,
      /**  KeepWhenRValueType  */  
   KeepWhenRValueType:string,
      /**  KeepWhenType  */  
   KeepWhenType:string,
      /**  ExtCompanyList  */  
   ExtCompanyList:string,
      /**  Comments  */  
   Comments:string,
      /**  Expression  */  
   Expression:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates if is allowed Enterprise Configuration  */  
   EntprsConf:boolean,
   KeepWhenField:string,
   KeepWhenTable:string,
      /**  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  */  
   MultiCompany:boolean,
   AsmPartNum:string,
      /**  If is Enterprise configuration allowed it will update if is Local Company or MultiCompany  */  
   CompanyName:string,
   CanUpdate:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRulesExprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  The sequence the rule is going to be applied.  */  
   RuleSeq:number,
      /**  Operation Sequence Number  */  
   OprSeq:number,
      /**  Material Sequence Number  */  
   MtlSeq:number,
      /**  Stores the parent part number within the multi-level BOM for which the rule is related.  */  
   ParPartNum:string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   AsmPartNum:string,
      /**  Alternate Routing method to be used for this rule.  */  
   AltMethod:string,
      /**  Uniquely identifies an OpDtl  */  
   OpDtlSeq:number,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  Method Rule Expression  */  
   Expression:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ProcessOrder  */  
   ProcessOrder:number,
      /**  RuleSetID  */  
   RuleSetID:number,
      /**  ExprType  */  
   ExprType:string,
      /**  LValue  */  
   LValue:string,
      /**  CompareOpr  */  
   CompareOpr:string,
      /**  RValue  */  
   RValue:string,
      /**  RValueType  */  
   RValueType:string,
      /**  ExprXMLItem  */  
   ExprXMLItem:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DispActionString:string,
   BOMElementSysRowID:string,
   BOMElementTableName:string,
   RuleTag:string,
      /**  Assing the default format for the constant editor  */  
   Format:string,
   dbField:string,
   dbTable:string,
   CanUpdate:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRulesOpDtlRow{
   Company:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   OprSeq:number,
   OpDtlSeq:number,
   OpDtlDesc:string,
   RuleTag:string,
   ParentRuleTag:string,
   HasRuleSet:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRulesOprRow{
   Company:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   OprSeq:number,
   OpCode:string,
   SubContract:boolean,
   OpDesc:string,
   RuleTag:string,
   ParentRuleTag:string,
   HasRuleSet:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRulesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  The sequence the rule is going to be applied.  */  
   RuleSeq:number,
      /**  Method Rule String  */  
   RuleString:string,
      /**  Method Rule Type  */  
   RuleType:string,
      /**  Method Rule Expression  */  
   RuleExpr:string,
      /**  Name for the calculated field  */  
   CalcName:string,
      /**  Calculated field data type  */  
   CalcDataType:string,
      /**  Database Field  */  
   dbField:string,
      /**  Database Table  */  
   dbTable:string,
      /**  Operation Sequence Number  */  
   OprSeq:number,
      /**  Material Sequence Number  */  
   MtlSeq:number,
      /**  Stores the parent part number within the multi-level BOM for which the rule is related.  */  
   ParPartNum:string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   AsmPartNum:string,
      /**  Defines what the rule is related to.  Valid values include Par, Opr, Mtl, Asm.  This is used in Gencode.p when creating the compiled code.  */  
   ElementType:string,
      /**  Alternate Routing method to be used for this rule.  */  
   AltMethod:string,
      /**  A unique identifier for the rule.  This will be generated in the database trigger.  */  
   RuleID:number,
      /**  Uniquely identifies an OpDtl  */  
   OpDtlSeq:number,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  Comments  */  
   Comments:string,
      /**  Rule Tag  */  
   RuleTag:string,
      /**  Process Sequence  */  
   ProcessSeq:number,
      /**  LValue  */  
   LValue:string,
      /**  CompareOpr  */  
   CompareOpr:string,
      /**  RValue  */  
   RValue:string,
      /**  RValueType  */  
   RValueType:string,
      /**  RuleSetID  */  
   RuleSetID:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CanUpdate:boolean,
      /**  The node that is currently selected in the tree.  */  
   CurrentNode:string,
   CurrentRuleLineage:string,
      /**  The parent node of the current node that is selected in the tree  */  
   ParentNode:string,
   BOMElementTableName:string,
   BOMElementSysRowID:string,
      /**  Assing the default format for the constant editor  */  
   Format:string,
      /**  Temporal column to show link phrase  */  
   DispLinkString:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtConfiguratorRuleTableset{
   PartRev:Erp_Tablesets_PartRevRow[],
   PcMethodVar:Erp_Tablesets_PcMethodVarRow[],
   PcRuleSet:Erp_Tablesets_PcRuleSetRow[],
   PcRules:Erp_Tablesets_PcRulesRow[],
   PcRulesExpr:Erp_Tablesets_PcRulesExprRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
      @param ipSingLevelConf
      @param lastNodeKey
   */  
export interface GetAllAlternateTrees_input{
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  If BOM will retrieve only first level  */  
   ipSingLevelConf:boolean,
      /**  Correspond to the path from the last element selected in TreeView  */  
   lastNodeKey:string,
}

export interface GetAllAlternateTrees_output{
   returnObj:Erp_Tablesets_PCRulesBOMTableset[],
}

   /** Required : 
      @param configID
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface GetAvailMethodVariables_input{
      /**  The configuration ID  */  
   configID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
}

export interface GetAvailMethodVariables_output{
parameters : {
      /**  output parameters  */  
   availMethodVars:string,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetByID_input{
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConfiguratorRuleTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConfiguratorRuleTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConfiguratorRuleTableset[],
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
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipRuleTag
      @param ipSingLevelConf
      @param ipConfigId
      @param ipMainPartNum
      @param ipMainRevisionNum
      @param ipMainAltMethod
      @param ds
   */  
export interface GetDatasetForTree_input{
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  if is the main revision or alternate revision will not have any ruletag only for materials  */  
   ipRuleTag:string,
      /**  If BOM will retrieve only first level  */  
   ipSingLevelConf:boolean,
      /**  Main ConfigID to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  */  
   ipConfigId:string,
      /**  Main PartNum to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  */  
   ipMainPartNum:string,
      /**  Main RevisionNum to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  */  
   ipMainRevisionNum:string,
      /**  Main AltMethod to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  */  
   ipMainAltMethod:string,
   ds:Erp_Tablesets_PCRulesBOMTableset[],
}

export interface GetDatasetForTree_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCRulesBOMTableset,
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
   returnObj:Erp_Tablesets_ConfiguratorRuleListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface GetNewPartRev_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
   partNum:string,
   revisionNum:string,
   altMethod:string,
}

export interface GetNewPartRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
      @param configID
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface GetNewPcMethodVar_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
   configID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
}

export interface GetNewPcMethodVar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
      @param configID
      @param partNum
      @param revisionNum
      @param altMethod
      @param boMElementTableName
      @param boMElementSysRowID
      @param ruleTag
   */  
export interface GetNewPcRuleSet_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
   configID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   boMElementTableName:string,
   boMElementSysRowID:string,
   ruleTag:string,
}

export interface GetNewPcRuleSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
      @param configID
      @param partNum
      @param revisionNum
      @param altMethod
      @param ruleSetID
      @param ruleSeq
      @param typeCode
   */  
export interface GetNewPcRulesExpr_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
   configID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   ruleSetID:number,
   ruleSeq:number,
   typeCode:string,
}

export interface GetNewPcRulesExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
      @param configID
      @param partNum
      @param revisionNum
      @param altMethod
      @param ruleSetID
   */  
export interface GetNewPcRules_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
   configID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   ruleSetID:number,
}

export interface GetNewPcRules_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param configID
   */  
export interface GetPrimaryPartNum_input{
      /**  Configuration ID  */  
   configID:string,
}

export interface GetPrimaryPartNum_output{
      /**  The Part Number is returned  */  
   returnObj:string,
}

   /** Required : 
      @param whereClausePartRev
      @param whereClausePcMethodVar
      @param whereClausePcRuleSet
      @param whereClausePcRules
      @param whereClausePcRulesExpr
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartRev:string,
   whereClausePcMethodVar:string,
   whereClausePcRuleSet:string,
   whereClausePcRules:string,
   whereClausePcRulesExpr:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConfiguratorRuleTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param configID
      @param targetEntityFilter
      @param filteredColumnList
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface GetValidTargetEntitiesAndInputs_input{
   configID:string,
   targetEntityFilter:string,
   filteredColumnList:boolean,
      /**  Part Number  */  
   partNum:string,
      /**  Revision Numerb  */  
   revisionNum:string,
      /**  Alternate method  */  
   altMethod:string,
}

export interface GetValidTargetEntitiesAndInputs_output{
   returnObj:Erp_Tablesets_CodeEditorPCDatasetTableset[],
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
      @param PcMethodVarRowid
      @param ds
   */  
export interface MethodVarMoveDown_input{
      /**  The RowIdent of the rule to be moved down  */  
   PcMethodVarRowid:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface MethodVarMoveDown_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param PcMethodVarRowid
      @param ds
   */  
export interface MethodVarMoveUp_input{
      /**  The RowIdent of the rule to be moved up  */  
   PcMethodVarRowid:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface MethodVarMoveUp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param PartNum
      @param configID
   */  
export interface OnChangePartNum_input{
      /**  Part Num field  */  
   PartNum:string,
      /**  Configuration ID  */  
   configID:string,
}

export interface OnChangePartNum_output{
      /**  if exists PartNum  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   outPartNum:string,
}
}

   /** Required : 
      @param newValue
      @param ds
   */  
export interface OnChangePcRulesExprLValue_input{
      /**  New value for LValue column  */  
   newValue:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangePcRulesExprLValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param newValue
      @param ds
   */  
export interface OnChangePcRulesLValue_input{
      /**  New value for LValue column  */  
   newValue:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangePcRulesLValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param altMethod
      @param configID
   */  
export interface OnChangedConfigID_input{
      /**  Part Num  */  
   partNum:string,
      /**  Revision Num  */  
   revisionNum:string,
      /**  Alt Method  */  
   altMethod:string,
      /**  proposed ConfigID  */  
   configID:string,
}

export interface OnChangedConfigID_output{
}

   /** Required : 
      @param newDataType
      @param ds
   */  
export interface OnChangedPcMethodVarDataType_input{
      /**  New DataType  */  
   newDataType:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangedPcMethodVarDataType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedPcMethodVarExprType_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangedPcMethodVarExprType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedPcRulesExprExprType_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangedPcRulesExprExprType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedPcRulesRuleType_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangedPcRulesRuleType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param multiCompany
      @param ds
   */  
export interface OnChangedRuleSetCompany_input{
      /**  Indicate if is multi company  */  
   multiCompany:boolean,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangedRuleSetCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param newDataType
      @param ds
   */  
export interface OnChangingPcMethodVarDataType_input{
      /**  New Data Type  */  
   newDataType:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangingPcMethodVarDataType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param newVarName
      @param ds
   */  
export interface OnChangingPcMethodVarVarName_input{
      /**  New DataType  */  
   newVarName:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface OnChangingPcMethodVarVarName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ipConfigID
   */  
export interface PromptForPassword_input{
      /**  Configuration ID of the revisions being synched.  */  
   ipConfigID:string,
}

export interface PromptForPassword_output{
parameters : {
      /**  output parameters  */  
   opPromptForPassword:boolean,
   opRevisionStatus:boolean,
   opRevisionFound:boolean,
}
}

   /** Required : 
      @param PcRulesRowid
      @param ds
   */  
export interface RulesMoveDown_input{
      /**  The RowIdent of the rule to be moved down  */  
   PcRulesRowid:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface RulesMoveDown_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param PcRulesRowid
      @param ds
   */  
export interface RulesMoveUp_input{
      /**  The RowIdent of the rule to be moved up  */  
   PcRulesRowid:string,
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface RulesMoveUp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param PcPartNum
   */  
export interface SalesKitConfiguration_input{
      /**  The current part number  */  
   PcPartNum:string,
}

export interface SalesKitConfiguration_output{
parameters : {
      /**  output parameters  */  
   SalesKit:boolean,
}
}

   /** Required : 
      @param ipApproved
      @param ipValidPassword
      @param ipConfigID
      @param ipAuditDesc
   */  
export interface SyncRevision_input{
      /**  The proposed approval flag  */  
   ipApproved:boolean,
      /**  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method
            in the UserFile BO.  */  
   ipValidPassword:boolean,
      /**  The configurator ID of the revisions to synchronize  */  
   ipConfigID:string,
      /**  The audit description entered for the configuration approval  */  
   ipAuditDesc:string,
}

export interface SyncRevision_output{
parameters : {
      /**  output parameters  */  
   revSynched:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConfiguratorRuleTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConfiguratorRuleTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidatePcRulesDelete_input{
   ds:Erp_Tablesets_ConfiguratorRuleTableset[],
}

export interface ValidatePcRulesDelete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorRuleTableset,
   outMsgDeletion:string,
}
}

   /** Required : 
      @param CurrConfigID
      @param PartNum
      @param RevisionNum
      @param AltMethod
   */  
export interface ValidateRevisionNum_input{
   CurrConfigID:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
}

export interface ValidateRevisionNum_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   CurrConfigID:string,
   typeMessage:number,
}
}

