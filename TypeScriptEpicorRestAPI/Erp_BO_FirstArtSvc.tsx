import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.FirstArtSvc
// Description: First Article Entry business logic
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/$metadata", {
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
   Description: Get FirstArts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FirstArts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtRow
   */  
export function get_FirstArts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FirstArts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FirstArtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FirstArtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FirstArts(requestBody:Erp_Tablesets_FirstArtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FirstArt item
   Description: Calls GetByID to retrieve the FirstArt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FirstArt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FirstArtRow
   */  
export function get_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FirstArtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_FirstArtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FirstArt for the service
   Description: Calls UpdateExt to update FirstArt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FirstArt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FirstArtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, requestBody:Erp_Tablesets_FirstArtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete FirstArt item
   Description: Call UpdateExt to delete FirstArt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FirstArt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")", {
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
   Description: Get FirstArtAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FirstArtAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtAttchRow
   */  
export function get_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_FirstArtAttches(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")/FirstArtAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FirstArtAttch item
   Description: Calls GetByID to retrieve the FirstArtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FirstArtAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FirstArtAttchRow
   */  
export function get_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FirstArtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_FirstArtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FirstArtAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FirstArtAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtAttchRow
   */  
export function get_FirstArtAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FirstArtAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FirstArtAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FirstArtAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FirstArtAttches(requestBody:Erp_Tablesets_FirstArtAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FirstArtAttch item
   Description: Calls GetByID to retrieve the FirstArtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FirstArtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FirstArtAttchRow
   */  
export function get_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FirstArtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_FirstArtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FirstArtAttch for the service
   Description: Calls UpdateExt to update FirstArtAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FirstArtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FirstArtAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_FirstArtAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FirstArtAttch item
   Description: Call UpdateExt to delete FirstArtAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FirstArtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtListRow)
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
export function get_GetRows(whereClauseFirstArt:string, whereClauseFirstArtAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFirstArt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFirstArt=" + whereClauseFirstArt
   }
   if(typeof whereClauseFirstArtAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFirstArtAttch=" + whereClauseFirstArtAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetRows" + params, {
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
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, assemblySeq:string, oprSeq:string, resourceID:string, seqNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }
   if(typeof assemblySeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assemblySeq=" + assemblySeq
   }
   if(typeof oprSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "oprSeq=" + oprSeq
   }
   if(typeof resourceID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "resourceID=" + resourceID
   }
   if(typeof seqNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "seqNum=" + seqNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetList" + params, {
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
   Summary: Invoke method GetHistory
   Description: This method takes in the key field values for a First Article, and returns a FirstArtList
dataset of the history of related inspections.
   OperationID: GetHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHistory(requestBody:GetHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetHistory", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAssembly
   Description: This method validates the ProposedAssemblySeq, then updates the following assembly-related fields:
FirstArt.JobAsmPartNum
FirstArt.JobAsmRevisionNum
            
This method should be run when the FirstArt.AssemblySeq field changes.
            
An exception is thrown if:
- No Job Assembly exists with the given Assembly Sequence Number
   OperationID: OnChangeAssembly
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssembly(requestBody:OnChangeAssembly_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAssembly_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/OnChangeAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeAssembly_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the pcProposedJobNum, then clears the job-related fields.
FirstArt.JobAsmPartNum
FirstArt.JobAsmRevisionNum
            
This method should be run when the FirstArt.JobNum field changes.
            
An exception is thrown if:
- No Job exists with the given Job Number
   OperationID: OnChangeJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:OnChangeJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/OnChangeJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOprSeq
   Description: This method validates the piProposedOprSeq, then updates the operation-related fields.
            
This method should be run when the FirstArt.OprSeq field changes.
            
An exception is thrown if:
- No Job Operation exists with the given OprSeq Number
            
A warning message is returned if there is no First Article quantity set on the Job Operation
   OperationID: OnChangeOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOprSeq(requestBody:OnChangeOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/OnChangeOprSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOprSeq_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewFirstArt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFirstArt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFirstArt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFirstArt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFirstArt(requestBody:GetNewFirstArt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFirstArt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetNewFirstArt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFirstArt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFirstArtAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFirstArtAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFirstArtAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFirstArtAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFirstArtAttch(requestBody:GetNewFirstArtAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFirstArtAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetNewFirstArtAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFirstArtAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FirstArtAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FirstArtListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FirstArtRow,
}

export interface Erp_Tablesets_FirstArtAttchRow{
   "Company":string,
   "JobNum":string,
   "AssemblySeq":number,
   "OprSeq":number,
   "ResourceID":string,
   "SeqNum":number,
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

export interface Erp_Tablesets_FirstArtListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job number to which this first article transaction applies.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the first article transaction applies to.  */  
   "AssemblySeq":number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   "ResourceID":string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   "SeqNum":number,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   "ExpectedQuantity":number,
      /**  An ID of the person who did the first article inspection.  */  
   "InspectorID":string,
      /**  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  */  
   "EmployeeNum":string,
      /**  This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  */  
   "FAStatus":string,
      /**  System date at time inspection time.  */  
   "ActionDate":string,
      /**  System Time (hr-min-sec) at time of inspection.  */  
   "ActionTime":number,
      /**  Contains comments about the inspection.  */  
   "CommentText":string,
      /**  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  */  
   "InspectedQuantity":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   "UOMCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   "JobAsmPartNum":string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   "JobAsmRevisionNum":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  */  
   "EmployeeName":string,
      /**  First Article Status Description  */  
   "FAStatusDescription":string,
      /**  Action Time in a Time Format  */  
   "DispActionTime":string,
      /**  UOM Code Description  */  
   "UOMDesc":string,
      /**  Inspector's Full Name.  */  
   "InspectorIDName":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "JobAsmDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Full description of Resource.  */  
   "ResourceIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FirstArtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job number to which this first article transaction applies.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the first article transaction applies to.  */  
   "AssemblySeq":number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   "ResourceID":string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   "SeqNum":number,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   "ExpectedQuantity":number,
      /**  An ID of the person who did the first article inspection.  */  
   "InspectorID":string,
      /**  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  */  
   "EmployeeNum":string,
      /**  This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  */  
   "FAStatus":string,
      /**  System date at time inspection time.  */  
   "ActionDate":string,
      /**  System Time (hr-min-sec) at time of inspection.  */  
   "ActionTime":number,
      /**  Contains comments about the inspection.  */  
   "CommentText":string,
      /**  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  */  
   "InspectedQuantity":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   "UOMCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   "JobAsmPartNum":string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   "JobAsmRevisionNum":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  */  
   "EmployeeName":string,
      /**  First Article Status Description  */  
   "FAStatusDescription":string,
      /**  Action Time in a Time Format  */  
   "DispActionTime":string,
      /**  UOM Code Description  */  
   "UOMDesc":string,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "BitFlag":number,
   "InspectorIDName":string,
   "JobAsmDescription":string,
   "JobNumPartDescription":string,
   "ResourceIDDescription":string,
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
      @param jobNum
      @param assemblySeq
      @param oprSeq
      @param resourceID
      @param seqNum
   */  
export interface DeleteByID_input{
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
   resourceID:string,
   seqNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FirstArtAttchRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   ResourceID:string,
   SeqNum:number,
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

export interface Erp_Tablesets_FirstArtListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job number to which this first article transaction applies.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the first article transaction applies to.  */  
   AssemblySeq:number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   ResourceID:string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   SeqNum:number,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   ExpectedQuantity:number,
      /**  An ID of the person who did the first article inspection.  */  
   InspectorID:string,
      /**  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  */  
   EmployeeNum:string,
      /**  This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  */  
   FAStatus:string,
      /**  System date at time inspection time.  */  
   ActionDate:string,
      /**  System Time (hr-min-sec) at time of inspection.  */  
   ActionTime:number,
      /**  Contains comments about the inspection.  */  
   CommentText:string,
      /**  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  */  
   InspectedQuantity:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   UOMCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   JobAsmPartNum:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   JobAsmRevisionNum:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  */  
   EmployeeName:string,
      /**  First Article Status Description  */  
   FAStatusDescription:string,
      /**  Action Time in a Time Format  */  
   DispActionTime:string,
      /**  UOM Code Description  */  
   UOMDesc:string,
      /**  Inspector's Full Name.  */  
   InspectorIDName:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   JobAsmDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Full description of Resource.  */  
   ResourceIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FirstArtListTableset{
   FirstArtList:Erp_Tablesets_FirstArtListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FirstArtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job number to which this first article transaction applies.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the first article transaction applies to.  */  
   AssemblySeq:number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   ResourceID:string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   SeqNum:number,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   ExpectedQuantity:number,
      /**  An ID of the person who did the first article inspection.  */  
   InspectorID:string,
      /**  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  */  
   EmployeeNum:string,
      /**  This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  */  
   FAStatus:string,
      /**  System date at time inspection time.  */  
   ActionDate:string,
      /**  System Time (hr-min-sec) at time of inspection.  */  
   ActionTime:number,
      /**  Contains comments about the inspection.  */  
   CommentText:string,
      /**  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  */  
   InspectedQuantity:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   UOMCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   JobAsmPartNum:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   JobAsmRevisionNum:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  */  
   EmployeeName:string,
      /**  First Article Status Description  */  
   FAStatusDescription:string,
      /**  Action Time in a Time Format  */  
   DispActionTime:string,
      /**  UOM Code Description  */  
   UOMDesc:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BitFlag:number,
   InspectorIDName:string,
   JobAsmDescription:string,
   JobNumPartDescription:string,
   ResourceIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FirstArtTableset{
   FirstArt:Erp_Tablesets_FirstArtRow[],
   FirstArtAttch:Erp_Tablesets_FirstArtAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFirstArtTableset{
   FirstArt:Erp_Tablesets_FirstArtRow[],
   FirstArtAttch:Erp_Tablesets_FirstArtAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
      @param assemblySeq
      @param oprSeq
      @param resourceID
      @param seqNum
   */  
export interface GetByID_input{
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
   resourceID:string,
   seqNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FirstArtTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FirstArtTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FirstArtTableset[],
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
      @param jobNum
      @param assemblySeq
      @param oprSeq
      @param resourceID
   */  
export interface GetHistory_input{
      /**  The Job Number  */  
   jobNum:string,
      /**  The Job Assembly Sequence  */  
   assemblySeq:number,
      /**  The Job Operation Sequence  */  
   oprSeq:number,
      /**  The Resource ID  */  
   resourceID:string,
}

export interface GetHistory_output{
   returnObj:Erp_Tablesets_FirstArtListTableset[],
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
   returnObj:Erp_Tablesets_FirstArtListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param jobNum
      @param assemblySeq
      @param oprSeq
      @param resourceID
      @param seqNum
   */  
export interface GetNewFirstArtAttch_input{
   ds:Erp_Tablesets_FirstArtTableset[],
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
   resourceID:string,
   seqNum:number,
}

export interface GetNewFirstArtAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FirstArtTableset,
}
}

   /** Required : 
      @param ds
      @param jobNum
      @param assemblySeq
      @param oprSeq
      @param resourceID
   */  
export interface GetNewFirstArt_input{
   ds:Erp_Tablesets_FirstArtTableset[],
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
   resourceID:string,
}

export interface GetNewFirstArt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FirstArtTableset,
}
}

   /** Required : 
      @param whereClauseFirstArt
      @param whereClauseFirstArtAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFirstArt:string,
   whereClauseFirstArtAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FirstArtTableset[],
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
      @param piProposedAssemblySeq
      @param ds
   */  
export interface OnChangeAssembly_input{
      /**  The new proposed Job Assembly value  */  
   piProposedAssemblySeq:number,
   ds:Erp_Tablesets_FirstArtTableset[],
}

export interface OnChangeAssembly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FirstArtTableset,
}
}

   /** Required : 
      @param pcProposedJobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  The new proposed Job Number value  */  
   pcProposedJobNum:string,
   ds:Erp_Tablesets_FirstArtTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FirstArtTableset,
}
}

   /** Required : 
      @param piProposedOprSeq
      @param ds
   */  
export interface OnChangeOprSeq_input{
      /**  The new proposed Job Operation Sequence value  */  
   piProposedOprSeq:number,
   ds:Erp_Tablesets_FirstArtTableset[],
}

export interface OnChangeOprSeq_output{
parameters : {
      /**  output parameters  */  
   pcWarningMsg:string,
   ds:Erp_Tablesets_FirstArtTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtFirstArtTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFirstArtTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FirstArtTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FirstArtTableset,
}
}

