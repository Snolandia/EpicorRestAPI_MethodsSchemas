import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.TranDocTypeSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/$metadata", {
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
   Description: Get TranDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TranDocTypes
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeRow
   */  
export function get_TranDocTypes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TranDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TranDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TranDocTypes(requestBody:Erp_Tablesets_TranDocTypeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes", {
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
   Summary: Calls GetByID to retrieve the TranDocType item
   Description: Calls GetByID to retrieve the TranDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TranDocTypeRow
   */  
export function get_TranDocTypes_Company_TranDocTypeID(Company:string, TranDocTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TranDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")", {
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
         resolve(data as Erp_Tablesets_TranDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TranDocType for the service
   Description: Calls UpdateExt to update TranDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TranDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TranDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TranDocTypes_Company_TranDocTypeID(Company:string, TranDocTypeID:string, requestBody:Erp_Tablesets_TranDocTypeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")", {
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
   Summary: Call UpdateExt to delete TranDocType item
   Description: Call UpdateExt to delete TranDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TranDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TranDocTypes_Company_TranDocTypeID(Company:string, TranDocTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")", {
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
   Description: Get TranDocTypeAuths items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TranDocTypeAuths1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeAuthRow
   */  
export function get_TranDocTypes_Company_TranDocTypeID_TranDocTypeAuths(Company:string, TranDocTypeID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")/TranDocTypeAuths", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TranDocTypeAuth item
   Description: Calls GetByID to retrieve the TranDocTypeAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranDocTypeAuth1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   */  
export function get_TranDocTypes_Company_TranDocTypeID_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company:string, TranDocTypeID:string, DcdUserID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TranDocTypeAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypes(" + Company + "," + TranDocTypeID + ")/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")", {
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
         resolve(data as Erp_Tablesets_TranDocTypeAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TranDocTypeAuths items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TranDocTypeAuths
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeAuthRow
   */  
export function get_TranDocTypeAuths(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TranDocTypeAuths
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TranDocTypeAuths(requestBody:Erp_Tablesets_TranDocTypeAuthRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths", {
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
   Summary: Calls GetByID to retrieve the TranDocTypeAuth item
   Description: Calls GetByID to retrieve the TranDocTypeAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranDocTypeAuth
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   */  
export function get_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company:string, TranDocTypeID:string, DcdUserID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TranDocTypeAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")", {
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
         resolve(data as Erp_Tablesets_TranDocTypeAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TranDocTypeAuth for the service
   Description: Calls UpdateExt to update TranDocTypeAuth. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TranDocTypeAuth
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TranDocTypeAuthRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company:string, TranDocTypeID:string, DcdUserID:string, requestBody:Erp_Tablesets_TranDocTypeAuthRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")", {
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
   Summary: Call UpdateExt to delete TranDocTypeAuth item
   Description: Call UpdateExt to delete TranDocTypeAuth item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TranDocTypeAuth
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TranDocTypeAuths_Company_TranDocTypeID_DcdUserID(Company:string, TranDocTypeID:string, DcdUserID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuths(" + Company + "," + TranDocTypeID + "," + DcdUserID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranDocTypeListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeListRow)
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
export function get_GetRows(whereClauseTranDocType:string, whereClauseTranDocTypeAuth:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTranDocType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTranDocType=" + whereClauseTranDocType
   }
   if(typeof whereClauseTranDocTypeAuth!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTranDocTypeAuth=" + whereClauseTranDocTypeAuth
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetRows" + params, {
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
export function get_GetByID(tranDocTypeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tranDocTypeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranDocTypeID=" + tranDocTypeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetByID" + params, {
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
   Summary: Invoke method OnChangeAllUsers
   Description: This method validates All Users flag.
   OperationID: OnChangeAllUsers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAllUsers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllUsers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAllUsers(requestBody:OnChangeAllUsers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAllUsers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/OnChangeAllUsers", {
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
         resolve(data as OnChangeAllUsers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAuthUser
   Description: This method check if the selected User has alreay default Transaction
Document Type.for this type to update flag Default correctly.
   OperationID: OnChangeAuthUser
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAuthUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAuthUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAuthUser(requestBody:OnChangeAuthUser_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAuthUser_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/OnChangeAuthUser", {
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
         resolve(data as OnChangeAuthUser_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeELIDefReportID
   Description: OnChangeELIDefReportID
   OperationID: OnChangeELIDefReportID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeELIDefReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeELIDefReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeELIDefReportID(requestBody:OnChangeELIDefReportID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeELIDefReportID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/OnChangeELIDefReportID", {
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
         resolve(data as OnChangeELIDefReportID_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetCodeDescList", {
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
   Summary: Invoke method TranDocTypeAuthValidate
   Description: Check for TranDocTypeAuth is unique
   OperationID: TranDocTypeAuthValidate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TranDocTypeAuthValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TranDocTypeAuthValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TranDocTypeAuthValidate(requestBody:TranDocTypeAuthValidate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TranDocTypeAuthValidate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/TranDocTypeAuthValidate", {
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
         resolve(data as TranDocTypeAuthValidate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistDefaultTranDocType
   OperationID: ExistDefaultTranDocType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistDefaultTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistDefaultTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistDefaultTranDocType(requestBody:ExistDefaultTranDocType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistDefaultTranDocType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/ExistDefaultTranDocType", {
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
         resolve(data as ExistDefaultTranDocType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePECode
   OperationID: OnChangePECode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePECode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePECode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePECode(requestBody:OnChangePECode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePECode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/OnChangePECode", {
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
         resolve(data as OnChangePECode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTranDocType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTranDocType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTranDocType(requestBody:GetNewTranDocType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTranDocType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetNewTranDocType", {
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
         resolve(data as GetNewTranDocType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTranDocTypeAuth
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTranDocTypeAuth
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTranDocTypeAuth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTranDocTypeAuth_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTranDocTypeAuth(requestBody:GetNewTranDocTypeAuth_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTranDocTypeAuth_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetNewTranDocTypeAuth", {
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
         resolve(data as GetNewTranDocTypeAuth_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranDocTypeSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeAuthRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TranDocTypeAuthRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TranDocTypeListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranDocTypeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TranDocTypeRow,
}

export interface Erp_Tablesets_TranDocTypeAuthRow{
      /**  Company  */  
   "Company":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  TranDocTypeAuthLine  */  
   "TranDocTypeAuthLine":number,
      /**  DcdUserID  */  
   "DcdUserID":string,
      /**  SystemTranID  */  
   "SystemTranID":string,
      /**  DefaultTranDocType  */  
   "DefaultTranDocType":boolean,
      /**  FirstForUser  */  
   "FirstForUser":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TranDocTypeListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Description  */  
   "Description":string,
      /**   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  */  
   "SystemTranID":string,
      /**  Indicates if the record is inactive  */  
   "Inactive":boolean,
      /**  Indicates if the document type is the default for the system transaction.  */  
   "SystemTranDefault":boolean,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   "GUIFormatCode":string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   "GUITaxTypeCode":string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   "GUIDeductCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  */  
   "EnableSystemTran":boolean,
      /**  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  */  
   "RowIDSystemTranDefault":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TranDocTypeRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Description  */  
   "Description":string,
      /**   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  */  
   "SystemTranID":string,
      /**  Indicates if the record is inactive  */  
   "Inactive":boolean,
      /**  Indicates if the document type is the default for the system transaction.  */  
   "SystemTranDefault":boolean,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   "GUIFormatCode":string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   "GUITaxTypeCode":string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   "GUIDeductCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAGIPCode  */  
   "AGAGIPCode":string,
      /**  AGARBACode  */  
   "AGARBACode":string,
      /**  AGCOMARBCode  */  
   "AGCOMARBCode":string,
      /**  AGDefaultLetter  */  
   "AGDefaultLetter":string,
      /**  Returns  */  
   "Returns":boolean,
      /**  AllUsers  */  
   "AllUsers":boolean,
      /**   Peru Localization Field.      
Non-Resident Invoices  */  
   "PENRInvoices":boolean,
      /**  EInvoice  */  
   "EInvoice":boolean,
      /**  PostTaxDeclaration  */  
   "PostTaxDeclaration":boolean,
      /**  TWGenerationType  */  
   "TWGenerationType":string,
      /**  Obsolete  */  
   "INIsExcisable":boolean,
      /**  INExportType  */  
   "INExportType":string,
      /**  Obsolete  */  
   "INPurchaseType":string,
      /**  Obsolete  */  
   "INIsServiceType":boolean,
      /**  Peru CSF: SUNAT Table 10  */  
   "PESunatTDT":string,
      /**  SelfInvoice  */  
   "SelfInvoice":boolean,
      /**  PESUNATDetOpType  */  
   "PESUNATDetOpType":string,
      /**  Peru invoice type  */  
   "PEInvoiceType":string,
      /**  Own Use  */  
   "MYOwnUse":boolean,
      /**  ELIEinvoice  */  
   "ELIEinvoice":boolean,
      /**  ELIDefaultEinvoice  */  
   "ELIDefaultEinvoice":boolean,
      /**  ELIDefReportID  */  
   "ELIDefReportID":string,
      /**  ELIDefStyleNum  */  
   "ELIDefStyleNum":number,
      /**  ELIDefToMail  */  
   "ELIDefToMail":string,
      /**  ELIDefCCMail  */  
   "ELIDefCCMail":string,
      /**  ELIDefMailTempID  */  
   "ELIDefMailTempID":string,
      /**  ELIDefFromMail  */  
   "ELIDefFromMail":string,
      /**  UNTDID 1001  */  
   "ExternalType":string,
      /**  Operator Code  */  
   "ELIOperatorCode":string,
      /**  Default E-invoice Report ID  */  
   "ELIRcptDefStyleNum":number,
      /**  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  */  
   "EnableSystemTran":boolean,
   "PEInvoiceTypeDesc":string,
   "RedStornoOpt":string,
      /**  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  */  
   "RowIDSystemTranDefault":string,
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
      @param tranDocTypeID
   */  
export interface DeleteByID_input{
   tranDocTypeID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TranDocTypeAuthRow{
      /**  Company  */  
   Company:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  TranDocTypeAuthLine  */  
   TranDocTypeAuthLine:number,
      /**  DcdUserID  */  
   DcdUserID:string,
      /**  SystemTranID  */  
   SystemTranID:string,
      /**  DefaultTranDocType  */  
   DefaultTranDocType:boolean,
      /**  FirstForUser  */  
   FirstForUser:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TranDocTypeListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Description  */  
   Description:string,
      /**   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  */  
   SystemTranID:string,
      /**  Indicates if the record is inactive  */  
   Inactive:boolean,
      /**  Indicates if the document type is the default for the system transaction.  */  
   SystemTranDefault:boolean,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  */  
   EnableSystemTran:boolean,
      /**  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  */  
   RowIDSystemTranDefault:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TranDocTypeListTableset{
   TranDocTypeList:Erp_Tablesets_TranDocTypeListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TranDocTypeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Description  */  
   Description:string,
      /**   The system transaction id assigned to the document type.  Values are:
ARInvoice - AR Invoices
CreditMemo - Credit Memos
PromNote - Promissory Notes
PackSlip - Packing Slips (Customer Shipments)
MiscShip - Miscellaneous Shipments
SCShip - Subcontractor Shipments
TOOrderShip - Transfer Order Shipments
WTaxCert - Withholding Tax Certificates  */  
   SystemTranID:string,
      /**  Indicates if the record is inactive  */  
   Inactive:boolean,
      /**  Indicates if the document type is the default for the system transaction.  */  
   SystemTranDefault:boolean,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAGIPCode  */  
   AGAGIPCode:string,
      /**  AGARBACode  */  
   AGARBACode:string,
      /**  AGCOMARBCode  */  
   AGCOMARBCode:string,
      /**  AGDefaultLetter  */  
   AGDefaultLetter:string,
      /**  Returns  */  
   Returns:boolean,
      /**  AllUsers  */  
   AllUsers:boolean,
      /**   Peru Localization Field.      
Non-Resident Invoices  */  
   PENRInvoices:boolean,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  PostTaxDeclaration  */  
   PostTaxDeclaration:boolean,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  Obsolete  */  
   INIsExcisable:boolean,
      /**  INExportType  */  
   INExportType:string,
      /**  Obsolete  */  
   INPurchaseType:string,
      /**  Obsolete  */  
   INIsServiceType:boolean,
      /**  Peru CSF: SUNAT Table 10  */  
   PESunatTDT:string,
      /**  SelfInvoice  */  
   SelfInvoice:boolean,
      /**  PESUNATDetOpType  */  
   PESUNATDetOpType:string,
      /**  Peru invoice type  */  
   PEInvoiceType:string,
      /**  Own Use  */  
   MYOwnUse:boolean,
      /**  ELIEinvoice  */  
   ELIEinvoice:boolean,
      /**  ELIDefaultEinvoice  */  
   ELIDefaultEinvoice:boolean,
      /**  ELIDefReportID  */  
   ELIDefReportID:string,
      /**  ELIDefStyleNum  */  
   ELIDefStyleNum:number,
      /**  ELIDefToMail  */  
   ELIDefToMail:string,
      /**  ELIDefCCMail  */  
   ELIDefCCMail:string,
      /**  ELIDefMailTempID  */  
   ELIDefMailTempID:string,
      /**  ELIDefFromMail  */  
   ELIDefFromMail:string,
      /**  UNTDID 1001  */  
   ExternalType:string,
      /**  Operator Code  */  
   ELIOperatorCode:string,
      /**  Default E-invoice Report ID  */  
   ELIRcptDefStyleNum:number,
      /**  According to the value of this field SystemTranDefault and Inactive field will be disable or enables.  */  
   EnableSystemTran:boolean,
   PEInvoiceTypeDesc:string,
   RedStornoOpt:string,
      /**  When SystemTranDefault is marked then looking for the previous SystranDefault, store the ID if is loaded in UI to updated it.  */  
   RowIDSystemTranDefault:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TranDocTypeTableset{
   TranDocType:Erp_Tablesets_TranDocTypeRow[],
   TranDocTypeAuth:Erp_Tablesets_TranDocTypeAuthRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTranDocTypeTableset{
   TranDocType:Erp_Tablesets_TranDocTypeRow[],
   TranDocTypeAuth:Erp_Tablesets_TranDocTypeAuthRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param systemTranID
      @param userID
   */  
export interface ExistDefaultTranDocType_input{
   systemTranID:string,
   userID:string,
}

export interface ExistDefaultTranDocType_output{
   returnObj:boolean,
}

   /** Required : 
      @param tranDocTypeID
   */  
export interface GetByID_input{
   tranDocTypeID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TranDocTypeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TranDocTypeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TranDocTypeTableset[],
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
   returnObj:Erp_Tablesets_TranDocTypeListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param tranDocTypeID
   */  
export interface GetNewTranDocTypeAuth_input{
   ds:Erp_Tablesets_TranDocTypeTableset[],
   tranDocTypeID:string,
}

export interface GetNewTranDocTypeAuth_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDocTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTranDocType_input{
   ds:Erp_Tablesets_TranDocTypeTableset[],
}

export interface GetNewTranDocType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDocTypeTableset,
}
}

   /** Required : 
      @param whereClauseTranDocType
      @param whereClauseTranDocTypeAuth
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTranDocType:string,
   whereClauseTranDocTypeAuth:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TranDocTypeTableset[],
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
      @param pAllUsers
   */  
export interface OnChangeAllUsers_input{
   ds:Erp_Tablesets_TranDocTypeTableset[],
      /**  The proposed All Users value  */  
   pAllUsers:boolean,
}

export interface OnChangeAllUsers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDocTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeAuthUser_input{
   ds:Erp_Tablesets_TranDocTypeTableset[],
}

export interface OnChangeAuthUser_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDocTypeTableset,
}
}

   /** Required : 
      @param eliDefReportID
      @param ds
   */  
export interface OnChangeELIDefReportID_input{
   eliDefReportID:string,
   ds:Erp_Tablesets_TranDocTypeTableset[],
}

export interface OnChangeELIDefReportID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDocTypeTableset,
}
}

   /** Required : 
      @param codeType
      @param ds
   */  
export interface OnChangePECode_input{
   codeType:string,
   ds:Erp_Tablesets_TranDocTypeTableset[],
}

export interface OnChangePECode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDocTypeTableset,
}
}

   /** Required : 
      @param tranDocTypeID
      @param dcdUserID
   */  
export interface TranDocTypeAuthValidate_input{
      /**  TranDocTypeID  */  
   tranDocTypeID:string,
      /**  DcdUserID  */  
   dcdUserID:string,
}

export interface TranDocTypeAuthValidate_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTranDocTypeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTranDocTypeTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TranDocTypeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDocTypeTableset,
}
}

