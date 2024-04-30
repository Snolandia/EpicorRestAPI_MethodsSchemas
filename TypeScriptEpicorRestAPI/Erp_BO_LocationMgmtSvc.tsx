import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.LocationMgmtSvc
// Description: class LocationMgmtSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/$metadata", {
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
   Description: Get LocationMgmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationMgmts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryRow
   */  
export function get_LocationMgmts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationMgmts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationInventoryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LocationInventoryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LocationMgmts(requestBody:Erp_Tablesets_LocationInventoryRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LocationMgmt item
   Description: Calls GetByID to retrieve the LocationMgmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationMgmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationInventoryRow
   */  
export function get_LocationMgmts_Company_LocationNum(Company:string, LocationNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationInventoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")", {
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
         resolve(data as Erp_Tablesets_LocationInventoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LocationMgmt for the service
   Description: Calls UpdateExt to update LocationMgmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationMgmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationInventoryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LocationMgmts_Company_LocationNum(Company:string, LocationNum:string, requestBody:Erp_Tablesets_LocationInventoryRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")", {
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
   Summary: Call UpdateExt to delete LocationMgmt item
   Description: Call UpdateExt to delete LocationMgmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationMgmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LocationMgmts_Company_LocationNum(Company:string, LocationNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")", {
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
   Description: Get LocationInventoryAddresses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationInventoryAddresses1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryAddressRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationInventoryAddresses(Company:string, LocationNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryAddressRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationInventoryAddresses", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryAddressRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LocationInventoryAddress item
   Description: Calls GetByID to retrieve the LocationInventoryAddress item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationInventoryAddress1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param AddressType Desc: AddressType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationInventoryAddresses_Company_LocationNum_AddressType(Company:string, LocationNum:string, AddressType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationInventoryAddressRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")", {
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
         resolve(data as Erp_Tablesets_LocationInventoryAddressRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LocationMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationMtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationMtlRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationMtls(Company:string, LocationNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationMtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LocationMtl item
   Description: Calls GetByID to retrieve the LocationMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationMtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationMtlRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company:string, LocationNum:string, JobNum:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_LocationMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LocationTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationTrans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationTranRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationTrans(Company:string, LocationNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LocationTran item
   Description: Calls GetByID to retrieve the LocationTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationTran1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param LocationSeqNum Desc: LocationSeqNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationTranRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationTrans_Company_LocationNum_LocationSeqNum(Company:string, LocationNum:string, LocationSeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")", {
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
         resolve(data as Erp_Tablesets_LocationTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LocationWarrantyTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationWarrantyTrans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationWarrantyTranRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationWarrantyTrans(Company:string, LocationNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationWarrantyTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationWarrantyTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationWarrantyTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LocationWarrantyTran item
   Description: Calls GetByID to retrieve the LocationWarrantyTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationWarrantyTran1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param WarrantySeqNum Desc: WarrantySeqNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   */  
export function get_LocationMgmts_Company_LocationNum_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company:string, LocationNum:string, WarrantySeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationWarrantyTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")", {
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
         resolve(data as Erp_Tablesets_LocationWarrantyTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LocationInventoryAddresses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationInventoryAddresses
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryAddressRow
   */  
export function get_LocationInventoryAddresses(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryAddressRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryAddressRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationInventoryAddresses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LocationInventoryAddresses(requestBody:Erp_Tablesets_LocationInventoryAddressRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LocationInventoryAddress item
   Description: Calls GetByID to retrieve the LocationInventoryAddress item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationInventoryAddress
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param AddressType Desc: AddressType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   */  
export function get_LocationInventoryAddresses_Company_LocationNum_AddressType(Company:string, LocationNum:string, AddressType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationInventoryAddressRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")", {
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
         resolve(data as Erp_Tablesets_LocationInventoryAddressRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LocationInventoryAddress for the service
   Description: Calls UpdateExt to update LocationInventoryAddress. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationInventoryAddress
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param AddressType Desc: AddressType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LocationInventoryAddresses_Company_LocationNum_AddressType(Company:string, LocationNum:string, AddressType:string, requestBody:Erp_Tablesets_LocationInventoryAddressRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")", {
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
   Summary: Call UpdateExt to delete LocationInventoryAddress item
   Description: Call UpdateExt to delete LocationInventoryAddress item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationInventoryAddress
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param AddressType Desc: AddressType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LocationInventoryAddresses_Company_LocationNum_AddressType(Company:string, LocationNum:string, AddressType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")", {
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
   Description: Get LocationMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationMtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationMtlRow
   */  
export function get_LocationMtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationMtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LocationMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LocationMtls(requestBody:Erp_Tablesets_LocationMtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LocationMtl item
   Description: Calls GetByID to retrieve the LocationMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationMtlRow
   */  
export function get_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company:string, LocationNum:string, JobNum:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_LocationMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LocationMtl for the service
   Description: Calls UpdateExt to update LocationMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company:string, LocationNum:string, JobNum:string, AssemblySeq:string, MtlSeq:string, requestBody:Erp_Tablesets_LocationMtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
   Summary: Call UpdateExt to delete LocationMtl item
   Description: Call UpdateExt to delete LocationMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company:string, LocationNum:string, JobNum:string, AssemblySeq:string, MtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
   Description: Get LocationTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationTranRow
   */  
export function get_LocationTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LocationTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LocationTrans(requestBody:Erp_Tablesets_LocationTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LocationTran item
   Description: Calls GetByID to retrieve the LocationTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param LocationSeqNum Desc: LocationSeqNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationTranRow
   */  
export function get_LocationTrans_Company_LocationNum_LocationSeqNum(Company:string, LocationNum:string, LocationSeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")", {
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
         resolve(data as Erp_Tablesets_LocationTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LocationTran for the service
   Description: Calls UpdateExt to update LocationTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param LocationSeqNum Desc: LocationSeqNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LocationTrans_Company_LocationNum_LocationSeqNum(Company:string, LocationNum:string, LocationSeqNum:string, requestBody:Erp_Tablesets_LocationTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")", {
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
   Summary: Call UpdateExt to delete LocationTran item
   Description: Call UpdateExt to delete LocationTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param LocationSeqNum Desc: LocationSeqNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LocationTrans_Company_LocationNum_LocationSeqNum(Company:string, LocationNum:string, LocationSeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")", {
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
   Description: Get LocationWarrantyTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationWarrantyTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationWarrantyTranRow
   */  
export function get_LocationWarrantyTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationWarrantyTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationWarrantyTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationWarrantyTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LocationWarrantyTrans(requestBody:Erp_Tablesets_LocationWarrantyTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LocationWarrantyTran item
   Description: Calls GetByID to retrieve the LocationWarrantyTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationWarrantyTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param WarrantySeqNum Desc: WarrantySeqNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   */  
export function get_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company:string, LocationNum:string, WarrantySeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LocationWarrantyTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")", {
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
         resolve(data as Erp_Tablesets_LocationWarrantyTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LocationWarrantyTran for the service
   Description: Calls UpdateExt to update LocationWarrantyTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationWarrantyTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param WarrantySeqNum Desc: WarrantySeqNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company:string, LocationNum:string, WarrantySeqNum:string, requestBody:Erp_Tablesets_LocationWarrantyTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")", {
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
   Summary: Call UpdateExt to delete LocationWarrantyTran item
   Description: Call UpdateExt to delete LocationWarrantyTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationWarrantyTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocationNum Desc: LocationNum   Required: True   Allow empty value : True
      @param WarrantySeqNum Desc: WarrantySeqNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company:string, LocationNum:string, WarrantySeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryListRow)
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
export function get_GetRows(whereClauseLocationInventory:string, whereClauseLocationInventoryAddress:string, whereClauseLocationMtl:string, whereClauseLocationTran:string, whereClauseLocationWarrantyTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLocationInventory!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocationInventory=" + whereClauseLocationInventory
   }
   if(typeof whereClauseLocationInventoryAddress!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocationInventoryAddress=" + whereClauseLocationInventoryAddress
   }
   if(typeof whereClauseLocationMtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocationMtl=" + whereClauseLocationMtl
   }
   if(typeof whereClauseLocationTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocationTran=" + whereClauseLocationTran
   }
   if(typeof whereClauseLocationWarrantyTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocationWarrantyTran=" + whereClauseLocationWarrantyTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetRows" + params, {
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
export function get_GetByID(locationNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof locationNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "locationNum=" + locationNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetList" + params, {
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
   Summary: Invoke method ChangedLocationWarrantyTranPartNum
   Description: Called when the Part is changed
   OperationID: ChangedLocationWarrantyTranPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedLocationWarrantyTranPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedLocationWarrantyTranPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedLocationWarrantyTranPartNum(requestBody:ChangedLocationWarrantyTranPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedLocationWarrantyTranPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ChangedLocationWarrantyTranPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedLocationWarrantyTranPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrentAddress
   Description: Returns the address of the requested type: L=Location, O=Owner, S=Sold To
   OperationID: GetCurrentAddress
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCurrentAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentAddress(requestBody:GetCurrentAddress_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrentAddress_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetCurrentAddress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCurrentAddress_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCustomerAddress
   Description: Update Order Header information with values from the Sold To when the Sold To is changed.
   OperationID: GetNewCustomerAddress
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCustomerAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustomerAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCustomerAddress(requestBody:GetNewCustomerAddress_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCustomerAddress_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetNewCustomerAddress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCustomerAddress_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOTMFAddress
   Description: Update Order Header information with values from the Sold To when the Sold To is changed.
   OperationID: GetNewOTMFAddress
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOTMFAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOTMFAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOTMFAddress(requestBody:GetNewOTMFAddress_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOTMFAddress_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetNewOTMFAddress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOTMFAddress_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLocationWarrantyTran
   Description: Get Location Warranty Transaction
   OperationID: GetLocationWarrantyTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLocationWarrantyTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLocationWarrantyTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLocationWarrantyTran(requestBody:GetLocationWarrantyTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLocationWarrantyTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetLocationWarrantyTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLocationWarrantyTran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedPartNum
   OperationID: ChangedPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedPartNum(requestBody:ChangedPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ChangedPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedWarrantyCode
   OperationID: ChangedWarrantyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedWarrantyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedWarrantyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedWarrantyCode(requestBody:ChangedWarrantyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedWarrantyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ChangedWarrantyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedWarrantyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCustomer
   OperationID: ValidateCustomer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCustomer(requestBody:ValidateCustomer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCustomer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ValidateCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateCustomer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateShipTo
   OperationID: ValidateShipTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShipTo(requestBody:ValidateShipTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateShipTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ValidateShipTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateShipTo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePartNum
   OperationID: ValidatePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePartNum(requestBody:ValidatePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ValidatePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSerialNumber
   OperationID: ValidateSerialNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialNumber(requestBody:ValidateSerialNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSerialNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ValidateSerialNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSerialNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMaterialOrigSerialNumber
   OperationID: ValidateMaterialOrigSerialNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMaterialOrigSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMaterialOrigSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMaterialOrigSerialNumber(requestBody:ValidateMaterialOrigSerialNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMaterialOrigSerialNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ValidateMaterialOrigSerialNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateMaterialOrigSerialNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMaterialLotNumber
   Description: This method validates Lot number that user can enter in case if multiple lots came up in Original Part search
   OperationID: ValidateMaterialLotNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMaterialLotNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMaterialLotNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMaterialLotNumber(requestBody:ValidateMaterialLotNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMaterialLotNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ValidateMaterialLotNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateMaterialLotNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateIDNumber
   OperationID: ValidateIDNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateIDNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateIDNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateIDNumber(requestBody:ValidateIDNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateIDNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/ValidateIDNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateIDNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLocationInventory
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationInventory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLocationInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLocationInventory(requestBody:GetNewLocationInventory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLocationInventory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetNewLocationInventory", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLocationInventory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLocationInventoryAddress
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationInventoryAddress
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLocationInventoryAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationInventoryAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLocationInventoryAddress(requestBody:GetNewLocationInventoryAddress_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLocationInventoryAddress_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetNewLocationInventoryAddress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLocationInventoryAddress_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLocationMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationMtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLocationMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLocationMtl(requestBody:GetNewLocationMtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLocationMtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetNewLocationMtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLocationMtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLocationTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLocationTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLocationTran(requestBody:GetNewLocationTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLocationTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetNewLocationTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLocationTran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLocationWarrantyTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationWarrantyTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLocationWarrantyTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationWarrantyTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLocationWarrantyTran(requestBody:GetNewLocationWarrantyTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLocationWarrantyTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetNewLocationWarrantyTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLocationWarrantyTran_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryAddressRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LocationInventoryAddressRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LocationInventoryListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LocationInventoryRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationMtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LocationMtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LocationTranRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationWarrantyTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LocationWarrantyTranRow,
}

export interface Erp_Tablesets_LocationInventoryAddressRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Unique ID of parent location  */  
   "LocationNum":number,
      /**  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  */  
   "AddressType":string,
      /**  Unique customer number for this location.  */  
   "CustNum":number,
      /**  Ship To number for this locatoin  */  
   "CustShipToNum":string,
      /**  The first line of the address for this location.  */  
   "Address1":string,
      /**  The second line of the address for this location.  */  
   "Address2":string,
      /**  The third line of the address for this location.  */  
   "Address3":string,
      /**  City portion of the address for this location  */  
   "City":string,
      /**  Contact for this location.  */  
   "Contact":string,
      /**  Country Number for this location.  */  
   "CountryNum":number,
      /**  The email address for this location.  */  
   "EmailAddress":string,
      /**  Fax number for this location  */  
   "FaxNum":string,
      /**  Name for this location.  */  
   "Name":string,
      /**  Phone number for this location.  */  
   "PhoneNum":string,
      /**  State for this location.  */  
   "State":string,
      /**  Zip for this locatoin  */  
   "Zip":string,
      /**  Use OTS  */  
   "UseOTS":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  */  
   "ConNum":number,
   "TranComment":string,
   "BitFlag":number,
   "CountryDescription":string,
   "CustomerECCType":string,
   "CustomerName":string,
   "CustomerCustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LocationInventoryListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique ID for Location Inventory record  */  
   "LocationNum":number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  */  
   "PartNum":string,
      /**  The sales order number that this detail shipment line is linked to.  */  
   "OrderNum":number,
      /**  Line Description  */  
   "LineDesc":string,
      /**  Serial number of part.  */  
   "SerialNumber":string,
      /**  Identification Number (example HIN, VIN).  */  
   "IDNum":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LocationInventoryRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique ID for Location Inventory record  */  
   "LocationNum":number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  */  
   "PartNum":string,
      /**  Site that the shipment is from.  */  
   "Plant":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackLine":number,
      /**  The sales order number that this detail shipment line is linked to.  */  
   "OrderNum":number,
      /**  The sales order line that this shipment detail line is linked to.  M  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to.  */  
   "OrderRelNum":number,
      /**  Job Number that supplied the quantity that was shipped.  */  
   "JobNum":string,
      /**  This is the current owner.  Valid values are (D)istributor, (C)ustomer  */  
   "CurrentOwner":string,
      /**  Order Comment  */  
   "OrderComment":string,
      /**  Line Description  */  
   "LineDesc":string,
      /**  The type of listing the location inventory item is: L=Leaser, S=Sale  */  
   "Listing":string,
      /**  Date when the location inventory was listed.  */  
   "ListingStartDate":string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  */  
   "WarrantyCode":string,
      /**  Warranty Comment  */  
   "WarrantyComment":string,
      /**  Date the warrany started.  */  
   "WarrantyStartDate":string,
      /**  Date the warranty will expired.  */  
   "WarrantyExpirationDate":string,
      /**  Lot Num  */  
   "LotNum":string,
      /**  Serial number of part.  */  
   "SerialNumber":string,
      /**  Identification Number (example HIN, VIN).  */  
   "IDNum":string,
      /**  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  */  
   "WarrantyTransfer":string,
      /**  An optional field that is used if the customer has a different Part number.  */  
   "XPartNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "InventoryAttributeSetID":number,
      /**  Shipping Address  */  
   "AddrList":string,
      /**  Billing Address  */  
   "BillAddr":string,
   "ExtAddress1":string,
   "ExtAddress2":string,
   "ExtAddress3":string,
   "ExtCity":string,
   "ExtContact":string,
   "ExtCountryNum":number,
   "ExtEmailAddress":string,
   "ExtFaxNum":string,
   "ExtName":string,
   "ExtPhoneNum":string,
   "ExtState":string,
   "ExtZIP":string,
   "NewAddrList":string,
   "NewCustID":string,
   "NewCustNum":number,
   "NewShipToNum":string,
   "NewUseOTMF":boolean,
   "TrackIDNum":boolean,
   "TrackSerialNum":boolean,
      /**  Transaction Comment  */  
   "TranComment":string,
      /**  Use OTS  */  
   "UseOTMF":boolean,
   "CustomerCustID":string,
   "ShipToNum":string,
      /**  Sold to address  */  
   "SoldToAddrList":string,
      /**  Owner address.  */  
   "OwnerAddrList":string,
      /**  Location Address.  */  
   "LocationAddrList":string,
      /**  Where is the transfer going to: (N)o Address Change,  (L)ocation, (O)wner, (B)oth.  Blank will be for a warranty change only.  */  
   "TransferAddrType":string,
      /**  Owner Busines Model  */  
   "OwnerBusinessModel":string,
      /**  Location Business Model  */  
   "LocationBusinessModel":string,
      /**  Owner Customer ID  */  
   "OwnerCustID":string,
      /**  Owner Ship To.  */  
   "OwnerShipToNum":string,
      /**  Owner Use One Time Mark For.  */  
   "OwnerUseOTMF":boolean,
      /**  Location Customer ID.  */  
   "LocationCustID":string,
      /**  Location Ship To.  */  
   "LocationShipToNum":string,
      /**  Location Use One Time Mark For.  */  
   "LocationUseOTMF":boolean,
      /**  Sold To Customer ID.  */  
   "SoldToCustID":string,
      /**  Sold To Ship To.  */  
   "SoldToShipToNum":string,
      /**  Sold To Use Ont Time Mark For.  */  
   "SoldToUseOTMF":boolean,
      /**  Sold To Business Model  */  
   "SoldToBusinessModel":string,
      /**  Addres type of owner : L=Locatoin, O=Owner, S=Sold To  */  
   "OwnerAddrType":string,
      /**  Date when transfer occured - writes to LocationTran.EffectiveDate  */  
   "EffectiveDate":string,
   "EnableDynAttrButton":boolean,
      /**  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  */  
   "NewConNum":number,
      /**  External field to hold the name of the selected customer contact for the Location record  */  
   "LocationAttn":string,
      /**  External field to hold the name of the selected customer contact for the selected record  */  
   "NewConName":string,
      /**  External field to hold the name of the selected customer contact for the Owner record  */  
   "OwnerAttn":string,
   "BitFlag":number,
   "FSWarrCdWarrDescription":string,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumAttrClassID":string,
   "PartNumSellingFactor":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LocationMtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   "JobComplete":boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   "IssuedComplete":boolean,
      /**  Job Number.  */  
   "JobNum":string,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   "PartNum":string,
      /**  A description of the material.  */  
   "Description":string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   "QtyPer":number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   "RequiredQty":number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   "IUM":string,
      /**  Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.  When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   "LeadTime":number,
      /**  A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.  It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   "RelatedOperation":number,
      /**  The material burden rate for this Job Material.  */  
   "MtlBurRate":number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstMtlBurUnitCost":number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   "IssuedQty":number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   "TotalCost":number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   "MtlBurCost":number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "ReqDate":string,
      /**  The warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   "SalvagePartNum":string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   "SalvageDescription":string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   "SalvageQtyPer":number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   "SalvageUM":string,
      /**  The salvage material burden rate for this Job Material.  */  
   "SalvageMtlBurRate":number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageUnitCredit":number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageEstMtlBurUnitCredit":number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   "SalvageQtyToDate":number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageCredit":number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageMtlBurCredit":number,
      /**  Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.  */  
   "MfgComment":string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   "VendorNum":number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   "BuyIt":boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   "Ordered":boolean,
      /**  Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.  */  
   "PurComment":string,
      /**  Indicates if this material will be backflushed.  Note: this field is defaulted from Part.BackFlush Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   "BackFlush":boolean,
      /**  Estimated Scrap.  */  
   "EstScrap":number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   "EstScrapType":string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   "FixedQty":boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   "FindNum":string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   "SndAlrtCmpl":boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   "Direct":boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   "MaterialMtlCost":number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialLabCost":number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialSubCost":number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialBurCost":number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageMtlCredit":number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageLbrCredit":number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageBurCredit":number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageSubCredit":number,
      /**  Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler: 'I' to ignore in eScheduler.  */  
   "APSAddResType":string,
      /**  The service call that this Material belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this material relates to.  */  
   "CallLine":number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  FS - Unit Price for the Material in base currency.  */  
   "UnitPrice":number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   "BillableUnitPrice":number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   "DocBillableUnitPrice":number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   "PricePerCode":string,
      /**  Is this a billable material item.  */  
   "Billable":boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   "ShippedQty":number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   "DocUnitPrice":number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   "QtyStagedToDate":number,
      /**  This material was added after initial setup of the job  */  
   "AddedMtl":boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   "MiscCharge":boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   "MiscCode":string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   "SCMiscCode":string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**  RFQ SRFQ Status: W= Waiting, A = Accepted, R = Requested, C = Receivedtatus.  */  
   "RFQStat":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "WIReqDate":string,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.  */  
   "BaseRequiredQty":number,
      /**  Unit of Measure of the JobMtl.BaseRequiredQty.  If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   "BaseUOM":string,
      /**  Material Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   "StagingWarehouseCode":string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   "StagingBinNum":string,
      /**  A non blank character indicates that the release could not be picked by the Auto Pick process. The possible values are: "L" - Order Line can't be shipped complete. "O" - Order can't be shipped complete. "I" - Insufficient quantity reserved"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstMtlUnitCost":number,
      /**  Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstLbrUnitCost":number,
      /**  Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstBurUnitCost":number,
      /**  Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstSubUnitCost":number,
      /**  Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstMtlUnitCredit":number,
      /**  Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstLbrUnitCredit":number,
      /**  Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstBurUnitCredit":number,
      /**  Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstSubUnitCredit":number,
      /**  The material quantity that has been loaned out to another job.  */  
   "LoanedQty":number,
      /**  The material quantity that has been borrowed from another job.  */  
   "BorrowedQty":number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   "ReassignSNAsm":boolean,
      /**  GeneralPlanInfo  */  
   "GeneralPlanInfo":string,
      /**  EstStdDescription  */  
   "EstStdDescription":string,
      /**  PricingUOM  */  
   "PricingUOM":string,
      /**  RemovedFromPlan  */  
   "RemovedFromPlan":boolean,
      /**  IsPOCostingMaintained  */  
   "IsPOCostingMaintained":boolean,
      /**  EstStdType  */  
   "EstStdType":number,
      /**  POCostingFactor  */  
   "POCostingFactor":number,
      /**  PlannedQtyPerUnit  */  
   "PlannedQtyPerUnit":number,
      /**  POCostingDirection  */  
   "POCostingDirection":number,
      /**  POCostingUnitVal  */  
   "POCostingUnitVal":number,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigStructTag":string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigGroupSeq":number,
      /**  ShowStatusIcon  */  
   "ShowStatusIcon":string,
      /**  Contract ID  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   "LinkToContract":boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   "StagingLotNum":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   "LocationView":boolean,
      /**  LotNum  */  
   "LotNum":string,
      /**  SerialNum  */  
   "SerialNum":string,
      /**  WarrantyCode  */  
   "WarrantyCode":string,
      /**  WarrantyComment  */  
   "WarrantyComment":string,
      /**  WarrantyStartDate  */  
   "WarrantyStartDate":string,
      /**  WarrantyExpirationDate  */  
   "WarrantyExpirationDate":string,
      /**  LocationNum  */  
   "LocationNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvageAttributeSetID":number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   "SalvagePlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvagePlanningAttributeSetID":number,
      /**  Dealer specific warranty code.  This is a non ERP warranty code.  */  
   "DealerWarranty":string,
      /**  Dealer specific warranty description  */  
   "DealerWarrantyDesc":string,
      /**  Dealer specifc warranty expiration date.  */  
   "DealerWarrantyExpiration":string,
      /**  Dealer specific warranty start date.  */  
   "DealerWarrantyStart":string,
      /**  Original Serial Number  */  
   "OriginalSerialNum":string,
   "OriginalPartNum":string,
   "BitFlag":number,
   "FSWarrCdWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LocationTranRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Unique ID of Location Inventory  */  
   "LocationNum":number,
      /**  LocationSeqNum  */  
   "LocationSeqNum":number,
      /**  The customer the transfer is for at that time.  */  
   "CustNum":number,
      /**  The current ship to the transfer is for at that time.  */  
   "CustShipToNum":string,
      /**  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  */  
   "AddressType":string,
      /**  The first line of the address for given location type at that time.  */  
   "Address1":string,
      /**  The second line of the address for given location type at that time.  */  
   "Address2":string,
      /**  The third line of the address for given location type at that time.  */  
   "Address3":string,
      /**  City portion of the address for given location type at that time.  */  
   "City":string,
      /**  Contact Name for given location type at that time.  */  
   "Contact":string,
      /**  Country number for the Ship To location for at that time.  */  
   "CountryNum":number,
      /**  The email address for given location type at that time.  */  
   "EmailAddress":string,
      /**  Fax number for given location type at that time.  */  
   "FaxNum":string,
      /**  Name for for given location type at that time.  */  
   "Name":string,
      /**  Phone number for for given location type at that time  */  
   "PhoneNum":string,
      /**  The state or province portion to the location for at that time.  */  
   "State":string,
      /**  The zip or postal code portion to location for at that time.  */  
   "Zip":string,
      /**  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  This columns is nno longer used.  */  
   "WarrantyTransfer":string,
      /**  Date when transfer occurred  */  
   "EffectiveDate":string,
      /**  Comment about the transfer transaction.  */  
   "Comment":string,
      /**  Created On  */  
   "CreatedOn":string,
      /**  Created By  */  
   "CreatedBy":string,
      /**  Warranty Code  */  
   "WarrantyCode":string,
      /**  Warranty Comment  */  
   "WarrantyComment":string,
      /**  Date when the warranty started.  */  
   "WarrantyStartDate":string,
      /**  Date when the warranty expires.  */  
   "WarrantyExpirationDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ShipToAddrList":string,
   "BitFlag":number,
   "CustomerECCType":string,
   "CustomerCustID":string,
   "FSWarrCdWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LocationWarrantyTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  LocationNum  */  
   "LocationNum":number,
      /**  Sequence number.  This is system generated and is not maintainable.  */  
   "WarrantySeqNum":number,
      /**  Finished good Identificaton Number  */  
   "IDNum":string,
      /**  SerialNum  */  
   "SerialNum":string,
      /**  Comment about the warranty transfer transaction.  */  
   "Comment":string,
      /**  Effective Date  */  
   "EffectiveDate":string,
      /**  HDCaseNum  */  
   "HDCaseNum":number,
      /**  ParentPartNum  */  
   "ParentPartNum":string,
      /**  OriginalPartNum  */  
   "OriginalPartNum":string,
      /**  OriginalPartSerialNum  */  
   "OriginalPartSerialNum":string,
      /**  NewPartNum  */  
   "NewPartNum":string,
      /**  NewPartSerialNum  */  
   "NewPartSerialNum":string,
      /**  PartDescription  */  
   "PartDescription":string,
      /**  WarrantyCode  */  
   "WarrantyCode":string,
      /**  WarrantyComment  */  
   "WarrantyComment":string,
      /**  Date when warranty started.  */  
   "WarrantyStartDate":string,
      /**  Date when warranty expires  */  
   "WarrantyExpirationDate":string,
      /**  Dealer Warranty, this is for a non Erp warranty.  */  
   "DealerWarranty":string,
      /**  Dealer warranty description, this is for a non Erp warranty  */  
   "DealerWarrantyDesc":string,
      /**  Date dealer warranty started, this is for a non Erp warranty  */  
   "DealerWarrantyStart":string,
      /**  Date dealer warranty expires, this is for a non Erp warranty.  */  
   "DealerWarrantyExpiration":string,
      /**  WarrantyUsage  */  
   "WarrantyUsage":string,
      /**  LotNum  */  
   "LotNum":string,
      /**  SystemCreated  */  
   "SystemCreated":boolean,
      /**  Created On  */  
   "CreatedOn":string,
      /**  Created By  */  
   "CreatedBy":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "FSWarrCdWarrDescription":string,
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
export interface ChangedLocationWarrantyTranPartNum_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface ChangedLocationWarrantyTranPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedPartNum_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface ChangedPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedWarrantyCode_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface ChangedWarrantyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param locationNum
   */  
export interface DeleteByID_input{
   locationNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_LocationInventoryAddressRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Unique ID of parent location  */  
   LocationNum:number,
      /**  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  */  
   AddressType:string,
      /**  Unique customer number for this location.  */  
   CustNum:number,
      /**  Ship To number for this locatoin  */  
   CustShipToNum:string,
      /**  The first line of the address for this location.  */  
   Address1:string,
      /**  The second line of the address for this location.  */  
   Address2:string,
      /**  The third line of the address for this location.  */  
   Address3:string,
      /**  City portion of the address for this location  */  
   City:string,
      /**  Contact for this location.  */  
   Contact:string,
      /**  Country Number for this location.  */  
   CountryNum:number,
      /**  The email address for this location.  */  
   EmailAddress:string,
      /**  Fax number for this location  */  
   FaxNum:string,
      /**  Name for this location.  */  
   Name:string,
      /**  Phone number for this location.  */  
   PhoneNum:string,
      /**  State for this location.  */  
   State:string,
      /**  Zip for this locatoin  */  
   Zip:string,
      /**  Use OTS  */  
   UseOTS:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  */  
   ConNum:number,
   TranComment:string,
   BitFlag:number,
   CountryDescription:string,
   CustomerECCType:string,
   CustomerName:string,
   CustomerCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LocationInventoryListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique ID for Location Inventory record  */  
   LocationNum:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  */  
   PartNum:string,
      /**  The sales order number that this detail shipment line is linked to.  */  
   OrderNum:number,
      /**  Line Description  */  
   LineDesc:string,
      /**  Serial number of part.  */  
   SerialNumber:string,
      /**  Identification Number (example HIN, VIN).  */  
   IDNum:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LocationInventoryListTableset{
   LocationInventoryList:Erp_Tablesets_LocationInventoryListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LocationInventoryRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique ID for Location Inventory record  */  
   LocationNum:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  */  
   PartNum:string,
      /**  Site that the shipment is from.  */  
   Plant:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackLine:number,
      /**  The sales order number that this detail shipment line is linked to.  */  
   OrderNum:number,
      /**  The sales order line that this shipment detail line is linked to.  M  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to.  */  
   OrderRelNum:number,
      /**  Job Number that supplied the quantity that was shipped.  */  
   JobNum:string,
      /**  This is the current owner.  Valid values are (D)istributor, (C)ustomer  */  
   CurrentOwner:string,
      /**  Order Comment  */  
   OrderComment:string,
      /**  Line Description  */  
   LineDesc:string,
      /**  The type of listing the location inventory item is: L=Leaser, S=Sale  */  
   Listing:string,
      /**  Date when the location inventory was listed.  */  
   ListingStartDate:string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  */  
   WarrantyCode:string,
      /**  Warranty Comment  */  
   WarrantyComment:string,
      /**  Date the warrany started.  */  
   WarrantyStartDate:string,
      /**  Date the warranty will expired.  */  
   WarrantyExpirationDate:string,
      /**  Lot Num  */  
   LotNum:string,
      /**  Serial number of part.  */  
   SerialNumber:string,
      /**  Identification Number (example HIN, VIN).  */  
   IDNum:string,
      /**  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  */  
   WarrantyTransfer:string,
      /**  An optional field that is used if the customer has a different Part number.  */  
   XPartNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   InventoryAttributeSetID:number,
      /**  Shipping Address  */  
   AddrList:string,
      /**  Billing Address  */  
   BillAddr:string,
   ExtAddress1:string,
   ExtAddress2:string,
   ExtAddress3:string,
   ExtCity:string,
   ExtContact:string,
   ExtCountryNum:number,
   ExtEmailAddress:string,
   ExtFaxNum:string,
   ExtName:string,
   ExtPhoneNum:string,
   ExtState:string,
   ExtZIP:string,
   NewAddrList:string,
   NewCustID:string,
   NewCustNum:number,
   NewShipToNum:string,
   NewUseOTMF:boolean,
   TrackIDNum:boolean,
   TrackSerialNum:boolean,
      /**  Transaction Comment  */  
   TranComment:string,
      /**  Use OTS  */  
   UseOTMF:boolean,
   CustomerCustID:string,
   ShipToNum:string,
      /**  Sold to address  */  
   SoldToAddrList:string,
      /**  Owner address.  */  
   OwnerAddrList:string,
      /**  Location Address.  */  
   LocationAddrList:string,
      /**  Where is the transfer going to: (N)o Address Change,  (L)ocation, (O)wner, (B)oth.  Blank will be for a warranty change only.  */  
   TransferAddrType:string,
      /**  Owner Busines Model  */  
   OwnerBusinessModel:string,
      /**  Location Business Model  */  
   LocationBusinessModel:string,
      /**  Owner Customer ID  */  
   OwnerCustID:string,
      /**  Owner Ship To.  */  
   OwnerShipToNum:string,
      /**  Owner Use One Time Mark For.  */  
   OwnerUseOTMF:boolean,
      /**  Location Customer ID.  */  
   LocationCustID:string,
      /**  Location Ship To.  */  
   LocationShipToNum:string,
      /**  Location Use One Time Mark For.  */  
   LocationUseOTMF:boolean,
      /**  Sold To Customer ID.  */  
   SoldToCustID:string,
      /**  Sold To Ship To.  */  
   SoldToShipToNum:string,
      /**  Sold To Use Ont Time Mark For.  */  
   SoldToUseOTMF:boolean,
      /**  Sold To Business Model  */  
   SoldToBusinessModel:string,
      /**  Addres type of owner : L=Locatoin, O=Owner, S=Sold To  */  
   OwnerAddrType:string,
      /**  Date when transfer occured - writes to LocationTran.EffectiveDate  */  
   EffectiveDate:string,
   EnableDynAttrButton:boolean,
      /**  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  */  
   NewConNum:number,
      /**  External field to hold the name of the selected customer contact for the Location record  */  
   LocationAttn:string,
      /**  External field to hold the name of the selected customer contact for the selected record  */  
   NewConName:string,
      /**  External field to hold the name of the selected customer contact for the Owner record  */  
   OwnerAttn:string,
   BitFlag:number,
   FSWarrCdWarrDescription:string,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumAttrClassID:string,
   PartNumSellingFactor:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LocationInventoryTableset{
   LocationInventory:Erp_Tablesets_LocationInventoryRow[],
   LocationInventoryAddress:Erp_Tablesets_LocationInventoryAddressRow[],
   LocationMtl:Erp_Tablesets_LocationMtlRow[],
   LocationTran:Erp_Tablesets_LocationTranRow[],
   LocationWarrantyTran:Erp_Tablesets_LocationWarrantyTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LocationMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   JobComplete:boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   PartNum:string,
      /**  A description of the material.  */  
   Description:string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   QtyPer:number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   IUM:string,
      /**  Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.  When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   LeadTime:number,
      /**  A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.  It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   RelatedOperation:number,
      /**  The material burden rate for this Job Material.  */  
   MtlBurRate:number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstMtlBurUnitCost:number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   IssuedQty:number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   TotalCost:number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   MtlBurCost:number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   ReqDate:string,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  The salvage material burden rate for this Job Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   SalvageQtyToDate:number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   SalvageCredit:number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   SalvageMtlBurCredit:number,
      /**  Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.  */  
   MfgComment:string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   BuyIt:boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   Ordered:boolean,
      /**  Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.  */  
   PurComment:string,
      /**  Indicates if this material will be backflushed.  Note: this field is defaulted from Part.BackFlush Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   BackFlush:boolean,
      /**  Estimated Scrap.  */  
   EstScrap:number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   Direct:boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   MaterialMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialSubCost:number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialBurCost:number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageMtlCredit:number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageLbrCredit:number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageBurCredit:number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageSubCredit:number,
      /**  Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler: 'I' to ignore in eScheduler.  */  
   APSAddResType:string,
      /**  The service call that this Material belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this material relates to.  */  
   CallLine:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  FS - Unit Price for the Material in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  Is this a billable material item.  */  
   Billable:boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   ShippedQty:number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   DocUnitPrice:number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   QtyStagedToDate:number,
      /**  This material was added after initial setup of the job  */  
   AddedMtl:boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   SCMiscCode:string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**  RFQ SRFQ Status: W= Waiting, A = Accepted, R = Requested, C = Receivedtatus.  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   WIReqDate:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.  */  
   BaseRequiredQty:number,
      /**  Unit of Measure of the JobMtl.BaseRequiredQty.  If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   BaseUOM:string,
      /**  Material Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   StagingBinNum:string,
      /**  A non blank character indicates that the release could not be picked by the Auto Pick process. The possible values are: "L" - Order Line can't be shipped complete. "O" - Order can't be shipped complete. "I" - Insufficient quantity reserved"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**  Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**  Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**  Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**  Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstMtlUnitCredit:number,
      /**  Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstLbrUnitCredit:number,
      /**  Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstBurUnitCredit:number,
      /**  Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstSubUnitCredit:number,
      /**  The material quantity that has been loaned out to another job.  */  
   LoanedQty:number,
      /**  The material quantity that has been borrowed from another job.  */  
   BorrowedQty:number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   ReassignSNAsm:boolean,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  PricingUOM  */  
   PricingUOM:string,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  IsPOCostingMaintained  */  
   IsPOCostingMaintained:boolean,
      /**  EstStdType  */  
   EstStdType:number,
      /**  POCostingFactor  */  
   POCostingFactor:number,
      /**  PlannedQtyPerUnit  */  
   PlannedQtyPerUnit:number,
      /**  POCostingDirection  */  
   POCostingDirection:number,
      /**  POCostingUnitVal  */  
   POCostingUnitVal:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigGroupSeq:number,
      /**  ShowStatusIcon  */  
   ShowStatusIcon:string,
      /**  Contract ID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   StagingLotNum:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  LotNum  */  
   LotNum:string,
      /**  SerialNum  */  
   SerialNum:string,
      /**  WarrantyCode  */  
   WarrantyCode:string,
      /**  WarrantyComment  */  
   WarrantyComment:string,
      /**  WarrantyStartDate  */  
   WarrantyStartDate:string,
      /**  WarrantyExpirationDate  */  
   WarrantyExpirationDate:string,
      /**  LocationNum  */  
   LocationNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  Dealer specific warranty code.  This is a non ERP warranty code.  */  
   DealerWarranty:string,
      /**  Dealer specific warranty description  */  
   DealerWarrantyDesc:string,
      /**  Dealer specifc warranty expiration date.  */  
   DealerWarrantyExpiration:string,
      /**  Dealer specific warranty start date.  */  
   DealerWarrantyStart:string,
      /**  Original Serial Number  */  
   OriginalSerialNum:string,
   OriginalPartNum:string,
   BitFlag:number,
   FSWarrCdWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LocationTranRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Unique ID of Location Inventory  */  
   LocationNum:number,
      /**  LocationSeqNum  */  
   LocationSeqNum:number,
      /**  The customer the transfer is for at that time.  */  
   CustNum:number,
      /**  The current ship to the transfer is for at that time.  */  
   CustShipToNum:string,
      /**  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  */  
   AddressType:string,
      /**  The first line of the address for given location type at that time.  */  
   Address1:string,
      /**  The second line of the address for given location type at that time.  */  
   Address2:string,
      /**  The third line of the address for given location type at that time.  */  
   Address3:string,
      /**  City portion of the address for given location type at that time.  */  
   City:string,
      /**  Contact Name for given location type at that time.  */  
   Contact:string,
      /**  Country number for the Ship To location for at that time.  */  
   CountryNum:number,
      /**  The email address for given location type at that time.  */  
   EmailAddress:string,
      /**  Fax number for given location type at that time.  */  
   FaxNum:string,
      /**  Name for for given location type at that time.  */  
   Name:string,
      /**  Phone number for for given location type at that time  */  
   PhoneNum:string,
      /**  The state or province portion to the location for at that time.  */  
   State:string,
      /**  The zip or postal code portion to location for at that time.  */  
   Zip:string,
      /**  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  This columns is nno longer used.  */  
   WarrantyTransfer:string,
      /**  Date when transfer occurred  */  
   EffectiveDate:string,
      /**  Comment about the transfer transaction.  */  
   Comment:string,
      /**  Created On  */  
   CreatedOn:string,
      /**  Created By  */  
   CreatedBy:string,
      /**  Warranty Code  */  
   WarrantyCode:string,
      /**  Warranty Comment  */  
   WarrantyComment:string,
      /**  Date when the warranty started.  */  
   WarrantyStartDate:string,
      /**  Date when the warranty expires.  */  
   WarrantyExpirationDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ShipToAddrList:string,
   BitFlag:number,
   CustomerECCType:string,
   CustomerCustID:string,
   FSWarrCdWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LocationWarrantyTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  LocationNum  */  
   LocationNum:number,
      /**  Sequence number.  This is system generated and is not maintainable.  */  
   WarrantySeqNum:number,
      /**  Finished good Identificaton Number  */  
   IDNum:string,
      /**  SerialNum  */  
   SerialNum:string,
      /**  Comment about the warranty transfer transaction.  */  
   Comment:string,
      /**  Effective Date  */  
   EffectiveDate:string,
      /**  HDCaseNum  */  
   HDCaseNum:number,
      /**  ParentPartNum  */  
   ParentPartNum:string,
      /**  OriginalPartNum  */  
   OriginalPartNum:string,
      /**  OriginalPartSerialNum  */  
   OriginalPartSerialNum:string,
      /**  NewPartNum  */  
   NewPartNum:string,
      /**  NewPartSerialNum  */  
   NewPartSerialNum:string,
      /**  PartDescription  */  
   PartDescription:string,
      /**  WarrantyCode  */  
   WarrantyCode:string,
      /**  WarrantyComment  */  
   WarrantyComment:string,
      /**  Date when warranty started.  */  
   WarrantyStartDate:string,
      /**  Date when warranty expires  */  
   WarrantyExpirationDate:string,
      /**  Dealer Warranty, this is for a non Erp warranty.  */  
   DealerWarranty:string,
      /**  Dealer warranty description, this is for a non Erp warranty  */  
   DealerWarrantyDesc:string,
      /**  Date dealer warranty started, this is for a non Erp warranty  */  
   DealerWarrantyStart:string,
      /**  Date dealer warranty expires, this is for a non Erp warranty.  */  
   DealerWarrantyExpiration:string,
      /**  WarrantyUsage  */  
   WarrantyUsage:string,
      /**  LotNum  */  
   LotNum:string,
      /**  SystemCreated  */  
   SystemCreated:boolean,
      /**  Created On  */  
   CreatedOn:string,
      /**  Created By  */  
   CreatedBy:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   FSWarrCdWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LocationWarrantyTranTableset{
   LocationWarrantyTran:Erp_Tablesets_LocationWarrantyTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtLocationInventoryTableset{
   LocationInventory:Erp_Tablesets_LocationInventoryRow[],
   LocationInventoryAddress:Erp_Tablesets_LocationInventoryAddressRow[],
   LocationMtl:Erp_Tablesets_LocationMtlRow[],
   LocationTran:Erp_Tablesets_LocationTranRow[],
   LocationWarrantyTran:Erp_Tablesets_LocationWarrantyTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param locationNum
   */  
export interface GetByID_input{
   locationNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LocationInventoryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LocationInventoryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LocationInventoryTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetCurrentAddress_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface GetCurrentAddress_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
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
   returnObj:Erp_Tablesets_LocationInventoryListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param locationNum
      @param idNum
   */  
export interface GetLocationWarrantyTran_input{
   locationNum:number,
   idNum:string,
}

export interface GetLocationWarrantyTran_output{
   returnObj:Erp_Tablesets_LocationWarrantyTranTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetNewCustomerAddress_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface GetNewCustomerAddress_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
      @param locationNum
   */  
export interface GetNewLocationInventoryAddress_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
   locationNum:number,
}

export interface GetNewLocationInventoryAddress_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewLocationInventory_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface GetNewLocationInventory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
      @param locationNum
      @param jobNum
      @param assemblySeq
   */  
export interface GetNewLocationMtl_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
   locationNum:number,
   jobNum:string,
   assemblySeq:number,
}

export interface GetNewLocationMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
      @param locationNum
   */  
export interface GetNewLocationTran_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
   locationNum:number,
}

export interface GetNewLocationTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
      @param locationNum
   */  
export interface GetNewLocationWarrantyTran_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
   locationNum:number,
}

export interface GetNewLocationWarrantyTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewOTMFAddress_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface GetNewOTMFAddress_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param whereClauseLocationInventory
      @param whereClauseLocationInventoryAddress
      @param whereClauseLocationMtl
      @param whereClauseLocationTran
      @param whereClauseLocationWarrantyTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLocationInventory:string,
   whereClauseLocationInventoryAddress:string,
   whereClauseLocationMtl:string,
   whereClauseLocationTran:string,
   whereClauseLocationWarrantyTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LocationInventoryTableset[],
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
   ds:Erp_Tablesets_UpdExtLocationInventoryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLocationInventoryTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LocationInventoryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LocationInventoryTableset,
}
}

   /** Required : 
      @param proposedCustID
   */  
export interface ValidateCustomer_input{
   proposedCustID:string,
}

export interface ValidateCustomer_output{
   returnObj:number,
}

   /** Required : 
      @param partNum
      @param proposeIDNum
   */  
export interface ValidateIDNumber_input{
   partNum:string,
   proposeIDNum:string,
}

export interface ValidateIDNumber_output{
   returnObj:boolean,
}

   /** Required : 
      @param partNum
      @param jobNum
      @param proposeLotNum
   */  
export interface ValidateMaterialLotNumber_input{
   partNum:string,
   jobNum:string,
   proposeLotNum:string,
}

export interface ValidateMaterialLotNumber_output{
   returnObj:boolean,
}

   /** Required : 
      @param partNum
      @param jobNum
      @param proposeSerialNo
   */  
export interface ValidateMaterialOrigSerialNumber_input{
   partNum:string,
   jobNum:string,
   proposeSerialNo:string,
}

export interface ValidateMaterialOrigSerialNumber_output{
   returnObj:boolean,
}

   /** Required : 
      @param proposedPartNum
   */  
export interface ValidatePartNum_input{
   proposedPartNum:string,
}

export interface ValidatePartNum_output{
   returnObj:string,
}

   /** Required : 
      @param partNum
      @param proposeSerialNo
   */  
export interface ValidateSerialNumber_input{
   partNum:string,
   proposeSerialNo:string,
}

export interface ValidateSerialNumber_output{
   returnObj:string,
}

   /** Required : 
      @param custNum
      @param proposedShipTo
   */  
export interface ValidateShipTo_input{
   custNum:number,
   proposedShipTo:string,
}

export interface ValidateShipTo_output{
   returnObj:string,
}

