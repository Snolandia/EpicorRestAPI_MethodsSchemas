import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ControlIDExtractSvc
// Description: Master file maintenance business logic for ControlIDExtract
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/$metadata", {
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
   Description: Get ControlIDExtracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDExtracts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractHeaderRow
   */  
export function get_ControlIDExtracts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDExtracts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ControlIDExtracts(requestBody:Erp_Tablesets_ControlIDExtractHeaderRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ControlIDExtract item
   Description: Calls GetByID to retrieve the ControlIDExtract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
   */  
export function get_ControlIDExtracts_Company_ControlIDExtractCode(Company:string, ControlIDExtractCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ControlIDExtractHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")", {
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
         resolve(data as Erp_Tablesets_ControlIDExtractHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ControlIDExtract for the service
   Description: Calls UpdateExt to update ControlIDExtract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlIDExtract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ControlIDExtracts_Company_ControlIDExtractCode(Company:string, ControlIDExtractCode:string, requestBody:Erp_Tablesets_ControlIDExtractHeaderRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")", {
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
   Summary: Call UpdateExt to delete ControlIDExtract item
   Description: Call UpdateExt to delete ControlIDExtract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlIDExtract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ControlIDExtracts_Company_ControlIDExtractCode(Company:string, ControlIDExtractCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")", {
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
   Description: Get ControlIDExtractSegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ControlIDExtractSegments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractSegmentRow
   */  
export function get_ControlIDExtracts_Company_ControlIDExtractCode_ControlIDExtractSegments(Company:string, ControlIDExtractCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")/ControlIDExtractSegments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ControlIDExtractSegment item
   Description: Calls GetByID to retrieve the ControlIDExtractSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtractSegment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   */  
export function get_ControlIDExtracts_Company_ControlIDExtractCode_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company:string, ControlIDExtractCode:string, SegmentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ControlIDExtractSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")", {
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
         resolve(data as Erp_Tablesets_ControlIDExtractSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ControlIDExtractSegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDExtractSegments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractSegmentRow
   */  
export function get_ControlIDExtractSegments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDExtractSegments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ControlIDExtractSegments(requestBody:Erp_Tablesets_ControlIDExtractSegmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ControlIDExtractSegment item
   Description: Calls GetByID to retrieve the ControlIDExtractSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtractSegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   */  
export function get_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company:string, ControlIDExtractCode:string, SegmentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ControlIDExtractSegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")", {
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
         resolve(data as Erp_Tablesets_ControlIDExtractSegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ControlIDExtractSegment for the service
   Description: Calls UpdateExt to update ControlIDExtractSegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlIDExtractSegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company:string, ControlIDExtractCode:string, SegmentNum:string, requestBody:Erp_Tablesets_ControlIDExtractSegmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")", {
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
   Summary: Call UpdateExt to delete ControlIDExtractSegment item
   Description: Call UpdateExt to delete ControlIDExtractSegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlIDExtractSegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ControlIDExtractCode Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      @param SegmentNum Desc: SegmentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company:string, ControlIDExtractCode:string, SegmentNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")", {
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
   Description: Get ControlIDExtractPCIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDExtractPCIDs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractPCIDRow
   */  
export function get_ControlIDExtractPCIDs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDExtractPCIDs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ControlIDExtractPCIDs(requestBody:Erp_Tablesets_ControlIDExtractPCIDRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ControlIDExtractPCID item
   Description: Calls GetByID to retrieve the ControlIDExtractPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtractPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DataIdentifierCode Desc: DataIdentifierCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
   */  
export function get_ControlIDExtractPCIDs_Company_DataIdentifierCode(Company:string, DataIdentifierCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ControlIDExtractPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs(" + Company + "," + DataIdentifierCode + ")", {
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
         resolve(data as Erp_Tablesets_ControlIDExtractPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ControlIDExtractPCID for the service
   Description: Calls UpdateExt to update ControlIDExtractPCID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlIDExtractPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DataIdentifierCode Desc: DataIdentifierCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ControlIDExtractPCIDs_Company_DataIdentifierCode(Company:string, DataIdentifierCode:string, requestBody:Erp_Tablesets_ControlIDExtractPCIDRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs(" + Company + "," + DataIdentifierCode + ")", {
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
   Summary: Call UpdateExt to delete ControlIDExtractPCID item
   Description: Call UpdateExt to delete ControlIDExtractPCID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlIDExtractPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DataIdentifierCode Desc: DataIdentifierCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ControlIDExtractPCIDs_Company_DataIdentifierCode(Company:string, DataIdentifierCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs(" + Company + "," + DataIdentifierCode + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractHeaderListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderListRow)
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
export function get_GetRows(whereClauseControlIDExtractHeader:string, whereClauseControlIDExtractSegment:string, whereClauseControlIDExtractPCID:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseControlIDExtractHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseControlIDExtractHeader=" + whereClauseControlIDExtractHeader
   }
   if(typeof whereClauseControlIDExtractSegment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseControlIDExtractSegment=" + whereClauseControlIDExtractSegment
   }
   if(typeof whereClauseControlIDExtractPCID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseControlIDExtractPCID=" + whereClauseControlIDExtractPCID
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetRows" + params, {
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
export function get_GetByID(controlIDExtractCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof controlIDExtractCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "controlIDExtractCode=" + controlIDExtractCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetList" + params, {
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
   Summary: Invoke method GetControlIDExtractPCID
   Description: This method was coded to retreive the ControlIDExtractPCID records.  Since the ControlIDExtractPCID does not have a
relation to the other 2 tables, this needs to be retreived manually if getbyID is not called.
   OperationID: GetControlIDExtractPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetControlIDExtractPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetControlIDExtractPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetControlIDExtractPCID(requestBody:GetControlIDExtractPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetControlIDExtractPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetControlIDExtractPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetControlIDExtractPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDimension
   Description: Call this method when the value of Dimension changed
   OperationID: OnChangeDimension
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDimension_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDimension_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDimension(requestBody:OnChangeDimension_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDimension_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/OnChangeDimension", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDimension_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeIsFixedLength
   Description: Call this method when the value of IsFixedLength changed
   OperationID: OnChangeIsFixedLength
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeIsFixedLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIsFixedLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIsFixedLength(requestBody:OnChangeIsFixedLength_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeIsFixedLength_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/OnChangeIsFixedLength", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeIsFixedLength_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSegmentType
   Description: Call this method when the value of SegmentType changed
   OperationID: OnChangeSegmentType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSegmentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSegmentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSegmentType(requestBody:OnChangeSegmentType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSegmentType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/OnChangeSegmentType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeSegmentType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeExtractPCIDIsFixedLength
   Description: Call this method when the value of ExtractPCIDIsFixedLength changed
   OperationID: OnChangeExtractPCIDIsFixedLength
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeExtractPCIDIsFixedLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExtractPCIDIsFixedLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeExtractPCIDIsFixedLength(requestBody:OnChangeExtractPCIDIsFixedLength_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeExtractPCIDIsFixedLength_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/OnChangeExtractPCIDIsFixedLength", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeExtractPCIDIsFixedLength_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Returns the Code/Desc list of the column
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewControlIDExtractHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlIDExtractHeader
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewControlIDExtractHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlIDExtractHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewControlIDExtractHeader(requestBody:GetNewControlIDExtractHeader_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewControlIDExtractHeader_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetNewControlIDExtractHeader", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewControlIDExtractHeader_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewControlIDExtractSegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlIDExtractSegment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewControlIDExtractSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlIDExtractSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewControlIDExtractSegment(requestBody:GetNewControlIDExtractSegment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewControlIDExtractSegment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetNewControlIDExtractSegment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewControlIDExtractSegment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewControlIDExtractPCID
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlIDExtractPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewControlIDExtractPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlIDExtractPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewControlIDExtractPCID(requestBody:GetNewControlIDExtractPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewControlIDExtractPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetNewControlIDExtractPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewControlIDExtractPCID_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ControlIDExtractHeaderListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ControlIDExtractHeaderRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractPCIDRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ControlIDExtractPCIDRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractSegmentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ControlIDExtractSegmentRow,
}

export interface Erp_Tablesets_ControlIDExtractHeaderListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Code that makes this set of Control ID Extract rules unique.  */  
   "ControlIDExtractCode":string,
      /**  Description of this set of Control ID Extract rules.  */  
   "ControlIDExtractDesc":string,
      /**  Identifies the sequence in which the Control ID Extract rules will be checked.  */  
   "ExtractSequence":number,
      /**  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  */  
   "DataIdentifier":string,
      /**  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  */  
   "IsFixedLength":boolean,
      /**  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  */  
   "DigitsInString":number,
      /**  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  */  
   "DataFormat":string,
      /**  Identifies the Group Separator Character for this set of Control ID Extract rules.  */  
   "GroupSeparatorCharacter":string,
      /**  Identifies the Record Separator Character for this set of Control ID Extract rules.  */  
   "RecordSeparatorCharacter":string,
      /**  Identifies the End of Transmission Character for this set of Control ID Extract rules.  */  
   "EndOfTransmissionCharacter":string,
      /**  Identifies additional information about this set of Control ID Extract rules.  */  
   "ExtractComments":string,
      /**  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  */  
   "Dimension":string,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevCharacter02":string,
      /**  Development use only.  */  
   "DevInteger01":number,
      /**  Development use only.  */  
   "DevInteger02":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  Development use only.  */  
   "DevBoolean02":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "EndOfTransmissionASCII":number,
   "GroupSeparatorASCII":number,
   "RecordSeparatorASCII":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ControlIDExtractHeaderRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Code that makes this set of Control ID Extract rules unique.  */  
   "ControlIDExtractCode":string,
      /**  Description of this set of Control ID Extract rules.  */  
   "ControlIDExtractDesc":string,
      /**  Identifies the sequence in which the Control ID Extract rules will be checked.  */  
   "ExtractSequence":number,
      /**  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  */  
   "DataIdentifier":string,
      /**  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  */  
   "IsFixedLength":boolean,
      /**  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  */  
   "DigitsInString":number,
      /**  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  */  
   "DataFormat":string,
      /**  Identifies the Group Separator Character for this set of Control ID Extract rules.  */  
   "GroupSeparatorCharacter":string,
      /**  Identifies the Record Separator Character for this set of Control ID Extract rules.  */  
   "RecordSeparatorCharacter":string,
      /**  Identifies the End of Transmission Character for this set of Control ID Extract rules.  */  
   "EndOfTransmissionCharacter":string,
      /**  Identifies additional information about this set of Control ID Extract rules.  */  
   "ExtractComments":string,
      /**  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  */  
   "Dimension":string,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevCharacter02":string,
      /**  Development use only.  */  
   "DevInteger01":number,
      /**  Development use only.  */  
   "DevInteger02":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  Development use only.  */  
   "DevBoolean02":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "EndOfTransmissionASCII":number,
   "GroupSeparatorASCII":number,
   "RecordSeparatorASCII":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ControlIDExtractPCIDRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique code assigned by the user for this data identifier.  */  
   "DataIdentifierCode":string,
      /**  Description of the data identifier.  */  
   "DataIdentifierDesc":string,
      /**  Identifies the character string match for the left side characters of the Control ID.  */  
   "DataIdentifier":string,
      /**  Indicates if the record is inactive or not. Default is false.  */  
   "Inactive":boolean,
      /**  Identifies the order in which the Control ID Extract data identifiers will be checked against the Control ID.  */  
   "ExtractSequence":number,
      /**  Identifies the number of digits from the right end of the Control ID string to be extracted.  */  
   "DigitsToExtract":number,
      /**  Identifies if the Control ID string is a fixed length.  */  
   "IsFixedLength":boolean,
      /**  Identifies the number of digits in the Control ID string if it is a fixed length.  */  
   "DigitsInString":number,
      /**  Identifies additional information about the Control ID Extract data identifier.  */  
   "ExtractComments":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Scan Minimum Length  */  
   "ScanMinLength":number,
      /**  Scan Maximum Length  */  
   "ScanMaxLength":number,
   "Active":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ControlIDExtractSegmentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Code that makes this set of Control ID Extract rules unique.  */  
   "ControlIDExtractCode":string,
      /**  Segment Number that uniquely identifies this segment within the set of Control ID Extract rules.  */  
   "SegmentNum":number,
      /**  Segment Type.  Valid Values are PCID and OTHER.  This will be expended in the future to handle other types.  */  
   "SegmentType":string,
      /**  Identifies the character string match for the left side characters of the string defined with this segment.  */  
   "DataIdentifier":string,
      /**  The position of this segment in the concatenated PCID value.  */  
   "PCIDSegmentPosition":number,
      /**  Segment Position in the string.  */  
   "SegmentPosition":number,
      /**  Position in the string of the start character of this segment.  */  
   "StartCharacterPosition":number,
      /**  Position in the string of the end character of this segment.  */  
   "EndCharacterPosition":number,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevCharacter02":string,
      /**  Development use only.  */  
   "DevInteger01":number,
      /**  Development use only.  */  
   "DevInteger02":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  Development use only.  */  
   "DevBoolean02":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
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
      @param controlIDExtractCode
   */  
export interface DeleteByID_input{
   controlIDExtractCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ControlIDExtractHeaderListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Code that makes this set of Control ID Extract rules unique.  */  
   ControlIDExtractCode:string,
      /**  Description of this set of Control ID Extract rules.  */  
   ControlIDExtractDesc:string,
      /**  Identifies the sequence in which the Control ID Extract rules will be checked.  */  
   ExtractSequence:number,
      /**  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  */  
   DataIdentifier:string,
      /**  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  */  
   IsFixedLength:boolean,
      /**  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  */  
   DigitsInString:number,
      /**  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  */  
   DataFormat:string,
      /**  Identifies the Group Separator Character for this set of Control ID Extract rules.  */  
   GroupSeparatorCharacter:string,
      /**  Identifies the Record Separator Character for this set of Control ID Extract rules.  */  
   RecordSeparatorCharacter:string,
      /**  Identifies the End of Transmission Character for this set of Control ID Extract rules.  */  
   EndOfTransmissionCharacter:string,
      /**  Identifies additional information about this set of Control ID Extract rules.  */  
   ExtractComments:string,
      /**  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  */  
   Dimension:string,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevCharacter02:string,
      /**  Development use only.  */  
   DevInteger01:number,
      /**  Development use only.  */  
   DevInteger02:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  Development use only.  */  
   DevBoolean02:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   EndOfTransmissionASCII:number,
   GroupSeparatorASCII:number,
   RecordSeparatorASCII:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ControlIDExtractHeaderRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Code that makes this set of Control ID Extract rules unique.  */  
   ControlIDExtractCode:string,
      /**  Description of this set of Control ID Extract rules.  */  
   ControlIDExtractDesc:string,
      /**  Identifies the sequence in which the Control ID Extract rules will be checked.  */  
   ExtractSequence:number,
      /**  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  */  
   DataIdentifier:string,
      /**  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  */  
   IsFixedLength:boolean,
      /**  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  */  
   DigitsInString:number,
      /**  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  */  
   DataFormat:string,
      /**  Identifies the Group Separator Character for this set of Control ID Extract rules.  */  
   GroupSeparatorCharacter:string,
      /**  Identifies the Record Separator Character for this set of Control ID Extract rules.  */  
   RecordSeparatorCharacter:string,
      /**  Identifies the End of Transmission Character for this set of Control ID Extract rules.  */  
   EndOfTransmissionCharacter:string,
      /**  Identifies additional information about this set of Control ID Extract rules.  */  
   ExtractComments:string,
      /**  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  */  
   Dimension:string,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevCharacter02:string,
      /**  Development use only.  */  
   DevInteger01:number,
      /**  Development use only.  */  
   DevInteger02:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  Development use only.  */  
   DevBoolean02:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   EndOfTransmissionASCII:number,
   GroupSeparatorASCII:number,
   RecordSeparatorASCII:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ControlIDExtractListTableset{
   ControlIDExtractHeaderList:Erp_Tablesets_ControlIDExtractHeaderListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ControlIDExtractPCIDRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique code assigned by the user for this data identifier.  */  
   DataIdentifierCode:string,
      /**  Description of the data identifier.  */  
   DataIdentifierDesc:string,
      /**  Identifies the character string match for the left side characters of the Control ID.  */  
   DataIdentifier:string,
      /**  Indicates if the record is inactive or not. Default is false.  */  
   Inactive:boolean,
      /**  Identifies the order in which the Control ID Extract data identifiers will be checked against the Control ID.  */  
   ExtractSequence:number,
      /**  Identifies the number of digits from the right end of the Control ID string to be extracted.  */  
   DigitsToExtract:number,
      /**  Identifies if the Control ID string is a fixed length.  */  
   IsFixedLength:boolean,
      /**  Identifies the number of digits in the Control ID string if it is a fixed length.  */  
   DigitsInString:number,
      /**  Identifies additional information about the Control ID Extract data identifier.  */  
   ExtractComments:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Scan Minimum Length  */  
   ScanMinLength:number,
      /**  Scan Maximum Length  */  
   ScanMaxLength:number,
   Active:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ControlIDExtractSegmentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Code that makes this set of Control ID Extract rules unique.  */  
   ControlIDExtractCode:string,
      /**  Segment Number that uniquely identifies this segment within the set of Control ID Extract rules.  */  
   SegmentNum:number,
      /**  Segment Type.  Valid Values are PCID and OTHER.  This will be expended in the future to handle other types.  */  
   SegmentType:string,
      /**  Identifies the character string match for the left side characters of the string defined with this segment.  */  
   DataIdentifier:string,
      /**  The position of this segment in the concatenated PCID value.  */  
   PCIDSegmentPosition:number,
      /**  Segment Position in the string.  */  
   SegmentPosition:number,
      /**  Position in the string of the start character of this segment.  */  
   StartCharacterPosition:number,
      /**  Position in the string of the end character of this segment.  */  
   EndCharacterPosition:number,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevCharacter02:string,
      /**  Development use only.  */  
   DevInteger01:number,
      /**  Development use only.  */  
   DevInteger02:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  Development use only.  */  
   DevBoolean02:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ControlIDExtractTableset{
   ControlIDExtractHeader:Erp_Tablesets_ControlIDExtractHeaderRow[],
   ControlIDExtractSegment:Erp_Tablesets_ControlIDExtractSegmentRow[],
   ControlIDExtractPCID:Erp_Tablesets_ControlIDExtractPCIDRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtControlIDExtractTableset{
   ControlIDExtractHeader:Erp_Tablesets_ControlIDExtractHeaderRow[],
   ControlIDExtractSegment:Erp_Tablesets_ControlIDExtractSegmentRow[],
   ControlIDExtractPCID:Erp_Tablesets_ControlIDExtractPCIDRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param controlIDExtractCode
   */  
export interface GetByID_input{
   controlIDExtractCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ControlIDExtractTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ControlIDExtractTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ControlIDExtractTableset[],
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
      @param ds
   */  
export interface GetControlIDExtractPCID_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface GetControlIDExtractPCID_output{
   returnObj:Erp_Tablesets_ControlIDExtractTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
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
   returnObj:Erp_Tablesets_ControlIDExtractListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewControlIDExtractHeader_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface GetNewControlIDExtractHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewControlIDExtractPCID_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface GetNewControlIDExtractPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

   /** Required : 
      @param ds
      @param controlIDExtractCode
   */  
export interface GetNewControlIDExtractSegment_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
   controlIDExtractCode:string,
}

export interface GetNewControlIDExtractSegment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

   /** Required : 
      @param whereClauseControlIDExtractHeader
      @param whereClauseControlIDExtractSegment
      @param whereClauseControlIDExtractPCID
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseControlIDExtractHeader:string,
   whereClauseControlIDExtractSegment:string,
   whereClauseControlIDExtractPCID:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ControlIDExtractTableset[],
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
   */  
export interface OnChangeDimension_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface OnChangeDimension_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeExtractPCIDIsFixedLength_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface OnChangeExtractPCIDIsFixedLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeIsFixedLength_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface OnChangeIsFixedLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeSegmentType_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface OnChangeSegmentType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtControlIDExtractTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtControlIDExtractTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ControlIDExtractTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ControlIDExtractTableset,
}
}

