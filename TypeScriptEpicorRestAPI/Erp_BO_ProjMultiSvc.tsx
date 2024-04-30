import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ProjMultiSvc
// Description: Service to have the visibility of all project cost/revenue details
in a single view (dashboard) and based on that information run the
revenue recognition for one or more selected projects at the same time.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/$metadata", {
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
   Description: Get ProjMultis items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProjMultis
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjMultiRow
   */  
export function get_ProjMultis(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProjMultis
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProjMultiRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProjMultiRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProjMultis(requestBody:Erp_Tablesets_ProjMultiRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis", {
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
   Summary: Calls GetByID to retrieve the ProjMulti item
   Description: Calls GetByID to retrieve the ProjMulti item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjMulti
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProjMultiRow
   */  
export function get_ProjMultis_Company_ProjectID(Company:string, ProjectID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProjMultiRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")", {
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
         resolve(data as Erp_Tablesets_ProjMultiRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProjMulti for the service
   Description: Calls UpdateExt to update ProjMulti. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProjMulti
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProjMultiRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProjMultis_Company_ProjectID(Company:string, ProjectID:string, requestBody:Erp_Tablesets_ProjMultiRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")", {
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
   Summary: Call UpdateExt to delete ProjMulti item
   Description: Call UpdateExt to delete ProjMulti item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProjMulti
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProjMultis_Company_ProjectID(Company:string, ProjectID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")", {
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
   Description: Get ProjectCsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProjectCsts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjectCstRow
   */  
export function get_ProjMultis_Company_ProjectID_ProjectCsts(Company:string, ProjectID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjectCstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")/ProjectCsts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjectCstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ProjectCst item
   Description: Calls GetByID to retrieve the ProjectCst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjectCst1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProjectCstRow
   */  
export function get_ProjMultis_Company_ProjectID_ProjectCsts_Company_ProjectID(Company:string, ProjectID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProjectCstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")/ProjectCsts(" + Company + "," + ProjectID + ")", {
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
         resolve(data as Erp_Tablesets_ProjectCstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ProjectCsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProjectCsts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjectCstRow
   */  
export function get_ProjectCsts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjectCstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjectCstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProjectCsts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProjectCstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProjectCstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProjectCsts(requestBody:Erp_Tablesets_ProjectCstRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts", {
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
   Summary: Calls GetByID to retrieve the ProjectCst item
   Description: Calls GetByID to retrieve the ProjectCst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjectCst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProjectCstRow
   */  
export function get_ProjectCsts_Company_ProjectID(Company:string, ProjectID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProjectCstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts(" + Company + "," + ProjectID + ")", {
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
         resolve(data as Erp_Tablesets_ProjectCstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProjectCst for the service
   Description: Calls UpdateExt to update ProjectCst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProjectCst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProjectCstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProjectCsts_Company_ProjectID(Company:string, ProjectID:string, requestBody:Erp_Tablesets_ProjectCstRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts(" + Company + "," + ProjectID + ")", {
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
   Summary: Call UpdateExt to delete ProjectCst item
   Description: Call UpdateExt to delete ProjectCst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProjectCst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProjectCsts_Company_ProjectID(Company:string, ProjectID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts(" + Company + "," + ProjectID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjMultiListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiListRow)
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
export function get_GetRows(whereClauseProjMulti:string, whereClauseProjectCst:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseProjMulti!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProjMulti=" + whereClauseProjMulti
   }
   if(typeof whereClauseProjectCst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProjectCst=" + whereClauseProjectCst
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetRows" + params, {
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
export function get_GetByID(projectID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof projectID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "projectID=" + projectID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsByFilter
   Description: It checks files of input filter ProjFilter if some of them are not empty
then creates where-clause against it and generates a total where-clause
against Project table
   OperationID: GetRowsByFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsByFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsByFilter(requestBody:GetRowsByFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsByFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetRowsByFilter", {
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
         resolve(data as GetRowsByFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshAll
   Description: Refresh UI with ProjectIDs
   OperationID: RefreshAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshAll(requestBody:RefreshAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/RefreshAll", {
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
         resolve(data as RefreshAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewProjMulti
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProjMulti
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewProjMulti_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProjMulti_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProjMulti(requestBody:GetNewProjMulti_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewProjMulti_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetNewProjMulti", {
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
         resolve(data as GetNewProjMulti_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewProjectCst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProjectCst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewProjectCst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProjectCst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProjectCst(requestBody:GetNewProjectCst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewProjectCst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetNewProjectCst", {
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
         resolve(data as GetNewProjectCst_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProjMultiListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProjMultiRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjectCstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProjectCstRow,
}

export interface Erp_Tablesets_ProjMultiListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Full description of Project Management Code.  */  
   "Description":string,
      /**  Start Date of the project  */  
   "StartDate":string,
      /**  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  */  
   "ConCustNum":number,
      /**  Employee ID of the person who has responsibility for the project  */  
   "ConProjMgr":string,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  */  
   "ConInvMeth":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  Last action performed on Project as relates to revenue recognition.  */  
   "LastAction":string,
      /**  Date when the LastAction happened to the Project.  */  
   "ActionDate":string,
   "Approved":boolean,
   "Selected":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ProjMultiRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Full description of Project Management Code.  */  
   "Description":string,
      /**  Indicates if this Project is active.  Can be changed directly by the user during entry.  */  
   "ActiveProject":boolean,
      /**  Editor widget for project comments.  */  
   "CommentText":string,
      /**  A LIST-DELIM delimited list of people.  */  
   "PersonList":string,
      /**  Will contain the coma separated list of the fields that the user has added to the project from within Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMap":string,
      /**  Will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Holds the default project warehouse code.  */  
   "WarehouseCode":string,
      /**  Holds the default project bin code.  */  
   "BinNum":string,
      /**  This holds the top level job to which all of the jobs created for a WBS Phase will be associated  */  
   "PrimaryJob":string,
      /**  This is the material placeholder in the primary project job to which all WBS Phase jobs will be linked.  */  
   "PrimaryMtl":number,
      /**  The sales category code used in the Revenue recognition process.  */  
   "SalesCatID":string,
      /**  The Product Group code used in the Revenue Recognition process.  */  
   "ProdCode":string,
      /**  RESERVED FOR FUTURE USE: Logical field. When set to true it indicates that the journals created to recognise the revenue for the project have been reversed.  */  
   "CloseAccrual":boolean,
      /**  Assembly Seq from JobAsmbl record.  */  
   "PrimaryAsmSeq":number,
      /**  Start Date of the project  */  
   "StartDate":string,
      /**  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  */  
   "ConCustNum":number,
      /**  Contract start date  */  
   "ConStartDate":string,
      /**  Date the contract is due to be complete  */  
   "ConEndDate":string,
      /**  Projected Contract End Date. Defaults to the Contract End Date but can be used to report on the projected end date.  */  
   "ConProjectedEnd":string,
      /**   Contract Reference number for project.
At the Epicor 9.05 release this field is reference only, at the Epicor 9.1 release when the whole contract system is enhanced then this field will reference an actual contract and a search will be provided.  */  
   "ConReference":string,
      /**  Employee ID of the person who has responsibility for the project  */  
   "ConProjMgr":string,
      /**  Total contract value for the project.  */  
   "ConTotValue":number,
      /**  Value of the posted invoices to date (system field)  */  
   "ConTotInv":number,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  */  
   "ConInvMeth":string,
      /**  Foreign key to the QMarkUp  */  
   "MarkUpID":string,
      /**  Override of Labor Markup Percent  */  
   "PBLbMarkUp":number,
      /**  Override of Material Markup Percent  */  
   "PBMtlMarkUp":number,
      /**  Override of Subcontract Markup Percentage  */  
   "PBSubMarkUp":number,
      /**  Override of Other Direct Cost Markup %  */  
   "PBMiscMarkUp":number,
      /**  Retention percentage. How this is used is dependent on RetentionProc field.  */  
   "PBRetentionPcnt":number,
      /**   How the retention percentage will be used.
The options are ?M? = Maximum of Contract Value
?P? = Percent of Invoice Value.  */  
   "PBRetentionProc":string,
      /**  Project Fee  */  
   "PBFeeProject":number,
      /**  Apply Fee with list of the options: F =  First Invoice Only, A = All Invoices  */  
   "PBFeeApply":string,
      /**  Fee Type with list of the options: P = Percentage, F = Fixed Amount  */  
   "PBFeeType":string,
      /**  Apply Fees on list with the options: N = Net Cost, G = Gross Cost.  */  
   "PBFeeApplyOn":string,
      /**  Fee Invoice Text in Free format to allow the user to enter text that will be displayed on the invoice  */  
   "PBFeeInvoiceText":string,
      /**  Fee that is to be charged against any labor charges on an invoice  */  
   "PBFeeLbrCharge":number,
      /**  Labor Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   "PBFeeLbrType":string,
      /**  Labor Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   "PBFeeLbrApply":string,
      /**  Fee that is to be charged against any material charges on an invoice  */  
   "PBFeeMtlCharge":number,
      /**  Material Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   "PBFeeMtlType":string,
      /**  Material Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   "PBFeeMtlApply":string,
      /**  Fee that is to be charged against any Subcontract charges on an invoice.  */  
   "PBFeeSubCharge":number,
      /**  Subcontract Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   "PBFeeSubType":string,
      /**  Subcontract Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   "PBFeeSubApply":string,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice.  */  
   "PBFeeMiscCharge":number,
      /**  Miscellaneous Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   "PBFeeMiscType":string,
      /**  Miscellaneous Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   "PBFeeMiscApply":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Contract Customer Bill To number, foreign key to Customer  */  
   "ConBTCustNum":number,
      /**  If invoices are allowed to be generated even if the element is over the predefined ceiling.  */  
   "ConOverCeiling":boolean,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   "ConRevMethod":string,
      /**  Price list is used to establish the price for any materials when the invoicing method is set to T & M or Cost Plus. Can be empty.  */  
   "ConListCode":string,
      /**  Hours for Invoicing allows the user to decide which hours are to be used by the invoicing process, it has system list with the options: L =  Labor, B = Burden  */  
   "ConHrsInvc":string,
      /**  Rate Type Code  */  
   "RateGrpCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   "LockRate":boolean,
      /**  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  */  
   "ExchangeRate":number,
      /**  This is the projected end date of the project but is not required and is only used if entered in the creation of the project job and for any user reporting requirements.  */  
   "EndDate":string,
      /**  Defaults from JCSyst.DfltPrjRtSrc. Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  */  
   "PBPrjRtSrc":string,
      /**  Value of the posted invoices to date (system field) in the Project currency  */  
   "DocConTotInv":number,
      /**  If set to true a new primary job will be created automatically for the project.  */  
   "CreatePrjJob":boolean,
      /**  Value of the posted invoices to date (system field) in the Reporting currency  */  
   "Rpt1ConTotInv":number,
      /**  Project revision number  */  
   "Revision":number,
      /**  Value of the posted invoices to date (system field) in the Reporting currency  */  
   "Rpt2ConTotInv":number,
      /**   This is the percentage of the costs for material, labor and burden that will be invoiced.
This is also used by the invoice entry process when invoicing regular shipments to determine the actual value of the invoice and how much will be relieved from the Progress Payments to date.  */  
   "PPAllowPcnt":number,
      /**  Value of the posted invoices to date (system field) in the Reporting currency  */  
   "Rpt3ConTotInv":number,
      /**   This will allow regular shipments to be invoiced normally.
Setting the field to true will cause the Customer Shipment process to place any packing slips for any sales order associated with the project to be placed on hold to prevent them being selected for invoicing. 
When the user changes this flag to true it will trigger business logic that will release the shipments for invoicing.  */  
   "HoldPrdInv":boolean,
      /**  Total contract value for the project. in the Project currency  */  
   "DocConTotValue":number,
      /**   This will default to true which will then trigger the Invoice Preparation process to produce a Progress Payment Invoice.
Setting this to false will cause the project to be ignored by the Invoice Preparation process.  */  
   "PPActive":boolean,
      /**  Total contract value for the project. in the Reporting currency  */  
   "Rpt1ConTotValue":number,
      /**  Total contract value for the project. in the Reporting currency  */  
   "Rpt2ConTotValue":number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments.  */  
   "TotLiqToDate":number,
      /**  Total contract value for the project. in the Reporting currency  */  
   "Rpt3ConTotValue":number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then  */  
   "PPCeilingTotal":number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Project currency  */  
   "DocPBFeeLbrCharge":number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  */  
   "Rpt1PBFeeLbrCharge":number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  */  
   "Rpt2PBFeeLbrCharge":number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  */  
   "Rpt3PBFeeLbrCharge":number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Project currency  */  
   "DocPBFeeMiscCharge":number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  */  
   "Rpt1PBFeeMiscCharge":number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  */  
   "Rpt2PBFeeMiscCharge":number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  */  
   "Rpt3PBFeeMiscCharge":number,
      /**  Fee that is to be charged against any material charges on an invoice in the Project currency  */  
   "DocPBFeeMtlCharge":number,
      /**  Fee that is to be charged against any material charges on an invoice in the Reporting currency  */  
   "Rpt1PBFeeMtlCharge":number,
      /**  Fee that is to be charged against any material charges on an invoice in the Reporting currency  */  
   "Rpt2PBFeeMtlCharge":number,
      /**  Fee that is to be charged against any material charges on an invoice in the Reporting currency  */  
   "Rpt3PBFeeMtlCharge":number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Project currency  */  
   "DocPBFeeSubCharge":number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  */  
   "Rpt1PBFeeSubCharge":number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  */  
   "Rpt2PBFeeSubCharge":number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  */  
   "Rpt3PBFeeSubCharge":number,
      /**  Allows individual ceilings to be applied to suppliers  */  
   "PBIndCeilingSup":boolean,
      /**  Allows individual ceilings to be applied to employee  */  
   "PBIndCeilingEmp":boolean,
      /**  Allows individual ceilings to be applied to role  */  
   "PBIndCeilingPRole":boolean,
      /**  Material Cost invoiced by date.  */  
   "PBDocInvoicedMtl":number,
      /**  Labor cost invoiced by date.  */  
   "PBDocInvoicedLbr":number,
      /**  Subcontract cost invoiced by date.  */  
   "PBDocInvoicedSub":number,
      /**  Material Burden Material cost invoiced by date.  */  
   "PBDocInvoicedMtlBur":number,
      /**  Other direct Costs invoiced by date.  */  
   "PBDocInvoicedMisc":number,
      /**  Burden Costs invoiced by date.  */  
   "PBDocInvoicedBur":number,
      /**  Fees charged by date  */  
   "PBDocInvoicedFees":number,
      /**  Next Temporary Invoice number used in the Invoice preparation table before invoice is generated  */  
   "NextTmpInvcNum":number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Project currency  */  
   "DocTotLiqToDate":number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  */  
   "Rpt1TotLiqToDate":number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  */  
   "Rpt2TotLiqToDate":number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  */  
   "Rpt3TotLiqToDate":number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Project currency  */  
   "DocPPCeilingTotal":number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  */  
   "Rpt1PPCeilingTotal":number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  */  
   "Rpt2PPCeilingTotal":number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  */  
   "Rpt3PPCeilingTotal":number,
      /**  Progress Billing - Order Number  */  
   "PBOrderNum":number,
      /**  Progress Payment - Order Number  */  
   "PPOrderNum":number,
      /**  Progress Billing - Order Line  */  
   "PBOrderLine":number,
      /**  Progress Payment - Order Line  */  
   "PPOrderLine":number,
      /**  Project Fee in the Project currency  */  
   "DocPBFeeProject":number,
      /**  Project Fee in the Reporting currency  */  
   "Rpt1PBFeeProject":number,
      /**  Project Fee in the Reporting currency  */  
   "Rpt2PBFeeProject":number,
      /**  Project Fee in the Reporting currency  */  
   "Rpt3PBFeeProject":number,
      /**  Set to true when the close billing has been executed. For Fixed Fee this is set only after all PBillSch are closed. For other types this is set when Close Project is executed.  */  
   "PBClose":boolean,
      /**  This field is set to true after the Project True Up has been executed.  */  
   "PBTrueUp":boolean,
      /**  Defines the Approvals Method for Time related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  */  
   "TimeApprovalsMethod":string,
      /**  Unique identifier of the workflow group for Time transactions related to this Project.  */  
   "TimeWFGroupID":string,
      /**  Defines the Approvals Method for Expenses related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  */  
   "ExpenseApprovalsMethod":string,
      /**  Unique identifier of the workflow group for Expense transactions related to this Project.  */  
   "ExpenseWFGroupID":string,
      /**  Number of Invoices generated for the Project  */  
   "PBNumInvoices":number,
      /**  List of fiscal years for which True Up was called  */  
   "PBTrueUpYearList":string,
      /**  Site Identifier  */  
   "Plant":string,
      /**  Customer Contract Number  */  
   "ConConNum":number,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  material lines. If blank the standard InvcDtl.TaxCatID defaulting will be used.  */  
   "MtlTaxCatID":string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  labor lines.  */  
   "LbrTaxCatID":string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  fee lines.  */  
   "FeeTaxCatID":string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  ODC lines. If blank use the tax category from the PurMisc misc charge code record  */  
   "ODCTaxCatID":string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID Subcontract lines.  */  
   "SubTaxCatID":string,
      /**  Descriptive code assigned by user which uniquely identifies a Tax Category to default for PB Invoice InvcDtl.TaxCatID  Burden lines.  */  
   "BdnTaxCatID":string,
      /**  Calculate taxes on the amount net of the retention (for future use)  */  
   "TaxOnNetOfRet":boolean,
      /**  Date of last project analysis run.  */  
   "LastAnalDate":string,
      /**  Indicates if full Re-gen is required for the project. When this is set, the next generate of project analysis will be full re-gen.  */  
   "RegenReqd":boolean,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling.  */  
   "PBCeilingTotal":number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Project currency  */  
   "DocPBCeilingTotal":number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  */  
   "Rpt1PBCeilingTotal":number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  */  
   "Rpt2PBCeilingTotal":number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  */  
   "Rpt3PBCeilingTotal":number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling.  */  
   "PBCeilingFees":number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Project currency  */  
   "DocPBCeilingFees":number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  */  
   "Rpt1PBCeilingFees":number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  */  
   "Rpt2PBCeilingFees":number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  */  
   "Rpt3PBCeilingFees":number,
      /**  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  */  
   "ChkEmpPrjRole":boolean,
      /**  Progress Payment Liquidation Percentage, used in Get Shipment.  */  
   "PPLiquidPct":number,
      /**  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  */  
   "PPAllOrderLines":boolean,
      /**  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  */  
   "PPAllPrjJobs":boolean,
      /**  AvoidPriceList  */  
   "AvoidPriceList":boolean,
      /**  PbsTaxCatID  */  
   "PbsTaxCatID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  Activate Revenue Recognition at WBS Phase level  */  
   "RecognizeRevenueAtPhaseLevel":boolean,
      /**  Indicates the date when the project is closed, if the project is reopen, the field will be cleared.  */  
   "ClosedDate":string,
      /**  Last action performed on Project as relates to revenue recognition.  */  
   "LastAction":string,
      /**  Date when the LastAction happened to the Project.  */  
   "ActionDate":string,
   "Approved":boolean,
   "Selected":boolean,
   "BitFlag":number,
   "ConCustNumName":string,
   "ConCustNumCustID":string,
   "ConCustNumBTName":string,
   "ConProjMgrLastName":string,
   "ConProjMgrName":string,
   "ConProjMgrFirstName":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "CustNum_c":number,
   "ShipToNum_c":string,
   "LienRequired_c":boolean,
   "DNBComplete_c":boolean,
   "DNBCompletedBy_c":string,
   "PermitRequired_c":boolean,
   "RightToLien_c":boolean,
   "RightToLienWithInDays_c":number,
   "ReviewedBy_c":string,
   "TermsCode_c":string,
   "AdditionalTerms_c":string,
   "PlannedShipDate_c":string,
   "SchedSubmittalDate_c":string,
   "FreightAmt_c":number,
   "NextMilestoneDate_c":string,
   "NextMilestoneDesc_c":string,
   "EstProfit_c":number,
   "EstMargin_c":number,
   "CommissionApproval_c":string,
   "CommissionApprovedBy_c":string,
   "CommissionApprovalDate_c":string,
}

export interface Erp_Tablesets_ProjectCstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Estimated burden cost.  */  
   "EstBurdenCost":number,
      /**  Estimated burden hours.  */  
   "EstBurdenHours":number,
      /**  Estimated labor cost.  */  
   "EstLaborCost":number,
      /**  Estimated labor hours.  */  
   "EstLaborHours":number,
      /**  Estimated subcontract cost.  */  
   "EstSubcontractCost":number,
      /**  Estimated material cost.  */  
   "EstMtlCost":number,
      /**  Estimated material burden cost.  */  
   "EstMtlBurdenCost":number,
      /**  To control if the project phase budget values are to be rolled up to the project  */  
   "RollBudgetstoProject":boolean,
      /**  to control if the project phase manual estimate to complete values are to be rolled up to the project  */  
   "RollManEstToCpte":boolean,
      /**  Total Costd labour hours for the Project  */  
   "TotEstLbrHrs":number,
      /**  Total estimated burden hours for the project  */  
   "TotEstBurdenHrs":number,
      /**  Total estimated labour cost for the project. This is production and setup combined.  */  
   "TotEstLbrCost":number,
      /**  Total estimated material costs for the project  */  
   "TotEstMtlCost":number,
      /**  Total estimated subcontract costs for the project  */  
   "TotEstSubContCost":number,
      /**  Total actual labour hours for the project  */  
   "TotActLbrHrs":number,
      /**  Total actual burden hours for the project.  */  
   "TotActBurHrs":number,
      /**  Total actual labour cost for the project. This is production and setup combined.  */  
   "TotActLbrCost":number,
      /**  Total actual burden cost for the project. This is production and setup combined.  */  
   "TotActBurCost":number,
      /**  Total actual subcontract costs for the project  */  
   "TotActSubContCost":number,
      /**  Total actual material costs for the project  */  
   "TotActMtlCost":number,
      /**  Total actual material burden costs for the project  */  
   "TotActMtlBurCost":number,
      /**  Manually entered estimate to complete for the labour hours for the project.  */  
   "ManEstCtcLbrHrs":number,
      /**  Manually entered estimate to complete for the burden hours for the project.  */  
   "ManEstCtcBurHrs":number,
      /**  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project.  */  
   "ManEstCtcLbrCost":number,
      /**  Manually entered estimate to complete for the burden cost for the project.  */  
   "ManEstCtcBurCost":number,
      /**  Manually entered estimate to complete for the Subcontract cost for the project.  */  
   "ManEstCtcSubConCost":number,
      /**  Manually entered estimate to complete for the material cost for the project.  */  
   "ManEstCtcMtlCost":number,
      /**  Manually entered estimate to complete for the material burden cost for the project.  */  
   "ManEstCtcMtlBurCost":number,
      /**  Total calculated cost to complete labour hours for the project.  */  
   "TotCtcLbrHours":number,
      /**  Total calculated cost to complete burden hours for the project.  */  
   "TotCtcBurHours":number,
      /**  Total calculated cost to complete burden cost for the project. This will be both production and setup.  */  
   "TotCtcBurCost":number,
      /**  Total calculated cost to complete labour cost for the project. This will be both production and setup.  */  
   "TotCtcLbrCost":number,
      /**  Total calculated cost to complete subcontract cost for the project.  */  
   "TotCtcSubConCost":number,
      /**  Total calculated cost to complete material cost for the project.  */  
   "TotCtcMtlCost":number,
      /**  Total calculated cost to complete material burden cost for the project.  */  
   "TotCtcMtlBurCost":number,
      /**  Total quoted labour hours for the project  */  
   "TotQuotLbrHrs":number,
      /**  Total quoted burden hours for the project  */  
   "TotQuotBurHrs":number,
      /**  Total quoted labour cost for the project. This will be both production and setup.  */  
   "TotQuotLbrCost":number,
      /**  Total quoted subcontract cost for the project.  */  
   "TotQuotSubContCost":number,
      /**  Total quoted material cost for the project.  */  
   "TotQuotMtlCost":number,
      /**  Total quoted material burden cost for the project.  */  
   "TotQuotMtlBurCost":number,
      /**  Total estimated burden costs for the project  */  
   "TotEstBurCost":number,
      /**  Total quoted burden cost for the project. This will be both production and setup.  */  
   "TotQuotBurCost":number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  */  
   "RevenueRecAutoToDate":number,
      /**  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   "MaterialRecAutoCstTodate":number,
      /**  The labor costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   "LaborRecAutoCstTodate":number,
      /**  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   "BurdenRecAutoCstTodate":number,
      /**  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  */  
   "MtlBurdenRecAutoCstTodate":number,
      /**  Total budget labour hours for the Project  */  
   "BudTotLbrHours":number,
      /**  Total budget burden hours for the Project  */  
   "BudTotBurHrs":number,
      /**  Total budget labour cost for the Project. This is production and setup combined.  */  
   "BudTotLbrCost":number,
      /**  Total budget burden cost for the Project. This is production and setup combined.  */  
   "BudTotBurCost":number,
      /**  Total budget subcontract costs for the Project  */  
   "BudTotSubCost":number,
      /**  Total budget material costs for the Project  */  
   "BudTotMtlCost":number,
      /**  Total budget material burden costs for the Project phase.  */  
   "BudTotMtlBurCost":number,
      /**  Total estimated material burden costs for the Project phase  */  
   "TotEstMtlBurCost":number,
      /**  The subcontract costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  */  
   "SubConRecAutoCstTodate":number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  */  
   "RevenueRecManToDate":number,
      /**  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   "MaterialRecManCstTodate":number,
      /**  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   "LaborRecManCstTodate":number,
      /**  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  */  
   "BurdenRecManCstTodate":number,
      /**  The subcontract costs posted to cost of sales to date. This is cost that has been manually recognised using this process  */  
   "SubConRecManCstTodate":number,
      /**  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   "MtlBurdenRecManCstTodate":number,
      /**  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  */  
   "MaterialCostOfSales":number,
      /**  The labor costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  */  
   "LaborCostOfSales":number,
      /**  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  */  
   "BurdenCostOfSales":number,
      /**  The subcontract costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActSubContractCost  */  
   "SubConCostOfSales":number,
      /**  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  */  
   "MtlBurdenCostOfSales":number,
      /**  Other Direct Cost Quoted  */  
   "TotQuotODCCost":number,
      /**  Other Direct Cost Estimated  */  
   "TotEstODCCost":number,
      /**  ODC Actual  */  
   "TotActODCCost":number,
      /**  Other direct cost manual CTC  */  
   "ManEstCTCODCCost":number,
      /**  Other direct Cost total CTC  */  
   "TotCTCODCCost":number,
      /**  Other direct Cost Budget Total  */  
   "BudTotODCCost":number,
      /**  Other Direct cost Recognition to Date  */  
   "ODCRecAutoCstToDate":number,
      /**  Other Direct Cost Manual Recognition to Date  */  
   "ODCRecManCstTodate":number,
      /**  Estimated other direct cost  */  
   "EstODCCost":number,
      /**  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  */  
   "BdnRecSeqPosted":number,
      /**  Number of Recalculation of burden amounts created by Revenue Recognition process  */  
   "BdnRecSeqLastAdded":number,
      /**  Sum of all Actual Burden Charges posted by today  */  
   "BdnRevenueAutoToday":number,
      /**  AsOfDate  */  
   "AsOfDate":string,
      /**  BuildAnalysis  */  
   "BuildAnalysis":boolean,
      /**  LbrPur  */  
   "LbrPur":number,
      /**  BurPur  */  
   "BurPur":number,
      /**  MtlPur  */  
   "MtlPur":number,
      /**  SubPur  */  
   "SubPur":number,
      /**  MtlBurPur  */  
   "MtlBurPur":number,
      /**  ODCPur  */  
   "ODCPur":number,
      /**  LaborLbrCstToDate  */  
   "LaborLbrCstToDate":number,
      /**  BurdenLbrCstToDate  */  
   "BurdenLbrCstToDate":number,
      /**  ActMtlNonJobCost  */  
   "ActMtlNonJobCost":number,
      /**  RecManPosted  */  
   "RecManPosted":number,
      /**  LbrManPosted  */  
   "LbrManPosted":number,
      /**  BurManPosted  */  
   "BurManPosted":number,
      /**  MtlManPosted  */  
   "MtlManPosted":number,
      /**  SubCManPosted  */  
   "SubCManPosted":number,
      /**  MtlBurManPosted  */  
   "MtlBurManPosted":number,
      /**  ODCManPosted  */  
   "ODCManPosted":number,
      /**  Reverse  */  
   "Reverse":string,
      /**  NextTmpInvcNum  */  
   "NextTmpInvcNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Percentage of Completion  */  
   "PercentageOfCompletion":number,
      /**  Labor Cost To Be Recognized  */  
   "ToBeRecognizedLbrCost":number,
      /**  Burden Cost To Be Recognized  */  
   "ToBeRecognizedBurCost":number,
      /**  Material Cost To Be Recognized  */  
   "ToBeRecognizedMtlCost":number,
      /**  Subcontract Cost To Be Recognized  */  
   "ToBeRecognizedSubCost":number,
      /**  Material Burden Cost To Be Recognized  */  
   "ToBeRecognizedMtlBurCost":number,
      /**  ODC Cost To Be Recognized  */  
   "ToBeRecognizedODCCost":number,
      /**  Revenue To Be Recognized  */  
   "ToBeRecognizedRevenue":number,
      /**  BillingToDate  */  
   "BillingToDate":number,
      /**  RecogToDtBilling  */  
   "RecogToDtBilling":number,
      /**  TotProjRev  */  
   "TotProjRev":number,
      /**  RecogToDtLbk  */  
   "RecogToDtLbk":number,
      /**  RecogToDtManual  */  
   "RecogToDtManual":number,
      /**  RetentionDt  */  
   "RetentionDt":number,
   "CurrencyCode":string,
   "DocBudTotBurCost":number,
   "DocBudTotLbrCost":number,
   "DocBudTotMtlBurCost":number,
   "DocBudTotMtlCost":number,
   "DocBudTotODCCost":number,
   "DocBudTotSubCost":number,
   "DocEstBurdenCost":number,
   "DocEstLaborCost":number,
   "DocEstMtlBurdenCost":number,
   "DocEstMtlCost":number,
   "DocEstODCCost":number,
   "DocEstSubcontractCost":number,
   "DocEstTotalCost":number,
   "DocGTActualCost":number,
   "DocGTBudgetCost":number,
   "DocGTCalculatedCost":number,
   "DocGTEstimatedCost":number,
   "DocGTManualCost":number,
   "DocGTQuotedCost":number,
   "DocProjectedTotalBurCost":number,
   "DocProjectedTotalCost":number,
   "DocProjectedTotalLbrCost":number,
   "DocProjectedTotalMtlBurCost":number,
   "DocProjectedTotalMtlCost":number,
   "DocProjectedTotalODCCost":number,
   "DocProjectedTotalSubContCost":number,
   "DocTotActMtlBurCost":number,
   "DocTotActMtlCost":number,
   "DocTotActODCCost":number,
   "DocTotActSubContCost":number,
   "DocTotCtcBurCost":number,
   "DocTotCtcLbrCost":number,
   "DocTotCtcMtlBurCost":number,
   "DocTotCtcMtlCost":number,
   "DocTotCTCODCCost":number,
   "DocTotCtcSubConCost":number,
   "DocTotEstBurCost":number,
   "DocTotEstLbrCost":number,
   "DocTotEstMtlBurCost":number,
   "DocTotEstMtlCost":number,
   "DocTotEstODCCost":number,
   "DocTotEstSubContCost":number,
   "DocTotQuotBurCost":number,
   "DocTotQuotLbrCost":number,
   "DocTotQuotMtlBurCost":number,
   "DocTotQuotMtlCost":number,
   "DocTotQuotODCCost":number,
   "DocTotQuotSubContCost":number,
      /**  This is a calculated field: the sum of the other Project.Est*Cost fields.  It is not stored in the database.  */  
   "EstTotalCost":number,
   "GTActualCost":number,
   "GTBudgetCost":number,
   "GTCalculatedCost":number,
   "GTEstimatedCost":number,
   "GTManualCost":number,
   "GTQuotedCost":number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   "ProjectedTotalBurCost":number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   "ProjectedTotalCost":number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   "ProjectedTotalLbrCost":number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   "ProjectedTotalMtlBurCost":number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   "ProjectedTotalMtlCost":number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   "ProjectedTotalODCCost":number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   "ProjectedTotalSubContCost":number,
      /**  Recognized to Date Billing  */  
   "ReconToDtBilling":number,
   "Rpt1BudTotBurCost":number,
   "Rpt1BudTotLbrCost":number,
   "Rpt1BudTotMtlBurCost":number,
   "Rpt1BudTotMtlCost":number,
   "Rpt1BudTotODCCost":number,
   "Rpt1BudTotSubCost":number,
   "Rpt1EstBurdenCost":number,
   "Rpt1EstLaborCost":number,
   "Rpt1EstMtlBurdenCost":number,
   "Rpt1EstMtlCost":number,
   "Rpt1EstODCCost":number,
   "Rpt1EstSubcontractCost":number,
   "Rpt1EstTotalCost":number,
   "Rpt1GTActualCost":number,
   "Rpt1GTBudgetCost":number,
   "Rpt1GTCalculatedCost":number,
   "Rpt1GTEstimatedCost":number,
   "Rpt1GTManualCost":number,
   "Rpt1GTQuotedCost":number,
   "Rpt1ManEstCtcBurCost":number,
   "Rpt1ManEstCtcLbrCost":number,
   "Rpt1ManEstCtcMtlBurCost":number,
   "Rpt1ManEstCtcMtlCost":number,
   "Rpt1ManEstCTCODCCost":number,
   "Rpt1ManEstCtcSubConCost":number,
   "Rpt1ProjectedTotalBurCost":number,
   "Rpt1ProjectedTotalCost":number,
   "Rpt1ProjectedTotalLbrCost":number,
   "Rpt1ProjectedTotalMtlBurCost":number,
   "Rpt1ProjectedTotalMtlCost":number,
   "Rpt1ProjectedTotalODCCost":number,
   "Rpt1ProjectedTotalSubContCost":number,
   "Rpt1TotActBurCost":number,
   "Rpt1TotActLbrCost":number,
   "Rpt1TotActMtlBurCost":number,
   "Rpt1TotActMtlCost":number,
   "Rpt1TotActODCCost":number,
   "Rpt1TotActSubContCost":number,
   "Rpt1TotCtcBurCost":number,
   "Rpt1TotCtcLbrCost":number,
   "Rpt1TotCtcMtlBurCost":number,
   "Rpt1TotCtcMtlCost":number,
   "Rpt1TotCTCODCCost":number,
   "Rpt1TotCtcSubConCost":number,
   "Rpt1TotEstBurCost":number,
   "Rpt1TotEstLbrCost":number,
   "Rpt1TotEstMtlBurCost":number,
   "Rpt1TotEstMtlCost":number,
   "Rpt1TotEstODCCost":number,
   "Rpt1TotEstSubContCost":number,
   "Rpt1TotQuotBurCost":number,
   "Rpt1TotQuotLbrCost":number,
   "Rpt1TotQuotMtlBurCost":number,
   "Rpt1TotQuotMtlCost":number,
   "Rpt1TotQuotODCCost":number,
   "Rpt1TotQuotSubContCost":number,
   "Rpt2BudTotBurCost":number,
   "Rpt2BudTotLbrCost":number,
   "Rpt2BudTotMtlBurCost":number,
   "Rpt2BudTotMtlCost":number,
   "Rpt2BudTotODCCost":number,
   "Rpt2BudTotSubCost":number,
   "Rpt2EstBurdenCost":number,
   "Rpt2EstLaborCost":number,
   "Rpt2EstMtlBurdenCost":number,
   "Rpt2EstMtlCost":number,
   "Rpt2EstODCCost":number,
   "Rpt2EstSubcontractCost":number,
   "Rpt2EstTotalCost":number,
   "Rpt2GTActualCost":number,
   "Rpt2GTBudgetCost":number,
   "Rpt2GTCalculatedCost":number,
   "Rpt2GTEstimatedCost":number,
   "Rpt2GTManualCost":number,
   "Rpt2GTQuotedCost":number,
   "Rpt2ManEstCtcBurCost":number,
   "Rpt2ManEstCtcLbrCost":number,
   "Rpt2ManEstCtcMtlBurCost":number,
   "Rpt2ManEstCtcMtlCost":number,
   "Rpt2ManEstCTCODCCost":number,
   "Rpt2ManEstCtcSubConCost":number,
   "Rpt2ProjectedTotalBurCost":number,
   "Rpt2ProjectedTotalCost":number,
   "Rpt2ProjectedTotalLbrCost":number,
   "Rpt2ProjectedTotalMtlBurCost":number,
   "Rpt2ProjectedTotalMtlCost":number,
   "Rpt2ProjectedTotalODCCost":number,
   "Rpt2ProjectedTotalSubContCost":number,
   "Rpt2TotActBurCost":number,
   "Rpt2TotActLbrCost":number,
   "Rpt2TotActMtlBurCost":number,
   "Rpt2TotActMtlCost":number,
   "Rpt2TotActODCCost":number,
   "Rpt2TotActSubContCost":number,
   "Rpt2TotCtcBurCost":number,
   "Rpt2TotCtcLbrCost":number,
   "Rpt2TotCtcMtlBurCost":number,
   "Rpt2TotCtcMtlCost":number,
   "Rpt2TotCTCODCCost":number,
   "Rpt2TotCtcSubConCost":number,
   "Rpt2TotEstBurCost":number,
   "Rpt2TotEstLbrCost":number,
   "Rpt2TotEstMtlBurCost":number,
   "Rpt2TotEstMtlCost":number,
   "Rpt2TotEstODCCost":number,
   "Rpt2TotEstSubContCost":number,
   "Rpt2TotQuotBurCost":number,
   "Rpt2TotQuotLbrCost":number,
   "Rpt2TotQuotMtlBurCost":number,
   "Rpt2TotQuotMtlCost":number,
   "Rpt2TotQuotODCCost":number,
   "Rpt2TotQuotSubContCost":number,
   "Rpt3BudTotBurCost":number,
   "Rpt3BudTotLbrCost":number,
   "Rpt3BudTotMtlBurCost":number,
   "Rpt3BudTotMtlCost":number,
   "Rpt3BudTotODCCost":number,
   "Rpt3BudTotSubCost":number,
   "Rpt3EstBurdenCost":number,
   "Rpt3EstLaborCost":number,
   "Rpt3EstMtlBurdenCost":number,
   "Rpt3EstMtlCost":number,
   "Rpt3EstODCCost":number,
   "Rpt3EstSubcontractCost":number,
   "Rpt3EstTotalCost":number,
   "Rpt3GTActualCost":number,
   "Rpt3GTBudgetCost":number,
   "Rpt3GTCalculatedCost":number,
   "Rpt3GTEstimatedCost":number,
   "Rpt3GTManualCost":number,
   "Rpt3GTQuotedCost":number,
   "Rpt3ManEstCtcBurCost":number,
   "Rpt3ManEstCtcLbrCost":number,
   "Rpt3ManEstCtcMtlBurCost":number,
   "Rpt3ManEstCtcMtlCost":number,
   "Rpt3ManEstCTCODCCost":number,
   "Rpt3ManEstCtcSubConCost":number,
   "Rpt3ProjectedTotalBurCost":number,
   "Rpt3ProjectedTotalCost":number,
   "Rpt3ProjectedTotalLbrCost":number,
   "Rpt3ProjectedTotalMtlBurCost":number,
   "Rpt3ProjectedTotalMtlCost":number,
   "Rpt3ProjectedTotalODCCost":number,
   "Rpt3ProjectedTotalSubContCost":number,
   "Rpt3TotActBurCost":number,
   "Rpt3TotActLbrCost":number,
   "Rpt3TotActMtlBurCost":number,
   "Rpt3TotActMtlCost":number,
   "Rpt3TotActODCCost":number,
   "Rpt3TotActSubContCost":number,
   "Rpt3TotCtcBurCost":number,
   "Rpt3TotCtcLbrCost":number,
   "Rpt3TotCtcMtlBurCost":number,
   "Rpt3TotCtcMtlCost":number,
   "Rpt3TotCTCODCCost":number,
   "Rpt3TotCtcSubConCost":number,
   "Rpt3TotEstBurCost":number,
   "Rpt3TotEstLbrCost":number,
   "Rpt3TotEstMtlBurCost":number,
   "Rpt3TotEstMtlCost":number,
   "Rpt3TotEstODCCost":number,
   "Rpt3TotEstSubContCost":number,
   "Rpt3TotQuotBurCost":number,
   "Rpt3TotQuotLbrCost":number,
   "Rpt3TotQuotMtlBurCost":number,
   "Rpt3TotQuotMtlCost":number,
   "Rpt3TotQuotODCCost":number,
   "Rpt3TotQuotSubContCost":number,
   "DocManEstCtcBurCost":number,
   "DocManEstCtcLbrCost":number,
   "DocManEstCtcMtlBurCost":number,
   "DocManEstCtcMtlCost":number,
   "DocManEstCTCODCCost":number,
   "DocManEstCtcSubConCost":number,
   "DocTotActBurCost":number,
   "DocTotActLbrCost":number,
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
      @param projectID
   */  
export interface DeleteByID_input{
   projectID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ProjFilterRow{
   ContractAmtFrom:number,
   ContractAmtTo:number,
   CustomerName:string,
   Description:string,
   ProjectIDFrom:string,
   ProjectIDTo:string,
   ProjectManagerID:string,
   Selected:boolean,
   StartDateFrom:string,
   StartDateTo:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProjFilterTableset{
   ProjFilter:Erp_Tablesets_ProjFilterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProjMultiListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Full description of Project Management Code.  */  
   Description:string,
      /**  Start Date of the project  */  
   StartDate:string,
      /**  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  */  
   ConCustNum:number,
      /**  Employee ID of the person who has responsibility for the project  */  
   ConProjMgr:string,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  */  
   ConInvMeth:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  Last action performed on Project as relates to revenue recognition.  */  
   LastAction:string,
      /**  Date when the LastAction happened to the Project.  */  
   ActionDate:string,
   Approved:boolean,
   Selected:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProjMultiListTableset{
   ProjMultiList:Erp_Tablesets_ProjMultiListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProjMultiRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Full description of Project Management Code.  */  
   Description:string,
      /**  Indicates if this Project is active.  Can be changed directly by the user during entry.  */  
   ActiveProject:boolean,
      /**  Editor widget for project comments.  */  
   CommentText:string,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**  Will contain the coma separated list of the fields that the user has added to the project from within Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMap:string,
      /**  Will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Holds the default project warehouse code.  */  
   WarehouseCode:string,
      /**  Holds the default project bin code.  */  
   BinNum:string,
      /**  This holds the top level job to which all of the jobs created for a WBS Phase will be associated  */  
   PrimaryJob:string,
      /**  This is the material placeholder in the primary project job to which all WBS Phase jobs will be linked.  */  
   PrimaryMtl:number,
      /**  The sales category code used in the Revenue recognition process.  */  
   SalesCatID:string,
      /**  The Product Group code used in the Revenue Recognition process.  */  
   ProdCode:string,
      /**  RESERVED FOR FUTURE USE: Logical field. When set to true it indicates that the journals created to recognise the revenue for the project have been reversed.  */  
   CloseAccrual:boolean,
      /**  Assembly Seq from JobAsmbl record.  */  
   PrimaryAsmSeq:number,
      /**  Start Date of the project  */  
   StartDate:string,
      /**  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  */  
   ConCustNum:number,
      /**  Contract start date  */  
   ConStartDate:string,
      /**  Date the contract is due to be complete  */  
   ConEndDate:string,
      /**  Projected Contract End Date. Defaults to the Contract End Date but can be used to report on the projected end date.  */  
   ConProjectedEnd:string,
      /**   Contract Reference number for project.
At the Epicor 9.05 release this field is reference only, at the Epicor 9.1 release when the whole contract system is enhanced then this field will reference an actual contract and a search will be provided.  */  
   ConReference:string,
      /**  Employee ID of the person who has responsibility for the project  */  
   ConProjMgr:string,
      /**  Total contract value for the project.  */  
   ConTotValue:number,
      /**  Value of the posted invoices to date (system field)  */  
   ConTotInv:number,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  */  
   ConInvMeth:string,
      /**  Foreign key to the QMarkUp  */  
   MarkUpID:string,
      /**  Override of Labor Markup Percent  */  
   PBLbMarkUp:number,
      /**  Override of Material Markup Percent  */  
   PBMtlMarkUp:number,
      /**  Override of Subcontract Markup Percentage  */  
   PBSubMarkUp:number,
      /**  Override of Other Direct Cost Markup %  */  
   PBMiscMarkUp:number,
      /**  Retention percentage. How this is used is dependent on RetentionProc field.  */  
   PBRetentionPcnt:number,
      /**   How the retention percentage will be used.
The options are ?M? = Maximum of Contract Value
?P? = Percent of Invoice Value.  */  
   PBRetentionProc:string,
      /**  Project Fee  */  
   PBFeeProject:number,
      /**  Apply Fee with list of the options: F =  First Invoice Only, A = All Invoices  */  
   PBFeeApply:string,
      /**  Fee Type with list of the options: P = Percentage, F = Fixed Amount  */  
   PBFeeType:string,
      /**  Apply Fees on list with the options: N = Net Cost, G = Gross Cost.  */  
   PBFeeApplyOn:string,
      /**  Fee Invoice Text in Free format to allow the user to enter text that will be displayed on the invoice  */  
   PBFeeInvoiceText:string,
      /**  Fee that is to be charged against any labor charges on an invoice  */  
   PBFeeLbrCharge:number,
      /**  Labor Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   PBFeeLbrType:string,
      /**  Labor Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   PBFeeLbrApply:string,
      /**  Fee that is to be charged against any material charges on an invoice  */  
   PBFeeMtlCharge:number,
      /**  Material Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   PBFeeMtlType:string,
      /**  Material Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   PBFeeMtlApply:string,
      /**  Fee that is to be charged against any Subcontract charges on an invoice.  */  
   PBFeeSubCharge:number,
      /**  Subcontract Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   PBFeeSubType:string,
      /**  Subcontract Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   PBFeeSubApply:string,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice.  */  
   PBFeeMiscCharge:number,
      /**  Miscellaneous Fee Type of with list of the options: P = Percentage, F = Fixed Amount  */  
   PBFeeMiscType:string,
      /**  Miscellaneous Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  */  
   PBFeeMiscApply:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Contract Customer Bill To number, foreign key to Customer  */  
   ConBTCustNum:number,
      /**  If invoices are allowed to be generated even if the element is over the predefined ceiling.  */  
   ConOverCeiling:boolean,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   ConRevMethod:string,
      /**  Price list is used to establish the price for any materials when the invoicing method is set to T & M or Cost Plus. Can be empty.  */  
   ConListCode:string,
      /**  Hours for Invoicing allows the user to decide which hours are to be used by the invoicing process, it has system list with the options: L =  Labor, B = Burden  */  
   ConHrsInvc:string,
      /**  Rate Type Code  */  
   RateGrpCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   LockRate:boolean,
      /**  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  */  
   ExchangeRate:number,
      /**  This is the projected end date of the project but is not required and is only used if entered in the creation of the project job and for any user reporting requirements.  */  
   EndDate:string,
      /**  Defaults from JCSyst.DfltPrjRtSrc. Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  */  
   PBPrjRtSrc:string,
      /**  Value of the posted invoices to date (system field) in the Project currency  */  
   DocConTotInv:number,
      /**  If set to true a new primary job will be created automatically for the project.  */  
   CreatePrjJob:boolean,
      /**  Value of the posted invoices to date (system field) in the Reporting currency  */  
   Rpt1ConTotInv:number,
      /**  Project revision number  */  
   Revision:number,
      /**  Value of the posted invoices to date (system field) in the Reporting currency  */  
   Rpt2ConTotInv:number,
      /**   This is the percentage of the costs for material, labor and burden that will be invoiced.
This is also used by the invoice entry process when invoicing regular shipments to determine the actual value of the invoice and how much will be relieved from the Progress Payments to date.  */  
   PPAllowPcnt:number,
      /**  Value of the posted invoices to date (system field) in the Reporting currency  */  
   Rpt3ConTotInv:number,
      /**   This will allow regular shipments to be invoiced normally.
Setting the field to true will cause the Customer Shipment process to place any packing slips for any sales order associated with the project to be placed on hold to prevent them being selected for invoicing. 
When the user changes this flag to true it will trigger business logic that will release the shipments for invoicing.  */  
   HoldPrdInv:boolean,
      /**  Total contract value for the project. in the Project currency  */  
   DocConTotValue:number,
      /**   This will default to true which will then trigger the Invoice Preparation process to produce a Progress Payment Invoice.
Setting this to false will cause the project to be ignored by the Invoice Preparation process.  */  
   PPActive:boolean,
      /**  Total contract value for the project. in the Reporting currency  */  
   Rpt1ConTotValue:number,
      /**  Total contract value for the project. in the Reporting currency  */  
   Rpt2ConTotValue:number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments.  */  
   TotLiqToDate:number,
      /**  Total contract value for the project. in the Reporting currency  */  
   Rpt3ConTotValue:number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then  */  
   PPCeilingTotal:number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Project currency  */  
   DocPBFeeLbrCharge:number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  */  
   Rpt1PBFeeLbrCharge:number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  */  
   Rpt2PBFeeLbrCharge:number,
      /**  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  */  
   Rpt3PBFeeLbrCharge:number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Project currency  */  
   DocPBFeeMiscCharge:number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  */  
   Rpt1PBFeeMiscCharge:number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  */  
   Rpt2PBFeeMiscCharge:number,
      /**  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  */  
   Rpt3PBFeeMiscCharge:number,
      /**  Fee that is to be charged against any material charges on an invoice in the Project currency  */  
   DocPBFeeMtlCharge:number,
      /**  Fee that is to be charged against any material charges on an invoice in the Reporting currency  */  
   Rpt1PBFeeMtlCharge:number,
      /**  Fee that is to be charged against any material charges on an invoice in the Reporting currency  */  
   Rpt2PBFeeMtlCharge:number,
      /**  Fee that is to be charged against any material charges on an invoice in the Reporting currency  */  
   Rpt3PBFeeMtlCharge:number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Project currency  */  
   DocPBFeeSubCharge:number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  */  
   Rpt1PBFeeSubCharge:number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  */  
   Rpt2PBFeeSubCharge:number,
      /**  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  */  
   Rpt3PBFeeSubCharge:number,
      /**  Allows individual ceilings to be applied to suppliers  */  
   PBIndCeilingSup:boolean,
      /**  Allows individual ceilings to be applied to employee  */  
   PBIndCeilingEmp:boolean,
      /**  Allows individual ceilings to be applied to role  */  
   PBIndCeilingPRole:boolean,
      /**  Material Cost invoiced by date.  */  
   PBDocInvoicedMtl:number,
      /**  Labor cost invoiced by date.  */  
   PBDocInvoicedLbr:number,
      /**  Subcontract cost invoiced by date.  */  
   PBDocInvoicedSub:number,
      /**  Material Burden Material cost invoiced by date.  */  
   PBDocInvoicedMtlBur:number,
      /**  Other direct Costs invoiced by date.  */  
   PBDocInvoicedMisc:number,
      /**  Burden Costs invoiced by date.  */  
   PBDocInvoicedBur:number,
      /**  Fees charged by date  */  
   PBDocInvoicedFees:number,
      /**  Next Temporary Invoice number used in the Invoice preparation table before invoice is generated  */  
   NextTmpInvcNum:number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Project currency  */  
   DocTotLiqToDate:number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  */  
   Rpt1TotLiqToDate:number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  */  
   Rpt2TotLiqToDate:number,
      /**  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  */  
   Rpt3TotLiqToDate:number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Project currency  */  
   DocPPCeilingTotal:number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  */  
   Rpt1PPCeilingTotal:number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  */  
   Rpt2PPCeilingTotal:number,
      /**  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  */  
   Rpt3PPCeilingTotal:number,
      /**  Progress Billing - Order Number  */  
   PBOrderNum:number,
      /**  Progress Payment - Order Number  */  
   PPOrderNum:number,
      /**  Progress Billing - Order Line  */  
   PBOrderLine:number,
      /**  Progress Payment - Order Line  */  
   PPOrderLine:number,
      /**  Project Fee in the Project currency  */  
   DocPBFeeProject:number,
      /**  Project Fee in the Reporting currency  */  
   Rpt1PBFeeProject:number,
      /**  Project Fee in the Reporting currency  */  
   Rpt2PBFeeProject:number,
      /**  Project Fee in the Reporting currency  */  
   Rpt3PBFeeProject:number,
      /**  Set to true when the close billing has been executed. For Fixed Fee this is set only after all PBillSch are closed. For other types this is set when Close Project is executed.  */  
   PBClose:boolean,
      /**  This field is set to true after the Project True Up has been executed.  */  
   PBTrueUp:boolean,
      /**  Defines the Approvals Method for Time related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  */  
   TimeApprovalsMethod:string,
      /**  Unique identifier of the workflow group for Time transactions related to this Project.  */  
   TimeWFGroupID:string,
      /**  Defines the Approvals Method for Expenses related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  */  
   ExpenseApprovalsMethod:string,
      /**  Unique identifier of the workflow group for Expense transactions related to this Project.  */  
   ExpenseWFGroupID:string,
      /**  Number of Invoices generated for the Project  */  
   PBNumInvoices:number,
      /**  List of fiscal years for which True Up was called  */  
   PBTrueUpYearList:string,
      /**  Site Identifier  */  
   Plant:string,
      /**  Customer Contract Number  */  
   ConConNum:number,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  material lines. If blank the standard InvcDtl.TaxCatID defaulting will be used.  */  
   MtlTaxCatID:string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  labor lines.  */  
   LbrTaxCatID:string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  fee lines.  */  
   FeeTaxCatID:string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID  ODC lines. If blank use the tax category from the PurMisc misc charge code record  */  
   ODCTaxCatID:string,
      /**  Tax Category to default for PB Invoice InvcDtl.TaxCatID Subcontract lines.  */  
   SubTaxCatID:string,
      /**  Descriptive code assigned by user which uniquely identifies a Tax Category to default for PB Invoice InvcDtl.TaxCatID  Burden lines.  */  
   BdnTaxCatID:string,
      /**  Calculate taxes on the amount net of the retention (for future use)  */  
   TaxOnNetOfRet:boolean,
      /**  Date of last project analysis run.  */  
   LastAnalDate:string,
      /**  Indicates if full Re-gen is required for the project. When this is set, the next generate of project analysis will be full re-gen.  */  
   RegenReqd:boolean,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling.  */  
   PBCeilingTotal:number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Project currency  */  
   DocPBCeilingTotal:number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  */  
   Rpt1PBCeilingTotal:number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  */  
   Rpt2PBCeilingTotal:number,
      /**  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  */  
   Rpt3PBCeilingTotal:number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling.  */  
   PBCeilingFees:number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Project currency  */  
   DocPBCeilingFees:number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  */  
   Rpt1PBCeilingFees:number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  */  
   Rpt2PBCeilingFees:number,
      /**  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  */  
   Rpt3PBCeilingFees:number,
      /**  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  */  
   ChkEmpPrjRole:boolean,
      /**  Progress Payment Liquidation Percentage, used in Get Shipment.  */  
   PPLiquidPct:number,
      /**  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  */  
   PPAllOrderLines:boolean,
      /**  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  */  
   PPAllPrjJobs:boolean,
      /**  AvoidPriceList  */  
   AvoidPriceList:boolean,
      /**  PbsTaxCatID  */  
   PbsTaxCatID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  Activate Revenue Recognition at WBS Phase level  */  
   RecognizeRevenueAtPhaseLevel:boolean,
      /**  Indicates the date when the project is closed, if the project is reopen, the field will be cleared.  */  
   ClosedDate:string,
      /**  Last action performed on Project as relates to revenue recognition.  */  
   LastAction:string,
      /**  Date when the LastAction happened to the Project.  */  
   ActionDate:string,
   Approved:boolean,
   Selected:boolean,
   BitFlag:number,
   ConCustNumName:string,
   ConCustNumCustID:string,
   ConCustNumBTName:string,
   ConProjMgrLastName:string,
   ConProjMgrName:string,
   ConProjMgrFirstName:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   CustNum_c:number,
   ShipToNum_c:string,
   LienRequired_c:boolean,
   DNBComplete_c:boolean,
   DNBCompletedBy_c:string,
   PermitRequired_c:boolean,
   RightToLien_c:boolean,
   RightToLienWithInDays_c:number,
   ReviewedBy_c:string,
   TermsCode_c:string,
   AdditionalTerms_c:string,
   PlannedShipDate_c:string,
   SchedSubmittalDate_c:string,
   FreightAmt_c:number,
   NextMilestoneDate_c:string,
   NextMilestoneDesc_c:string,
   EstProfit_c:number,
   EstMargin_c:number,
   CommissionApproval_c:string,
   CommissionApprovedBy_c:string,
   CommissionApprovalDate_c:string,
}

export interface Erp_Tablesets_ProjMultiTableset{
   ProjMulti:Erp_Tablesets_ProjMultiRow[],
   ProjectCst:Erp_Tablesets_ProjectCstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProjectCstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Estimated burden cost.  */  
   EstBurdenCost:number,
      /**  Estimated burden hours.  */  
   EstBurdenHours:number,
      /**  Estimated labor cost.  */  
   EstLaborCost:number,
      /**  Estimated labor hours.  */  
   EstLaborHours:number,
      /**  Estimated subcontract cost.  */  
   EstSubcontractCost:number,
      /**  Estimated material cost.  */  
   EstMtlCost:number,
      /**  Estimated material burden cost.  */  
   EstMtlBurdenCost:number,
      /**  To control if the project phase budget values are to be rolled up to the project  */  
   RollBudgetstoProject:boolean,
      /**  to control if the project phase manual estimate to complete values are to be rolled up to the project  */  
   RollManEstToCpte:boolean,
      /**  Total Costd labour hours for the Project  */  
   TotEstLbrHrs:number,
      /**  Total estimated burden hours for the project  */  
   TotEstBurdenHrs:number,
      /**  Total estimated labour cost for the project. This is production and setup combined.  */  
   TotEstLbrCost:number,
      /**  Total estimated material costs for the project  */  
   TotEstMtlCost:number,
      /**  Total estimated subcontract costs for the project  */  
   TotEstSubContCost:number,
      /**  Total actual labour hours for the project  */  
   TotActLbrHrs:number,
      /**  Total actual burden hours for the project.  */  
   TotActBurHrs:number,
      /**  Total actual labour cost for the project. This is production and setup combined.  */  
   TotActLbrCost:number,
      /**  Total actual burden cost for the project. This is production and setup combined.  */  
   TotActBurCost:number,
      /**  Total actual subcontract costs for the project  */  
   TotActSubContCost:number,
      /**  Total actual material costs for the project  */  
   TotActMtlCost:number,
      /**  Total actual material burden costs for the project  */  
   TotActMtlBurCost:number,
      /**  Manually entered estimate to complete for the labour hours for the project.  */  
   ManEstCtcLbrHrs:number,
      /**  Manually entered estimate to complete for the burden hours for the project.  */  
   ManEstCtcBurHrs:number,
      /**  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project.  */  
   ManEstCtcLbrCost:number,
      /**  Manually entered estimate to complete for the burden cost for the project.  */  
   ManEstCtcBurCost:number,
      /**  Manually entered estimate to complete for the Subcontract cost for the project.  */  
   ManEstCtcSubConCost:number,
      /**  Manually entered estimate to complete for the material cost for the project.  */  
   ManEstCtcMtlCost:number,
      /**  Manually entered estimate to complete for the material burden cost for the project.  */  
   ManEstCtcMtlBurCost:number,
      /**  Total calculated cost to complete labour hours for the project.  */  
   TotCtcLbrHours:number,
      /**  Total calculated cost to complete burden hours for the project.  */  
   TotCtcBurHours:number,
      /**  Total calculated cost to complete burden cost for the project. This will be both production and setup.  */  
   TotCtcBurCost:number,
      /**  Total calculated cost to complete labour cost for the project. This will be both production and setup.  */  
   TotCtcLbrCost:number,
      /**  Total calculated cost to complete subcontract cost for the project.  */  
   TotCtcSubConCost:number,
      /**  Total calculated cost to complete material cost for the project.  */  
   TotCtcMtlCost:number,
      /**  Total calculated cost to complete material burden cost for the project.  */  
   TotCtcMtlBurCost:number,
      /**  Total quoted labour hours for the project  */  
   TotQuotLbrHrs:number,
      /**  Total quoted burden hours for the project  */  
   TotQuotBurHrs:number,
      /**  Total quoted labour cost for the project. This will be both production and setup.  */  
   TotQuotLbrCost:number,
      /**  Total quoted subcontract cost for the project.  */  
   TotQuotSubContCost:number,
      /**  Total quoted material cost for the project.  */  
   TotQuotMtlCost:number,
      /**  Total quoted material burden cost for the project.  */  
   TotQuotMtlBurCost:number,
      /**  Total estimated burden costs for the project  */  
   TotEstBurCost:number,
      /**  Total quoted burden cost for the project. This will be both production and setup.  */  
   TotQuotBurCost:number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  */  
   RevenueRecAutoToDate:number,
      /**  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   MaterialRecAutoCstTodate:number,
      /**  The labor costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   LaborRecAutoCstTodate:number,
      /**  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   BurdenRecAutoCstTodate:number,
      /**  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  */  
   MtlBurdenRecAutoCstTodate:number,
      /**  Total budget labour hours for the Project  */  
   BudTotLbrHours:number,
      /**  Total budget burden hours for the Project  */  
   BudTotBurHrs:number,
      /**  Total budget labour cost for the Project. This is production and setup combined.  */  
   BudTotLbrCost:number,
      /**  Total budget burden cost for the Project. This is production and setup combined.  */  
   BudTotBurCost:number,
      /**  Total budget subcontract costs for the Project  */  
   BudTotSubCost:number,
      /**  Total budget material costs for the Project  */  
   BudTotMtlCost:number,
      /**  Total budget material burden costs for the Project phase.  */  
   BudTotMtlBurCost:number,
      /**  Total estimated material burden costs for the Project phase  */  
   TotEstMtlBurCost:number,
      /**  The subcontract costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  */  
   SubConRecAutoCstTodate:number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  */  
   RevenueRecManToDate:number,
      /**  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   MaterialRecManCstTodate:number,
      /**  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   LaborRecManCstTodate:number,
      /**  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  */  
   BurdenRecManCstTodate:number,
      /**  The subcontract costs posted to cost of sales to date. This is cost that has been manually recognised using this process  */  
   SubConRecManCstTodate:number,
      /**  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   MtlBurdenRecManCstTodate:number,
      /**  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  */  
   MaterialCostOfSales:number,
      /**  The labor costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  */  
   LaborCostOfSales:number,
      /**  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  */  
   BurdenCostOfSales:number,
      /**  The subcontract costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActSubContractCost  */  
   SubConCostOfSales:number,
      /**  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  */  
   MtlBurdenCostOfSales:number,
      /**  Other Direct Cost Quoted  */  
   TotQuotODCCost:number,
      /**  Other Direct Cost Estimated  */  
   TotEstODCCost:number,
      /**  ODC Actual  */  
   TotActODCCost:number,
      /**  Other direct cost manual CTC  */  
   ManEstCTCODCCost:number,
      /**  Other direct Cost total CTC  */  
   TotCTCODCCost:number,
      /**  Other direct Cost Budget Total  */  
   BudTotODCCost:number,
      /**  Other Direct cost Recognition to Date  */  
   ODCRecAutoCstToDate:number,
      /**  Other Direct Cost Manual Recognition to Date  */  
   ODCRecManCstTodate:number,
      /**  Estimated other direct cost  */  
   EstODCCost:number,
      /**  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  */  
   BdnRecSeqPosted:number,
      /**  Number of Recalculation of burden amounts created by Revenue Recognition process  */  
   BdnRecSeqLastAdded:number,
      /**  Sum of all Actual Burden Charges posted by today  */  
   BdnRevenueAutoToday:number,
      /**  AsOfDate  */  
   AsOfDate:string,
      /**  BuildAnalysis  */  
   BuildAnalysis:boolean,
      /**  LbrPur  */  
   LbrPur:number,
      /**  BurPur  */  
   BurPur:number,
      /**  MtlPur  */  
   MtlPur:number,
      /**  SubPur  */  
   SubPur:number,
      /**  MtlBurPur  */  
   MtlBurPur:number,
      /**  ODCPur  */  
   ODCPur:number,
      /**  LaborLbrCstToDate  */  
   LaborLbrCstToDate:number,
      /**  BurdenLbrCstToDate  */  
   BurdenLbrCstToDate:number,
      /**  ActMtlNonJobCost  */  
   ActMtlNonJobCost:number,
      /**  RecManPosted  */  
   RecManPosted:number,
      /**  LbrManPosted  */  
   LbrManPosted:number,
      /**  BurManPosted  */  
   BurManPosted:number,
      /**  MtlManPosted  */  
   MtlManPosted:number,
      /**  SubCManPosted  */  
   SubCManPosted:number,
      /**  MtlBurManPosted  */  
   MtlBurManPosted:number,
      /**  ODCManPosted  */  
   ODCManPosted:number,
      /**  Reverse  */  
   Reverse:string,
      /**  NextTmpInvcNum  */  
   NextTmpInvcNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Percentage of Completion  */  
   PercentageOfCompletion:number,
      /**  Labor Cost To Be Recognized  */  
   ToBeRecognizedLbrCost:number,
      /**  Burden Cost To Be Recognized  */  
   ToBeRecognizedBurCost:number,
      /**  Material Cost To Be Recognized  */  
   ToBeRecognizedMtlCost:number,
      /**  Subcontract Cost To Be Recognized  */  
   ToBeRecognizedSubCost:number,
      /**  Material Burden Cost To Be Recognized  */  
   ToBeRecognizedMtlBurCost:number,
      /**  ODC Cost To Be Recognized  */  
   ToBeRecognizedODCCost:number,
      /**  Revenue To Be Recognized  */  
   ToBeRecognizedRevenue:number,
      /**  BillingToDate  */  
   BillingToDate:number,
      /**  RecogToDtBilling  */  
   RecogToDtBilling:number,
      /**  TotProjRev  */  
   TotProjRev:number,
      /**  RecogToDtLbk  */  
   RecogToDtLbk:number,
      /**  RecogToDtManual  */  
   RecogToDtManual:number,
      /**  RetentionDt  */  
   RetentionDt:number,
   CurrencyCode:string,
   DocBudTotBurCost:number,
   DocBudTotLbrCost:number,
   DocBudTotMtlBurCost:number,
   DocBudTotMtlCost:number,
   DocBudTotODCCost:number,
   DocBudTotSubCost:number,
   DocEstBurdenCost:number,
   DocEstLaborCost:number,
   DocEstMtlBurdenCost:number,
   DocEstMtlCost:number,
   DocEstODCCost:number,
   DocEstSubcontractCost:number,
   DocEstTotalCost:number,
   DocGTActualCost:number,
   DocGTBudgetCost:number,
   DocGTCalculatedCost:number,
   DocGTEstimatedCost:number,
   DocGTManualCost:number,
   DocGTQuotedCost:number,
   DocProjectedTotalBurCost:number,
   DocProjectedTotalCost:number,
   DocProjectedTotalLbrCost:number,
   DocProjectedTotalMtlBurCost:number,
   DocProjectedTotalMtlCost:number,
   DocProjectedTotalODCCost:number,
   DocProjectedTotalSubContCost:number,
   DocTotActMtlBurCost:number,
   DocTotActMtlCost:number,
   DocTotActODCCost:number,
   DocTotActSubContCost:number,
   DocTotCtcBurCost:number,
   DocTotCtcLbrCost:number,
   DocTotCtcMtlBurCost:number,
   DocTotCtcMtlCost:number,
   DocTotCTCODCCost:number,
   DocTotCtcSubConCost:number,
   DocTotEstBurCost:number,
   DocTotEstLbrCost:number,
   DocTotEstMtlBurCost:number,
   DocTotEstMtlCost:number,
   DocTotEstODCCost:number,
   DocTotEstSubContCost:number,
   DocTotQuotBurCost:number,
   DocTotQuotLbrCost:number,
   DocTotQuotMtlBurCost:number,
   DocTotQuotMtlCost:number,
   DocTotQuotODCCost:number,
   DocTotQuotSubContCost:number,
      /**  This is a calculated field: the sum of the other Project.Est*Cost fields.  It is not stored in the database.  */  
   EstTotalCost:number,
   GTActualCost:number,
   GTBudgetCost:number,
   GTCalculatedCost:number,
   GTEstimatedCost:number,
   GTManualCost:number,
   GTQuotedCost:number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   ProjectedTotalBurCost:number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   ProjectedTotalCost:number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   ProjectedTotalLbrCost:number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   ProjectedTotalMtlBurCost:number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   ProjectedTotalMtlCost:number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   ProjectedTotalODCCost:number,
      /**  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  */  
   ProjectedTotalSubContCost:number,
      /**  Recognized to Date Billing  */  
   ReconToDtBilling:number,
   Rpt1BudTotBurCost:number,
   Rpt1BudTotLbrCost:number,
   Rpt1BudTotMtlBurCost:number,
   Rpt1BudTotMtlCost:number,
   Rpt1BudTotODCCost:number,
   Rpt1BudTotSubCost:number,
   Rpt1EstBurdenCost:number,
   Rpt1EstLaborCost:number,
   Rpt1EstMtlBurdenCost:number,
   Rpt1EstMtlCost:number,
   Rpt1EstODCCost:number,
   Rpt1EstSubcontractCost:number,
   Rpt1EstTotalCost:number,
   Rpt1GTActualCost:number,
   Rpt1GTBudgetCost:number,
   Rpt1GTCalculatedCost:number,
   Rpt1GTEstimatedCost:number,
   Rpt1GTManualCost:number,
   Rpt1GTQuotedCost:number,
   Rpt1ManEstCtcBurCost:number,
   Rpt1ManEstCtcLbrCost:number,
   Rpt1ManEstCtcMtlBurCost:number,
   Rpt1ManEstCtcMtlCost:number,
   Rpt1ManEstCTCODCCost:number,
   Rpt1ManEstCtcSubConCost:number,
   Rpt1ProjectedTotalBurCost:number,
   Rpt1ProjectedTotalCost:number,
   Rpt1ProjectedTotalLbrCost:number,
   Rpt1ProjectedTotalMtlBurCost:number,
   Rpt1ProjectedTotalMtlCost:number,
   Rpt1ProjectedTotalODCCost:number,
   Rpt1ProjectedTotalSubContCost:number,
   Rpt1TotActBurCost:number,
   Rpt1TotActLbrCost:number,
   Rpt1TotActMtlBurCost:number,
   Rpt1TotActMtlCost:number,
   Rpt1TotActODCCost:number,
   Rpt1TotActSubContCost:number,
   Rpt1TotCtcBurCost:number,
   Rpt1TotCtcLbrCost:number,
   Rpt1TotCtcMtlBurCost:number,
   Rpt1TotCtcMtlCost:number,
   Rpt1TotCTCODCCost:number,
   Rpt1TotCtcSubConCost:number,
   Rpt1TotEstBurCost:number,
   Rpt1TotEstLbrCost:number,
   Rpt1TotEstMtlBurCost:number,
   Rpt1TotEstMtlCost:number,
   Rpt1TotEstODCCost:number,
   Rpt1TotEstSubContCost:number,
   Rpt1TotQuotBurCost:number,
   Rpt1TotQuotLbrCost:number,
   Rpt1TotQuotMtlBurCost:number,
   Rpt1TotQuotMtlCost:number,
   Rpt1TotQuotODCCost:number,
   Rpt1TotQuotSubContCost:number,
   Rpt2BudTotBurCost:number,
   Rpt2BudTotLbrCost:number,
   Rpt2BudTotMtlBurCost:number,
   Rpt2BudTotMtlCost:number,
   Rpt2BudTotODCCost:number,
   Rpt2BudTotSubCost:number,
   Rpt2EstBurdenCost:number,
   Rpt2EstLaborCost:number,
   Rpt2EstMtlBurdenCost:number,
   Rpt2EstMtlCost:number,
   Rpt2EstODCCost:number,
   Rpt2EstSubcontractCost:number,
   Rpt2EstTotalCost:number,
   Rpt2GTActualCost:number,
   Rpt2GTBudgetCost:number,
   Rpt2GTCalculatedCost:number,
   Rpt2GTEstimatedCost:number,
   Rpt2GTManualCost:number,
   Rpt2GTQuotedCost:number,
   Rpt2ManEstCtcBurCost:number,
   Rpt2ManEstCtcLbrCost:number,
   Rpt2ManEstCtcMtlBurCost:number,
   Rpt2ManEstCtcMtlCost:number,
   Rpt2ManEstCTCODCCost:number,
   Rpt2ManEstCtcSubConCost:number,
   Rpt2ProjectedTotalBurCost:number,
   Rpt2ProjectedTotalCost:number,
   Rpt2ProjectedTotalLbrCost:number,
   Rpt2ProjectedTotalMtlBurCost:number,
   Rpt2ProjectedTotalMtlCost:number,
   Rpt2ProjectedTotalODCCost:number,
   Rpt2ProjectedTotalSubContCost:number,
   Rpt2TotActBurCost:number,
   Rpt2TotActLbrCost:number,
   Rpt2TotActMtlBurCost:number,
   Rpt2TotActMtlCost:number,
   Rpt2TotActODCCost:number,
   Rpt2TotActSubContCost:number,
   Rpt2TotCtcBurCost:number,
   Rpt2TotCtcLbrCost:number,
   Rpt2TotCtcMtlBurCost:number,
   Rpt2TotCtcMtlCost:number,
   Rpt2TotCTCODCCost:number,
   Rpt2TotCtcSubConCost:number,
   Rpt2TotEstBurCost:number,
   Rpt2TotEstLbrCost:number,
   Rpt2TotEstMtlBurCost:number,
   Rpt2TotEstMtlCost:number,
   Rpt2TotEstODCCost:number,
   Rpt2TotEstSubContCost:number,
   Rpt2TotQuotBurCost:number,
   Rpt2TotQuotLbrCost:number,
   Rpt2TotQuotMtlBurCost:number,
   Rpt2TotQuotMtlCost:number,
   Rpt2TotQuotODCCost:number,
   Rpt2TotQuotSubContCost:number,
   Rpt3BudTotBurCost:number,
   Rpt3BudTotLbrCost:number,
   Rpt3BudTotMtlBurCost:number,
   Rpt3BudTotMtlCost:number,
   Rpt3BudTotODCCost:number,
   Rpt3BudTotSubCost:number,
   Rpt3EstBurdenCost:number,
   Rpt3EstLaborCost:number,
   Rpt3EstMtlBurdenCost:number,
   Rpt3EstMtlCost:number,
   Rpt3EstODCCost:number,
   Rpt3EstSubcontractCost:number,
   Rpt3EstTotalCost:number,
   Rpt3GTActualCost:number,
   Rpt3GTBudgetCost:number,
   Rpt3GTCalculatedCost:number,
   Rpt3GTEstimatedCost:number,
   Rpt3GTManualCost:number,
   Rpt3GTQuotedCost:number,
   Rpt3ManEstCtcBurCost:number,
   Rpt3ManEstCtcLbrCost:number,
   Rpt3ManEstCtcMtlBurCost:number,
   Rpt3ManEstCtcMtlCost:number,
   Rpt3ManEstCTCODCCost:number,
   Rpt3ManEstCtcSubConCost:number,
   Rpt3ProjectedTotalBurCost:number,
   Rpt3ProjectedTotalCost:number,
   Rpt3ProjectedTotalLbrCost:number,
   Rpt3ProjectedTotalMtlBurCost:number,
   Rpt3ProjectedTotalMtlCost:number,
   Rpt3ProjectedTotalODCCost:number,
   Rpt3ProjectedTotalSubContCost:number,
   Rpt3TotActBurCost:number,
   Rpt3TotActLbrCost:number,
   Rpt3TotActMtlBurCost:number,
   Rpt3TotActMtlCost:number,
   Rpt3TotActODCCost:number,
   Rpt3TotActSubContCost:number,
   Rpt3TotCtcBurCost:number,
   Rpt3TotCtcLbrCost:number,
   Rpt3TotCtcMtlBurCost:number,
   Rpt3TotCtcMtlCost:number,
   Rpt3TotCTCODCCost:number,
   Rpt3TotCtcSubConCost:number,
   Rpt3TotEstBurCost:number,
   Rpt3TotEstLbrCost:number,
   Rpt3TotEstMtlBurCost:number,
   Rpt3TotEstMtlCost:number,
   Rpt3TotEstODCCost:number,
   Rpt3TotEstSubContCost:number,
   Rpt3TotQuotBurCost:number,
   Rpt3TotQuotLbrCost:number,
   Rpt3TotQuotMtlBurCost:number,
   Rpt3TotQuotMtlCost:number,
   Rpt3TotQuotODCCost:number,
   Rpt3TotQuotSubContCost:number,
   DocManEstCtcBurCost:number,
   DocManEstCtcLbrCost:number,
   DocManEstCtcMtlBurCost:number,
   DocManEstCtcMtlCost:number,
   DocManEstCTCODCCost:number,
   DocManEstCtcSubConCost:number,
   DocTotActBurCost:number,
   DocTotActLbrCost:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtProjMultiTableset{
   ProjMulti:Erp_Tablesets_ProjMultiRow[],
   ProjectCst:Erp_Tablesets_ProjectCstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param projectID
   */  
export interface GetByID_input{
   projectID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ProjMultiTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ProjMultiTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ProjMultiTableset[],
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
   returnObj:Erp_Tablesets_ProjMultiListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewProjMulti_input{
   ds:Erp_Tablesets_ProjMultiTableset[],
}

export interface GetNewProjMulti_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProjMultiTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewProjectCst_input{
   ds:Erp_Tablesets_ProjMultiTableset[],
}

export interface GetNewProjectCst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProjMultiTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetRowsByFilter_input{
   ds:Erp_Tablesets_ProjFilterTableset[],
}

export interface GetRowsByFilter_output{
   returnObj:Erp_Tablesets_ProjMultiTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProjFilterTableset,
}
}

   /** Required : 
      @param whereClauseProjMulti
      @param whereClauseProjectCst
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseProjMulti:string,
   whereClauseProjectCst:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ProjMultiTableset[],
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
      @param projectIDs
   */  
export interface RefreshAll_input{
   projectIDs:string,
}

export interface RefreshAll_output{
   returnObj:Erp_Tablesets_ProjMultiTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtProjMultiTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtProjMultiTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ProjMultiTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProjMultiTableset,
}
}

