import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ResourceGroupSvc
// Description: Resource Group
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/$metadata", {
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
   Description: Get ResourceGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceGroups
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupRow
   */  
export function get_ResourceGroups(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceGroups
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ResourceGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResourceGroups(requestBody:Erp_Tablesets_ResourceGroupRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups", {
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
   Summary: Calls GetByID to retrieve the ResourceGroup item
   Description: Calls GetByID to retrieve the ResourceGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ResourceGroupRow
   */  
export function get_ResourceGroups_Company_ResourceGrpID(Company:string, ResourceGrpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")", {
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
         resolve(data as Erp_Tablesets_ResourceGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ResourceGroup for the service
   Description: Calls UpdateExt to update ResourceGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ResourceGroups_Company_ResourceGrpID(Company:string, ResourceGrpID:string, requestBody:Erp_Tablesets_ResourceGroupRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")", {
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
   Summary: Call UpdateExt to delete ResourceGroup item
   Description: Call UpdateExt to delete ResourceGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ResourceGroups_Company_ResourceGrpID(Company:string, ResourceGrpID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")", {
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
   Description: Get Resources items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Resources1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceRow
   */  
export function get_ResourceGroups_Company_ResourceGrpID_Resources(Company:string, ResourceGrpID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/Resources", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Resource item
   Description: Calls GetByID to retrieve the Resource item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Resource1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ResourceRow
   */  
export function get_ResourceGroups_Company_ResourceGrpID_Resources_Company_ResourceID(Company:string, ResourceGrpID:string, ResourceID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/Resources(" + Company + "," + ResourceID + ")", {
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
         resolve(data as Erp_Tablesets_ResourceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ResourceCals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ResourceCals1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   */  
export function get_ResourceGroups_Company_ResourceGrpID_ResourceCals(Company:string, ResourceGrpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceCals", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ResourceCalRow
   */  
export function get_ResourceGroups_Company_ResourceGrpID_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
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
         resolve(data as Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ResourceGroupAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ResourceGroupAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupAttchRow
   */  
export function get_ResourceGroups_Company_ResourceGrpID_ResourceGroupAttches(Company:string, ResourceGrpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceGroupAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ResourceGroupAttch item
   Description: Calls GetByID to retrieve the ResourceGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceGroupAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   */  
export function get_ResourceGroups_Company_ResourceGrpID_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company:string, ResourceGrpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ResourceGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get Resources items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Resources
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceRow
   */  
export function get_Resources(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Resources
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ResourceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Resources(requestBody:Erp_Tablesets_ResourceRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources", {
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
   Summary: Calls GetByID to retrieve the Resource item
   Description: Calls GetByID to retrieve the Resource item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Resource
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ResourceRow
   */  
export function get_Resources_Company_ResourceID(Company:string, ResourceID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")", {
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
         resolve(data as Erp_Tablesets_ResourceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Resource for the service
   Description: Calls UpdateExt to update Resource. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Resource
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Resources_Company_ResourceID(Company:string, ResourceID:string, requestBody:Erp_Tablesets_ResourceRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")", {
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
   Summary: Call UpdateExt to delete Resource item
   Description: Call UpdateExt to delete Resource item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Resource
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Resources_Company_ResourceID(Company:string, ResourceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")", {
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
   Description: Get CapResLnks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CapResLnks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapResLnkRow
   */  
export function get_Resources_Company_ResourceID_CapResLnks(Company:string, ResourceID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapResLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")/CapResLnks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapResLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CapResLnk item
   Description: Calls GetByID to retrieve the CapResLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CapResLnk1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param CapabilityID Desc: CapabilityID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CapResLnkRow
   */  
export function get_Resources_Company_ResourceID_CapResLnks_Company_CapabilityID_ResourceID(Company:string, ResourceID:string, CapabilityID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CapResLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")", {
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
         resolve(data as Erp_Tablesets_CapResLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CapResLnks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CapResLnks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapResLnkRow
   */  
export function get_CapResLnks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapResLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapResLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CapResLnks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CapResLnkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CapResLnkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CapResLnks(requestBody:Erp_Tablesets_CapResLnkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks", {
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
   Summary: Calls GetByID to retrieve the CapResLnk item
   Description: Calls GetByID to retrieve the CapResLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CapResLnk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CapabilityID Desc: CapabilityID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CapResLnkRow
   */  
export function get_CapResLnks_Company_CapabilityID_ResourceID(Company:string, CapabilityID:string, ResourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CapResLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")", {
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
         resolve(data as Erp_Tablesets_CapResLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CapResLnk for the service
   Description: Calls UpdateExt to update CapResLnk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CapResLnk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CapabilityID Desc: CapabilityID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CapResLnkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CapResLnks_Company_CapabilityID_ResourceID(Company:string, CapabilityID:string, ResourceID:string, requestBody:Erp_Tablesets_CapResLnkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")", {
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
   Summary: Call UpdateExt to delete CapResLnk item
   Description: Call UpdateExt to delete CapResLnk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CapResLnk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CapabilityID Desc: CapabilityID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CapResLnks_Company_CapabilityID_ResourceID(Company:string, CapabilityID:string, ResourceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")", {
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
   Description: Get ResourceCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceCals
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   */  
export function get_ResourceCals(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceCals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ResourceCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResourceCals(requestBody:Erp_Tablesets_ResourceCalRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals", {
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
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ResourceCalRow
   */  
export function get_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
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
         resolve(data as Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ResourceCal for the service
   Description: Calls UpdateExt to update ResourceCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, requestBody:Erp_Tablesets_ResourceCalRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
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
   Summary: Call UpdateExt to delete ResourceCal item
   Description: Call UpdateExt to delete ResourceCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
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
   Description: Get ResourceGroupAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceGroupAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupAttchRow
   */  
export function get_ResourceGroupAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceGroupAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResourceGroupAttches(requestBody:Erp_Tablesets_ResourceGroupAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches", {
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
   Summary: Calls GetByID to retrieve the ResourceGroupAttch item
   Description: Calls GetByID to retrieve the ResourceGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceGroupAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   */  
export function get_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company:string, ResourceGrpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ResourceGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ResourceGroupAttch for the service
   Description: Calls UpdateExt to update ResourceGroupAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceGroupAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company:string, ResourceGrpID:string, DrawingSeq:string, requestBody:Erp_Tablesets_ResourceGroupAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ResourceGroupAttch item
   Description: Call UpdateExt to delete ResourceGroupAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceGroupAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company:string, ResourceGrpID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupListRow)
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
export function get_GetRows(whereClauseResourceGroup:string, whereClauseResourceGroupAttch:string, whereClauseResource:string, whereClauseCapResLnk:string, whereClauseResourceCal:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseResourceGroup!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseResourceGroup=" + whereClauseResourceGroup
   }
   if(typeof whereClauseResourceGroupAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseResourceGroupAttch=" + whereClauseResourceGroupAttch
   }
   if(typeof whereClauseResource!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseResource=" + whereClauseResource
   }
   if(typeof whereClauseCapResLnk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCapResLnk=" + whereClauseCapResLnk
   }
   if(typeof whereClauseResourceCal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseResourceCal=" + whereClauseResourceCal
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetRows" + params, {
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
export function get_GetByID(resourceGrpID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof resourceGrpID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "resourceGrpID=" + resourceGrpID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetCodeDescList", {
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
   Summary: Invoke method SelectDistinctInOutWhseQuery
   OperationID: SelectDistinctInOutWhseQuery
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectDistinctInOutWhseQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectDistinctInOutWhseQuery(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectDistinctInOutWhseQuery_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/SelectDistinctInOutWhseQuery", {
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
         resolve(data as SelectDistinctInOutWhseQuery_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildRsrcGrpResourceCalList
   Description: This method will populate the ttResourceCal table using the resource group
that was passed in.
   OperationID: BuildRsrcGrpResourceCalList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildRsrcGrpResourceCalList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildRsrcGrpResourceCalList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildRsrcGrpResourceCalList(requestBody:BuildRsrcGrpResourceCalList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildRsrcGrpResourceCalList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/BuildRsrcGrpResourceCalList", {
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
         resolve(data as BuildRsrcGrpResourceCalList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildRsrcResourceCalList
   Description: This method will populate the ttResourceCal table using the resource group
that was passed in.
   OperationID: BuildRsrcResourceCalList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildRsrcResourceCalList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildRsrcResourceCalList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildRsrcResourceCalList(requestBody:BuildRsrcResourceCalList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildRsrcResourceCalList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/BuildRsrcResourceCalList", {
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
         resolve(data as BuildRsrcResourceCalList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRGPlant
   Description: This method will verify that the Resource Group ID entered is from the Current
plant.
   OperationID: CheckRGPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRGPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRGPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRGPlant(requestBody:CheckRGPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRGPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CheckRGPlant", {
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
         resolve(data as CheckRGPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CustomizeResourceCalRsrc
   Description: This method will get a current ResourceCal record or create a temporary
ResourceCal record to be modified for a RESOURCE.  The ProdHours will be
defaulted from the weekday of the selected date.  If any changes are made
to the ttResourceCal record, the UpdateResourceCal method will have to be
called to write the temporary ResourceCal record to the database.
   OperationID: CustomizeResourceCalRsrc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomizeResourceCalRsrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeResourceCalRsrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomizeResourceCalRsrc(requestBody:CustomizeResourceCalRsrc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomizeResourceCalRsrc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CustomizeResourceCalRsrc", {
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
         resolve(data as CustomizeResourceCalRsrc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CustomizeResourceCalRsrcGrp
   Description: This method will get a current ResourceCal record or create a temporary
ResourceCal record to be modified for a RESOURCE GROUP.  The ProdHours
will be defaulted from the weekday of the selected date.  If any changes
are made to the ttResourceCal record, the UpdateResourceCal method will have
to be called to write the temporary ResourceCal record to the database.
   OperationID: CustomizeResourceCalRsrcGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomizeResourceCalRsrcGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeResourceCalRsrcGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomizeResourceCalRsrcGrp(requestBody:CustomizeResourceCalRsrcGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomizeResourceCalRsrcGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CustomizeResourceCalRsrcGrp", {
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
         resolve(data as CustomizeResourceCalRsrcGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteResourceCal
   Description: This method will delete ResourceCal record.
   OperationID: DeleteResourceCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteResourceCal(requestBody:DeleteResourceCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteResourceCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/DeleteResourceCal", {
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
         resolve(data as DeleteResourceCal_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/EnterpriseGetList", {
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
   Summary: Invoke method InsertNewResource
   Description: This method creates a new Resource after prompting for the
ResourceID and ResourceGrpID.
This is to replace the standard GetNewResource .
   OperationID: InsertNewResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InsertNewResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertNewResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertNewResource(requestBody:InsertNewResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InsertNewResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/InsertNewResource", {
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
         resolve(data as InsertNewResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveResource
   Description: This method creates a new Resource after prompting for the
ResourceID and ResourceGrpID.
This is to replace the standard GetNewResource .
   OperationID: MoveResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveResource(requestBody:MoveResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/MoveResource", {
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
         resolve(data as MoveResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveResourceCal
   Description: This method will change SpecialDay of ResourceCal record.
   OperationID: MoveResourceCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveResourceCal(requestBody:MoveResourceCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveResourceCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/MoveResourceCal", {
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
         resolve(data as MoveResourceCal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetInactiveFlag
   Description: Call this method when the Inactive Flag on the Resource Group changes and the
user answer "Yes" to set the inactive flag on the Resources.  All of the
Resources Inactive flags will be set to equal to the new inactive setting on the
Resource Group.
   OperationID: SetInactiveFlag
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetInactiveFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInactiveFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetInactiveFlag(requestBody:SetInactiveFlag_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetInactiveFlag_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/SetInactiveFlag", {
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
         resolve(data as SetInactiveFlag_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateResourceCal
   Description: This method will check to see if the current ttResourceCal record was modified.
If it was modified then it compares the capacity from the ttResourceCal
the capacity of the production calendar for that day of the week.  If they
are different, or if it is a special working day or non-working day then
it save the ttResourceCal record to the database.
   OperationID: UpdateResourceCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateResourceCal(requestBody:UpdateResourceCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateResourceCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/UpdateResourceCal", {
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
         resolve(data as UpdateResourceCal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateInspection
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ValidateInspection", {
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
   Summary: Invoke method ValidateResource
   Description: This method validates that the Resource exists and that it isn't assigned to
another Resource Group.
   OperationID: ValidateResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateResource(requestBody:ValidateResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ValidateResource", {
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
         resolve(data as ValidateResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   Description: Purpose:
Parameters:  none
Notes:
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetIfCurrentSiteHasExternalMES", {
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
   Summary: Invoke method RequestExternalMESActiveResourceTypeValidation
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: RequestExternalMESActiveResourceTypeValidation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RequestExternalMESActiveResourceTypeValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestExternalMESActiveResourceTypeValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RequestExternalMESActiveResourceTypeValidation(requestBody:RequestExternalMESActiveResourceTypeValidation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RequestExternalMESActiveResourceTypeValidation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/RequestExternalMESActiveResourceTypeValidation", {
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
         resolve(data as RequestExternalMESActiveResourceTypeValidation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedCharacteristicAttrClassID
   Description: Used when the Characteristic Attr Class ID is changed.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ChangedCharacteristicAttrClassID", {
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
   Summary: Invoke method ChangeResourceGroupResourceType
   Description: This method is called when the Resource Group ResourceType field is changed.
   OperationID: ChangeResourceGroupResourceType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeResourceGroupResourceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceGroupResourceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeResourceGroupResourceType(requestBody:ChangeResourceGroupResourceType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeResourceGroupResourceType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ChangeResourceGroupResourceType", {
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
         resolve(data as ChangeResourceGroupResourceType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeResourceResourceType
   Description: This method is called when the Resource ResourceType field is changed.
   OperationID: ChangeResourceResourceType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeResourceResourceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceResourceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeResourceResourceType(requestBody:ChangeResourceResourceType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeResourceResourceType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ChangeResourceResourceType", {
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
         resolve(data as ChangeResourceResourceType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetResourceGroupsExtMES
   Description: Get the list of resource groups for Mattec changes
   OperationID: GetResourceGroupsExtMES
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetResourceGroupsExtMES_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetResourceGroupsExtMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetResourceGroupsExtMES(requestBody:GetResourceGroupsExtMES_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetResourceGroupsExtMES_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetResourceGroupsExtMES", {
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
         resolve(data as GetResourceGroupsExtMES_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewResourceGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewResourceGroup(requestBody:GetNewResourceGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewResourceGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetNewResourceGroup", {
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
         resolve(data as GetNewResourceGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewResourceGroupAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceGroupAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewResourceGroupAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceGroupAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewResourceGroupAttch(requestBody:GetNewResourceGroupAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewResourceGroupAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetNewResourceGroupAttch", {
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
         resolve(data as GetNewResourceGroupAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewResource
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewResource(requestBody:GetNewResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetNewResource", {
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
         resolve(data as GetNewResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCapResLnk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCapResLnk
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCapResLnk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCapResLnk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCapResLnk(requestBody:GetNewCapResLnk_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCapResLnk_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetNewCapResLnk", {
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
         resolve(data as GetNewCapResLnk_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewResourceCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewResourceCal(requestBody:GetNewResourceCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewResourceCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetNewResourceCal", {
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
         resolve(data as GetNewResourceCal_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapResLnkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CapResLnkRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceCalRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceGroupAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceGroupListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceGroupRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceRow,
}

export interface Erp_Tablesets_CapResLnkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A code which uniquely identifies the Capability this link applies to.  */  
   "CapabilityID":string,
      /**  The ResourceID the Capability is being linked to.  */  
   "ResourceID":string,
      /**  A tie breaker.  If two Resources are equal, but a user would prefer to keep one busy, then the one with the highest priority will be selected first.  */  
   "ResourcePriority":number,
      /**  A Production Factor for the link.  */  
   "ProductionFactor":number,
      /**  A Setup Factor for the link.  */  
   "SetupFactor":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
   "BitFlag":number,
   "CapIDDescription":string,
   "ResourceDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ResourceCalRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A code uniquely identifies a Resource Group.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  Exception Day  */  
   "SpecialDay":string,
      /**  ProdHour01  */  
   "ProdHour01":boolean,
      /**  ProdHour02  */  
   "ProdHour02":boolean,
      /**  ProdHour03  */  
   "ProdHour03":boolean,
      /**  ProdHour04  */  
   "ProdHour04":boolean,
      /**  ProdHour05  */  
   "ProdHour05":boolean,
      /**  ProdHour06  */  
   "ProdHour06":boolean,
      /**  ProdHour07  */  
   "ProdHour07":boolean,
      /**  ProdHour08  */  
   "ProdHour08":boolean,
      /**  ProdHour09  */  
   "ProdHour09":boolean,
      /**  ProdHour10  */  
   "ProdHour10":boolean,
      /**  ProdHour11  */  
   "ProdHour11":boolean,
      /**  ProdHour12  */  
   "ProdHour12":boolean,
      /**  ProdHour13  */  
   "ProdHour13":boolean,
      /**  ProdHour14  */  
   "ProdHour14":boolean,
      /**  ProdHour15  */  
   "ProdHour15":boolean,
      /**  ProdHour16  */  
   "ProdHour16":boolean,
      /**  ProdHour17  */  
   "ProdHour17":boolean,
      /**  ProdHour18  */  
   "ProdHour18":boolean,
      /**  ProdHour19  */  
   "ProdHour19":boolean,
      /**  ProdHour20  */  
   "ProdHour20":boolean,
      /**  ProdHour21  */  
   "ProdHour21":boolean,
      /**  ProdHour22  */  
   "ProdHour22":boolean,
      /**  ProdHour23  */  
   "ProdHour23":boolean,
      /**  ProdHour24  */  
   "ProdHour24":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ExceptionLabel  */  
   "ExceptionLabel":string,
      /**  Display Exception Label  */  
   "DispExceptionLabel":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ResourceGroupAttchRow{
   "Company":string,
   "ResourceGrpID":string,
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

export interface Erp_Tablesets_ResourceGroupListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "ResourceGrpID":string,
      /**  Long description of the Resource Group.  */  
   "Description":string,
      /**   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  */  
   "Inactive":boolean,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   "JCDept":string,
      /**  The burden rate for production.  */  
   "ProdBurRate":number,
      /**  Default burden rate for Setup time.  */  
   "SetupBurRate":number,
      /**   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QProdBurRate":number,
      /**   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QSetupBurRate":number,
      /**  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  */  
   "ResourceType":string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   "InputWhse":string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   "OutputWhse":string,
      /**  Location  */  
   "Location":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   "CharacteristicAttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CharacteristicAttributeSetID":number,
   "JCDeptDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ResourceGroupRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "ResourceGrpID":string,
      /**  Long description of the Resource Group.  */  
   "Description":string,
      /**  Identifies the production calendar for this Resource Group.   If this equals "", then the ProdCal record is the Company Level production calendar.  */  
   "CalendarID":string,
      /**   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  */  
   "Inactive":boolean,
      /**  If it is Finite Resource Group, and this is true, then the user will be allow to overload this Resource Group from using the scheduling tools.  */  
   "AllowManualOverride":boolean,
      /**  The number of days out this Resource Group will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  */  
   "FiniteHorizon":number,
      /**   The number of Resources in this Resource Group. The number of Resources X HrsPerMachine = Capacity.
A Resource Group with zero Resources is considered infinite capacity.  */  
   "NumberOfMachines":number,
      /**  Number of Resources that one operation runs on at a time within this Resource Group.  This affects how much of the total daily Resource Group capacity is used up per operation.  If Resource Group has 4  Resource, 8 hour a day, and SchMachine = 2.  An operation will schedule up to 16 hours per day.   This is used as a default to the JobOper.Machines field.  */  
   "SchMachine":number,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   "BurdenType":string,
      /**  The number of hours of delay that occurs when an operation leaves this Resource Group before the next operation can begin in a different Resource Group.  */  
   "MoveHours":number,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   "JCDept":string,
      /**  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource Group before it can begin. (The opposite of MoveHours)  */  
   "QueHours":number,
      /**  Establishes the default operation used when referencing this Resource Group.  This is optional, but if entered it must be valid in the OpMaster.  */  
   "OpCode":string,
      /**  The burden rate for production.  */  
   "ProdBurRate":number,
      /**  The labor rate for production.  */  
   "ProdLabRate":number,
      /**  Default burden rate for Setup time.  */  
   "SetupBurRate":number,
      /**  Default labor rate for setup time.  */  
   "SetupLabRate":number,
      /**   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QProdBurRate":number,
      /**   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QProdLabRate":number,
      /**   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QSetupBurRate":number,
      /**   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QSetupLabRate":number,
      /**  Indicates if burden hours are split out among employees when multiple employees work simultaneously on the same job operation within this Resource Group.  This feature is only applicable to Data Collection.  Manual Labor Entry does not split the burden hours. The opposite is that each employee should have their burden hours = labor hours. This situation would occur in Resource Groups that actually have "people" as machines, such as an assembly or welding center where multiple people work on the same job.  */  
   "SplitBurden":boolean,
      /**  Defines the default crew size for work done in this Resource Group.   The number of people it physically takes to run the machine. This should not be confused with scheduled number of machines, which squeezes the schedule time. The crew size is a multiplier used in calculation of Production labor hours on operations.  */  
   "ProdCrewSize":number,
      /**  Defines the default setup crew size for work done in this Resource Group.  The number of people it physically takes to setup the Resource.  This should not be confused with scheduled number of machines, which squeezes the schedule time.  The crew size is a multiplier  used in calculation of setup labor hours for an operation.  */  
   "SetupCrewSize":number,
      /**  Defines a default Operation standard master ID for this Resource Group.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.  */  
   "OpStdID":string,
      /**  lib/Reloader.w program increments and assigns it to Joboper.ReloadNum as it processes JobOper records. It is used to prevent redundant reads during the For Each loop.  */  
   "ReloadNum":number,
      /**  A  recovery flag which indicates the status of the Reload process for this Resource Group.  Values; Blank or "Started".  */  
   "ReloadStatus":string,
      /**  DailyCapacity1  */  
   "DailyCapacity1":number,
      /**  DailyCapacity2  */  
   "DailyCapacity2":number,
      /**  DailyCapacity3  */  
   "DailyCapacity3":number,
      /**  DailyCapacity4  */  
   "DailyCapacity4":number,
      /**  DailyCapacity5  */  
   "DailyCapacity5":number,
      /**  DailyCapacity6  */  
   "DailyCapacity6":number,
      /**  DailyCapacity7  */  
   "DailyCapacity7":number,
      /**  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is Hourly dollar rate.  Set to "F" (flat) or "P" (percent).  */  
   "QBurdenType":string,
      /**  Indicates if burden hours should equal Labor Hours for work reported within this Resource Group.  This feature is only applicable to Data Collection.  This is intended to be used where an employee jumps between multiple job operations without clock in/out (for efficiency purposes).  Example: Employee works on 4 operations for 8am - 1200.  They clock out of all 4 at 12.  Each transaction is given 1hr of labor.  If this is checked then each transaction will also have 1hr of burden.  Otherwise they will have 4 hrs for a total of 16 burden hrs.  */  
   "BurdenEQLabor":boolean,
      /**  Used for scheduling.  If YES then a single operation in this Resoure Group can be split across multiple Resources.  */  
   "SplitOperations":boolean,
      /**  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  */  
   "ResourceType":string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   "InputWhse":string,
      /**  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  */  
   "InputBinNum":string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   "OutputWhse":string,
      /**  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  */  
   "OutputBinNum":string,
      /**  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  */  
   "BackflushWhse":string,
      /**  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  */  
   "BackflushBinNum":string,
      /**  Indicates that Resource Group is visible in Overload Informer.  */  
   "InformOverload":boolean,
      /**  The minimum overload threshold before a day shows up in the Overload Informer.  */  
   "MinOverloadPerc":number,
      /**  Is the Employee ID which will be defaulted into LaborDtl records which get created through backflushing.  If this field is blank, then the Employee ID on the LaborDtl record causing the backflush process to be triggered will be used.  */  
   "BackflushEmpID":string,
      /**  This flags the Resource Group as being a "SubContract" or an "Internal".  This will determine the default when adding an operation to a BOM, Job, or Quote.  */  
   "SubContract":boolean,
      /**  To toggle on and off the automove flag for a Resource Group.  When false , the default is to generate a move request. When true the default is to not generate a move request. These defaults can be seen when entering a quantity and ending an activity in labor entry.  */  
   "AutoMove":boolean,
      /**  Indicates if hours are split out using estimate values when working  on multiple  job operations.  */  
   "UseEstimates":boolean,
      /**  Daily Production Qty: The production quantity developed to satisfy demand.  The cell is designed to produce at that quantity for a given time frame (daily).  */  
   "DailyProdQty":number,
      /**  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  */  
   "BillLaborRate":number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity .   Once the production limit for a resource  has been reached, the Resource has been consumed for that day.  */  
   "DailyProdRate":number,
      /**  Location  */  
   "Location":boolean,
      /**  Distribute Load  */  
   "DistributeLoad":boolean,
      /**  Flag to indicate whether to track production activity of the resource group.  */  
   "TrkProdAct":boolean,
      /**  When the capcity changes for a resourceGroup (in Resource Group Entry), this flag is set to true to indicate that Generate Shop Capacity process needs to be run to update the ShopLoad records.  This used to be performed within ResourceGroupEntry but for performance reasons it is being moved to the Generate Shop Capacity process  */  
   "SetShopLoad":boolean,
      /**  TAKT Value  */  
   "TAKTValue":number,
      /**  Use Calendar for Move Time  */  
   "UseCalendarForMove":boolean,
      /**  Use Calendar for Queue Time  */  
   "UseCalendarForQueue":boolean,
      /**  URL  */  
   "URL":string,
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
      /**  MESQueue  */  
   "MESQueue":boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   "CharacteristicAttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CharacteristicAttributeSetID":number,
   "inputwhsedesc":string,
   "outputwhsedesc":string,
   "backflushempname":string,
   "backflushwhsedesc":string,
      /**  Indicates if the Inactive flag should be enabled.  */  
   "EnableInactive":boolean,
   "BitFlag":number,
   "JCDeptDescription":string,
   "OPCodeOpDesc":string,
   "OpStdDescription":string,
   "ProdCalDescription":string,
   "ResourceTypeExternalMESType":string,
   "ResourceTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ResourceRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  Full description of Resource.  */  
   "Description":string,
      /**   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  */  
   "Inactive":boolean,
      /**  If yes then this Resource is scheduled as though it has finite production capacity.  */  
   "Finite":boolean,
      /**  If it is Finite Resource, and this is true, then the user will be allow to overload this resource from using the scheduling tools.  */  
   "AllowManualOverride":boolean,
      /**  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  */  
   "NextMaintDate":string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   "OutputWhse":string,
      /**  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  */  
   "OutputBinNum":string,
      /**  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  */  
   "BackflushWhse":string,
      /**  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  */  
   "BackflushBinNum":string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   "InputWhse":string,
      /**  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  */  
   "InputBinNum":string,
      /**  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  */  
   "ResourceType":string,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   "ConcurrentCapacity":number,
      /**  Indicates the production quantities produced by this Resource will be tracked.  */  
   "TrackProdQty":boolean,
      /**  Links this Resource to a Part, which must be valid in the Part table.  */  
   "LinkedPart":string,
      /**  Asset number of the Resource.  Links the Resource to a Fixed Asset.  */  
   "AssetNum":string,
      /**  The burden rate for production.  */  
   "ProdBurRate":number,
      /**  The labor rate for production.  */  
   "ProdLabRate":number,
      /**  Default burden rate for Setup time.  */  
   "SetupBurRate":number,
      /**  Default labor rate for setup time.  */  
   "SetupLabRate":number,
      /**   Quoting burden rate for production on the Resource
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QProdBurRate":number,
      /**   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QProdLabRate":number,
      /**   Quoting burden rate for setup in the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QSetupBurRate":number,
      /**   Quoting burden rate for "setup" in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QSetupLabRate":number,
      /**  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is flat hourly rate.  Valid values are "F" (flat) or "P" (percent).  */  
   "QBurdenType":string,
      /**  Logical to direct where the burden rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   "GetDefaultBurdenFromGroup":boolean,
      /**  This key links the record to the Vendor file.  If this field is set this is be a subcontracted resource.  */  
   "VendorNum":number,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   "BurdenType":string,
      /**  Identifies the production calendar for this Resource.   If this equals "", then the ProdCal record is the Resource Group Level production calendar.  */  
   "CalendarID":string,
      /**  The number of hours of delay that occurs when an operation leaves this Resource before the next operation can begin in a different Resource.  */  
   "MoveHours":number,
      /**  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource before it can begin. (The opposite of MoveHours)  */  
   "QueHours":number,
      /**  Logical to direct where the Move Time and Queue time for the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  This also controls whether the FiniteHorizon  and SplitOperation is from the Resource Group.  */  
   "GetDefaultMQFromGroup":boolean,
      /**  Indicates that the Resource is visible in Overload Informer.  */  
   "InformOverload":boolean,
      /**  The minimum overload threshold before a day shows up in the Overload Informer.  */  
   "MinOverloadPerc":number,
      /**   Establishes the default operation used when referencing this Resource.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Resource is going to be used to create a JobOper record.  */  
   "OpCode":string,
      /**   Defines a default Operation standard master ID for this Resource.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Resource is going to be used to create a JobOper.  */  
   "OpStdID":string,
      /**  Logical to direct where the labor rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   "GetDefaultLaborFromGroup":boolean,
      /**  The number of days out this Resource will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  */  
   "FiniteHorizon":number,
      /**  To toggle on and off the AutoMove flag for a Resource.  When false, the default is to generate a move request.  When true the default is to not generate a move request.  These defaults can be seen when entering a quantity and ending an activity in labor entry.  */  
   "AutoMove":boolean,
      /**  Used for scheduling.  If YES then a single operation on this Resource can be split into multiple operations.  */  
   "SplitOperations":boolean,
      /**  The production Qty developed to satisfy demand.  The cell is designed to produce at that rate for a given time frame (daily) until this production qty is met.  */  
   "DailyProdQty":number,
      /**  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  */  
   "BillLaborRate":number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   "DailyProdRate":number,
      /**  Logical to direct where the Warehouse information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   "GetDefaultWhseFromGroup":boolean,
      /**  Location  */  
   "Location":boolean,
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
      /**  EquipID of Equip record that is related to the Asset.  Can be blank, be if entered must be a valid Equip reference.  Note: maintained by Equipment Entry.  Read only in Asset Entry.  */  
   "EquipID":string,
      /**  URL  */  
   "URL":string,
      /**  JDFDevice  */  
   "JDFDevice":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  NumCavs  */  
   "NumCavs":number,
      /**  RunnerWt  */  
   "RunnerWt":number,
      /**  SetupTime  */  
   "SetupTime":number,
      /**  TearDownTime  */  
   "TearDownTime":number,
      /**  MiscInfo1  */  
   "MiscInfo1":string,
      /**  MiscInfo2  */  
   "MiscInfo2":string,
      /**  Brand  */  
   "Brand":string,
      /**  LocID  */  
   "LocID":string,
      /**  PmMapNo  */  
   "PmMapNo":number,
      /**  SetupURL  */  
   "SetupURL":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MobileResource  */  
   "MobileResource":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  MESQueue  */  
   "MESQueue":boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   "CharacteristicAttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CharacteristicAttributeSetID":number,
      /**  If this field is true, it marks the selected Resource as Connected Process Control (CPC) enable. If disable, connection and/or sync will not be done.  */  
   "ECPCEnabled":boolean,
      /**  A flag set by the user. When true, system willcreate Equip record from the Resource if the Equip record does not already exist. The EquipID = ResourceID.  This occurs when the record is saved.  */  
   "EquipCreate":boolean,
      /**  Plant from Resource Group  */  
   "Plant":string,
   "ReadOnlyFields":string,
   "BitFlag":number,
   "LinkedPartTrackLots":boolean,
   "LinkedPartPartDescription":string,
   "LinkedPartIUM":string,
   "LinkedPartTrackSerialNum":boolean,
   "LinkedPartTrackDimension":boolean,
   "LinkedPartSellingFactor":number,
   "LinkedPartSalesUM":string,
   "LinkedPartPricePerCode":string,
   "OpCodeOpDesc":string,
   "OpStdDescription":string,
   "ProdCalDescription":string,
   "ResourceTypeDescription":string,
   "ResourceTypeExternalMESType":string,
   "WhseBackflushWhseDescDescription":string,
   "WhseInputWhseDescDescription":string,
   "WhseOutputWhseDescDescription":string,
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
      @param cResourceGrpID
   */  
export interface BuildRsrcGrpResourceCalList_input{
      /**  The current Resource GroupID  */  
   cResourceGrpID:string,
}

export interface BuildRsrcGrpResourceCalList_output{
   returnObj:Erp_Tablesets_ResourceGroupTableset[],
}

   /** Required : 
      @param cResourceGrpID
      @param cResourceID
   */  
export interface BuildRsrcResourceCalList_input{
      /**  The current Resource Group ID  */  
   cResourceGrpID:string,
      /**  The current Resource ID  */  
   cResourceID:string,
}

export interface BuildRsrcResourceCalList_output{
   returnObj:Erp_Tablesets_ResourceGroupTableset[],
}

   /** Required : 
      @param proposedResourceType
      @param ds
   */  
export interface ChangeResourceGroupResourceType_input{
      /**  The proposed value for ResourceType.  */  
   proposedResourceType:string,
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface ChangeResourceGroupResourceType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param proposedResourceType
      @param ds
   */  
export interface ChangeResourceResourceType_input{
      /**  The proposed value for ResourceType.  */  
   proposedResourceType:string,
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface ChangeResourceResourceType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedCharacteristicAttrClassID_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface ChangedCharacteristicAttrClassID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param cResourceGrpID
   */  
export interface CheckRGPlant_input{
      /**  The current Resource GroupID  */  
   cResourceGrpID:string,
}

export interface CheckRGPlant_output{
}

   /** Required : 
      @param cResourceGrpID
      @param daDate
      @param ds
   */  
export interface CustomizeResourceCalRsrcGrp_input{
      /**  The current Resource Group ID  */  
   cResourceGrpID:string,
      /**  The selected date to be customized  */  
   daDate:string,
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface CustomizeResourceCalRsrcGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param cResourceID
      @param cResourceGrpID
      @param daDate
      @param ds
   */  
export interface CustomizeResourceCalRsrc_input{
      /**  The current Resource ID  */  
   cResourceID:string,
      /**  The current Resource Group ID  */  
   cResourceGrpID:string,
      /**  The selected date to be customized  */  
   daDate:string,
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface CustomizeResourceCalRsrc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param resourceGrpID
   */  
export interface DeleteByID_input{
   resourceGrpID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
   */  
export interface DeleteResourceCal_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface DeleteResourceCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
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
   returnObj:Erp_Tablesets_ResourceGroupListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Erp_Tablesets_CapResLnkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A code which uniquely identifies the Capability this link applies to.  */  
   CapabilityID:string,
      /**  The ResourceID the Capability is being linked to.  */  
   ResourceID:string,
      /**  A tie breaker.  If two Resources are equal, but a user would prefer to keep one busy, then the one with the highest priority will be selected first.  */  
   ResourcePriority:number,
      /**  A Production Factor for the link.  */  
   ProductionFactor:number,
      /**  A Setup Factor for the link.  */  
   SetupFactor:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
   BitFlag:number,
   CapIDDescription:string,
   ResourceDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceCalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A code uniquely identifies a Resource Group.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  Exception Day  */  
   SpecialDay:string,
      /**  ProdHour01  */  
   ProdHour01:boolean,
      /**  ProdHour02  */  
   ProdHour02:boolean,
      /**  ProdHour03  */  
   ProdHour03:boolean,
      /**  ProdHour04  */  
   ProdHour04:boolean,
      /**  ProdHour05  */  
   ProdHour05:boolean,
      /**  ProdHour06  */  
   ProdHour06:boolean,
      /**  ProdHour07  */  
   ProdHour07:boolean,
      /**  ProdHour08  */  
   ProdHour08:boolean,
      /**  ProdHour09  */  
   ProdHour09:boolean,
      /**  ProdHour10  */  
   ProdHour10:boolean,
      /**  ProdHour11  */  
   ProdHour11:boolean,
      /**  ProdHour12  */  
   ProdHour12:boolean,
      /**  ProdHour13  */  
   ProdHour13:boolean,
      /**  ProdHour14  */  
   ProdHour14:boolean,
      /**  ProdHour15  */  
   ProdHour15:boolean,
      /**  ProdHour16  */  
   ProdHour16:boolean,
      /**  ProdHour17  */  
   ProdHour17:boolean,
      /**  ProdHour18  */  
   ProdHour18:boolean,
      /**  ProdHour19  */  
   ProdHour19:boolean,
      /**  ProdHour20  */  
   ProdHour20:boolean,
      /**  ProdHour21  */  
   ProdHour21:boolean,
      /**  ProdHour22  */  
   ProdHour22:boolean,
      /**  ProdHour23  */  
   ProdHour23:boolean,
      /**  ProdHour24  */  
   ProdHour24:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ExceptionLabel  */  
   ExceptionLabel:string,
      /**  Display Exception Label  */  
   DispExceptionLabel:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceGroupAttchRow{
   Company:string,
   ResourceGrpID:string,
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

export interface Erp_Tablesets_ResourceGroupListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  Long description of the Resource Group.  */  
   Description:string,
      /**   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  */  
   Inactive:boolean,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   JCDept:string,
      /**  The burden rate for production.  */  
   ProdBurRate:number,
      /**  Default burden rate for Setup time.  */  
   SetupBurRate:number,
      /**   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdBurRate:number,
      /**   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupBurRate:number,
      /**  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  */  
   ResourceType:string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   InputWhse:string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   OutputWhse:string,
      /**  Location  */  
   Location:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
   JCDeptDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceGroupListTableset{
   ResourceGroupList:Erp_Tablesets_ResourceGroupListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ResourceGroupRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  Long description of the Resource Group.  */  
   Description:string,
      /**  Identifies the production calendar for this Resource Group.   If this equals "", then the ProdCal record is the Company Level production calendar.  */  
   CalendarID:string,
      /**   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  */  
   Inactive:boolean,
      /**  If it is Finite Resource Group, and this is true, then the user will be allow to overload this Resource Group from using the scheduling tools.  */  
   AllowManualOverride:boolean,
      /**  The number of days out this Resource Group will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  */  
   FiniteHorizon:number,
      /**   The number of Resources in this Resource Group. The number of Resources X HrsPerMachine = Capacity.
A Resource Group with zero Resources is considered infinite capacity.  */  
   NumberOfMachines:number,
      /**  Number of Resources that one operation runs on at a time within this Resource Group.  This affects how much of the total daily Resource Group capacity is used up per operation.  If Resource Group has 4  Resource, 8 hour a day, and SchMachine = 2.  An operation will schedule up to 16 hours per day.   This is used as a default to the JobOper.Machines field.  */  
   SchMachine:number,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   BurdenType:string,
      /**  The number of hours of delay that occurs when an operation leaves this Resource Group before the next operation can begin in a different Resource Group.  */  
   MoveHours:number,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   JCDept:string,
      /**  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource Group before it can begin. (The opposite of MoveHours)  */  
   QueHours:number,
      /**  Establishes the default operation used when referencing this Resource Group.  This is optional, but if entered it must be valid in the OpMaster.  */  
   OpCode:string,
      /**  The burden rate for production.  */  
   ProdBurRate:number,
      /**  The labor rate for production.  */  
   ProdLabRate:number,
      /**  Default burden rate for Setup time.  */  
   SetupBurRate:number,
      /**  Default labor rate for setup time.  */  
   SetupLabRate:number,
      /**   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdBurRate:number,
      /**   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdLabRate:number,
      /**   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupBurRate:number,
      /**   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupLabRate:number,
      /**  Indicates if burden hours are split out among employees when multiple employees work simultaneously on the same job operation within this Resource Group.  This feature is only applicable to Data Collection.  Manual Labor Entry does not split the burden hours. The opposite is that each employee should have their burden hours = labor hours. This situation would occur in Resource Groups that actually have "people" as machines, such as an assembly or welding center where multiple people work on the same job.  */  
   SplitBurden:boolean,
      /**  Defines the default crew size for work done in this Resource Group.   The number of people it physically takes to run the machine. This should not be confused with scheduled number of machines, which squeezes the schedule time. The crew size is a multiplier used in calculation of Production labor hours on operations.  */  
   ProdCrewSize:number,
      /**  Defines the default setup crew size for work done in this Resource Group.  The number of people it physically takes to setup the Resource.  This should not be confused with scheduled number of machines, which squeezes the schedule time.  The crew size is a multiplier  used in calculation of setup labor hours for an operation.  */  
   SetupCrewSize:number,
      /**  Defines a default Operation standard master ID for this Resource Group.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.  */  
   OpStdID:string,
      /**  lib/Reloader.w program increments and assigns it to Joboper.ReloadNum as it processes JobOper records. It is used to prevent redundant reads during the For Each loop.  */  
   ReloadNum:number,
      /**  A  recovery flag which indicates the status of the Reload process for this Resource Group.  Values; Blank or "Started".  */  
   ReloadStatus:string,
      /**  DailyCapacity1  */  
   DailyCapacity1:number,
      /**  DailyCapacity2  */  
   DailyCapacity2:number,
      /**  DailyCapacity3  */  
   DailyCapacity3:number,
      /**  DailyCapacity4  */  
   DailyCapacity4:number,
      /**  DailyCapacity5  */  
   DailyCapacity5:number,
      /**  DailyCapacity6  */  
   DailyCapacity6:number,
      /**  DailyCapacity7  */  
   DailyCapacity7:number,
      /**  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is Hourly dollar rate.  Set to "F" (flat) or "P" (percent).  */  
   QBurdenType:string,
      /**  Indicates if burden hours should equal Labor Hours for work reported within this Resource Group.  This feature is only applicable to Data Collection.  This is intended to be used where an employee jumps between multiple job operations without clock in/out (for efficiency purposes).  Example: Employee works on 4 operations for 8am - 1200.  They clock out of all 4 at 12.  Each transaction is given 1hr of labor.  If this is checked then each transaction will also have 1hr of burden.  Otherwise they will have 4 hrs for a total of 16 burden hrs.  */  
   BurdenEQLabor:boolean,
      /**  Used for scheduling.  If YES then a single operation in this Resoure Group can be split across multiple Resources.  */  
   SplitOperations:boolean,
      /**  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  */  
   ResourceType:string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   InputWhse:string,
      /**  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  */  
   InputBinNum:string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   OutputWhse:string,
      /**  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  */  
   OutputBinNum:string,
      /**  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  */  
   BackflushWhse:string,
      /**  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  */  
   BackflushBinNum:string,
      /**  Indicates that Resource Group is visible in Overload Informer.  */  
   InformOverload:boolean,
      /**  The minimum overload threshold before a day shows up in the Overload Informer.  */  
   MinOverloadPerc:number,
      /**  Is the Employee ID which will be defaulted into LaborDtl records which get created through backflushing.  If this field is blank, then the Employee ID on the LaborDtl record causing the backflush process to be triggered will be used.  */  
   BackflushEmpID:string,
      /**  This flags the Resource Group as being a "SubContract" or an "Internal".  This will determine the default when adding an operation to a BOM, Job, or Quote.  */  
   SubContract:boolean,
      /**  To toggle on and off the automove flag for a Resource Group.  When false , the default is to generate a move request. When true the default is to not generate a move request. These defaults can be seen when entering a quantity and ending an activity in labor entry.  */  
   AutoMove:boolean,
      /**  Indicates if hours are split out using estimate values when working  on multiple  job operations.  */  
   UseEstimates:boolean,
      /**  Daily Production Qty: The production quantity developed to satisfy demand.  The cell is designed to produce at that quantity for a given time frame (daily).  */  
   DailyProdQty:number,
      /**  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  */  
   BillLaborRate:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity .   Once the production limit for a resource  has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Location  */  
   Location:boolean,
      /**  Distribute Load  */  
   DistributeLoad:boolean,
      /**  Flag to indicate whether to track production activity of the resource group.  */  
   TrkProdAct:boolean,
      /**  When the capcity changes for a resourceGroup (in Resource Group Entry), this flag is set to true to indicate that Generate Shop Capacity process needs to be run to update the ShopLoad records.  This used to be performed within ResourceGroupEntry but for performance reasons it is being moved to the Generate Shop Capacity process  */  
   SetShopLoad:boolean,
      /**  TAKT Value  */  
   TAKTValue:number,
      /**  Use Calendar for Move Time  */  
   UseCalendarForMove:boolean,
      /**  Use Calendar for Queue Time  */  
   UseCalendarForQueue:boolean,
      /**  URL  */  
   URL:string,
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
      /**  MESQueue  */  
   MESQueue:boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
   inputwhsedesc:string,
   outputwhsedesc:string,
   backflushempname:string,
   backflushwhsedesc:string,
      /**  Indicates if the Inactive flag should be enabled.  */  
   EnableInactive:boolean,
   BitFlag:number,
   JCDeptDescription:string,
   OPCodeOpDesc:string,
   OpStdDescription:string,
   ProdCalDescription:string,
   ResourceTypeExternalMESType:string,
   ResourceTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceGroupTableset{
   ResourceGroup:Erp_Tablesets_ResourceGroupRow[],
   ResourceGroupAttch:Erp_Tablesets_ResourceGroupAttchRow[],
   Resource:Erp_Tablesets_ResourceRow[],
   CapResLnk:Erp_Tablesets_CapResLnkRow[],
   ResourceCal:Erp_Tablesets_ResourceCalRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ResourceRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  Full description of Resource.  */  
   Description:string,
      /**   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  */  
   Inactive:boolean,
      /**  If yes then this Resource is scheduled as though it has finite production capacity.  */  
   Finite:boolean,
      /**  If it is Finite Resource, and this is true, then the user will be allow to overload this resource from using the scheduling tools.  */  
   AllowManualOverride:boolean,
      /**  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  */  
   NextMaintDate:string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   OutputWhse:string,
      /**  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  */  
   OutputBinNum:string,
      /**  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  */  
   BackflushWhse:string,
      /**  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  */  
   BackflushBinNum:string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   InputWhse:string,
      /**  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  */  
   InputBinNum:string,
      /**  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  */  
   ResourceType:string,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  Indicates the production quantities produced by this Resource will be tracked.  */  
   TrackProdQty:boolean,
      /**  Links this Resource to a Part, which must be valid in the Part table.  */  
   LinkedPart:string,
      /**  Asset number of the Resource.  Links the Resource to a Fixed Asset.  */  
   AssetNum:string,
      /**  The burden rate for production.  */  
   ProdBurRate:number,
      /**  The labor rate for production.  */  
   ProdLabRate:number,
      /**  Default burden rate for Setup time.  */  
   SetupBurRate:number,
      /**  Default labor rate for setup time.  */  
   SetupLabRate:number,
      /**   Quoting burden rate for production on the Resource
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdBurRate:number,
      /**   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdLabRate:number,
      /**   Quoting burden rate for setup in the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupBurRate:number,
      /**   Quoting burden rate for "setup" in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupLabRate:number,
      /**  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is flat hourly rate.  Valid values are "F" (flat) or "P" (percent).  */  
   QBurdenType:string,
      /**  Logical to direct where the burden rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   GetDefaultBurdenFromGroup:boolean,
      /**  This key links the record to the Vendor file.  If this field is set this is be a subcontracted resource.  */  
   VendorNum:number,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   BurdenType:string,
      /**  Identifies the production calendar for this Resource.   If this equals "", then the ProdCal record is the Resource Group Level production calendar.  */  
   CalendarID:string,
      /**  The number of hours of delay that occurs when an operation leaves this Resource before the next operation can begin in a different Resource.  */  
   MoveHours:number,
      /**  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource before it can begin. (The opposite of MoveHours)  */  
   QueHours:number,
      /**  Logical to direct where the Move Time and Queue time for the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  This also controls whether the FiniteHorizon  and SplitOperation is from the Resource Group.  */  
   GetDefaultMQFromGroup:boolean,
      /**  Indicates that the Resource is visible in Overload Informer.  */  
   InformOverload:boolean,
      /**  The minimum overload threshold before a day shows up in the Overload Informer.  */  
   MinOverloadPerc:number,
      /**   Establishes the default operation used when referencing this Resource.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Resource is going to be used to create a JobOper record.  */  
   OpCode:string,
      /**   Defines a default Operation standard master ID for this Resource.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Resource is going to be used to create a JobOper.  */  
   OpStdID:string,
      /**  Logical to direct where the labor rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   GetDefaultLaborFromGroup:boolean,
      /**  The number of days out this Resource will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  */  
   FiniteHorizon:number,
      /**  To toggle on and off the AutoMove flag for a Resource.  When false, the default is to generate a move request.  When true the default is to not generate a move request.  These defaults can be seen when entering a quantity and ending an activity in labor entry.  */  
   AutoMove:boolean,
      /**  Used for scheduling.  If YES then a single operation on this Resource can be split into multiple operations.  */  
   SplitOperations:boolean,
      /**  The production Qty developed to satisfy demand.  The cell is designed to produce at that rate for a given time frame (daily) until this production qty is met.  */  
   DailyProdQty:number,
      /**  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  */  
   BillLaborRate:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Logical to direct where the Warehouse information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   GetDefaultWhseFromGroup:boolean,
      /**  Location  */  
   Location:boolean,
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
      /**  EquipID of Equip record that is related to the Asset.  Can be blank, be if entered must be a valid Equip reference.  Note: maintained by Equipment Entry.  Read only in Asset Entry.  */  
   EquipID:string,
      /**  URL  */  
   URL:string,
      /**  JDFDevice  */  
   JDFDevice:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  NumCavs  */  
   NumCavs:number,
      /**  RunnerWt  */  
   RunnerWt:number,
      /**  SetupTime  */  
   SetupTime:number,
      /**  TearDownTime  */  
   TearDownTime:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  Brand  */  
   Brand:string,
      /**  LocID  */  
   LocID:string,
      /**  PmMapNo  */  
   PmMapNo:number,
      /**  SetupURL  */  
   SetupURL:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MobileResource  */  
   MobileResource:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  MESQueue  */  
   MESQueue:boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
      /**  If this field is true, it marks the selected Resource as Connected Process Control (CPC) enable. If disable, connection and/or sync will not be done.  */  
   ECPCEnabled:boolean,
      /**  A flag set by the user. When true, system willcreate Equip record from the Resource if the Equip record does not already exist. The EquipID = ResourceID.  This occurs when the record is saved.  */  
   EquipCreate:boolean,
      /**  Plant from Resource Group  */  
   Plant:string,
   ReadOnlyFields:string,
   BitFlag:number,
   LinkedPartTrackLots:boolean,
   LinkedPartPartDescription:string,
   LinkedPartIUM:string,
   LinkedPartTrackSerialNum:boolean,
   LinkedPartTrackDimension:boolean,
   LinkedPartSellingFactor:number,
   LinkedPartSalesUM:string,
   LinkedPartPricePerCode:string,
   OpCodeOpDesc:string,
   OpStdDescription:string,
   ProdCalDescription:string,
   ResourceTypeDescription:string,
   ResourceTypeExternalMESType:string,
   WhseBackflushWhseDescDescription:string,
   WhseInputWhseDescDescription:string,
   WhseOutputWhseDescDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtResourceGroupTableset{
   ResourceGroup:Erp_Tablesets_ResourceGroupRow[],
   ResourceGroupAttch:Erp_Tablesets_ResourceGroupAttchRow[],
   Resource:Erp_Tablesets_ResourceRow[],
   CapResLnk:Erp_Tablesets_CapResLnkRow[],
   ResourceCal:Erp_Tablesets_ResourceCalRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param resourceGrpID
   */  
export interface GetByID_input{
   resourceGrpID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ResourceGroupTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ResourceGroupTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ResourceGroupTableset[],
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
   returnObj:Erp_Tablesets_ResourceGroupListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param capabilityID
   */  
export interface GetNewCapResLnk_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
   capabilityID:string,
}

export interface GetNewCapResLnk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
      @param resourceGrpID
      @param resourceID
   */  
export interface GetNewResourceCal_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
   resourceGrpID:string,
   resourceID:string,
}

export interface GetNewResourceCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
      @param resourceGrpID
   */  
export interface GetNewResourceGroupAttch_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
   resourceGrpID:string,
}

export interface GetNewResourceGroupAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewResourceGroup_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface GetNewResourceGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewResource_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface GetNewResource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetResourceGroupsExtMES_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetResourceGroupsExtMES_output{
   returnObj:Erp_Tablesets_ResourceGroupListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseResourceGroup
      @param whereClauseResourceGroupAttch
      @param whereClauseResource
      @param whereClauseCapResLnk
      @param whereClauseResourceCal
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseResourceGroup:string,
   whereClauseResourceGroupAttch:string,
   whereClauseResource:string,
   whereClauseCapResLnk:string,
   whereClauseResourceCal:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ResourceGroupTableset[],
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
      @param ipResourceID
      @param ipResourceGrpID
      @param ds
   */  
export interface InsertNewResource_input{
      /**  The new resource id value.  */  
   ipResourceID:string,
      /**  The resourcegrp id value that you are adding this resource to  */  
   ipResourceGrpID:string,
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface InsertNewResource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
      @param pOriginalDay
      @param pNewDay
   */  
export interface MoveResourceCal_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
      /**  The original day of the excpetion  */  
   pOriginalDay:string,
      /**  The new day the excpetion was moved to  */  
   pNewDay:string,
}

export interface MoveResourceCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
      @param ipResourceID
      @param ipFromResourceGrpID
      @param ipToResourceGrpID
   */  
export interface MoveResource_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
      /**  The moving resource id value.  */  
   ipResourceID:string,
      /**  The resourcegrp id value that you are moving the resource from.  */  
   ipFromResourceGrpID:string,
      /**  The resourcegrp id value that you are moving the resource to.  */  
   ipToResourceGrpID:string,
}

export interface MoveResource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
   showWarningMessage:boolean,
}
}

   /** Required : 
      @param company
      @param resourceType
   */  
export interface RequestExternalMESActiveResourceTypeValidation_input{
   company:string,
   resourceType:string,
}

export interface RequestExternalMESActiveResourceTypeValidation_output{
   returnObj:boolean,
}

export interface SelectDistinctInOutWhseQuery_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface SetInactiveFlag_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface SetInactiveFlag_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtResourceGroupTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtResourceGroupTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateResourceCal_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface UpdateResourceCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ResourceGroupTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceGroupTableset,
}
}

   /** Required : 
      @param ipProposedInspPlan
      @param ipProposedSpecId
   */  
export interface ValidateInspection_input{
      /**  The new proposed InspPlanPartNum value  */  
   ipProposedInspPlan:string,
      /**  The new proposed SpecID value  */  
   ipProposedSpecId:string,
}

export interface ValidateInspection_output{
}

   /** Required : 
      @param ipResourceID
      @param ipResourceGrpID
   */  
export interface ValidateResource_input{
      /**  The resource id value to validate.  */  
   ipResourceID:string,
      /**  The resourcegrp id value to validate.  */  
   ipResourceGrpID:string,
}

export interface ValidateResource_output{
}

