import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ContainerTrackingSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/$metadata", {
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
   Description: Get ContainerTrackings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerTrackings
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderRow
   */  
export function get_ContainerTrackings(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerTrackings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerTrackings(requestBody:Erp_Tablesets_ContainerHeaderRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerTracking item
   Description: Calls GetByID to retrieve the ContainerTracking item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerTracking
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerHeaderRow
   */  
export function get_ContainerTrackings_Company_ContainerID(Company:string, ContainerID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")", {
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
         resolve(data as Erp_Tablesets_ContainerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerTracking for the service
   Description: Calls UpdateExt to update ContainerTracking. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerTracking
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerTrackings_Company_ContainerID(Company:string, ContainerID:string, requestBody:Erp_Tablesets_ContainerHeaderRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")", {
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
   Summary: Call UpdateExt to delete ContainerTracking item
   Description: Call UpdateExt to delete ContainerTracking item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerTracking
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerTrackings_Company_ContainerID(Company:string, ContainerID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")", {
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
   Description: Get ContainerDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDetails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerDetails(Company:string, ContainerID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerDetails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerDetail item
   Description: Calls GetByID to retrieve the ContainerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDetailRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ContainerHeaderTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerHeaderTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderTaxRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerHeaderTaxes(Company:string, ContainerID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerHeaderTax item
   Description: Calls GetByID to retrieve the ContainerHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ContainerMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerMiscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerMiscs(Company:string, ContainerID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerMiscs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerMisc item
   Description: Calls GetByID to retrieve the ContainerMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMisc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerMiscRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerMiscs_Company_ContainerID_MiscSeq(Company:string, ContainerID:string, MiscSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ContainerHeaderAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerHeaderAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderAttchRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerHeaderAttches(Company:string, ContainerID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerHeaderAttch item
   Description: Calls GetByID to retrieve the ContainerHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   */  
export function get_ContainerTrackings_Company_ContainerID_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company:string, ContainerID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ContainerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDetails
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailRow
   */  
export function get_ContainerDetails(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerDetails(requestBody:Erp_Tablesets_ContainerDetailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerDetail item
   Description: Calls GetByID to retrieve the ContainerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDetailRow
   */  
export function get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerDetail for the service
   Description: Calls UpdateExt to update ContainerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, requestBody:Erp_Tablesets_ContainerDetailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
   Summary: Call UpdateExt to delete ContainerDetail item
   Description: Call UpdateExt to delete ContainerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
   Description: Get ContainerDetailTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDetailTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailTaxRow
   */  
export function get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailTaxes(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerDetailTax item
   Description: Calls GetByID to retrieve the ContainerDetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   */  
export function get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ContainerDuties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDuties1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDutyRow
   */  
export function get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDuties(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDuties", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerDuty item
   Description: Calls GetByID to retrieve the ContainerDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDuty1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDutyRow
   */  
export function get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DutySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ContainerDetailAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDetailAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailAttchRow
   */  
export function get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailAttches(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerDetailAttch item
   Description: Calls GetByID to retrieve the ContainerDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   */  
export function get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ContainerDetailTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDetailTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailTaxRow
   */  
export function get_ContainerDetailTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDetailTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerDetailTaxes(requestBody:Erp_Tablesets_ContainerDetailTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerDetailTax item
   Description: Calls GetByID to retrieve the ContainerDetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   */  
export function get_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerDetailTax for the service
   Description: Calls UpdateExt to update ContainerDetailTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDetailTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_ContainerDetailTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete ContainerDetailTax item
   Description: Call UpdateExt to delete ContainerDetailTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDetailTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get ContainerDuties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDuties
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDutyRow
   */  
export function get_ContainerDuties(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDuties
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDutyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerDutyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerDuties(requestBody:Erp_Tablesets_ContainerDutyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerDuty item
   Description: Calls GetByID to retrieve the ContainerDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDuty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDutyRow
   */  
export function get_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DutySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerDuty for the service
   Description: Calls UpdateExt to update ContainerDuty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDuty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDutyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DutySeq:string, requestBody:Erp_Tablesets_ContainerDutyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")", {
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
   Summary: Call UpdateExt to delete ContainerDuty item
   Description: Call UpdateExt to delete ContainerDuty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDuty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DutySeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")", {
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
   Description: Get ContainerDetailAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDetailAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailAttchRow
   */  
export function get_ContainerDetailAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDetailAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerDetailAttches(requestBody:Erp_Tablesets_ContainerDetailAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerDetailAttch item
   Description: Calls GetByID to retrieve the ContainerDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   */  
export function get_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerDetailAttch for the service
   Description: Calls UpdateExt to update ContainerDetailAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_ContainerDetailAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ContainerDetailAttch item
   Description: Call UpdateExt to delete ContainerDetailAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company:string, ContainerID:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
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
   Description: Get ContainerHeaderTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerHeaderTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderTaxRow
   */  
export function get_ContainerHeaderTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerHeaderTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerHeaderTaxes(requestBody:Erp_Tablesets_ContainerHeaderTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerHeaderTax item
   Description: Calls GetByID to retrieve the ContainerHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   */  
export function get_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerHeaderTax for the service
   Description: Calls UpdateExt to update ContainerHeaderTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerHeaderTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_ContainerHeaderTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete ContainerHeaderTax item
   Description: Call UpdateExt to delete ContainerHeaderTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerHeaderTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get ContainerMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerMiscs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscRow
   */  
export function get_ContainerMiscs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerMiscs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerMiscs(requestBody:Erp_Tablesets_ContainerMiscRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerMisc item
   Description: Calls GetByID to retrieve the ContainerMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerMiscRow
   */  
export function get_ContainerMiscs_Company_ContainerID_MiscSeq(Company:string, ContainerID:string, MiscSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerMisc for the service
   Description: Calls UpdateExt to update ContainerMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerMiscs_Company_ContainerID_MiscSeq(Company:string, ContainerID:string, MiscSeq:string, requestBody:Erp_Tablesets_ContainerMiscRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")", {
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
   Summary: Call UpdateExt to delete ContainerMisc item
   Description: Call UpdateExt to delete ContainerMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerMiscs_Company_ContainerID_MiscSeq(Company:string, ContainerID:string, MiscSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")", {
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
   Description: Get ContainerMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerMiscTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscTaxRow
   */  
export function get_ContainerMiscs_Company_ContainerID_MiscSeq_ContainerMiscTaxes(Company:string, ContainerID:string, MiscSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")/ContainerMiscTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContainerMiscTax item
   Description: Calls GetByID to retrieve the ContainerMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMiscTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   */  
export function get_ContainerMiscs_Company_ContainerID_MiscSeq_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ContainerMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerMiscTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscTaxRow
   */  
export function get_ContainerMiscTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerMiscTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerMiscTaxes(requestBody:Erp_Tablesets_ContainerMiscTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerMiscTax item
   Description: Calls GetByID to retrieve the ContainerMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   */  
export function get_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerMiscTax for the service
   Description: Calls UpdateExt to update ContainerMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_ContainerMiscTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete ContainerMiscTax item
   Description: Call UpdateExt to delete ContainerMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, ContainerID:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get ContainerHeaderAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerHeaderAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderAttchRow
   */  
export function get_ContainerHeaderAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerHeaderAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerHeaderAttches(requestBody:Erp_Tablesets_ContainerHeaderAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ContainerHeaderAttch item
   Description: Calls GetByID to retrieve the ContainerHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   */  
export function get_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company:string, ContainerID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ContainerHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerHeaderAttch for the service
   Description: Calls UpdateExt to update ContainerHeaderAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerHeaderAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company:string, ContainerID:string, DrawingSeq:string, requestBody:Erp_Tablesets_ContainerHeaderAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ContainerHeaderAttch item
   Description: Call UpdateExt to delete ContainerHeaderAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerHeaderAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContainerID Desc: ContainerID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company:string, ContainerID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseContainerHeader:string, whereClauseContainerHeaderAttch:string, whereClauseContainerDetail:string, whereClauseContainerDetailAttch:string, whereClauseContainerDetailTax:string, whereClauseContainerDuty:string, whereClauseContainerHeaderTax:string, whereClauseContainerMisc:string, whereClauseContainerMiscTax:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseContainerHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerHeader=" + whereClauseContainerHeader
   }
   if(typeof whereClauseContainerHeaderAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerHeaderAttch=" + whereClauseContainerHeaderAttch
   }
   if(typeof whereClauseContainerDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerDetail=" + whereClauseContainerDetail
   }
   if(typeof whereClauseContainerDetailAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerDetailAttch=" + whereClauseContainerDetailAttch
   }
   if(typeof whereClauseContainerDetailTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerDetailTax=" + whereClauseContainerDetailTax
   }
   if(typeof whereClauseContainerDuty!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerDuty=" + whereClauseContainerDuty
   }
   if(typeof whereClauseContainerHeaderTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerHeaderTax=" + whereClauseContainerHeaderTax
   }
   if(typeof whereClauseContainerMisc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerMisc=" + whereClauseContainerMisc
   }
   if(typeof whereClauseContainerMiscTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerMiscTax=" + whereClauseContainerMiscTax
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetRows" + params, {
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
export function get_GetByID(containerID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof containerID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "containerID=" + containerID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetList" + params, {
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
   Summary: Invoke method CalculateContainerTaxes
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
   OperationID: CalculateContainerTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateContainerTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateContainerTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateContainerTaxes(requestBody:CalculateContainerTaxes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateContainerTaxes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/CalculateContainerTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CalculateContainerTaxes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateContainerIndCost
   Description: Creates the default Miscellaneous Charges for the Container based on the
selected APInvMsc records.
   OperationID: CreateContainerIndCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateContainerIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateContainerIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateContainerIndCost(requestBody:CreateContainerIndCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateContainerIndCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/CreateContainerIndCost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateContainerIndCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMultiDetails
   Description: Purpose:
Parameters:
<param name="ds">Container Tracking Data Set</param><param name="containerErrors">List of PO releases not added as container details </param><param name="detailAdded">Indicates that at least one detail was added and is used by the UI to determine if the zero volume message is to be displayed </param>
Notes:
   OperationID: CreateMultiDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMultiDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMultiDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMultiDetails(requestBody:CreateMultiDetails_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMultiDetails_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/CreateMultiDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateMultiDetails_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DisburseLandedCosts
   Description: Purpose:  Disburse the landed costs across the container details
<param name="ipContainerID">Container IDt</param><param name="opLCApplied">Total applied landed cost</param>
   OperationID: DisburseLandedCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DisburseLandedCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisburseLandedCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisburseLandedCosts(requestBody:DisburseLandedCosts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DisburseLandedCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/DisburseLandedCosts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DisburseLandedCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPInvMiscCharges
   Description: Gets the list of AP Invoice Miscellaneous Charges marked as Landed Cost and
and not linked to any container or receipt yet.
   OperationID: GetAPInvMiscCharges
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAPInvMiscCharges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPInvMiscCharges_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPInvMiscCharges(requestBody:GetAPInvMiscCharges_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPInvMiscCharges_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetAPInvMiscCharges", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetAPInvMiscCharges_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContainerClassInfo
   Description: This method defaults the container class information into
the conatiner header file whenever the container class is added/amended
   OperationID: GetContainerClassInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContainerClassInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerClassInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContainerClassInfo(requestBody:GetContainerClassInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContainerClassInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetContainerClassInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetContainerClassInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContainerDetailToSplit
   Description: Gets the Detail of a specific Container Header to be splitted.
   OperationID: GetContainerDetailToSplit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContainerDetailToSplit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerDetailToSplit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContainerDetailToSplit(requestBody:GetContainerDetailToSplit_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContainerDetailToSplit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetContainerDetailToSplit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetContainerDetailToSplit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContainerMiscToTransfer
   Description: Gets the Indirect Costs of a specific Container Header to be transfered.
   OperationID: GetContainerMiscToTransfer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContainerMiscToTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerMiscToTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContainerMiscToTransfer(requestBody:GetContainerMiscToTransfer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContainerMiscToTransfer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetContainerMiscToTransfer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetContainerMiscToTransfer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveContainerLCAmt
   Description: Purpose:  Apply the disbursed Container's additional Landed Costs among the existing
Container Receipt details.  This procedure share similar logic used in the
ReceiveContainerLCAmt procedure for distributing the LCAmt as a regular receipt
mtlburden cost or variance cost. This procedure does not create new RcvDtl
record for the remainder of qty to be received.
<param name="inContainerID">Container ID</param><param name="opMessage">Message to return back to user.</param>
   OperationID: ReceiveContainerLCAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveContainerLCAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerLCAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveContainerLCAmt(requestBody:ReceiveContainerLCAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveContainerLCAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ReceiveContainerLCAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReceiveContainerLCAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshLCApplied
   Description: Purpose:  Refresh the external field LCAppliedAmt after a change to LC detail amount
Parameters:
<param name="ipContainerID">Container ID</param><param name="opLCApplied">Calculated Landed Cost applied amount</param>
Notes:
   OperationID: RefreshLCApplied
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshLCApplied_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshLCApplied_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshLCApplied(requestBody:RefreshLCApplied_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshLCApplied_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/RefreshLCApplied", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshLCApplied_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetLandedCostDisbursements
   Description: Initialize landed cost amounts to 0 and updates the landed cost disburse method.
   OperationID: ResetLandedCostDisbursements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetLandedCostDisbursements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetLandedCostDisbursements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetLandedCostDisbursements(requestBody:ResetLandedCostDisbursements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetLandedCostDisbursements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ResetLandedCostDisbursements", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ResetLandedCostDisbursements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ShipContainer
   Description: container To Ship
   OperationID: ShipContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ShipContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShipContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipContainer(requestBody:ShipContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ShipContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ShipContainer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ShipContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SplitContainerShipment
   Description: Splits a Container by creating a new Container Header and assigning the
selected Container Detail lines into the new Container.
   OperationID: SplitContainerShipment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SplitContainerShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SplitContainerShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SplitContainerShipment(requestBody:SplitContainerShipment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SplitContainerShipment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/SplitContainerShipment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SplitContainerShipment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TransferIndirectCosts
   Description: Transfers Indirect Costs from one container to another.
   OperationID: TransferIndirectCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TransferIndirectCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransferIndirectCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransferIndirectCosts(requestBody:TransferIndirectCosts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TransferIndirectCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/TransferIndirectCosts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TransferIndirectCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnShipContainer
   Description: container To UnShip
   OperationID: UnShipContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnShipContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnShipContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnShipContainer(requestBody:UnShipContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnShipContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/UnShipContainer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnShipContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateLCAppliedAmt
   Description: Purpose:  Update the applied landed cost
Parameters:  none
<param name="origLCAmt">original landed cost amount</param><param name="newLCAmt">new landed cost amount</param><param name="ipcontainerID">container ID</param><param name="ipAppliedAmt">current applied landed cost amount</param><param name="totApplied">total applied landed cost</param>
Notes:
   OperationID: UpdateLCAppliedAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateLCAppliedAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLCAppliedAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateLCAppliedAmt(requestBody:UpdateLCAppliedAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateLCAppliedAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/UpdateLCAppliedAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateLCAppliedAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateLandedCostDisbursements
   Description: Purpose: Validate the landed cost distributions
Parameters:
<param name="ipContainerID">Container ID</param><param name="ds">Container Tracking Data Set</param><param name="lcError">error message</param>
   OperationID: ValidateLandedCostDisbursements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateLandedCostDisbursements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLandedCostDisbursements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateLandedCostDisbursements(requestBody:ValidateLandedCostDisbursements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateLandedCostDisbursements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ValidateLandedCostDisbursements", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateLandedCostDisbursements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcDtlExtTransValue
   Description: Purpose: Calculate Container Indirect Costs / Extended Costs and Duty
Parameters:  none
<param name="ds">ContainerTrackingTableSet</param>
Notes:
   OperationID: CalcDtlExtTransValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalcDtlExtTransValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcDtlExtTransValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcDtlExtTransValue(requestBody:CalcDtlExtTransValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalcDtlExtTransValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/CalcDtlExtTransValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CalcDtlExtTransValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateExtCostAndWeight
   Description: Purpose:  recalculates the weight and extcost and is called whenever the
ship qty changes
Parameters:
<param name="shipQty">Quantity to ship</param><param name="shipUOM">Shipping UOM</param><param name="partNum">Part number on container detail</param><param name="ourUnitCost">Unit Cost on container detail</param><param name="weight">Extended weight of detail</param><param name="grossWeight">Gross weight of detail</param><param name="vExtCost">Extended container cost or value</param><param name="poNum">Container PO Number</param><param name="poLine">Container PO Line</param>
Notes:
   OperationID: CalculateExtCostAndWeight
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateExtCostAndWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateExtCostAndWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateExtCostAndWeight(requestBody:CalculateExtCostAndWeight_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateExtCostAndWeight_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/CalculateExtCostAndWeight", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CalculateExtCostAndWeight_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlPOInfo
   Description: This method updates the dataset when the detail Line PONum field has changed.
   OperationID: GetDtlPOInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlPOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlPOInfo(requestBody:GetDtlPOInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlPOInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetDtlPOInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDtlPOInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlPOLineInfo
   Description: This method updates the dataset when the detail Line POLine field has changed.
   OperationID: GetDtlPOLineInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlPOLineInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOLineInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlPOLineInfo(requestBody:GetDtlPOLineInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlPOLineInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetDtlPOLineInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDtlPOLineInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlQtyInfo
   Description: This method updates the dataset when the ShipQty or IUM field changes
   OperationID: GetDtlQtyInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlQtyInfo(requestBody:GetDtlQtyInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlQtyInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetDtlQtyInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDtlQtyInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOReleaseInfo
   Description: This method defaults the container class information into
the conatiner header file whenever the container class is added/amended
   OperationID: GetPOReleaseInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPOReleaseInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOReleaseInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOReleaseInfo(requestBody:GetPOReleaseInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPOReleaseInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetPOReleaseInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPOReleaseInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlCommodity
   Description: This method should be invoked when the CommodityCode in ContainerDetail changes.
This method will validate the commodity code and get defaults.
   OperationID: OnChangeDtlCommodity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCommodity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCommodity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlCommodity(requestBody:OnChangeDtlCommodity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlCommodity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDtlCommodity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDtlCommodity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlCountryNum
   Description: This method should be invoked when the OrigCountryNum in ContainerDetail changes.
This method will validate country of origin.
   OperationID: OnChangeDtlCountryNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlCountryNum(requestBody:OnChangeDtlCountryNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlCountryNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDtlCountryNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDtlCountryNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlLCIndCost
   Description: This method should be invoked when the LCIndCost in ContainerDetail changes.
This method will validate the manually disbursed indirect cost.
   OperationID: OnChangeDtlLCIndCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlLCIndCost(requestBody:OnChangeDtlLCIndCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlLCIndCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDtlLCIndCost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDtlLCIndCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlUpliftPercent
   Description: This method should be invoked when the UpliftPercent in ContainerDetail changes.
This method will validate the UpliftPercent and calculate the Uplift Indirect Cost.
   OperationID: OnChangeDtlUpliftPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlUpliftPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlUpliftPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlUpliftPercent(requestBody:OnChangeDtlUpliftPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlUpliftPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDtlUpliftPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDtlUpliftPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPOTransValue
   Description: This method should be invoked when the PO Transaction Value has changed.
   OperationID: OnChangedPOTransValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedPOTransValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPOTransValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPOTransValue(requestBody:OnChangedPOTransValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedPOTransValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangedPOTransValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangedPOTransValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateShipQty
   Description: Purpose:  Validate the container detail ship qty
Parameters:
<param name="shipQty">Proposed Ship Qty</param><param name="shipUOM">Ship Qty UOM</param><param name="ium">PODetail.IUM</param><param name="partNum">PartNum</param><param name="poNum">Purchase order number</param><param name="poLine">Purchase order line number</param><param name="poRelNum">Purchase order release number</param><param name="WarningMsg">Warning mesage</param>
Notes:
   OperationID: ValidateShipQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateShipQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShipQty(requestBody:ValidateShipQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateShipQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ValidateShipQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateShipQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlTaxCatID
   Description: This method should be invoked when TaxCatID changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxCatID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlTaxCatID(requestBody:OnChangeDtlTaxCatID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlTaxCatID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDtlTaxCatID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDtlTaxCatID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlTaxExempt
   Description: This method should be invoked when TaxExempt changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxExempt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlTaxExempt(requestBody:OnChangeDtlTaxExempt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlTaxExempt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDtlTaxExempt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDtlTaxExempt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedDetailTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates DetailTax
tax amounts based on the new tax percent.
   OperationID: OnChangedDetailTaxManual
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedDetailTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDetailTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedDetailTaxManual(requestBody:OnChangedDetailTaxManual_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedDetailTaxManual_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangedDetailTaxManual", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangedDetailTaxManual_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxFixedAmount
   Description: Method to call when changing the fixed amount on the ContainerDetailTax table currently
   OperationID: OnChangeDetailTaxFixedAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxFixedAmount(requestBody:OnChangeDetailTaxFixedAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxFixedAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxFixedAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxFixedAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates ContainerDetailTax
tax amounts based on the new tax percent.
   OperationID: OnChangeDetailTaxTaxPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxTaxPercent(requestBody:OnChangeDetailTaxTaxPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxTaxPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxTaxPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxTaxPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxRateCode
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: OnChangeDetailTaxRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxRateCode(requestBody:OnChangeDetailTaxRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxRateCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates DetailTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeDetailTaxReportableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxReportableAmt(requestBody:OnChangeDetailTaxReportableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxReportableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxReportableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxReportableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates DetailTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeDetailTaxTaxableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxTaxableAmt(requestBody:OnChangeDetailTaxTaxableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxTaxableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxTaxableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxTaxableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates DetailTax
tax amounts based on the new tax amount.
   OperationID: OnChangeDetailTaxTaxAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxTaxAmt(requestBody:OnChangeDetailTaxTaxAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxTaxAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxTaxAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxTaxAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates DetailTax
tax amounts based on the new tax percent.
   OperationID: OnChangeDetailTaxTaxDeductable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxTaxDeductable(requestBody:OnChangeDetailTaxTaxDeductable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxTaxDeductable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxTaxDeductable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxTaxDeductable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDetailTaxTaxCode
   Description: Method to call when changing the tax code on a DetailTax record.  Validates the tax code and
updates DetailTax tax amounts based on the new tax code.
   OperationID: OnChangeDetailTaxTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDetailTaxTaxCode(requestBody:OnChangeDetailTaxTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDetailTaxTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDetailTaxTaxCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDetailTaxTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedMiscTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates MiscTax
tax amounts based on the new tax percent.
   OperationID: OnChangedMiscTaxManual
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedMiscTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedMiscTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedMiscTaxManual(requestBody:OnChangedMiscTaxManual_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedMiscTaxManual_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangedMiscTaxManual", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangedMiscTaxManual_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxFixedAmount
   Description: Method to call when changing the fixed amount on the ContainerMiscTax table currently
   OperationID: OnChangeMiscTaxFixedAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxFixedAmount(requestBody:OnChangeMiscTaxFixedAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxFixedAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxFixedAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxFixedAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates ContainerMiscTax
tax amounts based on the new tax percent.
   OperationID: OnChangeMiscTaxTaxPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxTaxPercent(requestBody:OnChangeMiscTaxTaxPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxTaxPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxTaxPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxTaxPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxRateCode
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: OnChangeMiscTaxRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxRateCode(requestBody:OnChangeMiscTaxRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxRateCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates MiscTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeMiscTaxReportableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxReportableAmt(requestBody:OnChangeMiscTaxReportableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxReportableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxReportableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxReportableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates MiscTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeMiscTaxTaxableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxTaxableAmt(requestBody:OnChangeMiscTaxTaxableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxTaxableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxTaxableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxTaxableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates MiscTax
tax amounts based on the new tax amount.
   OperationID: OnChangeMiscTaxTaxAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxTaxAmt(requestBody:OnChangeMiscTaxTaxAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxTaxAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxTaxAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxTaxAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates MiscTax
tax amounts based on the new tax percent.
   OperationID: OnChangeMiscTaxTaxDeductable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxTaxDeductable(requestBody:OnChangeMiscTaxTaxDeductable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxTaxDeductable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxTaxDeductable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxTaxDeductable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxTaxCode
   Description: Method to call when changing the tax code on a MiscTax record.  Validates the tax code and
updates MiscTax tax amounts based on the new tax code.
   OperationID: OnChangeMiscTaxTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxTaxCode(requestBody:OnChangeMiscTaxTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxTaxCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDutyTariffCode
   Description: This method should be invoked when the Tariff Code changes. This method will validate
the tariffcode and defaults the duty amount.
   OperationID: OnChangeDutyTariffCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDutyTariffCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDutyTariffCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDutyTariffCode(requestBody:OnChangeDutyTariffCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDutyTariffCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDutyTariffCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDutyTariffCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckContainerBeforeShipping
   Description: Purpose:  Edit container before allowing user to ship
Parameters:
<param name="ipContainerID">ContainerID</param>
Notes:
   OperationID: CheckContainerBeforeShipping
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckContainerBeforeShipping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckContainerBeforeShipping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckContainerBeforeShipping(requestBody:CheckContainerBeforeShipping_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckContainerBeforeShipping_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/CheckContainerBeforeShipping", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckContainerBeforeShipping_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultContainerCost
   Description: Calculates container cost when CostPerVolume or Volume change
   OperationID: DefaultContainerCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultContainerCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultContainerCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultContainerCost(requestBody:DefaultContainerCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultContainerCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/DefaultContainerCost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultContainerCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultCostPerVolume
   Description: Calculates the CostPerVolume
   OperationID: DefaultCostPerVolume
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultCostPerVolume_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultCostPerVolume_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultCostPerVolume(requestBody:DefaultCostPerVolume_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultCostPerVolume_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/DefaultCostPerVolume", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultCostPerVolume_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeContainerClass
   Description: This method should be invoked when the Kinetic Container Class ID changes. This method will validate
the container class and pull in the new default class information.
   OperationID: OnChangeContainerClass
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeContainerClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeContainerClass(requestBody:OnChangeContainerClass_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeContainerClass_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeContainerClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeContainerClass_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShippingDays
   Description: This method should be invoked when the Kinetic Container Header Shipping Days changes.
   OperationID: OnChangeShippingDays
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShippingDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShippingDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShippingDays(requestBody:OnChangeShippingDays_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShippingDays_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeShippingDays", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeShippingDays_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShipDate
   Description: This method should be invoked when the Kinetic Container Header Ship Date changes.
   OperationID: OnChangeShipDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShipDate(requestBody:OnChangeShipDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShipDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeShipDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeShipDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDueDate
   Description: This method should be invoked when the Kinetic Container Header Due Date changes.
   OperationID: OnChangeDueDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDueDate(requestBody:OnChangeDueDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDueDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeDueDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDueDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeContainerDetailLCIndCost
   Description: This method should be invoked when the Kinetic ContainerDetail LCIndCost changes.
   OperationID: OnChangeContainerDetailLCIndCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeContainerDetailLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerDetailLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeContainerDetailLCIndCost(requestBody:OnChangeContainerDetailLCIndCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeContainerDetailLCIndCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeContainerDetailLCIndCost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeContainerDetailLCIndCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateDetailExtValues
   Description: This method should be invoked when the Kinetic ContainerDetail ContainerShipQty or ShipQtyUOm changes.
   OperationID: CalculateDetailExtValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateDetailExtValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateDetailExtValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateDetailExtValues(requestBody:CalculateDetailExtValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateDetailExtValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/CalculateDetailExtValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CalculateDetailExtValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeClassCode
   Description: This method should be invoked when the Container Class ID changes. This method will validate
the container class and pull in the new default class information.
   OperationID: OnChangeClassCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeClassCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClassCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeClassCode(requestBody:OnChangeClassCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeClassCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeClassCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeClassCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeConNum
   Description: This method should be invoked when the ConNum changes. This method will validate
the VendCnt and pull in the new default information.
   OperationID: OnChangeConNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeConNum(requestBody:OnChangeConNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeConNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeConNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeConNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLoadPort
   Description: This method should be invoked when the Loading Port ID changes.
This method validate selected Port and set default value of Country Imported From.
   OperationID: OnChangeLoadPort
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLoadPort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLoadPort_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLoadPort(requestBody:OnChangeLoadPort_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLoadPort_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeLoadPort", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeLoadPort_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShipStatus
   Description: This method should be invoked when the Ship Status changes. This method will validate
the ship status and returns a value to indicate if the UI needs to run special method
to ship/unship container details when necessary.
   OperationID: OnChangeShipStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShipStatus(requestBody:OnChangeShipStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShipStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeShipStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeShipStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendor
   Description: This method should be invoked when the vendor ID changes. This method will validate
the vendor and pull in the new default vendor information.
   OperationID: OnChangeVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendor(requestBody:OnChangeVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdateContainer
   Description: This method will return a message if the Container Header has a change in
UpliftPercent. The user will be asked if the change should be applied to
all the Container Details as well. Also it will return a message if the Shipment Class has changed
asking if the indirect costs associated with the new class should be added to the container.
This method should be called when the user saves the record but before the Update method is called.
   OperationID: PreUpdateContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdateContainer(requestBody:PreUpdateContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreUpdateContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/PreUpdateContainer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreUpdateContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscApplyDate
   Description: This method should be invoked when the Apply Date in ContainerMisc changes.
This method will validate the date and get new exchange rate.
   OperationID: OnChangeMiscApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscApplyDate(requestBody:OnChangeMiscApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscCharge
   Description: This method should be invoked when the Miscellaneous Charge ID changes. This
method will validate the misc. charge and pull in the new default information.
   OperationID: OnChangeMiscCharge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscCharge(requestBody:OnChangeMiscCharge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscCharge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscCharge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscCharge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxCatID
   Description: This method should be invoked when TaxCatID changes. It will retrieve the default tax flag based on entered Tax Cat ID.
   OperationID: OnChangeMiscTaxCatID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxCatID(requestBody:OnChangeMiscTaxCatID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxCatID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxCatID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxCatID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnUpdateMiscCharge
   Description: This method should be invoked when the Container Detaile has changed and an update on Container Misc is needed. This
method will validate the misc. charge and pull in the new default information.
   OperationID: OnUpdateMiscCharge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnUpdateMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnUpdateMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnUpdateMiscCharge(requestBody:OnUpdateMiscCharge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnUpdateMiscCharge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnUpdateMiscCharge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnUpdateMiscCharge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscCurrencyCode
   Description: This method should be invoked when the Currency Code in ContainerMisc changes.
This method will validate the currency code and pull in the new default information.
   OperationID: OnChangeMiscCurrencyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscCurrencyCode(requestBody:OnChangeMiscCurrencyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscCurrencyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscCurrencyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscCurrencyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscDocEstimateAmt
   Description: This method should be invoked when the ContainerMisc.EstimateAmt changes. This
method will validate the amount and convert it to the base currency.
   OperationID: OnChangeMiscDocEstimateAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscDocEstimateAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscDocEstimateAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscDocEstimateAmt(requestBody:OnChangeMiscDocEstimateAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscDocEstimateAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscDocEstimateAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscDocEstimateAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscExchangeRate
   Description: This method should be invoked when the Currency Exchange Rate in ContainerMisc changes.
   OperationID: OnChangeMiscExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscExchangeRate(requestBody:OnChangeMiscExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscInvoiceLine
   Description: This method should be invoked when the Invoice Line in ContainerMisc changes.
This method will validate the invoice line and pull in the new default information.
   OperationID: OnChangeMiscInvoiceLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscInvoiceLine(requestBody:OnChangeMiscInvoiceLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscInvoiceLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscInvoiceLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscInvoiceLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscInvoiceNum
   Description: This method should be invoked when the Invoice Number in ContainerMisc changes.
This method will validate the invoice number and pull in the new default information.
   OperationID: OnChangeMiscInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscInvoiceNum(requestBody:OnChangeMiscInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscMscNum
   Description: This method should be invoked when the MscNum in ContainerMisc changes.
This method will validate the MscNum and pull in the new default information.
   OperationID: OnChangeMiscMscNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscMscNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscMscNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscMscNum(requestBody:OnChangeMiscMscNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscMscNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscMscNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscMscNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscPercentage
   Description: This method should be invoked when the percenate value changes on a container Misc Charge
   OperationID: OnChangeMiscPercentage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscPercentage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscPercentage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscPercentage(requestBody:OnChangeMiscPercentage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscPercentage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscPercentage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscPercentage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscRateGrp
   Description: This method should be invoked when the Currency Rate Group in ContainerMisc changes.
This method will validate the rate group and get new exchange rate.
   OperationID: OnChangeMiscRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscRateGrp(requestBody:OnChangeMiscRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxRegionCode
   Description: This method should be invoked when the Tax Liability is changed.
   OperationID: OnChangeMiscTaxRegionCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxRegionCode(requestBody:OnChangeMiscTaxRegionCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxRegionCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscTaxRegionCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscTaxRegionCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscVendor
   Description: This method should be invoked when the vendor ID in ContainerMisc changes.
This method will validate the vendor and pull in the new default vendor information.
   OperationID: OnChangeMiscVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscVendor(requestBody:OnChangeMiscVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/OnChangeMiscVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMiscVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerHeader
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerHeader(requestBody:GetNewContainerHeader_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerHeader_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerHeader", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerHeader_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerHeaderAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerHeaderAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerHeaderAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerHeaderAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerHeaderAttch(requestBody:GetNewContainerHeaderAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerHeaderAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerHeaderAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerHeaderAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerDetail(requestBody:GetNewContainerDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerDetail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerDetail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerDetailAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDetailAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerDetailAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDetailAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerDetailAttch(requestBody:GetNewContainerDetailAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerDetailAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerDetailAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerDetailAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerDetailTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDetailTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerDetailTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDetailTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerDetailTax(requestBody:GetNewContainerDetailTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerDetailTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerDetailTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerDetailTax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerDuty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDuty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerDuty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDuty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerDuty(requestBody:GetNewContainerDuty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerDuty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerDuty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerDuty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerHeaderTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerHeaderTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerHeaderTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerHeaderTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerHeaderTax(requestBody:GetNewContainerHeaderTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerHeaderTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerHeaderTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerHeaderTax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerMisc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerMisc(requestBody:GetNewContainerMisc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerMisc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerMisc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerMisc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContainerMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerMiscTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContainerMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerMiscTax(requestBody:GetNewContainerMiscTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContainerMiscTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetNewContainerMiscTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewContainerMiscTax_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerDetailAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerDetailRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerDetailTaxRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDutyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerDutyRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerHeaderAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerHeaderListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerHeaderRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerHeaderTaxRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerMiscRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerMiscTaxRow,
}

export interface Erp_Tablesets_ContainerDetailAttchRow{
   "Company":string,
   "ContainerID":number,
   "PONum":number,
   "POLine":number,
   "PORelNum":number,
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

export interface Erp_Tablesets_ContainerDetailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  The quantity of the PO Release that is shipped on this container.  */  
   "ContainerShipQty":number,
      /**  UOM of Shipment Quantity.  */  
   "ShipQtyUOm":string,
      /**  Free form text describing the container detail.  */  
   "Comment":string,
      /**  Purchase order number that uniquely identifies the purchase order on this container.  */  
   "PONum":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  */  
   "PORelNum":number,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Amount of space consumed in the container by this detail line, often specified in cubic square feet.  */  
   "Volume":number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   "VolumeUOM":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCAmt":number,
      /**  Nett Weight  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   "NetWeightUOM":string,
      /**  Unit cost based on our unit of measure.  */  
   "OurUnitCost":number,
      /**  Unit cost based on our unit of measure in document currency.  */  
   "DocOurUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OurUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OurUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OurUnitCost":number,
      /**  Country Number of the Origin Country from the PO?s Supplier Purchase Point.  */  
   "OrigCountryNum":number,
      /**  Container shipment line reference or name.  */  
   "ContainerLineRef":string,
      /**  Arrived Quantity as reported in the receipt line.  */  
   "ArrivedQty":number,
      /**  Unit of Measure of the Arrived Qty.  */  
   "ArrivedQtyUOM":string,
      /**  Received Quantity as reported in the receipt line.  */  
   "ReceivedQty":number,
      /**  Unit of Measure of the Received Qty  */  
   "ReceivedQtyUOM":string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   "ShipStatus":string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCDutyAmt":number,
      /**  The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCIndCost":number,
      /**  This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   "POTransValue":number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   "ExtTransValue":number,
      /**  The date the container shipment detail is received. Defaults as current system date.  */  
   "ReceivedDate":string,
      /**  Harmonized System (HS) goods classification code.  */  
   "CommodityCode":string,
      /**  The date the container shipment detail arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCSpecLineDutyAmt":number,
      /**  The total Landed Cost Amount received for this container shipment line.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCUpliftIndCost":number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.NetWeightUOM is not known.  */  
   "GrossWeightUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**  Indicates if the Receipt line is Taxable  */  
   "Taxable":boolean,
      /**  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  */  
   "TaxExempt":string,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   "InAppliedLCVariance":number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment line.  */  
   "InAppliedRcptLCAmt":number,
      /**  Internal usage for inclusive taxes - This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   "InExtTransValue":number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCAmt":number,
      /**  Internal usage for inclusive taxes - The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCDutyAmt":number,
      /**  Internal usage for inclusive taxes - The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCIndCost":number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line.The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCSpecLineDutyAmt":number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCUpliftIndCost":number,
      /**  Internal usage for inclusive taxes -This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   "InPOTransValue":number,
      /**  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  */  
   "NoTaxRecalc":boolean,
   "BaseWeight":number,
   "BaseWeightUOM":string,
      /**  Logical used by row rules to determine whether or not the container detail line is read only.  */  
   "ContainerShipped":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   "EnableTransValue":boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   "EnableUplift":boolean,
      /**  Extended container detail unit cost  */  
   "ExtCost":number,
   "IUM":string,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   "ManualLC":boolean,
      /**  Indicates if the PO release tied to this detail entry is open or closed.  */  
   "OpenPoRelease":boolean,
   "PartNum":string,
   "PlantName":string,
   "PoLineDesc":string,
      /**  Quantity already received on this PO Release  */  
   "PORelRcvdQty":number,
      /**  Remaining Qty  */  
   "PORelRemQty":number,
   "PUM":string,
      /**  Container Detail Shipped Date  */  
   "ShipDate":string,
   "SupplierPartNum":string,
      /**  The Tax Liability for the associated purchase order.  */  
   "TaxRegionCode":string,
      /**  Full description of Tax Region.  */  
   "TaxRegionDescription":string,
   "ThisTranQty":number,
   "ThisTranUOM":string,
      /**  Total dedicated Tax amount  */  
   "TotDedTaxAmt":number,
      /**  Total Self Assessed Tax amount  */  
   "TotSATaxAmt":number,
      /**  Total tax amount.  This is the sum of ContainerDetailTax.TaxAmt.  */  
   "TotTaxAmt":number,
      /**  Logical indicates to the UI when a key field has been changed.  Set this to yes if this is the row you want the UI to find and display.  */  
   "UpdatedKeyRow":boolean,
      /**  Logical indicating that a valid po number, po line and po release has been entered and the user may not update the other container detail values.  */  
   "ValidPOInfoEntered":boolean,
      /**  Flag to indicate if record can be updated.  */  
   "AllowUpdate":boolean,
   "BaseVolume":number,
   "BaseVolumeUOM":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Optional field that contains our revision. Default from the PartRev.RevisionNum field.  */  
   "RevisionNum":string,
   "BitFlag":number,
   "CommodityDescription":string,
   "ContainerHeaderContainerDescription":string,
   "ContainerHeaderShipDate":string,
   "CountryNumDescription":string,
   "POHeaderInPrice":boolean,
   "PORelBTOOrderNum":number,
   "PORelBTOOrderLine":number,
   "PORelRefCodeDesc":string,
   "PORelPurchasingFactor":number,
   "PORelXRelQty":number,
   "PORelOpenRelease":boolean,
   "PORelRelQty":number,
   "PORelNeedByDate":string,
   "PORelBTOOrderRelNum":number,
   "PORelPromiseDt":string,
   "PORelPurchasingFactorDirection":string,
   "PORelArrivedQty":number,
   "PORelDueDate":string,
   "PORelPlant":string,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerDetailTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  ReportableAmt  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who created this record  */  
   "CreatedBy":string,
      /**  Date and time when this record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Date and time when the record was last changed.  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BaseCurrSymbol":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "EnableSuperGRate":string,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrFixedAmount":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrFixedAmount":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrFixedAmount":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "DocScrDedTaxAmt":number,
   "DocScrFixedAmount":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerDutyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Purchase order number that uniquely identifies the purchase order on this container.  */  
   "PONum":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  */  
   "PORelNum":number,
      /**  Unique Number automatically assigned which is used along with ContainerID, PONum, POLine and PORelNum to uniquely identify the Duty record within the Container Shipment Line.  */  
   "DutySeq":number,
      /**  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  */  
   "TariffCode":string,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  */  
   "DutyAmt":number,
      /**  Container Duty Comments  */  
   "CommentText":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  InDutyAmt  */  
   "InDutyAmt":number,
      /**  Flag to indicate if record can be updated.  */  
   "AllowUpdate":boolean,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount - Screen Value  */  
   "ScrDutyAmt":number,
   "BitFlag":number,
   "POHeaderTaxRegionCode":string,
   "POHeaderInPrice":boolean,
   "TariffDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerHeaderAttchRow{
   "Company":string,
   "ContainerID":number,
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

export interface Erp_Tablesets_ContainerHeaderListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Date the container is to ship.  */  
   "ShipDate":string,
      /**  Logical indicating if the container has shipped.  */  
   "Shipped":boolean,
      /**  Class of this container.  Must be a valid entry in the ContainerClass master file.  */  
   "ContainerClass":string,
      /**  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "ContainerCost":number,
      /**   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  */  
   "ShippingDays":number,
      /**  Notes/comments about the container shipment.  */  
   "ContainerComments":string,
      /**  Free form text that describes this particular container.  */  
   "ContainerDescription":string,
      /**  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  */  
   "NewPoRelAtReceipt":boolean,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   "Volume":number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  */  
   "VolumeUOM":string,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   "CostPerVolume":number,
      /**  The container reference is typically the shipping company's assigned container ID.  */  
   "ContainerReference":string,
      /**  Reference information for landed cost.  */  
   "LCReference":string,
      /**  Landed Cost Comments  */  
   "LCComment":string,
      /**  This field holds the variance amount for the landed costs.  */  
   "LCVariance":number,
      /**  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  */  
   "LCDisburseMethod":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Currency Date  */  
   "CurrencyDate":string,
      /**  Total cost to ship this container in the doc currency.  */  
   "DocContainerCost":number,
      /**  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  */  
   "PORelShipOption":string,
      /**  Reporting currency value of this field  */  
   "Rpt1ContainerCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ContainerCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ContainerCost":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   "LoadPortID":string,
      /**  Valid port location where goods are unloaded.  */  
   "DechargePortID":string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   "ShipViaCode":string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   "FOB":string,
      /**  Number of Containers in this shipment.  */  
   "ContainerCount":number,
      /**  Number of Packages in this shipment.  */  
   "PackageCount":number,
      /**  Total Weight of the shipment.  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   "WeightUOM":string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  This key links the record to the Vendor file.  */  
   "VendorNum":number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   "ConNum":number,
      /**  Bill of Lading Number  */  
   "BOLading":string,
      /**  Bill of Exchange Number  */  
   "BOExchange":string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   "ShipStatus":string,
      /**  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  */  
   "PORelRcptOption":string,
      /**  Stores the number of the import document.  */  
   "ImportNum":string,
      /**  Name of the vessel containing the shipment.  */  
   "Vessel":string,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   "SpecDutyAmt":number,
      /**  The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   "AppliedLCAmt":number,
      /**  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "ContainerDutyAmt":number,
      /**  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "ContainerIndCost":number,
      /**  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  */  
   "ApplyToLC":boolean,
      /**  The date the container shipment arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  The date the container shipment is received. Defaults as current system date.  */  
   "ReceivedDate":string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   "PurPoint":string,
      /**  The total Landed Cost Amount received for this container shipment.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "UpliftIndCost":number,
      /**  The date that the Container Shipment is due to arrive.  */  
   "DueDate":string,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Stores the Country from which the document is imported.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  */  
   "ImportedFromDesc":string,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ContainerID in display format.  */  
   "DisplayContainerID":string,
      /**  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  */  
   "ResetPORelDates":boolean,
      /**  Logical used to indicate if all po rels for the current plant have been received.  */  
   "eshReceived":boolean,
      /**  Total shipment value  */  
   "TotalExtCost":number,
      /**  Total weight of the items shipped on the container detail.  */  
   "TotalWeight":number,
      /**  Amount of Landed Cost applied  */  
   "LCAppliedAmt":number,
      /**  Landed Cost account for display  */  
   "LCAccount":string,
      /**  Account Description  */  
   "LCAccountDesc":string,
   "SkipLandedCost":boolean,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  */  
   "LCMessage":string,
      /**  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  */  
   "PartialReceipt":boolean,
      /**  Display Ship Status.  */  
   "DispShipStatus":string,
      /**  Display Receipt Status  */  
   "DispRcptStatus":string,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   "EnableUplift":boolean,
      /**  Flag to indicate if record can be updated.  */  
   "AllowUpdate":boolean,
      /**  Flag to indicate if record can be updated after Receipt.  */  
   "EnableLCAfterRcpt":boolean,
      /**  Flag to indicate if container details can be split into another container shipment.  */  
   "EnableSplitContainer":boolean,
      /**  Flag to indicate if indirect costs can be transferred into another container shipment.  */  
   "EnableTransferCost":boolean,
      /**  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  */  
   "UpdateDtlRecs":boolean,
      /**  Flag to indicate that all container receipt details will be "received" automatically.  */  
   "ReceiveAll":boolean,
      /**  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  */  
   "TestImportFields":boolean,
      /**  Descriptive text identifying the Container Class  */  
   "ContainerClassDescription":string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   "DechargePortPortID":string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   "DechargePortDescription":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   "LoadPortPortID":string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   "LoadPortDescription":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Contact name.  */  
   "VendCntName":string,
      /**  Contact email address.  */  
   "VendCntEmailAddress":string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   "VendCntPhoneNum":string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   "VendCntFaxNum":string,
      /**  Second address line of the Supplier  */  
   "VendorAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorZIP":string,
      /**  First address line of the Supplier  */  
   "VendorAddress1":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorDefaultFOB":string,
      /**  City portion of the address of the Supplier  */  
   "VendorCity":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorTermsCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerHeaderRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Date the container is to ship.  */  
   "ShipDate":string,
      /**  Logical indicating if the container has shipped.  */  
   "Shipped":boolean,
      /**  Class of this container.  Must be a valid entry in the ContainerClass master file.  */  
   "ContainerClass":string,
      /**  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "ContainerCost":number,
      /**   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  */  
   "ShippingDays":number,
      /**  Notes/comments about the container shipment.  */  
   "ContainerComments":string,
      /**  Free form text that describes this particular container.  */  
   "ContainerDescription":string,
      /**  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  */  
   "NewPoRelAtReceipt":boolean,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   "Volume":number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  */  
   "VolumeUOM":string,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   "CostPerVolume":number,
      /**  The container reference is typically the shipping company's assigned container ID.  */  
   "ContainerReference":string,
      /**  Reference information for landed cost.  */  
   "LCReference":string,
      /**  Landed Cost Comments  */  
   "LCComment":string,
      /**  This field holds the variance amount for the landed costs.  */  
   "LCVariance":number,
      /**  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  */  
   "LCDisburseMethod":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Currency Date  */  
   "CurrencyDate":string,
      /**  Total cost to ship this container in the doc currency.  */  
   "DocContainerCost":number,
      /**  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  */  
   "PORelShipOption":string,
      /**  Reporting currency value of this field  */  
   "Rpt1ContainerCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ContainerCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ContainerCost":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   "LoadPortID":string,
      /**  Valid port location where goods are unloaded.  */  
   "DechargePortID":string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   "ShipViaCode":string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   "FOB":string,
      /**  Number of Containers in this shipment.  */  
   "ContainerCount":number,
      /**  Number of Packages in this shipment.  */  
   "PackageCount":number,
      /**  Total Weight of the shipment.  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   "WeightUOM":string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  This key links the record to the Vendor file.  */  
   "VendorNum":number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   "ConNum":number,
      /**  Bill of Lading Number  */  
   "BOLading":string,
      /**  Bill of Exchange Number  */  
   "BOExchange":string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   "ShipStatus":string,
      /**  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  */  
   "PORelRcptOption":string,
      /**  Stores the number of the import document.  */  
   "ImportNum":string,
      /**  Name of the vessel containing the shipment.  */  
   "Vessel":string,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   "SpecDutyAmt":number,
      /**  The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   "AppliedLCAmt":number,
      /**  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "ContainerDutyAmt":number,
      /**  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "ContainerIndCost":number,
      /**  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  */  
   "ApplyToLC":boolean,
      /**  The date the container shipment arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  The date the container shipment is received. Defaults as current system date.  */  
   "ReceivedDate":string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   "PurPoint":string,
      /**  The total Landed Cost Amount received for this container shipment.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "UpliftIndCost":number,
      /**  The date that the Container Shipment is due to arrive.  */  
   "DueDate":string,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Stores the Country from which the document is imported.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  */  
   "ImportedFromDesc":string,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  **NOT USED - REMOVE**  */  
   "AdditionalShippingDays":number,
      /**  **NOT USED - Remove **  */  
   "EstimatedArrivalDate":string,
      /**  Set from the earliest need by date set against the po releases.  */  
   "NeedByDate":string,
      /**  Specifies the date on which the supplier has promised to deliver the container.  */  
   "PromiseDate":string,
      /**  Reflects whether taxes have been calculated  */  
   "TaxesCalculated":boolean,
      /**  Internal usage for inclusive taxes -The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   "InAppliedLCAmt":number,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   "InAppliedLCVariance":number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment.  */  
   "InAppliedRcptLCAmt":number,
      /**  Internal usage for inclusive taxes - Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "InContainerCost":number,
      /**  Internal usage for inclusive taxes - This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "InContainerDutyAmt":number,
      /**  Internal usage for inclusive taxes - This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "InContainerIndCost":number,
      /**  Internal usage for inclusive taxes - Total cost to ship this container in the doc currency.  */  
   "InDocContainerCost":number,
      /**  ** NOT USED TO BE DROPPED 10.2 **  */  
   "InLCAppliedAmt":number,
      /**  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  */  
   "InLCVariance":number,
      /**  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   "InSpecDutyAmt":number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   "InUpliftIndCost":number,
      /**  ContainerID in display format.  */  
   "DisplayContainerID":string,
      /**  Display Receipt Status  */  
   "DispRcptStatus":string,
      /**  Display Ship Status.  */  
   "DispShipStatus":string,
      /**   Flag poplulated from XbSyst.ReceiptTaxCalculate 
Determines if taxes can be calculated at update or via action menu  */  
   "EnableCalcTaxes":boolean,
      /**  Flag to indicate if record can be updated after Receipt.  */  
   "EnableLCAfterRcpt":boolean,
      /**  Flag to indicate if container details can be split into another container shipment.  */  
   "EnableSplitContainer":boolean,
      /**  Flag to indicate if indirect costs can be transferred into another container shipment.  */  
   "EnableTransferCost":boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   "EnableUplift":boolean,
      /**  Logical used to indicate if all po rels for the current plant have been received.  */  
   "eshReceived":boolean,
      /**  Landed Cost account for display  */  
   "LCAccount":string,
      /**  Account Description  */  
   "LCAccountDesc":string,
      /**  Amount of Landed Cost applied  */  
   "LCAppliedAmt":number,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  */  
   "LCMessage":string,
      /**  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  */  
   "PartialReceipt":boolean,
      /**  Flag to indicate that all container receipt details will be "received" automatically.  */  
   "ReceiveAll":boolean,
      /**  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  */  
   "ResetPORelDates":boolean,
   "SkipLandedCost":boolean,
      /**  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  */  
   "TestImportFields":boolean,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   "TotalAmt":number,
      /**  Total shipment value  */  
   "TotalExtCost":number,
      /**  Total weight of the items shipped on the container detail.  */  
   "TotalWeight":number,
      /**  Total Deductable Tax Amount  */  
   "TotDedTaxAmt":number,
      /**  Total duties amount.  */  
   "TotDutiesAmt":number,
      /**  Total Indirect Costs amount.  */  
   "TotIndirectCostsAmt":number,
      /**  Total amount for all Container Lines  */  
   "TotLinesAmt":number,
      /**  Total Self Assessed Tax Amount  */  
   "TotSATaxAmt":number,
      /**  Total Tax amount.  */  
   "TotTaxAmt":number,
      /**  Total WithHolding Tax Amount  */  
   "TotWHTaxAmt":number,
      /**  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  */  
   "UpdateDtlRecs":boolean,
   "UpdIndCosts":boolean,
      /**  Flag to indicate if record can be updated.  */  
   "AllowUpdate":boolean,
      /**   Flag poplulated from XbSyst.APTaxLnLevel.  
Determines if taxes are calculated at line level (true) or document level (false)  */  
   "EnableTaxAtLineLevel":boolean,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Determine if the Apply Landed Cost button in Kinetic should be disabled.  */  
   "DisableApplyLandedCost":boolean,
      /**  Flag to determine for Kinetic if use can leave the Container Header record/screen.  */  
   "OkToLeaveContainerHead":boolean,
   "BitFlag":number,
   "ContainerClassDescription":string,
   "DechargePortDescription":string,
   "DechargePortPortID":string,
   "FOBDescription":string,
   "LoadPortPortID":string,
   "LoadPortDescription":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "VendCntPhoneNum":string,
   "VendCntName":string,
   "VendCntFaxNum":string,
   "VendCntEmailAddress":string,
   "VendorCountry":string,
   "VendorState":string,
   "VendorZIP":string,
   "VendorCity":string,
   "VendorVendorID":string,
   "VendorTermsCode":string,
   "VendorName":string,
   "VendorAddress3":string,
   "VendorDefaultFOB":string,
   "VendorAddress1":string,
   "VendorCurrencyCode":string,
   "VendorAddress2":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerHeaderTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who created this record  */  
   "CreatedBy":string,
      /**  Date and time when this record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Date and time when the record was last changed.  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution Date  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  TextCode  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  flag to indicate if this record is used only to total detail records,  */  
   "SummaryOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "EnableSuperGRate":boolean,
   "Rpt1ScrDedTaxAmt":number,
      /**  Display field for Rpt1ScrFixedAmount  */  
   "Rpt1ScrFixedAmount":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
      /**  Display field for Rpt2FixedAmount  */  
   "Rpt2ScrFixedAmount":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
      /**  Display field for Rpt3rFixedAmount  */  
   "Rpt3ScrFixedAmount":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrDocDedTaxAmt":number,
      /**  Doc Fixed Amount  */  
   "ScrDocFixedAmount":number,
   "ScrDocReportableAmt":number,
   "ScrDocTaxableAmt":number,
   "ScrDocTaxAmt":number,
   "ScrDocTaxAmtVar":number,
      /**  FixedAmount  */  
   "ScrFixedAmount":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerMiscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Unique Number automatically assigned within the ContainerID to uniquely identify each Indirect Costs for this container shipment.  */  
   "MiscSeq":number,
      /**  Miscellaneous Charge ID that is flagged for Landed Cost  */  
   "MiscCode":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Invoice Number from corresponding APInvMsc record.  */  
   "InvoiceNum":string,
      /**  Invoice Line from corresponding APInvMsc record.  */  
   "InvoiceLine":number,
      /**  The unique sequence number identifying the AP invoice miscellaneous charge.  */  
   "MscNum":number,
      /**  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  */  
   "ExcludeFromLC":boolean,
      /**  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  */  
   "IncTransValue":boolean,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   "LCDisburseMethod":string,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available.  */  
   "EstimateAmt":number,
      /**  Estimated Amount in currency specified.  */  
   "DocEstimateAmt":number,
      /**  Actual Amount coming from the posted AP invoice miscellaneous charge.  */  
   "ActualAmt":number,
      /**  Actual Amount in currency specified.  */  
   "DocActualAmt":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Container Indirect Cost Comments  */  
   "CommentText":string,
      /**  Reporting currency value of the Estimated Amount.  */  
   "Rpt1EstimateAmt":number,
      /**  Reporting currency value of the Estimated Amount.  */  
   "Rpt2EstimateAmt":number,
      /**  Reporting currency value of the Estimated Amount.  */  
   "Rpt3EstimateAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt1ActualAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt2ActualAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt3ActualAmt":number,
      /**  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  */  
   "ApplyDate":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Historical Doc Estimate Amount  */  
   "DocHstEstimateAmt":number,
      /**  Historical Estimate Amount  */  
   "HstEstimateAmt":number,
      /**  Historical Rpt1 Estimate Amount  */  
   "Rpt1HstEstimateAmt":number,
      /**  Historical Rpt2 Estimate Amount  */  
   "Rpt2HstEstimateAmt":number,
      /**  Historical Rpt3 Estimate Amount  */  
   "Rpt3HstEstimateAmt":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  Indicates the Tax Category for this Indirect Cost. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**  Indicates if the Indirect Cost is Taxable  */  
   "Taxable":boolean,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   "NoTaxRecalc":boolean,
      /**  The Tax Liability for this Receipt  */  
   "TaxRegionCode":string,
      /**  Internal usage for inclusive taxes - Estimated Amount used in landed cost calculation if actual amount is not available.  */  
   "InEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Estimated Amount in currency specified.  */  
   "DocInEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   "Rpt1InEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   "Rpt2InEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   "Rpt3InEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Historical Estimate Amount  */  
   "InHstEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Historical Doc Estimate Amount  */  
   "DocInHstEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Historical Rpt1 Estimate Amount  */  
   "Rpt1InHstEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Historical Rpt2 Estimate Amount  */  
   "Rpt2InHstEstimateAmt":number,
      /**  Internal usage for inclusive taxes - Historical Rpt3 Estimate Amount  */  
   "Rpt3InHstEstimateAmt":number,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Flag to indicate if record can be updated.  */  
   "AllowUpdate":boolean,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   "BaseCurrSymbol":string,
      /**  Total dedicated Tax amount.  */  
   "TotDedTaxAmt":number,
      /**  Total Self Assessed Tax amount  */  
   "TotSATaxAmt":number,
      /**  Total tax amount  */  
   "TotTaxAmt":number,
      /**  Exchange rate that will be used for this indirect cost.  */  
   "ExchangeRate":number,
      /**  Label for ExchangeRate  */  
   "RateLabel":string,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  */  
   "ScrEstimateAmt":number,
      /**  Reporting currency value of the Estimated Amount - Screen Value  */  
   "Rpt1ScrEstimateAmt":number,
      /**  Reporting currency value of the Estimated Amount - Screen value  */  
   "Rpt2ScrEstimateAmt":number,
      /**  Reporting currency value of the Estimated Amount - Screen value  */  
   "Rpt3ScrEstimateAmt":number,
      /**  Historical Estimate Amount - Screen value  */  
   "ScrHstEstimateAmt":number,
      /**  Historical Rpt1 Estimate Amount - Screen value  */  
   "Rpt1ScrHstEstimateAmt":number,
      /**  Historical Rpt2 Estimate Amount - Screen value  */  
   "Rpt2ScrHstEstimateAmt":number,
      /**  Historical Rpt3 Estimate Amount - Screen value  */  
   "Rpt3ScrHstEstimateAmt":number,
      /**  Estimated Amount in currency specified - Screen value  */  
   "DocScrEstimateAmt":number,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  */  
   "DocScrHstEstimateAmt":number,
   "BitFlag":number,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrDesc":string,
   "PurMiscLCAmount":number,
   "PurMiscLCCurrencyCode":string,
   "PurMiscDescription":string,
   "PurMiscLCDisburseMethod":string,
   "RateGrpDescription":string,
   "TaxCatIDDescription":string,
   "TaxRegionCodeDescription":string,
   "VendorCurrencyCode":string,
   "VendorDefaultFOB":string,
   "VendorAddress3":string,
   "VendorState":string,
   "VendorCity":string,
   "VendorVendorID":string,
   "VendorTermsCode":string,
   "VendorName":string,
   "VendorAddress2":string,
   "VendorAddress1":string,
   "VendorZIP":string,
   "VendorCountry":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerMiscTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  */  
   "MiscSeq":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   "MiscCode":string,
      /**  ReportableAmt  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who created this record  */  
   "CreatedBy":string,
      /**  Date and time when this record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Date and time when the record was last changed.  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DocScrDedTaxAmt":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "Rpt1ScrFixedAmount":number,
   "Rpt2ScrFixedAmount":number,
   "Rpt3ScrFixedAmount":number,
   "DocScrFixedAmount":number,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "BitFlag":number,
   "ContainerMiscApplyDate":string,
   "ContainerMiscInPrice":boolean,
   "ContainerMiscCurrencyCode":string,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
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
export interface CalcDtlExtTransValue_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface CalcDtlExtTransValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param containerID
      @param calledFromUI
      @param refreshTableSet
      @param ds
   */  
export interface CalculateContainerTaxes_input{
   containerID:number,
   calledFromUI:boolean,
   refreshTableSet:boolean,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface CalculateContainerTaxes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipShipQty
      @param ipShipQtyUOM
      @param ds
   */  
export interface CalculateDetailExtValues_input{
      /**  Proposed ContainerDetail ContainerShipQty  */  
   ipShipQty:number,
      /**  Proposed ContainerDetail ShipQtyUOm  */  
   ipShipQtyUOM:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface CalculateDetailExtValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param shipQty
      @param shipUOM
      @param partNum
      @param ourUnitCost
      @param poNum
      @param poLine
   */  
export interface CalculateExtCostAndWeight_input{
   shipQty:number,
   shipUOM:string,
   partNum:string,
   ourUnitCost:number,
   poNum:number,
   poLine:number,
}

export interface CalculateExtCostAndWeight_output{
parameters : {
      /**  output parameters  */  
   weight:number,
   grossWeight:number,
   vExtCost:number,
}
}

   /** Required : 
      @param ipContainerID
   */  
export interface CheckContainerBeforeShipping_input{
   ipContainerID:number,
}

export interface CheckContainerBeforeShipping_output{
}

   /** Required : 
      @param ds
      @param ds1
   */  
export interface CreateContainerIndCost_input{
   ds:Erp_Tablesets_APInvMiscChargesTableset[],
   ds1:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface CreateContainerIndCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvMiscChargesTableset,
   ds1:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CreateMultiDetails_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface CreateMultiDetails_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
   containerErrors:string,
   detailAdded:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultContainerCost_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface DefaultContainerCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultCostPerVolume_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface DefaultCostPerVolume_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param containerID
   */  
export interface DeleteByID_input{
   containerID:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipContainerID
   */  
export interface DisburseLandedCosts_input{
   ipContainerID:number,
}

export interface DisburseLandedCosts_output{
parameters : {
      /**  output parameters  */  
   opLCApplied:number,
}
}

export interface Erp_Tablesets_APInvMiscChargesTableset{
   APInvMsc:Erp_Tablesets_APInvMscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APInvMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   InvoiceNum:string,
      /**  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  */  
   InvoiceLine:number,
      /**  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  */  
   MscNum:number,
      /**  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  */  
   Description:string,
      /**  miscellaneous amount.  */  
   MiscAmt:number,
      /**  miscellaneous amount in the vendor currency.  */  
   DocMiscAmt:number,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   PONum:number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  */  
   POLine:number,
      /**  Sequence number of the Miscellaneous Charge  */  
   SeqNum:number,
      /**   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  */  
   TaxCatID:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceLine:number,
      /**  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  */  
   GlbMscNum:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  Reference to the APInvExp record that contains the gl distribution for this charge.  */  
   InvExpSeq:number,
      /**  Indicates if the AP Miscellaneous Charge is for Landed Cost.  */  
   LCFlag:boolean,
      /**  The Container Shipment ID (also known as the ContainerID).  */  
   ContainerID:number,
      /**  The Vendors purchase point ID of the associated receipt's indirect cost.  */  
   PurPoint:string,
      /**  Vendors Packing Slip # of the associated receipt's indirect cost.  */  
   PackSlip:string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  */  
   LCVendorNum:number,
      /**  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   LCDisburseMethod:string,
      /**  miscellaneous amount including taxes.  */  
   InMiscAmt:number,
      /**  miscellaneous amount in the vendor currency including taxes.  */  
   DocInMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InMiscAmt:number,
      /**  Reserved for Development - Integer  */  
   DevInt1:number,
      /**  Reserved for Development - Integer  */  
   DevInt2:number,
      /**  Reserved for development - decimal  */  
   DevDec1:number,
      /**  Reserved for development - decimal  */  
   DevDec2:number,
      /**  Reserved for development - decimal  */  
   DevDec3:number,
      /**  Reserved for development - decimal  */  
   DevDec4:number,
      /**  Reserved for development  - logical  */  
   DevLog1:boolean,
      /**  Reserved for development - logical  */  
   DevLog2:boolean,
      /**  Reserved for development  - character  */  
   DevChar1:string,
      /**  Reserved for development - character  */  
   DevChar2:string,
      /**  Reserved for development - date  */  
   DevDate1:string,
      /**  Reserved for development - date  */  
   DevDate2:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  NoTaxRecalc  */  
   NoTaxRecalc:boolean,
      /**  Code1099ID  */  
   Code1099ID:string,
      /**  FormTypeID  */  
   FormTypeID:string,
      /**  Gen1099Code  */  
   Gen1099Code:string,
      /**  TaxExemptReasonCode  */  
   TaxExemptReasonCode:string,
      /**  The Plastic Packaging Tax Report ID.  */  
   PlasticPackTaxReportID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DebitMemo:boolean,
   DocScrTotalDedTax:number,
   DocScrTotalSATax:number,
   DocScrTotalTax:number,
   GroupID:string,
   InPrice:boolean,
   LCEnabled:boolean,
   Posted:boolean,
   RecordSource:string,
   Rpt1ScrMiscAmt:number,
   Rpt1ScrTotalDedTax:number,
   Rpt1ScrTotalSATax:number,
   Rpt1ScrTotalTax:number,
   Rpt2ScrMiscAmt:number,
   Rpt2ScrTotalDedTax:number,
   Rpt2ScrTotalSATax:number,
   Rpt2ScrTotalTax:number,
   Rpt3ScrMiscAmt:number,
   Rpt3ScrTotalDedTax:number,
   Rpt3ScrTotalSATax:number,
   Rpt3ScrTotalTax:number,
   ScrDocMiscAmt:number,
   ScrMiscAmt:number,
   ScrTotalDedTax:number,
   ScrTotalSATax:number,
   ScrTotalTax:number,
   Selected:boolean,
   BaseCurrSymbol:string,
   BitFlag:number,
   InvoiceNumDescription:string,
   MiscCodeLCCurrencyCode:string,
   MiscCodeLCDisburseMethod:string,
   MiscCodeDescription:string,
   MiscCodeLCAmount:number,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   POLinePartNum:string,
   TaxCatIDDescription:string,
   VendorNumAddress3:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumTermsCode:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorNumVendorID:string,
   VendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerDetailAttchRow{
   Company:string,
   ContainerID:number,
   PONum:number,
   POLine:number,
   PORelNum:number,
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

export interface Erp_Tablesets_ContainerDetailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  The quantity of the PO Release that is shipped on this container.  */  
   ContainerShipQty:number,
      /**  UOM of Shipment Quantity.  */  
   ShipQtyUOm:string,
      /**  Free form text describing the container detail.  */  
   Comment:string,
      /**  Purchase order number that uniquely identifies the purchase order on this container.  */  
   PONum:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  */  
   PORelNum:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Amount of space consumed in the container by this detail line, often specified in cubic square feet.  */  
   Volume:number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   VolumeUOM:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCAmt:number,
      /**  Nett Weight  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   NetWeightUOM:string,
      /**  Unit cost based on our unit of measure.  */  
   OurUnitCost:number,
      /**  Unit cost based on our unit of measure in document currency.  */  
   DocOurUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1OurUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2OurUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3OurUnitCost:number,
      /**  Country Number of the Origin Country from the PO?s Supplier Purchase Point.  */  
   OrigCountryNum:number,
      /**  Container shipment line reference or name.  */  
   ContainerLineRef:string,
      /**  Arrived Quantity as reported in the receipt line.  */  
   ArrivedQty:number,
      /**  Unit of Measure of the Arrived Qty.  */  
   ArrivedQtyUOM:string,
      /**  Received Quantity as reported in the receipt line.  */  
   ReceivedQty:number,
      /**  Unit of Measure of the Received Qty  */  
   ReceivedQtyUOM:string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   ShipStatus:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCDutyAmt:number,
      /**  The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCIndCost:number,
      /**  This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   POTransValue:number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   ExtTransValue:number,
      /**  The date the container shipment detail is received. Defaults as current system date.  */  
   ReceivedDate:string,
      /**  Harmonized System (HS) goods classification code.  */  
   CommodityCode:string,
      /**  The date the container shipment detail arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCSpecLineDutyAmt:number,
      /**  The total Landed Cost Amount received for this container shipment line.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.NetWeightUOM is not known.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  Indicates if the Receipt line is Taxable  */  
   Taxable:boolean,
      /**  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  */  
   TaxExempt:string,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment line.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   InExtTransValue:number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCAmt:number,
      /**  Internal usage for inclusive taxes - The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCIndCost:number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line.The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCSpecLineDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCUpliftIndCost:number,
      /**  Internal usage for inclusive taxes -This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   InPOTransValue:number,
      /**  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  */  
   NoTaxRecalc:boolean,
   BaseWeight:number,
   BaseWeightUOM:string,
      /**  Logical used by row rules to determine whether or not the container detail line is read only.  */  
   ContainerShipped:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   EnableTransValue:boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   EnableUplift:boolean,
      /**  Extended container detail unit cost  */  
   ExtCost:number,
   IUM:string,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   ManualLC:boolean,
      /**  Indicates if the PO release tied to this detail entry is open or closed.  */  
   OpenPoRelease:boolean,
   PartNum:string,
   PlantName:string,
   PoLineDesc:string,
      /**  Quantity already received on this PO Release  */  
   PORelRcvdQty:number,
      /**  Remaining Qty  */  
   PORelRemQty:number,
   PUM:string,
      /**  Container Detail Shipped Date  */  
   ShipDate:string,
   SupplierPartNum:string,
      /**  The Tax Liability for the associated purchase order.  */  
   TaxRegionCode:string,
      /**  Full description of Tax Region.  */  
   TaxRegionDescription:string,
   ThisTranQty:number,
   ThisTranUOM:string,
      /**  Total dedicated Tax amount  */  
   TotDedTaxAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount.  This is the sum of ContainerDetailTax.TaxAmt.  */  
   TotTaxAmt:number,
      /**  Logical indicates to the UI when a key field has been changed.  Set this to yes if this is the row you want the UI to find and display.  */  
   UpdatedKeyRow:boolean,
      /**  Logical indicating that a valid po number, po line and po release has been entered and the user may not update the other container detail values.  */  
   ValidPOInfoEntered:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
   BaseVolume:number,
   BaseVolumeUOM:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Optional field that contains our revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
   BitFlag:number,
   CommodityDescription:string,
   ContainerHeaderContainerDescription:string,
   ContainerHeaderShipDate:string,
   CountryNumDescription:string,
   POHeaderInPrice:boolean,
   PORelBTOOrderNum:number,
   PORelBTOOrderLine:number,
   PORelRefCodeDesc:string,
   PORelPurchasingFactor:number,
   PORelXRelQty:number,
   PORelOpenRelease:boolean,
   PORelRelQty:number,
   PORelNeedByDate:string,
   PORelBTOOrderRelNum:number,
   PORelPromiseDt:string,
   PORelPurchasingFactorDirection:string,
   PORelArrivedQty:number,
   PORelDueDate:string,
   PORelPlant:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerDetailTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time when the record was last changed.  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrSymbol:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   EnableSuperGRate:string,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrFixedAmount:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrFixedAmount:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrFixedAmount:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   DocScrDedTaxAmt:number,
   DocScrFixedAmount:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerDetailToSplitRow{
   CommCodeDesc:string,
   ContainerID:number,
   ContainerLineRef:string,
   CountryDesc:string,
   PartNum:string,
   POLine:number,
   PONum:number,
   PORelNum:number,
   POTransValue:number,
   Selected:boolean,
   UpliftPercent:number,
   Volume:number,
   Weight:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerDetailToSplitTableset{
   ContainerDetailToSplit:Erp_Tablesets_ContainerDetailToSplitRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ContainerDutyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Purchase order number that uniquely identifies the purchase order on this container.  */  
   PONum:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  */  
   PORelNum:number,
      /**  Unique Number automatically assigned which is used along with ContainerID, PONum, POLine and PORelNum to uniquely identify the Duty record within the Container Shipment Line.  */  
   DutySeq:number,
      /**  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  */  
   TariffCode:string,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  */  
   DutyAmt:number,
      /**  Container Duty Comments  */  
   CommentText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  InDutyAmt  */  
   InDutyAmt:number,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount - Screen Value  */  
   ScrDutyAmt:number,
   BitFlag:number,
   POHeaderTaxRegionCode:string,
   POHeaderInPrice:boolean,
   TariffDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerHeaderAttchRow{
   Company:string,
   ContainerID:number,
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

export interface Erp_Tablesets_ContainerHeaderListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Date the container is to ship.  */  
   ShipDate:string,
      /**  Logical indicating if the container has shipped.  */  
   Shipped:boolean,
      /**  Class of this container.  Must be a valid entry in the ContainerClass master file.  */  
   ContainerClass:string,
      /**  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerCost:number,
      /**   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  */  
   ShippingDays:number,
      /**  Notes/comments about the container shipment.  */  
   ContainerComments:string,
      /**  Free form text that describes this particular container.  */  
   ContainerDescription:string,
      /**  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  */  
   NewPoRelAtReceipt:boolean,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  */  
   VolumeUOM:string,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   CostPerVolume:number,
      /**  The container reference is typically the shipping company's assigned container ID.  */  
   ContainerReference:string,
      /**  Reference information for landed cost.  */  
   LCReference:string,
      /**  Landed Cost Comments  */  
   LCComment:string,
      /**  This field holds the variance amount for the landed costs.  */  
   LCVariance:number,
      /**  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  */  
   LCDisburseMethod:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Currency Date  */  
   CurrencyDate:string,
      /**  Total cost to ship this container in the doc currency.  */  
   DocContainerCost:number,
      /**  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  */  
   PORelShipOption:string,
      /**  Reporting currency value of this field  */  
   Rpt1ContainerCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ContainerCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ContainerCost:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   LoadPortID:string,
      /**  Valid port location where goods are unloaded.  */  
   DechargePortID:string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   ShipViaCode:string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   FOB:string,
      /**  Number of Containers in this shipment.  */  
   ContainerCount:number,
      /**  Number of Packages in this shipment.  */  
   PackageCount:number,
      /**  Total Weight of the shipment.  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Bill of Lading Number  */  
   BOLading:string,
      /**  Bill of Exchange Number  */  
   BOExchange:string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   ShipStatus:string,
      /**  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  */  
   PORelRcptOption:string,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Name of the vessel containing the shipment.  */  
   Vessel:string,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   SpecDutyAmt:number,
      /**  The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   AppliedLCAmt:number,
      /**  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerDutyAmt:number,
      /**  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerIndCost:number,
      /**  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  */  
   ApplyToLC:boolean,
      /**  The date the container shipment arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  The date the container shipment is received. Defaults as current system date.  */  
   ReceivedDate:string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  The total Landed Cost Amount received for this container shipment.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   UpliftIndCost:number,
      /**  The date that the Container Shipment is due to arrive.  */  
   DueDate:string,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Stores the Country from which the document is imported.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  */  
   ImportedFromDesc:string,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ContainerID in display format.  */  
   DisplayContainerID:string,
      /**  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  */  
   ResetPORelDates:boolean,
      /**  Logical used to indicate if all po rels for the current plant have been received.  */  
   eshReceived:boolean,
      /**  Total shipment value  */  
   TotalExtCost:number,
      /**  Total weight of the items shipped on the container detail.  */  
   TotalWeight:number,
      /**  Amount of Landed Cost applied  */  
   LCAppliedAmt:number,
      /**  Landed Cost account for display  */  
   LCAccount:string,
      /**  Account Description  */  
   LCAccountDesc:string,
   SkipLandedCost:boolean,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  */  
   LCMessage:string,
      /**  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  */  
   PartialReceipt:boolean,
      /**  Display Ship Status.  */  
   DispShipStatus:string,
      /**  Display Receipt Status  */  
   DispRcptStatus:string,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   EnableUplift:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
      /**  Flag to indicate if record can be updated after Receipt.  */  
   EnableLCAfterRcpt:boolean,
      /**  Flag to indicate if container details can be split into another container shipment.  */  
   EnableSplitContainer:boolean,
      /**  Flag to indicate if indirect costs can be transferred into another container shipment.  */  
   EnableTransferCost:boolean,
      /**  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  */  
   UpdateDtlRecs:boolean,
      /**  Flag to indicate that all container receipt details will be "received" automatically.  */  
   ReceiveAll:boolean,
      /**  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  */  
   TestImportFields:boolean,
      /**  Descriptive text identifying the Container Class  */  
   ContainerClassDescription:string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   DechargePortPortID:string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   DechargePortDescription:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   LoadPortPortID:string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   LoadPortDescription:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Contact name.  */  
   VendCntName:string,
      /**  Contact email address.  */  
   VendCntEmailAddress:string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   VendCntPhoneNum:string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   VendCntFaxNum:string,
      /**  Second address line of the Supplier  */  
   VendorAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorCurrencyCode:string,
      /**  Can be blank.  */  
   VendorState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorZIP:string,
      /**  First address line of the Supplier  */  
   VendorAddress1:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorDefaultFOB:string,
      /**  City portion of the address of the Supplier  */  
   VendorCity:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorTermsCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerHeaderListTableset{
   ContainerHeaderList:Erp_Tablesets_ContainerHeaderListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ContainerHeaderRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Date the container is to ship.  */  
   ShipDate:string,
      /**  Logical indicating if the container has shipped.  */  
   Shipped:boolean,
      /**  Class of this container.  Must be a valid entry in the ContainerClass master file.  */  
   ContainerClass:string,
      /**  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerCost:number,
      /**   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  */  
   ShippingDays:number,
      /**  Notes/comments about the container shipment.  */  
   ContainerComments:string,
      /**  Free form text that describes this particular container.  */  
   ContainerDescription:string,
      /**  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  */  
   NewPoRelAtReceipt:boolean,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  */  
   VolumeUOM:string,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   CostPerVolume:number,
      /**  The container reference is typically the shipping company's assigned container ID.  */  
   ContainerReference:string,
      /**  Reference information for landed cost.  */  
   LCReference:string,
      /**  Landed Cost Comments  */  
   LCComment:string,
      /**  This field holds the variance amount for the landed costs.  */  
   LCVariance:number,
      /**  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  */  
   LCDisburseMethod:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Currency Date  */  
   CurrencyDate:string,
      /**  Total cost to ship this container in the doc currency.  */  
   DocContainerCost:number,
      /**  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  */  
   PORelShipOption:string,
      /**  Reporting currency value of this field  */  
   Rpt1ContainerCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ContainerCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ContainerCost:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   LoadPortID:string,
      /**  Valid port location where goods are unloaded.  */  
   DechargePortID:string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   ShipViaCode:string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   FOB:string,
      /**  Number of Containers in this shipment.  */  
   ContainerCount:number,
      /**  Number of Packages in this shipment.  */  
   PackageCount:number,
      /**  Total Weight of the shipment.  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Bill of Lading Number  */  
   BOLading:string,
      /**  Bill of Exchange Number  */  
   BOExchange:string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   ShipStatus:string,
      /**  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  */  
   PORelRcptOption:string,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Name of the vessel containing the shipment.  */  
   Vessel:string,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   SpecDutyAmt:number,
      /**  The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   AppliedLCAmt:number,
      /**  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerDutyAmt:number,
      /**  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerIndCost:number,
      /**  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  */  
   ApplyToLC:boolean,
      /**  The date the container shipment arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  The date the container shipment is received. Defaults as current system date.  */  
   ReceivedDate:string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  The total Landed Cost Amount received for this container shipment.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   UpliftIndCost:number,
      /**  The date that the Container Shipment is due to arrive.  */  
   DueDate:string,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Stores the Country from which the document is imported.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  */  
   ImportedFromDesc:string,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  **NOT USED - REMOVE**  */  
   AdditionalShippingDays:number,
      /**  **NOT USED - Remove **  */  
   EstimatedArrivalDate:string,
      /**  Set from the earliest need by date set against the po releases.  */  
   NeedByDate:string,
      /**  Specifies the date on which the supplier has promised to deliver the container.  */  
   PromiseDate:string,
      /**  Reflects whether taxes have been calculated  */  
   TaxesCalculated:boolean,
      /**  Internal usage for inclusive taxes -The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   InAppliedLCAmt:number,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InContainerCost:number,
      /**  Internal usage for inclusive taxes - This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InContainerDutyAmt:number,
      /**  Internal usage for inclusive taxes - This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InContainerIndCost:number,
      /**  Internal usage for inclusive taxes - Total cost to ship this container in the doc currency.  */  
   InDocContainerCost:number,
      /**  ** NOT USED TO BE DROPPED 10.2 **  */  
   InLCAppliedAmt:number,
      /**  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  */  
   InLCVariance:number,
      /**  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   InSpecDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InUpliftIndCost:number,
      /**  ContainerID in display format.  */  
   DisplayContainerID:string,
      /**  Display Receipt Status  */  
   DispRcptStatus:string,
      /**  Display Ship Status.  */  
   DispShipStatus:string,
      /**   Flag poplulated from XbSyst.ReceiptTaxCalculate 
Determines if taxes can be calculated at update or via action menu  */  
   EnableCalcTaxes:boolean,
      /**  Flag to indicate if record can be updated after Receipt.  */  
   EnableLCAfterRcpt:boolean,
      /**  Flag to indicate if container details can be split into another container shipment.  */  
   EnableSplitContainer:boolean,
      /**  Flag to indicate if indirect costs can be transferred into another container shipment.  */  
   EnableTransferCost:boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   EnableUplift:boolean,
      /**  Logical used to indicate if all po rels for the current plant have been received.  */  
   eshReceived:boolean,
      /**  Landed Cost account for display  */  
   LCAccount:string,
      /**  Account Description  */  
   LCAccountDesc:string,
      /**  Amount of Landed Cost applied  */  
   LCAppliedAmt:number,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  */  
   LCMessage:string,
      /**  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  */  
   PartialReceipt:boolean,
      /**  Flag to indicate that all container receipt details will be "received" automatically.  */  
   ReceiveAll:boolean,
      /**  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  */  
   ResetPORelDates:boolean,
   SkipLandedCost:boolean,
      /**  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  */  
   TestImportFields:boolean,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   TotalAmt:number,
      /**  Total shipment value  */  
   TotalExtCost:number,
      /**  Total weight of the items shipped on the container detail.  */  
   TotalWeight:number,
      /**  Total Deductable Tax Amount  */  
   TotDedTaxAmt:number,
      /**  Total duties amount.  */  
   TotDutiesAmt:number,
      /**  Total Indirect Costs amount.  */  
   TotIndirectCostsAmt:number,
      /**  Total amount for all Container Lines  */  
   TotLinesAmt:number,
      /**  Total Self Assessed Tax Amount  */  
   TotSATaxAmt:number,
      /**  Total Tax amount.  */  
   TotTaxAmt:number,
      /**  Total WithHolding Tax Amount  */  
   TotWHTaxAmt:number,
      /**  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  */  
   UpdateDtlRecs:boolean,
   UpdIndCosts:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
      /**   Flag poplulated from XbSyst.APTaxLnLevel.  
Determines if taxes are calculated at line level (true) or document level (false)  */  
   EnableTaxAtLineLevel:boolean,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Determine if the Apply Landed Cost button in Kinetic should be disabled.  */  
   DisableApplyLandedCost:boolean,
      /**  Flag to determine for Kinetic if use can leave the Container Header record/screen.  */  
   OkToLeaveContainerHead:boolean,
   BitFlag:number,
   ContainerClassDescription:string,
   DechargePortDescription:string,
   DechargePortPortID:string,
   FOBDescription:string,
   LoadPortPortID:string,
   LoadPortDescription:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   VendCntPhoneNum:string,
   VendCntName:string,
   VendCntFaxNum:string,
   VendCntEmailAddress:string,
   VendorCountry:string,
   VendorState:string,
   VendorZIP:string,
   VendorCity:string,
   VendorVendorID:string,
   VendorTermsCode:string,
   VendorName:string,
   VendorAddress3:string,
   VendorDefaultFOB:string,
   VendorAddress1:string,
   VendorCurrencyCode:string,
   VendorAddress2:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerHeaderTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time when the record was last changed.  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution Date  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  TextCode  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  flag to indicate if this record is used only to total detail records,  */  
   SummaryOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   EnableSuperGRate:boolean,
   Rpt1ScrDedTaxAmt:number,
      /**  Display field for Rpt1ScrFixedAmount  */  
   Rpt1ScrFixedAmount:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
      /**  Display field for Rpt2FixedAmount  */  
   Rpt2ScrFixedAmount:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
      /**  Display field for Rpt3rFixedAmount  */  
   Rpt3ScrFixedAmount:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrDocDedTaxAmt:number,
      /**  Doc Fixed Amount  */  
   ScrDocFixedAmount:number,
   ScrDocReportableAmt:number,
   ScrDocTaxableAmt:number,
   ScrDocTaxAmt:number,
   ScrDocTaxAmtVar:number,
      /**  FixedAmount  */  
   ScrFixedAmount:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Unique Number automatically assigned within the ContainerID to uniquely identify each Indirect Costs for this container shipment.  */  
   MiscSeq:number,
      /**  Miscellaneous Charge ID that is flagged for Landed Cost  */  
   MiscCode:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvMsc record.  */  
   InvoiceNum:string,
      /**  Invoice Line from corresponding APInvMsc record.  */  
   InvoiceLine:number,
      /**  The unique sequence number identifying the AP invoice miscellaneous charge.  */  
   MscNum:number,
      /**  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  */  
   ExcludeFromLC:boolean,
      /**  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  */  
   IncTransValue:boolean,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   LCDisburseMethod:string,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available.  */  
   EstimateAmt:number,
      /**  Estimated Amount in currency specified.  */  
   DocEstimateAmt:number,
      /**  Actual Amount coming from the posted AP invoice miscellaneous charge.  */  
   ActualAmt:number,
      /**  Actual Amount in currency specified.  */  
   DocActualAmt:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Container Indirect Cost Comments  */  
   CommentText:string,
      /**  Reporting currency value of the Estimated Amount.  */  
   Rpt1EstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount.  */  
   Rpt2EstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount.  */  
   Rpt3EstimateAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt1ActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt2ActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt3ActualAmt:number,
      /**  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  */  
   ApplyDate:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Historical Doc Estimate Amount  */  
   DocHstEstimateAmt:number,
      /**  Historical Estimate Amount  */  
   HstEstimateAmt:number,
      /**  Historical Rpt1 Estimate Amount  */  
   Rpt1HstEstimateAmt:number,
      /**  Historical Rpt2 Estimate Amount  */  
   Rpt2HstEstimateAmt:number,
      /**  Historical Rpt3 Estimate Amount  */  
   Rpt3HstEstimateAmt:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  Indicates the Tax Category for this Indirect Cost. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  Indicates if the Indirect Cost is Taxable  */  
   Taxable:boolean,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   NoTaxRecalc:boolean,
      /**  The Tax Liability for this Receipt  */  
   TaxRegionCode:string,
      /**  Internal usage for inclusive taxes - Estimated Amount used in landed cost calculation if actual amount is not available.  */  
   InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Estimated Amount in currency specified.  */  
   DocInEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   Rpt1InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   Rpt2InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   Rpt3InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Estimate Amount  */  
   InHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Doc Estimate Amount  */  
   DocInHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Rpt1 Estimate Amount  */  
   Rpt1InHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Rpt2 Estimate Amount  */  
   Rpt2InHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Rpt3 Estimate Amount  */  
   Rpt3InHstEstimateAmt:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   BaseCurrSymbol:string,
      /**  Total dedicated Tax amount.  */  
   TotDedTaxAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount  */  
   TotTaxAmt:number,
      /**  Exchange rate that will be used for this indirect cost.  */  
   ExchangeRate:number,
      /**  Label for ExchangeRate  */  
   RateLabel:string,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  */  
   ScrEstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount - Screen Value  */  
   Rpt1ScrEstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount - Screen value  */  
   Rpt2ScrEstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount - Screen value  */  
   Rpt3ScrEstimateAmt:number,
      /**  Historical Estimate Amount - Screen value  */  
   ScrHstEstimateAmt:number,
      /**  Historical Rpt1 Estimate Amount - Screen value  */  
   Rpt1ScrHstEstimateAmt:number,
      /**  Historical Rpt2 Estimate Amount - Screen value  */  
   Rpt2ScrHstEstimateAmt:number,
      /**  Historical Rpt3 Estimate Amount - Screen value  */  
   Rpt3ScrHstEstimateAmt:number,
      /**  Estimated Amount in currency specified - Screen value  */  
   DocScrEstimateAmt:number,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  */  
   DocScrHstEstimateAmt:number,
   BitFlag:number,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   PurMiscLCAmount:number,
   PurMiscLCCurrencyCode:string,
   PurMiscDescription:string,
   PurMiscLCDisburseMethod:string,
   RateGrpDescription:string,
   TaxCatIDDescription:string,
   TaxRegionCodeDescription:string,
   VendorCurrencyCode:string,
   VendorDefaultFOB:string,
   VendorAddress3:string,
   VendorState:string,
   VendorCity:string,
   VendorVendorID:string,
   VendorTermsCode:string,
   VendorName:string,
   VendorAddress2:string,
   VendorAddress1:string,
   VendorZIP:string,
   VendorCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerMiscTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  */  
   MiscSeq:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   MiscCode:string,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time when the record was last changed.  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   Rpt1ScrFixedAmount:number,
   Rpt2ScrFixedAmount:number,
   Rpt3ScrFixedAmount:number,
   DocScrFixedAmount:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   BitFlag:number,
   ContainerMiscApplyDate:string,
   ContainerMiscInPrice:boolean,
   ContainerMiscCurrencyCode:string,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerMiscToTransferRow{
   ContainerID:number,
   DocActualAmt:number,
   DocEstimateAmt:number,
   EstimateAmt:number,
   InvoiceLine:number,
   InvoiceNum:string,
   LCDisburseMethod:string,
   MiscSeq:number,
   MscNum:number,
   Selected:boolean,
   MiscCodeDesc:string,
   CurrencyCode:string,
   Type:string,
   Percentage:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerMiscToTransferTableset{
   ContainerMiscToTransfer:Erp_Tablesets_ContainerMiscToTransferRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ContainerTrackingTableset{
   ContainerHeader:Erp_Tablesets_ContainerHeaderRow[],
   ContainerHeaderAttch:Erp_Tablesets_ContainerHeaderAttchRow[],
   ContainerDetail:Erp_Tablesets_ContainerDetailRow[],
   ContainerDetailAttch:Erp_Tablesets_ContainerDetailAttchRow[],
   ContainerDetailTax:Erp_Tablesets_ContainerDetailTaxRow[],
   ContainerDuty:Erp_Tablesets_ContainerDutyRow[],
   ContainerHeaderTax:Erp_Tablesets_ContainerHeaderTaxRow[],
   ContainerMisc:Erp_Tablesets_ContainerMiscRow[],
   ContainerMiscTax:Erp_Tablesets_ContainerMiscTaxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtContainerTrackingTableset{
   ContainerHeader:Erp_Tablesets_ContainerHeaderRow[],
   ContainerHeaderAttch:Erp_Tablesets_ContainerHeaderAttchRow[],
   ContainerDetail:Erp_Tablesets_ContainerDetailRow[],
   ContainerDetailAttch:Erp_Tablesets_ContainerDetailAttchRow[],
   ContainerDetailTax:Erp_Tablesets_ContainerDetailTaxRow[],
   ContainerDuty:Erp_Tablesets_ContainerDutyRow[],
   ContainerHeaderTax:Erp_Tablesets_ContainerHeaderTaxRow[],
   ContainerMisc:Erp_Tablesets_ContainerMiscRow[],
   ContainerMiscTax:Erp_Tablesets_ContainerMiscTaxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipContainerID
   */  
export interface GetAPInvMiscCharges_input{
      /**  Container ID  */  
   ipContainerID:number,
}

export interface GetAPInvMiscCharges_output{
   returnObj:Erp_Tablesets_APInvMiscChargesTableset[],
}

   /** Required : 
      @param containerID
   */  
export interface GetByID_input{
   containerID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ContainerTrackingTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ContainerTrackingTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ContainerTrackingTableset[],
}

   /** Required : 
      @param cclass
   */  
export interface GetContainerClassInfo_input{
      /**  cclass  */  
   cclass:string,
}

export interface GetContainerClassInfo_output{
parameters : {
      /**  output parameters  */  
   volume:number,
   containerCost:number,
   CostPerVolume:number,
   shippingDays:number,
   validContainer:boolean,
}
}

   /** Required : 
      @param ipContainerID
   */  
export interface GetContainerDetailToSplit_input{
      /**  Container ID  */  
   ipContainerID:number,
}

export interface GetContainerDetailToSplit_output{
   returnObj:Erp_Tablesets_ContainerDetailToSplitTableset[],
}

   /** Required : 
      @param ipContainerID
   */  
export interface GetContainerMiscToTransfer_input{
      /**  Container ID  */  
   ipContainerID:number,
}

export interface GetContainerMiscToTransfer_output{
   returnObj:Erp_Tablesets_ContainerMiscToTransferTableset[],
}

   /** Required : 
      @param ds
      @param poLine
      @param poNum
   */  
export interface GetDtlPOInfo_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
      /**  Receipt Line to check  */  
   poLine:number,
      /**  New PO Number  */  
   poNum:number,
}

export interface GetDtlPOInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param poNum
      @param poLine
      @param ds
   */  
export interface GetDtlPOLineInfo_input{
      /**  New POLine Number  */  
   poNum:number,
      /**  Receipt Line to check  */  
   poLine:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface GetDtlPOLineInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
      @param poRelNum
      @param inputShipQty
      @param inputIUM
      @param whichField
   */  
export interface GetDtlQtyInfo_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
      /**  Container PO Number  */  
   poNum:number,
      /**  Container PO Line  */  
   poLine:number,
      /**  Container PO Rel  */  
   poRelNum:number,
      /**  Proposed change to the Ship qty field  */  
   inputShipQty:number,
      /**  Proposed change to the IUM field  */  
   inputIUM:string,
      /**  Indicates either 'QTY' or 'UOM' field changed  */  
   whichField:string,
}

export interface GetDtlQtyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
   warnMsg:string,
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
   returnObj:Erp_Tablesets_ContainerHeaderListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param containerID
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface GetNewContainerDetailAttch_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface GetNewContainerDetailAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param containerID
      @param poNum
      @param poLine
      @param poRelNum
      @param taxCode
      @param rateCode
   */  
export interface GetNewContainerDetailTax_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
   poNum:number,
   poLine:number,
   poRelNum:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewContainerDetailTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param containerID
      @param poNum
      @param poLine
   */  
export interface GetNewContainerDetail_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
   poNum:number,
   poLine:number,
}

export interface GetNewContainerDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param containerID
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface GetNewContainerDuty_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface GetNewContainerDuty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param containerID
   */  
export interface GetNewContainerHeaderAttch_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
}

export interface GetNewContainerHeaderAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param containerID
      @param taxCode
      @param rateCode
   */  
export interface GetNewContainerHeaderTax_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewContainerHeaderTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewContainerHeader_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface GetNewContainerHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param containerID
      @param miscSeq
      @param taxCode
      @param rateCode
   */  
export interface GetNewContainerMiscTax_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
   miscSeq:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewContainerMiscTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
      @param containerID
   */  
export interface GetNewContainerMisc_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
   containerID:number,
}

export interface GetNewContainerMisc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param porelnum
      @param ds
   */  
export interface GetPOReleaseInfo_input{
      /**  pore num  */  
   porelnum:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface GetPOReleaseInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param whereClauseContainerHeader
      @param whereClauseContainerHeaderAttch
      @param whereClauseContainerDetail
      @param whereClauseContainerDetailAttch
      @param whereClauseContainerDetailTax
      @param whereClauseContainerDuty
      @param whereClauseContainerHeaderTax
      @param whereClauseContainerMisc
      @param whereClauseContainerMiscTax
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseContainerHeader:string,
   whereClauseContainerHeaderAttch:string,
   whereClauseContainerDetail:string,
   whereClauseContainerDetailAttch:string,
   whereClauseContainerDetailTax:string,
   whereClauseContainerDuty:string,
   whereClauseContainerHeaderTax:string,
   whereClauseContainerMisc:string,
   whereClauseContainerMiscTax:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ContainerTrackingTableset[],
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
      @param ipClassCode
      @param ds
   */  
export interface OnChangeClassCode_input{
      /**  Proposed Container Class Code to be validated  */  
   ipClassCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeClassCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipConNum
      @param ds
   */  
export interface OnChangeConNum_input{
      /**  Proposed ConNum to be validated  */  
   ipConNum:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipClassCode
      @param ds
   */  
export interface OnChangeContainerClass_input{
      /**  Proposed Container Class Code to be validated  */  
   ipClassCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeContainerClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipLCIndCost
      @param ds
   */  
export interface OnChangeContainerDetailLCIndCost_input{
      /**  Proposed LCIndCost  */  
   ipLCIndCost:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeContainerDetailLCIndCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedFixedAmt
      @param ds
   */  
export interface OnChangeDetailTaxFixedAmount_input{
      /**  The proposed reportable amount  */  
   proposedFixedAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedRateCode
      @param ds
   */  
export interface OnChangeDetailTaxRateCode_input{
      /**  The proposed rate code  */  
   proposedRateCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedReportableAmt
      @param ds
   */  
export interface OnChangeDetailTaxReportableAmt_input{
      /**  The proposed reportable amount  */  
   proposedReportableAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxAmt
      @param ds
   */  
export interface OnChangeDetailTaxTaxAmt_input{
      /**  The proposed tax amount  */  
   proposedTaxAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxCode
      @param ds
   */  
export interface OnChangeDetailTaxTaxCode_input{
      /**  The proposed tax code  */  
   proposedTaxCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxDeductable
      @param ds
   */  
export interface OnChangeDetailTaxTaxDeductable_input{
      /**  The proposed tax deductable  */  
   proposedTaxDeductable:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxTaxDeductable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxPercent
      @param ds
   */  
export interface OnChangeDetailTaxTaxPercent_input{
      /**  The proposed tax percent  */  
   proposedTaxPercent:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxableAmt
      @param ds
   */  
export interface OnChangeDetailTaxTaxableAmt_input{
      /**  The proposed taxable amount  */  
   proposedTaxableAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDetailTaxTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipCommCode
      @param ds
   */  
export interface OnChangeDtlCommodity_input{
      /**  Proposed Commodity Code to be validated  */  
   ipCommCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDtlCommodity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipCountryNum
      @param ds
   */  
export interface OnChangeDtlCountryNum_input{
      /**  Proposed Country of Origin to be validated  */  
   ipCountryNum:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDtlCountryNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipLCIndCost
      @param LCIndCostSum
      @param ds
   */  
export interface OnChangeDtlLCIndCost_input{
      /**  Proposed LC Indirect Cose to be validated  */  
   ipLCIndCost:number,
      /**  Total amount of Indirect cost on all the lines  */  
   LCIndCostSum:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDtlLCIndCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param taxCatID
      @param ds
   */  
export interface OnChangeDtlTaxCatID_input{
      /**  Tax Category  */  
   taxCatID:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDtlTaxCatID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param taxExempt
      @param ds
   */  
export interface OnChangeDtlTaxExempt_input{
      /**  Tax Exempt  */  
   taxExempt:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDtlTaxExempt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipUpliftPercent
      @param ds
   */  
export interface OnChangeDtlUpliftPercent_input{
      /**  Proposed Uplift Percentage to be validated  */  
   ipUpliftPercent:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDtlUpliftPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipDueDate
      @param ds
   */  
export interface OnChangeDueDate_input{
      /**  Proposed Container Due Date to be validated  */  
   ipDueDate:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDueDate_output{
parameters : {
      /**  output parameters  */  
   opErrorMessage:string,
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipTariffCode
      @param ds
   */  
export interface OnChangeDutyTariffCode_input{
      /**  Proposed Tariff Code to be validated  */  
   ipTariffCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeDutyTariffCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipLoadPortID
      @param ds
   */  
export interface OnChangeLoadPort_input{
      /**  Loading Port ID  */  
   ipLoadPortID:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeLoadPort_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipApplyDate
      @param ds
   */  
export interface OnChangeMiscApplyDate_input{
      /**  Proposed Apply Date to be validated  */  
   ipApplyDate:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipChargeID
      @param ds
   */  
export interface OnChangeMiscCharge_input{
      /**  Proposed PurMisc ID to be validated  */  
   ipChargeID:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscCharge_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipCurrCode
      @param ds
   */  
export interface OnChangeMiscCurrencyCode_input{
      /**  Proposed Currency Code to be validated  */  
   ipCurrCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipDocEstimateAmt
      @param ds
   */  
export interface OnChangeMiscDocEstimateAmt_input{
      /**  Proposed Estimate Amount in document currency  */  
   ipDocEstimateAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscDocEstimateAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipExchangeRate
      @param ds
   */  
export interface OnChangeMiscExchangeRate_input{
      /**  Proposed Currency Exchange Rate to be validated  */  
   ipExchangeRate:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipInvLine
      @param ds
   */  
export interface OnChangeMiscInvoiceLine_input{
      /**  The AP Invoice Line to be validated  */  
   ipInvLine:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipInvNum
      @param ipVendorNum
      @param ds
   */  
export interface OnChangeMiscInvoiceNum_input{
      /**  The AP Invoice Number to be validated  */  
   ipInvNum:string,
      /**  The Vendor Number associated with the invoice  */  
   ipVendorNum:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipMscNum
      @param ds
   */  
export interface OnChangeMiscMscNum_input{
      /**  The AP Invoice Line Miscellaneous Sequence Number to be validated  */  
   ipMscNum:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscMscNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param percentage
      @param ds
   */  
export interface OnChangeMiscPercentage_input{
      /**  Percentage Amount  */  
   percentage:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscPercentage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipRateGrpCode
      @param ds
   */  
export interface OnChangeMiscRateGrp_input{
      /**  Proposed Currency Rate Group Code to be validated  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param taxCatID
      @param ds
   */  
export interface OnChangeMiscTaxCatID_input{
   taxCatID:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxCatID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedFixedAmt
      @param ds
   */  
export interface OnChangeMiscTaxFixedAmount_input{
      /**  The proposed reportable amount  */  
   proposedFixedAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedRateCode
      @param ds
   */  
export interface OnChangeMiscTaxRateCode_input{
      /**  The proposed rate code  */  
   proposedRateCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param taxRegionCode
      @param ds
   */  
export interface OnChangeMiscTaxRegionCode_input{
   taxRegionCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxRegionCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedReportableAmt
      @param ds
   */  
export interface OnChangeMiscTaxReportableAmt_input{
      /**  The proposed reportable amount  */  
   proposedReportableAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxAmt
      @param ds
   */  
export interface OnChangeMiscTaxTaxAmt_input{
      /**  The proposed tax amount  */  
   proposedTaxAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxCode
      @param ds
   */  
export interface OnChangeMiscTaxTaxCode_input{
      /**  The proposed tax code  */  
   proposedTaxCode:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxDeductable
      @param ds
   */  
export interface OnChangeMiscTaxTaxDeductable_input{
      /**  The proposed tax deductable  */  
   proposedTaxDeductable:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxTaxDeductable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxPercent
      @param ds
   */  
export interface OnChangeMiscTaxTaxPercent_input{
      /**  The proposed tax percent  */  
   proposedTaxPercent:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param proposedTaxableAmt
      @param ds
   */  
export interface OnChangeMiscTaxTaxableAmt_input{
      /**  The proposed taxable amount  */  
   proposedTaxableAmt:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscTaxTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param VendID
      @param ds
   */  
export interface OnChangeMiscVendor_input{
      /**  Proposed vendor ID to be validated  */  
   VendID:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeMiscVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipShipDate
      @param ds
   */  
export interface OnChangeShipDate_input{
      /**  Proposed Container Class Code to be validated  */  
   ipShipDate:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeShipDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipShipStat
      @param ds
   */  
export interface OnChangeShipStatus_input{
      /**  Proposed Shipment Status to be validated  */  
   ipShipStat:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeShipStatus_output{
parameters : {
      /**  output parameters  */  
   opShipLogic:string,
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipShippingDays
      @param ds
   */  
export interface OnChangeShippingDays_input{
      /**  Proposed Container Class Code to be validated  */  
   ipShippingDays:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeShippingDays_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param VendID
      @param ds
   */  
export interface OnChangeVendor_input{
      /**  Proposed vendor ID to be validated  */  
   VendID:string,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedDetailTaxManual_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangedDetailTaxManual_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedMiscTaxManual_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangedMiscTaxManual_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedPOTransValue_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface OnChangedPOTransValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipChargeID
   */  
export interface OnUpdateMiscCharge_input{
      /**  Proposed PurMisc ID to be validated  */  
   ipChargeID:string,
}

export interface OnUpdateMiscCharge_output{
}

   /** Required : 
      @param ds
   */  
export interface PreUpdateContainer_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface PreUpdateContainer_output{
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
   opShipmentClassMsg:string,
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param inContainerID
   */  
export interface ReceiveContainerLCAmt_input{
   inContainerID:number,
}

export interface ReceiveContainerLCAmt_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipContainerID
   */  
export interface RefreshLCApplied_input{
   ipContainerID:number,
}

export interface RefreshLCApplied_output{
parameters : {
      /**  output parameters  */  
   opLCApplied:number,
}
}

   /** Required : 
      @param ipContainerID
      @param ipDisburseMethod
   */  
export interface ResetLandedCostDisbursements_input{
      /**  Container ID to reset  */  
   ipContainerID:number,
      /**  Landed Cost Disbursment method  */  
   ipDisburseMethod:string,
}

export interface ResetLandedCostDisbursements_output{
}

   /** Required : 
      @param containerToShip
   */  
export interface ShipContainer_input{
      /**  container To Ship  */  
   containerToShip:number,
}

export interface ShipContainer_output{
}

   /** Required : 
      @param ds
   */  
export interface SplitContainerShipment_input{
   ds:Erp_Tablesets_ContainerDetailToSplitTableset[],
}

export interface SplitContainerShipment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerDetailToSplitTableset,
   opContainerID:number,
}
}

   /** Required : 
      @param ipTargetContainerID
      @param ds
   */  
export interface TransferIndirectCosts_input{
      /**  Target Container ID  */  
   ipTargetContainerID:number,
   ds:Erp_Tablesets_ContainerMiscToTransferTableset[],
}

export interface TransferIndirectCosts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerMiscToTransferTableset,
}
}

   /** Required : 
      @param containerToUnShip
   */  
export interface UnShipContainer_input{
      /**  container To UnShip  */  
   containerToUnShip:number,
}

export interface UnShipContainer_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtContainerTrackingTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtContainerTrackingTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param origLCAmt
      @param newLCAmt
      @param ipcontainerID
      @param ipAppliedAmt
   */  
export interface UpdateLCAppliedAmt_input{
   origLCAmt:number,
   newLCAmt:number,
   ipcontainerID:number,
   ipAppliedAmt:number,
}

export interface UpdateLCAppliedAmt_output{
parameters : {
      /**  output parameters  */  
   totApplied:number,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param ipContainerID
      @param ds
   */  
export interface ValidateLandedCostDisbursements_input{
   ipContainerID:number,
   ds:Erp_Tablesets_ContainerTrackingTableset[],
}

export interface ValidateLandedCostDisbursements_output{
parameters : {
      /**  output parameters  */  
   lcError:string,
}
}

   /** Required : 
      @param shipQty
      @param shipUOM
      @param ium
      @param partNum
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface ValidateShipQty_input{
   shipQty:number,
   shipUOM:string,
   ium:string,
   partNum:string,
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface ValidateShipQty_output{
parameters : {
      /**  output parameters  */  
   WarningMsg:string,
}
}

