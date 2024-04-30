import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PkgControlConfigSvc
// Description: PkgControlConfigSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/$metadata", {
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
   Description: Get PkgControlConfigs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlConfigs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlRow
   */  
export function get_PkgControlConfigs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlConfigs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PkgControlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlConfigs(requestBody:Erp_Tablesets_PkgControlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PkgControlConfig item
   Description: Calls GetByID to retrieve the PkgControlConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlConfig
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PkgControlRow
   */  
export function get_PkgControlConfigs_Company_Plant_PkgControlIDCode(Company:string, Plant:string, PkgControlIDCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")", {
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
         resolve(data as Erp_Tablesets_PkgControlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlConfig for the service
   Description: Calls UpdateExt to update PkgControlConfig. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlConfig
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlConfigs_Company_Plant_PkgControlIDCode(Company:string, Plant:string, PkgControlIDCode:string, requestBody:Erp_Tablesets_PkgControlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")", {
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
   Summary: Call UpdateExt to delete PkgControlConfig item
   Description: Call UpdateExt to delete PkgControlConfig item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlConfig
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlConfigs_Company_Plant_PkgControlIDCode(Company:string, Plant:string, PkgControlIDCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")", {
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
   Description: Get PkgControlSegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PkgControlSegments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlSegmentRow
   */  
export function get_PkgControlConfigs_Company_Plant_PkgControlIDCode_PkgControlSegments(Company:string, Plant:string, PkgControlIDCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")/PkgControlSegments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PkgControlSegment item
   Description: Calls GetByID to retrieve the PkgControlSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlSegment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   */  
export function get_PkgControlConfigs_Company_Plant_PkgControlIDCode_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company:string, Plant:string, PkgControlIDCode:string, SegmentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")", {
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
         resolve(data as Erp_Tablesets_PkgControlSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PkgControlSegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlSegments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlSegmentRow
   */  
export function get_PkgControlSegments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlSegments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PkgControlSegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlSegments(requestBody:Erp_Tablesets_PkgControlSegmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PkgControlSegment item
   Description: Calls GetByID to retrieve the PkgControlSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlSegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   */  
export function get_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company:string, Plant:string, PkgControlIDCode:string, SegmentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")", {
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
         resolve(data as Erp_Tablesets_PkgControlSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlSegment for the service
   Description: Calls UpdateExt to update PkgControlSegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlSegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company:string, Plant:string, PkgControlIDCode:string, SegmentNum:string, requestBody:Erp_Tablesets_PkgControlSegmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")", {
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
   Summary: Call UpdateExt to delete PkgControlSegment item
   Description: Call UpdateExt to delete PkgControlSegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlSegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company:string, Plant:string, PkgControlIDCode:string, SegmentNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlListRow)
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
export function get_GetRows(whereClausePkgControl:string, whereClausePkgControlSegment:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePkgControl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControl=" + whereClausePkgControl
   }
   if(typeof whereClausePkgControlSegment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControlSegment=" + whereClausePkgControlSegment
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetRows" + params, {
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
export function get_GetByID(plant:string, pkgControlIDCode:string, epicorHeaders?:Headers){
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
   if(typeof pkgControlIDCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pkgControlIDCode=" + pkgControlIDCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetList" + params, {
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
   Summary: Invoke method InitializeStaticPCID
   Description: Initializes a Static PCID if it does not already exist.
   OperationID: InitializeStaticPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InitializeStaticPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeStaticPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitializeStaticPCID(requestBody:InitializeStaticPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InitializeStaticPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/InitializeStaticPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InitializeStaticPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InitializeDynamicPCID
   Description: Initializes a Dynamic PCID if it does not already exist.
   OperationID: InitializeDynamicPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InitializeDynamicPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeDynamicPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitializeDynamicPCID(requestBody:InitializeDynamicPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InitializeDynamicPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/InitializeDynamicPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InitializeDynamicPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeActive
   Description: This method performs validation for active flag
   OperationID: OnChangeActive
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeActive(requestBody:OnChangeActive_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeActive_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/OnChangeActive", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeActive_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAllowVoid
   Description: This method resets default values when AllowVoid changes
   OperationID: OnChangeAllowVoid
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAllowVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllowVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAllowVoid(requestBody:OnChangeAllowVoid_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAllowVoid_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/OnChangeAllowVoid", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeAllowVoid_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeControlIDCode
   Description: Update Control ID information when the Control ID Code is changed.
   OperationID: OnChangeControlIDCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeControlIDCode(requestBody:OnChangeControlIDCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeControlIDCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/OnChangeControlIDCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeControlIDCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePkgCode
   Description: Update Package Code information when the Package Code is changed.
   OperationID: OnChangePkgCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePkgCode(requestBody:OnChangePkgCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePkgCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/OnChangePkgCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePkgCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PkgControlPreUpdate
   Description: Called before update - checks to see if PCID has already been initialized with different settings.
Warning if static PCID / flags changed / in use
   OperationID: PkgControlPreUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PkgControlPreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PkgControlPreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlPreUpdate(requestBody:PkgControlPreUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PkgControlPreUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlPreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PkgControlPreUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrintPCID
   Description: Print PCID
   OperationID: PrintPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrintPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrintPCID(requestBody:PrintPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrintPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PrintPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PrintPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List from Service Designer.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method OnChangePkgControlIDCode
   OperationID: OnChangePkgControlIDCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePkgControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePkgControlIDCode(requestBody:OnChangePkgControlIDCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePkgControlIDCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/OnChangePkgControlIDCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePkgControlIDCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePkgControlType
   OperationID: OnChangePkgControlType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePkgControlType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgControlType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePkgControlType(requestBody:OnChangePkgControlType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePkgControlType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/OnChangePkgControlType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePkgControlType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateStaticEmptyBinNum
   Description: Validates if a given Bin is valid for the given Warehouse.
   OperationID: ValidateStaticEmptyBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateStaticEmptyBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateStaticEmptyBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateStaticEmptyBinNum(requestBody:ValidateStaticEmptyBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateStaticEmptyBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/ValidateStaticEmptyBinNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateStaticEmptyBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateStaticEmptyWarehouseCode
   Description: Validates if a given Warehouse is valid.
   OperationID: ValidateStaticEmptyWarehouseCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateStaticEmptyWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateStaticEmptyWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateStaticEmptyWarehouseCode(requestBody:ValidateStaticEmptyWarehouseCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateStaticEmptyWarehouseCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/ValidateStaticEmptyWarehouseCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateStaticEmptyWarehouseCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPkgControl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPkgControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControl(requestBody:GetNewPkgControl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPkgControl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetNewPkgControl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPkgControl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPkgControlSegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlSegment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControlSegment(requestBody:GetNewPkgControlSegment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPkgControlSegment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetNewPkgControlSegment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPkgControlSegment_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlSegmentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlSegmentRow,
}

export interface Erp_Tablesets_PkgControlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   "PkgControlType":string,
      /**  Package Control ID Code.  */  
   "PkgControlIDCode":string,
      /**  Package Control ID Description.  */  
   "PkgControlIDDesc":string,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   "PkgControlType":string,
      /**  Package Control ID Code.  */  
   "PkgControlIDCode":string,
      /**  Package Control ID Description.  */  
   "PkgControlIDDesc":string,
      /**  Unique packaging code assigned by the user.  */  
   "PkgCode":string,
      /**  Unique code assigned by the user for this Control ID.  */  
   "ControlIDCode":string,
      /**  If false then PCID is a single-level PCID that cannot be associated with a Parent.  */  
   "AllowParentPCID":boolean,
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM and Part Quantity per child PCID. This is referred to as a Master PCID otherwise it would be referred to as a MixedMaster PCID.  */  
   "AllowMixedChildPCIDs":boolean,
      /**  If false then PCID must contain only one LotNum for each Part on the PCID.  */  
   "AllowMixedLots":boolean,
      /**  If false then PCID must contain only one UOM per Part on the PCID.  */  
   "AllowMixedUOMs":boolean,
      /**  If false then PCID must contain only one Serial Number per PCID.  */  
   "AllowMultipleSerialNumsPerPCID":boolean,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   "LabelPrintControlled":boolean,
      /**  If false then the number of PCID label prints will not be tracked.  */  
   "LabelPrintCounter":boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  */  
   "AllowVoid":boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be deleted.  */  
   "AllowDelete":boolean,
      /**  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  */  
   "ArchivePCIDHistory":boolean,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  If false then PCID must contain only one PartNum.  */  
   "AllowMixedParts":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Indicates of an Initialization of a PCID has occurred using this Package Control ID Configuration.  The value is false when an initialization has not occurred to indicate last value fields do not hold a true last value.  Once an initialization has occurred, last value fields contain ongoing values to be used for incrementing.  */  
   "InitializationHasOccurred":boolean,
      /**  Indicates if the package control ID is an outbound container.  */  
   "OutboundContainer":boolean,
      /**  DefaultForStatic  */  
   "DefaultForStatic":boolean,
      /**  DefaultForDynamic  */  
   "DefaultForDynamic":boolean,
      /**  Warehouse where a Static PCID will be stored when emptied.  */  
   "StaticEmptyWarehouseCode":string,
      /**  Bin where a Static PCID will be stored when emptied.  */  
   "StaticEmptyBinNum":string,
      /**  Indicates if the record is active or not. Default is true.  */  
   "Active":boolean,
      /**  If true, disable ControlIDCode.  If false, enable ControlIDCode  */  
   "DisableControlIDCode":boolean,
      /**  Package Control ID example.  */  
   "ExampleIDValue":string,
      /**  Indicates if the Package Control ID has been used.  Default is false.  */  
   "InUse":boolean,
      /**  Package Control ID starting range.  */  
   "RangeFrom":string,
      /**  Package Control ID ending range.  */  
   "RangeTo":string,
   "Reinitialize":boolean,
      /**  The number of characters used in the Package Control ID.  */  
   "CharactersUsed":number,
      /**  The number of segments defined and associated with the Package Control ID.  */  
   "DefinedSegments":number,
      /**  Static Empty Bin Description  */  
   "StaticEmptyBinDesc":string,
      /**  Empty Static Warehouse Description  */  
   "StaticEmptyWarehouseDesc":string,
   "BitFlag":number,
   "ControlIDControlIDDesc":string,
   "PackingDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlSegmentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   "PkgControlType":string,
      /**  Package Control ID Code.  */  
   "PkgControlIDCode":string,
      /**  Unique code assigned by the user for this Control ID.  */  
   "ControlIDCode":string,
      /**  Unique Segment Number within the Control ID Code.  */  
   "SegmentNum":number,
      /**  Segment Description.  */  
   "SegmentDesc":string,
      /**  Segment starting string of the alphanumeric range based on segment format.  */  
   "AlphaRangeFrom":string,
      /**  Segment ending string of the alphanumeric range based on segment format.  */  
   "AlphaRangeTo":string,
      /**  Segment last value string of the alphanumeric range based on segment format.  */  
   "AlphaRangeLastValue":string,
      /**  Segment starting value of the numeric range based on segment format.  */  
   "NumericRangeFrom":number,
      /**  Segment ending value of the numeric range based on segment format.  */  
   "NumericRangeTo":number,
      /**  Segment last value of the numeric range based on segment format.  */  
   "NumericRangeLastValue":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Segment Position within the Control ID.  */  
   "SegmentPosition":number,
      /**  Segment Type.  Valid values are AlphaSequential, NumericSequential, DateNumericSequential, Date, and Fixed.  There can be an unlimited number of Fixed segments, only one segment of each other type may exist within the Control ID.  DateNumericSequential may only exist if a Date segment exists.  */  
   "SegmentType":string,
      /**  Segment format as input by the user. Valid values are "&" for AlphaNumeric segments, "@" for Alpha Only segments, "#" for Numeric Only segments.  For date segments, "<D>" represents a 2 digit day, "<M>" represents a 2 digit month, "<YY>" represents a 2 digit year, "<YYYY>" represents a 4 digit year, "<TJD>" represents a 5 digit Truncated Julian Date, and "<T>" represents time in a 6 digit integer.  Valid values for Fixed segments are "a-z", "A-Z", "0-9", "-"  */  
   "SegmentFormat":string,
      /**  Based on the segment type:  If segment type is Sequential, value is Sequential.  If segment type is Fixed, value is Fixed.  */  
   "RolloverTrigger":string,
      /**  Indicates the action to be taken when the Control ID reaches its limit.  Valid values vary per Rollover Trigger.  If rollover trigger is Sequential or DateNumericSequential, valid values are Stop and Range From.  If rollover trigger is Fixed or Date, valid value is blank.  */  
   "RolloverAction":string,
      /**  Segment last value of the date based on segment format.  */  
   "DateLastValue":string,
      /**  Indicates if the segment is of a fixed length.  */  
   "IsFixedLength":boolean,
   "ExampleIDValue":string,
      /**  Starting at value - used to initialize the last value for newly created configurations  */  
   "NumericRangeStartingAt":number,
      /**  Starting at value - used to initialize the last value for newly created configurations  */  
   "AlphaRangeStartingAt":string,
   "BitFlag":number,
   "ControlIDControlIDDesc":string,
   "PkgControlPkgControlIDDesc":string,
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
      @param plant
      @param pkgControlIDCode
   */  
export interface DeleteByID_input{
   plant:string,
   pkgControlIDCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PkgControlConfigListTableset{
   PkgControlList:Erp_Tablesets_PkgControlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlConfigTableset{
   PkgControl:Erp_Tablesets_PkgControlRow[],
   PkgControlSegment:Erp_Tablesets_PkgControlSegmentRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   PkgControlType:string,
      /**  Package Control ID Code.  */  
   PkgControlIDCode:string,
      /**  Package Control ID Description.  */  
   PkgControlIDDesc:string,
      /**  Inactive  */  
   Inactive:boolean,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   PkgControlType:string,
      /**  Package Control ID Code.  */  
   PkgControlIDCode:string,
      /**  Package Control ID Description.  */  
   PkgControlIDDesc:string,
      /**  Unique packaging code assigned by the user.  */  
   PkgCode:string,
      /**  Unique code assigned by the user for this Control ID.  */  
   ControlIDCode:string,
      /**  If false then PCID is a single-level PCID that cannot be associated with a Parent.  */  
   AllowParentPCID:boolean,
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM and Part Quantity per child PCID. This is referred to as a Master PCID otherwise it would be referred to as a MixedMaster PCID.  */  
   AllowMixedChildPCIDs:boolean,
      /**  If false then PCID must contain only one LotNum for each Part on the PCID.  */  
   AllowMixedLots:boolean,
      /**  If false then PCID must contain only one UOM per Part on the PCID.  */  
   AllowMixedUOMs:boolean,
      /**  If false then PCID must contain only one Serial Number per PCID.  */  
   AllowMultipleSerialNumsPerPCID:boolean,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   LabelPrintControlled:boolean,
      /**  If false then the number of PCID label prints will not be tracked.  */  
   LabelPrintCounter:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  */  
   AllowVoid:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be deleted.  */  
   AllowDelete:boolean,
      /**  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  */  
   ArchivePCIDHistory:boolean,
      /**  Inactive  */  
   Inactive:boolean,
      /**  If false then PCID must contain only one PartNum.  */  
   AllowMixedParts:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates of an Initialization of a PCID has occurred using this Package Control ID Configuration.  The value is false when an initialization has not occurred to indicate last value fields do not hold a true last value.  Once an initialization has occurred, last value fields contain ongoing values to be used for incrementing.  */  
   InitializationHasOccurred:boolean,
      /**  Indicates if the package control ID is an outbound container.  */  
   OutboundContainer:boolean,
      /**  DefaultForStatic  */  
   DefaultForStatic:boolean,
      /**  DefaultForDynamic  */  
   DefaultForDynamic:boolean,
      /**  Warehouse where a Static PCID will be stored when emptied.  */  
   StaticEmptyWarehouseCode:string,
      /**  Bin where a Static PCID will be stored when emptied.  */  
   StaticEmptyBinNum:string,
      /**  Indicates if the record is active or not. Default is true.  */  
   Active:boolean,
      /**  If true, disable ControlIDCode.  If false, enable ControlIDCode  */  
   DisableControlIDCode:boolean,
      /**  Package Control ID example.  */  
   ExampleIDValue:string,
      /**  Indicates if the Package Control ID has been used.  Default is false.  */  
   InUse:boolean,
      /**  Package Control ID starting range.  */  
   RangeFrom:string,
      /**  Package Control ID ending range.  */  
   RangeTo:string,
   Reinitialize:boolean,
      /**  The number of characters used in the Package Control ID.  */  
   CharactersUsed:number,
      /**  The number of segments defined and associated with the Package Control ID.  */  
   DefinedSegments:number,
      /**  Static Empty Bin Description  */  
   StaticEmptyBinDesc:string,
      /**  Empty Static Warehouse Description  */  
   StaticEmptyWarehouseDesc:string,
   BitFlag:number,
   ControlIDControlIDDesc:string,
   PackingDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlSegmentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   PkgControlType:string,
      /**  Package Control ID Code.  */  
   PkgControlIDCode:string,
      /**  Unique code assigned by the user for this Control ID.  */  
   ControlIDCode:string,
      /**  Unique Segment Number within the Control ID Code.  */  
   SegmentNum:number,
      /**  Segment Description.  */  
   SegmentDesc:string,
      /**  Segment starting string of the alphanumeric range based on segment format.  */  
   AlphaRangeFrom:string,
      /**  Segment ending string of the alphanumeric range based on segment format.  */  
   AlphaRangeTo:string,
      /**  Segment last value string of the alphanumeric range based on segment format.  */  
   AlphaRangeLastValue:string,
      /**  Segment starting value of the numeric range based on segment format.  */  
   NumericRangeFrom:number,
      /**  Segment ending value of the numeric range based on segment format.  */  
   NumericRangeTo:number,
      /**  Segment last value of the numeric range based on segment format.  */  
   NumericRangeLastValue:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Segment Position within the Control ID.  */  
   SegmentPosition:number,
      /**  Segment Type.  Valid values are AlphaSequential, NumericSequential, DateNumericSequential, Date, and Fixed.  There can be an unlimited number of Fixed segments, only one segment of each other type may exist within the Control ID.  DateNumericSequential may only exist if a Date segment exists.  */  
   SegmentType:string,
      /**  Segment format as input by the user. Valid values are "&" for AlphaNumeric segments, "@" for Alpha Only segments, "#" for Numeric Only segments.  For date segments, "<D>" represents a 2 digit day, "<M>" represents a 2 digit month, "<YY>" represents a 2 digit year, "<YYYY>" represents a 4 digit year, "<TJD>" represents a 5 digit Truncated Julian Date, and "<T>" represents time in a 6 digit integer.  Valid values for Fixed segments are "a-z", "A-Z", "0-9", "-"  */  
   SegmentFormat:string,
      /**  Based on the segment type:  If segment type is Sequential, value is Sequential.  If segment type is Fixed, value is Fixed.  */  
   RolloverTrigger:string,
      /**  Indicates the action to be taken when the Control ID reaches its limit.  Valid values vary per Rollover Trigger.  If rollover trigger is Sequential or DateNumericSequential, valid values are Stop and Range From.  If rollover trigger is Fixed or Date, valid value is blank.  */  
   RolloverAction:string,
      /**  Segment last value of the date based on segment format.  */  
   DateLastValue:string,
      /**  Indicates if the segment is of a fixed length.  */  
   IsFixedLength:boolean,
   ExampleIDValue:string,
      /**  Starting at value - used to initialize the last value for newly created configurations  */  
   NumericRangeStartingAt:number,
      /**  Starting at value - used to initialize the last value for newly created configurations  */  
   AlphaRangeStartingAt:string,
   BitFlag:number,
   ControlIDControlIDDesc:string,
   PkgControlPkgControlIDDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPkgControlConfigTableset{
   PkgControl:Erp_Tablesets_PkgControlRow[],
   PkgControlSegment:Erp_Tablesets_PkgControlSegmentRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param pkgControlIDCode
   */  
export interface GetByID_input{
   plant:string,
   pkgControlIDCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PkgControlConfigTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PkgControlConfigTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PkgControlConfigTableset[],
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
   returnObj:Erp_Tablesets_PkgControlConfigListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param pkgControlIDCode
   */  
export interface GetNewPkgControlSegment_input{
   ds:Erp_Tablesets_PkgControlConfigTableset[],
   plant:string,
   pkgControlIDCode:string,
}

export interface GetNewPkgControlSegment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewPkgControl_input{
   ds:Erp_Tablesets_PkgControlConfigTableset[],
   plant:string,
}

export interface GetNewPkgControl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param whereClausePkgControl
      @param whereClausePkgControlSegment
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePkgControl:string,
   whereClausePkgControlSegment:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PkgControlConfigTableset[],
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
      @param ipCompany
      @param ipPlant
      @param ipPkgControlIDCode
   */  
export interface InitializeDynamicPCID_input{
      /**  Current Company  */  
   ipCompany:string,
      /**  Current Site  */  
   ipPlant:string,
      /**  Package Control ID Code  */  
   ipPkgControlIDCode:string,
}

export interface InitializeDynamicPCID_output{
}

   /** Required : 
      @param ipCompany
      @param ipPlant
      @param ipPkgControlIDCode
   */  
export interface InitializeStaticPCID_input{
      /**  Current Company  */  
   ipCompany:string,
      /**  Current Site  */  
   ipPlant:string,
      /**  Package Control ID Code  */  
   ipPkgControlIDCode:string,
}

export interface InitializeStaticPCID_output{
parameters : {
      /**  output parameters  */  
   PCID:string,
}
}

   /** Required : 
      @param activeFlag
      @param ds
   */  
export interface OnChangeActive_input{
      /**  Proposed active value  */  
   activeFlag:boolean,
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface OnChangeActive_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param ipAllowVoid
      @param ds
   */  
export interface OnChangeAllowVoid_input{
      /**  Proposed AllowVoid field  */  
   ipAllowVoid:boolean,
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface OnChangeAllowVoid_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param ipControlIDCode
      @param ds
   */  
export interface OnChangeControlIDCode_input{
      /**  The Control ID Code  */  
   ipControlIDCode:string,
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface OnChangeControlIDCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param ipPkgCode
      @param ds
   */  
export interface OnChangePkgCode_input{
      /**  The Package Code  */  
   ipPkgCode:string,
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface OnChangePkgCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param proposedPkgControlIDCode
      @param ds
   */  
export interface OnChangePkgControlIDCode_input{
   proposedPkgControlIDCode:string,
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface OnChangePkgControlIDCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param proposedPkgControlType
      @param ds
   */  
export interface OnChangePkgControlType_input{
   proposedPkgControlType:string,
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface OnChangePkgControlType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PkgControlPreUpdate_input{
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface PkgControlPreUpdate_output{
parameters : {
      /**  output parameters  */  
   msg:string,
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param ipPCID
      @param ipPrinterID
   */  
export interface PrintPCID_input{
      /**  PCID  */  
   ipPCID:string,
      /**  Printer ID  */  
   ipPrinterID:string,
}

export interface PrintPCID_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPkgControlConfigTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPkgControlConfigTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PkgControlConfigTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlConfigTableset,
}
}

   /** Required : 
      @param warehouseCode
      @param binNum
   */  
export interface ValidateStaticEmptyBinNum_input{
   warehouseCode:string,
   binNum:string,
}

export interface ValidateStaticEmptyBinNum_output{
   returnObj:boolean,
}

   /** Required : 
      @param warehouseCode
      @param currentPlantID
   */  
export interface ValidateStaticEmptyWarehouseCode_input{
   warehouseCode:string,
   currentPlantID:string,
}

export interface ValidateStaticEmptyWarehouseCode_output{
   returnObj:boolean,
}

