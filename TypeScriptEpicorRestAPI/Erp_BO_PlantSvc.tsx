import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PlantSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/$metadata", {
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
   Description: Get Plants items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Plants
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantRow
   */  
export function get_Plants(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Plants
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Plants(requestBody:Erp_Tablesets_PlantRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Plant item
   Description: Calls GetByID to retrieve the Plant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Plant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant1 Desc: Plant1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantRow
   */  
export function get_Plants_Company_Plant1(Company:string, Plant1:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")", {
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
         resolve(data as Erp_Tablesets_PlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Plant for the service
   Description: Calls UpdateExt to update Plant. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Plant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant1 Desc: Plant1   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Plants_Company_Plant1(Company:string, Plant1:string, requestBody:Erp_Tablesets_PlantRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")", {
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
   Summary: Call UpdateExt to delete Plant item
   Description: Call UpdateExt to delete Plant item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Plant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant1 Desc: Plant1   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Plants_Company_Plant1(Company:string, Plant1:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")", {
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
   Description: Get PlantEGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantEGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant1 Desc: Plant1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantEGLCRow
   */  
export function get_Plants_Company_Plant1_PlantEGLCs(Company:string, Plant1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")/PlantEGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantEGLC item
   Description: Calls GetByID to retrieve the PlantEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantEGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant1 Desc: Plant1   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantEGLCRow
   */  
export function get_Plants_Company_Plant1_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, Plant1:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlantAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant1 Desc: Plant1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantAttchRow
   */  
export function get_Plants_Company_Plant1_PlantAttches(Company:string, Plant1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")/PlantAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantAttch item
   Description: Calls GetByID to retrieve the PlantAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant1 Desc: Plant1   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantAttchRow
   */  
export function get_Plants_Company_Plant1_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant1:string, Plant:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PlantEGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantEGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantEGLCRow
   */  
export function get_PlantEGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantEGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantEGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantEGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantEGLCs(requestBody:Erp_Tablesets_PlantEGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantEGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantEGLC item
   Description: Calls GetByID to retrieve the PlantEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantEGLC
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
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantEGLCRow
   */  
export function get_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantEGLC for the service
   Description: Calls UpdateExt to update PlantEGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantEGLC
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
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:Erp_Tablesets_PlantEGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete PlantEGLC item
   Description: Call UpdateExt to delete PlantEGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantEGLC
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
export function delete_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get PlantAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantAttchRow
   */  
export function get_PlantAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantAttches(requestBody:Erp_Tablesets_PlantAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantAttch item
   Description: Calls GetByID to retrieve the PlantAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantAttchRow
   */  
export function get_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantAttch for the service
   Description: Calls UpdateExt to update PlantAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, requestBody:Erp_Tablesets_PlantAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PlantAttch item
   Description: Call UpdateExt to delete PlantAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantListRow)
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
export function get_GetRows(whereClausePlant:string, whereClausePlantAttch:string, whereClausePlantEGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePlant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlant=" + whereClausePlant
   }
   if(typeof whereClausePlantAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantAttch=" + whereClausePlantAttch
   }
   if(typeof whereClausePlantEGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantEGLC=" + whereClausePlantEGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetRows" + params, {
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
export function get_GetByID(plant:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetByID" + params, {
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
   Summary: Invoke method GetNewPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlant(requestBody:GetNewPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetNewPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRegion
   Description: Checks whether Region code exists and active.
   OperationID: CheckRegion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRegion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRegion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRegion(requestBody:CheckRegion_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRegion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/CheckRegion", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRegion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ETCAfterAddrVal
   Description: After the tax integration has been called, update the Plant address if it
was changed.
   OperationID: ETCAfterAddrVal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ETCAfterAddrVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCAfterAddrVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ETCAfterAddrVal(requestBody:ETCAfterAddrVal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ETCAfterAddrVal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/ETCAfterAddrVal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ETCAfterAddrVal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ETCValidateAddress
   Description: Call tax integration and loads temp tables from the results.
   OperationID: ETCValidateAddress
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ETCValidateAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCValidateAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ETCValidateAddress(requestBody:ETCValidateAddress_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ETCValidateAddress_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/ETCValidateAddress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ETCValidateAddress_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllPlants
   Description: Get all plants related with the company loaded and authorized for the current user
   OperationID: GetAllPlants
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllPlants_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllPlants(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllPlants_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetAllPlants", {
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
         resolve(data as GetAllPlants_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompleteList
   Description: This method is the same as GetList(), except that it causes a bypass of the call to
removeUnauthorizedRows.  It is to be used only in the situations where the
user is allowed to see Plants for which they are not authorized, such as in
this example from Vantage Help for Multi-Plant Management:
The selection list for Plants will include all Plants for the To option
when creating Plant to Plant transfers. However, when receiving a Plant
to Plant transfer the user must be authorized to the receiving Plant.
   OperationID: GetCompleteList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCompleteList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompleteList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompleteList(requestBody:GetCompleteList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCompleteList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetCompleteList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCompleteList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDisabledFields
   Description: This method will send a list of fields to be disabled on the UI
side if either the Multi-Plant or Advanced Planning and Scheduling
license is not available or MRP, data collection and field service.
   OperationID: GetDisabledFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisabledFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDisabledFields(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDisabledFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetDisabledFields", {
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
         resolve(data as GetDisabledFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsAuthorizedForPlant
   Description: IsAuthorizedForPlant determines whether the logged user is allowed to access a specific plant
   OperationID: IsAuthorizedForPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsAuthorizedForPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAuthorizedForPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsAuthorizedForPlant(requestBody:IsAuthorizedForPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsAuthorizedForPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/IsAuthorizedForPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsAuthorizedForPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfCalendarID
   Description: This method validates the CalendarID
   OperationID: OnChangeOfCalendarID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfCalendarID(requestBody:OnChangeOfCalendarID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfCalendarID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/OnChangeOfCalendarID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfCalendarID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PlantCostIDChanged
   Description: This method should be called anytime the PlantCostID is changed when updating a plant record (this
method does not need to be called when adding a record).  This method returns message text to
present to the user in question form.  The question informs the user Plant General Ledger Cost
values will need to be updated, do they wish to continue with this change.
   OperationID: PlantCostIDChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PlantCostIDChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantCostIDChanged(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PlantCostIDChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/PlantCostIDChanged", {
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
         resolve(data as PlantCostIDChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSystemTimeZoneList
   Description: This method returns a list of Microsoft Time Zone Index Values and their corresponding display name
   OperationID: GetSystemTimeZoneList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemTimeZoneList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSystemTimeZoneList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSystemTimeZoneList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetSystemTimeZoneList", {
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
         resolve(data as GetSystemTimeZoneList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckUDCodesExistence
   Description: CheckUDCodesExistence
   OperationID: CheckUDCodesExistence
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckUDCodesExistence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUDCodesExistence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckUDCodesExistence(requestBody:CheckUDCodesExistence_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckUDCodesExistence_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/CheckUDCodesExistence", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckUDCodesExistence_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListPlants
   Description: Returns a List Dataset for GetListPlants
   OperationID: GetListPlants
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListPlants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPlants_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListPlants(requestBody:GetListPlants_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListPlants_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetListPlants", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListPlants_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListAuthorizedPlants
   Description: Returns a List Dataset for Authorized Plants
   OperationID: GetListAuthorizedPlants
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListAuthorizedPlants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAuthorizedPlants_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListAuthorizedPlants(requestBody:GetListAuthorizedPlants_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListAuthorizedPlants_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetListAuthorizedPlants", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListAuthorizedPlants_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UploadLogoImage
   Description: Upload logo image
   OperationID: UploadLogoImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UploadLogoImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadLogoImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadLogoImage(requestBody:UploadLogoImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UploadLogoImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/UploadLogoImage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UploadLogoImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateLogoImage
   Description: Update logo image in database
   OperationID: UpdateLogoImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateLogoImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLogoImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateLogoImage(requestBody:UpdateLogoImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateLogoImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/UpdateLogoImage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateLogoImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckVATFormat
   Description: This method test the validity of the VAT format
   OperationID: CheckVATFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckVATFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVATFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckVATFormat(requestBody:CheckVATFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckVATFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/CheckVATFormat", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckVATFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantAttch(requestBody:GetNewPlantAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetNewPlantAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantEGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantEGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantEGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantEGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantEGLC(requestBody:GetNewPlantEGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantEGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetNewPlantEGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantEGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantEGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantRow,
}

export interface Erp_Tablesets_PlantAttchRow{
   "Company":string,
   "Plant":string,
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

export interface Erp_Tablesets_PlantEGLCRow{
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
      /**  Plant  */  
   "Plant":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  The Site name. Used on shipping reports.  */  
   "Name":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantRow{
      /**  Company Identifier.  */  
   "Company":string,
   "Plant1":string,
      /**  The Site name. Used on shipping reports.  */  
   "Name":string,
      /**  Site address line 1.  */  
   "Address1":string,
      /**  Site address line 2.  */  
   "Address2":string,
      /**  Site address line 3.  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Main phone number of the Site.  */  
   "PhoneNum":string,
      /**  Main fax number of the Site.  */  
   "FaxNum":string,
      /**  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  */  
   "CommentText":string,
      /**  Number of days early that a supply source (Job or PO) can be without MRP suggesting to postpone the supply.  */  
   "PlanningExceptionDays":number,
      /**  Intrastat Region  */  
   "ISRegion":string,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   "PlantCostID":string,
      /**  Lead Time added to the mfg item to determine the start date.  */  
   "PrepTime":number,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   "KitTime":number,
      /**  If checked, then Transfer Orders will be created when the requirement is marked as "firm".  */  
   "ReqTransferHeader":boolean,
      /**  Identifies the default Production Calendar for this Site.   If this equals "", then the ProdCal record is the Company level production calendar.  */  
   "CalendarID":string,
      /**  Transfer Shipment entry action to a Transfer Order.  Valid values are "WARN", "STOP" or "NONE" .  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the shipment and transfer request does not have a header.  STOP means that the request cannot be added to the shipment.  NONE allows the request to be added to the shipment with no warnings.  */  
   "AllowShipAction":string,
      /**  Number of days before a sugestion is automatically converted to a firmed requirement.  */  
   "AutoConfirmWindow":number,
      /**  When this field is checked then if transfer orders are being created automatically then each suggestion will create a separate transfer order  */  
   "SingleLineOrder":boolean,
      /**  Maximum Operation Start Delay  */  
   "MaxOpStartDelay":number,
      /**  Maximum Operation Length  */  
   "MaxOpLength":number,
      /**  Default Station ID for the Site  */  
   "DefStationID":string,
      /**  Number of days to the end of the finite horizon window  */  
   "FiniteHorz":number,
      /**  Used by MRP.  */  
   "NextUnfirmJob":string,
      /**  Used by MRP.  */  
   "NextUnfirmTFLine":string,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  Number of days to the beginning of the rough cut scheduling horizon window  */  
   "RCutHorz":number,
      /**  Include lead time in manufacturing lead time calculation  */  
   "IncLeadTime":boolean,
      /**  Include transfer lead time in manufacturing lead time calculation  */  
   "IncTransLeadTime":boolean,
      /**  Include receive time in manufacturing lead time calculation  */  
   "IncReceiveTime":boolean,
      /**  Include kit time in manufacturing lead time calculation  */  
   "IncKitTime":boolean,
      /**  Include rough cut parameters in manufacturing lead time calculation  */  
   "IncRCParams":boolean,
      /**  Defines the number of days from the current date the scheduling uses to create job records within the Shop Load table.  */  
   "OverloadHorz":number,
      /**   Determines if the start-to-start job operation offset will be used for production or setup time.  If setup

is chosen, a secondary operation with a start to start relationship will schedule setup to begin xxx 

minutes (defined in the operation) after the production starts on the primary operation.  If production is 

chosen then the production time of the secondary operation will be scheduled to start xxx minutes after the 

production starts on the primary operation.  */  
   "SchedulingSendAhead":string,
      /**  Unfirm Series Horizon  */  
   "UnfirmSeriesHorizon":number,
      /**  AutoFirmHorizon  */  
   "AutoFirmHorizon":number,
      /**  Name of the person responsible for delivery  */  
   "ManagerName":string,
      /**  Branch ID (Used Primary for Thailand Localization)  */  
   "BranchID":string,
      /**  Pertains to Maintenance Management. Site which performs Equipment Maintenance for the this Site.  Note; Maintenance will be allowed in Equipments Site or MaintSite of it's Site.  */  
   "MaintPlant":string,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Site Description 1  */  
   "SiteDesc1":string,
      /**  Site Description 2  */  
   "SiteDesc2":string,
      /**  Site Type: 0-Normal, 2-Main Site, 3-Sub Site, 5-Consolidated  */  
   "SiteType":string,
      /**  Business Type Code  */  
   "BusinessTypeCode":string,
      /**  Business Type Description 1  */  
   "BusTypeDesc1":string,
      /**  Business Type Description 2  */  
   "BusTypeDesc2":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGDefaultInvoicingPoint  */  
   "AGDefaultInvoicingPoint":string,
      /**  It will force the times to be Start to Start when scheduling this kind of operations.  */  
   "ForceSSTime":boolean,
      /**  It will force the times to be Finish to Finish when scheduling this kind of operations  */  
   "ForceFFTime":boolean,
      /**  Within the leadtime window (MRP Start Date + Lead Time) use Lead Time Days of supply logic in place of standard days of supply  */  
   "UseLeadTimeDOS":boolean,
      /**  Within the lead time window, allow consumption of minimum qty until below safety  */  
   "AllowMinQty":boolean,
      /**  It will allow the user to move the job in regardless of material constraints and Subcontract PO?s  */  
   "IgnoreMtlConstraints":boolean,
      /**  AGProvinceCode  */  
   "AGProvinceCode":string,
      /**  AGLocationCode  */  
   "AGLocationCode":string,
      /**  AGNeighborhood  */  
   "AGNeighborhood":string,
      /**  AGStreet  */  
   "AGStreet":string,
      /**  AGStreetNumber  */  
   "AGStreetNumber":string,
      /**  AGExtraStreetNumber  */  
   "AGExtraStreetNumber":string,
      /**  AGFloor  */  
   "AGFloor":string,
      /**  AGApartment  */  
   "AGApartment":string,
      /**  MXMunicipio  */  
   "MXMunicipio":string,
      /**  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  */  
   "MaxLateDaysPORel":number,
      /**  Obsolete  */  
   "INECCNumber":string,
      /**  Obsolete  */  
   "INExciseRange":string,
      /**  Obsolete  */  
   "INExciseDivision":string,
      /**  Obsolete  */  
   "INExCommissionRate":string,
      /**  INTINNumber  */  
   "INTINNumber":string,
      /**  Obsolete  */  
   "INCSTNumber":string,
      /**  Obsolete  */  
   "INSTRegistration":string,
      /**  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  */  
   "UseSchedulingMultiJob":boolean,
      /**  Will allow to auto load all child jobs related to the selected job at the Job Scheduling Board.  */  
   "AutoLoadChildJobs":boolean,
      /**  Will allow to auto load all parent jobs related to the selected job at the Job Scheduling Board.  */  
   "AutoLoadParentJobs":boolean,
      /**  Indicate to schedule engine to get the final date of the parent job and do backwards all the group of jobs to minimize gaps.  */  
   "MinimizeWIP":boolean,
      /**  Time Zone of the site.  */  
   "TimeZoneID":string,
      /**  Not used.  */  
   "TimeZoneAdjustForDST":boolean,
      /**  SyncReqBy  */  
   "SyncReqBy":boolean,
      /**  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  */  
   "ACWPercentage":number,
      /**  It is the time used for schedule engine when scheduling backwards automatically. In some screens it is just a default and can be modified before scheduling.  */  
   "BWSchedStartTime":number,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  Determines if the Plant has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  Determines the schedule direction that will default when manually scheduling a job. The following screens will be impacted by this setting: Job Entry, Service Job Entry, Maintenance Job Entry, Job Scheduling Board, Multi Resource Scheduling Board, Resource Scheduling Board, Job Manager, Project Entry.  */  
   "SchedulingDirection":string,
      /**  US1099PayersTIN  */  
   "US1099PayersTIN":string,
      /**  US1099NameControl  */  
   "US1099NameControl":string,
      /**  US1099OfficeCode  */  
   "US1099OfficeCode":string,
      /**  US1099ContactPerson  */  
   "US1099ContactPerson":string,
      /**  US1099EmailAddress  */  
   "US1099EMailAddress":string,
      /**  US1099FaxNum  */  
   "US1099FaxNum":string,
      /**  US1099PhoneNum  */  
   "US1099PhoneNum":string,
      /**  US1099TransControlCode  */  
   "US1099TransControlCode":string,
      /**  US1099Name1  */  
   "US1099Name1":string,
      /**  US1099Name2  */  
   "US1099Name2":string,
      /**  US1099Address1  */  
   "US1099Address1":string,
      /**  US1099Address2  */  
   "US1099Address2":string,
      /**  US1099Address3  */  
   "US1099Address3":string,
      /**  US1099City  */  
   "US1099City":string,
      /**  US1099State  */  
   "US1099State":string,
      /**  US1099ZIP  */  
   "US1099ZIP":string,
      /**  TaxID  */  
   "TaxID":string,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
      /**  Reason code for cost code change.  */  
   "ReasonCode":string,
      /**  Reason code required flag.  */  
   "ReasonReq":boolean,
      /**  Reason type  */  
   "ReasonType":string,
      /**  Indicates if the scheduling logic in the system is not used because a third party scheduling.  */  
   "Use3rdPartySched":boolean,
      /**  Reason Code Description  */  
   "ReasonCodeDescription":string,
      /**  Background color for site (Kinetic UI).  */  
   "KineticColor":string,
   "LogoFileName":string,
   "LogoImageContent":string,
      /**  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  */  
   "MXISTMO":string,
   "BitFlag":number,
   "AGLocationDescription":string,
   "AGProvinceCodeDescription":string,
   "CalendarIDDescription":string,
   "CompanySendToFSA":boolean,
   "CountryNumDescription":string,
   "MaintPlantName":string,
   "PlantCostDescription":string,
   "XbSystSiteIsLegalEntity":boolean,
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
      @param cCodeID
   */  
export interface CheckRegion_input{
      /**  Code ID for check.  */  
   cCodeID:string,
}

export interface CheckRegion_output{
}

   /** Required : 
      @param cCodeID
   */  
export interface CheckUDCodesExistence_input{
   cCodeID:string,
}

export interface CheckUDCodesExistence_output{
parameters : {
      /**  output parameters  */  
   lUDCodeExists:boolean,
}
}

   /** Required : 
      @param taxID
   */  
export interface CheckVATFormat_input{
      /**  tax ID  */  
   taxID:string,
}

export interface CheckVATFormat_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param ds1
      @param PlantID
   */  
export interface ETCAfterAddrVal_input{
   ds:Erp_Tablesets_PlantTableset[],
   ds1:Erp_Tablesets_ETCAddrValidationTableset[],
      /**  Plant.Plant  */  
   PlantID:string,
}

export interface ETCAfterAddrVal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset,
}
}

   /** Required : 
      @param PlantID
   */  
export interface ETCValidateAddress_input{
      /**  Plant.Plant  */  
   PlantID:string,
}

export interface ETCValidateAddress_output{
   returnObj:Erp_Tablesets_ETCAddrValidationTableset[],
parameters : {
      /**  output parameters  */  
   StatusFlag:boolean,
   ErrorFlag:boolean,
   ErrorMsg:string,
}
}

export interface Erp_Tablesets_ETCAddrValidationTableset{
   ETCAddress:Erp_Tablesets_ETCAddressRow[],
   ETCMessage:Erp_Tablesets_ETCMessageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ETCAddressRow{
      /**  Company  */  
   Company:string,
      /**  City name  */  
   City:string,
      /**  Country name  */  
   Country:string,
      /**  Address line 1  */  
   Line1:string,
      /**  Address line 2  */  
   Line2:string,
      /**  Address line 3  */  
   Line3:string,
      /**  Postal or ZIP code  */  
   PostalCode:string,
      /**  State or province name  */  
   Region:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  */  
   UpdateAddr:boolean,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  */  
   TransactionID:string,
      /**  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  */  
   UpdateAllowed:boolean,
      /**  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  */  
   RequestID:string,
      /**  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  */  
   AddressCode:string,
      /**  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  */  
   AddressType:string,
      /**  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  */  
   CarrierRoute:string,
      /**  City name  */  
   ValidCity:string,
      /**  Country name  */  
   ValidCountry:string,
      /**  County name  */  
   County:string,
      /**  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  */  
   FipsCode:string,
      /**  Line one of the valid address returned by the tax integration.  */  
   ValidLine1:string,
      /**  Line two of the valid address returned by the tax integration.  */  
   ValidLine2:string,
      /**  Line three of the valid address returned by the tax integration.  */  
   ValidLine3:string,
      /**  Line four of the valid address returned by the tax integration.  */  
   ValidLine4:string,
      /**  Postal code returned by the tax integration.  */  
   ValidPostalCode:string,
      /**  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  */  
   PostNet:string,
      /**  State or province name or abbreviation returned by the tax integration.  */  
   ValidRegion:string,
      /**  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   ResultCode:string,
      /**  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  */  
   ResultSeq:number,
      /**  Carrier Route description  */  
   CarrierRouteDesc:string,
      /**  Address type description  */  
   AddressTypeDesc:string,
   OTSCountry:string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  */  
   ACWPercentage:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ETCMessageRow{
      /**  Company  */  
   Company:string,
   Details:string,
      /**  URL to help page for this message  */  
   Helplink:string,
      /**  Gets the name of the message  */  
   Name:string,
      /**  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  */  
   RefersTo:string,
      /**  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   Severity:string,
      /**  source of the message  */  
   Source:string,
      /**  concise summary of the message  */  
   Summary:string,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  */  
   TransactionID:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  Programitically assigned.  */  
   RequestID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantAttchRow{
   Company:string,
   Plant:string,
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

export interface Erp_Tablesets_PlantEGLCRow{
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
      /**  Plant  */  
   Plant:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  The Site name. Used on shipping reports.  */  
   Name:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantListTableset{
   PlantList:Erp_Tablesets_PlantListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PlantRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  The Site name. Used on shipping reports.  */  
   Name:string,
      /**  Site address line 1.  */  
   Address1:string,
      /**  Site address line 2.  */  
   Address2:string,
      /**  Site address line 3.  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Main phone number of the Site.  */  
   PhoneNum:string,
      /**  Main fax number of the Site.  */  
   FaxNum:string,
      /**  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  */  
   CommentText:string,
      /**  Number of days early that a supply source (Job or PO) can be without MRP suggesting to postpone the supply.  */  
   PlanningExceptionDays:number,
      /**  Intrastat Region  */  
   ISRegion:string,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   PlantCostID:string,
      /**  Lead Time added to the mfg item to determine the start date.  */  
   PrepTime:number,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   KitTime:number,
      /**  If checked, then Transfer Orders will be created when the requirement is marked as "firm".  */  
   ReqTransferHeader:boolean,
      /**  Identifies the default Production Calendar for this Site.   If this equals "", then the ProdCal record is the Company level production calendar.  */  
   CalendarID:string,
      /**  Transfer Shipment entry action to a Transfer Order.  Valid values are "WARN", "STOP" or "NONE" .  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the shipment and transfer request does not have a header.  STOP means that the request cannot be added to the shipment.  NONE allows the request to be added to the shipment with no warnings.  */  
   AllowShipAction:string,
      /**  Number of days before a sugestion is automatically converted to a firmed requirement.  */  
   AutoConfirmWindow:number,
      /**  When this field is checked then if transfer orders are being created automatically then each suggestion will create a separate transfer order  */  
   SingleLineOrder:boolean,
      /**  Maximum Operation Start Delay  */  
   MaxOpStartDelay:number,
      /**  Maximum Operation Length  */  
   MaxOpLength:number,
      /**  Default Station ID for the Site  */  
   DefStationID:string,
      /**  Number of days to the end of the finite horizon window  */  
   FiniteHorz:number,
      /**  Used by MRP.  */  
   NextUnfirmJob:string,
      /**  Used by MRP.  */  
   NextUnfirmTFLine:string,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  Number of days to the beginning of the rough cut scheduling horizon window  */  
   RCutHorz:number,
      /**  Include lead time in manufacturing lead time calculation  */  
   IncLeadTime:boolean,
      /**  Include transfer lead time in manufacturing lead time calculation  */  
   IncTransLeadTime:boolean,
      /**  Include receive time in manufacturing lead time calculation  */  
   IncReceiveTime:boolean,
      /**  Include kit time in manufacturing lead time calculation  */  
   IncKitTime:boolean,
      /**  Include rough cut parameters in manufacturing lead time calculation  */  
   IncRCParams:boolean,
      /**  Defines the number of days from the current date the scheduling uses to create job records within the Shop Load table.  */  
   OverloadHorz:number,
      /**   Determines if the start-to-start job operation offset will be used for production or setup time.  If setup

is chosen, a secondary operation with a start to start relationship will schedule setup to begin xxx 

minutes (defined in the operation) after the production starts on the primary operation.  If production is 

chosen then the production time of the secondary operation will be scheduled to start xxx minutes after the 

production starts on the primary operation.  */  
   SchedulingSendAhead:string,
      /**  Unfirm Series Horizon  */  
   UnfirmSeriesHorizon:number,
      /**  AutoFirmHorizon  */  
   AutoFirmHorizon:number,
      /**  Name of the person responsible for delivery  */  
   ManagerName:string,
      /**  Branch ID (Used Primary for Thailand Localization)  */  
   BranchID:string,
      /**  Pertains to Maintenance Management. Site which performs Equipment Maintenance for the this Site.  Note; Maintenance will be allowed in Equipments Site or MaintSite of it's Site.  */  
   MaintPlant:string,
      /**  Site Code  */  
   SiteCode:string,
      /**  Site Description 1  */  
   SiteDesc1:string,
      /**  Site Description 2  */  
   SiteDesc2:string,
      /**  Site Type: 0-Normal, 2-Main Site, 3-Sub Site, 5-Consolidated  */  
   SiteType:string,
      /**  Business Type Code  */  
   BusinessTypeCode:string,
      /**  Business Type Description 1  */  
   BusTypeDesc1:string,
      /**  Business Type Description 2  */  
   BusTypeDesc2:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGDefaultInvoicingPoint  */  
   AGDefaultInvoicingPoint:string,
      /**  It will force the times to be Start to Start when scheduling this kind of operations.  */  
   ForceSSTime:boolean,
      /**  It will force the times to be Finish to Finish when scheduling this kind of operations  */  
   ForceFFTime:boolean,
      /**  Within the leadtime window (MRP Start Date + Lead Time) use Lead Time Days of supply logic in place of standard days of supply  */  
   UseLeadTimeDOS:boolean,
      /**  Within the lead time window, allow consumption of minimum qty until below safety  */  
   AllowMinQty:boolean,
      /**  It will allow the user to move the job in regardless of material constraints and Subcontract PO?s  */  
   IgnoreMtlConstraints:boolean,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGLocationCode  */  
   AGLocationCode:string,
      /**  AGNeighborhood  */  
   AGNeighborhood:string,
      /**  AGStreet  */  
   AGStreet:string,
      /**  AGStreetNumber  */  
   AGStreetNumber:string,
      /**  AGExtraStreetNumber  */  
   AGExtraStreetNumber:string,
      /**  AGFloor  */  
   AGFloor:string,
      /**  AGApartment  */  
   AGApartment:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  */  
   MaxLateDaysPORel:number,
      /**  Obsolete  */  
   INECCNumber:string,
      /**  Obsolete  */  
   INExciseRange:string,
      /**  Obsolete  */  
   INExciseDivision:string,
      /**  Obsolete  */  
   INExCommissionRate:string,
      /**  INTINNumber  */  
   INTINNumber:string,
      /**  Obsolete  */  
   INCSTNumber:string,
      /**  Obsolete  */  
   INSTRegistration:string,
      /**  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  */  
   UseSchedulingMultiJob:boolean,
      /**  Will allow to auto load all child jobs related to the selected job at the Job Scheduling Board.  */  
   AutoLoadChildJobs:boolean,
      /**  Will allow to auto load all parent jobs related to the selected job at the Job Scheduling Board.  */  
   AutoLoadParentJobs:boolean,
      /**  Indicate to schedule engine to get the final date of the parent job and do backwards all the group of jobs to minimize gaps.  */  
   MinimizeWIP:boolean,
      /**  Time Zone of the site.  */  
   TimeZoneID:string,
      /**  Not used.  */  
   TimeZoneAdjustForDST:boolean,
      /**  SyncReqBy  */  
   SyncReqBy:boolean,
      /**  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  */  
   ACWPercentage:number,
      /**  It is the time used for schedule engine when scheduling backwards automatically. In some screens it is just a default and can be modified before scheduling.  */  
   BWSchedStartTime:number,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Determines if the Plant has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Determines the schedule direction that will default when manually scheduling a job. The following screens will be impacted by this setting: Job Entry, Service Job Entry, Maintenance Job Entry, Job Scheduling Board, Multi Resource Scheduling Board, Resource Scheduling Board, Job Manager, Project Entry.  */  
   SchedulingDirection:string,
      /**  US1099PayersTIN  */  
   US1099PayersTIN:string,
      /**  US1099NameControl  */  
   US1099NameControl:string,
      /**  US1099OfficeCode  */  
   US1099OfficeCode:string,
      /**  US1099ContactPerson  */  
   US1099ContactPerson:string,
      /**  US1099EmailAddress  */  
   US1099EMailAddress:string,
      /**  US1099FaxNum  */  
   US1099FaxNum:string,
      /**  US1099PhoneNum  */  
   US1099PhoneNum:string,
      /**  US1099TransControlCode  */  
   US1099TransControlCode:string,
      /**  US1099Name1  */  
   US1099Name1:string,
      /**  US1099Name2  */  
   US1099Name2:string,
      /**  US1099Address1  */  
   US1099Address1:string,
      /**  US1099Address2  */  
   US1099Address2:string,
      /**  US1099Address3  */  
   US1099Address3:string,
      /**  US1099City  */  
   US1099City:string,
      /**  US1099State  */  
   US1099State:string,
      /**  US1099ZIP  */  
   US1099ZIP:string,
      /**  TaxID  */  
   TaxID:string,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
      /**  Reason code for cost code change.  */  
   ReasonCode:string,
      /**  Reason code required flag.  */  
   ReasonReq:boolean,
      /**  Reason type  */  
   ReasonType:string,
      /**  Indicates if the scheduling logic in the system is not used because a third party scheduling.  */  
   Use3rdPartySched:boolean,
      /**  Reason Code Description  */  
   ReasonCodeDescription:string,
      /**  Background color for site (Kinetic UI).  */  
   KineticColor:string,
   LogoFileName:string,
   LogoImageContent:string,
      /**  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  */  
   MXISTMO:string,
   BitFlag:number,
   AGLocationDescription:string,
   AGProvinceCodeDescription:string,
   CalendarIDDescription:string,
   CompanySendToFSA:boolean,
   CountryNumDescription:string,
   MaintPlantName:string,
   PlantCostDescription:string,
   XbSystSiteIsLegalEntity:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantTableset{
   Plant:Erp_Tablesets_PlantRow[],
   PlantAttch:Erp_Tablesets_PlantAttchRow[],
   PlantEGLC:Erp_Tablesets_PlantEGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPlantTableset{
   Plant:Erp_Tablesets_PlantRow[],
   PlantAttch:Erp_Tablesets_PlantAttchRow[],
   PlantEGLC:Erp_Tablesets_PlantEGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetAllPlants_output{
   returnObj:Erp_Tablesets_PlantListTableset[],
}

   /** Required : 
      @param plant
   */  
export interface GetByID_input{
   plant:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PlantTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PlantTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PlantTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetCompleteList_input{
      /**  (optional)Additional Where conditions.  */  
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetCompleteList_output{
   returnObj:Erp_Tablesets_PlantListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetDisabledFields_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListAuthorizedPlants_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetListAuthorizedPlants_output{
   returnObj:Erp_Tablesets_PlantListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param companyID
      @param userID
      @param tblUIDs
      @param pageSize
      @param absolutePage
   */  
export interface GetListPlants_input{
      /**  whereClause  */  
   whereClause:string,
   companyID:string,
      /**  payment method name  */  
   userID:string,
      /**  list of payment UIDs  */  
   tblUIDs:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListPlants_output{
   returnObj:Erp_Tablesets_PlantListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   returnObj:Erp_Tablesets_PlantListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewPlantAttch_input{
   ds:Erp_Tablesets_PlantTableset[],
   plant:string,
}

export interface GetNewPlantAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset,
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
export interface GetNewPlantEGLC_input{
   ds:Erp_Tablesets_PlantTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewPlantEGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPlant_input{
   ds:Erp_Tablesets_PlantTableset[],
}

export interface GetNewPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset,
}
}

   /** Required : 
      @param whereClausePlant
      @param whereClausePlantAttch
      @param whereClausePlantEGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePlant:string,
   whereClausePlantAttch:string,
   whereClausePlantEGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PlantTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSystemTimeZoneList_output{
   returnObj:string,
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
      @param plantID
   */  
export interface IsAuthorizedForPlant_input{
      /**  The plant ID parameter.  */  
   plantID:string,
}

export interface IsAuthorizedForPlant_output{
parameters : {
      /**  output parameters  */  
   isValid:boolean,
}
}

   /** Required : 
      @param calendarID
      @param ds
   */  
export interface OnChangeOfCalendarID_input{
      /**  Proposed Calendar ID field  */  
   calendarID:string,
   ds:Erp_Tablesets_PlantTableset[],
}

export interface OnChangeOfCalendarID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset,
}
}

export interface PlantCostIDChanged_output{
parameters : {
      /**  output parameters  */  
   pcQuestion:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPlantTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPlantTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param plant
      @param fileName
      @param fileContents
   */  
export interface UpdateLogoImage_input{
   plant:string,
   fileName:string,
   fileContents:string,
}

export interface UpdateLogoImage_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PlantTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface UploadLogoImage_input{
   ds:Erp_Tablesets_PlantTableset[],
}

export interface UploadLogoImage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset,
}
}

