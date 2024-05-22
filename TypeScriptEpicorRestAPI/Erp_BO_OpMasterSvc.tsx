import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.OpMasterSvc
// Description: Production operation codes master file.
DELETE: Not allowed if referenced in  JobOper, OpStd or BomOper files.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/$metadata", {
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
   Description: Get OpMasters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasters
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterRow
   */  
export function get_OpMasters(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasters(requestBody:Erp_Tablesets_OpMasterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMaster item
   Description: Calls GetByID to retrieve the OpMaster item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMaster
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterRow
   */  
export function get_OpMasters_Company_OpCode(Company:string, OpCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMaster for the service
   Description: Calls UpdateExt to update OpMaster. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMaster
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasters_Company_OpCode(Company:string, OpCode:string, requestBody:Erp_Tablesets_OpMasterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")", {
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
   Summary: Call UpdateExt to delete OpMaster item
   Description: Call UpdateExt to delete OpMaster item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMaster
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasters_Company_OpCode(Company:string, OpCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")", {
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
   Description: Get OpMasRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasRestrictions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictionRow
   */  
export function get_OpMasters_Company_OpCode_OpMasRestrictions(Company:string, OpCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasRestrictions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OpMasRestriction item
   Description: Calls GetByID to retrieve the OpMasRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestriction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   */  
export function get_OpMasters_Company_OpCode_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company:string, OpCode:string, RestrictionTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")", {
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
         resolve(data as Erp_Tablesets_OpMasRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get OpMasterActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterActions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionRow
   */  
export function get_OpMasters_Company_OpCode_OpMasterActions(Company:string, OpCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterActions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OpMasterAction item
   Description: Calls GetByID to retrieve the OpMasterAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterActionRow
   */  
export function get_OpMasters_Company_OpCode_OpMasterActions_Company_OpCode_ActionSeq(Company:string, OpCode:string, ActionSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get OpMasterInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterInsps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterInspRow
   */  
export function get_OpMasters_Company_OpCode_OpMasterInsps(Company:string, OpCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterInsps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OpMasterInsp item
   Description: Calls GetByID to retrieve the OpMasterInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterInsp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterInspRow
   */  
export function get_OpMasters_Company_OpCode_OpMasterInsps_Company_OpCode_PlanSeq(Company:string, OpCode:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get OpMasDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasDtlRow
   */  
export function get_OpMasters_Company_OpCode_OpMasDtls(Company:string, OpCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OpMasDtl item
   Description: Calls GetByID to retrieve the OpMasDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasDtlRow
   */  
export function get_OpMasters_Company_OpCode_OpMasDtls_Company_OpCode_OpDtlSeq(Company:string, OpCode:string, OpDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get OpMasterAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterAttchRow
   */  
export function get_OpMasters_Company_OpCode_OpMasterAttches(Company:string, OpCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OpMasterAttch item
   Description: Calls GetByID to retrieve the OpMasterAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterAttchRow
   */  
export function get_OpMasters_Company_OpCode_OpMasterAttches_Company_OpCode_DrawingSeq(Company:string, OpCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get OpMasRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasRestrictions
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictionRow
   */  
export function get_OpMasRestrictions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasRestrictions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasRestrictions(requestBody:Erp_Tablesets_OpMasRestrictionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMasRestriction item
   Description: Calls GetByID to retrieve the OpMasRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   */  
export function get_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company:string, OpCode:string, RestrictionTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")", {
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
         resolve(data as Erp_Tablesets_OpMasRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMasRestriction for the service
   Description: Calls UpdateExt to update OpMasRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company:string, OpCode:string, RestrictionTypeID:string, requestBody:Erp_Tablesets_OpMasRestrictionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")", {
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
   Summary: Call UpdateExt to delete OpMasRestriction item
   Description: Call UpdateExt to delete OpMasRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company:string, OpCode:string, RestrictionTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")", {
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
   Description: Get OpMasRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasRestrictSubsts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictSubstRow
   */  
export function get_OpMasRestrictions_Company_OpCode_RestrictionTypeID_OpMasRestrictSubsts(Company:string, OpCode:string, RestrictionTypeID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")/OpMasRestrictSubsts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OpMasRestrictSubst item
   Description: Calls GetByID to retrieve the OpMasRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestrictSubst1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   */  
export function get_OpMasRestrictions_Company_OpCode_RestrictionTypeID_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company:string, OpCode:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
         resolve(data as Erp_Tablesets_OpMasRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get OpMasRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasRestrictSubsts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictSubstRow
   */  
export function get_OpMasRestrictSubsts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasRestrictSubsts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasRestrictSubsts(requestBody:Erp_Tablesets_OpMasRestrictSubstRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMasRestrictSubst item
   Description: Calls GetByID to retrieve the OpMasRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   */  
export function get_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company:string, OpCode:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
         resolve(data as Erp_Tablesets_OpMasRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMasRestrictSubst for the service
   Description: Calls UpdateExt to update OpMasRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company:string, OpCode:string, RestrictionTypeID:string, SubstanceID:string, requestBody:Erp_Tablesets_OpMasRestrictSubstRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
   Summary: Call UpdateExt to delete OpMasRestrictSubst item
   Description: Call UpdateExt to delete OpMasRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company:string, OpCode:string, RestrictionTypeID:string, SubstanceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
   Description: Get OpMasterActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterActions
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionRow
   */  
export function get_OpMasterActions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterActions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasterActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasterActions(requestBody:Erp_Tablesets_OpMasterActionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMasterAction item
   Description: Calls GetByID to retrieve the OpMasterAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterActionRow
   */  
export function get_OpMasterActions_Company_OpCode_ActionSeq(Company:string, OpCode:string, ActionSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMasterAction for the service
   Description: Calls UpdateExt to update OpMasterAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasterActions_Company_OpCode_ActionSeq(Company:string, OpCode:string, ActionSeq:string, requestBody:Erp_Tablesets_OpMasterActionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")", {
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
   Summary: Call UpdateExt to delete OpMasterAction item
   Description: Call UpdateExt to delete OpMasterAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasterActions_Company_OpCode_ActionSeq(Company:string, OpCode:string, ActionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")", {
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
   Description: Get OpMasterActionParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterActionParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionParamRow
   */  
export function get_OpMasterActions_Company_OpCode_ActionSeq_OpMasterActionParams(Company:string, OpCode:string, ActionSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")/OpMasterActionParams", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OpMasterActionParam item
   Description: Calls GetByID to retrieve the OpMasterActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterActionParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   */  
export function get_OpMasterActions_Company_OpCode_ActionSeq_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company:string, OpCode:string, ActionSeq:string, ActionParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get OpMasterActionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterActionParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionParamRow
   */  
export function get_OpMasterActionParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterActionParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasterActionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasterActionParams(requestBody:Erp_Tablesets_OpMasterActionParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMasterActionParam item
   Description: Calls GetByID to retrieve the OpMasterActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   */  
export function get_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company:string, OpCode:string, ActionSeq:string, ActionParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMasterActionParam for the service
   Description: Calls UpdateExt to update OpMasterActionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company:string, OpCode:string, ActionSeq:string, ActionParamSeq:string, requestBody:Erp_Tablesets_OpMasterActionParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")", {
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
   Summary: Call UpdateExt to delete OpMasterActionParam item
   Description: Call UpdateExt to delete OpMasterActionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company:string, OpCode:string, ActionSeq:string, ActionParamSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")", {
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
   Description: Get OpMasterInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterInsps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterInspRow
   */  
export function get_OpMasterInsps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterInsps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasterInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasterInsps(requestBody:Erp_Tablesets_OpMasterInspRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMasterInsp item
   Description: Calls GetByID to retrieve the OpMasterInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterInspRow
   */  
export function get_OpMasterInsps_Company_OpCode_PlanSeq(Company:string, OpCode:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMasterInsp for the service
   Description: Calls UpdateExt to update OpMasterInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasterInsps_Company_OpCode_PlanSeq(Company:string, OpCode:string, PlanSeq:string, requestBody:Erp_Tablesets_OpMasterInspRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")", {
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
   Summary: Call UpdateExt to delete OpMasterInsp item
   Description: Call UpdateExt to delete OpMasterInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasterInsps_Company_OpCode_PlanSeq(Company:string, OpCode:string, PlanSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")", {
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
   Description: Get OpMasDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasDtlRow
   */  
export function get_OpMasDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasDtls(requestBody:Erp_Tablesets_OpMasDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMasDtl item
   Description: Calls GetByID to retrieve the OpMasDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasDtlRow
   */  
export function get_OpMasDtls_Company_OpCode_OpDtlSeq(Company:string, OpCode:string, OpDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMasDtl for the service
   Description: Calls UpdateExt to update OpMasDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasDtls_Company_OpCode_OpDtlSeq(Company:string, OpCode:string, OpDtlSeq:string, requestBody:Erp_Tablesets_OpMasDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete OpMasDtl item
   Description: Call UpdateExt to delete OpMasDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasDtls_Company_OpCode_OpDtlSeq(Company:string, OpCode:string, OpDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")", {
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
   Description: Get OpMasterAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterAttchRow
   */  
export function get_OpMasterAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OpMasterAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpMasterAttches(requestBody:Erp_Tablesets_OpMasterAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the OpMasterAttch item
   Description: Calls GetByID to retrieve the OpMasterAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OpMasterAttchRow
   */  
export function get_OpMasterAttches_Company_OpCode_DrawingSeq(Company:string, OpCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OpMasterAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_OpMasterAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OpMasterAttch for the service
   Description: Calls UpdateExt to update OpMasterAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OpMasterAttches_Company_OpCode_DrawingSeq(Company:string, OpCode:string, DrawingSeq:string, requestBody:Erp_Tablesets_OpMasterAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete OpMasterAttch item
   Description: Call UpdateExt to delete OpMasterAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OpMasterAttches_Company_OpCode_DrawingSeq(Company:string, OpCode:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterListRow)
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
export function get_GetRows(whereClauseOpMaster:string, whereClauseOpMasterAttch:string, whereClauseOpMasRestriction:string, whereClauseOpMasRestrictSubst:string, whereClauseOpMasterAction:string, whereClauseOpMasterActionParam:string, whereClauseOpMasterInsp:string, whereClauseOpMasDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseOpMaster!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMaster=" + whereClauseOpMaster
   }
   if(typeof whereClauseOpMasterAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMasterAttch=" + whereClauseOpMasterAttch
   }
   if(typeof whereClauseOpMasRestriction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMasRestriction=" + whereClauseOpMasRestriction
   }
   if(typeof whereClauseOpMasRestrictSubst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMasRestrictSubst=" + whereClauseOpMasRestrictSubst
   }
   if(typeof whereClauseOpMasterAction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMasterAction=" + whereClauseOpMasterAction
   }
   if(typeof whereClauseOpMasterActionParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMasterActionParam=" + whereClauseOpMasterActionParam
   }
   if(typeof whereClauseOpMasterInsp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMasterInsp=" + whereClauseOpMasterInsp
   }
   if(typeof whereClauseOpMasDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOpMasDtl=" + whereClauseOpMasDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetRows" + params, {
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
export function get_GetByID(opCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof opCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "opCode=" + opCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetByID" + params, {
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
   Summary: Invoke method ChangedCharacteristicAttrClassID
   Description: Method that is called when the Characteristic Attribute ID is changed.
   OperationID: ChangedCharacteristicAttrClassID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedCharacteristicAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCharacteristicAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedCharacteristicAttrClassID(requestBody:ChangedCharacteristicAttrClassID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedCharacteristicAttrClassID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangedCharacteristicAttrClassID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedCharacteristicAttrClassID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCapabilityID
   Description: Method to call when changing the Capability ID. Blank is a valid entry for Capability ID.
   OperationID: ChangeCapabilityID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCapabilityID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapabilityID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCapabilityID(requestBody:ChangeCapabilityID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCapabilityID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeCapabilityID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCapabilityID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpMasRestrictionType
   Description: This methods assigns associated fields when OpMasRestriction.RestrictionTypeID changes.
   OperationID: ChangeOpMasRestrictionType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOpMasRestrictionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasRestrictionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpMasRestrictionType(requestBody:ChangeOpMasRestrictionType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOpMasRestrictionType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeOpMasRestrictionType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOpMasRestrictionType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpMasRestrictSubstance
   Description: This methods assigns associated fields when OpMasRestrictSubst.SubstanceID changes.
   OperationID: ChangeOpMasRestrictSubstance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOpMasRestrictSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasRestrictSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpMasRestrictSubstance(requestBody:ChangeOpMasRestrictSubstance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOpMasRestrictSubstance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeOpMasRestrictSubstance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOpMasRestrictSubstance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpMasterPrimaryProdOpDtl
   Description: This method checks if the entered primary production operation detail is valid.
This method should run when the OpMaster.ScrPrimaryProdOpDtl field changes.
   OperationID: ChangeOpMasterPrimaryProdOpDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOpMasterPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasterPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpMasterPrimaryProdOpDtl(requestBody:ChangeOpMasterPrimaryProdOpDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOpMasterPrimaryProdOpDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeOpMasterPrimaryProdOpDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOpMasterPrimaryProdOpDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOpMasterPrimarySetupOpDtl
   Description: This method checks if the entered primary setup operation detail is valid.
This method should run when the OpMaster.ScrPrimarySetupOpDtl field changes.
   OperationID: ChangeOpMasterPrimarySetupOpDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOpMasterPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasterPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOpMasterPrimarySetupOpDtl(requestBody:ChangeOpMasterPrimarySetupOpDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOpMasterPrimarySetupOpDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeOpMasterPrimarySetupOpDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOpMasterPrimarySetupOpDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeResourceGrpID
   Description: Method to call when changing the Resource Group ID.  This method will update OpMasDtl
with the default labor and burden rates from the new resource group.  Blank is a valid
entry for Resource Group ID.
   OperationID: ChangeResourceGrpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeResourceGrpID(requestBody:ChangeResourceGrpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeResourceGrpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeResourceGrpID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeResourceGrpID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeResourceID
   Description: Method to call when changing the Resource ID.  Blank is a valid entry for Resource ID.
   OperationID: ChangeResourceID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeResourceID(requestBody:ChangeResourceID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeResourceID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeResourceID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeResourceID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendorNumVendorID
   Description: Method to call when changing the Vendor Num. Blank is a valid entry for Vendor Num.
   OperationID: ChangeVendorNumVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendorNumVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorNumVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorNumVendorID(requestBody:ChangeVendorNumVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendorNumVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ChangeVendorNumVendorID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendorNumVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckInactiveSchedRequirement
   Description: Method to call check the capability, resource group, or resource is active.
This method should be called prior to calling the Update method on an OpMasDtl record.
Will return message text to present to the user if the code is inactive.  The
message is asking the user if it is OK to save the record with an inactive code.
If the user answers yes, the record can be saved.  If a blank value is returned
for InactiveMessage, continue as normal - no special processing needs to occur.
   OperationID: CheckInactiveSchedRequirement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckInactiveSchedRequirement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInactiveSchedRequirement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckInactiveSchedRequirement(requestBody:CheckInactiveSchedRequirement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckInactiveSchedRequirement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/CheckInactiveSchedRequirement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckInactiveSchedRequirement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDandOpType
   Description: A variation of the standard GetByID. Gets a OpMaster for a specific OpCode with consideration of OpType(s).
Note OpType is a comma separated list of Operation types to be considered valid for this Get.
Used as a predecessor to calling GetByID.
   OperationID: GetByIDandOpType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDandOpType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDandOpType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDandOpType(requestBody:GetByIDandOpType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDandOpType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetByIDandOpType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByIDandOpType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetProjectRoles
   OperationID: GetProjectRoles
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectRoles_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProjectRoles(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetProjectRoles_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetProjectRoles", {
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
         resolve(data as GetProjectRoles_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertCapability
   Description: This methods allows for the insertion of Capability on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertCapability
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InsertCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertCapability(requestBody:InsertCapability_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InsertCapability_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/InsertCapability", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InsertCapability_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertResource
   Description: This methods allows for the insertion of Resource on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InsertResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertResource(requestBody:InsertResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InsertResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/InsertResource", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InsertResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InsertResourceGroup
   Description: This methods allows for the insertion of Resource Group on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertResourceGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InsertResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertResourceGroup(requestBody:InsertResourceGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InsertResourceGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/InsertResourceGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InsertResourceGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasDtlForOPMasDtlType
   Description: This method overrides the original GetNewOpMasDtl and populates the OpMasDtlType with the given argument.
   OperationID: GetNewOpMasDtlForOPMasDtlType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasDtlForOPMasDtlType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasDtlForOPMasDtlType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasDtlForOPMasDtlType(requestBody:GetNewOpMasDtlForOPMasDtlType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasDtlForOPMasDtlType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasDtlForOPMasDtlType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasDtlForOPMasDtlType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInspection(requestBody:ValidateInspection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateInspection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/ValidateInspection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateInspection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   OperationID: GetIfCurrentSiteHasExternalMES
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIfCurrentSiteHasExternalMES(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetIfCurrentSiteHasExternalMES_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetIfCurrentSiteHasExternalMES", {
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
         resolve(data as GetIfCurrentSiteHasExternalMES_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnterpriseGetList
   Description: Will invoke GetList or perform the Enterprise Search when enterpriseSearchText / enterpriseBAQID is provided
   OperationID: EnterpriseGetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EnterpriseGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnterpriseGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnterpriseGetList(requestBody:EnterpriseGetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EnterpriseGetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/EnterpriseGetList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as EnterpriseGetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingActionSeq
   Description: Performs validation an change of the Action sequence and syncs the child Action Parameter sequence
   OperationID: OnChangingActionSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingActionSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingActionSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingActionSeq(requestBody:OnChangingActionSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingActionSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OnChangingActionSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingActionSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingActionParamSeq
   Description: Performs validation an change of the Action Parameter sequence
   OperationID: OnChangingActionParamSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingActionParamSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingActionParamSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingActionParamSeq(requestBody:OnChangingActionParamSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingActionParamSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OnChangingActionParamSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingActionParamSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMaster
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMaster
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMaster(requestBody:GetNewOpMaster_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMaster_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMaster_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasterAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasterAttch(requestBody:GetNewOpMasterAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasterAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasterAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasterAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasRestriction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasRestriction(requestBody:GetNewOpMasRestriction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasRestriction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasRestriction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasRestriction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasRestrictSubst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasRestrictSubst(requestBody:GetNewOpMasRestrictSubst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasRestrictSubst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasRestrictSubst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasRestrictSubst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasterAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterAction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasterAction(requestBody:GetNewOpMasterAction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasterAction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasterAction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasterAction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasterActionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterActionParam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterActionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterActionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasterActionParam(requestBody:GetNewOpMasterActionParam_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasterActionParam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasterActionParam", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasterActionParam_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasterInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterInsp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasterInsp(requestBody:GetNewOpMasterInsp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasterInsp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasterInsp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasterInsp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOpMasDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOpMasDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOpMasDtl(requestBody:GetNewOpMasDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOpMasDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetNewOpMasDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOpMasDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictSubstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasRestrictSubstRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasRestrictionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasterActionParamRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasterActionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasterAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterInspRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasterInspRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasterListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OpMasterRow,
}

export interface Erp_Tablesets_OpMasDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Cannot be blank.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   "OpDtlSeq":number,
      /**  Identifies which part of the production phase the resource is needed.   Valid values are "S", indicating the resource is required for the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   "SetupOrProd":string,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   "CapabilityID":string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  */  
   "ResourceID":string,
      /**  The standard setup hours for the operation.   This is the setup time required for each machine.  */  
   "SetupHours":number,
      /**  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  */  
   "ProdHours":number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   "NumResources":number,
      /**  Description is initially created when the OpMasDtl is created.   If the OpMasDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "OpDtlDesc":string,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   "ConcurrentCapacity":number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   "DailyProdRate":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Production Crew Size  */  
   "ProdCrewSize":number,
      /**  Setup Crew Size  */  
   "SetUpCrewSize":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrimaryProd  */  
   "PrimaryProd":boolean,
      /**  PrimarySetup  */  
   "PrimarySetup":boolean,
   "CapabilityDesc":string,
   "ResourceDesc":string,
   "ResourceGrpDesc":string,
   "SchedResourceDesc":string,
   "Location":boolean,
   "OPMasDtlType":string,
      /**  Resource Characteristic Attribute Class ID  */  
   "ResourceCharAttrClassID":string,
      /**  Resource Characteristic Attribute Set ID  */  
   "ResourceCharAttrSetID":number,
      /**  Resource SysRowID  */  
   "ResourceSysRowID":string,
      /**  Resource Group Characteristic Attribute Class ID  */  
   "ResourceGrpCharAttrClassID":string,
      /**  Resource Group Characteristic Attribute Set ID  */  
   "ResourceGrpCharAttrSetID":number,
      /**  Resource Group SysRowID  */  
   "ResourceGrpSysRowID":string,
   "BitFlag":number,
   "CapabilityIDDescription":string,
   "OpCodeOpDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OpMasRestrictSubstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  Substance identification.  */  
   "SubstanceID":string,
      /**  Default weight of the substance per primary part of UOM  */  
   "Weight":number,
      /**  By default the primary UOM of the part.  */  
   "WeightUOM":string,
      /**  When true then weight is disregarded in compliance roll-up.  */  
   "Manual":boolean,
      /**  The date when exempt status for this substance expires.  */  
   "ExemptDate":string,
      /**  Optional. Exemption certificate.  */  
   "ExemptCertificate":string,
      /**  Indicates if the Operation Restriction Substance is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  */  
   "Inactive":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Exempt":boolean,
   "BitFlag":number,
   "OpCodeOpDesc":string,
   "RestrictionTypeDescription":string,
   "SubstanceDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OpMasRestrictionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  */  
   "Manual":boolean,
      /**  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  */  
   "Compliance":string,
      /**  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  */  
   "ComplianceDate":string,
      /**  Indicates if the Operation Restriction Type is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  */  
   "Inactive":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Weight":boolean,
   "BitFlag":number,
   "OpCodeOpDesc":string,
   "RestrictionTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OpMasterActionParamRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identity of Operation master record.  */  
   "OpCode":string,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  A sequence number which uniquely identifies parameter within the Operation/Action set.  */  
   "ActionParamSeq":number,
      /**  ActionParamFieldDataType  */  
   "ActionParamFieldDataType":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueCharacter":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueDate":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueDecimal":number,
      /**  Value of Action Parameter.  */  
   "ActionParamValueInteger":number,
      /**  Value of Action Parameter.  */  
   "ActionParamValueLogical":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OpMasterActionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identity of Operation master record.  */  
   "OpCode":string,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  Description of Action.  */  
   "ActionDesc":string,
      /**  Indicates if this action must be completed before Operation can be completed.  */  
   "Required":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OpMasterAttchRow{
   "Company":string,
   "OpCode":string,
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

export interface Erp_Tablesets_OpMasterInspRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
      /**  A sequence number that uniquely identifies the PartOprInsp ecord within the Part operation  */  
   "PlanSeq":number,
      /**  The inspection plan part number (configurator part number).  */  
   "InspPlanPartNum":string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   "SpecID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SpecHedDescription":string,
   "BitFlag":number,
   "InspPlanDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OpMasterListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpDesc":string,
      /**  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  */  
   "BuyerID":string,
   "BuyerName":string,
      /**  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  */  
   "OPType":string,
   "AllowInCurPlant":boolean,
      /**  SubContract Operation  */  
   "Subcontract":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Operation has Characteristics  */  
   "HasCharacteristics":boolean,
      /**  Operations has some Actions.  */  
   "HasActions":boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   "CharacteristicAttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CharacteristicAttributeSetID":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OpMasterRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpDesc":string,
      /**  Key of the OpText record that is to be associated with this operation.  This is an optional field.  If entered it must be valid.  The purpose is that the OpText.Text data will be printed on the router after the operation detail.  The OpText is intended to be used for things such as creating inspection check off lines on the router.  */  
   "OpTextID":string,
      /**  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  */  
   "BuyerID":string,
      /**  Advanced Planning and Scheduling (eScheduling) preparatory operation flag.  A prep operation is usually a kitting operation.  Not used by the Manufacturing System scheduling module.  */  
   "APSPrepOpF":boolean,
      /**  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  */  
   "OPType":string,
      /**  FS - Editor widget for Operation comments.  */  
   "CommentText":string,
      /**  FS - Labor rate used for  time on an operation.  Time per hour per technician.  */  
   "BillLaborRate":number,
      /**  FS - The estimated Labor hours for the operation.  */  
   "EstLabHours":number,
      /**  Used to sort operations when load leveling by Op Code.  */  
   "SchedPrecedence":number,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  This key links the record to the Vendor file.  */  
   "VendorNum":number,
      /**  SubContract Operation  */  
   "Subcontract":boolean,
      /**   Indicates whether the expected production yield quantity should be changed based on actual production quantity and the PrdYldRecalc under percent threshold established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   "PrdYldRecalcExpected":boolean,
      /**   Indicates the shrink percent which will cause the expected production yield quantity to be recalculated based on actual production quantity if PrdYldRecalcExpected = true.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   "PrdYldRecalcUnderPct":number,
      /**   Indicates whether shop warning alerts should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   "PrdYldShopWrnAlert":boolean,
      /**   Indicates whether shop warning messages should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   "PrdYldShopWrn":boolean,
      /**   Indicates the shrink percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on  the settings of PrdYldShopWrnAlert and PrdYldShopWrn
This will only have an effect if Job.Head.ProductionYield = true.  */  
   "PrdYldShopWrnUnderPct":number,
      /**   Indicates the increased production percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on the settings of PrdYldShopWrnAlert and PrdYldShopWrn.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   "PrdYldShopWrnOverPct":number,
      /**  Indicate if the operation adds restricted substances.  */  
   "RestrictSubstance":boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for a job operation.  */  
   "RoughCutCode":string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   "SendAheadType":string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   "SendAheadOffset":number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   "PrjRoleList":string,
      /**  Role Default (should be in selected)  */  
   "RoleCodeDefault":string,
      /**  Indicates if Operation includes all roles  */  
   "UseAllRoles":boolean,
      /**  JDFMaterial  */  
   "JDFMaterial":string,
      /**  JDFDevice  */  
   "JDFDevice":string,
      /**  JDFOperation  */  
   "JDFOperation":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   "CharacteristicAttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CharacteristicAttributeSetID":number,
   "AllowInCurPlant":boolean,
   "OpMasDtlExists":boolean,
   "PrimaryProdOpDtlDesc":string,
   "PrimarySetupOpDtlDesc":string,
   "ScrPrimaryProdOpDtl":number,
   "ScrPrimarySetupOpDtl":number,
      /**  Operations has some Actions.  */  
   "HasActions":boolean,
      /**  Operation has Characteristics  */  
   "HasCharacteristics":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "BuyerName":string,
   "OPTextDescription":string,
   "RoleCdRoleDescription":string,
   "RoughCutParamDescription":string,
   "VendorNumTermsCode":string,
   "VendorNumZIP":string,
   "VendorNumCountry":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCity":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
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
      @param ProposedCapID
      @param ds
   */  
export interface ChangeCapabilityID_input{
      /**  The proposed Capability ID  */  
   ProposedCapID:string,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeCapabilityID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOpMasRestrictSubstance_input{
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeOpMasRestrictSubstance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOpMasRestrictionType_input{
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeOpMasRestrictionType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ProposedProdOpDtl
      @param ds
   */  
export interface ChangeOpMasterPrimaryProdOpDtl_input{
      /**  The proposed primary production operation detail sequence  */  
   ProposedProdOpDtl:number,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeOpMasterPrimaryProdOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ProposedSetupOpDtl
      @param ds
   */  
export interface ChangeOpMasterPrimarySetupOpDtl_input{
      /**  The proposed primary setup operation detail sequence  */  
   ProposedSetupOpDtl:number,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeOpMasterPrimarySetupOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ProposedResGrpID
      @param ds
   */  
export interface ChangeResourceGrpID_input{
      /**  The proposed Resource Group ID  */  
   ProposedResGrpID:string,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeResourceGrpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ProposedResourceID
      @param ds
   */  
export interface ChangeResourceID_input{
      /**  The proposed Resource ID  */  
   ProposedResourceID:string,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeResourceID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ProposedVendorNumVendorID
      @param ds
   */  
export interface ChangeVendorNumVendorID_input{
      /**  The proposed Vendor ID  */  
   ProposedVendorNumVendorID:string,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangeVendorNumVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedCharacteristicAttrClassID_input{
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ChangedCharacteristicAttrClassID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckInactiveSchedRequirement_input{
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface CheckInactiveSchedRequirement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
   InactiveMessage:string,
}
}

   /** Required : 
      @param opCode
   */  
export interface DeleteByID_input{
   opCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param whereClause
      @param enterpriseBAQID
      @param enterpriseSearchText
      @param pageSize
      @param absolutePage
   */  
export interface EnterpriseGetList_input{
      /**  whereClause  */  
   whereClause:string,
      /**  Enterprise BAQ ID  */  
   enterpriseBAQID:string,
      /**  Enterprise Search  */  
   enterpriseSearchText:string,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface EnterpriseGetList_output{
   returnObj:Erp_Tablesets_OpMasterListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Erp_Tablesets_OpMasDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Cannot be blank.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  Identifies which part of the production phase the resource is needed.   Valid values are "S", indicating the resource is required for the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   SetupOrProd:string,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   CapabilityID:string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  */  
   ResourceID:string,
      /**  The standard setup hours for the operation.   This is the setup time required for each machine.  */  
   SetupHours:number,
      /**  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  */  
   ProdHours:number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   NumResources:number,
      /**  Description is initially created when the OpMasDtl is created.   If the OpMasDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   OpDtlDesc:string,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Production Crew Size  */  
   ProdCrewSize:number,
      /**  Setup Crew Size  */  
   SetUpCrewSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrimaryProd  */  
   PrimaryProd:boolean,
      /**  PrimarySetup  */  
   PrimarySetup:boolean,
   CapabilityDesc:string,
   ResourceDesc:string,
   ResourceGrpDesc:string,
   SchedResourceDesc:string,
   Location:boolean,
   OPMasDtlType:string,
      /**  Resource Characteristic Attribute Class ID  */  
   ResourceCharAttrClassID:string,
      /**  Resource Characteristic Attribute Set ID  */  
   ResourceCharAttrSetID:number,
      /**  Resource SysRowID  */  
   ResourceSysRowID:string,
      /**  Resource Group Characteristic Attribute Class ID  */  
   ResourceGrpCharAttrClassID:string,
      /**  Resource Group Characteristic Attribute Set ID  */  
   ResourceGrpCharAttrSetID:number,
      /**  Resource Group SysRowID  */  
   ResourceGrpSysRowID:string,
   BitFlag:number,
   CapabilityIDDescription:string,
   OpCodeOpDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasRestrictSubstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  Substance identification.  */  
   SubstanceID:string,
      /**  Default weight of the substance per primary part of UOM  */  
   Weight:number,
      /**  By default the primary UOM of the part.  */  
   WeightUOM:string,
      /**  When true then weight is disregarded in compliance roll-up.  */  
   Manual:boolean,
      /**  The date when exempt status for this substance expires.  */  
   ExemptDate:string,
      /**  Optional. Exemption certificate.  */  
   ExemptCertificate:string,
      /**  Indicates if the Operation Restriction Substance is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  */  
   Inactive:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Exempt:boolean,
   BitFlag:number,
   OpCodeOpDesc:string,
   RestrictionTypeDescription:string,
   SubstanceDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  */  
   Manual:boolean,
      /**  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  */  
   Compliance:string,
      /**  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  */  
   ComplianceDate:string,
      /**  Indicates if the Operation Restriction Type is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  */  
   Inactive:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Weight:boolean,
   BitFlag:number,
   OpCodeOpDesc:string,
   RestrictionTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasterActionParamRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identity of Operation master record.  */  
   OpCode:string,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  A sequence number which uniquely identifies parameter within the Operation/Action set.  */  
   ActionParamSeq:number,
      /**  ActionParamFieldDataType  */  
   ActionParamFieldDataType:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueCharacter:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDate:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDecimal:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueInteger:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueLogical:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasterActionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identity of Operation master record.  */  
   OpCode:string,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  Description of Action.  */  
   ActionDesc:string,
      /**  Indicates if this action must be completed before Operation can be completed.  */  
   Required:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasterAttchRow{
   Company:string,
   OpCode:string,
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

export interface Erp_Tablesets_OpMasterInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  A sequence number that uniquely identifies the PartOprInsp ecord within the Part operation  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasterListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpDesc:string,
      /**  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  */  
   BuyerID:string,
   BuyerName:string,
      /**  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  */  
   OPType:string,
   AllowInCurPlant:boolean,
      /**  SubContract Operation  */  
   Subcontract:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Operation has Characteristics  */  
   HasCharacteristics:boolean,
      /**  Operations has some Actions.  */  
   HasActions:boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasterListTableset{
   OpMasterList:Erp_Tablesets_OpMasterListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OpMasterRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpDesc:string,
      /**  Key of the OpText record that is to be associated with this operation.  This is an optional field.  If entered it must be valid.  The purpose is that the OpText.Text data will be printed on the router after the operation detail.  The OpText is intended to be used for things such as creating inspection check off lines on the router.  */  
   OpTextID:string,
      /**  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  */  
   BuyerID:string,
      /**  Advanced Planning and Scheduling (eScheduling) preparatory operation flag.  A prep operation is usually a kitting operation.  Not used by the Manufacturing System scheduling module.  */  
   APSPrepOpF:boolean,
      /**  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  */  
   OPType:string,
      /**  FS - Editor widget for Operation comments.  */  
   CommentText:string,
      /**  FS - Labor rate used for  time on an operation.  Time per hour per technician.  */  
   BillLaborRate:number,
      /**  FS - The estimated Labor hours for the operation.  */  
   EstLabHours:number,
      /**  Used to sort operations when load leveling by Op Code.  */  
   SchedPrecedence:number,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  SubContract Operation  */  
   Subcontract:boolean,
      /**   Indicates whether the expected production yield quantity should be changed based on actual production quantity and the PrdYldRecalc under percent threshold established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   PrdYldRecalcExpected:boolean,
      /**   Indicates the shrink percent which will cause the expected production yield quantity to be recalculated based on actual production quantity if PrdYldRecalcExpected = true.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   PrdYldRecalcUnderPct:number,
      /**   Indicates whether shop warning alerts should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   PrdYldShopWrnAlert:boolean,
      /**   Indicates whether shop warning messages should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   PrdYldShopWrn:boolean,
      /**   Indicates the shrink percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on  the settings of PrdYldShopWrnAlert and PrdYldShopWrn
This will only have an effect if Job.Head.ProductionYield = true.  */  
   PrdYldShopWrnUnderPct:number,
      /**   Indicates the increased production percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on the settings of PrdYldShopWrnAlert and PrdYldShopWrn.
This will only have an effect if Job.Head.ProductionYield = true.  */  
   PrdYldShopWrnOverPct:number,
      /**  Indicate if the operation adds restricted substances.  */  
   RestrictSubstance:boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for a job operation.  */  
   RoughCutCode:string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Role Default (should be in selected)  */  
   RoleCodeDefault:string,
      /**  Indicates if Operation includes all roles  */  
   UseAllRoles:boolean,
      /**  JDFMaterial  */  
   JDFMaterial:string,
      /**  JDFDevice  */  
   JDFDevice:string,
      /**  JDFOperation  */  
   JDFOperation:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
   AllowInCurPlant:boolean,
   OpMasDtlExists:boolean,
   PrimaryProdOpDtlDesc:string,
   PrimarySetupOpDtlDesc:string,
   ScrPrimaryProdOpDtl:number,
   ScrPrimarySetupOpDtl:number,
      /**  Operations has some Actions.  */  
   HasActions:boolean,
      /**  Operation has Characteristics  */  
   HasCharacteristics:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   BuyerName:string,
   OPTextDescription:string,
   RoleCdRoleDescription:string,
   RoughCutParamDescription:string,
   VendorNumTermsCode:string,
   VendorNumZIP:string,
   VendorNumCountry:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumName:string,
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasterTableset{
   OpMaster:Erp_Tablesets_OpMasterRow[],
   OpMasterAttch:Erp_Tablesets_OpMasterAttchRow[],
   OpMasRestriction:Erp_Tablesets_OpMasRestrictionRow[],
   OpMasRestrictSubst:Erp_Tablesets_OpMasRestrictSubstRow[],
   OpMasterAction:Erp_Tablesets_OpMasterActionRow[],
   OpMasterActionParam:Erp_Tablesets_OpMasterActionParamRow[],
   OpMasterInsp:Erp_Tablesets_OpMasterInspRow[],
   OpMasDtl:Erp_Tablesets_OpMasDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtOpMasterTableset{
   OpMaster:Erp_Tablesets_OpMasterRow[],
   OpMasterAttch:Erp_Tablesets_OpMasterAttchRow[],
   OpMasRestriction:Erp_Tablesets_OpMasRestrictionRow[],
   OpMasRestrictSubst:Erp_Tablesets_OpMasRestrictSubstRow[],
   OpMasterAction:Erp_Tablesets_OpMasterActionRow[],
   OpMasterActionParam:Erp_Tablesets_OpMasterActionParamRow[],
   OpMasterInsp:Erp_Tablesets_OpMasterInspRow[],
   OpMasDtl:Erp_Tablesets_OpMasDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param opCode
   */  
export interface GetByID_input{
   opCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
}

   /** Required : 
      @param opCode
      @param opType
   */  
export interface GetByIDandOpType_input{
      /**  Opmaster.OpCode  */  
   opCode:string,
      /**  Opmaster.OpType  */  
   opType:string,
}

export interface GetByIDandOpType_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

export interface GetIfCurrentSiteHasExternalMES_output{
   returnObj:boolean,
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
   returnObj:Erp_Tablesets_OpMasterListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param OpCode
      @param OPMasDtlType
   */  
export interface GetNewOpMasDtlForOPMasDtlType_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   OpCode:string,
   OPMasDtlType:string,
}

export interface GetNewOpMasDtlForOPMasDtlType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
   */  
export interface GetNewOpMasDtl_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   opCode:string,
}

export interface GetNewOpMasDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
      @param restrictionTypeID
   */  
export interface GetNewOpMasRestrictSubst_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   opCode:string,
   restrictionTypeID:string,
}

export interface GetNewOpMasRestrictSubst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
   */  
export interface GetNewOpMasRestriction_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   opCode:string,
}

export interface GetNewOpMasRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
      @param actionSeq
   */  
export interface GetNewOpMasterActionParam_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   opCode:string,
   actionSeq:number,
}

export interface GetNewOpMasterActionParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
   */  
export interface GetNewOpMasterAction_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   opCode:string,
}

export interface GetNewOpMasterAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
   */  
export interface GetNewOpMasterAttch_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   opCode:string,
}

export interface GetNewOpMasterAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param opCode
   */  
export interface GetNewOpMasterInsp_input{
   ds:Erp_Tablesets_OpMasterTableset[],
   opCode:string,
}

export interface GetNewOpMasterInsp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewOpMaster_input{
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface GetNewOpMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

export interface GetProjectRoles_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param whereClauseOpMaster
      @param whereClauseOpMasterAttch
      @param whereClauseOpMasRestriction
      @param whereClauseOpMasRestrictSubst
      @param whereClauseOpMasterAction
      @param whereClauseOpMasterActionParam
      @param whereClauseOpMasterInsp
      @param whereClauseOpMasDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseOpMaster:string,
   whereClauseOpMasterAttch:string,
   whereClauseOpMasRestriction:string,
   whereClauseOpMasRestrictSubst:string,
   whereClauseOpMasterAction:string,
   whereClauseOpMasterActionParam:string,
   whereClauseOpMasterInsp:string,
   whereClauseOpMasDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
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
      @param ipOpMasterRowID
      @param ipCapabilityID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
   */  
export interface InsertCapability_input{
      /**  The rowid of the OpMaster record to add the operation detail to  */  
   ipOpMasterRowID:string,
      /**  The Capability ID being added  */  
   ipCapabilityID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
}

export interface InsertCapability_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
}

   /** Required : 
      @param ipOpMasterRowID
      @param ipResourceGrpID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
   */  
export interface InsertResourceGroup_input{
      /**  The rowid of the OpMaster record to add the operation detail to  */  
   ipOpMasterRowID:string,
      /**  The Resource Group ID being added  */  
   ipResourceGrpID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
}

export interface InsertResourceGroup_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
}

   /** Required : 
      @param ipOpMasterRowID
      @param ipResourceID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
   */  
export interface InsertResource_input{
      /**  The rowid of the OpMaster record to add the operation detail to  */  
   ipOpMasterRowID:string,
      /**  The Resource ID being added  */  
   ipResourceID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
}

export interface InsertResource_output{
   returnObj:Erp_Tablesets_OpMasterTableset[],
}

   /** Required : 
      @param actionParamSeq
      @param ds
   */  
export interface OnChangingActionParamSeq_input{
   actionParamSeq:number,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface OnChangingActionParamSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param newActionSeq
      @param ds
   */  
export interface OnChangingActionSeq_input{
   newActionSeq:number,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface OnChangingActionSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtOpMasterTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtOpMasterTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

   /** Required : 
      @param ipProposedInspPlan
      @param ipProposedSpecId
      @param ds
   */  
export interface ValidateInspection_input{
      /**  The new proposed InspPlanPartNum value  */  
   ipProposedInspPlan:string,
      /**  The new proposed SpecID value  */  
   ipProposedSpecId:string,
   ds:Erp_Tablesets_OpMasterTableset[],
}

export interface ValidateInspection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OpMasterTableset,
}
}

