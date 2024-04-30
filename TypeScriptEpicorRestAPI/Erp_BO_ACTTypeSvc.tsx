import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ACTTypeSvc
// Description: ActType Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/$metadata", {
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
   Description: Get ACTTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTTypes
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeRow
   */  
export function get_ACTTypes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ACTTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ACTTypes(requestBody:Erp_Tablesets_ACTTypeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes", {
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
   Summary: Calls GetByID to retrieve the ACTType item
   Description: Calls GetByID to retrieve the ACTType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ACTTypeRow
   */  
export function get_ACTTypes_Company_ACTTypeUID(Company:string, ACTTypeUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ACTTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")", {
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
         resolve(data as Erp_Tablesets_ACTTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ACTType for the service
   Description: Calls UpdateExt to update ACTType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ACTTypes_Company_ACTTypeUID(Company:string, ACTTypeUID:string, requestBody:Erp_Tablesets_ACTTypeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")", {
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
   Summary: Call UpdateExt to delete ACTType item
   Description: Call UpdateExt to delete ACTType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ACTTypes_Company_ACTTypeUID(Company:string, ACTTypeUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")", {
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
   Description: Get ACTRevisions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ACTRevisions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTRevisionRow
   */  
export function get_ACTTypes_Company_ACTTypeUID_ACTRevisions(Company:string, ACTTypeUID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTRevisionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")/ACTRevisions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTRevisionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ACTRevision item
   Description: Calls GetByID to retrieve the ACTRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTRevision1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ACTRevisionRow
   */  
export function get_ACTTypes_Company_ACTTypeUID_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ACTRevisionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTTypes(" + Company + "," + ACTTypeUID + ")/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")", {
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
         resolve(data as Erp_Tablesets_ACTRevisionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ACTRevisions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTRevisions
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTRevisionRow
   */  
export function get_ACTRevisions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTRevisionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTRevisionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTRevisions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTRevisionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ACTRevisionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ACTRevisions(requestBody:Erp_Tablesets_ACTRevisionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions", {
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
   Summary: Calls GetByID to retrieve the ACTRevision item
   Description: Calls GetByID to retrieve the ACTRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTRevision
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ACTRevisionRow
   */  
export function get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ACTRevisionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")", {
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
         resolve(data as Erp_Tablesets_ACTRevisionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ACTRevision for the service
   Description: Calls UpdateExt to update ACTRevision. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTRevision
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTRevisionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, requestBody:Erp_Tablesets_ACTRevisionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")", {
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
   Summary: Call UpdateExt to delete ACTRevision item
   Description: Call UpdateExt to delete ACTRevision item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTRevision
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")", {
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
   Description: Get ABTDocLines items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTDocLines1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTDocLineRow
   */  
export function get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ABTDocLines(Company:string, ACTTypeUID:string, ACTRevisionUID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTDocLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ABTDocLines", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTDocLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ABTDocLine item
   Description: Calls GetByID to retrieve the ABTDocLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTDocLine1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTDocLineRow
   */  
export function get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTDocLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTDocLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ACTBooks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ACTBooks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTBookRow
   */  
export function get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ACTBooks(Company:string, ACTTypeUID:string, ACTRevisionUID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTBookRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ACTBooks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTBookRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ACTBook item
   Description: Calls GetByID to retrieve the ACTBook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTBook1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ACTBookRow
   */  
export function get_ACTRevisions_Company_ACTTypeUID_ACTRevisionUID_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ACTBookRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTRevisions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + ")/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")", {
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
         resolve(data as Erp_Tablesets_ACTBookRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ABTDocLines items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTDocLines
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTDocLineRow
   */  
export function get_ABTDocLines(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTDocLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTDocLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTDocLines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTDocLineRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ABTDocLineRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTDocLines(requestBody:Erp_Tablesets_ABTDocLineRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines", {
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
   Summary: Calls GetByID to retrieve the ABTDocLine item
   Description: Calls GetByID to retrieve the ABTDocLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTDocLine
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTDocLineRow
   */  
export function get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTDocLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTDocLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ABTDocLine for the service
   Description: Calls UpdateExt to update ABTDocLine. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTDocLine
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTDocLineRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, requestBody:Erp_Tablesets_ABTDocLineRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")", {
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
   Summary: Call UpdateExt to delete ABTDocLine item
   Description: Call UpdateExt to delete ABTDocLine item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTDocLine
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")", {
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
   Description: Get ABTAmounts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTAmounts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTAmountRow
   */  
export function get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmounts(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTAmountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTAmounts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTAmountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ABTAmount item
   Description: Calls GetByID to retrieve the ABTAmount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTAmount1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTAmountUID Desc: ABTAmountUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTAmountRow
   */  
export function get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTAmountUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTAmountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTAmountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ABTPostEntities items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTPostEntities1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostEntityRow
   */  
export function get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntities(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTPostEntities", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ABTPostEntity item
   Description: Calls GetByID to retrieve the ABTPostEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostEntity1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTPostEntityRow
   */  
export function get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTPostEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTPostEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ABTQueries items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTQueries1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQueryRow
   */  
export function get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueries(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTQueries", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ABTQuery item
   Description: Calls GetByID to retrieve the ABTQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQuery1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTQueryRow
   */  
export function get_ABTDocLines_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLines(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + ")/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ABTAmounts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTAmounts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTAmountRow
   */  
export function get_ABTAmounts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTAmountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTAmountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTAmounts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTAmountRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ABTAmountRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTAmounts(requestBody:Erp_Tablesets_ABTAmountRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts", {
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
   Summary: Calls GetByID to retrieve the ABTAmount item
   Description: Calls GetByID to retrieve the ABTAmount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTAmount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTAmountUID Desc: ABTAmountUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTAmountRow
   */  
export function get_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTAmountUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTAmountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTAmountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ABTAmount for the service
   Description: Calls UpdateExt to update ABTAmount. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTAmount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTAmountUID Desc: ABTAmountUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTAmountRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTAmountUID:string, requestBody:Erp_Tablesets_ABTAmountRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")", {
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
   Summary: Call UpdateExt to delete ABTAmount item
   Description: Call UpdateExt to delete ABTAmount item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTAmount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTAmountUID Desc: ABTAmountUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ABTAmounts_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTAmountUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTAmountUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTAmounts(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTAmountUID + ")", {
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
   Description: Get ABTPostEntities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTPostEntities
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostEntityRow
   */  
export function get_ABTPostEntities(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTPostEntities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTPostEntityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ABTPostEntityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTPostEntities(requestBody:Erp_Tablesets_ABTPostEntityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities", {
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
   Summary: Calls GetByID to retrieve the ABTPostEntity item
   Description: Calls GetByID to retrieve the ABTPostEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTPostEntityRow
   */  
export function get_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTPostEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTPostEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ABTPostEntity for the service
   Description: Calls UpdateExt to update ABTPostEntity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTPostEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTPostEntityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, requestBody:Erp_Tablesets_ABTPostEntityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")", {
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
   Summary: Call UpdateExt to delete ABTPostEntity item
   Description: Call UpdateExt to delete ABTPostEntity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTPostEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")", {
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
   Description: Get ABTPostCodes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTPostCodes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostCodeRow
   */  
export function get_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodes(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")/ABTPostCodes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ABTPostCode item
   Description: Calls GetByID to retrieve the ABTPostCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostCode1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param ABTPostCodeUID Desc: ABTPostCodeUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTPostCodeRow
   */  
export function get_ABTPostEntities_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, ABTPostCodeUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTPostCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostEntities(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + ")/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTPostCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ABTPostCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTPostCodes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTPostCodeRow
   */  
export function get_ABTPostCodes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTPostCodes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTPostCodeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ABTPostCodeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTPostCodes(requestBody:Erp_Tablesets_ABTPostCodeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes", {
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
   Summary: Calls GetByID to retrieve the ABTPostCode item
   Description: Calls GetByID to retrieve the ABTPostCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTPostCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param ABTPostCodeUID Desc: ABTPostCodeUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTPostCodeRow
   */  
export function get_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, ABTPostCodeUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTPostCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTPostCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ABTPostCode for the service
   Description: Calls UpdateExt to update ABTPostCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTPostCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param ABTPostCodeUID Desc: ABTPostCodeUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTPostCodeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, ABTPostCodeUID:string, requestBody:Erp_Tablesets_ABTPostCodeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")", {
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
   Summary: Call UpdateExt to delete ABTPostCode item
   Description: Call UpdateExt to delete ABTPostCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTPostCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTPostEntityUID Desc: ABTPostEntityUID   Required: True
      @param ABTPostCodeUID Desc: ABTPostCodeUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ABTPostCodes_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTPostEntityUID_ABTPostCodeUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTPostEntityUID:string, ABTPostCodeUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodes(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTPostEntityUID + "," + ABTPostCodeUID + ")", {
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
   Description: Get ABTQueries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTQueries
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQueryRow
   */  
export function get_ABTQueries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTQueries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTQueryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ABTQueryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTQueries(requestBody:Erp_Tablesets_ABTQueryRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries", {
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
   Summary: Calls GetByID to retrieve the ABTQuery item
   Description: Calls GetByID to retrieve the ABTQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQuery
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTQueryRow
   */  
export function get_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ABTQuery for the service
   Description: Calls UpdateExt to update ABTQuery. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTQuery
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTQueryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, requestBody:Erp_Tablesets_ABTQueryRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")", {
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
   Summary: Call UpdateExt to delete ABTQuery item
   Description: Call UpdateExt to delete ABTQuery item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTQuery
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")", {
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
   Description: Get ABTQParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ABTQParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQParamRow
   */  
export function get_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_ABTQParams(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")/ABTQParams", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ABTQParam item
   Description: Calls GetByID to retrieve the ABTQParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param BAQParamLinkUID Desc: BAQParamLinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTQParamRow
   */  
export function get_ABTQueries_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, BAQParamLinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTQParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQueries(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + ")/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTQParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ABTQParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ABTQParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ABTQParamRow
   */  
export function get_ABTQParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ABTQParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ABTQParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ABTQParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTQParams(requestBody:Erp_Tablesets_ABTQParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams", {
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
   Summary: Calls GetByID to retrieve the ABTQParam item
   Description: Calls GetByID to retrieve the ABTQParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ABTQParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param BAQParamLinkUID Desc: BAQParamLinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ABTQParamRow
   */  
export function get_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, BAQParamLinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ABTQParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")", {
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
         resolve(data as Erp_Tablesets_ABTQParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ABTQParam for the service
   Description: Calls UpdateExt to update ABTQParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ABTQParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param BAQParamLinkUID Desc: BAQParamLinkUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ABTQParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, BAQParamLinkUID:string, requestBody:Erp_Tablesets_ABTQParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")", {
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
   Summary: Call UpdateExt to delete ABTQParam item
   Description: Call UpdateExt to delete ABTQParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ABTQParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param ABTDocLineUID Desc: ABTDocLineUID   Required: True
      @param ABTQueryUID Desc: ABTQueryUID   Required: True
      @param BAQParamLinkUID Desc: BAQParamLinkUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ABTQParams_Company_ACTTypeUID_ACTRevisionUID_ABTDocLineUID_ABTQueryUID_BAQParamLinkUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, ABTDocLineUID:string, ABTQueryUID:string, BAQParamLinkUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTQParams(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + ABTDocLineUID + "," + ABTQueryUID + "," + BAQParamLinkUID + ")", {
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
   Description: Get ACTBooks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTBooks
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTBookRow
   */  
export function get_ACTBooks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTBookRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTBookRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTBooks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTBookRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ACTBookRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ACTBooks(requestBody:Erp_Tablesets_ACTBookRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks", {
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
   Summary: Calls GetByID to retrieve the ACTBook item
   Description: Calls GetByID to retrieve the ACTBook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTBook
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ACTBookRow
   */  
export function get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ACTBookRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")", {
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
         resolve(data as Erp_Tablesets_ACTBookRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ACTBook for the service
   Description: Calls UpdateExt to update ACTBook. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTBook
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTBookRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, requestBody:Erp_Tablesets_ACTBookRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")", {
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
   Summary: Call UpdateExt to delete ACTBook item
   Description: Call UpdateExt to delete ACTBook item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTBook
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")", {
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
   Description: Get BookingRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BookingRules1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookingRuleRow
   */  
export function get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookingRules(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookingRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookingRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookingRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BookingRule item
   Description: Calls GetByID to retrieve the BookingRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookingRule1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BookingRuleRow
   */  
export function get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BookingRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")", {
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
         resolve(data as Erp_Tablesets_BookingRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BRFunctions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BRFunctions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFunctionRow
   */  
export function get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BRFunctions(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFunctionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BRFunctions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFunctionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BRFunction item
   Description: Calls GetByID to retrieve the BRFunction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFunction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FunctionUID Desc: FunctionUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BRFunctionRow
   */  
export function get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, FunctionUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BRFunctionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")", {
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
         resolve(data as Erp_Tablesets_BRFunctionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BookVars items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BookVars1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookVarRow
   */  
export function get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVars(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookVars", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BookVar item
   Description: Calls GetByID to retrieve the BookVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookVar1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BookVarUID Desc: BookVarUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BookVarRow
   */  
export function get_ACTBooks_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, BookVarUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BookVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ACTBooks(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + ")/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")", {
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
         resolve(data as Erp_Tablesets_BookVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BookingRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BookingRules
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookingRuleRow
   */  
export function get_BookingRules(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookingRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookingRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BookingRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BookingRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BookingRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookingRules(requestBody:Erp_Tablesets_BookingRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules", {
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
   Summary: Calls GetByID to retrieve the BookingRule item
   Description: Calls GetByID to retrieve the BookingRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookingRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BookingRuleRow
   */  
export function get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BookingRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")", {
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
         resolve(data as Erp_Tablesets_BookingRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BookingRule for the service
   Description: Calls UpdateExt to update BookingRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BookingRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BookingRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, requestBody:Erp_Tablesets_BookingRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")", {
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
   Summary: Call UpdateExt to delete BookingRule item
   Description: Call UpdateExt to delete BookingRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BookingRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")", {
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
   Description: Get BookValRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BookValRules1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookValRuleRow
   */  
export function get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BookValRules(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookValRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BookValRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookValRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BookValRule item
   Description: Calls GetByID to retrieve the BookValRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookValRule1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param VRuleUID Desc: VRuleUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BookValRuleRow
   */  
export function get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, VRuleUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BookValRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")", {
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
         resolve(data as Erp_Tablesets_BookValRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BROperations items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BROperations1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationRow
   */  
export function get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperations(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperations", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BROperation item
   Description: Calls GetByID to retrieve the BROperation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperation1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BROperationRow
   */  
export function get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BROperationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
         resolve(data as Erp_Tablesets_BROperationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BROperationCustoms items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BROperationCustoms1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationCustomRow
   */  
export function get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperationCustoms(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationCustomRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperationCustoms", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationCustomRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BROperationCustom item
   Description: Calls GetByID to retrieve the BROperationCustom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperationCustom1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BROperationCustomRow
   */  
export function get_BookingRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BROperationCustomRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + ")/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
         resolve(data as Erp_Tablesets_BROperationCustomRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BookValRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BookValRules
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookValRuleRow
   */  
export function get_BookValRules(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookValRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookValRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BookValRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BookValRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BookValRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookValRules(requestBody:Erp_Tablesets_BookValRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules", {
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
   Summary: Calls GetByID to retrieve the BookValRule item
   Description: Calls GetByID to retrieve the BookValRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookValRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param VRuleUID Desc: VRuleUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BookValRuleRow
   */  
export function get_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, VRuleUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BookValRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")", {
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
         resolve(data as Erp_Tablesets_BookValRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BookValRule for the service
   Description: Calls UpdateExt to update BookValRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BookValRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param VRuleUID Desc: VRuleUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BookValRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, VRuleUID:string, requestBody:Erp_Tablesets_BookValRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")", {
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
   Summary: Call UpdateExt to delete BookValRule item
   Description: Call UpdateExt to delete BookValRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BookValRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param VRuleUID Desc: VRuleUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BookValRules_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_VRuleUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, VRuleUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookValRules(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + VRuleUID + ")", {
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
   Description: Get BROperations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BROperations
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationRow
   */  
export function get_BROperations(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BROperations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BROperationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BROperationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROperations(requestBody:Erp_Tablesets_BROperationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations", {
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
   Summary: Calls GetByID to retrieve the BROperation item
   Description: Calls GetByID to retrieve the BROperation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BROperationRow
   */  
export function get_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BROperationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
         resolve(data as Erp_Tablesets_BROperationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BROperation for the service
   Description: Calls UpdateExt to update BROperation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BROperation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BROperationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, requestBody:Erp_Tablesets_BROperationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
   Summary: Call UpdateExt to delete BROperation item
   Description: Call UpdateExt to delete BROperation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BROperation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BROperations_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
   Description: Get BROperationCustoms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BROperationCustoms
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BROperationCustomRow
   */  
export function get_BROperationCustoms(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationCustomRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationCustomRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BROperationCustoms
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BROperationCustomRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BROperationCustomRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROperationCustoms(requestBody:Erp_Tablesets_BROperationCustomRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms", {
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
   Summary: Calls GetByID to retrieve the BROperationCustom item
   Description: Calls GetByID to retrieve the BROperationCustom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BROperationCustom
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BROperationCustomRow
   */  
export function get_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BROperationCustomRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
         resolve(data as Erp_Tablesets_BROperationCustomRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BROperationCustom for the service
   Description: Calls UpdateExt to update BROperationCustom. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BROperationCustom
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BROperationCustomRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, requestBody:Erp_Tablesets_BROperationCustomRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
   Summary: Call UpdateExt to delete BROperationCustom item
   Description: Call UpdateExt to delete BROperationCustom item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BROperationCustom
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param RuleUID Desc: RuleUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BROperationCustoms_Company_ACTTypeUID_ACTRevisionUID_BookID_RuleUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, RuleUID:string, OperationUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustoms(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + RuleUID + "," + OperationUID + ")", {
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
   Description: Get BRFunctions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BRFunctions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFunctionRow
   */  
export function get_BRFunctions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFunctionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFunctionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BRFunctions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BRFunctionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BRFunctionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFunctions(requestBody:Erp_Tablesets_BRFunctionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions", {
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
   Summary: Calls GetByID to retrieve the BRFunction item
   Description: Calls GetByID to retrieve the BRFunction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFunction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FunctionUID Desc: FunctionUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BRFunctionRow
   */  
export function get_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, FunctionUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BRFunctionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")", {
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
         resolve(data as Erp_Tablesets_BRFunctionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BRFunction for the service
   Description: Calls UpdateExt to update BRFunction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BRFunction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FunctionUID Desc: FunctionUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BRFunctionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, FunctionUID:string, requestBody:Erp_Tablesets_BRFunctionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")", {
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
   Summary: Call UpdateExt to delete BRFunction item
   Description: Call UpdateExt to delete BRFunction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BRFunction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FunctionUID Desc: FunctionUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BRFunctions_Company_ACTTypeUID_ACTRevisionUID_BookID_FunctionUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, FunctionUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctions(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + FunctionUID + ")", {
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
   Description: Get BookVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BookVars
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BookVarRow
   */  
export function get_BookVars(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BookVars
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BookVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BookVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookVars(requestBody:Erp_Tablesets_BookVarRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars", {
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
   Summary: Calls GetByID to retrieve the BookVar item
   Description: Calls GetByID to retrieve the BookVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BookVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BookVarUID Desc: BookVarUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BookVarRow
   */  
export function get_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, BookVarUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BookVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")", {
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
         resolve(data as Erp_Tablesets_BookVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BookVar for the service
   Description: Calls UpdateExt to update BookVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BookVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BookVarUID Desc: BookVarUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BookVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, BookVarUID:string, requestBody:Erp_Tablesets_BookVarRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")", {
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
   Summary: Call UpdateExt to delete BookVar item
   Description: Call UpdateExt to delete BookVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BookVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BookVarUID Desc: BookVarUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BookVars_Company_ACTTypeUID_ACTRevisionUID_BookID_BookVarUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, BookID:string, BookVarUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVars(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + BookID + "," + BookVarUID + ")", {
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
   Description: Get BRFuncArgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BRFuncArgs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFuncArgsRow
   */  
export function get_BRFuncArgs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncArgsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncArgsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BRFuncArgs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BRFuncArgsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BRFuncArgsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFuncArgs(requestBody:Erp_Tablesets_BRFuncArgsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs", {
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
   Summary: Calls GetByID to retrieve the BRFuncArg item
   Description: Calls GetByID to retrieve the BRFuncArg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFuncArg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param FunctionUID Desc: FunctionUID   Required: True
      @param ArgumentUID Desc: ArgumentUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BRFuncArgsRow
   */  
export function get_BRFuncArgs_Company_ACTTypeUID_ACTRevisionUID_FunctionUID_ArgumentUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, FunctionUID:string, ArgumentUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BRFuncArgsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FunctionUID + "," + ArgumentUID + ")", {
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
         resolve(data as Erp_Tablesets_BRFuncArgsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BRFuncArg for the service
   Description: Calls UpdateExt to update BRFuncArg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BRFuncArg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param FunctionUID Desc: FunctionUID   Required: True
      @param ArgumentUID Desc: ArgumentUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BRFuncArgsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BRFuncArgs_Company_ACTTypeUID_ACTRevisionUID_FunctionUID_ArgumentUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, FunctionUID:string, ArgumentUID:string, requestBody:Erp_Tablesets_BRFuncArgsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FunctionUID + "," + ArgumentUID + ")", {
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
   Summary: Call UpdateExt to delete BRFuncArg item
   Description: Call UpdateExt to delete BRFuncArg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BRFuncArg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param FunctionUID Desc: FunctionUID   Required: True
      @param ArgumentUID Desc: ArgumentUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BRFuncArgs_Company_ACTTypeUID_ACTRevisionUID_FunctionUID_ArgumentUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, FunctionUID:string, ArgumentUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncArgs(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FunctionUID + "," + ArgumentUID + ")", {
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
   Description: Get BRFuncOperations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BRFuncOperations
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BRFuncOperationRow
   */  
export function get_BRFuncOperations(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncOperationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncOperationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BRFuncOperations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BRFuncOperationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BRFuncOperationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFuncOperations(requestBody:Erp_Tablesets_BRFuncOperationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations", {
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
   Summary: Calls GetByID to retrieve the BRFuncOperation item
   Description: Calls GetByID to retrieve the BRFuncOperation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BRFuncOperation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param FuncOperUID Desc: FuncOperUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BRFuncOperationRow
   */  
export function get_BRFuncOperations_Company_ACTTypeUID_ACTRevisionUID_FuncOperUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, FuncOperUID:string, OperationUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BRFuncOperationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FuncOperUID + "," + OperationUID + ")", {
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
         resolve(data as Erp_Tablesets_BRFuncOperationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BRFuncOperation for the service
   Description: Calls UpdateExt to update BRFuncOperation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BRFuncOperation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param FuncOperUID Desc: FuncOperUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BRFuncOperationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BRFuncOperations_Company_ACTTypeUID_ACTRevisionUID_FuncOperUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, FuncOperUID:string, OperationUID:string, requestBody:Erp_Tablesets_BRFuncOperationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FuncOperUID + "," + OperationUID + ")", {
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
   Summary: Call UpdateExt to delete BRFuncOperation item
   Description: Call UpdateExt to delete BRFuncOperation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BRFuncOperation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ACTTypeUID Desc: ACTTypeUID   Required: True
      @param ACTRevisionUID Desc: ACTRevisionUID   Required: True
      @param FuncOperUID Desc: FuncOperUID   Required: True
      @param OperationUID Desc: OperationUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BRFuncOperations_Company_ACTTypeUID_ACTRevisionUID_FuncOperUID_OperationUID(Company:string, ACTTypeUID:string, ACTRevisionUID:string, FuncOperUID:string, OperationUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperations(" + Company + "," + ACTTypeUID + "," + ACTRevisionUID + "," + FuncOperUID + "," + OperationUID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeListRow)
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
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClauseACTType:string, whereClauseACTRevision:string, whereClauseABTDocLine:string, whereClauseABTAmount:string, whereClauseABTPostEntity:string, whereClauseABTPostCode:string, whereClauseABTQuery:string, whereClauseABTQParam:string, whereClauseACTBook:string, whereClauseBookingRule:string, whereClauseBookValRule:string, whereClauseBROperation:string, whereClauseBROperationCustom:string, whereClauseBRFunction:string, whereClauseBookVar:string, whereClauseBRFuncArgs:string, whereClauseBRFuncOperation:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseACTType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseACTType=" + whereClauseACTType
   }
   if(typeof whereClauseACTRevision!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseACTRevision=" + whereClauseACTRevision
   }
   if(typeof whereClauseABTDocLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseABTDocLine=" + whereClauseABTDocLine
   }
   if(typeof whereClauseABTAmount!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseABTAmount=" + whereClauseABTAmount
   }
   if(typeof whereClauseABTPostEntity!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseABTPostEntity=" + whereClauseABTPostEntity
   }
   if(typeof whereClauseABTPostCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseABTPostCode=" + whereClauseABTPostCode
   }
   if(typeof whereClauseABTQuery!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseABTQuery=" + whereClauseABTQuery
   }
   if(typeof whereClauseABTQParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseABTQParam=" + whereClauseABTQParam
   }
   if(typeof whereClauseACTBook!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseACTBook=" + whereClauseACTBook
   }
   if(typeof whereClauseBookingRule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBookingRule=" + whereClauseBookingRule
   }
   if(typeof whereClauseBookValRule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBookValRule=" + whereClauseBookValRule
   }
   if(typeof whereClauseBROperation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBROperation=" + whereClauseBROperation
   }
   if(typeof whereClauseBROperationCustom!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBROperationCustom=" + whereClauseBROperationCustom
   }
   if(typeof whereClauseBRFunction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBRFunction=" + whereClauseBRFunction
   }
   if(typeof whereClauseBookVar!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBookVar=" + whereClauseBookVar
   }
   if(typeof whereClauseBRFuncArgs!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBRFuncArgs=" + whereClauseBRFuncArgs
   }
   if(typeof whereClauseBRFuncOperation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBRFuncOperation=" + whereClauseBRFuncOperation
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(acTTypeUID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof acTTypeUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "acTTypeUID=" + acTTypeUID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetList" + params, {
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
   Summary: Invoke method GetRelatedContextItemsCustom
   Description: Returns tree of available values for substitute in functions params for rule's custom operations
   OperationID: GetRelatedContextItemsCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedContextItemsCustom(requestBody:GetRelatedContextItemsCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelatedContextItemsCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRelatedContextItemsCustom", {
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
         resolve(data as GetRelatedContextItemsCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelatedContextItems
   Description: Returns tree of available values for substitute in functions params for rule's base operations
   OperationID: GetRelatedContextItems
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedContextItems(requestBody:GetRelatedContextItems_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelatedContextItems_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRelatedContextItems", {
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
         resolve(data as GetRelatedContextItems_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessFormulaParamClick
   Description: Handle click on function's param in Base operations. It just can return data in ACTTypeSubDataTableset or just execute command with modifying linkcombo data
   OperationID: ProcessFormulaParamClick
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessFormulaParamClick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFormulaParamClick_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessFormulaParamClick(requestBody:ProcessFormulaParamClick_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessFormulaParamClick_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ProcessFormulaParamClick", {
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
         resolve(data as ProcessFormulaParamClick_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessFormulaParamClickCustom
   Description: Handle click on function's param in Custom operations. It just can return data in ACTTypeSubDataTableset or just execute command with modifying linkcombo data
   OperationID: ProcessFormulaParamClickCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessFormulaParamClickCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFormulaParamClickCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessFormulaParamClickCustom(requestBody:ProcessFormulaParamClickCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessFormulaParamClickCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ProcessFormulaParamClickCustom", {
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
         resolve(data as ProcessFormulaParamClickCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessFormulaParamClickFuncOper
   Description: Handle click on function's param in function's operations. It just can return data in ACTTypeSubDataTableset or just execute command with modifying linkcombo data
   OperationID: ProcessFormulaParamClickFuncOper
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessFormulaParamClickFuncOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFormulaParamClickFuncOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessFormulaParamClickFuncOper(requestBody:ProcessFormulaParamClickFuncOper_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessFormulaParamClickFuncOper_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ProcessFormulaParamClickFuncOper", {
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
         resolve(data as ProcessFormulaParamClickFuncOper_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetValueTypesForPostCode
   Description: GetValueTypesForPostCode
   OperationID: GetValueTypesForPostCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetValueTypesForPostCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValueTypesForPostCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetValueTypesForPostCode(requestBody:GetValueTypesForPostCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetValueTypesForPostCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetValueTypesForPostCode", {
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
         resolve(data as GetValueTypesForPostCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnBROperationIsLogicalConditionChanged
   OperationID: OnBROperationIsLogicalConditionChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnBROperationIsLogicalConditionChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationIsLogicalConditionChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnBROperationIsLogicalConditionChanged(requestBody:OnBROperationIsLogicalConditionChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnBROperationIsLogicalConditionChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnBROperationIsLogicalConditionChanged", {
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
         resolve(data as OnBROperationIsLogicalConditionChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnBROperationCustomIsLogicalConditionChanged
   OperationID: OnBROperationCustomIsLogicalConditionChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnBROperationCustomIsLogicalConditionChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationCustomIsLogicalConditionChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnBROperationCustomIsLogicalConditionChanged(requestBody:OnBROperationCustomIsLogicalConditionChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnBROperationCustomIsLogicalConditionChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnBROperationCustomIsLogicalConditionChanged", {
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
         resolve(data as OnBROperationCustomIsLogicalConditionChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnBRFuncOperationIsLogicalConditionChanged
   OperationID: OnBRFuncOperationIsLogicalConditionChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnBRFuncOperationIsLogicalConditionChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBRFuncOperationIsLogicalConditionChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnBRFuncOperationIsLogicalConditionChanged(requestBody:OnBRFuncOperationIsLogicalConditionChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnBRFuncOperationIsLogicalConditionChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnBRFuncOperationIsLogicalConditionChanged", {
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
         resolve(data as OnBRFuncOperationIsLogicalConditionChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnBROperationContainerTypeChanging
   Description: Validates proposed value of the ContairerType value in the BROperation table
   OperationID: OnBROperationContainerTypeChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnBROperationContainerTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationContainerTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnBROperationContainerTypeChanging(requestBody:OnBROperationContainerTypeChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnBROperationContainerTypeChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnBROperationContainerTypeChanging", {
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
         resolve(data as OnBROperationContainerTypeChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnBROperationCustomContainerTypeChanging
   Description: Validates proposed value of the ContairerType value in the BROperationCustom table
   OperationID: OnBROperationCustomContainerTypeChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnBROperationCustomContainerTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBROperationCustomContainerTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnBROperationCustomContainerTypeChanging(requestBody:OnBROperationCustomContainerTypeChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnBROperationCustomContainerTypeChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnBROperationCustomContainerTypeChanging", {
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
         resolve(data as OnBROperationCustomContainerTypeChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnBRFuncOperationContainerTypeChanging
   Description: Validates proposed value of the ContairerType value in the BRFuncOperation table
   OperationID: OnBRFuncOperationContainerTypeChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnBRFuncOperationContainerTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBRFuncOperationContainerTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnBRFuncOperationContainerTypeChanging(requestBody:OnBRFuncOperationContainerTypeChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnBRFuncOperationContainerTypeChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnBRFuncOperationContainerTypeChanging", {
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
         resolve(data as OnBRFuncOperationContainerTypeChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OperationFunctionUIDChanging
   Description: Invoked when FunctionUID is changed on BRFuncOperation/BROperation/BROperationCustom
   OperationID: OperationFunctionUIDChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OperationFunctionUIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OperationFunctionUIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OperationFunctionUIDChanging(requestBody:OperationFunctionUIDChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OperationFunctionUIDChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OperationFunctionUIDChanging", {
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
         resolve(data as OperationFunctionUIDChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BROperationUpdateContainer
   OperationID: BROperationUpdateContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BROperationUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROperationUpdateContainer(requestBody:BROperationUpdateContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BROperationUpdateContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationUpdateContainer", {
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
         resolve(data as BROperationUpdateContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BROperationCustomUpdateContainer
   OperationID: BROperationCustomUpdateContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BROperationCustomUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationCustomUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROperationCustomUpdateContainer(requestBody:BROperationCustomUpdateContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BROperationCustomUpdateContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustomUpdateContainer", {
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
         resolve(data as BROperationCustomUpdateContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BRFuncOperationUpdateContainer
   OperationID: BRFuncOperationUpdateContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BRFuncOperationUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFuncOperationUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFuncOperationUpdateContainer(requestBody:BRFuncOperationUpdateContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BRFuncOperationUpdateContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperationUpdateContainer", {
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
         resolve(data as BRFuncOperationUpdateContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BROperationUpdateContainerFormula
   OperationID: BROperationUpdateContainerFormula
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BROperationUpdateContainerFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationUpdateContainerFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROperationUpdateContainerFormula(requestBody:BROperationUpdateContainerFormula_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BROperationUpdateContainerFormula_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationUpdateContainerFormula", {
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
         resolve(data as BROperationUpdateContainerFormula_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BROPerationCustomUpdateContainerFormula
   OperationID: BROPerationCustomUpdateContainerFormula
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BROPerationCustomUpdateContainerFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROPerationCustomUpdateContainerFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROPerationCustomUpdateContainerFormula(requestBody:BROPerationCustomUpdateContainerFormula_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BROPerationCustomUpdateContainerFormula_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROPerationCustomUpdateContainerFormula", {
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
         resolve(data as BROPerationCustomUpdateContainerFormula_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BRFuncOperationUpdateContainerFormula
   OperationID: BRFuncOperationUpdateContainerFormula
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BRFuncOperationUpdateContainerFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFuncOperationUpdateContainerFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFuncOperationUpdateContainerFormula(requestBody:BRFuncOperationUpdateContainerFormula_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BRFuncOperationUpdateContainerFormula_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperationUpdateContainerFormula", {
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
         resolve(data as BRFuncOperationUpdateContainerFormula_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectionCriteriaAddOnClick
   Description: Updates SelectionCriteria value on Add button click
   OperationID: SelectionCriteriaAddOnClick
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectionCriteriaAddOnClick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectionCriteriaAddOnClick_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectionCriteriaAddOnClick(requestBody:SelectionCriteriaAddOnClick_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectionCriteriaAddOnClick_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/SelectionCriteriaAddOnClick", {
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
         resolve(data as SelectionCriteriaAddOnClick_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddMultipleBooks
   Description: Adds new ACTBook records.  Multiple books can be created by passing ~ separated list.  Records are saved to the DB.
   OperationID: AddMultipleBooks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddMultipleBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMultipleBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddMultipleBooks(requestBody:AddMultipleBooks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddMultipleBooks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/AddMultipleBooks", {
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
         resolve(data as AddMultipleBooks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ABTBookGetNewExt
   Description: Add new GLBook to Transaction Type without loading of system functions.
   OperationID: ABTBookGetNewExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ABTBookGetNewExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTBookGetNewExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTBookGetNewExt(requestBody:ABTBookGetNewExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ABTBookGetNewExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTBookGetNewExt", {
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
         resolve(data as ABTBookGetNewExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadTwoDatasetsTestMethod1
   OperationID: LoadTwoDatasetsTestMethod1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadTwoDatasetsTestMethod1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadTwoDatasetsTestMethod1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadTwoDatasetsTestMethod1(requestBody:LoadTwoDatasetsTestMethod1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadTwoDatasetsTestMethod1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadTwoDatasetsTestMethod1", {
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
         resolve(data as LoadTwoDatasetsTestMethod1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateTwoDatasetsTestMethod1
   OperationID: UpdateTwoDatasetsTestMethod1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateTwoDatasetsTestMethod1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateTwoDatasetsTestMethod1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateTwoDatasetsTestMethod1(requestBody:UpdateTwoDatasetsTestMethod1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateTwoDatasetsTestMethod1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/UpdateTwoDatasetsTestMethod1", {
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
         resolve(data as UpdateTwoDatasetsTestMethod1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSyntaxRevision
   Description: Checks all function and rules in a revision for syntax errors. Updates IsError and ErrorText fields.
   OperationID: CheckSyntaxRevision
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSyntaxRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntaxRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSyntaxRevision(requestBody:CheckSyntaxRevision_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSyntaxRevision_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CheckSyntaxRevision", {
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
         resolve(data as CheckSyntaxRevision_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSyntaxFunction
   Description: Checks the current function for syntax errors. Updates IsError and ErrorText fields.
   OperationID: CheckSyntaxFunction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSyntaxFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntaxFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSyntaxFunction(requestBody:CheckSyntaxFunction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSyntaxFunction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CheckSyntaxFunction", {
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
         resolve(data as CheckSyntaxFunction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSyntaxRule
   Description: Checks the current rule for syntax errors. Updates IsError and ErrorText fields.
   OperationID: CheckSyntaxRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSyntaxRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntaxRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSyntaxRule(requestBody:CheckSyntaxRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSyntaxRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CheckSyntaxRule", {
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
         resolve(data as CheckSyntaxRule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewACTType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewACTType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewACTType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewACTType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewACTType(requestBody:GetNewACTType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewACTType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewACTType", {
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
         resolve(data as GetNewACTType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewACTRevision
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewACTRevision
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewACTRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewACTRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewACTRevision(requestBody:GetNewACTRevision_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewACTRevision_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewACTRevision", {
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
         resolve(data as GetNewACTRevision_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewABTDocLine
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTDocLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewABTDocLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTDocLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewABTDocLine(requestBody:GetNewABTDocLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewABTDocLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewABTDocLine", {
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
         resolve(data as GetNewABTDocLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewABTAmount
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewABTAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewABTAmount(requestBody:GetNewABTAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewABTAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewABTAmount", {
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
         resolve(data as GetNewABTAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewABTPostEntity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTPostEntity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewABTPostEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTPostEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewABTPostEntity(requestBody:GetNewABTPostEntity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewABTPostEntity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewABTPostEntity", {
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
         resolve(data as GetNewABTPostEntity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewABTPostCode
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTPostCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewABTPostCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTPostCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewABTPostCode(requestBody:GetNewABTPostCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewABTPostCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewABTPostCode", {
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
         resolve(data as GetNewABTPostCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewABTQuery
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTQuery
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewABTQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewABTQuery(requestBody:GetNewABTQuery_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewABTQuery_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewABTQuery", {
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
         resolve(data as GetNewABTQuery_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewABTQParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewABTQParam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewABTQParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewABTQParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewABTQParam(requestBody:GetNewABTQParam_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewABTQParam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewABTQParam", {
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
         resolve(data as GetNewABTQParam_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewACTBook
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewACTBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewACTBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewACTBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewACTBook(requestBody:GetNewACTBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewACTBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewACTBook", {
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
         resolve(data as GetNewACTBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBookingRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBookingRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBookingRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBookingRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBookingRule(requestBody:GetNewBookingRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBookingRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewBookingRule", {
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
         resolve(data as GetNewBookingRule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBROperation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBROperation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBROperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBROperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBROperation(requestBody:GetNewBROperation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBROperation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewBROperation", {
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
         resolve(data as GetNewBROperation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBROperationCustom
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBROperationCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBROperationCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBROperationCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBROperationCustom(requestBody:GetNewBROperationCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBROperationCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewBROperationCustom", {
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
         resolve(data as GetNewBROperationCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBRFunction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBRFunction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBRFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBRFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBRFunction(requestBody:GetNewBRFunction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBRFunction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewBRFunction", {
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
         resolve(data as GetNewBRFunction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBookVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBookVar
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBookVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBookVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBookVar(requestBody:GetNewBookVar_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBookVar_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewBookVar", {
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
         resolve(data as GetNewBookVar_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBRFuncArgs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBRFuncArgs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBRFuncArgs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBRFuncArgs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBRFuncArgs(requestBody:GetNewBRFuncArgs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBRFuncArgs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewBRFuncArgs", {
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
         resolve(data as GetNewBRFuncArgs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBRFuncOperation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBRFuncOperation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBRFuncOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBRFuncOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBRFuncOperation(requestBody:GetNewBRFuncOperation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBRFuncOperation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetNewBRFuncOperation", {
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
         resolve(data as GetNewBRFuncOperation_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/UpdateExt", {
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

   /**  
   Summary: Invoke method GetFunctionPhrase
   Description: Returns Function name for the linked combo
   OperationID: GetFunctionPhrase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFunctionPhrase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionPhrase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionPhrase(requestBody:GetFunctionPhrase_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFunctionPhrase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFunctionPhrase", {
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
         resolve(data as GetFunctionPhrase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BRFunctionPhraseElementMove
   Description: move up/down the phrase element inside the structure
   OperationID: BRFunctionPhraseElementMove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BRFunctionPhraseElementMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFunctionPhraseElementMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFunctionPhraseElementMove(requestBody:BRFunctionPhraseElementMove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BRFunctionPhraseElementMove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctionPhraseElementMove", {
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
         resolve(data as BRFunctionPhraseElementMove_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BRFunctionPhraseUpdate
   Description: Update function name
   OperationID: BRFunctionPhraseUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BRFunctionPhraseUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFunctionPhraseUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFunctionPhraseUpdate(requestBody:BRFunctionPhraseUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BRFunctionPhraseUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFunctionPhraseUpdate", {
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
         resolve(data as BRFunctionPhraseUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBRFunctionPhraseElementText
   Description: Handling of change Phrase Element text
   OperationID: OnChangeBRFunctionPhraseElementText
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionPhraseElementText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionPhraseElementText_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBRFunctionPhraseElementText(requestBody:OnChangeBRFunctionPhraseElementText_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBRFunctionPhraseElementText_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangeBRFunctionPhraseElementText", {
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
         resolve(data as OnChangeBRFunctionPhraseElementText_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBRFunctionPhraseElementType
   Description: Handling of change Phrase Element type
   OperationID: OnChangeBRFunctionPhraseElementType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionPhraseElementType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionPhraseElementType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBRFunctionPhraseElementType(requestBody:OnChangeBRFunctionPhraseElementType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBRFunctionPhraseElementType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangeBRFunctionPhraseElementType", {
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
         resolve(data as OnChangeBRFunctionPhraseElementType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBRFunctionPhraseElementArgType
   Description: Handling of changing Function Argument type in the function phrase
   OperationID: OnChangeBRFunctionPhraseElementArgType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionPhraseElementArgType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionPhraseElementArgType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBRFunctionPhraseElementArgType(requestBody:OnChangeBRFunctionPhraseElementArgType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBRFunctionPhraseElementArgType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangeBRFunctionPhraseElementArgType", {
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
         resolve(data as OnChangeBRFunctionPhraseElementArgType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FunctionPhraseElementGetNew
   Description: Creates new BRFunctionPhrase row
   OperationID: FunctionPhraseElementGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FunctionPhraseElementGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FunctionPhraseElementGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FunctionPhraseElementGetNew(requestBody:FunctionPhraseElementGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FunctionPhraseElementGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/FunctionPhraseElementGetNew", {
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
         resolve(data as FunctionPhraseElementGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FunctionPhraseElementDelete
   Description: Delete Function Phrase Element row
   OperationID: FunctionPhraseElementDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FunctionPhraseElementDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FunctionPhraseElementDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FunctionPhraseElementDelete(requestBody:FunctionPhraseElementDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FunctionPhraseElementDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/FunctionPhraseElementDelete", {
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
         resolve(data as FunctionPhraseElementDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFunctionPhraseElements
   Description: Returns the list of Function Phrase elements
   OperationID: GetFunctionPhraseElements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFunctionPhraseElements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionPhraseElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionPhraseElements(requestBody:GetFunctionPhraseElements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFunctionPhraseElements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFunctionPhraseElements", {
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
         resolve(data as GetFunctionPhraseElements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelatedContextItemsFunctionPhrase
   Description: returns the list of available Function Argument types in hierarchical structure
   OperationID: GetRelatedContextItemsFunctionPhrase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsFunctionPhrase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsFunctionPhrase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedContextItemsFunctionPhrase(requestBody:GetRelatedContextItemsFunctionPhrase_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelatedContextItemsFunctionPhrase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRelatedContextItemsFunctionPhrase", {
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
         resolve(data as GetRelatedContextItemsFunctionPhrase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CompareRevisions
   Description: Compares the revisions and returns the tree
   OperationID: CompareRevisions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CompareRevisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompareRevisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CompareRevisions(requestBody:CompareRevisions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CompareRevisions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CompareRevisions", {
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
         resolve(data as CompareRevisions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLeftTree
   Description: Compares the operations and gets the Left/Revision 1 tree
   OperationID: GetLeftTree
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLeftTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLeftTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLeftTree(requestBody:GetLeftTree_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLeftTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetLeftTree", {
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
         resolve(data as GetLeftTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRightTree
   Description: Compares the operations and gets the Right/Revision 2 tree
   OperationID: GetRightTree
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRightTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRightTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRightTree(requestBody:GetRightTree_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRightTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRightTree", {
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
         resolve(data as GetRightTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFunctionTree
   Description: Returns Function Tree structure.
   OperationID: Get_GetFunctionTree
      @param GPostingUID Desc: Function SysRowID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)   Required: True   Allow empty value : True
      @param NodeID Desc: Fake node.   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetFunctionTree(GPostingUID:string, NodeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof GPostingUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "GPostingUID=" + GPostingUID
   }
   if(typeof NodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "NodeID=" + NodeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFunctionTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFunctionTree" + params, {
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
         resolve(data as GetFunctionTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPostingRuleBaseTree
   Description: Returns Posting Rule Base Tree structure.
   OperationID: Get_GetPostingRuleBaseTree
      @param GPostingUID Desc: Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)   Required: True   Allow empty value : True
      @param NodeID Desc: Fake node.   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostingRuleBaseTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetPostingRuleBaseTree(GPostingUID:string, NodeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof GPostingUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "GPostingUID=" + GPostingUID
   }
   if(typeof NodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "NodeID=" + NodeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPostingRuleBaseTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetPostingRuleBaseTree" + params, {
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
         resolve(data as GetPostingRuleBaseTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPostingRuleCustomizationTree
   Description: Returns Posting Rule Base Tree structure.
   OperationID: Get_GetPostingRuleCustomizationTree
      @param GPostingUID Desc: Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)   Required: True   Allow empty value : True
      @param NodeID Desc: Fake node.   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostingRuleCustomizationTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetPostingRuleCustomizationTree(GPostingUID:string, NodeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof GPostingUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "GPostingUID=" + GPostingUID
   }
   if(typeof NodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "NodeID=" + NodeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPostingRuleCustomizationTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetPostingRuleCustomizationTree" + params, {
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
         resolve(data as GetPostingRuleCustomizationTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InitializeForTests
   Description: This method is used for Unit Tests to initialize data
   OperationID: InitializeForTests
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeForTests_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitializeForTests(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InitializeForTests_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/InitializeForTests", {
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
         resolve(data as InitializeForTests_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CanActivateRevision
   Description: Check if ACTRevision can be Activated or not
   OperationID: CanActivateRevision
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CanActivateRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanActivateRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CanActivateRevision(requestBody:CanActivateRevision_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CanActivateRevision_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CanActivateRevision", {
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
         resolve(data as CanActivateRevision_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustomContextMenuXml
   Description: Returns context menu items as xml for rules constructor.
   OperationID: GetCustomContextMenuXml
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCustomContextMenuXml_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomContextMenuXml_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomContextMenuXml(requestBody:GetCustomContextMenuXml_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCustomContextMenuXml_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetCustomContextMenuXml", {
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
         resolve(data as GetCustomContextMenuXml_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ABTDocLineGetNew
   Description: Create new BR Operation.
   OperationID: ABTDocLineGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ABTDocLineGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTDocLineGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTDocLineGetNew(requestBody:ABTDocLineGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ABTDocLineGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTDocLineGetNew", {
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
         resolve(data as ABTDocLineGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ABTPostCodeGetNew
   Description: Create new ABTPostcode.
   OperationID: ABTPostCodeGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ABTPostCodeGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTPostCodeGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTPostCodeGetNew(requestBody:ABTPostCodeGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ABTPostCodeGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTPostCodeGetNew", {
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
         resolve(data as ABTPostCodeGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ABTBookGetNew
   Description: Add book to book list.
   OperationID: ABTBookGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ABTBookGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ABTBookGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ABTBookGetNew(requestBody:ABTBookGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ABTBookGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ABTBookGetNew", {
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
         resolve(data as ABTBookGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddMappedBook
   Description: Adds a mapped book.
   OperationID: AddMappedBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddMappedBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMappedBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddMappedBook(requestBody:AddMappedBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddMappedBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/AddMappedBook", {
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
         resolve(data as AddMappedBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BookingRuleGetNew
   Description: Create new Booking Rule.
   OperationID: BookingRuleGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BookingRuleGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookingRuleGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookingRuleGetNew(requestBody:BookingRuleGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BookingRuleGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookingRuleGetNew", {
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
         resolve(data as BookingRuleGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBookingRuleName
   Description: Check value new DisplayName for rule. It should be unique in one book.
   OperationID: OnChangeBookingRuleName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBookingRuleName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookingRuleName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBookingRuleName(requestBody:OnChangeBookingRuleName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBookingRuleName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangeBookingRuleName", {
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
         resolve(data as OnChangeBookingRuleName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BookVariableGetNew
   Description: Create new variable of type of type book, function, rule.
   OperationID: BookVariableGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BookVariableGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookVariableGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookVariableGetNew(requestBody:BookVariableGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BookVariableGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVariableGetNew", {
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
         resolve(data as BookVariableGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BRFuncOperationGetNew
   Description: Create new BR Operation.
   OperationID: BRFuncOperationGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BRFuncOperationGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BRFuncOperationGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BRFuncOperationGetNew(requestBody:BRFuncOperationGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BRFuncOperationGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BRFuncOperationGetNew", {
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
         resolve(data as BRFuncOperationGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBRFunctionFormula
   Description: Check value new Formula for function. It should be unique in one book.
   OperationID: OnChangeBRFunctionFormula
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBRFunctionFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBRFunctionFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBRFunctionFormula(requestBody:OnChangeBRFunctionFormula_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBRFunctionFormula_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangeBRFunctionFormula", {
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
         resolve(data as OnChangeBRFunctionFormula_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BROperationGetNew
   Description: Create new BR Operation.
   OperationID: BROperationGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BROperationGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROperationGetNew(requestBody:BROperationGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BROperationGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationGetNew", {
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
         resolve(data as BROperationGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BROperationCustomGetNew
   Description: Create new BR Operation Customization.
   OperationID: BROperationCustomGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BROperationCustomGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BROperationCustomGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BROperationCustomGetNew(requestBody:BROperationCustomGetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BROperationCustomGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BROperationCustomGetNew", {
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
         resolve(data as BROperationCustomGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBAQ
   Description: Refresh parameter list after BAQ change.
   OperationID: ChangeBAQ
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBAQ(requestBody:ChangeBAQ_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeBAQ_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ChangeBAQ", {
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
         resolve(data as ChangeBAQ_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRevisionStatusMode
   Description: Change Revision Status or Mode.
   OperationID: ChangeRevisionStatusMode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRevisionStatusMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionStatusMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevisionStatusMode(requestBody:ChangeRevisionStatusMode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRevisionStatusMode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ChangeRevisionStatusMode", {
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
         resolve(data as ChangeRevisionStatusMode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBAQExists
   Description: Checks if BAQ exists.
   OperationID: CheckBAQExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBAQExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBAQExists(requestBody:CheckBAQExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBAQExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CheckBAQExists", {
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
         resolve(data as CheckBAQExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBeforeActivateRevision
   Description: Return an error if revision cannot be activated
   OperationID: CheckBeforeActivateRevision
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBeforeActivateRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeActivateRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBeforeActivateRevision(requestBody:CheckBeforeActivateRevision_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBeforeActivateRevision_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CheckBeforeActivateRevision", {
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
         resolve(data as CheckBeforeActivateRevision_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListMappedBooksWithRules
   Description: Return list of mapped books having posting rules or functions for a particular revision. Used by UI when copy revision.
   OperationID: ListMappedBooksWithRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ListMappedBooksWithRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListMappedBooksWithRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListMappedBooksWithRules(requestBody:ListMappedBooksWithRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListMappedBooksWithRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ListMappedBooksWithRules", {
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
         resolve(data as ListMappedBooksWithRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BookIsNotEmpty
   Description: Returns true if book has defined booking rules or functions.
   OperationID: BookIsNotEmpty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BookIsNotEmpty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookIsNotEmpty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookIsNotEmpty(requestBody:BookIsNotEmpty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BookIsNotEmpty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookIsNotEmpty", {
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
         resolve(data as BookIsNotEmpty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyListOfFunctions
   Description: Copy defined function list
   OperationID: CopyListOfFunctions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyListOfFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyListOfFunctions(requestBody:CopyListOfFunctions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyListOfFunctions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CopyListOfFunctions", {
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
         resolve(data as CopyListOfFunctions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyListOfFunctionsWithWarn
   Description: Copy defined function list
   OperationID: CopyListOfFunctionsWithWarn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyListOfFunctionsWithWarn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfFunctionsWithWarn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyListOfFunctionsWithWarn(requestBody:CopyListOfFunctionsWithWarn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyListOfFunctionsWithWarn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CopyListOfFunctionsWithWarn", {
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
         resolve(data as CopyListOfFunctionsWithWarn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyListOfRules
   Description: Copy defined booking rule list
   OperationID: CopyListOfRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyListOfRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyListOfRules(requestBody:CopyListOfRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyListOfRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CopyListOfRules", {
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
         resolve(data as CopyListOfRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyListOfRulesWithWarn
   Description: Copy defined booking rule list
   OperationID: CopyListOfRulesWithWarn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyListOfRulesWithWarn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyListOfRulesWithWarn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyListOfRulesWithWarn(requestBody:CopyListOfRulesWithWarn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyListOfRulesWithWarn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CopyListOfRulesWithWarn", {
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
         resolve(data as CopyListOfRulesWithWarn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyOperations
   Description: Allow copy defined operation in different GL Transaction Type.
   OperationID: CopyOperations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyOperations(requestBody:CopyOperations_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyOperations_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CopyOperations", {
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
         resolve(data as CopyOperations_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CustomUpdate
   Description: Custom Update Database
   OperationID: CustomUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomUpdate(requestBody:CustomUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/CustomUpdate", {
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
         resolve(data as CustomUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteACTBook
   OperationID: DeleteACTBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteACTBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteACTBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteACTBook(requestBody:DeleteACTBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteACTBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/DeleteACTBook", {
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
         resolve(data as DeleteACTBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteMappedBook
   OperationID: DeleteMappedBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteMappedBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMappedBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteMappedBook(requestBody:DeleteMappedBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteMappedBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/DeleteMappedBook", {
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
         resolve(data as DeleteMappedBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteOpItems
   Description: Delete single Operation or with child operations
   OperationID: DeleteOpItems
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteOpItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOpItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteOpItems(requestBody:DeleteOpItems_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteOpItems_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/DeleteOpItems", {
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
         resolve(data as DeleteOpItems_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteBROperationCustom
   Description: Delete single Custom Operation or with child operations
   OperationID: DeleteBROperationCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteBROperationCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBROperationCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteBROperationCustom(requestBody:DeleteBROperationCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteBROperationCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/DeleteBROperationCustom", {
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
         resolve(data as DeleteBROperationCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRevisionByName
   Description: Delete revision by Revision Code.
   OperationID: DeleteRevisionByName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRevisionByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRevisionByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRevisionByName(requestBody:DeleteRevisionByName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRevisionByName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/DeleteRevisionByName", {
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
         resolve(data as DeleteRevisionByName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRevsBeforeImport
   Description: Delete all previous revisions for spec. transaction types.
   OperationID: DeleteRevsBeforeImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRevsBeforeImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRevsBeforeImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRevsBeforeImport(requestBody:DeleteRevsBeforeImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRevsBeforeImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/DeleteRevsBeforeImport", {
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
         resolve(data as DeleteRevsBeforeImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AfterDeleteVBDItem
   Description: For Develop Mode Revision should be updated after deletion any Item from VBD Structure
   OperationID: AfterDeleteVBDItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AfterDeleteVBDItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteVBDItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterDeleteVBDItem(requestBody:AfterDeleteVBDItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AfterDeleteVBDItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/AfterDeleteVBDItem", {
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
         resolve(data as AfterDeleteVBDItem_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AfterDeleteBookItem
   Description: For Develop Mode Book should be updated after deletion any its Item
   OperationID: AfterDeleteBookItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AfterDeleteBookItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteBookItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterDeleteBookItem(requestBody:AfterDeleteBookItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AfterDeleteBookItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/AfterDeleteBookItem", {
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
         resolve(data as AfterDeleteBookItem_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AfterDeleteFunctionItem
   Description: For Develop Mode Book and Function should be updated after deletion any Function Item
   OperationID: AfterDeleteFunctionItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AfterDeleteFunctionItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteFunctionItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterDeleteFunctionItem(requestBody:AfterDeleteFunctionItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AfterDeleteFunctionItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/AfterDeleteFunctionItem", {
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
         resolve(data as AfterDeleteFunctionItem_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AfterDeleteRuleItem
   Description: For Develop Mode Book and Rule should be updated after deletion any Rule Item
   OperationID: AfterDeleteRuleItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AfterDeleteRuleItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterDeleteRuleItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterDeleteRuleItem(requestBody:AfterDeleteRuleItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AfterDeleteRuleItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/AfterDeleteRuleItem", {
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
         resolve(data as AfterDeleteRuleItem_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportToXML
   Description: Export revision to XML format
   OperationID: ExportToXML
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportToXML_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToXML_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportToXML(requestBody:ExportToXML_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportToXML_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ExportToXML", {
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
         resolve(data as ExportToXML_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FillBAQDescription
   Description: Populates BAQDescription field with the value from corresponding BAQ for all entried with ADDED or UPDATED status.
   OperationID: FillBAQDescription
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FillBAQDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillBAQDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FillBAQDescription(requestBody:FillBAQDescription_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FillBAQDescription_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/FillBAQDescription", {
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
         resolve(data as FillBAQDescription_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TryCompile
   Description: Compile Post file for GL Transaction Type Revision to check for compilation errors
Throws CompilationException with first 100 exceptions in ExceptionMessageList
   OperationID: TryCompile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TryCompile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TryCompile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TryCompile(requestBody:TryCompile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TryCompile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/TryCompile", {
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
         resolve(data as TryCompile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateTemplate
   Description: Generate Template
   OperationID: GenerateTemplate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateTemplate(requestBody:GenerateTemplate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateTemplate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GenerateTemplate", {
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
         resolve(data as GenerateTemplate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllACTTypesForExport
   Description: Returns all revisions for Export Form
   OperationID: GetAllACTTypesForExport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllACTTypesForExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllACTTypesForExport(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllACTTypesForExport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetAllACTTypesForExport", {
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
         resolve(data as GetAllACTTypesForExport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBookVarOwnerID
   Description: Get list of book variable owner id's.
If owner is function or rule the list will include names and id's.
   OperationID: GetBookVarOwnerID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBookVarOwnerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVarOwnerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBookVarOwnerID(requestBody:GetBookVarOwnerID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBookVarOwnerID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBookVarOwnerID", {
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
         resolve(data as GetBookVarOwnerID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBookVarOwnerTypes
   Description: Get list of bookVar owners - Global, Book, Rule, Function.
   OperationID: GetBookVarOwnerTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVarOwnerTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBookVarOwnerTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBookVarOwnerTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBookVarOwnerTypes", {
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
         resolve(data as GetBookVarOwnerTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBRContainerRows
   Description: Get list of fields.
   OperationID: GetBRContainerRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBRContainerRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBRContainerRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBRContainerRows(requestBody:GetBRContainerRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBRContainerRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBRContainerRows", {
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
         resolve(data as GetBRContainerRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrentVersion
   Description: Get ACTType ID by Name.
   OperationID: GetCurrentVersion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCurrentVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentVersion(requestBody:GetCurrentVersion_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrentVersion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetCurrentVersion", {
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
         resolve(data as GetCurrentVersion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEntityForBookingRule
   Description: Get a value of Entity for a Booking Rule in table PatchFld.
   OperationID: GetEntityForBookingRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEntityForBookingRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntityForBookingRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEntityForBookingRule(requestBody:GetEntityForBookingRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEntityForBookingRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetEntityForBookingRule", {
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
         resolve(data as GetEntityForBookingRule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFlowList
   Description: Get list of flow statements.
   OperationID: GetFlowList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFlowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFlowList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFlowList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFlowList", {
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
         resolve(data as GetFlowList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIDByName
   Description: Get ACTType ID by Name.
   OperationID: GetIDByName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetIDByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIDByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIDByName(requestBody:GetIDByName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetIDByName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetIDByName", {
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
         resolve(data as GetIDByName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOperatorList
   Description: Get list of operators.
   OperationID: GetOperatorList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOperatorList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOperatorList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetOperatorList", {
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
         resolve(data as GetOperatorList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPostCodeTypes
   Description: Get list of possible post code types.
   OperationID: GetPostCodeTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostCodeTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPostCodeTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPostCodeTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetPostCodeTypes", {
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
         resolve(data as GetPostCodeTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevisionIDByName
   Description: Get ACTRevision ID by Name.
   OperationID: GetRevisionIDByName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRevisionIDByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionIDByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevisionIDByName(requestBody:GetRevisionIDByName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRevisionIDByName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRevisionIDByName", {
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
         resolve(data as GetRevisionIDByName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetStatusList
   Description: Get list of revision statuses.
   OperationID: GetStatusList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatusList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetStatusList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetStatusList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetStatusList", {
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
         resolve(data as GetStatusList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSummarizeList
   Description: Get list of summarize options.
   OperationID: GetSummarizeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSummarizeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSummarizeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSummarizeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetSummarizeList", {
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
         resolve(data as GetSummarizeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTrCurrencyList
   Description: Transactional currency options.
   OperationID: GetTrCurrencyList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTrCurrencyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTrCurrencyList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTrCurrencyList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetTrCurrencyList", {
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
         resolve(data as GetTrCurrencyList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVarTypes
   Description: Get list of possible types.
   OperationID: GetVarTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVarTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVarTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVarTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetVarTypes", {
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
         resolve(data as GetVarTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWarningRevisionStatus
   Description: Return warning if status is changing.
   OperationID: GetWarningRevisionStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWarningRevisionStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarningRevisionStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWarningRevisionStatus(requestBody:GetWarningRevisionStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWarningRevisionStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetWarningRevisionStatus", {
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
         resolve(data as GetWarningRevisionStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportFromXML
   Description: Import revision to XML format (obsolete method)
   OperationID: ImportFromXML
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportFromXML_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFromXML_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportFromXML(requestBody:ImportFromXML_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportFromXML_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ImportFromXML", {
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
         resolve(data as ImportFromXML_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportGLTransactionType
   Description: Import revision
   OperationID: ImportGLTransactionType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportGLTransactionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportGLTransactionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportGLTransactionType(requestBody:ImportGLTransactionType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportGLTransactionType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ImportGLTransactionType", {
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
         resolve(data as ImportGLTransactionType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHashSystemXml
   Description: Get hash Value of System Xml
   OperationID: GetHashSystemXml
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetHashSystemXml_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHashSystemXml_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHashSystemXml(requestBody:GetHashSystemXml_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetHashSystemXml_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetHashSystemXml", {
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
         resolve(data as GetHashSystemXml_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadSystemGLTransactionType
   Description: LoadSystemGLTransactionType
   OperationID: LoadSystemGLTransactionType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadSystemGLTransactionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadSystemGLTransactionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadSystemGLTransactionType(requestBody:LoadSystemGLTransactionType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadSystemGLTransactionType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadSystemGLTransactionType", {
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
         resolve(data as LoadSystemGLTransactionType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadBookDataForImport
   Description: Load list of Books, their COA Segments and Default Segment Mapping information for import for selected companies.
   OperationID: LoadBookDataForImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadBookDataForImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBookDataForImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadBookDataForImport(requestBody:LoadBookDataForImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadBookDataForImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadBookDataForImport", {
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
         resolve(data as LoadBookDataForImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportProcessIsAllowed
   Description: Check that manual import process can be started
   OperationID: ImportProcessIsAllowed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportProcessIsAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportProcessIsAllowed(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportProcessIsAllowed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ImportProcessIsAllowed", {
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
         resolve(data as ImportProcessIsAllowed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingABTQuery
   Description: Check ABTQuery is in use when it is trying to change.
   OperationID: OnChangingABTQuery
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingABTQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingABTQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingABTQuery(requestBody:OnChangingABTQuery_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingABTQuery_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangingABTQuery", {
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
         resolve(data as OnChangingABTQuery_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingPostCode
   Description: Check PostCode is in use when it is trying to change.
   OperationID: OnChangingPostCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingPostCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPostCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingPostCode(requestBody:OnChangingPostCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingPostCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangingPostCode", {
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
         resolve(data as OnChangingPostCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsVarInUse
   Description: Checks if a variable (book, function, rule) is used.
   OperationID: IsVarInUse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsVarInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsVarInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsVarInUse(requestBody:IsVarInUse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsVarInUse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/IsVarInUse", {
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
         resolve(data as IsVarInUse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadACTBook
   Description: Load Book details for one book or all
   OperationID: LoadACTBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadACTBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadACTBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadACTBook(requestBody:LoadACTBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadACTBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadACTBook", {
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
         resolve(data as LoadACTBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadAmount
   Description: Load ABTAmount records for Document Line
   OperationID: LoadAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadAmount(requestBody:LoadAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadAmount", {
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
         resolve(data as LoadAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadBooks
   OperationID: LoadBooks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadBooks(requestBody:LoadBooks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadBooks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadBooks", {
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
         resolve(data as LoadBooks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadBookVar
   Description: Load Book details for one book or all
   OperationID: LoadBookVar
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadBookVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBookVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadBookVar(requestBody:LoadBookVar_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadBookVar_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadBookVar", {
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
         resolve(data as LoadBookVar_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadBrFuncArgs
   Description: Load Function arguments
   OperationID: LoadBrFuncArgs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadBrFuncArgs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBrFuncArgs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadBrFuncArgs(requestBody:LoadBrFuncArgs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadBrFuncArgs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadBrFuncArgs", {
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
         resolve(data as LoadBrFuncArgs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadBrFuncOperation
   Description: Load Functions
   OperationID: LoadBrFuncOperation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadBrFuncOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBrFuncOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadBrFuncOperation(requestBody:LoadBrFuncOperation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadBrFuncOperation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadBrFuncOperation", {
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
         resolve(data as LoadBrFuncOperation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadBROperation
   Description: Load Br Operations one or all
   OperationID: LoadBROperation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadBROperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBROperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadBROperation(requestBody:LoadBROperation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadBROperation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadBROperation", {
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
         resolve(data as LoadBROperation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadDocumentLine
   Description: Load Function arguments
   OperationID: LoadDocumentLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadDocumentLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDocumentLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadDocumentLine(requestBody:LoadDocumentLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadDocumentLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadDocumentLine", {
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
         resolve(data as LoadDocumentLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadDocumentLineBAQ
   Description: Load Document Line BAQ
   OperationID: LoadDocumentLineBAQ
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadDocumentLineBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDocumentLineBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadDocumentLineBAQ(requestBody:LoadDocumentLineBAQ_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadDocumentLineBAQ_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadDocumentLineBAQ", {
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
         resolve(data as LoadDocumentLineBAQ_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadDocumentLineBAQParam
   Description: Load Document Line BAQ
   OperationID: LoadDocumentLineBAQParam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadDocumentLineBAQParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDocumentLineBAQParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadDocumentLineBAQParam(requestBody:LoadDocumentLineBAQParam_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadDocumentLineBAQParam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadDocumentLineBAQParam", {
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
         resolve(data as LoadDocumentLineBAQParam_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadFunction
   Description: Load Functions
   OperationID: LoadFunction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadFunction(requestBody:LoadFunction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadFunction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadFunction", {
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
         resolve(data as LoadFunction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadRevision
   Description: Load revision Details by ID, called when tree node is expanded, can load only first record isFullLoad = 0.
   OperationID: LoadRevision
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadRevision(requestBody:LoadRevision_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadRevision_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadRevision", {
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
         resolve(data as LoadRevision_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadACTType
   Description: Load actType Details by ID, called instaed of GetByID to not load all data
   OperationID: LoadACTType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadACTType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadACTType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadACTType(requestBody:LoadACTType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadACTType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadACTType", {
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
         resolve(data as LoadACTType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadRevisionVersions
   Description: Load revision Versionss.
   OperationID: LoadRevisionVersions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadRevisionVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRevisionVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadRevisionVersions(requestBody:LoadRevisionVersions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadRevisionVersions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadRevisionVersions", {
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
         resolve(data as LoadRevisionVersions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadRule
   Description: Load Rules one or all
   OperationID: LoadRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadRule(requestBody:LoadRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadRule", {
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
         resolve(data as LoadRule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBVRuleAction
   Description: This method should be called when action of validation rule is changed.
   OperationID: OnChangeBVRuleAction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBVRuleAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBVRuleAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBVRuleAction(requestBody:OnChangeBVRuleAction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBVRuleAction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangeBVRuleAction", {
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
         resolve(data as OnChangeBVRuleAction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeEntityDataSource
   Description: This method should be called when Datasource of Post Entity is changed.
   OperationID: OnChangeEntityDataSource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeEntityDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEntityDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEntityDataSource(requestBody:OnChangeEntityDataSource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeEntityDataSource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/OnChangeEntityDataSource", {
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
         resolve(data as OnChangeEntityDataSource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostCodeSourceRefresh
   Description: refresh datasource of post codes.
   OperationID: PostCodeSourceRefresh
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PostCodeSourceRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostCodeSourceRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostCodeSourceRefresh(requestBody:PostCodeSourceRefresh_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PostCodeSourceRefresh_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/PostCodeSourceRefresh", {
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
         resolve(data as PostCodeSourceRefresh_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshBookList
   Description: Refresh Books list
   OperationID: RefreshBookList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshBookList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshBookList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshBookList(requestBody:RefreshBookList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshBookList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/RefreshBookList", {
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
         resolve(data as RefreshBookList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RevisionCopyFrom
   Description: Create copy of Revision.
   OperationID: RevisionCopyFrom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RevisionCopyFrom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionCopyFrom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RevisionCopyFrom(requestBody:RevisionCopyFrom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RevisionCopyFrom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/RevisionCopyFrom", {
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
         resolve(data as RevisionCopyFrom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateABTVerForImport
   Description: Validate vesrions of imported data
   OperationID: ValidateABTVerForImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateABTVerForImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateABTVerForImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateABTVerForImport(requestBody:ValidateABTVerForImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateABTVerForImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ValidateABTVerForImport", {
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
         resolve(data as ValidateABTVerForImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UndoUpdateVersionsWithRefreshDS
   Description: Undo updated vesions of Revision and load result in dataset
   OperationID: UndoUpdateVersionsWithRefreshDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UndoUpdateVersionsWithRefreshDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoUpdateVersionsWithRefreshDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UndoUpdateVersionsWithRefreshDS(requestBody:UndoUpdateVersionsWithRefreshDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UndoUpdateVersionsWithRefreshDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/UndoUpdateVersionsWithRefreshDS", {
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
         resolve(data as UndoUpdateVersionsWithRefreshDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateVersionsWithRefreshDS
   Description: Update Versions for Revision and load result in dataset
   OperationID: UpdateVersionsWithRefreshDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateVersionsWithRefreshDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateVersionsWithRefreshDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateVersionsWithRefreshDS(requestBody:UpdateVersionsWithRefreshDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateVersionsWithRefreshDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/UpdateVersionsWithRefreshDS", {
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
         resolve(data as UpdateVersionsWithRefreshDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBookVersions
   Description: Get Book Versions
   OperationID: GetBookVersions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBookVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBookVersions(requestBody:GetBookVersions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBookVersions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBookVersions", {
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
         resolve(data as GetBookVersions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRuleVersions
   Description: Get Rule Versions
   OperationID: GetRuleVersions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRuleVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRuleVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRuleVersions(requestBody:GetRuleVersions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRuleVersions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRuleVersions", {
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
         resolve(data as GetRuleVersions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFuncVersions
   Description: Get Function Versions
   OperationID: GetFuncVersions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFuncVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFuncVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFuncVersions(requestBody:GetFuncVersions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFuncVersions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFuncVersions", {
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
         resolve(data as GetFuncVersions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevVersions
   Description: Get Revision Versions
   OperationID: GetRevVersions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRevVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevVersions(requestBody:GetRevVersions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRevVersions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRevVersions", {
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
         resolve(data as GetRevVersions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCOAMap
   Description: Purpose: Validate COAMapID
<param name="ipCOAMapUID">COA Map ID to validate</param><param name="ipSourceCOA">COA for the Source Book</param><param name="ipMappedCOA">COA for the Mapped Book</param>
Notes:
   OperationID: ValidateCOAMap
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCOAMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOAMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCOAMap(requestBody:ValidateCOAMap_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCOAMap_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/ValidateCOAMap", {
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
         resolve(data as ValidateCOAMap_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBookPackage
   Description: Return package of selected book
   OperationID: GetBookPackage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBookPackage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookPackage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBookPackage(requestBody:GetBookPackage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBookPackage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBookPackage", {
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
         resolve(data as GetBookPackage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDExt
   Description: Returns ACTType with Active and Draft revisions
   OperationID: GetByIDExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDExt(requestBody:GetByIDExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetByIDExt", {
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
         resolve(data as GetByIDExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID_Revisions
   Description: Returns ACTType with given revisions
   OperationID: GetByID_Revisions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByID_Revisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_Revisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByID_Revisions(requestBody:GetByID_Revisions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_Revisions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetByID_Revisions", {
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
         resolve(data as GetByID_Revisions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RevisionStatusChanging
   Description: Executes when user changes Revision status
   OperationID: RevisionStatusChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RevisionStatusChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionStatusChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RevisionStatusChanging(requestBody:RevisionStatusChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RevisionStatusChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/RevisionStatusChanging", {
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
         resolve(data as RevisionStatusChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BookVarNameTypeChanging
   Description: Executes when BookVar Name or Type changed.
   OperationID: BookVarNameTypeChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BookVarNameTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookVarNameTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookVarNameTypeChanging(requestBody:BookVarNameTypeChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BookVarNameTypeChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVarNameTypeChanging", {
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
         resolve(data as BookVarNameTypeChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BookVarOwnerChanging
   Description: Executes when BookVar Owner is changed.
   OperationID: BookVarOwnerChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BookVarOwnerChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookVarOwnerChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BookVarOwnerChanging(requestBody:BookVarOwnerChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BookVarOwnerChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BookVarOwnerChanging", {
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
         resolve(data as BookVarOwnerChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TableDataFieldChanging
   Description: Executes when DataTable Field name is changed.
   OperationID: TableDataFieldChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TableDataFieldChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableDataFieldChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TableDataFieldChanging(requestBody:TableDataFieldChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TableDataFieldChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/TableDataFieldChanging", {
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
         resolve(data as TableDataFieldChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PopulationMethodChanging
   Description: Refresh ABTPostCode fields after PopulationMethod is changing
   OperationID: PopulationMethodChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PopulationMethodChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulationMethodChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PopulationMethodChanging(requestBody:PopulationMethodChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PopulationMethodChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/PopulationMethodChanging", {
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
         resolve(data as PopulationMethodChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BAQDataFieldChanging
   Description: Executes when BAQFataField is changed.
   OperationID: BAQDataFieldChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BAQDataFieldChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQDataFieldChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQDataFieldChanging(requestBody:BAQDataFieldChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BAQDataFieldChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/BAQDataFieldChanging", {
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
         resolve(data as BAQDataFieldChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevisionsList
   Description: Returns revision list with its status
   OperationID: GetRevisionsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRevisionsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevisionsList(requestBody:GetRevisionsList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRevisionsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRevisionsList", {
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
         resolve(data as GetRevisionsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevisionStatusesList
   Description: Returns statuses for revision.
   OperationID: GetRevisionStatusesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionStatusesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevisionStatusesList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRevisionStatusesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRevisionStatusesList", {
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
         resolve(data as GetRevisionStatusesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGLControlTypesList
   Description: Returns list of GL Control types
   OperationID: GetGLControlTypesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGLControlTypesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLControlTypesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLControlTypesList(requestBody:GetGLControlTypesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGLControlTypesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetGLControlTypesList", {
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
         resolve(data as GetGLControlTypesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRuleContextsList
   Description: Returns contexts of given GL Control type.
   OperationID: GetRuleContextsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRuleContextsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRuleContextsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRuleContextsList(requestBody:GetRuleContextsList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRuleContextsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRuleContextsList", {
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
         resolve(data as GetRuleContextsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMapBookList
   Description: Returns list of Books for mapping
   OperationID: GetMapBookList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMapBookList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapBookList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMapBookList(requestBody:GetMapBookList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMapBookList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetMapBookList", {
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
         resolve(data as GetMapBookList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPostEntityDataSourceList
   Description: Returns list for Post Entity DataSource combobox
   OperationID: GetPostEntityDataSourceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPostEntityDataSourceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostEntityDataSourceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPostEntityDataSourceList(requestBody:GetPostEntityDataSourceList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPostEntityDataSourceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetPostEntityDataSourceList", {
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
         resolve(data as GetPostEntityDataSourceList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFieldsOfBAQList
   Description: Returns delimited list of fields of given BAQ
   OperationID: GetFieldsOfBAQList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFieldsOfBAQList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldsOfBAQList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldsOfBAQList(requestBody:GetFieldsOfBAQList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFieldsOfBAQList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFieldsOfBAQList", {
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
         resolve(data as GetFieldsOfBAQList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCOAMapsList
   Description: Returns COA Map Data
   OperationID: GetCOAMapsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCOAMapsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOAMapsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOAMapsList(requestBody:GetCOAMapsList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCOAMapsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetCOAMapsList", {
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
         resolve(data as GetCOAMapsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCOAIDForBook
   Description: returns COA Id for the book.
   OperationID: GetCOAIDForBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCOAIDForBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOAIDForBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOAIDForBook(requestBody:GetCOAIDForBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCOAIDForBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetCOAIDForBook", {
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
         resolve(data as GetCOAIDForBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFieldsOfTable
   Description: Get delimited list of fields of given table
   OperationID: GetFieldsOfTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFieldsOfTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldsOfTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldsOfTable(requestBody:GetFieldsOfTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFieldsOfTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFieldsOfTable", {
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
         resolve(data as GetFieldsOfTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadRuleVariables
   OperationID: LoadRuleVariables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadRuleVariables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadRuleVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadRuleVariables(requestBody:LoadRuleVariables_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadRuleVariables_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadRuleVariables", {
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
         resolve(data as LoadRuleVariables_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadABTStructure
   OperationID: LoadABTStructure
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadABTStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadABTStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadABTStructure(requestBody:LoadABTStructure_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadABTStructure_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadABTStructure", {
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
         resolve(data as LoadABTStructure_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadGLCntrlTypes
   Description: Load GL Control Contexts
   OperationID: LoadGLCntrlTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadGLCntrlTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadGLCntrlTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadGLCntrlTypes(requestBody:LoadGLCntrlTypes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadGLCntrlTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/LoadGLCntrlTypes", {
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
         resolve(data as LoadGLCntrlTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPostCodeTypesExt
   Description: Get list of possible Data types for post code for Kinetic. It is required to work with link-combo component.
   OperationID: GetPostCodeTypesExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPostCodeTypesExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostCodeTypesExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPostCodeTypesExt(requestBody:GetPostCodeTypesExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPostCodeTypesExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetPostCodeTypesExt", {
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
         resolve(data as GetPostCodeTypesExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContainerPhraseItems
   Description: Returns data of available containers for Container combo
   OperationID: GetContainerPhraseItems
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContainerPhraseItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerPhraseItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContainerPhraseItems(requestBody:GetContainerPhraseItems_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContainerPhraseItems_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetContainerPhraseItems", {
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
         resolve(data as GetContainerPhraseItems_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetConditionList
   Description: Returns Condition Flow list
   OperationID: GetConditionList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConditionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConditionList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetConditionList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetConditionList", {
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
         resolve(data as GetConditionList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFunctionResultTypeList
   Description: Returns the list of available data types for the Book/Function variable
   OperationID: GetFunctionResultTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFunctionResultTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionResultTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionResultTypeList(requestBody:GetFunctionResultTypeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFunctionResultTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFunctionResultTypeList", {
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
         resolve(data as GetFunctionResultTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBookVarTypeList
   Description: Returns the list of available data types for the Book/Function variable
   OperationID: GetBookVarTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBookVarTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookVarTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBookVarTypeList(requestBody:GetBookVarTypeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBookVarTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetBookVarTypeList", {
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
         resolve(data as GetBookVarTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCommonTypeList
   Description: Returns the list of available types for the variable type
   OperationID: GetCommonTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCommonTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCommonTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCommonTypeList(requestBody:GetCommonTypeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCommonTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetCommonTypeList", {
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
         resolve(data as GetCommonTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFormulaPhraseItems
   Description: Returns data for Formula combo
   OperationID: GetFormulaPhraseItems
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFormulaPhraseItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormulaPhraseItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFormulaPhraseItems(requestBody:GetFormulaPhraseItems_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFormulaPhraseItems_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetFormulaPhraseItems", {
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
         resolve(data as GetFormulaPhraseItems_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelatedContextItemsBookVarType
   OperationID: GetRelatedContextItemsBookVarType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsBookVarType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsBookVarType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedContextItemsBookVarType(requestBody:GetRelatedContextItemsBookVarType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelatedContextItemsBookVarType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRelatedContextItemsBookVarType", {
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
         resolve(data as GetRelatedContextItemsBookVarType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelatedContextItemsFunctionResultType
   OperationID: GetRelatedContextItemsFunctionResultType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsFunctionResultType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsFunctionResultType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedContextItemsFunctionResultType(requestBody:GetRelatedContextItemsFunctionResultType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelatedContextItemsFunctionResultType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRelatedContextItemsFunctionResultType", {
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
         resolve(data as GetRelatedContextItemsFunctionResultType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelatedContextItemsFuncOper
   OperationID: GetRelatedContextItemsFuncOper
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelatedContextItemsFuncOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedContextItemsFuncOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedContextItemsFuncOper(requestBody:GetRelatedContextItemsFuncOper_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelatedContextItemsFuncOper_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeSvc/GetRelatedContextItemsFuncOper", {
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
         resolve(data as GetRelatedContextItemsFuncOper_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTAmountRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ABTAmountRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTDocLineRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ABTDocLineRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostCodeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ABTPostCodeRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTPostEntityRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ABTPostEntityRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ABTQParamRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ABTQueryRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ABTQueryRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTBookRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ACTBookRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTRevisionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ACTRevisionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ACTTypeListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ACTTypeRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncArgsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BRFuncArgsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFuncOperationRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BRFuncOperationRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BRFunctionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BRFunctionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationCustomRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BROperationCustomRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BROperationRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BROperationRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookValRuleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BookValRuleRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookVarRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BookVarRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BookingRuleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BookingRuleRow,
}

export interface Erp_Tablesets_ABTAmountRow{
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the Document Line.  */  
   "ABTDocLineUID":number,
      /**  Amount UID. Technical identifier.  */  
   "ABTAmountUID":number,
      /**  Identifies the amount element. Application processes use the identifier. This field is display only when the program displays an accounting transaction type used by application programs.  */  
   "Qualifier":string,
      /**  Detailed description of the Amount.  */  
   "Description":string,
      /**  Indicates default Amounts for VBD templates.  */  
   "IsDefault":boolean,
      /**  Reference to the Company.  */  
   "Company":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "DevelopMode":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ABTDocLineRow{
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Document Line UID. Technical identifier.  */  
   "ABTDocLineUID":number,
      /**  Identifies the document line. Various application processes use the identifier.  */  
   "Qualifier":string,
      /**  Indicates default entities for VBD templates.  */  
   "IsDefault":boolean,
      /**  Associated with the document line database table name.  */  
   "DataSource":string,
      /**  Provides a detailed description of the document line.  */  
   "Description":string,
      /**  Reference to the Parent document line.  */  
   "ParentABTDocLineUID":number,
      /**  An order number indicating the document line place in the sequence of lines.  */  
   "SequenceNumber":number,
      /**  Path in VBD structure.  */  
   "DocLinePath":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "DevelopMode":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ABTPostCodeRow{
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the Document Line UID.  */  
   "ABTDocLineUID":number,
      /**  Reference to the Post Entity.  */  
   "ABTPostEntityUID":number,
      /**  Posting Code UID. Technical identifier.  */  
   "ABTPostCodeUID":number,
      /**  Population method for the user-defined field  */  
   "PopulationMethod":number,
      /**  Identifies the posting code. Application processes use the identifier.  */  
   "Qualifier":string,
      /**  Describes the posting code. The description provides information to users of this program.  */  
   "Description":string,
      /**  Associated with the Posting Code database table name.  */  
   "DataSource":string,
      /**  Name of the BAQ or Table field from where the field will be populated in case it is user-defined field  */  
   "DataField":string,
      /**  Indicates default entities for VBD templates.  */  
   "IsDefault":boolean,
      /**  This field stores Posting Code datatype.  */  
   "CodeType":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DBSchemaName  */  
   "DBSchemaName":string,
      /**  Contains Ice.QueryField.Alias  */  
   "BAQDataField":string,
   "BAQDataSource":string,
   "DevelopMode":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "TableDataField":string,
   "TableDataSource":string,
      /**  Contains Ice.QueryField.FieldName  */  
   "BAQDataFieldName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ABTPostEntityRow{
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the Document Line.  */  
   "ABTDocLineUID":number,
      /**  Post Entity UID. Technical identifier.  */  
   "ABTPostEntityUID":number,
      /**  Identifies the entity element. Application processes use the identifier.  */  
   "Qualifier":string,
      /**  Describes the entity. The description provides information to users of this program.  */  
   "Description":string,
      /**  Indicates default entities for VBD templates.  */  
   "IsDefault":boolean,
      /**  An order number indicating the Post Entity place in the sequence of Post Entyties.  */  
   "SequenceNumber":number,
      /**  Indicates if this entity stores keys for reference GLControl.  */  
   "IsReference":boolean,
      /**  Identifies the table used to supply data for posting codes or amount elements that belong to the entity.  */  
   "DataSource":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DBSchemaName  */  
   "DBSchemaName":string,
   "DevelopMode":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ABTQParamRow{
      /**  BAQ Param Link UID.  */  
   "BAQParamLinkUID":number,
      /**  Reference to the Query.  */  
   "ABTQueryUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Paremeter in BAQ.  */  
   "BAQParam":string,
      /**  Parameter from the current Query.  */  
   "ABTBAQParam":string,
      /**  Reference to the Document Line.  */  
   "ABTDocLineUID":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "DevelopMode":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ABTQueryRow{
      /**  Query UID. Technical key.  */  
   "ABTQueryUID":number,
      /**  Reference to Business Activity Query.  */  
   "BAQID":string,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates default Queries for VBD templates.  */  
   "IsDefault":boolean,
      /**  Reference to the Document Line.  */  
   "ABTDocLineUID":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BAQDescription":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "DevelopMode":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ACTBookRow{
      /**  Reference to the Company  */  
   "Company":string,
      /**  Reference to the Book  */  
   "BookID":string,
      /**  Provides a description of the book. This field is display-only.  */  
   "Description":string,
      /**  Currency of the Book  */  
   "BookCurrency":string,
      /**  Type of Book  */  
   "BOOKType":string,
      /**  Reference to the COA  */  
   "COAID":string,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Yes, if Book is Active  */  
   "ActiveFlag":number,
      /**  Yes, If the book is default  */  
   "DefaultBook":boolean,
      /**  Reference to the book, that transaction will be used.  */  
   "MapBookID":string,
      /**  Reference to the COA Map.  */  
   "COAMapUID":number,
      /**  Yes, If mapping will be used.If no- booking rules will be used for creation of transaction.  */  
   "UseMapFlag":boolean,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization
3)     Override  */  
   "Summarize":number,
      /**  Indicates default books for VBD templates.  */  
   "IsDefault":boolean,
      /**  Shows what will be used for transaction creating, 0 - Booking Rules, 1 -  COA Mapping, 2 - Direct  */  
   "MapType":number,
      /**  Transactional currency, Indicates what currency to use in book mapping. [0] -  is document , [1]  is source book's currency, used  in book mapping.  */  
   "TranCurr":number,
      /**  VBD Version  */  
   "ABTVer":string,
      /**  Patch VBD Version  */  
   "PatchABTVer":string,
      /**  Specifies the rule set version. Uses a single numeric sequence and increments every time a rule in the rule set changes.  */  
   "RulesetVer":number,
      /**  Specifies the patch rule set version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  */  
   "PatchRulesetVer":number,
      /**  Package  */  
   "Package":string,
      /**  Indicates that Rulese was modified  */  
   "Modified":boolean,
      /**  Value of Modified filed before last Update versions  */  
   "PrevModified":boolean,
      /**  Indicates that Versions were updated manually  */  
   "ManuallyUpdVer":boolean,
      /**  Indicates that Patch Verstion were updated last time  */  
   "UpdatePatchVer":boolean,
      /**  Specifies the package name (for example, Standard, Extended, Russia) of the assigned rules set (posting rules, functions, and variables) and is used to automatically upgrade rule sets in packages that Epicor supports.  */  
   "BasePackage":string,
      /**  Localization Ruleset Version  */  
   "LocRulesetVer":number,
      /**  Value of LocRulesetVer filed before last Update versions  */  
   "LocPrevRulesetVer":number,
      /**  Localization Patch Ruleset Version  */  
   "LocPatchRulesetVer":number,
      /**  Value of LocPatchRulesetVer filed before last Update versions  */  
   "LocPrevPatchRulesetVer":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Enabling/disabling customization for the Book  */  
   "EnableCustomization":boolean,
      /**  Identifies that ruleset was partially updated during conversion for revision using common dll  */  
   "PartiallyUpdated":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "MapBookCOAID":string,
   "DevelopMode":boolean,
   "DisableBookMapping":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ACTRevisionRow{
      /**  Unique Revision Identifier.  */  
   "ACTRevisionUID":number,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  A user-defined code of revision (unique within one account transaction type).  */  
   "RevisionCode":string,
      /**   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  */  
   "RevisionStatus":string,
      /**  Revision description.  */  
   "Description":string,
      /**  Yes- then all transaction will leave in Review Journal. User must confirm it manually, No - transaction will be created in GLJournal or left in Review Journal if the transaction is not valid.  */  
   "SendToReviewJournal":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates default Revisions for VBD templates.  */  
   "IsDefault":boolean,
      /**  Standard or Exteded  */  
   "RType":string,
      /**  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  */  
   "ABTVer":string,
      /**  Version of build, is used to save time and don't recompile revison each time.  */  
   "VersionUID":number,
      /**  Value of ABTVer field before last Update Versions  */  
   "PrevABTVer":string,
      /**  Patch VBD Version  */  
   "PatchABTVer":string,
      /**  Value of PatchABTVer field before last Update Versions  */  
   "PrevPatchABTVer":string,
      /**  Localization Version  */  
   "LocVer":number,
      /**  Patch Localizasion Version  */  
   "PatchLocVer":number,
      /**  Indicates tha patch version was updated last time  */  
   "UpdatePatchVer":boolean,
      /**  Indicates that Revision data were modified  */  
   "Modified":boolean,
      /**  Value of Modified field before last Update Versions  */  
   "PrevModified":boolean,
      /**  Indicates that Version was updated manually  */  
   "ManuallyUpdVer":boolean,
      /**  Indicates that VBD structure was changed and demand changes in Pre_Post Code  */  
   "NeedPrePostUpdate":boolean,
      /**  Value of RevisionStatus field before last Update Versions  */  
   "PrevRevisionStatus":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates that the Revision was not updated during conversion 'Import GL Transaction Types' because of segment mapping error. After correction Segment Mapping on GL Book Entry, conversion can be run again.  */  
   "PendingConversion":boolean,
      /**  Identifies that common dll can be used for this revision  */  
   "CanUseSysAssembly":boolean,
      /**  Name of posting assembly  */  
   "PostAssemblyName":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ACTTypeListRow{
      /**  Unique GL Transaction Type Identifier.  */  
   "ACTTypeUID":number,
      /**  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  */  
   "DisplayName":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Describes the GL Transaction Type. The description provades information to users of this program  */  
   "DetailedDescription":string,
      /**  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  */  
   "Limited":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ACTTypeRow{
      /**  Unique GL Transaction Type Identifier.  */  
   "ACTTypeUID":number,
      /**  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  */  
   "DisplayName":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Describes the GL Transaction Type. The description provades information to users of this program  */  
   "DetailedDescription":string,
      /**  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  */  
   "Limited":boolean,
      /**  Flag to enable logging of the GL Transaction Type.  */  
   "IsLog":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates that an error occurred during update of the GL Transaction Type in conversion program 'Import GL Transaction Types'  */  
   "ConversionErrors":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "IsLocked":boolean,
   "LockStatus":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BRFuncArgsRow{
      /**  Reference to the Parent function UID.  */  
   "FunctionUID":number,
      /**  Name of function argument  */  
   "ArgName":string,
      /**  Type of function argument  */  
   "ArgType":string,
      /**  Technical name  */  
   "PRGName":string,
      /**  Technical type  */  
   "PRGType":string,
      /**  Reference to the Revision  */  
   "ACTRevisionUID":number,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Unique Argument identifier.  */  
   "ArgumentUID":number,
      /**  Reference to  the company  */  
   "Company":string,
      /**  Indicates default Function Arguments for ABT templates.  */  
   "IsDefault":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "DevelopMode":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BRFuncOperationRow{
      /**  Operation unique ID. Technical identifier.  */  
   "OperationUID":number,
      /**  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  */  
   "ParentOperationUID":number,
      /**  The identifier of the control flow operator.  */  
   "ControlFlowOperator":string,
      /**  The identifier of the target container.  */  
   "Container":string,
      /**  The name of formula.  */  
   "Formula":string,
      /**  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  */  
   "SequenceNumber":number,
      /**  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  */  
   "ChildSequenceNumber":number,
      /**  System ID of used function.  */  
   "FunctionUID":number,
      /**  Technical text of the function(formula)  */  
   "PRGText":string,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Reference to the Function of the GL Transaction Type.  */  
   "FuncOperUID":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  The identifier of the target container.  */  
   "PRGContainer":string,
      /**  Indicates default Function Operations for ABT templates.  */  
   "IsDefault":boolean,
      /**  LocModified  */  
   "LocModified":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DevelopMode":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
      /**  Contains error text in generated code.  */  
   "ErrorText":string,
      /**  Allow use icon easier.  */  
   "IsError":boolean,
      /**  Unified container type for both Operation and Logical Condition types  */  
   "ContainerType":string,
      /**  Indicates 'Logical Condition' type of the operation  */  
   "IsLogicalCondition":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BRFunctionRow{
      /**  Unique Function identifier.  */  
   "FunctionUID":number,
      /**  Name of the function.  */  
   "Name":string,
      /**  Technical name of function  */  
   "PRGName":string,
      /**  If the function is system.  */  
   "IsSystem":boolean,
      /**  Detail description for function.  */  
   "Description":string,
      /**  Type of function result.  */  
   "ResultType":string,
      /**  Technical text of function.  */  
   "PRGPattern":string,
      /**  Reference to the Revisions.  */  
   "ACTRevisionUID":number,
      /**  Reference to the GL Transaction Type  */  
   "ACTTypeUID":number,
      /**  Reference to Book.  */  
   "BookID":string,
      /**  Text of function  */  
   "Formula":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Text field to store the For Each criteria expression .  */  
   "DocLinePath":string,
      /**  Indicates default Functions for ABT templates.  */  
   "IsDefault":boolean,
      /**  ManuallyUpdVer  */  
   "ManuallyUpdVer":boolean,
      /**  Specifies the function version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  */  
   "FuncVer":number,
      /**  PatchFuncVer  */  
   "PatchFuncVer":number,
      /**  PrevModified  */  
   "PrevModified":boolean,
      /**  Modified  */  
   "Modified":boolean,
      /**  LocVer  */  
   "LocVer":number,
      /**  LocPatchVer  */  
   "LocPatchVer":number,
      /**  LocModified  */  
   "LocModified":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "DevelopMode":boolean,
      /**  Is used to show icon in Tree.  */  
   "IsError":boolean,
      /**  Contains error text for a function.  */  
   "ErrorText":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BROperationCustomRow{
      /**  Company Indetifier.  */  
   "Company":string,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the Book.  */  
   "BookID":string,
      /**  Reference to the parent booking rule.  */  
   "RuleUID":number,
      /**  Operation unique ID. Technical identifier.  */  
   "OperationUID":number,
      /**  Reference to the parent operation  */  
   "ParentOperationUID":number,
      /**  An order number indicating the operation’s place in the sequence of execution.  */  
   "ChildSequenceNumber":number,
      /**  The identifier of the control flow operator.  */  
   "ControlFlowOperator":string,
      /**  The identifier of the target container.  */  
   "Container":string,
      /**  The operation's main formula.  */  
   "Formula":string,
      /**  Function unique ID.  */  
   "FunctionUID":number,
      /**  Code for operation  */  
   "PRGText":string,
      /**  The identifier of the target container.  */  
   "PRGContainer":string,
      /**  Audit column. Populate UserID who created the row.  */  
   "CreatedBy":string,
      /**  Audit column. Populate time of creation row.  */  
   "CreatedOn":string,
      /**  Audit column. Populate UserID of last person who updated the row.  */  
   "ChangedBy":string,
      /**  Audit column. Populate time of updating the row.  */  
   "ChangedOn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
      /**  Contains error text in generated code.  */  
   "ErrorText":string,
      /**  Allow use icon easier.  */  
   "IsError":boolean,
      /**  Unified container type for both Operation and Logical Condition types  */  
   "ContainerType":string,
      /**  Indicates 'Logical Condition' type of the operation  */  
   "IsLogicalCondition":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BROperationRow{
      /**  Operation unique ID. Technical identifier.  */  
   "OperationUID":number,
      /**  Reference to the parent booking rule.  */  
   "RuleUID":number,
      /**  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  */  
   "ParentOperationUID":number,
      /**  The identifier of the control flow operator.  */  
   "ControlFlowOperator":string,
      /**  The identifier of the target container.  */  
   "Container":string,
      /**  The operation's main formula.  */  
   "Formula":string,
      /**  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  */  
   "SequenceNumber":number,
      /**  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  */  
   "ChildSequenceNumber":number,
      /**  Function unique ID. Technical identifier.  */  
   "FunctionUID":number,
      /**  Progress Code for operation  */  
   "PRGText":string,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  The identifier of the target container.  */  
   "PRGContainer":string,
      /**  Reference to the Book.  */  
   "BookID":string,
      /**  Indicates default Operations for ABT templates.  */  
   "IsDefault":boolean,
      /**  LocModified  */  
   "LocModified":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Unified container type for both Operation and Logical Condition types  */  
   "ContainerType":string,
   "DevelopMode":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
      /**  Contains error text in generated code.  */  
   "ErrorText":string,
      /**  Allow use icon easier.  */  
   "IsError":boolean,
      /**  Field to support functionality of link-combo in Kinetic (Container in operations)  */  
   "LLink01":string,
      /**  Indicates 'Logical Condition' type of the operation  */  
   "IsLogicalCondition":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BookValRuleRow{
      /**  Unique value.Primary key  */  
   "BVRuleUID":number,
      /**  Technical key of Validation Rule  */  
   "VRuleUID":number,
      /**  Validation rule description  */  
   "Description":string,
      /**  Error, Ignor, Warning, Autocorrect, Autocorrect with warning  */  
   "Action":string,
      /**  Validation level : Book, Booking Rule, Company etc  */  
   "VLevel":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Reference to Book.  */  
   "BookID":string,
      /**  Account transaction type UID. Technical identifier.  */  
   "ACTTypeUID":number,
      /**  Reference to the parent account transaction revision.  */  
   "ACTRevisionUID":number,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Indicates default validation rules for ABT templates.  */  
   "IsDefault":boolean,
      /**  List of actions (used in combo boxes).  */  
   "ActionList":string,
      /**  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  */  
   "RuleType":string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
   "DevelopMode":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BookVarRow{
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Reference to the Book  */  
   "BookID":string,
      /**  BookVar unique ID.  */  
   "BookVarUID":number,
      /**  Variable Name  */  
   "VarName":string,
      /**  Variable Type  */  
   "VarType":string,
      /**  Variable context, possible values: Global, Book, Rule, Function.  */  
   "vType":string,
      /**  ID of context, for example if vType = Function then vUID = FunctionUID.  */  
   "vUID":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates default Variables for VBD templates.  */  
   "IsDefault":boolean,
      /**  LocModified  */  
   "LocModified":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DevelopMode":boolean,
      /**  the field is used for generation post program  */  
   "isSystem":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
      /**  Function or Rule Description.  */  
   "OwnerDescription":string,
      /**  VarType display.  */  
   "VarTypeDisplay":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BookingRuleRow{
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**  Reference to the Revision.  */  
   "ACTRevisionUID":number,
      /**  Booking rule name to be displayed in the tree view navigation control.  */  
   "DisplayName":string,
      /**  Booking rule detailed description.  */  
   "DetailedDescription":string,
      /**  Text field to store the selection criteria expression .  */  
   "SelectionCriteria":string,
      /**  Reference to the Book.  */  
   "BookID":string,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  It is Rule for Posting process or special for GLControl calculation.  */  
   "IsPost":boolean,
      /**  Text field to store the For Each criteria expression .  */  
   "ForEach":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Rule run once, usual it is used for calculation Book variables or Header variables (that can be calculated once).  */  
   "IsHeader":boolean,
      /**  Determines whether the posting process uses the rule.  */  
   "IsActive":boolean,
      /**  Stores a reference to a credit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing..  */  
   "CreditContext":string,
      /**  Stores a reference to a debit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing.  */  
   "DebitContext":string,
      /**  Reference  Context is used for pre-Posting rules  */  
   "RefContext":string,
      /**  Determines the GL control type that applies to the rule. The control type affects the processing of accounts generated by the rule. Pre-posting GL controls use the type to determine the reference context, used to set the default for a GL account field. The type also controls the credit and debit contexts for posting rules.  */  
   "GLControlType":string,
      /**  Indicates default Rules for ABT templates.  */  
   "IsDefault":boolean,
      /**  Primary key from the Entity is a source of keys for TranGLC table that save Reference control of the Booking Rule.  */  
   "Entity":string,
      /**  IsReference  */  
   "IsReference":boolean,
      /**  Indicates that Versions were updated manually  */  
   "ManuallyUpdVer":boolean,
      /**  Specifies the individual rule version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  */  
   "RuleVer":number,
      /**  Specifies the individual rule patch version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  */  
   "PatchRuleVer":number,
      /**  Value of Modified field before last Update Versions  */  
   "PrevModified":boolean,
      /**  Indicates that data were modified  */  
   "Modified":boolean,
      /**  LocVer  */  
   "LocVer":number,
      /**  LocPatchVer  */  
   "LocPatchVer":number,
      /**  LocModified  */  
   "LocModified":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Enabling/disabling customization for the Book  */  
   "EnableCustomization":boolean,
      /**  Indicates that base information on rule was changed. In this case this rule will not be automatically updated during converstion program to save user's changes.  */  
   "BaseModified":boolean,
      /**  Indicates that rule contaion operations on 'Customization' part  */  
   "Customization":boolean,
      /**  Used to bind UI control.  */  
   "Operator":string,
      /**  Selection Criteria Display.  */  
   "SelCriteriaDisplay":string,
      /**  Used to bind UI control.  */  
   "Argument":string,
   "DevelopMode":boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   "Loaded":number,
      /**  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  */  
   "RuleType":string,
      /**  Is used to show icon in Tree.  */  
   "IsError":boolean,
      /**  Contains error text for a rule.  */  
   "ErrorText":string,
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
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param ds
   */  
export interface ABTBookGetNewExt_input{
   actTypeUID:number,
   actRevisionUID:number,
   bookID:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ABTBookGetNewExt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param ds
   */  
export interface ABTBookGetNew_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  Book ID  */  
   bookID:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ABTBookGetNew_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param parentAbtDocLineUID
      @param ds
   */  
export interface ABTDocLineGetNew_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  Parent ABTDocLineUID  */  
   parentAbtDocLineUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ABTDocLineGetNew_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param abtDocLineUID
      @param abtPostEntityUID
      @param developMode
      @param ds
   */  
export interface ABTPostCodeGetNew_input{
      /**  actTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  abtDocLineUID  */  
   abtDocLineUID:number,
      /**  abtPostEntityUID  */  
   abtPostEntityUID:number,
      /**  Developer Mode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ABTPostCodeGetNew_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param mapBookID
      @param scrBookID
      @param coaMapUID
      @param tranCurr
   */  
export interface AddMappedBook_input{
      /**  act TypeUID  */  
   actTypeUID:number,
      /**  ACT RevisionUID  */  
   actRevisionUID:number,
      /**  map BookID  */  
   mapBookID:string,
      /**  scr BookID  */  
   scrBookID:string,
      /**  coa MapUID  */  
   coaMapUID:number,
      /**  tran Curr  */  
   tranCurr:number,
}

export interface AddMappedBook_output{
parameters : {
      /**  output parameters  */  
   newRevUID:number,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookIDList
      @param ds
   */  
export interface AddMultipleBooks_input{
   actTypeUID:number,
   actRevisionUID:number,
      /**  "~" separated list of books  */  
   bookIDList:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface AddMultipleBooks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param developMode
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookID
      @param ds
   */  
export interface AfterDeleteBookItem_input{
      /**  DevelopMode flag  */  
   developMode:boolean,
      /**  ACTTypeUID of deleted row  */  
   aCTTypeUID:number,
      /**  ACTRevisionUID of deleted row  */  
   aCTRevisionUID:number,
      /**  BookID of deleted row  */  
   bookID:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface AfterDeleteBookItem_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param developMode
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookID
      @param functionUID
      @param ds
   */  
export interface AfterDeleteFunctionItem_input{
      /**  DevelopMode flag  */  
   developMode:boolean,
      /**  ACTTypeUID of deleted row  */  
   aCTTypeUID:number,
      /**  ACTRevisionUID of deleted row  */  
   aCTRevisionUID:number,
      /**  BookID of deleted row  */  
   bookID:string,
      /**  FunctionUID of deleted row  */  
   functionUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface AfterDeleteFunctionItem_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param developMode
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookID
      @param ruleUID
      @param ds
   */  
export interface AfterDeleteRuleItem_input{
      /**  DevelopMode flag  */  
   developMode:boolean,
      /**  ACTTypeUID of deleted row  */  
   aCTTypeUID:number,
      /**  ACTRevisionUID of deleted row  */  
   aCTRevisionUID:number,
      /**  BookID of deleted row  */  
   bookID:string,
      /**  RuleUID of deleted row  */  
   ruleUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface AfterDeleteRuleItem_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param developMode
      @param aCTTypeUID
      @param aCTRevisionUID
      @param ds
   */  
export interface AfterDeleteVBDItem_input{
      /**  DevelopMode flag  */  
   developMode:boolean,
      /**  ACTTypeUID of deleted row  */  
   aCTTypeUID:number,
      /**  ACTRevisionUID of deleted row  */  
   aCTRevisionUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface AfterDeleteVBDItem_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param proposedValue
      @param BAQID
      @param ds
   */  
export interface BAQDataFieldChanging_input{
   proposedValue:string,
   BAQID:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BAQDataFieldChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param functionUID
      @param operationUID
      @param chldSequenceNumber
      @param ds
   */  
export interface BRFuncOperationGetNew_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  functionUID  */  
   functionUID:number,
      /**  operationUID  */  
   operationUID:number,
      /**  childSequenceNumber  */  
   chldSequenceNumber:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BRFuncOperationGetNew_output{
parameters : {
      /**  output parameters  */  
   chldSequenceNumber:number,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param sTypeFull
      @param lcdsContainer
      @param dsSub
      @param ds
   */  
export interface BRFuncOperationUpdateContainerFormula_input{
   sTypeFull:string,
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BRFuncOperationUpdateContainerFormula_output{
parameters : {
      /**  output parameters  */  
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param sTypeFull
      @param lcdsContainer
      @param dsSub
      @param ds
   */  
export interface BRFuncOperationUpdateContainer_input{
   sTypeFull:string,
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BRFuncOperationUpdateContainer_output{
parameters : {
      /**  output parameters  */  
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param elementOrderEdited
      @param direction
      @param ds
      @param dsSub
   */  
export interface BRFunctionPhraseElementMove_input{
      /**  the value in the Order field of the edited column  */  
   elementOrderEdited:number,
      /**  movement direction 0 - move down, 1 - move ap  */  
   direction:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
}

export interface BRFunctionPhraseElementMove_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
}
}

   /** Required : 
      @param ds
      @param dsSub
   */  
export interface BRFunctionPhraseUpdate_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
}

export interface BRFunctionPhraseUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
}
}

   /** Required : 
      @param sTypeFull
      @param lcdsContainer
      @param dsSub
      @param ds
   */  
export interface BROPerationCustomUpdateContainerFormula_input{
   sTypeFull:string,
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BROPerationCustomUpdateContainerFormula_output{
parameters : {
      /**  output parameters  */  
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param ruleUID
      @param operationUID
      @param chldSequenceNumber
      @param ds
   */  
export interface BROperationCustomGetNew_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  ruleUID  */  
   ruleUID:number,
      /**  operationUID  */  
   operationUID:number,
      /**  childSequenceNumber  */  
   chldSequenceNumber:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BROperationCustomGetNew_output{
parameters : {
      /**  output parameters  */  
   chldSequenceNumber:number,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param sTypeFull
      @param lcdsContainer
      @param dsSub
      @param ds
   */  
export interface BROperationCustomUpdateContainer_input{
   sTypeFull:string,
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BROperationCustomUpdateContainer_output{
parameters : {
      /**  output parameters  */  
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param ruleUID
      @param operationUID
      @param chldSequenceNumber
      @param ds
   */  
export interface BROperationGetNew_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  ruleUID  */  
   ruleUID:number,
      /**  operationUID  */  
   operationUID:number,
      /**  childSequenceNumber  */  
   chldSequenceNumber:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BROperationGetNew_output{
parameters : {
      /**  output parameters  */  
   chldSequenceNumber:number,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param sTypeFull
      @param lcdsContainer
      @param dsSub
      @param ds
   */  
export interface BROperationUpdateContainerFormula_input{
   sTypeFull:string,
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BROperationUpdateContainerFormula_output{
parameters : {
      /**  output parameters  */  
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param sTypeFull
      @param lcdsContainer
      @param dsSub
      @param ds
   */  
export interface BROperationUpdateContainer_input{
   sTypeFull:string,
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BROperationUpdateContainer_output{
parameters : {
      /**  output parameters  */  
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
   */  
export interface BookIsNotEmpty_input{
      /**  actTypeUID  */  
   actTypeUID:number,
      /**  iACTRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
}

export interface BookIsNotEmpty_output{
   returnObj:boolean,
}

   /** Required : 
      @param proposedValue
      @param column
      @param ds
   */  
export interface BookVarNameTypeChanging_input{
   proposedValue:string,
      /**  Name or type  */  
   column:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BookVarNameTypeChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface BookVarOwnerChanging_input{
   proposedValue:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BookVarOwnerChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param vType
      @param vUID
      @param developMode
      @param ds
   */  
export interface BookVariableGetNew_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  vType  */  
   vType:string,
      /**  vUID  */  
   vUID:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BookVariableGetNew_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param isPost
      @param isRef
      @param ds
   */  
export interface BookingRuleGetNew_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  Is Post Rule  */  
   isPost:boolean,
      /**  Is Reference Rule  */  
   isRef:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface BookingRuleGetNew_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param cACTTypeName
      @param cABTVer
      @param cPatchABTVer
   */  
export interface CanActivateRevision_input{
      /**  ACTType Display Name  */  
   cACTTypeName:string,
      /**  ABT Version  */  
   cABTVer:string,
      /**  Patch ABT Version  */  
   cPatchABTVer:string,
}

export interface CanActivateRevision_output{
   returnObj:boolean,
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param abtDocLineUID
      @param abtQueryUID
      @param baqName
      @param ds
   */  
export interface ChangeBAQ_input{
      /**  actTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  abtDocLineUID  */  
   abtDocLineUID:number,
      /**  abtQueryUID  */  
   abtQueryUID:number,
      /**  baqName  */  
   baqName:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ChangeBAQ_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param companyName
      @param iACTTypeUID
      @param iACTRevisionUID
      @param cStatus
      @param ds
   */  
export interface ChangeRevisionStatusMode_input{
      /**  CompanyName  */  
   companyName:string,
      /**  iACTTypeUID  */  
   iACTTypeUID:number,
      /**  iACTRevisionUID  */  
   iACTRevisionUID:number,
      /**  Status  */  
   cStatus:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ChangeRevisionStatusMode_output{
parameters : {
      /**  output parameters  */  
   lNeedRefresh:boolean,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param baqid
   */  
export interface CheckBAQExists_input{
      /**  BAQ Id  */  
   baqid:string,
}

export interface CheckBAQExists_output{
parameters : {
      /**  output parameters  */  
   isexisted:boolean,
}
}

   /** Required : 
      @param companyName
      @param iACTTypeUID
      @param iACTRevisionUID
   */  
export interface CheckBeforeActivateRevision_input{
      /**  CompanyName  */  
   companyName:string,
      /**  iACTTypeUID  */  
   iACTTypeUID:number,
      /**  iACTRevisionUID  */  
   iACTRevisionUID:number,
}

export interface CheckBeforeActivateRevision_output{
parameters : {
      /**  output parameters  */  
   cError:string,
   cWarning:string,
}
}

   /** Required : 
      @param companyName
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookId
      @param functionUID
      @param ds
   */  
export interface CheckSyntaxFunction_input{
   companyName:string,
   aCTTypeUID:number,
   aCTRevisionUID:number,
   bookId:string,
   functionUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface CheckSyntaxFunction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
   errorsExist:boolean,
}
}

   /** Required : 
      @param companyName
      @param aCTTypeUID
      @param aCTRevisionUID
      @param ds
   */  
export interface CheckSyntaxRevision_input{
   companyName:string,
   aCTTypeUID:number,
   aCTRevisionUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface CheckSyntaxRevision_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
   errorsExist:boolean,
   errorInFunction:boolean,
   errorFirstUID:number,
}
}

   /** Required : 
      @param companyName
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookId
      @param ruleUID
      @param ds
   */  
export interface CheckSyntaxRule_input{
   companyName:string,
   aCTTypeUID:number,
   aCTRevisionUID:number,
   bookId:string,
   ruleUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface CheckSyntaxRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
   errorsExist:boolean,
}
}

   /** Required : 
      @param GPostingUID
      @param NodeID
   */  
export interface CompareRevisions_input{
      /**  A ~ (tilde) separated list consisting of:
            0 = ACTTypeUID
            1 = Revision 1 name
            2 = Revision 2 name  */  
   GPostingUID:string,
      /**  Not currently used  */  
   NodeID:string,
}

export interface CompareRevisions_output{
      /**  Tree Object  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param listOfFuncUID
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param destinationACTTypeUID
      @param destinationRevisionUID
      @param destinationBookUID
      @param developMode
   */  
export interface CopyListOfFunctionsWithWarn_input{
      /**  List UIDs of copied Functions  */  
   listOfFuncUID:string,
      /**  Source ACTTypeUID  */  
   actTypeUID:number,
      /**  Source ACTRevisionUID  */  
   actRevisionUID:number,
      /**  Source BookID  */  
   bookID:string,
      /**  identifier of destination ActType  */  
   destinationACTTypeUID:number,
      /**  identifier of destination revision  */  
   destinationRevisionUID:number,
      /**  identifier of destination book  */  
   destinationBookUID:string,
      /**  Developer Mode  */  
   developMode:boolean,
}

export interface CopyListOfFunctionsWithWarn_output{
parameters : {
      /**  output parameters  */  
   warnMessage:string,
}
}

   /** Required : 
      @param listOfFuncUID
      @param destinationACTTypeUID
      @param destinationRevisionUID
      @param destinationBookUID
   */  
export interface CopyListOfFunctions_input{
      /**  listOfFuncUID  */  
   listOfFuncUID:string,
      /**  identifier of destination ActType  */  
   destinationACTTypeUID:number,
      /**  identifier of destination revision  */  
   destinationRevisionUID:number,
      /**  identifier of destination book  */  
   destinationBookUID:string,
}

export interface CopyListOfFunctions_output{
}

   /** Required : 
      @param listOfRuleUID
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param destinationACTTypeUID
      @param destinationRevisionUID
      @param destinationBookUID
      @param developMode
   */  
export interface CopyListOfRulesWithWarn_input{
      /**  listOfRuleUID  */  
   listOfRuleUID:string,
      /**  source actTypeUID  */  
   actTypeUID:number,
      /**  source actRevisionUID  */  
   actRevisionUID:number,
      /**  source BookID  */  
   bookID:string,
      /**  identifier of destination ActType  */  
   destinationACTTypeUID:number,
      /**  identifier of destination revision  */  
   destinationRevisionUID:number,
      /**  identifier of destination book  */  
   destinationBookUID:string,
      /**  development mode  */  
   developMode:boolean,
}

export interface CopyListOfRulesWithWarn_output{
parameters : {
      /**  output parameters  */  
   warnMessage:string,
}
}

   /** Required : 
      @param listOfRuleUID
      @param destinationACTTypeUID
      @param destinationRevisionUID
      @param destinationBookUID
   */  
export interface CopyListOfRules_input{
      /**  listOfRuleUID  */  
   listOfRuleUID:string,
      /**  identifier of destination ActType  */  
   destinationACTTypeUID:number,
      /**  identifier of destination revision  */  
   destinationRevisionUID:number,
      /**  identifier of destination book  */  
   destinationBookUID:string,
}

export interface CopyListOfRules_output{
}

   /** Required : 
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookID
      @param ruleUID
      @param functionUID
      @param operationUID
      @param isCustomOp
      @param destACTTypeUID
      @param destACTRevisionUID
      @param destBookID
      @param destRuleUID
      @param destFunctionUID
      @param destOperationUID
      @param destIsCustomOp
      @param bMulti
      @param bMove
      @param developMode
      @param copyDs
      @param ds
   */  
export interface CopyOperations_input{
      /**  source ACTTypeUID  */  
   aCTTypeUID:number,
      /**  source ACTRevisionUID  */  
   aCTRevisionUID:number,
      /**  source bookID  */  
   bookID:string,
      /**  source RuleUID  */  
   ruleUID:number,
      /**  source FunctionUID  */  
   functionUID:number,
      /**  OperationUID. If this value is zero then all operations of rule/function will be copied.  */  
   operationUID:number,
      /**  Copy from custom operations  */  
   isCustomOp:boolean,
      /**  ACTTypeUID destination  */  
   destACTTypeUID:number,
      /**  ACTRevisionUID destination  */  
   destACTRevisionUID:number,
      /**  destBookID  */  
   destBookID:string,
      /**  RuleUID destination  */  
   destRuleUID:number,
      /**  FunctionUID destination  */  
   destFunctionUID:number,
      /**  identifier of destination operation  */  
   destOperationUID:number,
      /**  Copy to custom operations  */  
   destIsCustomOp:boolean,
      /**  Multi Copy  */  
   bMulti:boolean,
      /**  Move  */  
   bMove:boolean,
      /**  DevelopMode  */  
   developMode:boolean,
   copyDs:Erp_Tablesets_ACTTypeCopyPasteTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface CopyOperations_output{
parameters : {
      /**  output parameters  */  
   warnMessage:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CustomUpdate_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface CustomUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookID
      @param developMode
   */  
export interface DeleteACTBook_input{
      /**  aCTTypeUID  */  
   aCTTypeUID:number,
      /**  aCTRevisionUID  */  
   aCTRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  DevelopMode  */  
   developMode:boolean,
}

export interface DeleteACTBook_output{
}

   /** Required : 
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookID
      @param ruleUID
      @param operationUID
      @param bMulti
      @param ds
   */  
export interface DeleteBROperationCustom_input{
      /**  ACTTypeUID  */  
   aCTTypeUID:number,
      /**  ACTRevisionUID  */  
   aCTRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  RuleUID  */  
   ruleUID:number,
      /**  OperationUID. If value is zero then remove all operations from rule customizaion.  */  
   operationUID:number,
      /**  Multi Delete  */  
   bMulti:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface DeleteBROperationCustom_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param acTTypeUID
   */  
export interface DeleteByID_input{
   acTTypeUID:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param mapBookID
   */  
export interface DeleteMappedBook_input{
      /**  act TypeUID  */  
   actTypeUID:number,
      /**  ACT RevisionUID  */  
   actRevisionUID:number,
      /**  map BookID  */  
   mapBookID:string,
}

export interface DeleteMappedBook_output{
parameters : {
      /**  output parameters  */  
   newRevUID:number,
}
}

   /** Required : 
      @param aCTTypeUID
      @param aCTRevisionUID
      @param bookID
      @param ruleUID
      @param functionUID
      @param operationUID
      @param bMulti
      @param developMode
      @param ds
   */  
export interface DeleteOpItems_input{
      /**  ACTTypeUID  */  
   aCTTypeUID:number,
      /**  ACTRevisionUID  */  
   aCTRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  RuleUID  */  
   ruleUID:number,
      /**  FunctionUID  */  
   functionUID:number,
      /**  OperationUID. If value is zero then remove all base operations from rule/function.  */  
   operationUID:number,
      /**  Multi Delete  */  
   bMulti:boolean,
      /**  DevelopMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface DeleteOpItems_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param acttypeUID
      @param revisionCode
      @param compList
   */  
export interface DeleteRevisionByName_input{
      /**  ACTType ACTTypeUID  */  
   acttypeUID:number,
      /**  ACTRevision Revision Code  */  
   revisionCode:string,
      /**  Companies List  */  
   compList:string,
}

export interface DeleteRevisionByName_output{
}

   /** Required : 
      @param typeName
      @param compList
   */  
export interface DeleteRevsBeforeImport_input{
      /**  ACTType Display Name  */  
   typeName:string,
      /**  Companies List  */  
   compList:string,
}

export interface DeleteRevsBeforeImport_output{
}

export interface Erp_Tablesets_ABTAmountRow{
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the Document Line.  */  
   ABTDocLineUID:number,
      /**  Amount UID. Technical identifier.  */  
   ABTAmountUID:number,
      /**  Identifies the amount element. Application processes use the identifier. This field is display only when the program displays an accounting transaction type used by application programs.  */  
   Qualifier:string,
      /**  Detailed description of the Amount.  */  
   Description:string,
      /**  Indicates default Amounts for VBD templates.  */  
   IsDefault:boolean,
      /**  Reference to the Company.  */  
   Company:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   DevelopMode:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ABTDocLineRow{
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Document Line UID. Technical identifier.  */  
   ABTDocLineUID:number,
      /**  Identifies the document line. Various application processes use the identifier.  */  
   Qualifier:string,
      /**  Indicates default entities for VBD templates.  */  
   IsDefault:boolean,
      /**  Associated with the document line database table name.  */  
   DataSource:string,
      /**  Provides a detailed description of the document line.  */  
   Description:string,
      /**  Reference to the Parent document line.  */  
   ParentABTDocLineUID:number,
      /**  An order number indicating the document line place in the sequence of lines.  */  
   SequenceNumber:number,
      /**  Path in VBD structure.  */  
   DocLinePath:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   DevelopMode:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ABTPostCodeRow{
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the Document Line UID.  */  
   ABTDocLineUID:number,
      /**  Reference to the Post Entity.  */  
   ABTPostEntityUID:number,
      /**  Posting Code UID. Technical identifier.  */  
   ABTPostCodeUID:number,
      /**  Population method for the user-defined field  */  
   PopulationMethod:number,
      /**  Identifies the posting code. Application processes use the identifier.  */  
   Qualifier:string,
      /**  Describes the posting code. The description provides information to users of this program.  */  
   Description:string,
      /**  Associated with the Posting Code database table name.  */  
   DataSource:string,
      /**  Name of the BAQ or Table field from where the field will be populated in case it is user-defined field  */  
   DataField:string,
      /**  Indicates default entities for VBD templates.  */  
   IsDefault:boolean,
      /**  This field stores Posting Code datatype.  */  
   CodeType:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DBSchemaName  */  
   DBSchemaName:string,
      /**  Contains Ice.QueryField.Alias  */  
   BAQDataField:string,
   BAQDataSource:string,
   DevelopMode:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   TableDataField:string,
   TableDataSource:string,
      /**  Contains Ice.QueryField.FieldName  */  
   BAQDataFieldName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ABTPostEntityRow{
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the Document Line.  */  
   ABTDocLineUID:number,
      /**  Post Entity UID. Technical identifier.  */  
   ABTPostEntityUID:number,
      /**  Identifies the entity element. Application processes use the identifier.  */  
   Qualifier:string,
      /**  Describes the entity. The description provides information to users of this program.  */  
   Description:string,
      /**  Indicates default entities for VBD templates.  */  
   IsDefault:boolean,
      /**  An order number indicating the Post Entity place in the sequence of Post Entyties.  */  
   SequenceNumber:number,
      /**  Indicates if this entity stores keys for reference GLControl.  */  
   IsReference:boolean,
      /**  Identifies the table used to supply data for posting codes or amount elements that belong to the entity.  */  
   DataSource:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DBSchemaName  */  
   DBSchemaName:string,
   DevelopMode:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ABTQParamRow{
      /**  BAQ Param Link UID.  */  
   BAQParamLinkUID:number,
      /**  Reference to the Query.  */  
   ABTQueryUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Paremeter in BAQ.  */  
   BAQParam:string,
      /**  Parameter from the current Query.  */  
   ABTBAQParam:string,
      /**  Reference to the Document Line.  */  
   ABTDocLineUID:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   DevelopMode:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ABTQueryRow{
      /**  Query UID. Technical key.  */  
   ABTQueryUID:number,
      /**  Reference to Business Activity Query.  */  
   BAQID:string,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates default Queries for VBD templates.  */  
   IsDefault:boolean,
      /**  Reference to the Document Line.  */  
   ABTDocLineUID:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BAQDescription:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   DevelopMode:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTBookRow{
      /**  Reference to the Company  */  
   Company:string,
      /**  Reference to the Book  */  
   BookID:string,
      /**  Provides a description of the book. This field is display-only.  */  
   Description:string,
      /**  Currency of the Book  */  
   BookCurrency:string,
      /**  Type of Book  */  
   BOOKType:string,
      /**  Reference to the COA  */  
   COAID:string,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Yes, if Book is Active  */  
   ActiveFlag:number,
      /**  Yes, If the book is default  */  
   DefaultBook:boolean,
      /**  Reference to the book, that transaction will be used.  */  
   MapBookID:string,
      /**  Reference to the COA Map.  */  
   COAMapUID:number,
      /**  Yes, If mapping will be used.If no- booking rules will be used for creation of transaction.  */  
   UseMapFlag:boolean,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization
3)     Override  */  
   Summarize:number,
      /**  Indicates default books for VBD templates.  */  
   IsDefault:boolean,
      /**  Shows what will be used for transaction creating, 0 - Booking Rules, 1 -  COA Mapping, 2 - Direct  */  
   MapType:number,
      /**  Transactional currency, Indicates what currency to use in book mapping. [0] -  is document , [1]  is source book's currency, used  in book mapping.  */  
   TranCurr:number,
      /**  VBD Version  */  
   ABTVer:string,
      /**  Patch VBD Version  */  
   PatchABTVer:string,
      /**  Specifies the rule set version. Uses a single numeric sequence and increments every time a rule in the rule set changes.  */  
   RulesetVer:number,
      /**  Specifies the patch rule set version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  */  
   PatchRulesetVer:number,
      /**  Package  */  
   Package:string,
      /**  Indicates that Rulese was modified  */  
   Modified:boolean,
      /**  Value of Modified filed before last Update versions  */  
   PrevModified:boolean,
      /**  Indicates that Versions were updated manually  */  
   ManuallyUpdVer:boolean,
      /**  Indicates that Patch Verstion were updated last time  */  
   UpdatePatchVer:boolean,
      /**  Specifies the package name (for example, Standard, Extended, Russia) of the assigned rules set (posting rules, functions, and variables) and is used to automatically upgrade rule sets in packages that Epicor supports.  */  
   BasePackage:string,
      /**  Localization Ruleset Version  */  
   LocRulesetVer:number,
      /**  Value of LocRulesetVer filed before last Update versions  */  
   LocPrevRulesetVer:number,
      /**  Localization Patch Ruleset Version  */  
   LocPatchRulesetVer:number,
      /**  Value of LocPatchRulesetVer filed before last Update versions  */  
   LocPrevPatchRulesetVer:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Enabling/disabling customization for the Book  */  
   EnableCustomization:boolean,
      /**  Identifies that ruleset was partially updated during conversion for revision using common dll  */  
   PartiallyUpdated:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   MapBookCOAID:string,
   DevelopMode:boolean,
   DisableBookMapping:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTRevisionRow{
      /**  Unique Revision Identifier.  */  
   ACTRevisionUID:number,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  A user-defined code of revision (unique within one account transaction type).  */  
   RevisionCode:string,
      /**   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  */  
   RevisionStatus:string,
      /**  Revision description.  */  
   Description:string,
      /**  Yes- then all transaction will leave in Review Journal. User must confirm it manually, No - transaction will be created in GLJournal or left in Review Journal if the transaction is not valid.  */  
   SendToReviewJournal:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates default Revisions for VBD templates.  */  
   IsDefault:boolean,
      /**  Standard or Exteded  */  
   RType:string,
      /**  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  */  
   ABTVer:string,
      /**  Version of build, is used to save time and don't recompile revison each time.  */  
   VersionUID:number,
      /**  Value of ABTVer field before last Update Versions  */  
   PrevABTVer:string,
      /**  Patch VBD Version  */  
   PatchABTVer:string,
      /**  Value of PatchABTVer field before last Update Versions  */  
   PrevPatchABTVer:string,
      /**  Localization Version  */  
   LocVer:number,
      /**  Patch Localizasion Version  */  
   PatchLocVer:number,
      /**  Indicates tha patch version was updated last time  */  
   UpdatePatchVer:boolean,
      /**  Indicates that Revision data were modified  */  
   Modified:boolean,
      /**  Value of Modified field before last Update Versions  */  
   PrevModified:boolean,
      /**  Indicates that Version was updated manually  */  
   ManuallyUpdVer:boolean,
      /**  Indicates that VBD structure was changed and demand changes in Pre_Post Code  */  
   NeedPrePostUpdate:boolean,
      /**  Value of RevisionStatus field before last Update Versions  */  
   PrevRevisionStatus:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that the Revision was not updated during conversion 'Import GL Transaction Types' because of segment mapping error. After correction Segment Mapping on GL Book Entry, conversion can be run again.  */  
   PendingConversion:boolean,
      /**  Identifies that common dll can be used for this revision  */  
   CanUseSysAssembly:boolean,
      /**  Name of posting assembly  */  
   PostAssemblyName:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTTypeCopyPasteTableset{
   BRFuncOperation:Erp_Tablesets_BRFuncOperationRow[],
   BROperation:Erp_Tablesets_BROperationRow[],
   BROperationCustom:Erp_Tablesets_BROperationCustomRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ACTTypeImportBookTableset{
   ACTTypeImportComp:Erp_Tablesets_ACTTypeImportCompRow[],
   COASegmentNameList:Erp_Tablesets_COASegmentNameListRow[],
   GLBookList:Erp_Tablesets_GLBookListRow[],
   GLBookPackageSegmentMap:Erp_Tablesets_GLBookPackageSegmentMapRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ACTTypeImportCompRow{
   Company:string,
      /**  Indicates that import shoulc be done for this Company  */  
   Selected:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTTypeImportOpTableset{
   ACTTypeImportComp:Erp_Tablesets_ACTTypeImportCompRow[],
   GLBookMap:Erp_Tablesets_GLBookMapRow[],
   GLSegmentMap:Erp_Tablesets_GLSegmentMapRow[],
   RevisionImportOp:Erp_Tablesets_RevisionImportOpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ACTTypeListRow{
      /**  Unique GL Transaction Type Identifier.  */  
   ACTTypeUID:number,
      /**  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  */  
   DisplayName:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Describes the GL Transaction Type. The description provades information to users of this program  */  
   DetailedDescription:string,
      /**  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  */  
   Limited:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTTypeListTableset{
   ACTTypeList:Erp_Tablesets_ACTTypeListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ACTTypeRow{
      /**  Unique GL Transaction Type Identifier.  */  
   ACTTypeUID:number,
      /**  Name of the GL Tranaction Type to be displayed in the tree view navigation control.  */  
   DisplayName:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Describes the GL Transaction Type. The description provades information to users of this program  */  
   DetailedDescription:string,
      /**  Yes - if the transaction type has not VBD and Booking Rules,has just one Active Revision. Posting in this case is hard coded.  */  
   Limited:boolean,
      /**  Flag to enable logging of the GL Transaction Type.  */  
   IsLog:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that an error occurred during update of the GL Transaction Type in conversion program 'Import GL Transaction Types'  */  
   ConversionErrors:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   IsLocked:boolean,
   LockStatus:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTTypeSubDataTableset{
   BRFunctionPhrase:Erp_Tablesets_BRFunctionPhraseRow[],
   HierarchicalData:Erp_Tablesets_HierarchicalDataRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ACTTypeTableset{
   ACTType:Erp_Tablesets_ACTTypeRow[],
   ACTRevision:Erp_Tablesets_ACTRevisionRow[],
   ABTDocLine:Erp_Tablesets_ABTDocLineRow[],
   ABTAmount:Erp_Tablesets_ABTAmountRow[],
   ABTPostEntity:Erp_Tablesets_ABTPostEntityRow[],
   ABTPostCode:Erp_Tablesets_ABTPostCodeRow[],
   ABTQuery:Erp_Tablesets_ABTQueryRow[],
   ABTQParam:Erp_Tablesets_ABTQParamRow[],
   ACTBook:Erp_Tablesets_ACTBookRow[],
   BookingRule:Erp_Tablesets_BookingRuleRow[],
   BookValRule:Erp_Tablesets_BookValRuleRow[],
   BROperation:Erp_Tablesets_BROperationRow[],
   BROperationCustom:Erp_Tablesets_BROperationCustomRow[],
   BRFunction:Erp_Tablesets_BRFunctionRow[],
   BookVar:Erp_Tablesets_BookVarRow[],
   BRFuncArgs:Erp_Tablesets_BRFuncArgsRow[],
   BRFuncOperation:Erp_Tablesets_BRFuncOperationRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BRFuncArgsRow{
      /**  Reference to the Parent function UID.  */  
   FunctionUID:number,
      /**  Name of function argument  */  
   ArgName:string,
      /**  Type of function argument  */  
   ArgType:string,
      /**  Technical name  */  
   PRGName:string,
      /**  Technical type  */  
   PRGType:string,
      /**  Reference to the Revision  */  
   ACTRevisionUID:number,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Unique Argument identifier.  */  
   ArgumentUID:number,
      /**  Reference to  the company  */  
   Company:string,
      /**  Indicates default Function Arguments for ABT templates.  */  
   IsDefault:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   DevelopMode:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BRFuncOperationRow{
      /**  Operation unique ID. Technical identifier.  */  
   OperationUID:number,
      /**  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  */  
   ParentOperationUID:number,
      /**  The identifier of the control flow operator.  */  
   ControlFlowOperator:string,
      /**  The identifier of the target container.  */  
   Container:string,
      /**  The name of formula.  */  
   Formula:string,
      /**  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  */  
   SequenceNumber:number,
      /**  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  */  
   ChildSequenceNumber:number,
      /**  System ID of used function.  */  
   FunctionUID:number,
      /**  Technical text of the function(formula)  */  
   PRGText:string,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Reference to the Function of the GL Transaction Type.  */  
   FuncOperUID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  The identifier of the target container.  */  
   PRGContainer:string,
      /**  Indicates default Function Operations for ABT templates.  */  
   IsDefault:boolean,
      /**  LocModified  */  
   LocModified:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DevelopMode:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
      /**  Contains error text in generated code.  */  
   ErrorText:string,
      /**  Allow use icon easier.  */  
   IsError:boolean,
      /**  Unified container type for both Operation and Logical Condition types  */  
   ContainerType:string,
      /**  Indicates 'Logical Condition' type of the operation  */  
   IsLogicalCondition:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BRFunctionPhraseRow{
   ACTTypeUID:number,
   ACTRevisionUID:number,
   FunctionUID:number,
   ArgumentUID:number,
      /**  Text of the function phrase element  */  
   ElementText:string,
      /**  Element type  */  
   ElementType:string,
      /**  Order of phrase elements  */  
   Order:number,
   ArgType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BRFunctionRow{
      /**  Unique Function identifier.  */  
   FunctionUID:number,
      /**  Name of the function.  */  
   Name:string,
      /**  Technical name of function  */  
   PRGName:string,
      /**  If the function is system.  */  
   IsSystem:boolean,
      /**  Detail description for function.  */  
   Description:string,
      /**  Type of function result.  */  
   ResultType:string,
      /**  Technical text of function.  */  
   PRGPattern:string,
      /**  Reference to the Revisions.  */  
   ACTRevisionUID:number,
      /**  Reference to the GL Transaction Type  */  
   ACTTypeUID:number,
      /**  Reference to Book.  */  
   BookID:string,
      /**  Text of function  */  
   Formula:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Text field to store the For Each criteria expression .  */  
   DocLinePath:string,
      /**  Indicates default Functions for ABT templates.  */  
   IsDefault:boolean,
      /**  ManuallyUpdVer  */  
   ManuallyUpdVer:boolean,
      /**  Specifies the function version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  */  
   FuncVer:number,
      /**  PatchFuncVer  */  
   PatchFuncVer:number,
      /**  PrevModified  */  
   PrevModified:boolean,
      /**  Modified  */  
   Modified:boolean,
      /**  LocVer  */  
   LocVer:number,
      /**  LocPatchVer  */  
   LocPatchVer:number,
      /**  LocModified  */  
   LocModified:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   DevelopMode:boolean,
      /**  Is used to show icon in Tree.  */  
   IsError:boolean,
      /**  Contains error text for a function.  */  
   ErrorText:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BROperationCustomRow{
      /**  Company Indetifier.  */  
   Company:string,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the Book.  */  
   BookID:string,
      /**  Reference to the parent booking rule.  */  
   RuleUID:number,
      /**  Operation unique ID. Technical identifier.  */  
   OperationUID:number,
      /**  Reference to the parent operation  */  
   ParentOperationUID:number,
      /**  An order number indicating the operation’s place in the sequence of execution.  */  
   ChildSequenceNumber:number,
      /**  The identifier of the control flow operator.  */  
   ControlFlowOperator:string,
      /**  The identifier of the target container.  */  
   Container:string,
      /**  The operation's main formula.  */  
   Formula:string,
      /**  Function unique ID.  */  
   FunctionUID:number,
      /**  Code for operation  */  
   PRGText:string,
      /**  The identifier of the target container.  */  
   PRGContainer:string,
      /**  Audit column. Populate UserID who created the row.  */  
   CreatedBy:string,
      /**  Audit column. Populate time of creation row.  */  
   CreatedOn:string,
      /**  Audit column. Populate UserID of last person who updated the row.  */  
   ChangedBy:string,
      /**  Audit column. Populate time of updating the row.  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
      /**  Contains error text in generated code.  */  
   ErrorText:string,
      /**  Allow use icon easier.  */  
   IsError:boolean,
      /**  Unified container type for both Operation and Logical Condition types  */  
   ContainerType:string,
      /**  Indicates 'Logical Condition' type of the operation  */  
   IsLogicalCondition:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BROperationRow{
      /**  Operation unique ID. Technical identifier.  */  
   OperationUID:number,
      /**  Reference to the parent booking rule.  */  
   RuleUID:number,
      /**  Reference to the parent operation (necessary to support the hierarchical operations structure; references the OperationUID field in the same table).  */  
   ParentOperationUID:number,
      /**  The identifier of the control flow operator.  */  
   ControlFlowOperator:string,
      /**  The identifier of the target container.  */  
   Container:string,
      /**  The operation's main formula.  */  
   Formula:string,
      /**  An order number indicating the operation?s place in the sequence of execution ? for the whole set of ruleset?s operations.  */  
   SequenceNumber:number,
      /**  An order number indicating the operation?s place in the sequence of execution ? for a single block of operations on a single hierarchy level.  */  
   ChildSequenceNumber:number,
      /**  Function unique ID. Technical identifier.  */  
   FunctionUID:number,
      /**  Progress Code for operation  */  
   PRGText:string,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  The identifier of the target container.  */  
   PRGContainer:string,
      /**  Reference to the Book.  */  
   BookID:string,
      /**  Indicates default Operations for ABT templates.  */  
   IsDefault:boolean,
      /**  LocModified  */  
   LocModified:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unified container type for both Operation and Logical Condition types  */  
   ContainerType:string,
   DevelopMode:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
      /**  Contains error text in generated code.  */  
   ErrorText:string,
      /**  Allow use icon easier.  */  
   IsError:boolean,
      /**  Field to support functionality of link-combo in Kinetic (Container in operations)  */  
   LLink01:string,
      /**  Indicates 'Logical Condition' type of the operation  */  
   IsLogicalCondition:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BookValRuleRow{
      /**  Unique value.Primary key  */  
   BVRuleUID:number,
      /**  Technical key of Validation Rule  */  
   VRuleUID:number,
      /**  Validation rule description  */  
   Description:string,
      /**  Error, Ignor, Warning, Autocorrect, Autocorrect with warning  */  
   Action:string,
      /**  Validation level : Book, Booking Rule, Company etc  */  
   VLevel:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Reference to Book.  */  
   BookID:string,
      /**  Account transaction type UID. Technical identifier.  */  
   ACTTypeUID:number,
      /**  Reference to the parent account transaction revision.  */  
   ACTRevisionUID:number,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Indicates default validation rules for ABT templates.  */  
   IsDefault:boolean,
      /**  List of actions (used in combo boxes).  */  
   ActionList:string,
      /**  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  */  
   RuleType:string,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
   DevelopMode:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BookVarRow{
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Reference to the Book  */  
   BookID:string,
      /**  BookVar unique ID.  */  
   BookVarUID:number,
      /**  Variable Name  */  
   VarName:string,
      /**  Variable Type  */  
   VarType:string,
      /**  Variable context, possible values: Global, Book, Rule, Function.  */  
   vType:string,
      /**  ID of context, for example if vType = Function then vUID = FunctionUID.  */  
   vUID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates default Variables for VBD templates.  */  
   IsDefault:boolean,
      /**  LocModified  */  
   LocModified:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DevelopMode:boolean,
      /**  the field is used for generation post program  */  
   isSystem:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
      /**  Function or Rule Description.  */  
   OwnerDescription:string,
      /**  VarType display.  */  
   VarTypeDisplay:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BookingRuleRow{
      /**  Technical identifier.  */  
   RuleUID:number,
      /**  Reference to the Revision.  */  
   ACTRevisionUID:number,
      /**  Booking rule name to be displayed in the tree view navigation control.  */  
   DisplayName:string,
      /**  Booking rule detailed description.  */  
   DetailedDescription:string,
      /**  Text field to store the selection criteria expression .  */  
   SelectionCriteria:string,
      /**  Reference to the Book.  */  
   BookID:string,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  It is Rule for Posting process or special for GLControl calculation.  */  
   IsPost:boolean,
      /**  Text field to store the For Each criteria expression .  */  
   ForEach:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Rule run once, usual it is used for calculation Book variables or Header variables (that can be calculated once).  */  
   IsHeader:boolean,
      /**  Determines whether the posting process uses the rule.  */  
   IsActive:boolean,
      /**  Stores a reference to a credit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing..  */  
   CreditContext:string,
      /**  Stores a reference to a debit context for use by another posting rule. Posting rules can create a GL control that stores the rule's output for use in subsequent processing.  */  
   DebitContext:string,
      /**  Reference  Context is used for pre-Posting rules  */  
   RefContext:string,
      /**  Determines the GL control type that applies to the rule. The control type affects the processing of accounts generated by the rule. Pre-posting GL controls use the type to determine the reference context, used to set the default for a GL account field. The type also controls the credit and debit contexts for posting rules.  */  
   GLControlType:string,
      /**  Indicates default Rules for ABT templates.  */  
   IsDefault:boolean,
      /**  Primary key from the Entity is a source of keys for TranGLC table that save Reference control of the Booking Rule.  */  
   Entity:string,
      /**  IsReference  */  
   IsReference:boolean,
      /**  Indicates that Versions were updated manually  */  
   ManuallyUpdVer:boolean,
      /**  Specifies the individual rule version. Uses a single numeric sequence and increments every time a change is made in a corresponding rule.  */  
   RuleVer:number,
      /**  Specifies the individual rule patch version. Uses a single numeric sequence and increments each time a change is released in a patch to a client between service packs. The patch version resets to zero every time a service pack is released.  */  
   PatchRuleVer:number,
      /**  Value of Modified field before last Update Versions  */  
   PrevModified:boolean,
      /**  Indicates that data were modified  */  
   Modified:boolean,
      /**  LocVer  */  
   LocVer:number,
      /**  LocPatchVer  */  
   LocPatchVer:number,
      /**  LocModified  */  
   LocModified:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Enabling/disabling customization for the Book  */  
   EnableCustomization:boolean,
      /**  Indicates that base information on rule was changed. In this case this rule will not be automatically updated during converstion program to save user's changes.  */  
   BaseModified:boolean,
      /**  Indicates that rule contaion operations on 'Customization' part  */  
   Customization:boolean,
      /**  Used to bind UI control.  */  
   Operator:string,
      /**  Selection Criteria Display.  */  
   SelCriteriaDisplay:string,
      /**  Used to bind UI control.  */  
   Argument:string,
   DevelopMode:boolean,
      /**   0- not loaded on client       
1-loaded fully
2- partial  */  
   Loaded:number,
      /**  RuleType - PrePost(calculation in pre-post mode before posting), Post(standard posting) or Ref (Calculate reference GLControl during posting)  */  
   RuleType:string,
      /**  Is used to show icon in Tree.  */  
   IsError:boolean,
      /**  Contains error text for a rule.  */  
   ErrorText:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegmentNameListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Name of Segment  */  
   SegmentName:string,
      /**  Short name of segment.  */  
   Abbreviation:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBookListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Descripiton of Book  */  
   Description:string,
      /**  Indicates if this is the Main Book.  Only one main book is allowed.  */  
   MainBook:boolean,
      /**  Chart of Account Code  */  
   COACode:string,
      /**  Indicates the base currency for the book  */  
   CurrencyCode:string,
      /**  Indicates the type of book.  Standard, Consolidation, etc.  */  
   BookType:number,
   COACodeDescription:string,
      /**  Indicates if the book is inactive  */  
   Inactive:boolean,
      /**  Identifier for the Fiscal Calendar assigned to the book  */  
   FiscalCalendarID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates how opening balances will be updated  */  
   OpenBalUpdateOpt:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBookMapRow{
      /**  Company value. If it is empty that mean that mapping is used for all companies, that do not have specified data.  */  
   Company:string,
      /**  Source BookID  */  
   ImportBook:string,
      /**  COA Code of Source Book  */  
   ImportCOA:string,
      /**  Target Book ID  */  
   MapBook:string,
      /**  COA Code of Target Book  */  
   MapCOA:string,
      /**  Package of Source Book  */  
   Package:string,
      /**  New Revision Code  */  
   RevisionCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBookPackageSegmentMapRow{
      /**  Company ID  */  
   Company:string,
      /**  Book ID  */  
   BookID:string,
      /**  Posting Rules Package  */  
   Package:string,
      /**  Segment Number in Posting Rules Package  */  
   SourceSegmentNbr:number,
      /**  Segment Number in COA of the Book  */  
   TargetSegmentNbr:number,
      /**  User ID of the user who created the record  */  
   CreatedBy:string,
      /**  The date/ time that the record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record  */  
   ChangedBy:string,
      /**  The date/ time that the record was last changed  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Chart of Account Code  */  
   COACode:string,
      /**  Target Segment Name  */  
   TargetSegmentName:string,
   BitFlag:number,
   SourceSegmentName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLSegmentMapRow{
      /**  Company value. If it is empty that mean that mapping is used for all companies, that do not have specified data.  */  
   Company:string,
      /**  Source Book ID  */  
   ImportBook:string,
      /**  COA Code of Source Book  */  
   ImportCOA:string,
      /**  Source Segment Name  */  
   ImportSegmentName:string,
      /**  Source Segment Number  */  
   ImportSegmentNum:number,
      /**  Target Book ID  */  
   MapBook:string,
      /**  COA Code of Target Book  */  
   MapCOA:string,
      /**  Target Segment Name  */  
   MapSegmentName:string,
      /**  Target Segment Number  */  
   MapSegmentNum:number,
      /**  Package of Source Book  */  
   Package:string,
      /**  New Revision Code  */  
   RevisionCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HierarchicalDataRow{
      /**  ID  */  
   ID:string,
      /**  ParentID  */  
   ParentID:string,
      /**  Name  */  
   Name:string,
      /**  DataType  */  
   DataType:string,
      /**  DisplayText  */  
   DisplayText:string,
      /**  FormulaText  */  
   FormulaText:string,
      /**  Node can be selected in the tree.  */  
   Selectable:boolean,
      /**  DataTypeIsValueType  */  
   DataTypeIsValueType:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LinkComboDataTableset{
   PhraseItem:Erp_Tablesets_PhraseItemRow[],
   PhraseItemBinding:Erp_Tablesets_PhraseItemBindingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PhraseItemBindingRow{
   link01:string,
   link02:string,
   link03:string,
   link04:string,
   link05:string,
   link06:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PhraseItemRow{
   alwaysClickable:boolean,
   defaultValue:string,
   epBinding:string,
   itemId:string,
   maxWidth:number,
   phraseItemId:string,
   type:string,
   value:string,
   dataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RevisionImportOpRow{
      /**  ACT Revision UID of updated revision  */  
   ACTRevisionUID:number,
      /**  Indicate that VBD Structure should be updated during import in Update Mode  */  
   ImportABT:boolean,
      /**  Indicate that Ruleset should be updated during import in Update Mode  */  
   ImportBR:boolean,
   NewRevisionCode:string,
      /**  Flag to indicate that existing Revision with "New Revision Code" should be removed before import.  */  
   ReplaceExisting:boolean,
   RevisionCode:string,
      /**  Indicate that import shoud be done in Update Mode  */  
   UpdateMode:boolean,
   ACTTypeName:string,
   FileName:string,
   XMLData:string,
      /**  Indicates that imported file is system  */  
   IsSystemXML:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtACTTypeTableset{
   ACTType:Erp_Tablesets_ACTTypeRow[],
   ACTRevision:Erp_Tablesets_ACTRevisionRow[],
   ABTDocLine:Erp_Tablesets_ABTDocLineRow[],
   ABTAmount:Erp_Tablesets_ABTAmountRow[],
   ABTPostEntity:Erp_Tablesets_ABTPostEntityRow[],
   ABTPostCode:Erp_Tablesets_ABTPostCodeRow[],
   ABTQuery:Erp_Tablesets_ABTQueryRow[],
   ABTQParam:Erp_Tablesets_ABTQParamRow[],
   ACTBook:Erp_Tablesets_ACTBookRow[],
   BookingRule:Erp_Tablesets_BookingRuleRow[],
   BookValRule:Erp_Tablesets_BookValRuleRow[],
   BROperation:Erp_Tablesets_BROperationRow[],
   BROperationCustom:Erp_Tablesets_BROperationCustomRow[],
   BRFunction:Erp_Tablesets_BRFunctionRow[],
   BookVar:Erp_Tablesets_BookVarRow[],
   BRFuncArgs:Erp_Tablesets_BRFuncArgsRow[],
   BRFuncOperation:Erp_Tablesets_BRFuncOperationRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param strRevisionList
      @param aCTTypeUID
      @param developMode
   */  
export interface ExportToXML_input{
      /**  strRevisionList  */  
   strRevisionList:string,
      /**  aCTTypeUID  */  
   aCTTypeUID:number,
      /**  Developer Mode  */  
   developMode:boolean,
}

export interface ExportToXML_output{
parameters : {
      /**  output parameters  */  
   cXML:any[],
}
}

   /** Required : 
      @param ds
   */  
export interface FillBAQDescription_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface FillBAQDescription_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface FunctionPhraseElementDelete_input{
   ds:Erp_Tablesets_ACTTypeSubDataTableset[],
}

export interface FunctionPhraseElementDelete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeSubDataTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface FunctionPhraseElementGetNew_input{
   ds:Erp_Tablesets_ACTTypeSubDataTableset[],
}

export interface FunctionPhraseElementGetNew_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeSubDataTableset,
}
}

   /** Required : 
      @param companyName
      @param aCTTypeUID
      @param aCTRevisionUID
   */  
export interface GenerateTemplate_input{
      /**  Company Name  */  
   companyName:string,
      /**  aCTTypeUID  */  
   aCTTypeUID:number,
      /**  aCTRevisionUID  */  
   aCTRevisionUID:number,
}

export interface GenerateTemplate_output{
parameters : {
      /**  output parameters  */  
   errorText:string,
}
}

export interface GetAllACTTypesForExport_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param tag
      @param bookID
      @param actTypeUID
      @param actRevisionUID
   */  
export interface GetBRContainerRows_input{
      /**  tag  */  
   tag:string,
      /**  bookID  */  
   bookID:string,
      /**  actTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
}

export interface GetBRContainerRows_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param company
      @param actTypeName
      @param revisionCode
      @param BookID
   */  
export interface GetBookPackage_input{
      /**  Company  */  
   company:string,
      /**  GL Transaction Type Name  */  
   actTypeName:string,
      /**  Revision Code  */  
   revisionCode:string,
      /**  BookID  */  
   BookID:string,
}

export interface GetBookPackage_output{
      /**  Package  */  
   returnObj:string,
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param ownerType
   */  
export interface GetBookVarOwnerID_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  ownerType  */  
   ownerType:string,
}

export interface GetBookVarOwnerID_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

export interface GetBookVarOwnerTypes_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

   /** Required : 
      @param itemBinding
      @param ds
   */  
export interface GetBookVarTypeList_input{
      /**  the name of binding for linked combo control  */  
   itemBinding:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetBookVarTypeList_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
   */  
export interface GetBookVersions_input{
      /**  ACTTypeUID  */  
   actTypeUID:number,
      /**  ACTRevisionUID  */  
   actRevisionUID:number,
      /**  BookID  */  
   bookID:string,
}

export interface GetBookVersions_output{
parameters : {
      /**  output parameters  */  
   opPackage:string,
   opRulesetVer:number,
   opPatchRulesetVer:number,
}
}

   /** Required : 
      @param acTTypeUID
      @param developMode
   */  
export interface GetByIDExt_input{
   acTTypeUID:number,
      /**  flag Developer Mode  */  
   developMode:boolean,
}

export interface GetByIDExt_output{
   returnObj:Erp_Tablesets_ACTTypeTableset[],
}

   /** Required : 
      @param acTTypeUID
      @param revisions
      @param developMode
   */  
export interface GetByID_Revisions_input{
   acTTypeUID:number,
      /**  Revision list (Comma delimiter)  */  
   revisions:string,
      /**  flag Developer Mode  */  
   developMode:boolean,
}

export interface GetByID_Revisions_output{
   returnObj:Erp_Tablesets_ACTTypeTableset[],
}

   /** Required : 
      @param acTTypeUID
   */  
export interface GetByID_input{
   acTTypeUID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ACTTypeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ACTTypeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ACTTypeTableset[],
}

   /** Required : 
      @param BookID
   */  
export interface GetCOAIDForBook_input{
   BookID:string,
}

export interface GetCOAIDForBook_output{
   returnObj:string,
}

   /** Required : 
      @param mapBookCOAID
      @param currentBookCOAID
   */  
export interface GetCOAMapsList_input{
   mapBookCOAID:string,
   currentBookCOAID:string,
}

export interface GetCOAMapsList_output{
   returnObj:string,
}

   /** Required : 
      @param itemBinding
      @param currentType
   */  
export interface GetCommonTypeList_input{
   itemBinding:string,
      /**  BookVar.VarType or BRFunction.ResultType  */  
   currentType:string,
}

export interface GetCommonTypeList_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
}

export interface GetConditionList_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
}

   /** Required : 
      @param actTypeID
      @param actRevisionUID
      @param bookID
      @param functionUID
      @param ruleUID
      @param container
      @param isLogicalCondition
      @param tableName
   */  
export interface GetContainerPhraseItems_input{
   actTypeID:number,
   actRevisionUID:number,
   bookID:string,
   functionUID:number,
   ruleUID:number,
   container:string,
   isLogicalCondition:boolean,
   tableName:string,
}

export interface GetContainerPhraseItems_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
}

   /** Required : 
      @param actTypeName
   */  
export interface GetCurrentVersion_input{
      /**  ACT Type Name  */  
   actTypeName:string,
}

export interface GetCurrentVersion_output{
parameters : {
      /**  output parameters  */  
   abtVer:string,
}
}

   /** Required : 
      @param iACTTypeUID
      @param iACTRevisionUID
      @param sBookID
      @param iRuleUID
      @param iFunctionID
   */  
export interface GetCustomContextMenuXml_input{
      /**  ACTTypeUID  */  
   iACTTypeUID:number,
      /**  ACTRevisionUID  */  
   iACTRevisionUID:number,
      /**  BookID  */  
   sBookID:string,
      /**  RuleUID  */  
   iRuleUID:number,
      /**  FunctionUID  */  
   iFunctionID:number,
}

export interface GetCustomContextMenuXml_output{
parameters : {
      /**  output parameters  */  
   sXML:any[],
}
}

   /** Required : 
      @param actTypeID
      @param actRevisionUID
      @param bookID
      @param ruleID
   */  
export interface GetEntityForBookingRule_input{
      /**  ACTTypeUID  */  
   actTypeID:number,
      /**  ACTRevisionUID  */  
   actRevisionUID:number,
      /**  BookID  */  
   bookID:string,
      /**  RuleUID  */  
   ruleID:number,
}

export interface GetEntityForBookingRule_output{
parameters : {
      /**  output parameters  */  
   brEntity:string,
}
}

   /** Required : 
      @param BAQID
   */  
export interface GetFieldsOfBAQList_input{
   BAQID:string,
}

export interface GetFieldsOfBAQList_output{
   returnObj:string,
}

   /** Required : 
      @param schema
      @param table
   */  
export interface GetFieldsOfTable_input{
   schema:string,
   table:string,
}

export interface GetFieldsOfTable_output{
   returnObj:string,
}

export interface GetFlowList_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param ruleUID
      @param functionUID
      @param container
      @param containerType
      @param formula
      @param bookID
      @param docLinePath
      @param funcOperUID
      @param isLogicalCondition
      @param bindingSuffix
   */  
export interface GetFormulaPhraseItems_input{
   actTypeUID:number,
   actRevisionUID:number,
   ruleUID:number,
   functionUID:number,
   container:string,
   containerType:string,
   formula:string,
   bookID:string,
      /**  BRFunction.DocLinePath OR BookingRule.ForEach  */  
   docLinePath:string,
      /**  0 if not BRFuncOperation  */  
   funcOperUID:number,
   isLogicalCondition:boolean,
      /**  'Custom' if BROperation, 'FuncOper' of BRFuncOperation, '' if BROperation  */  
   bindingSuffix:string,
}

export interface GetFormulaPhraseItems_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param functionUID
   */  
export interface GetFuncVersions_input{
      /**  ACTTypeUID  */  
   actTypeUID:number,
      /**  ACTRevisionUID  */  
   actRevisionUID:number,
      /**  BookID  */  
   bookID:string,
      /**  FunctionUID  */  
   functionUID:number,
}

export interface GetFuncVersions_output{
parameters : {
      /**  output parameters  */  
   opFuncVer:number,
   opPatchFuncVer:number,
}
}

   /** Required : 
      @param ds
   */  
export interface GetFunctionPhraseElements_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetFunctionPhraseElements_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param functionUID
      @param name
   */  
export interface GetFunctionPhrase_input{
   actTypeUID:number,
   actRevisionUID:number,
   functionUID:number,
   name:string,
}

export interface GetFunctionPhrase_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
}

   /** Required : 
      @param itemBinding
      @param ds
   */  
export interface GetFunctionResultTypeList_input{
      /**  the name of binding for linked combo control  */  
   itemBinding:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetFunctionResultTypeList_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param GPostingUID
      @param NodeID
   */  
export interface GetFunctionTree_input{
      /**  Function SysRowID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)  */  
   GPostingUID:string,
      /**  Fake node.  */  
   NodeID:string,
}

export interface GetFunctionTree_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param ruleType
   */  
export interface GetGLControlTypesList_input{
      /**  Rule Type  */  
   ruleType:string,
}

export interface GetGLControlTypesList_output{
   returnObj:string,
}

   /** Required : 
      @param actTypeName
      @param package
   */  
export interface GetHashSystemXml_input{
      /**  GL Transaction Type Name  */  
   actTypeName:string,
      /**  Package  */  
   package:string,
}

export interface GetHashSystemXml_output{
parameters : {
      /**  output parameters  */  
   value:string,
}
}

   /** Required : 
      @param companyName
      @param actTypeName
   */  
export interface GetIDByName_input{
      /**  CompanyName  */  
   companyName:string,
      /**  ACT Type Name  */  
   actTypeName:string,
}

export interface GetIDByName_output{
parameters : {
      /**  output parameters  */  
   actTypeID:number,
}
}

   /** Required : 
      @param GPostingUID
      @param NodeID
   */  
export interface GetLeftTree_input{
      /**  A ~ (tilde) separated list consisting of:
            0 = Node text
            1 = Node tag  */  
   GPostingUID:string,
      /**  Not currently used  */  
   NodeID:string,
}

export interface GetLeftTree_output{
      /**  Tree Object  */  
   returnObj:any,      //schema had no properties on an object.
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
   returnObj:Erp_Tablesets_ACTTypeListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param currentBookID
   */  
export interface GetMapBookList_input{
   actTypeUID:number,
   actRevisionUID:number,
   currentBookID:string,
}

export interface GetMapBookList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param abTDocLineUID
   */  
export interface GetNewABTAmount_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   abTDocLineUID:number,
}

export interface GetNewABTAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
   */  
export interface GetNewABTDocLine_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
}

export interface GetNewABTDocLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param abTDocLineUID
      @param abTPostEntityUID
   */  
export interface GetNewABTPostCode_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   abTDocLineUID:number,
   abTPostEntityUID:number,
}

export interface GetNewABTPostCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param abTDocLineUID
   */  
export interface GetNewABTPostEntity_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   abTDocLineUID:number,
}

export interface GetNewABTPostEntity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param abTDocLineUID
      @param abTQueryUID
   */  
export interface GetNewABTQParam_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   abTDocLineUID:number,
   abTQueryUID:number,
}

export interface GetNewABTQParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param abTDocLineUID
   */  
export interface GetNewABTQuery_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   abTDocLineUID:number,
}

export interface GetNewABTQuery_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
   */  
export interface GetNewACTBook_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
}

export interface GetNewACTBook_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
   */  
export interface GetNewACTRevision_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
}

export interface GetNewACTRevision_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewACTType_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetNewACTType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param functionUID
   */  
export interface GetNewBRFuncArgs_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   functionUID:number,
}

export interface GetNewBRFuncArgs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param funcOperUID
   */  
export interface GetNewBRFuncOperation_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   funcOperUID:number,
}

export interface GetNewBRFuncOperation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param bookID
   */  
export interface GetNewBRFunction_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   bookID:string,
}

export interface GetNewBRFunction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param bookID
      @param ruleUID
   */  
export interface GetNewBROperationCustom_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   bookID:string,
   ruleUID:number,
}

export interface GetNewBROperationCustom_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param bookID
      @param ruleUID
   */  
export interface GetNewBROperation_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   bookID:string,
   ruleUID:number,
}

export interface GetNewBROperation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param bookID
   */  
export interface GetNewBookVar_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   bookID:string,
}

export interface GetNewBookVar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param acTTypeUID
      @param acTRevisionUID
      @param bookID
   */  
export interface GetNewBookingRule_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
   acTTypeUID:number,
   acTRevisionUID:number,
   bookID:string,
}

export interface GetNewBookingRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

export interface GetOperatorList_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

   /** Required : 
      @param currentValue
   */  
export interface GetPostCodeTypesExt_input{
   currentValue:string,
}

export interface GetPostCodeTypesExt_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
}

export interface GetPostCodeTypes_output{
parameters : {
      /**  output parameters  */  
   strTypes:string,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param abtDocLineUID
      @param schemaName
      @param developMode
      @param isDefault
   */  
export interface GetPostEntityDataSourceList_input{
   actTypeUID:number,
   actRevisionUID:number,
   abtDocLineUID:number,
   schemaName:string,
   developMode:boolean,
   isDefault:boolean,
}

export interface GetPostEntityDataSourceList_output{
   returnObj:string,
}

   /** Required : 
      @param GPostingUID
      @param NodeID
   */  
export interface GetPostingRuleBaseTree_input{
      /**  Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)  */  
   GPostingUID:string,
      /**  Fake node.  */  
   NodeID:string,
}

export interface GetPostingRuleBaseTree_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param GPostingUID
      @param NodeID
   */  
export interface GetPostingRuleCustomizationTree_input{
      /**  Function ID (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 for test purposes)  */  
   GPostingUID:string,
      /**  Fake node.  */  
   NodeID:string,
}

export interface GetPostingRuleCustomizationTree_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param whoIsCalled
      @param tag
      @param ds
   */  
export interface GetRelatedContextItemsBookVarType_input{
   whoIsCalled:string,
   tag:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetRelatedContextItemsBookVarType_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param whoIsCalled
      @param tag
      @param ds
   */  
export interface GetRelatedContextItemsCustom_input{
   whoIsCalled:string,
   tag:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetRelatedContextItemsCustom_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param whoIsCalled
      @param tag
      @param ds
   */  
export interface GetRelatedContextItemsFuncOper_input{
   whoIsCalled:string,
   tag:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetRelatedContextItemsFuncOper_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetRelatedContextItemsFunctionPhrase_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetRelatedContextItemsFunctionPhrase_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param whoIsCalled
      @param tag
      @param ds
   */  
export interface GetRelatedContextItemsFunctionResultType_input{
   whoIsCalled:string,
   tag:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetRelatedContextItemsFunctionResultType_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param whoIsCalled
      @param tag
      @param ds
   */  
export interface GetRelatedContextItems_input{
   whoIsCalled:string,
   tag:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface GetRelatedContextItems_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
   */  
export interface GetRevVersions_input{
      /**  ACTTypeUID  */  
   actTypeUID:number,
      /**  ACTRevisionUID  */  
   actRevisionUID:number,
}

export interface GetRevVersions_output{
parameters : {
      /**  output parameters  */  
   opABTVer:string,
   opPatchABTVer:string,
}
}

   /** Required : 
      @param companyName
      @param actRevisionCode
      @param actTypeID
   */  
export interface GetRevisionIDByName_input{
      /**  Company Name  */  
   companyName:string,
      /**  ACT Revision Code  */  
   actRevisionCode:string,
      /**  ACTTypeID  */  
   actTypeID:number,
}

export interface GetRevisionIDByName_output{
parameters : {
      /**  output parameters  */  
   actRevisionID:number,
}
}

export interface GetRevisionStatusesList_output{
   returnObj:string,
}

   /** Required : 
      @param actTypeUID
   */  
export interface GetRevisionsList_input{
   actTypeUID:number,
}

export interface GetRevisionsList_output{
   returnObj:string,
}

   /** Required : 
      @param GPostingUID
      @param NodeID
   */  
export interface GetRightTree_input{
      /**  A ~ (tilde) separated list consisting of:
            0 = Node text
            1 = Node tag  */  
   GPostingUID:string,
      /**  Not currently used  */  
   NodeID:string,
}

export interface GetRightTree_output{
      /**  Tree Object  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param whereClauseACTType
      @param whereClauseACTRevision
      @param whereClauseABTDocLine
      @param whereClauseABTAmount
      @param whereClauseABTPostEntity
      @param whereClauseABTPostCode
      @param whereClauseABTQuery
      @param whereClauseABTQParam
      @param whereClauseACTBook
      @param whereClauseBookingRule
      @param whereClauseBookValRule
      @param whereClauseBROperation
      @param whereClauseBROperationCustom
      @param whereClauseBRFunction
      @param whereClauseBookVar
      @param whereClauseBRFuncArgs
      @param whereClauseBRFuncOperation
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseACTType:string,
   whereClauseACTRevision:string,
   whereClauseABTDocLine:string,
   whereClauseABTAmount:string,
   whereClauseABTPostEntity:string,
   whereClauseABTPostCode:string,
   whereClauseABTQuery:string,
   whereClauseABTQParam:string,
   whereClauseACTBook:string,
   whereClauseBookingRule:string,
   whereClauseBookValRule:string,
   whereClauseBROperation:string,
   whereClauseBROperationCustom:string,
   whereClauseBRFunction:string,
   whereClauseBookVar:string,
   whereClauseBRFuncArgs:string,
   whereClauseBRFuncOperation:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ACTTypeTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ruleType
      @param glControlType
   */  
export interface GetRuleContextsList_input{
      /**  Rule Type  */  
   ruleType:string,
      /**  GL Control Type  */  
   glControlType:string,
}

export interface GetRuleContextsList_output{
   returnObj:string,
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param ruleUID
   */  
export interface GetRuleVersions_input{
      /**  ACTTypeUID  */  
   actTypeUID:number,
      /**  ACTRevisionUID  */  
   actRevisionUID:number,
      /**  BookID  */  
   bookID:string,
      /**  RuleUID  */  
   ruleUID:number,
}

export interface GetRuleVersions_output{
parameters : {
      /**  output parameters  */  
   opRuleVer:number,
   opPatchRuleVer:number,
}
}

export interface GetStatusList_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

export interface GetSummarizeList_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

export interface GetTrCurrencyList_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param docLineUID
      @param abtPostEntityUID
      @param abtPostCodeUID
   */  
export interface GetValueTypesForPostCode_input{
   actTypeUID:number,
   actRevisionUID:number,
   docLineUID:number,
   abtPostEntityUID:number,
   abtPostCodeUID:number,
}

export interface GetValueTypesForPostCode_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
}

export interface GetVarTypes_output{
parameters : {
      /**  output parameters  */  
   arTypes:string,
}
}

   /** Required : 
      @param iACTTypeUID
      @param iACTRevisionUID
      @param cStatus
   */  
export interface GetWarningRevisionStatus_input{
      /**  iACTTypeUID  */  
   iACTTypeUID:number,
      /**  iACTRevisionUID  */  
   iACTRevisionUID:number,
      /**  Status  */  
   cStatus:string,
}

export interface GetWarningRevisionStatus_output{
parameters : {
      /**  output parameters  */  
   cWarning:string,
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
      @param typeName
      @param cRevisionList
      @param cXML
      @param compList
      @param bookMap
   */  
export interface ImportFromXML_input{
      /**  ACTType Display Name  */  
   typeName:string,
      /**  Revisions List  */  
   cRevisionList:string,
      /**  XML Document Element  */  
   cXML:object
      /**  Companies List  */  
   compList:string,
      /**  Books Map as List  */  
   bookMap:string,
}

export interface ImportFromXML_output{
parameters : {
      /**  output parameters  */  
   ErrorMess:string,
}
}

   /** Required : 
      @param actTypeName
      @param cXML
      @param actTypeImportOpDs
   */  
export interface ImportGLTransactionType_input{
      /**  ACTType Display Name  */  
   actTypeName:string,
      /**  XML Document Element  */  
   cXML:object
   actTypeImportOpDs:Erp_Tablesets_ACTTypeImportOpTableset[],
}

export interface ImportGLTransactionType_output{
parameters : {
      /**  output parameters  */  
   ErrorMess:string,
}
}

export interface ImportProcessIsAllowed_output{
}

export interface InitializeForTests_output{
}

   /** Required : 
      @param acttypeuid
      @param actrevisionuid
      @param bookid
      @param bookvaruid
      @param errorreturn
   */  
export interface IsVarInUse_input{
      /**  acttypeuid  */  
   acttypeuid:number,
      /**  actrevisionuid  */  
   actrevisionuid:number,
      /**  bookid  */  
   bookid:string,
      /**  bookvaruid  */  
   bookvaruid:number,
      /**  errorreturn  */  
   errorreturn:boolean,
}

export interface IsVarInUse_output{
parameters : {
      /**  output parameters  */  
   isinuse:boolean,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
   */  
export interface ListMappedBooksWithRules_input{
      /**  actTypeUID  */  
   actTypeUID:number,
      /**  iACTRevisionUID  */  
   actRevisionUID:number,
}

export interface ListMappedBooksWithRules_output{
   returnObj:string,
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param docLinePathSelection
      @param showAmountChild
      @param isEntityMenu
      @param showEntityEmptyOrBAQ
   */  
export interface LoadABTStructure_input{
   actTypeUID:number,
   actRevisionUID:number,
   docLinePathSelection:string,
   showAmountChild:boolean,
   isEntityMenu:boolean,
   showEntityEmptyOrBAQ:boolean,
}

export interface LoadABTStructure_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param isFullLoad
      @param developMode
      @param ds
   */  
export interface LoadACTBook_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  isFullLoad  */  
   isFullLoad:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadACTBook_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
   */  
export interface LoadACTType_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
}

export interface LoadACTType_output{
   returnObj:Erp_Tablesets_ACTTypeTableset[],
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param abtDocLineUID
      @param developMode
      @param ds
   */  
export interface LoadAmount_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  abtDocLineUID  */  
   abtDocLineUID:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param bookingRuleUID
      @param developMode
      @param ds
   */  
export interface LoadBROperation_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  bookingRuleUID  */  
   bookingRuleUID:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadBROperation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface LoadBookDataForImport_input{
   ds:Erp_Tablesets_ACTTypeImportBookTableset[],
}

export interface LoadBookDataForImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeImportBookTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param developMode
      @param ds
   */  
export interface LoadBookVar_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadBookVar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param aCTRevisionUID
   */  
export interface LoadBooks_input{
   aCTRevisionUID:number,
}

export interface LoadBooks_output{
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param functionUID
      @param developMode
      @param ds
   */  
export interface LoadBrFuncArgs_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  functionUID  */  
   functionUID:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadBrFuncArgs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param functionUID
      @param developMode
      @param ds
   */  
export interface LoadBrFuncOperation_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  functionUID  */  
   functionUID:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadBrFuncOperation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param abtDocLineUID
      @param abtQueryUID
      @param developMode
      @param ds
   */  
export interface LoadDocumentLineBAQParam_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  abtDocLineUID  */  
   abtDocLineUID:number,
      /**  abtQueryUID  */  
   abtQueryUID:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadDocumentLineBAQParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param abtDocLineUID
      @param developMode
      @param ds
   */  
export interface LoadDocumentLineBAQ_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  abtDocLineUID  */  
   abtDocLineUID:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadDocumentLineBAQ_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param abtDocLineUID
      @param isFullLoad
      @param developMode
      @param ds
   */  
export interface LoadDocumentLine_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  abtDocLineUID  */  
   abtDocLineUID:number,
      /**  isFullLoad  */  
   isFullLoad:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadDocumentLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param functionUID
      @param isFullLoad
      @param developMode
      @param ds
   */  
export interface LoadFunction_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  functionUID  */  
   functionUID:number,
      /**  isFullLoad  */  
   isFullLoad:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadFunction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param glControlType
   */  
export interface LoadGLCntrlTypes_input{
   glControlType:string,
}

export interface LoadGLCntrlTypes_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
}
}

   /** Required : 
      @param ds
      @param actTypeUID
      @param actRevisionUID
   */  
export interface LoadRevisionVersions_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
      /**  actTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
}

export interface LoadRevisionVersions_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param isFullLoad
      @param developMode
      @param ds
   */  
export interface LoadRevision_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  isFullLoad  */  
   isFullLoad:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadRevision_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param bookingRuleUID
      @param developMode
      @param ds
   */  
export interface LoadRuleVariables_input{
   actTypeUID:number,
   actRevisionUID:number,
   bookID:string,
   bookingRuleUID:number,
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadRuleVariables_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param bookingRuleUID
      @param isFullLoad
      @param developMode
      @param ds
   */  
export interface LoadRule_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  bookingRuleUID  */  
   bookingRuleUID:number,
      /**  isFullLoad  */  
   isFullLoad:number,
      /**  developMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param package
      @param actTypeName
      @param ds
   */  
export interface LoadSystemGLTransactionType_input{
      /**  Package  */  
   package:string,
      /**  GL Transaction type Name  */  
   actTypeName:string,
   ds:Erp_Tablesets_ACTTypeImportOpTableset[],
}

export interface LoadSystemGLTransactionType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeImportOpTableset,
   ErrorMess:string,
}
}

   /** Required : 
      @param lcdsContainer
      @param ds
   */  
export interface LoadTwoDatasetsTestMethod1_input{
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface LoadTwoDatasetsTestMethod1_output{
parameters : {
      /**  output parameters  */  
   lcdsContainer:Erp_Tablesets_LinkComboDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface OnBRFuncOperationContainerTypeChanging_input{
   proposedValue:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnBRFuncOperationContainerTypeChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnBRFuncOperationIsLogicalConditionChanged_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnBRFuncOperationIsLogicalConditionChanged_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface OnBROperationContainerTypeChanging_input{
   proposedValue:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnBROperationContainerTypeChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface OnBROperationCustomContainerTypeChanging_input{
   proposedValue:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnBROperationCustomContainerTypeChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnBROperationCustomIsLogicalConditionChanged_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnBROperationCustomIsLogicalConditionChanged_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnBROperationIsLogicalConditionChanged_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnBROperationIsLogicalConditionChanged_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param functionUID
      @param newFormula
   */  
export interface OnChangeBRFunctionFormula_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  functionUID  */  
   functionUID:number,
      /**  new formula  */  
   newFormula:string,
}

export interface OnChangeBRFunctionFormula_output{
}

   /** Required : 
      @param newType
      @param ds
   */  
export interface OnChangeBRFunctionPhraseElementArgType_input{
   newType:string,
   ds:Erp_Tablesets_ACTTypeSubDataTableset[],
}

export interface OnChangeBRFunctionPhraseElementArgType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeSubDataTableset,
}
}

   /** Required : 
      @param newText
      @param ds
      @param dsSub
   */  
export interface OnChangeBRFunctionPhraseElementText_input{
      /**  new element text  */  
   newText:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset[],
}

export interface OnChangeBRFunctionPhraseElementText_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
   dsSub:Erp_Tablesets_ACTTypeSubDataTableset,
}
}

   /** Required : 
      @param newType
      @param ds
   */  
export interface OnChangeBRFunctionPhraseElementType_input{
      /**  new type  */  
   newType:string,
   ds:Erp_Tablesets_ACTTypeSubDataTableset[],
}

export interface OnChangeBRFunctionPhraseElementType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeSubDataTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeBVRuleAction_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnChangeBVRuleAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param bookID
      @param ruleUID
      @param newName
   */  
export interface OnChangeBookingRuleName_input{
      /**  aCTTypeUID  */  
   actTypeUID:number,
      /**  actRevisionUID  */  
   actRevisionUID:number,
      /**  bookID  */  
   bookID:string,
      /**  ruleUID  */  
   ruleUID:number,
      /**  new DispalyName  */  
   newName:string,
}

export interface OnChangeBookingRuleName_output{
}

   /** Required : 
      @param iNewDataSource
      @param ds
   */  
export interface OnChangeEntityDataSource_input{
      /**  Proposed Value  */  
   iNewDataSource:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OnChangeEntityDataSource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ACTTypeUID
      @param ACTRevisionUID
      @param ABTDocLineUID
      @param BAQID
      @param NewBAQID
   */  
export interface OnChangingABTQuery_input{
      /**  ACTTypeUID  */  
   ACTTypeUID:number,
      /**  ACTRevisionUID  */  
   ACTRevisionUID:number,
      /**  ABTDocLineUID  */  
   ABTDocLineUID:number,
      /**  BAQID  */  
   BAQID:string,
      /**  NewBAQID  */  
   NewBAQID:string,
}

export interface OnChangingABTQuery_output{
}

   /** Required : 
      @param ACTTypeUID
      @param ACTRevisionUID
      @param ABTDocLineUID
      @param ABTPostEntityUID
      @param postCodePath
      @param newPostCode
   */  
export interface OnChangingPostCode_input{
      /**  ACTTypeUID  */  
   ACTTypeUID:number,
      /**  ACTRevisionUID  */  
   ACTRevisionUID:number,
      /**  ACTRevisionUID  */  
   ABTDocLineUID:number,
      /**  ABTPostEntityUID  */  
   ABTPostEntityUID:number,
      /**  postCodePath  */  
   postCodePath:string,
      /**  newPostCode  */  
   newPostCode:string,
}

export interface OnChangingPostCode_output{
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param ruleUID
      @param container
      @param containerType
      @param bookID
      @param docLinePath
      @param funcOperUID
      @param isLogicalCondition
      @param bindingSuffix
      @param proposedValue
      @param ds
   */  
export interface OperationFunctionUIDChanging_input{
   actTypeUID:number,
   actRevisionUID:number,
   ruleUID:number,
   container:string,
   containerType:string,
   bookID:string,
      /**  BRFunction.DocLinePath OR BookingRule.ForEach  */  
   docLinePath:string,
      /**  0 if not BRFuncOperation  */  
   funcOperUID:number,
   isLogicalCondition:boolean,
      /**  'Custom' if BROperation, 'FuncOper' of BRFuncOperation, '' if BROperation  */  
   bindingSuffix:string,
   proposedValue:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface OperationFunctionUIDChanging_output{
   returnObj:Erp_Tablesets_LinkComboDataTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param populationMethod
      @param developMode
      @param ds
   */  
export interface PopulationMethodChanging_input{
      /**  new populationMethod value  */  
   populationMethod:number,
      /**  flag DevelopMode  */  
   developMode:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface PopulationMethodChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PostCodeSourceRefresh_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface PostCodeSourceRefresh_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param clickedTag
      @param linkComboDS
      @param ds
   */  
export interface ProcessFormulaParamClickCustom_input{
   clickedTag:string,
   linkComboDS:Erp_Tablesets_LinkComboDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ProcessFormulaParamClickCustom_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   linkComboDS:Erp_Tablesets_LinkComboDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param clickedTag
      @param linkComboDS
      @param ds
   */  
export interface ProcessFormulaParamClickFuncOper_input{
   clickedTag:string,
   linkComboDS:Erp_Tablesets_LinkComboDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ProcessFormulaParamClickFuncOper_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   linkComboDS:Erp_Tablesets_LinkComboDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param clickedTag
      @param linkComboDS
      @param ds
   */  
export interface ProcessFormulaParamClick_input{
   clickedTag:string,
   linkComboDS:Erp_Tablesets_LinkComboDataTableset[],
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface ProcessFormulaParamClick_output{
   returnObj:Erp_Tablesets_ACTTypeSubDataTableset[],
parameters : {
      /**  output parameters  */  
   value:string,
   dataType:string,
   linkComboDS:Erp_Tablesets_LinkComboDataTableset,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param aCTRevisionUID
   */  
export interface RefreshBookList_input{
      /**  ACTRevisionUID  */  
   aCTRevisionUID:number,
}

export interface RefreshBookList_output{
}

   /** Required : 
      @param actTypeCopyFromUID
      @param revisionCopyFromUID
      @param isDocOnly
   */  
export interface RevisionCopyFrom_input{
      /**  actTypeCopyFromUID  */  
   actTypeCopyFromUID:number,
      /**  RevisionCopyFromUID  */  
   revisionCopyFromUID:number,
      /**  isDocOnly  */  
   isDocOnly:boolean,
}

export interface RevisionCopyFrom_output{
parameters : {
      /**  output parameters  */  
   newRevUID:number,
}
}

   /** Required : 
      @param proposedValue
      @param developMode
      @param answer
      @param ds
   */  
export interface RevisionStatusChanging_input{
      /**  proposed value of Revision Status  */  
   proposedValue:string,
      /**  Developer mode  */  
   developMode:boolean,
      /**  User's answer on question. For second pass.  */  
   answer:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface RevisionStatusChanging_output{
parameters : {
      /**  output parameters  */  
   question:string,
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param dataType
      @param ABTField
      @param ds
   */  
export interface SelectionCriteriaAddOnClick_input{
   dataType:string,
   ABTField:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface SelectionCriteriaAddOnClick_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface TableDataFieldChanging_input{
   proposedValue:string,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface TableDataFieldChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param companyName
      @param aCTTypeUID
      @param aCTRevisionUID
   */  
export interface TryCompile_input{
      /**  Company ID  */  
   companyName:string,
      /**  ACTType ID  */  
   aCTTypeUID:number,
      /**  ACTRevision ID  */  
   aCTRevisionUID:number,
}

export interface TryCompile_output{
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param ds
   */  
export interface UndoUpdateVersionsWithRefreshDS_input{
      /**  ACTTypeUID  */  
   actTypeUID:number,
      /**  ACTRevisionUID  */  
   actRevisionUID:number,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface UndoUpdateVersionsWithRefreshDS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtACTTypeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtACTTypeTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateTwoDatasetsTestMethod1_input{
   ds:Erp_Tablesets_LinkComboDataTableset[],
}

export interface UpdateTwoDatasetsTestMethod1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LinkComboDataTableset,
}
}

   /** Required : 
      @param actTypeUID
      @param actRevisionUID
      @param updatePatchVer
      @param ds
   */  
export interface UpdateVersionsWithRefreshDS_input{
      /**  ACTTypeUID  */  
   actTypeUID:number,
      /**  ACTRevisionUID  */  
   actRevisionUID:number,
      /**  it is true if need update Patch Versions  */  
   updatePatchVer:boolean,
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface UpdateVersionsWithRefreshDS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ACTTypeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeTableset,
}
}

   /** Required : 
      @param actTypeName
      @param newRevCode
      @param newABTVer
      @param newPatchABTVer
      @param updateMode
      @param importABT
      @param importRulseset
   */  
export interface ValidateABTVerForImport_input{
      /**  ACTType Name  */  
   actTypeName:string,
      /**  New RevisionCode  */  
   newRevCode:string,
      /**  New ABT Version  */  
   newABTVer:string,
      /**  New Patch ABT Version  */  
   newPatchABTVer:string,
      /**  In Update Mode  */  
   updateMode:boolean,
      /**  Need Import ABT Structure  */  
   importABT:boolean,
      /**  Need Import Ruleset  */  
   importRulseset:boolean,
}

export interface ValidateABTVerForImport_output{
parameters : {
      /**  output parameters  */  
   outCanBeImported:boolean,
   outCanBeActivated:boolean,
   outMessage:string,
}
}

   /** Required : 
      @param ipCOAMapUID
      @param ipSourceCOA
      @param ipMappedCOA
   */  
export interface ValidateCOAMap_input{
   ipCOAMapUID:number,
   ipSourceCOA:string,
   ipMappedCOA:string,
}

export interface ValidateCOAMap_output{
}

