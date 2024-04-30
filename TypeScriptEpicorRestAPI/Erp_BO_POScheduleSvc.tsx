import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.POScheduleSvc
// Description: POSchedule BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/$metadata", {
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
   Description: Get POSchedules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POSchedules
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleRow
   */  
export function get_POSchedules(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POSchedules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POScheduleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.POScheduleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POSchedules(requestBody:Erp_Tablesets_POScheduleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the POSchedule item
   Description: Calls GetByID to retrieve the POSchedule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.POScheduleRow
   */  
export function get_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")", {
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
         resolve(data as Erp_Tablesets_POScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POSchedule for the service
   Description: Calls UpdateExt to update POSchedule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.POScheduleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, requestBody:Erp_Tablesets_POScheduleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")", {
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
   Summary: Call UpdateExt to delete POSchedule item
   Description: Call UpdateExt to delete POSchedule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")", {
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
   Description: Get POScheduleDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POScheduleDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleDtlRow
   */  
export function get_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev_POScheduleDtls(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")/POScheduleDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the POScheduleDtl item
   Description: Calls GetByID to retrieve the POScheduleDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POScheduleDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param ContractPORelNum Desc: ContractPORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.POScheduleDtlRow
   */  
export function get_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, ContractPORelNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POScheduleDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")", {
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
         resolve(data as Erp_Tablesets_POScheduleDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get POScheduleDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POScheduleDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleDtlRow
   */  
export function get_POScheduleDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POScheduleDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POScheduleDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.POScheduleDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POScheduleDtls(requestBody:Erp_Tablesets_POScheduleDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the POScheduleDtl item
   Description: Calls GetByID to retrieve the POScheduleDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POScheduleDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param ContractPORelNum Desc: ContractPORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.POScheduleDtlRow
   */  
export function get_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, ContractPORelNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POScheduleDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")", {
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
         resolve(data as Erp_Tablesets_POScheduleDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POScheduleDtl for the service
   Description: Calls UpdateExt to update POScheduleDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POScheduleDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param ContractPORelNum Desc: ContractPORelNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.POScheduleDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, ContractPORelNum:string, requestBody:Erp_Tablesets_POScheduleDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")", {
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
   Summary: Call UpdateExt to delete POScheduleDtl item
   Description: Call UpdateExt to delete POScheduleDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POScheduleDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param ContractRev Desc: ContractRev   Required: True
      @param ContractPORelNum Desc: ContractPORelNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company:string, Plant:string, ContractPONum:string, ContractPOLine:string, ContractRev:string, ContractPORelNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleListRow)
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
export function get_GetRows(whereClausePOSchedule:string, whereClausePOScheduleDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePOSchedule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOSchedule=" + whereClausePOSchedule
   }
   if(typeof whereClausePOScheduleDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOScheduleDtl=" + whereClausePOScheduleDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, contractPONum:string, contractPOLine:string, contractRev:string, epicorHeaders?:Headers){
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
   if(typeof contractPONum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractPONum=" + contractPONum
   }
   if(typeof contractPOLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractPOLine=" + contractPOLine
   }
   if(typeof contractRev!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractRev=" + contractRev
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetList" + params, {
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
   Summary: Invoke method ApproveAllSchedules
   Description: Approved all schedules
   OperationID: ApproveAllSchedules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApproveAllSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAllSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveAllSchedules(requestBody:ApproveAllSchedules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApproveAllSchedules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/ApproveAllSchedules", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ApproveAllSchedules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApproveMultiVendorSchedule
   Description: Approved one schedule
   OperationID: ApproveMultiVendorSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApproveMultiVendorSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveMultiVendorSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveMultiVendorSchedule(requestBody:ApproveMultiVendorSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApproveMultiVendorSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/ApproveMultiVendorSchedule", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ApproveMultiVendorSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApproveSchedule
   Description: Approved one schedule
   OperationID: ApproveSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApproveSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveSchedule(requestBody:ApproveSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApproveSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/ApproveSchedule", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ApproveSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOtherSchedules
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">Part number of part to check for multiple schedules </param><param name="opScheduleFound">Was another schedule foud for this part? </param>
   OperationID: CheckOtherSchedules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckOtherSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOtherSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOtherSchedules(requestBody:CheckOtherSchedules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckOtherSchedules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/CheckOtherSchedules", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckOtherSchedules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyQuantities
   Description: Provides a simply way of being able to copy the quantities from either the Current, Suggestion or Adjusted fields to the Proposed field for the whole schedule
   OperationID: CopyQuantities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyQuantities(requestBody:CopyQuantities_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyQuantities_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/CopyQuantities", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyQuantities_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LastPackSlip
   OperationID: LastPackSlip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LastPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LastPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LastPackSlip(requestBody:LastPackSlip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LastPackSlip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/LastPackSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LastPackSlip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSharedSupplierValidation
   Description: Purpose: GetSharedSupplierValidation
Parameters:  none
Notes:
<param name="opSharedSupplierValidation">Shared Supplier Validation? Yes/No</param>
   OperationID: GetSharedSupplierValidation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSharedSupplierValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSharedSupplierValidation(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSharedSupplierValidation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetSharedSupplierValidation", {
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
         resolve(data as GetSharedSupplierValidation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetSharedSupplierValidation
   Description: Sets a variable behind the Part Schedule Shared Supplier Validation option
   OperationID: SetSharedSupplierValidation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetSharedSupplierValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSharedSupplierValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSharedSupplierValidation(requestBody:SetSharedSupplierValidation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetSharedSupplierValidation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/SetSharedSupplierValidation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetSharedSupplierValidation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApproveAllSchedulesDS
   Description: Approved all schedules by data set
   OperationID: ApproveAllSchedulesDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApproveAllSchedulesDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAllSchedulesDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveAllSchedulesDS(requestBody:ApproveAllSchedulesDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApproveAllSchedulesDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/ApproveAllSchedulesDS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ApproveAllSchedulesDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPOSchedule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPOSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOSchedule(requestBody:GetNewPOSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPOSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetNewPOSchedule", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPOSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPOScheduleDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOScheduleDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPOScheduleDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOScheduleDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOScheduleDtl(requestBody:GetNewPOScheduleDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPOScheduleDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetNewPOScheduleDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPOScheduleDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POScheduleDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POScheduleListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POScheduleRow,
}

export interface Erp_Tablesets_POScheduleDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   "ContractPONum":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ContractPOLine":number,
      /**  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  */  
   "ContractRev":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "ContractPORelNum":number,
      /**  The last Packing Slip processed for this Contract Purchase Order.  */  
   "LastPackSlip":string,
      /**  The Receipt Date of the last Receipt for this Contract Purchase Order.  */  
   "LastReceiptDate":string,
      /**  Receipt quantity in our unit of measure.  */  
   "LastReceiptOurQty":number,
      /**  Date of the current schedule, suggested demand, adjusted schedule, or proposed schedule.  */  
   "ScheduleDate":string,
      /**  The Week Number relating to the Work Date.  */  
   "WeekNum":number,
      /**  The Week Year relating to the Work Date.  */  
   "WeekYear":number,
      /**  Current Scheduled Quantity corresponding to a PORel.  */  
   "CurrentOurQty":number,
      /**  The quantity created by the Generate PO Suggestions process.  */  
   "SuggestedOurQty":number,
      /**  The quantity that the Generate PO Schedules process is suggesting.  Includes a minimum quantity and is determined by the Periodicity code being used.  */  
   "AdjustedOurQty":number,
      /**  Quantity the user may propose via the Purchase Order Contract Schedule Maintenance.  */  
   "ProposedOurQty":number,
      /**  Inventory UOM  */  
   "OurQtyUOM":string,
      /**  The last packing slip number that a receipt was made against this Purchase Order Contract at the time Generate Purchase Suggestions was run.  */  
   "POSuggLastPackSlip":string,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  */  
   "PurchasingFactor":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  For development use only.  */  
   "DevChar01":string,
      /**  For development use only.  */  
   "DevChar02":string,
      /**  For development use only.  */  
   "DevChar03":string,
      /**  For development use only.  */  
   "DevChar04":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Adjusted Our Qty displayed in terms of the Primary UOM of the Part.  */  
   "AdjustedOurQtyDisp":number,
      /**  Current Our Qty displayed in terms of the Primary UOM of the Part.  */  
   "CurrentOurQtyDisp":number,
      /**  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  */  
   "ProposedOurQtyDisp":number,
      /**  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  */  
   "SuggestedOurQtyDisp":number,
      /**  Primary Inventory UOM for the Part  */  
   "IUM":string,
   "ReceivedOurQtyDisp":number,
   "BitFlag":number,
   "PlantName":string,
   "PODetailPartNum":string,
   "PODetailPUM":string,
   "PORelReceivedQty":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_POScheduleListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   "ContractPONum":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ContractPOLine":number,
      /**  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  */  
   "ContractRev":number,
      /**  Date the Purchase Order Schedule was created.  */  
   "CreateDate":string,
      /**  Date the Purchase Order Schedule was approved.  */  
   "ApprovedDate":string,
      /**  Date the Purchase Order Schedule was printed.  */  
   "PrintedDate":string,
      /**  Date the Purchase Order Schedule was last executed.  */  
   "LastRunDate":string,
      /**  Is this Revision of the Purchase Order Schedule active?  */  
   "ActiveRevision":boolean,
      /**  Part Number for this Purchase Order Contract Schedule.  */  
   "PartNum":string,
      /**  Supplier Number for this Purchase Order Contract Schedule.  */  
   "VendorNum":number,
      /**  The ID that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  For development use only.  */  
   "DevChar01":string,
      /**  For development use only.  */  
   "DevChar02":string,
      /**  For development use only.  */  
   "DevChar03":string,
      /**  For development use only.  */  
   "DevChar04":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  POHeader.ContractEndDate  */  
   "ContractEndDate":string,
      /**  POHeader.ContractStartDate  */  
   "ContractStartDate":string,
      /**  PODetail.ContractQty  */  
   "ContractQty":number,
      /**  Part.PartDescription  */  
   "PartDescription":string,
      /**  VendorID  */  
   "VendorID":string,
      /**  VendorName  */  
   "VendorName":string,
      /**  POHeader.PurPoint  */  
   "PurPoint":string,
   "POSuggLastPackSlip":string,
   "LastPackSlip":string,
   "LastReceiptDate":string,
   "LastReceiptOurQty":number,
      /**  PODetail.ContractQtyUOM  */  
   "ContractQtyUOM":string,
      /**  Last Receipt UOM  */  
   "LastReceiptOurQtyUOM":string,
   "PurchaseScheduleMode":string,
   "ReductionMethod":number,
      /**  The sum of PORel.ArrivedQty for the current PO Line  */  
   "TotalArrivedQuantity":number,
      /**  The sum of PORel.Received for the current PO Line  */  
   "TotalReceiptQuantity":number,
   "PartPartDescription":string,
   "PartIUM":string,
   "PlantName":string,
   "PODetailContractQty":number,
   "PODetailContractQtyUOM":string,
   "PODetailOrderQty":number,
   "POHeaderPurPoint":string,
   "POHeaderContractEndDate":string,
   "POHeaderContractStartDate":string,
   "VendorVendorID":string,
   "VendorName_":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_POScheduleRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   "ContractPONum":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ContractPOLine":number,
      /**  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  */  
   "ContractRev":number,
      /**  Date the Purchase Order Schedule was created.  */  
   "CreateDate":string,
      /**  Date the Purchase Order Schedule was approved.  */  
   "ApprovedDate":string,
      /**  Date the Purchase Order Schedule was printed.  */  
   "PrintedDate":string,
      /**  Date the Purchase Order Schedule was last executed.  */  
   "LastRunDate":string,
      /**  Is this Revision of the Purchase Order Schedule active?  */  
   "ActiveRevision":boolean,
      /**  Part Number for this Purchase Order Contract Schedule.  */  
   "PartNum":string,
      /**  Supplier Number for this Purchase Order Contract Schedule.  */  
   "VendorNum":number,
      /**  The ID that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  For development use only.  */  
   "DevChar01":string,
      /**  For development use only.  */  
   "DevChar02":string,
      /**  For development use only.  */  
   "DevChar03":string,
      /**  For development use only.  */  
   "DevChar04":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PODetail.ContractQty  */  
   "ContractQty":number,
      /**  Part.PartDescription  */  
   "PartDescription":string,
      /**  VendorID  */  
   "VendorID":string,
      /**  POHeader.PurPoint  */  
   "PurPoint":string,
   "POSuggLastPackSlip":string,
   "LastPackSlip":string,
   "LastReceiptDate":string,
   "LastReceiptOurQty":number,
      /**  PODetail.ContractQtyUOM  */  
   "ContractQtyUOM":string,
      /**  Last Receipt UOM  */  
   "LastReceiptOurQtyUOM":string,
   "PurchaseScheduleMode":string,
   "ReductionMethod":number,
      /**  The sum of PORel.ArrivedQty for the current PO Line  */  
   "TotalArrivedQuantity":number,
      /**  The sum of PORel.Received for the current PO Line  */  
   "TotalReceiptQuantity":number,
      /**  VendorName  */  
   "VendorName":string,
   "BitFlag":number,
   "PartIUM":string,
   "PartPartDescription":string,
   "PlantName":string,
   "PODetailContractQty":number,
   "PODetailContractQtyUOM":string,
   "PODetailOrderQty":number,
   "POHeaderContractStartDate":string,
   "POHeaderPurPoint":string,
   "POHeaderContractEndDate":string,
   "VendorVendorID":string,
   "VendorName_":string,
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
      @param ds
   */  
export interface ApproveAllSchedulesDS_input{
   ds:Erp_Tablesets_POScheduleTableset[],
}

export interface ApproveAllSchedulesDS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POScheduleTableset,
}
}

   /** Required : 
      @param poScheduleIDList
      @param reductionMethodList
   */  
export interface ApproveAllSchedules_input{
      /**  A Guid array carrying all PO Schedule Row IDs to be approved  */  
   poScheduleIDList:string,
      /**  An int array carrying PO Schedules Reduction Method  */  
   reductionMethodList:number,
}

export interface ApproveAllSchedules_output{
}

   /** Required : 
      @param ds
   */  
export interface ApproveMultiVendorSchedule_input{
   ds:Erp_Tablesets_POScheduleTableset[],
}

export interface ApproveMultiVendorSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POScheduleTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ApproveSchedule_input{
   ds:Erp_Tablesets_POScheduleTableset[],
}

export interface ApproveSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POScheduleTableset,
}
}

   /** Required : 
      @param ipPartNum
   */  
export interface CheckOtherSchedules_input{
   ipPartNum:string,
}

export interface CheckOtherSchedules_output{
parameters : {
      /**  output parameters  */  
   opScheduleFound:boolean,
}
}

   /** Required : 
      @param ipFromField
      @param ipPlant
      @param ipContractPONum
      @param ipContractPOLine
      @param ipContractRev
      @param ds
   */  
export interface CopyQuantities_input{
      /**  The From field value  */  
   ipFromField:string,
      /**  The current Plant value  */  
   ipPlant:string,
      /**  The current ContractPONum value  */  
   ipContractPONum:number,
      /**  The current ContractPOLine value  */  
   ipContractPOLine:number,
      /**  The current ContractRev value  */  
   ipContractRev:number,
   ds:Erp_Tablesets_POScheduleTableset[],
}

export interface CopyQuantities_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POScheduleTableset,
}
}

   /** Required : 
      @param plant
      @param contractPONum
      @param contractPOLine
      @param contractRev
   */  
export interface DeleteByID_input{
   plant:string,
   contractPONum:number,
   contractPOLine:number,
   contractRev:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_POScheduleDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   ContractPONum:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ContractPOLine:number,
      /**  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  */  
   ContractRev:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   ContractPORelNum:number,
      /**  The last Packing Slip processed for this Contract Purchase Order.  */  
   LastPackSlip:string,
      /**  The Receipt Date of the last Receipt for this Contract Purchase Order.  */  
   LastReceiptDate:string,
      /**  Receipt quantity in our unit of measure.  */  
   LastReceiptOurQty:number,
      /**  Date of the current schedule, suggested demand, adjusted schedule, or proposed schedule.  */  
   ScheduleDate:string,
      /**  The Week Number relating to the Work Date.  */  
   WeekNum:number,
      /**  The Week Year relating to the Work Date.  */  
   WeekYear:number,
      /**  Current Scheduled Quantity corresponding to a PORel.  */  
   CurrentOurQty:number,
      /**  The quantity created by the Generate PO Suggestions process.  */  
   SuggestedOurQty:number,
      /**  The quantity that the Generate PO Schedules process is suggesting.  Includes a minimum quantity and is determined by the Periodicity code being used.  */  
   AdjustedOurQty:number,
      /**  Quantity the user may propose via the Purchase Order Contract Schedule Maintenance.  */  
   ProposedOurQty:number,
      /**  Inventory UOM  */  
   OurQtyUOM:string,
      /**  The last packing slip number that a receipt was made against this Purchase Order Contract at the time Generate Purchase Suggestions was run.  */  
   POSuggLastPackSlip:string,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  */  
   PurchasingFactor:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  For development use only.  */  
   DevChar01:string,
      /**  For development use only.  */  
   DevChar02:string,
      /**  For development use only.  */  
   DevChar03:string,
      /**  For development use only.  */  
   DevChar04:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Adjusted Our Qty displayed in terms of the Primary UOM of the Part.  */  
   AdjustedOurQtyDisp:number,
      /**  Current Our Qty displayed in terms of the Primary UOM of the Part.  */  
   CurrentOurQtyDisp:number,
      /**  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  */  
   ProposedOurQtyDisp:number,
      /**  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  */  
   SuggestedOurQtyDisp:number,
      /**  Primary Inventory UOM for the Part  */  
   IUM:string,
   ReceivedOurQtyDisp:number,
   BitFlag:number,
   PlantName:string,
   PODetailPartNum:string,
   PODetailPUM:string,
   PORelReceivedQty:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POScheduleListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   ContractPONum:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ContractPOLine:number,
      /**  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  */  
   ContractRev:number,
      /**  Date the Purchase Order Schedule was created.  */  
   CreateDate:string,
      /**  Date the Purchase Order Schedule was approved.  */  
   ApprovedDate:string,
      /**  Date the Purchase Order Schedule was printed.  */  
   PrintedDate:string,
      /**  Date the Purchase Order Schedule was last executed.  */  
   LastRunDate:string,
      /**  Is this Revision of the Purchase Order Schedule active?  */  
   ActiveRevision:boolean,
      /**  Part Number for this Purchase Order Contract Schedule.  */  
   PartNum:string,
      /**  Supplier Number for this Purchase Order Contract Schedule.  */  
   VendorNum:number,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  For development use only.  */  
   DevChar01:string,
      /**  For development use only.  */  
   DevChar02:string,
      /**  For development use only.  */  
   DevChar03:string,
      /**  For development use only.  */  
   DevChar04:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  POHeader.ContractEndDate  */  
   ContractEndDate:string,
      /**  POHeader.ContractStartDate  */  
   ContractStartDate:string,
      /**  PODetail.ContractQty  */  
   ContractQty:number,
      /**  Part.PartDescription  */  
   PartDescription:string,
      /**  VendorID  */  
   VendorID:string,
      /**  VendorName  */  
   VendorName:string,
      /**  POHeader.PurPoint  */  
   PurPoint:string,
   POSuggLastPackSlip:string,
   LastPackSlip:string,
   LastReceiptDate:string,
   LastReceiptOurQty:number,
      /**  PODetail.ContractQtyUOM  */  
   ContractQtyUOM:string,
      /**  Last Receipt UOM  */  
   LastReceiptOurQtyUOM:string,
   PurchaseScheduleMode:string,
   ReductionMethod:number,
      /**  The sum of PORel.ArrivedQty for the current PO Line  */  
   TotalArrivedQuantity:number,
      /**  The sum of PORel.Received for the current PO Line  */  
   TotalReceiptQuantity:number,
   PartPartDescription:string,
   PartIUM:string,
   PlantName:string,
   PODetailContractQty:number,
   PODetailContractQtyUOM:string,
   PODetailOrderQty:number,
   POHeaderPurPoint:string,
   POHeaderContractEndDate:string,
   POHeaderContractStartDate:string,
   VendorVendorID:string,
   VendorName_:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POScheduleListTableset{
   POScheduleList:Erp_Tablesets_POScheduleListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_POScheduleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   ContractPONum:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ContractPOLine:number,
      /**  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  */  
   ContractRev:number,
      /**  Date the Purchase Order Schedule was created.  */  
   CreateDate:string,
      /**  Date the Purchase Order Schedule was approved.  */  
   ApprovedDate:string,
      /**  Date the Purchase Order Schedule was printed.  */  
   PrintedDate:string,
      /**  Date the Purchase Order Schedule was last executed.  */  
   LastRunDate:string,
      /**  Is this Revision of the Purchase Order Schedule active?  */  
   ActiveRevision:boolean,
      /**  Part Number for this Purchase Order Contract Schedule.  */  
   PartNum:string,
      /**  Supplier Number for this Purchase Order Contract Schedule.  */  
   VendorNum:number,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  For development use only.  */  
   DevChar01:string,
      /**  For development use only.  */  
   DevChar02:string,
      /**  For development use only.  */  
   DevChar03:string,
      /**  For development use only.  */  
   DevChar04:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PODetail.ContractQty  */  
   ContractQty:number,
      /**  Part.PartDescription  */  
   PartDescription:string,
      /**  VendorID  */  
   VendorID:string,
      /**  POHeader.PurPoint  */  
   PurPoint:string,
   POSuggLastPackSlip:string,
   LastPackSlip:string,
   LastReceiptDate:string,
   LastReceiptOurQty:number,
      /**  PODetail.ContractQtyUOM  */  
   ContractQtyUOM:string,
      /**  Last Receipt UOM  */  
   LastReceiptOurQtyUOM:string,
   PurchaseScheduleMode:string,
   ReductionMethod:number,
      /**  The sum of PORel.ArrivedQty for the current PO Line  */  
   TotalArrivedQuantity:number,
      /**  The sum of PORel.Received for the current PO Line  */  
   TotalReceiptQuantity:number,
      /**  VendorName  */  
   VendorName:string,
   BitFlag:number,
   PartIUM:string,
   PartPartDescription:string,
   PlantName:string,
   PODetailContractQty:number,
   PODetailContractQtyUOM:string,
   PODetailOrderQty:number,
   POHeaderContractStartDate:string,
   POHeaderPurPoint:string,
   POHeaderContractEndDate:string,
   VendorVendorID:string,
   VendorName_:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POScheduleTableset{
   POSchedule:Erp_Tablesets_POScheduleRow[],
   POScheduleDtl:Erp_Tablesets_POScheduleDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPOScheduleTableset{
   POSchedule:Erp_Tablesets_POScheduleRow[],
   POScheduleDtl:Erp_Tablesets_POScheduleDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param contractPONum
      @param contractPOLine
      @param contractRev
   */  
export interface GetByID_input{
   plant:string,
   contractPONum:number,
   contractPOLine:number,
   contractRev:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_POScheduleTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_POScheduleTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_POScheduleTableset[],
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
   returnObj:Erp_Tablesets_POScheduleListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param contractPONum
      @param contractPOLine
      @param contractRev
   */  
export interface GetNewPOScheduleDtl_input{
   ds:Erp_Tablesets_POScheduleTableset[],
   plant:string,
   contractPONum:number,
   contractPOLine:number,
   contractRev:number,
}

export interface GetNewPOScheduleDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POScheduleTableset,
}
}

   /** Required : 
      @param ds
      @param plant
      @param contractPONum
      @param contractPOLine
   */  
export interface GetNewPOSchedule_input{
   ds:Erp_Tablesets_POScheduleTableset[],
   plant:string,
   contractPONum:number,
   contractPOLine:number,
}

export interface GetNewPOSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POScheduleTableset,
}
}

   /** Required : 
      @param whereClausePOSchedule
      @param whereClausePOScheduleDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePOSchedule:string,
   whereClausePOScheduleDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_POScheduleTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSharedSupplierValidation_output{
parameters : {
      /**  output parameters  */  
   opSharedSupplierValidation:boolean,
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
      @param ipPONum
      @param ipPOLine
   */  
export interface LastPackSlip_input{
   ipPONum:number,
   ipPOLine:number,
}

export interface LastPackSlip_output{
parameters : {
      /**  output parameters  */  
   opPackSlip:string,
   opReceiptDate:string,
   opReceiptOurQty:number,
   opReceiptOurQtyUOM:string,
}
}

   /** Required : 
      @param ipSharedSupplierValidation
   */  
export interface SetSharedSupplierValidation_input{
      /**  True or False  */  
   ipSharedSupplierValidation:boolean,
}

export interface SetSharedSupplierValidation_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPOScheduleTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPOScheduleTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_POScheduleTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POScheduleTableset,
}
}

