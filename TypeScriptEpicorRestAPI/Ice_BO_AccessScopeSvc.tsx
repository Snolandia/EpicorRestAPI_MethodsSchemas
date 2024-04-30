import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.AccessScopeSvc
// Description: AccessScope service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/$metadata", {
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
   Description: Get AccessScopes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccessScopes
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeRow
   */  
export function get_AccessScopes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccessScopes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AccessScopeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.AccessScopeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AccessScopes(requestBody:Ice_Tablesets_AccessScopeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes", {
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
   Summary: Calls GetByID to retrieve the AccessScope item
   Description: Calls GetByID to retrieve the AccessScope item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScope
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.AccessScopeRow
   */  
export function get_AccessScopes_Company_AccessScopeID(Company:string, AccessScopeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AccessScopeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")", {
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
         resolve(data as Ice_Tablesets_AccessScopeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AccessScope for the service
   Description: Calls UpdateExt to update AccessScope. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccessScope
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.AccessScopeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AccessScopes_Company_AccessScopeID(Company:string, AccessScopeID:string, requestBody:Ice_Tablesets_AccessScopeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")", {
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
   Summary: Call UpdateExt to delete AccessScope item
   Description: Call UpdateExt to delete AccessScope item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccessScope
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AccessScopes_Company_AccessScopeID(Company:string, AccessScopeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")", {
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
   Description: Get AccessScopeEntities items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AccessScopeEntities1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeEntityRow
   */  
export function get_AccessScopes_Company_AccessScopeID_AccessScopeEntities(Company:string, AccessScopeID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")/AccessScopeEntities", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AccessScopeEntity item
   Description: Calls GetByID to retrieve the AccessScopeEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeEntity1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   */  
export function get_AccessScopes_Company_AccessScopeID_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AccessScopeEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")", {
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
         resolve(data as Ice_Tablesets_AccessScopeEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AccessScopeEntities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccessScopeEntities
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeEntityRow
   */  
export function get_AccessScopeEntities(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccessScopeEntities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.AccessScopeEntityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AccessScopeEntities(requestBody:Ice_Tablesets_AccessScopeEntityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities", {
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
   Summary: Calls GetByID to retrieve the AccessScopeEntity item
   Description: Calls GetByID to retrieve the AccessScopeEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   */  
export function get_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AccessScopeEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")", {
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
         resolve(data as Ice_Tablesets_AccessScopeEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AccessScopeEntity for the service
   Description: Calls UpdateExt to update AccessScopeEntity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccessScopeEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, requestBody:Ice_Tablesets_AccessScopeEntityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")", {
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
   Summary: Call UpdateExt to delete AccessScopeEntity item
   Description: Call UpdateExt to delete AccessScopeEntity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccessScopeEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")", {
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
   Description: Get AccessScopeBOMethods items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AccessScopeBOMethods1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeBOMethodRow
   */  
export function get_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID_AccessScopeBOMethods(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeBOMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")/AccessScopeBOMethods", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeBOMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AccessScopeBOMethod item
   Description: Calls GetByID to retrieve the AccessScopeBOMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeBOMethod1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param MethodID Desc: MethodID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   */  
export function get_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, MethodID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AccessScopeBOMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")", {
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
         resolve(data as Ice_Tablesets_AccessScopeBOMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AccessScopeBOMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccessScopeBOMethods
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeBOMethodRow
   */  
export function get_AccessScopeBOMethods(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeBOMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeBOMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccessScopeBOMethods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AccessScopeBOMethods(requestBody:Ice_Tablesets_AccessScopeBOMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods", {
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
   Summary: Calls GetByID to retrieve the AccessScopeBOMethod item
   Description: Calls GetByID to retrieve the AccessScopeBOMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeBOMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param MethodID Desc: MethodID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   */  
export function get_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, MethodID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AccessScopeBOMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")", {
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
         resolve(data as Ice_Tablesets_AccessScopeBOMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AccessScopeBOMethod for the service
   Description: Calls UpdateExt to update AccessScopeBOMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccessScopeBOMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param MethodID Desc: MethodID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, MethodID:string, requestBody:Ice_Tablesets_AccessScopeBOMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")", {
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
   Summary: Call UpdateExt to delete AccessScopeBOMethod item
   Description: Call UpdateExt to delete AccessScopeBOMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccessScopeBOMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AccessScopeID Desc: AccessScopeID   Required: True   Allow empty value : True
      @param EntityType Desc: EntityType   Required: True   Allow empty value : True
      @param EntityID Desc: EntityID   Required: True   Allow empty value : True
      @param MethodID Desc: MethodID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company:string, AccessScopeID:string, EntityType:string, EntityID:string, MethodID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeListRow)
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
export function get_GetRows(whereClauseAccessScope:string, whereClauseAccessScopeEntity:string, whereClauseAccessScopeBOMethod:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAccessScope!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAccessScope=" + whereClauseAccessScope
   }
   if(typeof whereClauseAccessScopeEntity!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAccessScopeEntity=" + whereClauseAccessScopeEntity
   }
   if(typeof whereClauseAccessScopeBOMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAccessScopeBOMethod=" + whereClauseAccessScopeBOMethod
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, accessScopeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof accessScopeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "accessScopeID=" + accessScopeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetList" + params, {
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
   Summary: Invoke method GetServiceMethodList
   Description: This method returns a delimited list of the public methods for the given
object.  This could be used to provide a "picker list" as a starting point
when adding a new Security record related to a method.  These would look the
same as a Security record for an object, but with a SecCode field that has
been appended with "." + MethodName.
For example, a security record for the
   OperationID: GetServiceMethodList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetServiceMethodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServiceMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetServiceMethodList(requestBody:GetServiceMethodList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetServiceMethodList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetServiceMethodList", {
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
         resolve(data as GetServiceMethodList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AccessScopeAllowFunctionExecution
   Description: Returns true if the AccessScope library function is authorized.
   OperationID: AccessScopeAllowFunctionExecution
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AccessScopeAllowFunctionExecution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AccessScopeAllowFunctionExecution_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AccessScopeAllowFunctionExecution(requestBody:AccessScopeAllowFunctionExecution_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AccessScopeAllowFunctionExecution_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeAllowFunctionExecution", {
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
         resolve(data as AccessScopeAllowFunctionExecution_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyAccessSope
   Description: Copy an existing AccessScope to a new AccessScope row
   OperationID: CopyAccessSope
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyAccessSope_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyAccessSope_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyAccessSope(requestBody:CopyAccessSope_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyAccessSope_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/CopyAccessSope", {
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
         resolve(data as CopyAccessSope_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAccessScope
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAccessScope
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAccessScope_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAccessScope_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAccessScope(requestBody:GetNewAccessScope_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAccessScope_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetNewAccessScope", {
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
         resolve(data as GetNewAccessScope_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAccessScopeEntity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAccessScopeEntity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAccessScopeEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAccessScopeEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAccessScopeEntity(requestBody:GetNewAccessScopeEntity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAccessScopeEntity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetNewAccessScopeEntity", {
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
         resolve(data as GetNewAccessScopeEntity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAccessScopeBOMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAccessScopeBOMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAccessScopeBOMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAccessScopeBOMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAccessScopeBOMethod(requestBody:GetNewAccessScopeBOMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAccessScopeBOMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetNewAccessScopeBOMethod", {
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
         resolve(data as GetNewAccessScopeBOMethod_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeBOMethodRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AccessScopeBOMethodRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeEntityRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AccessScopeEntityRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AccessScopeListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AccessScopeRow,
}

export interface Ice_Tablesets_AccessScopeBOMethodRow{
      /**  Company  */  
   "Company":string,
      /**  AccessScopeID  */  
   "AccessScopeID":string,
      /**  EntityType  */  
   "EntityType":string,
      /**  EntityID  */  
   "EntityID":string,
      /**  MethodID  */  
   "MethodID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_AccessScopeEntityRow{
      /**  Company  */  
   "Company":string,
      /**  AccessScopeID  */  
   "AccessScopeID":string,
      /**  EntityType  */  
   "EntityType":string,
      /**  EntityID  */  
   "EntityID":string,
      /**  EntityDescription  */  
   "EntityDescription":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_AccessScopeListRow{
      /**  Company  */  
   "Company":string,
      /**  AccessScopeID  */  
   "AccessScopeID":string,
      /**  Description  */  
   "Description":string,
      /**  AllowExemptBO  */  
   "AllowExemptBO":boolean,
      /**  IsActive  */  
   "IsActive":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_AccessScopeRow{
      /**  Company  */  
   "Company":string,
      /**  AccessScopeID  */  
   "AccessScopeID":string,
      /**  Description  */  
   "Description":string,
      /**  AllowExemptBO  */  
   "AllowExemptBO":boolean,
      /**  IsActive  */  
   "IsActive":boolean,
      /**  CompanyVisibility  */  
   "CompanyVisibility":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  All Companies Flag  */  
   "AllCompanies":boolean,
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
      @param libraryID
      @param functionID
   */  
export interface AccessScopeAllowFunctionExecution_input{
      /**  The entity id or library name.  */  
   libraryID:string,
      /**  The method or function name.  */  
   functionID:string,
}

export interface AccessScopeAllowFunctionExecution_output{
      /**  true|false  */  
   returnObj:boolean,
}

   /** Required : 
      @param sourceCompany
      @param sourceAccessID
      @param targetsourceAccessID
      @param targetDescription
   */  
export interface CopyAccessSope_input{
      /**  Existing Menu Company  */  
   sourceCompany:string,
      /**  Source Access scope ID  */  
   sourceAccessID:string,
      /**  New Access scope ID  */  
   targetsourceAccessID:string,
      /**  New Access scope description  */  
   targetDescription:string,
}

export interface CopyAccessSope_output{
   returnObj:Ice_Tablesets_AccessScopeTableset[],
}

   /** Required : 
      @param company
      @param accessScopeID
   */  
export interface DeleteByID_input{
   company:string,
   accessScopeID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param company
      @param accessScopeID
   */  
export interface GetByID_input{
   company:string,
   accessScopeID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_AccessScopeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_AccessScopeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_AccessScopeTableset[],
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
   returnObj:Ice_Tablesets_AccessScopeListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param accessScopeID
      @param entityType
      @param entityID
   */  
export interface GetNewAccessScopeBOMethod_input{
   ds:Ice_Tablesets_AccessScopeTableset[],
   company:string,
   accessScopeID:string,
   entityType:string,
   entityID:string,
}

export interface GetNewAccessScopeBOMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AccessScopeTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param accessScopeID
      @param entityType
   */  
export interface GetNewAccessScopeEntity_input{
   ds:Ice_Tablesets_AccessScopeTableset[],
   company:string,
   accessScopeID:string,
   entityType:string,
}

export interface GetNewAccessScopeEntity_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AccessScopeTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewAccessScope_input{
   ds:Ice_Tablesets_AccessScopeTableset[],
   company:string,
}

export interface GetNewAccessScope_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AccessScopeTableset,
}
}

   /** Required : 
      @param whereClauseAccessScope
      @param whereClauseAccessScopeEntity
      @param whereClauseAccessScopeBOMethod
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAccessScope:string,
   whereClauseAccessScopeEntity:string,
   whereClauseAccessScopeBOMethod:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_AccessScopeTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param service
   */  
export interface GetServiceMethodList_input{
      /**  The security code for which you want the list of methods.  */  
   service:string,
}

export interface GetServiceMethodList_output{
   returnObj:Ice_Tablesets_AccessScopeMethodsTableset[],
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

export interface Ice_Tablesets_AccessScopeBOMethodRow{
      /**  Company  */  
   Company:string,
      /**  AccessScopeID  */  
   AccessScopeID:string,
      /**  EntityType  */  
   EntityType:string,
      /**  EntityID  */  
   EntityID:string,
      /**  MethodID  */  
   MethodID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AccessScopeEntityRow{
      /**  Company  */  
   Company:string,
      /**  AccessScopeID  */  
   AccessScopeID:string,
      /**  EntityType  */  
   EntityType:string,
      /**  EntityID  */  
   EntityID:string,
      /**  EntityDescription  */  
   EntityDescription:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AccessScopeListRow{
      /**  Company  */  
   Company:string,
      /**  AccessScopeID  */  
   AccessScopeID:string,
      /**  Description  */  
   Description:string,
      /**  AllowExemptBO  */  
   AllowExemptBO:boolean,
      /**  IsActive  */  
   IsActive:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AccessScopeListTableset{
   AccessScopeList:Ice_Tablesets_AccessScopeListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_AccessScopeMethodsRow{
      /**  Method Name  */  
   MethodName:string,
      /**  Service Name  */  
   Service:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AccessScopeMethodsTableset{
   AccessScopeMethods:Ice_Tablesets_AccessScopeMethodsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_AccessScopeRow{
      /**  Company  */  
   Company:string,
      /**  AccessScopeID  */  
   AccessScopeID:string,
      /**  Description  */  
   Description:string,
      /**  AllowExemptBO  */  
   AllowExemptBO:boolean,
      /**  IsActive  */  
   IsActive:boolean,
      /**  CompanyVisibility  */  
   CompanyVisibility:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  All Companies Flag  */  
   AllCompanies:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AccessScopeTableset{
   AccessScope:Ice_Tablesets_AccessScopeRow[],
   AccessScopeEntity:Ice_Tablesets_AccessScopeEntityRow[],
   AccessScopeBOMethod:Ice_Tablesets_AccessScopeBOMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtAccessScopeTableset{
   AccessScope:Ice_Tablesets_AccessScopeRow[],
   AccessScopeEntity:Ice_Tablesets_AccessScopeEntityRow[],
   AccessScopeBOMethod:Ice_Tablesets_AccessScopeBOMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtAccessScopeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtAccessScopeTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_AccessScopeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AccessScopeTableset,
}
}

