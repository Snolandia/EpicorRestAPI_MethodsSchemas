import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RoleCdSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/$metadata", {
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
   Description: Get RoleCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RoleCds
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RoleCdRow
   */  
export function get_RoleCds(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RoleCds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RoleCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RoleCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RoleCds(requestBody:Erp_Tablesets_RoleCdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RoleCd item
   Description: Calls GetByID to retrieve the RoleCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RoleCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCode Desc: RoleCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RoleCdRow
   */  
export function get_RoleCds_Company_RoleCode(Company:string, RoleCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RoleCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")", {
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
         resolve(data as Erp_Tablesets_RoleCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RoleCd for the service
   Description: Calls UpdateExt to update RoleCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RoleCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCode Desc: RoleCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RoleCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RoleCds_Company_RoleCode(Company:string, RoleCode:string, requestBody:Erp_Tablesets_RoleCdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")", {
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
   Summary: Call UpdateExt to delete RoleCd item
   Description: Call UpdateExt to delete RoleCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RoleCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCode Desc: RoleCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RoleCds_Company_RoleCode(Company:string, RoleCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")", {
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
   Description: Get PrjRoleRts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PrjRoleRts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCode Desc: RoleCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PrjRoleRtRow
   */  
export function get_RoleCds_Company_RoleCode_PrjRoleRts(Company:string, RoleCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PrjRoleRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")/PrjRoleRts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PrjRoleRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PrjRoleRt item
   Description: Calls GetByID to retrieve the PrjRoleRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PrjRoleRt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCode Desc: RoleCode   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PrjRoleRtRow
   */  
export function get_RoleCds_Company_RoleCode_PrjRoleRts_Company_RoleCd_Seq(Company:string, RoleCode:string, RoleCd:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PrjRoleRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")", {
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
         resolve(data as Erp_Tablesets_PrjRoleRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PrjRoleRts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PrjRoleRts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PrjRoleRtRow
   */  
export function get_PrjRoleRts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PrjRoleRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PrjRoleRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PrjRoleRts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PrjRoleRtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PrjRoleRtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrjRoleRts(requestBody:Erp_Tablesets_PrjRoleRtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PrjRoleRt item
   Description: Calls GetByID to retrieve the PrjRoleRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PrjRoleRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PrjRoleRtRow
   */  
export function get_PrjRoleRts_Company_RoleCd_Seq(Company:string, RoleCd:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PrjRoleRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")", {
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
         resolve(data as Erp_Tablesets_PrjRoleRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PrjRoleRt for the service
   Description: Calls UpdateExt to update PrjRoleRt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PrjRoleRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PrjRoleRtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PrjRoleRts_Company_RoleCd_Seq(Company:string, RoleCd:string, Seq:string, requestBody:Erp_Tablesets_PrjRoleRtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete PrjRoleRt item
   Description: Call UpdateExt to delete PrjRoleRt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PrjRoleRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PrjRoleRts_Company_RoleCd_Seq(Company:string, RoleCd:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RoleCdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdListRow)
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
export function get_GetRows(whereClauseRoleCd:string, whereClausePrjRoleRt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRoleCd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRoleCd=" + whereClauseRoleCd
   }
   if(typeof whereClausePrjRoleRt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePrjRoleRt=" + whereClausePrjRoleRt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/GetRows" + params, {
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
export function get_GetByID(roleCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof roleCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "roleCode=" + roleCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/GetList" + params, {
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
   Summary: Invoke method ChangeSupervisorRole
   Description: Method to call when changing supervisor role.
   OperationID: ChangeSupervisorRole
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSupervisorRole_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupervisorRole_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSupervisorRole(requestBody:ChangeSupervisorRole_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSupervisorRole_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/ChangeSupervisorRole", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSupervisorRole_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCapabilityBefUpd
   OperationID: CheckCapabilityBefUpd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCapabilityBefUpd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCapabilityBefUpd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCapabilityBefUpd(requestBody:CheckCapabilityBefUpd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCapabilityBefUpd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/CheckCapabilityBefUpd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckCapabilityBefUpd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateOKDelete
   Description: Method used to validate if the Role Code is currently in use by operations,
employees or projects
   OperationID: ValidateOKDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateOKDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOKDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOKDelete(requestBody:ValidateOKDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateOKDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/ValidateOKDelete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateOKDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRoleCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRoleCd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRoleCd(requestBody:GetNewRoleCd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRoleCd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/GetNewRoleCd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRoleCd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPrjRoleRt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPrjRoleRt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPrjRoleRt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPrjRoleRt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPrjRoleRt(requestBody:GetNewPrjRoleRt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPrjRoleRt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/GetNewPrjRoleRt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPrjRoleRt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PrjRoleRtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PrjRoleRtRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RoleCdListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RoleCdRow,
}

export interface Erp_Tablesets_PrjRoleRtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Role Code  */  
   "RoleCd":string,
      /**  The effective date of the project role code rate.  */  
   "RateEffDte":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Time Type Code  */  
   "TimeTypCd":string,
      /**  The charge rate for role code expressed in the designated currency code.  */  
   "Rate":number,
      /**  The end date of the project role code rate.  */  
   "RateEndDte":string,
      /**  Sequence field used to keep the primary key unique  */  
   "Seq":number,
      /**  Marks this PrjRoleRt as global, available to be sent out to other companies.  */  
   "GlobalPrjRoleRt":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "RoleCdRoleDescription":string,
   "TimeTypCdDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RoleCdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this role assigned by the user.  */  
   "RoleCode":string,
      /**  A description of the role.  */  
   "RoleDescription":string,
      /**  Determines whether or not this role is available in certain drop-down selection lists.  */  
   "Inactive":boolean,
      /**  Determines whether or not this role is a commisionable role.  */  
   "Commissionable":boolean,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "ResourceGrpID":string,
      /**  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  */  
   "UseResGrp":boolean,
      /**  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  */  
   "TimeApprover":boolean,
      /**  Determines if this Role includes the ability to be chosen as a Expense Approver.  */  
   "ExpenseApprover":boolean,
      /**  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  */  
   "EmployeeRole":boolean,
      /**  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   "ApprovalSupervisorLevel":number,
      /**  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  */  
   "SupervisorRole":boolean,
      /**  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  */  
   "ProjectMgrRole":boolean,
      /**  Marks this RoleCd as global, available to be sent out to other companies.  */  
   "GlobalRoleCd":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  */  
   "UseResGrpDisable":boolean,
      /**  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  */  
   "TEAppRequired":boolean,
      /**  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  */  
   "TEApprovalRole":boolean,
      /**  Long description of the Resource Group.  */  
   "ResourceGroupDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RoleCdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this role assigned by the user.  */  
   "RoleCode":string,
      /**  A description of the role.  */  
   "RoleDescription":string,
      /**  Determines whether or not this role is available in certain drop-down selection lists.  */  
   "Inactive":boolean,
      /**  Determines whether or not this role is a commisionable role.  */  
   "Commissionable":boolean,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "ResourceGrpID":string,
      /**  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  */  
   "UseResGrp":boolean,
      /**  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  */  
   "TimeApprover":boolean,
      /**  Determines if this Role includes the ability to be chosen as a Expense Approver.  */  
   "ExpenseApprover":boolean,
      /**  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  */  
   "EmployeeRole":boolean,
      /**  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   "ApprovalSupervisorLevel":number,
      /**  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  */  
   "SupervisorRole":boolean,
      /**  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  */  
   "ProjectMgrRole":boolean,
      /**  Marks this RoleCd as global, available to be sent out to other companies.  */  
   "GlobalRoleCd":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  */  
   "UseResGrpDisable":boolean,
      /**  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  */  
   "TEAppRequired":boolean,
      /**  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  */  
   "TEApprovalRole":boolean,
   "BitFlag":number,
   "ResourceGroupDescription":string,
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
      @param ProposedSupervisorRole
      @param ds
   */  
export interface ChangeSupervisorRole_input{
      /**  The proposed supervisor role value  */  
   ProposedSupervisorRole:boolean,
   ds:Erp_Tablesets_RoleCdTableset[],
}

export interface ChangeSupervisorRole_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RoleCdTableset,
}
}

   /** Required : 
      @param iCapabilityID
      @param iDescription
      @param iResourceGrpID
   */  
export interface CheckCapabilityBefUpd_input{
   iCapabilityID:string,
   iDescription:string,
   iResourceGrpID:string,
}

export interface CheckCapabilityBefUpd_output{
parameters : {
      /**  output parameters  */  
   oResourceGrp:number,
}
}

   /** Required : 
      @param roleCode
   */  
export interface DeleteByID_input{
   roleCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PrjRoleRtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Role Code  */  
   RoleCd:string,
      /**  The effective date of the project role code rate.  */  
   RateEffDte:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Time Type Code  */  
   TimeTypCd:string,
      /**  The charge rate for role code expressed in the designated currency code.  */  
   Rate:number,
      /**  The end date of the project role code rate.  */  
   RateEndDte:string,
      /**  Sequence field used to keep the primary key unique  */  
   Seq:number,
      /**  Marks this PrjRoleRt as global, available to be sent out to other companies.  */  
   GlobalPrjRoleRt:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CurrencyDocumentDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   RoleCdRoleDescription:string,
   TimeTypCdDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RoleCdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this role assigned by the user.  */  
   RoleCode:string,
      /**  A description of the role.  */  
   RoleDescription:string,
      /**  Determines whether or not this role is available in certain drop-down selection lists.  */  
   Inactive:boolean,
      /**  Determines whether or not this role is a commisionable role.  */  
   Commissionable:boolean,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  */  
   UseResGrp:boolean,
      /**  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  */  
   TimeApprover:boolean,
      /**  Determines if this Role includes the ability to be chosen as a Expense Approver.  */  
   ExpenseApprover:boolean,
      /**  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  */  
   EmployeeRole:boolean,
      /**  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   ApprovalSupervisorLevel:number,
      /**  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  */  
   SupervisorRole:boolean,
      /**  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  */  
   ProjectMgrRole:boolean,
      /**  Marks this RoleCd as global, available to be sent out to other companies.  */  
   GlobalRoleCd:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  */  
   UseResGrpDisable:boolean,
      /**  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  */  
   TEAppRequired:boolean,
      /**  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  */  
   TEApprovalRole:boolean,
      /**  Long description of the Resource Group.  */  
   ResourceGroupDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RoleCdListTableset{
   RoleCdList:Erp_Tablesets_RoleCdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RoleCdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this role assigned by the user.  */  
   RoleCode:string,
      /**  A description of the role.  */  
   RoleDescription:string,
      /**  Determines whether or not this role is available in certain drop-down selection lists.  */  
   Inactive:boolean,
      /**  Determines whether or not this role is a commisionable role.  */  
   Commissionable:boolean,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  */  
   UseResGrp:boolean,
      /**  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  */  
   TimeApprover:boolean,
      /**  Determines if this Role includes the ability to be chosen as a Expense Approver.  */  
   ExpenseApprover:boolean,
      /**  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  */  
   EmployeeRole:boolean,
      /**  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   ApprovalSupervisorLevel:number,
      /**  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  */  
   SupervisorRole:boolean,
      /**  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  */  
   ProjectMgrRole:boolean,
      /**  Marks this RoleCd as global, available to be sent out to other companies.  */  
   GlobalRoleCd:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  */  
   UseResGrpDisable:boolean,
      /**  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  */  
   TEAppRequired:boolean,
      /**  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  */  
   TEApprovalRole:boolean,
   BitFlag:number,
   ResourceGroupDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RoleCdTableset{
   RoleCd:Erp_Tablesets_RoleCdRow[],
   PrjRoleRt:Erp_Tablesets_PrjRoleRtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRoleCdTableset{
   RoleCd:Erp_Tablesets_RoleCdRow[],
   PrjRoleRt:Erp_Tablesets_PrjRoleRtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param roleCode
   */  
export interface GetByID_input{
   roleCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RoleCdTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RoleCdTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RoleCdTableset[],
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
   returnObj:Erp_Tablesets_RoleCdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param roleCd
   */  
export interface GetNewPrjRoleRt_input{
   ds:Erp_Tablesets_RoleCdTableset[],
   roleCd:string,
}

export interface GetNewPrjRoleRt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RoleCdTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRoleCd_input{
   ds:Erp_Tablesets_RoleCdTableset[],
}

export interface GetNewRoleCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RoleCdTableset,
}
}

   /** Required : 
      @param whereClauseRoleCd
      @param whereClausePrjRoleRt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRoleCd:string,
   whereClausePrjRoleRt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RoleCdTableset[],
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
   ds:Erp_Tablesets_UpdExtRoleCdTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRoleCdTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RoleCdTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RoleCdTableset,
}
}

   /** Required : 
      @param ipRoleCode
   */  
export interface ValidateOKDelete_input{
      /**  The role code value  */  
   ipRoleCode:string,
}

export interface ValidateOKDelete_output{
parameters : {
      /**  output parameters  */  
   opOKDelete:boolean,
}
}

