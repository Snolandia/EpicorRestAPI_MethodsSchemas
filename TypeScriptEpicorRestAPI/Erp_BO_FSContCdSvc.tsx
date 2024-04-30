import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.FSContCdSvc
// Description: Field Service Contract Codes
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get FSContCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContCds
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContCdRow
   */  
export function get_FSContCds(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/FSContCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContCds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FSContCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSContCds(requestBody:Erp_Tablesets_FSContCdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/FSContCds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FSContCd item
   Description: Calls GetByID to retrieve the FSContCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractCode Desc: ContractCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FSContCdRow
   */  
export function get_FSContCds_Company_ContractCode(Company:string, ContractCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/FSContCds(" + Company + "," + ContractCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSContCd for the service
   Description: Calls UpdateExt to update FSContCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractCode Desc: ContractCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSContCds_Company_ContractCode(Company:string, ContractCode:string, requestBody:Erp_Tablesets_FSContCdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/FSContCds(" + Company + "," + ContractCode + ")", {
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
   Summary: Call UpdateExt to delete FSContCd item
   Description: Call UpdateExt to delete FSContCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractCode Desc: ContractCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSContCds_Company_ContractCode(Company:string, ContractCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/FSContCds(" + Company + "," + ContractCode + ")", {
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
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractCode Desc: ContractCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_FSContCds_Company_ContractCode_EntityGLCs(Company:string, ContractCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/FSContCds(" + Company + "," + ContractCode + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractCode Desc: ContractCode   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_FSContCds_Company_ContractCode_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, ContractCode:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/FSContCds(" + Company + "," + ContractCode + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:Erp_Tablesets_EntityGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:Erp_Tablesets_EntityGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContCdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContCdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContCdListRow)
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
export function get_GetRows(whereClauseFSContCd:string, whereClauseEntityGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFSContCd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSContCd=" + whereClauseFSContCd
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(contractCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof contractCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractCode=" + contractCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method ChangeDeferredRev
   Description: Performs required logic when FSContCd.DeferredRev is modified.
   OperationID: ChangeDeferredRev
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDeferredRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDeferredRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDeferredRev(requestBody:ChangeDeferredRev_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDeferredRev_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeDeferredRev", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDeferredRev_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalCal
   Description: Performs required logic when FSContCd.FiscalCalendarID is modified.
   OperationID: ChangeFiscalCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalCal(requestBody:ChangeFiscalCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeFiscalCal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFiscalCal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoted
   Description: This method should be called to set Quoted.
   OperationID: ChangeQuoted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuoted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoted(requestBody:ChangeQuoted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuoted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeQuoted", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeQuoted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRACode
   Description: Performs required logic when FSContCd.RACode is modified.
   OperationID: ChangeRACode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRACode(requestBody:ChangeRACode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRACode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeRACode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRACode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRecurringInv
   Description: This method should be called to set Recurring Inv.
   OperationID: ChangeRecurringInv
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRecurringInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRecurringInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRecurringInv(requestBody:ChangeRecurringInv_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRecurringInv_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeRecurringInv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRecurringInv_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRenewable
   Description: This method should be called to set RenewalCode and ShipRenewal when Renewable = false.
   OperationID: ChangeRenewable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRenewable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRenewable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRenewable(requestBody:ChangeRenewable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRenewable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeRenewable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRenewable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRenewalCode
   Description: Purpose:
Parameters:
<param name="ipRenewalCode">proposed renewal code</param><param name="ds"> FSContCd data set </param>
Notes:
   OperationID: ChangeRenewalCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRenewalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRenewalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRenewalCode(requestBody:ChangeRenewalCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRenewalCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeRenewalCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRenewalCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaskSet
   Description: Performs required logic when FSContCd.TaskSetID is modified.
   OperationID: ChangeTaskSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaskSet(requestBody:ChangeTaskSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaskSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ChangeTaskSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTaskSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Returns a list of code descriptions
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ValidateServiceContract
   Description: Method names longer than 50 characters not supported by Service Designer.
This is why the name is smaller and not so descriptive.
Validates if exists a Valid Service Contract (specified date less than ServiceContract.ExpireDate)
for the specified Contract Code that is Send To FSA.
   OperationID: ValidateServiceContract
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateServiceContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateServiceContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateServiceContract(requestBody:ValidateServiceContract_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateServiceContract_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/ValidateServiceContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateServiceContract_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSContCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContCd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFSContCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSContCd(requestBody:GetNewFSContCd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFSContCd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetNewFSContCd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFSContCd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:GetNewEntityGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEntityGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEntityGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSContCdSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContCdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContCdListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContCdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContCdRow,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContCdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the contract assigned by the user.  */  
   "ContractCode":string,
      /**  Description of the service contract.  */  
   "ContractDescription":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContCdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the contract assigned by the user.  */  
   "ContractCode":string,
      /**  Description of the service contract.  */  
   "ContractDescription":string,
      /**  Duration that the service contract is in effect.  */  
   "Duration":number,
      /**  Whether the duration is in days, months or years.  */  
   "Modifier":string,
      /**  Determines whether or not material costs are covered by the warranty.  */  
   "Material":boolean,
      /**  Determines whether or not labor costs are covered by the warranty.  */  
   "Labor":boolean,
      /**  Determines whether or not miscellaneous costs are covered by the warranty.  */  
   "Misc":boolean,
      /**  ***Search the code to see if this field is referenced anywhere. If not, remove it from the database.  */  
   "Closed":boolean,
      /**  The unit price of the service contract. Note: Used in conjunction with the PricePer and RecurringInv fields.  */  
   "UnitPrice":number,
      /**  Comments about the service contract. Will print on the Sales Order Acknowledgement and Service Call Ticket forms.  */  
   "CommentText":string,
      /**  Determines whether or not this contract is for onsite service calls.  */  
   "OnSite":boolean,
      /**  Indicates whether or not the service contract will be invoiced on a recurring basis.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated. Currently the only option is monthly.  */  
   "RecurringFreq":string,
      /**  Modifier used in determining the service contract's price. Daily, Monthly and Contract are the available choices. Note: Used in conjunction with the UnitPrice and RecurringInv fields.  */  
   "PricePer":string,
      /**  The Tax Category (TaxCat.TaxCatID) assigned to the service contract.  */  
   "TaxCatID":string,
      /**  Marks this FSContCd as global, available to be sent out to other companies.  */  
   "GlobalFSContCd":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Indicates whether or not a contract must be shipped before it can be invoiced.  */  
   "ShipContract":boolean,
      /**  Identifies the parameters used for renewing a contract.  */  
   "RenewalCode":string,
      /**  Indicates whether or not the renewal must be shiped before it can be invoiced.  */  
   "ShipRenewal":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates how often an invoice is generated for the contract  */  
   "FiscalCalendarID":string,
      /**  Indicates if the contract that uses this contract code is valid for renewal.  */  
   "Renewable":boolean,
      /**  Indicates if a quote needs to be created and approved by the customer before a contract can be invoiced.  */  
   "QuotedContract":boolean,
      /**  Indicates the task set used when creating a quote for a contract renewal  */  
   "TaskSetID":string,
      /**  Determines if the Service Contract has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  Fiscal Calendar Description  */  
   "FiscalCalDescription":string,
      /**  Task Set Description  */  
   "TaskSetDescription":string,
      /**  Tax Category Description  */  
   "TaxCatDesc":string,
   "BitFlag":number,
   "CompanySendToFSA":boolean,
   "RASchedCdRADesc":string,
   "TaxCatIDDescription":string,
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
      @param ipDeferredRev
      @param ds
   */  
export interface ChangeDeferredRev_input{
      /**  Proposed input value of Deferred Rev  */  
   ipDeferredRev:boolean,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeDeferredRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ipFiscalCal
      @param ds
   */  
export interface ChangeFiscalCal_input{
      /**  Proposed input value of FiscalCalendarID  */  
   ipFiscalCal:string,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeFiscalCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ipQuoted
      @param ds
   */  
export interface ChangeQuoted_input{
      /**  Quoted.  */  
   ipQuoted:boolean,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeQuoted_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ipRACode
      @param ds
   */  
export interface ChangeRACode_input{
      /**  Proposed input value of RA Code  */  
   ipRACode:string,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeRACode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ipRecurInv
      @param ds
   */  
export interface ChangeRecurringInv_input{
      /**  Recurring Invoice.  */  
   ipRecurInv:boolean,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeRecurringInv_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ipRenewable
      @param ds
   */  
export interface ChangeRenewable_input{
      /**  Renewal true or false code  */  
   ipRenewable:boolean,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeRenewable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ipRenewalCode
      @param ds
   */  
export interface ChangeRenewalCode_input{
   ipRenewalCode:string,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeRenewalCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ipTaskSet
      @param ds
   */  
export interface ChangeTaskSet_input{
      /**  Proposed input value of TaskSetID  */  
   ipTaskSet:string,
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface ChangeTaskSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param contractCode
   */  
export interface DeleteByID_input{
   contractCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContCdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the contract assigned by the user.  */  
   ContractCode:string,
      /**  Description of the service contract.  */  
   ContractDescription:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContCdListTableset{
   FSContCdList:Erp_Tablesets_FSContCdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FSContCdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the contract assigned by the user.  */  
   ContractCode:string,
      /**  Description of the service contract.  */  
   ContractDescription:string,
      /**  Duration that the service contract is in effect.  */  
   Duration:number,
      /**  Whether the duration is in days, months or years.  */  
   Modifier:string,
      /**  Determines whether or not material costs are covered by the warranty.  */  
   Material:boolean,
      /**  Determines whether or not labor costs are covered by the warranty.  */  
   Labor:boolean,
      /**  Determines whether or not miscellaneous costs are covered by the warranty.  */  
   Misc:boolean,
      /**  ***Search the code to see if this field is referenced anywhere. If not, remove it from the database.  */  
   Closed:boolean,
      /**  The unit price of the service contract. Note: Used in conjunction with the PricePer and RecurringInv fields.  */  
   UnitPrice:number,
      /**  Comments about the service contract. Will print on the Sales Order Acknowledgement and Service Call Ticket forms.  */  
   CommentText:string,
      /**  Determines whether or not this contract is for onsite service calls.  */  
   OnSite:boolean,
      /**  Indicates whether or not the service contract will be invoiced on a recurring basis.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated. Currently the only option is monthly.  */  
   RecurringFreq:string,
      /**  Modifier used in determining the service contract's price. Daily, Monthly and Contract are the available choices. Note: Used in conjunction with the UnitPrice and RecurringInv fields.  */  
   PricePer:string,
      /**  The Tax Category (TaxCat.TaxCatID) assigned to the service contract.  */  
   TaxCatID:string,
      /**  Marks this FSContCd as global, available to be sent out to other companies.  */  
   GlobalFSContCd:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Indicates whether or not a contract must be shipped before it can be invoiced.  */  
   ShipContract:boolean,
      /**  Identifies the parameters used for renewing a contract.  */  
   RenewalCode:string,
      /**  Indicates whether or not the renewal must be shiped before it can be invoiced.  */  
   ShipRenewal:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates how often an invoice is generated for the contract  */  
   FiscalCalendarID:string,
      /**  Indicates if the contract that uses this contract code is valid for renewal.  */  
   Renewable:boolean,
      /**  Indicates if a quote needs to be created and approved by the customer before a contract can be invoiced.  */  
   QuotedContract:boolean,
      /**  Indicates the task set used when creating a quote for a contract renewal  */  
   TaskSetID:string,
      /**  Determines if the Service Contract has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Fiscal Calendar Description  */  
   FiscalCalDescription:string,
      /**  Task Set Description  */  
   TaskSetDescription:string,
      /**  Tax Category Description  */  
   TaxCatDesc:string,
   BitFlag:number,
   CompanySendToFSA:boolean,
   RASchedCdRADesc:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContCdTableset{
   FSContCd:Erp_Tablesets_FSContCdRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFSContCdTableset{
   FSContCd:Erp_Tablesets_FSContCdRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param contractCode
   */  
export interface GetByID_input{
   contractCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FSContCdTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FSContCdTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FSContCdTableset[],
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
   returnObj:Erp_Tablesets_FSContCdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_FSContCdTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFSContCd_input{
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface GetNewFSContCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param whereClauseFSContCd
      @param whereClauseEntityGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFSContCd:string,
   whereClauseEntityGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FSContCdTableset[],
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
   ds:Erp_Tablesets_UpdExtFSContCdTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFSContCdTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FSContCdTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSContCdTableset,
}
}

   /** Required : 
      @param companyId
      @param contractCode
      @param effectiveDate
   */  
export interface ValidateServiceContract_input{
      /**  Company Id.  */  
   companyId:string,
      /**  Contract Code  */  
   contractCode:string,
      /**  Datetime to validate.  */  
   effectiveDate:string,
}

export interface ValidateServiceContract_output{
   returnObj:boolean,
}

