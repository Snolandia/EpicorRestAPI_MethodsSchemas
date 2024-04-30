import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.EquipSvc
// Description: Equipment Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/$metadata", {
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
   Description: Get Equips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Equips
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipRow
   */  
export function get_Equips(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Equips
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EquipRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Equips(requestBody:Erp_Tablesets_EquipRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Equip item
   Description: Calls GetByID to retrieve the Equip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Equip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EquipRow
   */  
export function get_Equips_Company_EquipID(Company:string, EquipID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EquipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")", {
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
         resolve(data as Erp_Tablesets_EquipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Equip for the service
   Description: Calls UpdateExt to update Equip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Equip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Equips_Company_EquipID(Company:string, EquipID:string, requestBody:Erp_Tablesets_EquipRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")", {
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
   Summary: Call UpdateExt to delete Equip item
   Description: Call UpdateExt to delete Equip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Equip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Equips_Company_EquipID(Company:string, EquipID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")", {
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
   Description: Get EquipPlans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EquipPlans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanRow
   */  
export function get_Equips_Company_EquipID_EquipPlans(Company:string, EquipID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipPlans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EquipPlan item
   Description: Calls GetByID to retrieve the EquipPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlan1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EquipPlanRow
   */  
export function get_Equips_Company_EquipID_EquipPlans_Company_EquipID_PlanNum(Company:string, EquipID:string, PlanNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EquipPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")", {
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
         resolve(data as Erp_Tablesets_EquipPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EquipAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EquipAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipAttchRow
   */  
export function get_Equips_Company_EquipID_EquipAttches(Company:string, EquipID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EquipAttch item
   Description: Calls GetByID to retrieve the EquipAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EquipAttchRow
   */  
export function get_Equips_Company_EquipID_EquipAttches_Company_EquipID_DrawingSeq(Company:string, EquipID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EquipAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_EquipAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EquipPlans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EquipPlans
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanRow
   */  
export function get_EquipPlans(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EquipPlans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipPlanRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EquipPlanRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EquipPlans(requestBody:Erp_Tablesets_EquipPlanRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the EquipPlan item
   Description: Calls GetByID to retrieve the EquipPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlan
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EquipPlanRow
   */  
export function get_EquipPlans_Company_EquipID_PlanNum(Company:string, EquipID:string, PlanNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EquipPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")", {
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
         resolve(data as Erp_Tablesets_EquipPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EquipPlan for the service
   Description: Calls UpdateExt to update EquipPlan. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EquipPlan
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipPlanRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EquipPlans_Company_EquipID_PlanNum(Company:string, EquipID:string, PlanNum:string, requestBody:Erp_Tablesets_EquipPlanRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")", {
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
   Summary: Call UpdateExt to delete EquipPlan item
   Description: Call UpdateExt to delete EquipPlan item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EquipPlan
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EquipPlans_Company_EquipID_PlanNum(Company:string, EquipID:string, PlanNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")", {
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
   Description: Get EquipPlanAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EquipPlanAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanAttchRow
   */  
export function get_EquipPlans_Company_EquipID_PlanNum_EquipPlanAttches(Company:string, EquipID:string, PlanNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")/EquipPlanAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EquipPlanAttch item
   Description: Calls GetByID to retrieve the EquipPlanAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlanAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   */  
export function get_EquipPlans_Company_EquipID_PlanNum_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company:string, EquipID:string, PlanNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EquipPlanAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_EquipPlanAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EquipPlanAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EquipPlanAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanAttchRow
   */  
export function get_EquipPlanAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EquipPlanAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EquipPlanAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EquipPlanAttches(requestBody:Erp_Tablesets_EquipPlanAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the EquipPlanAttch item
   Description: Calls GetByID to retrieve the EquipPlanAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlanAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   */  
export function get_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company:string, EquipID:string, PlanNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EquipPlanAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_EquipPlanAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EquipPlanAttch for the service
   Description: Calls UpdateExt to update EquipPlanAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EquipPlanAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company:string, EquipID:string, PlanNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_EquipPlanAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete EquipPlanAttch item
   Description: Call UpdateExt to delete EquipPlanAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EquipPlanAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param PlanNum Desc: PlanNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company:string, EquipID:string, PlanNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")", {
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
   Description: Get EquipAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EquipAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipAttchRow
   */  
export function get_EquipAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EquipAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EquipAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EquipAttches(requestBody:Erp_Tablesets_EquipAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the EquipAttch item
   Description: Calls GetByID to retrieve the EquipAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EquipAttchRow
   */  
export function get_EquipAttches_Company_EquipID_DrawingSeq(Company:string, EquipID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EquipAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_EquipAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EquipAttch for the service
   Description: Calls UpdateExt to update EquipAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EquipAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EquipAttches_Company_EquipID_DrawingSeq(Company:string, EquipID:string, DrawingSeq:string, requestBody:Erp_Tablesets_EquipAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete EquipAttch item
   Description: Call UpdateExt to delete EquipAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EquipAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EquipAttches_Company_EquipID_DrawingSeq(Company:string, EquipID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipListRow)
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
export function get_GetRows(whereClauseEquip:string, whereClauseEquipAttch:string, whereClauseEquipPlan:string, whereClauseEquipPlanAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseEquip!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEquip=" + whereClauseEquip
   }
   if(typeof whereClauseEquipAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEquipAttch=" + whereClauseEquipAttch
   }
   if(typeof whereClauseEquipPlan!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEquipPlan=" + whereClauseEquipPlan
   }
   if(typeof whereClauseEquipPlanAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEquipPlanAttch=" + whereClauseEquipPlanAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetRows" + params, {
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
export function get_GetByID(equipID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof equipID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "equipID=" + equipID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetList" + params, {
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
   Summary: Invoke method CalcAvgUsage
   Description: This method returns the Average Daily Usage
   OperationID: CalcAvgUsage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalcAvgUsage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAvgUsage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcAvgUsage(requestBody:CalcAvgUsage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalcAvgUsage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/CalcAvgUsage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CalcAvgUsage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportAssets
   Description: This method should be called when Import Assets records.
   OperationID: ImportAssets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportAssets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportAssets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportAssets(requestBody:ImportAssets_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportAssets_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/ImportAssets", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportAssets_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportResources
   Description: This method should be called when Import Resources records.
   OperationID: ImportResources
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportResources_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportResources_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportResources(requestBody:ImportResources_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportResources_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/ImportResources", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportResources_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsMaintPlant
   Description: Returns true if Current Plant is a Maintenance plant.
Created to be called from EquipEntry.
If not a Maintenance plan the form will be in "Read Only" mode
   OperationID: IsMaintPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsMaintPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsMaintPlant(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsMaintPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/IsMaintPlant", {
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
         resolve(data as IsMaintPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAssetNum
   Description: This method should be called when AssetNum change.
   OperationID: OnChangeAssetNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAssetNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssetNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssetNum(requestBody:OnChangeAssetNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAssetNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeAssetNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeAssetNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeEquipTemplateJobNum
   Description: This method should be called when Equip.TemplateJobNum changes.
   OperationID: OnChangeEquipTemplateJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeEquipTemplateJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipTemplateJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEquipTemplateJobNum(requestBody:OnChangeEquipTemplateJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeEquipTemplateJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeEquipTemplateJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeEquipTemplateJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeIssueTopics
   Description: This method should be invoked when the IssueTopics changes.
Validates and sets the individual IssueTopic fields.
   OperationID: OnChangeIssueTopics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeIssueTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIssueTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIssueTopics(requestBody:OnChangeIssueTopics_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeIssueTopics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeIssueTopics", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeIssueTopics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMeterFreq
   Description: This method should be called when MeterFreq change.
   OperationID: OnChangeMeterFreq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMeterFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMeterFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMeterFreq(requestBody:OnChangeMeterFreq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMeterFreq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeMeterFreq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMeterFreq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeParentEquipID
   Description: This method should be called when ParentEquipID change.
   OperationID: OnChangeParentEquipID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeParentEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeParentEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeParentEquipID(requestBody:OnChangeParentEquipID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeParentEquipID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeParentEquipID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeParentEquipID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeProjectID
   Description: This method should be called when ProjectID change.
   OperationID: OnChangeProjectID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeProjectID(requestBody:OnChangeProjectID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeProjectID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeProjectID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeProjectID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeResourceID
   Description: This method should be called when ResourceID change.
   OperationID: OnChangeResourceID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeResourceID(requestBody:OnChangeResourceID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeResourceID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeResourceID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeResourceID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSellingPurPoint
   Description: This method should be called when SellingPurPoint change.
   OperationID: OnChangeSellingPurPoint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSellingPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSellingPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSellingPurPoint(requestBody:OnChangeSellingPurPoint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSellingPurPoint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeSellingPurPoint", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeSellingPurPoint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSellingVendor
   Description: This method should be called when SellingVendor change.
   OperationID: OnChangeSellingVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSellingVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSellingVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSellingVendor(requestBody:OnChangeSellingVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSellingVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeSellingVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeSellingVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeServicePurPoint
   Description: This method should be called when ServicePurPoint change.
   OperationID: OnChangeServicePurPoint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeServicePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeServicePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeServicePurPoint(requestBody:OnChangeServicePurPoint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeServicePurPoint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeServicePurPoint", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeServicePurPoint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeServiceVendor
   Description: This method should be called when ServiceVendor change.
   OperationID: OnChangeServiceVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeServiceVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeServiceVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeServiceVendor(requestBody:OnChangeServiceVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeServiceVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeServiceVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeServiceVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTemplateJobNum
   Description: This method should be called when EquipPlan.TemplateJobNum change.
   OperationID: OnChangeTemplateJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTemplateJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTemplateJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTemplateJobNum(requestBody:OnChangeTemplateJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTemplateJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeTemplateJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTemplateJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTimeFreq
   Description: This method should be called when TimeFreq change.
   OperationID: OnChangeTimeFreq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTimeFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTimeFreq(requestBody:OnChangeTimeFreq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTimeFreq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeTimeFreq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTimeFreq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTimeUOM
   Description: This method should be called when TimeUOM change.
   OperationID: OnChangeTimeUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTimeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTimeUOM(requestBody:OnChangeTimeUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTimeUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/OnChangeTimeUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTimeUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEquip
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEquip(requestBody:GetNewEquip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEquip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetNewEquip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEquip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEquipAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquipAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEquipAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquipAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEquipAttch(requestBody:GetNewEquipAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEquipAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetNewEquipAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEquipAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEquipPlan
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquipPlan
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEquipPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquipPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEquipPlan(requestBody:GetNewEquipPlan_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEquipPlan_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetNewEquipPlan", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEquipPlan_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEquipPlanAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquipPlanAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEquipPlanAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquipPlanAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEquipPlanAttch(requestBody:GetNewEquipPlanAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEquipPlanAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetNewEquipPlanAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEquipPlanAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EquipAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EquipListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EquipPlanAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EquipPlanRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EquipRow,
}

export interface Erp_Tablesets_EquipAttchRow{
   "Company":string,
   "EquipID":string,
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

export interface Erp_Tablesets_EquipListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   "EquipID":string,
      /**  Site in which the equipment is currently located.  */  
   "Plant":string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   "InActive":boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   "Description":string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   "StatusID":string,
      /**  OEM Number  */  
   "OEM":string,
      /**  Serial Number of equipment  */  
   "SerialNum":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  Model Number  */  
   "Model":string,
      /**  Date that equipment was first put into service. Required field.  */  
   "InServiceDate":string,
      /**  Warrenty Expiration Date  */  
   "WarrantyExpDate":string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   "TypeID":string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "SellingVendorNum":number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "SellingPurPoint":string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "ServiceVendorNum":number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "ServicePurPoint":string,
      /**  Foreign Component key to the FAsset table.  */  
   "AssetNum":string,
      /**  Comments about the Equipment.  */  
   "Comments":string,
      /**  Allows entry of freeform equipment specifications.  */  
   "Specs":string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   "MeterUOM":string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   "CurrentMeter":number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   "ReadingComment":string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   "LocID":string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   "ParentEquipID":string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   "LaborMeterOpt":string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   "ReadingDate":string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   "ReadingTime":number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   "InspPlanPartNum":string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   "SpecID":string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   "LastCalDate":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   "ProjectID":string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   "UOMClassID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   "Lineage":string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   "TemplateJobNum":string,
   "AvgDailyUsage":number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   "GlobalEquip":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "JCDeptDesc":string,
      /**  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  */  
   "DisablePlant":boolean,
      /**  Mandatory description of the asset.  */  
   "AssetNumAssetDescription":string,
      /**  Description the Location.  Cannot be blank.  */  
   "EquipLocDescription":string,
      /**  Description of Equipment Status. Cannot be blank.  */  
   "EquipStatusDescription":string,
      /**  Description of Equipment Type. Cannot be blank.  */  
   "EquipTypeDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Full description of Equipment. Cannot be blank.  */  
   "ParentDescription":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Full description of Project Management Code.  */  
   "ProjectDescription":string,
      /**  Description  */  
   "ProjPhaseDescription":string,
      /**  Full description of Resource.  */  
   "ResourceDescription":string,
      /**  Long description of the Resource Group.  */  
   "ResourceGroupDescription":string,
      /**  Purchase Point Name...can't be blank.  */  
   "SellingVendorNameName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "SellingVendorNumVendorID":string,
      /**  Purchase Point Name...can't be blank.  */  
   "ServiceVendorNameName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "ServiceVendorNumVendorID":string,
      /**  A decription for the UOMClass.  Mandatory.  */  
   "UOMClassIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EquipPlanAttchRow{
   "Company":string,
   "EquipID":string,
   "PlanNum":number,
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

export interface Erp_Tablesets_EquipPlanRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  EquipID that this EquipPlan record is for. A foreign key component to parent Equip record.  */  
   "EquipID":string,
      /**  A number which uniquely identifies a preventative maintenance plan for a specific piece of equipment.  Generated by the system as PlanNum of last EquipPlan of a specific Company/EquipID + 1.  */  
   "PlanNum":number,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   "InActive":boolean,
      /**   Description of maintenance plan. Cannot be blank.
Example: "30,000 Mile Checkup".  
Note: Will be used as the JobHead.PartDescription when the maintenance job is created.  */  
   "Description":string,
      /**  Time Based Frequency. Examples Days, Weeks, Months  */  
   "TimeFreq":number,
      /**  Qualifies the TimeFreq value as "Days, Weeks,  or Months"  */  
   "TimeUOM":string,
      /**  A metered value, that when reached triggers the maintenance plan. Example: At  5000 miles this Maintenance is required. The Equip.MeterUOM qualifies this value.  */  
   "MeterFreq":number,
      /**   Indicates if Plan is to be performed at every occurance or only the first occurance of the defined frequencies.
Example of a Recurring Plan would be "Change oil every 5000 miles".
An example of a non recurring plan would be "Initial Break in checkup".  */  
   "Recurs":boolean,
      /**  Next Date that this Maintenance Plan should be performed. This is relevant only to a "time based" maintenance plan (TimeFreq > 0) otherwise it is null and not maintainable. If TimeFreq, TimeUOM changes or when Plan is executed, it is set as today + time frequency (in days). Note; can be manually updated allowing the user to control the next time based event.  */  
   "NextDate":string,
      /**  Next Meter Reading at which this Maintenance Plan should be performed. This is relevant only to a "meter based" maintenance plan (MeterFreq > 0) otherwise it is zero and not maintainable. If MeterFreq changes or when Plan is executed, it is set as CurrentMeter + MeterFreq.  Note; can be manually updated allowing the user to control the next meter event.  For example, the frequency is 3000 Miles, however, you set NextMeter to 500 Miles for the Initial Break In Checkup.  */  
   "NextMeter":number,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   "TemplateJobNum":string,
      /**  Internal field indicating if it is time current action being taken. Used by the PMPP (Preventive Maintenance Plan Processor) to quickly find Plans which need to be performed. Set to "P" (Pending), when the Maintenance Job is closed or deleted. Set to "Q" (Queued) when the Plans frequencies are met.  That is, NextMeter > 0 and <= Current or NextDate <> ? and <= Today. Setting based on meter occurs as part of the Meter Reading process. Setting based on Date, is done, periodically by the PMPP. Set to "I" (Initiated) by the PMPP when a Job is generated.  */  
   "ActionStatus":string,
      /**  Maintenance Issue Topic 1.  Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   "IssueTopicID2":string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   "IssueTopicID3":string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   "IssueTopicID4":string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   "IssueTopicID5":string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   "IssueTopicID6":string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   "IssueTopicID7":string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   "IssueTopicID8":string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   "IssueTopicID9":string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   "IssueTopicID10":string,
      /**  Number of days prior to the actual  maintenance event that the system should create the Maintenance Job.    This applies to both time based and meter based plans. Defaults to  MMSyst.MaintBuffer value.  */  
   "MaintBuffer":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "MeterUOM":string,
      /**  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  */  
   "IssueTopics":string,
   "BitFlag":number,
   "IssueTopicID1Description":string,
   "IssueTopicID10Description":string,
   "IssueTopicID2Description":string,
   "IssueTopicID3Description":string,
   "IssueTopicID4Description":string,
   "IssueTopicID5Description":string,
   "IssueTopicID6Description":string,
   "IssueTopicID7Description":string,
   "IssueTopicID8Description":string,
   "IssueTopicID9Description":string,
   "JobNumPartDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EquipRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   "EquipID":string,
      /**  Site in which the equipment is currently located.  */  
   "Plant":string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   "InActive":boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   "Description":string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   "StatusID":string,
      /**  OEM Number  */  
   "OEM":string,
      /**  Serial Number of equipment  */  
   "SerialNum":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  Model Number  */  
   "Model":string,
      /**  Date that equipment was first put into service. Required field.  */  
   "InServiceDate":string,
      /**  Warrenty Expiration Date  */  
   "WarrantyExpDate":string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   "TypeID":string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "SellingVendorNum":number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "SellingPurPoint":string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "ServiceVendorNum":number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "ServicePurPoint":string,
      /**  Foreign Component key to the FAsset table.  */  
   "AssetNum":string,
      /**  Comments about the Equipment.  */  
   "Comments":string,
      /**  Allows entry of freeform equipment specifications.  */  
   "Specs":string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   "MeterUOM":string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   "CurrentMeter":number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   "ReadingComment":string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   "LocID":string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   "ParentEquipID":string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   "LaborMeterOpt":string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   "ReadingDate":string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   "ReadingTime":number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   "InspPlanPartNum":string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   "SpecID":string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   "LastCalDate":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   "ProjectID":string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   "UOMClassID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   "Lineage":string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   "TemplateJobNum":string,
   "AvgDailyUsage":number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   "GlobalEquip":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "JCDeptDesc":string,
      /**  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  */  
   "DisablePlant":boolean,
   "BitFlag":number,
   "AssetNumAssetDescription":string,
   "EquipLocDescription":string,
   "EquipStatusDescription":string,
   "EquipTypeDescription":string,
   "JobNumPartDescription":string,
   "ParentDescription":string,
   "PlantName":string,
   "ProjectDescription":string,
   "ProjPhaseDescription":string,
   "ResourceDescription":string,
   "ResourceGroupDescription":string,
   "SellingVendorNameName":string,
   "SellingVendorNumVendorID":string,
   "ServiceVendorNameName":string,
   "ServiceVendorNumVendorID":string,
   "UOMClassIDDescription":string,
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
      @param equipID
   */  
export interface CalcAvgUsage_input{
      /**  equipID  */  
   equipID:string,
}

export interface CalcAvgUsage_output{
parameters : {
      /**  output parameters  */  
   avgUsage:number,
}
}

   /** Required : 
      @param equipID
   */  
export interface DeleteByID_input{
   equipID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_EquipAttchRow{
   Company:string,
   EquipID:string,
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

export interface Erp_Tablesets_EquipListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   EquipID:string,
      /**  Site in which the equipment is currently located.  */  
   Plant:string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   InActive:boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   Description:string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   StatusID:string,
      /**  OEM Number  */  
   OEM:string,
      /**  Serial Number of equipment  */  
   SerialNum:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  Model Number  */  
   Model:string,
      /**  Date that equipment was first put into service. Required field.  */  
   InServiceDate:string,
      /**  Warrenty Expiration Date  */  
   WarrantyExpDate:string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   TypeID:string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   SellingVendorNum:number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   SellingPurPoint:string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   ServiceVendorNum:number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   ServicePurPoint:string,
      /**  Foreign Component key to the FAsset table.  */  
   AssetNum:string,
      /**  Comments about the Equipment.  */  
   Comments:string,
      /**  Allows entry of freeform equipment specifications.  */  
   Specs:string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   MeterUOM:string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   CurrentMeter:number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   ReadingComment:string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   LocID:string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   ParentEquipID:string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   LaborMeterOpt:string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   ReadingDate:string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   ReadingTime:number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   InspPlanPartNum:string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   SpecID:string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   LastCalDate:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   ProjectID:string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   UOMClassID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   Lineage:string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   TemplateJobNum:string,
   AvgDailyUsage:number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   GlobalEquip:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   JCDeptDesc:string,
      /**  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  */  
   DisablePlant:boolean,
      /**  Mandatory description of the asset.  */  
   AssetNumAssetDescription:string,
      /**  Description the Location.  Cannot be blank.  */  
   EquipLocDescription:string,
      /**  Description of Equipment Status. Cannot be blank.  */  
   EquipStatusDescription:string,
      /**  Description of Equipment Type. Cannot be blank.  */  
   EquipTypeDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Full description of Equipment. Cannot be blank.  */  
   ParentDescription:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Full description of Project Management Code.  */  
   ProjectDescription:string,
      /**  Description  */  
   ProjPhaseDescription:string,
      /**  Full description of Resource.  */  
   ResourceDescription:string,
      /**  Long description of the Resource Group.  */  
   ResourceGroupDescription:string,
      /**  Purchase Point Name...can't be blank.  */  
   SellingVendorNameName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   SellingVendorNumVendorID:string,
      /**  Purchase Point Name...can't be blank.  */  
   ServiceVendorNameName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   ServiceVendorNumVendorID:string,
      /**  A decription for the UOMClass.  Mandatory.  */  
   UOMClassIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EquipListTableset{
   EquipList:Erp_Tablesets_EquipListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EquipPlanAttchRow{
   Company:string,
   EquipID:string,
   PlanNum:number,
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

export interface Erp_Tablesets_EquipPlanRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  EquipID that this EquipPlan record is for. A foreign key component to parent Equip record.  */  
   EquipID:string,
      /**  A number which uniquely identifies a preventative maintenance plan for a specific piece of equipment.  Generated by the system as PlanNum of last EquipPlan of a specific Company/EquipID + 1.  */  
   PlanNum:number,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   InActive:boolean,
      /**   Description of maintenance plan. Cannot be blank.
Example: "30,000 Mile Checkup".  
Note: Will be used as the JobHead.PartDescription when the maintenance job is created.  */  
   Description:string,
      /**  Time Based Frequency. Examples Days, Weeks, Months  */  
   TimeFreq:number,
      /**  Qualifies the TimeFreq value as "Days, Weeks,  or Months"  */  
   TimeUOM:string,
      /**  A metered value, that when reached triggers the maintenance plan. Example: At  5000 miles this Maintenance is required. The Equip.MeterUOM qualifies this value.  */  
   MeterFreq:number,
      /**   Indicates if Plan is to be performed at every occurance or only the first occurance of the defined frequencies.
Example of a Recurring Plan would be "Change oil every 5000 miles".
An example of a non recurring plan would be "Initial Break in checkup".  */  
   Recurs:boolean,
      /**  Next Date that this Maintenance Plan should be performed. This is relevant only to a "time based" maintenance plan (TimeFreq > 0) otherwise it is null and not maintainable. If TimeFreq, TimeUOM changes or when Plan is executed, it is set as today + time frequency (in days). Note; can be manually updated allowing the user to control the next time based event.  */  
   NextDate:string,
      /**  Next Meter Reading at which this Maintenance Plan should be performed. This is relevant only to a "meter based" maintenance plan (MeterFreq > 0) otherwise it is zero and not maintainable. If MeterFreq changes or when Plan is executed, it is set as CurrentMeter + MeterFreq.  Note; can be manually updated allowing the user to control the next meter event.  For example, the frequency is 3000 Miles, however, you set NextMeter to 500 Miles for the Initial Break In Checkup.  */  
   NextMeter:number,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   TemplateJobNum:string,
      /**  Internal field indicating if it is time current action being taken. Used by the PMPP (Preventive Maintenance Plan Processor) to quickly find Plans which need to be performed. Set to "P" (Pending), when the Maintenance Job is closed or deleted. Set to "Q" (Queued) when the Plans frequencies are met.  That is, NextMeter > 0 and <= Current or NextDate <> ? and <= Today. Setting based on meter occurs as part of the Meter Reading process. Setting based on Date, is done, periodically by the PMPP. Set to "I" (Initiated) by the PMPP when a Job is generated.  */  
   ActionStatus:string,
      /**  Maintenance Issue Topic 1.  Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   IssueTopicID2:string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   IssueTopicID3:string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   IssueTopicID4:string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   IssueTopicID5:string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   IssueTopicID6:string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   IssueTopicID7:string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   IssueTopicID8:string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   IssueTopicID9:string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   IssueTopicID10:string,
      /**  Number of days prior to the actual  maintenance event that the system should create the Maintenance Job.    This applies to both time based and meter based plans. Defaults to  MMSyst.MaintBuffer value.  */  
   MaintBuffer:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   MeterUOM:string,
      /**  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  */  
   IssueTopics:string,
   BitFlag:number,
   IssueTopicID1Description:string,
   IssueTopicID10Description:string,
   IssueTopicID2Description:string,
   IssueTopicID3Description:string,
   IssueTopicID4Description:string,
   IssueTopicID5Description:string,
   IssueTopicID6Description:string,
   IssueTopicID7Description:string,
   IssueTopicID8Description:string,
   IssueTopicID9Description:string,
   JobNumPartDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EquipRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   EquipID:string,
      /**  Site in which the equipment is currently located.  */  
   Plant:string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   InActive:boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   Description:string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   StatusID:string,
      /**  OEM Number  */  
   OEM:string,
      /**  Serial Number of equipment  */  
   SerialNum:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  Model Number  */  
   Model:string,
      /**  Date that equipment was first put into service. Required field.  */  
   InServiceDate:string,
      /**  Warrenty Expiration Date  */  
   WarrantyExpDate:string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   TypeID:string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   SellingVendorNum:number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   SellingPurPoint:string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   ServiceVendorNum:number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   ServicePurPoint:string,
      /**  Foreign Component key to the FAsset table.  */  
   AssetNum:string,
      /**  Comments about the Equipment.  */  
   Comments:string,
      /**  Allows entry of freeform equipment specifications.  */  
   Specs:string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   MeterUOM:string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   CurrentMeter:number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   ReadingComment:string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   LocID:string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   ParentEquipID:string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   LaborMeterOpt:string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   ReadingDate:string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   ReadingTime:number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   InspPlanPartNum:string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   SpecID:string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   LastCalDate:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   ProjectID:string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   UOMClassID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   Lineage:string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   TemplateJobNum:string,
   AvgDailyUsage:number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   GlobalEquip:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   JCDeptDesc:string,
      /**  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  */  
   DisablePlant:boolean,
   BitFlag:number,
   AssetNumAssetDescription:string,
   EquipLocDescription:string,
   EquipStatusDescription:string,
   EquipTypeDescription:string,
   JobNumPartDescription:string,
   ParentDescription:string,
   PlantName:string,
   ProjectDescription:string,
   ProjPhaseDescription:string,
   ResourceDescription:string,
   ResourceGroupDescription:string,
   SellingVendorNameName:string,
   SellingVendorNumVendorID:string,
   ServiceVendorNameName:string,
   ServiceVendorNumVendorID:string,
   UOMClassIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EquipTableset{
   Equip:Erp_Tablesets_EquipRow[],
   EquipAttch:Erp_Tablesets_EquipAttchRow[],
   EquipPlan:Erp_Tablesets_EquipPlanRow[],
   EquipPlanAttch:Erp_Tablesets_EquipPlanAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtEquipTableset{
   Equip:Erp_Tablesets_EquipRow[],
   EquipAttch:Erp_Tablesets_EquipAttchRow[],
   EquipPlan:Erp_Tablesets_EquipPlanRow[],
   EquipPlanAttch:Erp_Tablesets_EquipPlanAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param equipID
   */  
export interface GetByID_input{
   equipID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_EquipTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_EquipTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_EquipTableset[],
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
   returnObj:Erp_Tablesets_EquipListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param equipID
   */  
export interface GetNewEquipAttch_input{
   ds:Erp_Tablesets_EquipTableset[],
   equipID:string,
}

export interface GetNewEquipAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ds
      @param equipID
      @param planNum
   */  
export interface GetNewEquipPlanAttch_input{
   ds:Erp_Tablesets_EquipTableset[],
   equipID:string,
   planNum:number,
}

export interface GetNewEquipPlanAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ds
      @param equipID
   */  
export interface GetNewEquipPlan_input{
   ds:Erp_Tablesets_EquipTableset[],
   equipID:string,
}

export interface GetNewEquipPlan_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewEquip_input{
   ds:Erp_Tablesets_EquipTableset[],
}

export interface GetNewEquip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param whereClauseEquip
      @param whereClauseEquipAttch
      @param whereClauseEquipPlan
      @param whereClauseEquipPlanAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseEquip:string,
   whereClauseEquipAttch:string,
   whereClauseEquipPlan:string,
   whereClauseEquipPlanAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_EquipTableset[],
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
      @param ipAssetNum
      @param ds
   */  
export interface ImportAssets_input{
      /**  Asset Num  */  
   ipAssetNum:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface ImportAssets_output{
parameters : {
      /**  output parameters  */  
   vMsg:string,
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ipResourceID
      @param ds
   */  
export interface ImportResources_input{
      /**  ResourceID  */  
   ipResourceID:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface ImportResources_output{
parameters : {
      /**  output parameters  */  
   vMsg:string,
   ds:Erp_Tablesets_EquipTableset,
}
}

export interface IsMaintPlant_output{
parameters : {
      /**  output parameters  */  
   isMaintPlant:boolean,
}
}

   /** Required : 
      @param assetNum
      @param ds
   */  
export interface OnChangeAssetNum_input{
      /**  assetNum  */  
   assetNum:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeAssetNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ipJobNum
      @param ds
   */  
export interface OnChangeEquipTemplateJobNum_input{
      /**  Job Num  */  
   ipJobNum:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeEquipTemplateJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param topics
      @param ds
   */  
export interface OnChangeIssueTopics_input{
      /**  Proposed topics string id  */  
   topics:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeIssueTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ipMeterFreq
      @param ds
   */  
export interface OnChangeMeterFreq_input{
      /**  Meter Freq  */  
   ipMeterFreq:number,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeMeterFreq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param parentID
      @param ds
   */  
export interface OnChangeParentEquipID_input{
      /**  parentID  */  
   parentID:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeParentEquipID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param projectID
      @param ds
   */  
export interface OnChangeProjectID_input{
      /**  projectID  */  
   projectID:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param resourceID
      @param ds
   */  
export interface OnChangeResourceID_input{
      /**  resourceID  */  
   resourceID:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeResourceID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param sellingPurPoint
      @param ds
   */  
export interface OnChangeSellingPurPoint_input{
      /**  sellingPurPoint  */  
   sellingPurPoint:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeSellingPurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param vendorID
      @param ds
   */  
export interface OnChangeSellingVendor_input{
      /**  vendorID  */  
   vendorID:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeSellingVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param servicePurPoint
      @param ds
   */  
export interface OnChangeServicePurPoint_input{
      /**  sellingPurPoint  */  
   servicePurPoint:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeServicePurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param vendorID
      @param ds
   */  
export interface OnChangeServiceVendor_input{
      /**  vendorID  */  
   vendorID:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeServiceVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ipJobNum
      @param ds
   */  
export interface OnChangeTemplateJobNum_input{
      /**  Job Num  */  
   ipJobNum:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeTemplateJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ipTimeFreq
      @param ds
   */  
export interface OnChangeTimeFreq_input{
      /**  Time Freq  */  
   ipTimeFreq:number,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeTimeFreq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ipTimeUOM
      @param ds
   */  
export interface OnChangeTimeUOM_input{
      /**  Time UOM  */  
   ipTimeUOM:string,
   ds:Erp_Tablesets_EquipTableset[],
}

export interface OnChangeTimeUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtEquipTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtEquipTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_EquipTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EquipTableset,
}
}

