import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CCPartSelectUpdSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/$metadata", {
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
   Description: Get CCPartSelectUpds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCPartSelectUpds
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrRow
   */  
export function get_CCPartSelectUpds(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCPartSelectUpds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CCHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCPartSelectUpds(requestBody:Erp_Tablesets_CCHdrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CCPartSelectUpd item
   Description: Calls GetByID to retrieve the CCPartSelectUpd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPartSelectUpd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCHdrRow
   */  
export function get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
         resolve(data as Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCPartSelectUpd for the service
   Description: Calls UpdateExt to update CCPartSelectUpd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCPartSelectUpd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, requestBody:Erp_Tablesets_CCHdrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
   Summary: Call UpdateExt to delete CCPartSelectUpd item
   Description: Call UpdateExt to delete CCPartSelectUpd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCPartSelectUpd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
   Description: Get CCDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlRow
   */  
export function get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CCDtl item
   Description: Calls GetByID to retrieve the CCDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCDtlRow
   */  
export function get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
         resolve(data as Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CCPCIDs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCPCIDs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDRow
   */  
export function get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CCPCID item
   Description: Calls GetByID to retrieve the CCPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCID1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCPCIDRow
   */  
export function get_CCPartSelectUpds_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPartSelectUpds(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
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
         resolve(data as Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CCDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlRow
   */  
export function get_CCDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CCDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCDtls(requestBody:Erp_Tablesets_CCDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CCDtl item
   Description: Calls GetByID to retrieve the CCDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCDtlRow
   */  
export function get_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
         resolve(data as Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCDtl for the service
   Description: Calls UpdateExt to update CCDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, requestBody:Erp_Tablesets_CCDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
   Summary: Call UpdateExt to delete CCDtl item
   Description: Call UpdateExt to delete CCDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
   Description: Get CCPCIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCPCIDs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDRow
   */  
export function get_CCPCIDs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCPCIDs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CCPCIDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCPCIDs(requestBody:Erp_Tablesets_CCPCIDRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CCPCID item
   Description: Calls GetByID to retrieve the CCPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCPCIDRow
   */  
export function get_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
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
         resolve(data as Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCPCID for the service
   Description: Calls UpdateExt to update CCPCID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, requestBody:Erp_Tablesets_CCPCIDRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
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
   Summary: Call UpdateExt to delete CCPCID item
   Description: Call UpdateExt to delete CCPCID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
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
   Description: Get CCPCIDSelecteds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCPCIDSelecteds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDSelectedRow
   */  
export function get_CCPCIDSelecteds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDSelectedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDSelectedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCPCIDSelecteds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCPCIDSelecteds(requestBody:Erp_Tablesets_CCPCIDSelectedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CCPCIDSelected item
   Description: Calls GetByID to retrieve the CCPCIDSelected item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCIDSelected
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
   */  
export function get_CCPCIDSelecteds_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCPCIDSelectedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_CCPCIDSelectedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCPCIDSelected for the service
   Description: Calls UpdateExt to update CCPCIDSelected. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCPCIDSelected
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCPCIDSelectedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCPCIDSelecteds_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_CCPCIDSelectedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CCPCIDSelected item
   Description: Call UpdateExt to delete CCPCIDSelected item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCPCIDSelected
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCPCIDSelecteds_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CCPCIDSelecteds(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCCHdr:string, whereClauseCCDtl:string, whereClauseCCPCID:string, whereClauseCCPCIDSelected:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCCHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCHdr=" + whereClauseCCHdr
   }
   if(typeof whereClauseCCDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCDtl=" + whereClauseCCDtl
   }
   if(typeof whereClauseCCPCID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCPCID=" + whereClauseCCPCID
   }
   if(typeof whereClauseCCPCIDSelected!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCPCIDSelected=" + whereClauseCCPCIDSelected
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetRows" + params, {
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
   Required: True
   Required: True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, warehouseCode:string, ccYear:string, ccMonth:string, fullPhysical:string, cycleSeq:string, epicorHeaders?:Headers){
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
   if(typeof warehouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warehouseCode=" + warehouseCode
   }
   if(typeof ccYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ccYear=" + ccYear
   }
   if(typeof ccMonth!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ccMonth=" + ccMonth
   }
   if(typeof fullPhysical!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fullPhysical=" + fullPhysical
   }
   if(typeof cycleSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cycleSeq=" + cycleSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetList" + params, {
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
   Summary: Invoke method MoveParts
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="moveToMonth">The move-to month</param>
/// <param name="moveToYear">The move-to month</param>
/// <param name="moveToCycle">The move-to month</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: MoveParts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveParts(requestBody:MoveParts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveParts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/MoveParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MoveParts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:OnChangingAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/OnChangingAttributeSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/OnChangingRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Purpose:
Parameters:  none
Notes:
///<param name="ipPartNum">Input Part Number</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/OnChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCID
   Description: Purpose:
Parameters:  none
Notes:
///<param name="ipPCID">Part Number</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: OnChangePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCID(requestBody:OnChangePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/OnChangePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveParts
   Description: Purpose: Deletes all CCDtl for a particular CCHdr
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: RemoveParts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveParts(requestBody:RemoveParts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveParts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/RemoveParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RemoveParts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemovePCIDs
   Description: Purpose: Deletes all PCIDs for a particular CCHdr
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: RemovePCIDs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemovePCIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePCIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemovePCIDs(requestBody:RemovePCIDs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemovePCIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/RemovePCIDs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RemovePCIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MovePCIDs
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="moveToMonth">The move-to month</param>
/// <param name="moveToYear">The move-to month</param>
/// <param name="moveToCycle">The move-to month</param>
/// <param name="ds">CCPartSelectUpd dataset</param>
   OperationID: MovePCIDs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MovePCIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MovePCIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MovePCIDs(requestBody:MovePCIDs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MovePCIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/MovePCIDs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MovePCIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePCIDSelected
   Description: Purpose: Updates CCPCIDSelected with values from WhseBin
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpdTableset dataset</param>
   OperationID: UpdatePCIDSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdatePCIDSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePCIDSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePCIDSelected(requestBody:UpdatePCIDSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdatePCIDSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/UpdatePCIDSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdatePCIDSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreatePCIDSelected
   Description: Purpose: Creates CCPCIDSelected from PkgControlHdr
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpdTableset dataset</param>
/// <param name="whseCode" /> warehouse code
/// <param name="frBin" /> from bin
/// <param name="toBin" /> to bin
/// <param name="frZone" /> from zone
/// <param name="toZone" /> to zone
   OperationID: CreatePCIDSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreatePCIDSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePCIDSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePCIDSelected(requestBody:CreatePCIDSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreatePCIDSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/CreatePCIDSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreatePCIDSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassAddPartAttributeSets
   Description: Purpose: Creates CCDtl records for all valid attribute sets for an attribute set tracked part
Parameters:  none
Notes:
<param name="ds">CCPartSelectUpdTableset dataset</param><param name="ccHdrSysRowID">SysRowID for the CCHdr to which the CCDtl will be added</param><param name="partNum">Part Number for which the attribute sets will be added</param>
   OperationID: MassAddPartAttributeSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MassAddPartAttributeSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAddPartAttributeSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassAddPartAttributeSets(requestBody:MassAddPartAttributeSets_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MassAddPartAttributeSets_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/MassAddPartAttributeSets", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MassAddPartAttributeSets_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddPCIDToCycle
   Description: Purpose: Creates CCPCID records from PCCPCIDSelected
Parameters:  none
Notes:
/// <param name="ds">CCPartSelectUpdTableset dataset</param>
/// <param name="year"> year</param>
/// <param name="month"> month</param>
/// <param name="fullPhysical"> fullPhysical</param>
/// <param name="cycleSeq"> cycleSeq</param>
   OperationID: AddPCIDToCycle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddPCIDToCycle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPCIDToCycle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddPCIDToCycle(requestBody:AddPCIDToCycle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddPCIDToCycle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/AddPCIDToCycle", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AddPCIDToCycle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Purpose: Deletes all CCDtl for a particular CCHdr
Parameters:  none
Notes:
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetNewCCHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCHdr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCCHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCHdr(requestBody:GetNewCCHdr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCCHdr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetNewCCHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCCHdr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCCDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCCDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCDtl(requestBody:GetNewCCDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCCDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetNewCCDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCCDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCCPCID
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCCPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCPCID(requestBody:GetNewCCPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCCPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetNewCCPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCCPCID_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCPartSelectUpdSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCHdrListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCHdrRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCPCIDRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDSelectedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCPCIDSelectedRow,
}

export interface Erp_Tablesets_CCDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   "AllocationVariance":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  Part Number selected for counting.  */  
   "PartNum":string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   "TotFrozenVal":number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   "TotFrozenQOH":number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   "PostStatus":number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   "CDRCode":string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   "TotCountVal":number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   "TotCountQOH":number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   "DateRemoved":string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   "RemovedBy":string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   "MoveToCycle":string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "PcntTolerance":number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCCode":string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyToleranceUsed":boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   "PcntToleranceUsed":boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   "ValToleranceUsed":boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   "QtyAdjTolerance":number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   "VarToleranceStat":number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   "PostAdjustment":number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyTolerance":number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   "ValueTolerance":number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "BaseUOM":string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   "TotActivityBeforeCount":number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   "TotActivityBeforeVal":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   "AddedByBlankTag":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCSeq":number,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   "EnableCDRCode":boolean,
      /**  Moved To Cycle Seq  */  
   "MovedToCycleSeq":number,
      /**  Moved to Month  */  
   "MovedToMonth":number,
      /**  Moved to Year  */  
   "MovedToYear":number,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   "MovePart":boolean,
      /**  Month name of MonthToMonth field  */  
   "MoveToMonthName":string,
      /**  Post Status Description  */  
   "PostStatusDesc":string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   "QtyAdjustmentStatus":string,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   "QtyVariance":number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   "ValueVariance":number,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   "VarToleranceStatDesc":string,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   "VoidPartTags":boolean,
      /**  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  */  
   "AddAllAttributeSets":boolean,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "EnableAttributeSetSearch":boolean,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
   "BitFlag":number,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodEnd":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "ReasonDescription":string,
   "WarehseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCHdrListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   "CycleDate":string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   "CycleStatus":number,
      /**  This is the date the tags were generated  */  
   "TagGenDate":string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   "SeqStartDate":string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   "TimeSeqStarted":number,
      /**  This is the date the cycle was completed or cancelled.  */  
   "CompleteDate":string,
      /**  This is the time the cycle was completed or cancelled.  */  
   "CompleteTime":number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   "AdjustPosted":boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   "SheetOrTag":number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   "TotalParts":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   "TotalPCIDSelected":number,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   "NumOfBlankTags":number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   "BlankTagsOnly":boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   "TagSortOption":number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   "PostTransDate":string,
      /**  External field used to hold the Post Counts log filename.  */  
   "LogFileName":string,
   "EnablePrintTags":boolean,
   "EnableReprintTags":boolean,
   "EnableVoidTagsByPart":boolean,
   "EnableVoidBlankTags":boolean,
   "EnableStartCountSeq":boolean,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   "RemoveAllParts":boolean,
   "CycleDateString":string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   "CycleStatusDesc":string,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   "CancelPI":boolean,
      /**  Month Name  */  
   "MonthName":string,
      /**  Description.  */  
   "CCHdrWarehseDescription":string,
      /**  Defines the end date of the period  */  
   "CCPeriodDefnPeriodEnd":string,
      /**  Defines the start date of the count period  */  
   "CCPeriodDefnPeriodStart":string,
      /**  Unique period description assigned by the user.  */  
   "CCPeriodDefnPeriodDesc":string,
   "WhseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCHdrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   "CycleDate":string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   "CycleStatus":number,
      /**  This is the date the tags were generated  */  
   "TagGenDate":string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   "SeqStartDate":string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   "TimeSeqStarted":number,
      /**  This is the date the cycle was completed or cancelled.  */  
   "CompleteDate":string,
      /**  This is the time the cycle was completed or cancelled.  */  
   "CompleteTime":number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   "AdjustPosted":boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   "SheetOrTag":number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   "TotalParts":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IncludeNonNettable  */  
   "IncludeNonNettable":boolean,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   "TotalPCIDSelected":number,
      /**  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  */  
   "NestedPCID":boolean,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   "CancelPI":boolean,
   "CycleDateString":string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   "CycleStatusDesc":string,
   "EnablePrintTags":boolean,
   "EnableReprintTags":boolean,
   "EnableStartCountSeq":boolean,
   "EnableVoidBlankTags":boolean,
   "EnableVoidTagsByPart":boolean,
      /**  External field used to hold the Post Counts log filename.  */  
   "LogFileName":string,
      /**  Month Name  */  
   "MonthName":string,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   "NumOfBlankTags":number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   "PostTransDate":string,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   "RemoveAllParts":boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   "TagSortOption":number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   "BlankTagsOnly":boolean,
      /**  field used by GenerateTags to indicate how many blank PCID tags should be generated  */  
   "NumOfBlankPCIDTags":number,
   "PartPostedExists":boolean,
   "TrackedNumberSerialPart":boolean,
      /**  Indicates that any PartNumTrackSerialNum = true exist in details  */  
   "PartNumTrackSerialNum":boolean,
   "BitFlag":number,
   "CCHdrWarehseDescription":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodEnd":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCPCIDRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Site Identifier  */  
   "Plant":string,
      /**  Warehouse identifier  */  
   "WarehouseCode":string,
      /**  Calendar year that this cycle count is for  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  True = full physical inventory count cycle, false = cycle count cycle  */  
   "FullPhysical":boolean,
      /**  Cycle Sequence  */  
   "CycleSeq":number,
      /**  Equates to a PkgControlHeader PCID. It could be top level or a nested PCID.  */  
   "PCID":string,
      /**  The Parent PCID defined for this CCPCID.PCID  */  
   "ParentPCID":string,
      /**  The outermost PCID that contains this CCPCID.PCID  */  
   "TopLevelPCID":string,
      /**  True indicates this PCID was added to the cycle during count entry using a blank tag.  */  
   "AddedByBlankTag":boolean,
      /**  If any ItemPartNum count of this PCID has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE. For consistency with CCDtl, not currently used  */  
   "AllocationVariance":boolean,
      /**  Bin number defaulted from PkgControlHeader or entered on a blank tag  */  
   "BinNum":string,
      /**  There will be data here only if PostStatus =3 and the PCID was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   "MoveToCycle":string,
      /**  The date the PCID was removed from  the cycle. (PostStatus=3)  */  
   "DateRemoved":string,
      /**  This is the user id of the person that removed the PCID from the cycle (PostStatus=3)  */  
   "RemovedBy":string,
      /**  This data is created by the cycle count variance report process.  Used by the posting process to determine whether to post adjustments to inventory.  Code Desc: 0`Not Yet Evaluated~1`Adjustment Will Not Post~2`Adjustment Will Post  */  
   "PostAdjustment":number,
      /**  The posting status of the PCID. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made. 2= the count for this PCID has been processed by the post final counts process and inventory adjustments were not made 3= PCID was removed from the cycle after tags were generated, no posting required Code Desc: 0`Not Posted~1`Adjustment Posted~2`No Adjustment  Required~3`Voided  */  
   "PostStatus":number,
      /**  Reserved for development use.  */  
   "CCPCIDBoolean01":boolean,
      /**  Reserved for development use.  */  
   "CCPCIDBoolean02":boolean,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter01":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter02":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter03":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter04":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter05":string,
      /**  Reserved for development use.  */  
   "CCPCIDDate01":string,
      /**  Reserved for development use.  */  
   "CCPCIDDate02":string,
      /**  Reserved for development use.  */  
   "CCPCIDDecimal01":number,
      /**  Reserved for development use.  */  
   "CCPCIDDecimal02":number,
      /**  Used for indicating the level at which this PCIDis nested below the top level it is associated to  */  
   "CCPCIDInteger01":number,
      /**  Reserved for development use.  */  
   "CCPCIDInteger02":number,
      /**  The warehouse to which the PCID should be moved during posting.  */  
   "MoveToWarehouseCode":string,
      /**  The warehouse bin to which the PCID should be moved during posting.  */  
   "MoveToBinNum":string,
      /**  The PCID to which this PCID should be added during posting.  */  
   "AddToPCID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Indicates if the CCPCID was selected for move or delete in Cycle Count Part / PCID Selection Update.  */  
   "MovePCID":boolean,
      /**  Needed if the user will be able to move PCID from one cycle to another in Part Selection Update  */  
   "MovetoMonthName":string,
      /**  Used to indicate that the VoidTagsByPCID processing should be done for this PCID.  */  
   "VoidPCIDTags":boolean,
      /**  The Month that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodSeq.  */  
   "MovedToMonth":number,
      /**  The Year that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodYear.  */  
   "MovedToYear":number,
      /**  The Cycle that this PCID was moved to during posting.  Format consistent with CCHdr.CycleSeq.  */  
   "MovedToCycleSeq":number,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   "QtyAdjustmentStatus":string,
   "BitFlag":number,
   "CCPeriodDefnPeriodEnd":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodDesc":string,
   "WarehseDescription":string,
   "WhseBinDescription":string,
   "WhseBinAisle":string,
   "WhseBinZoneID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCPCIDSelectedRow{
      /**  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  */  
   "Aisle":string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   "BinNum":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  */  
   "Elevation":number,
      /**  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  */  
   "Face":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  Site where the PCID is currently located.  */  
   "Plant":string,
      /**  Set to true if selected by the user.  */  
   "Selected":boolean,
      /**  Warehouse where the PCID is currently located.  */  
   "WarehouseCode":string,
      /**  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  */  
   "ZoneID":string,
   "SysRowID":string,
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
      @param year
      @param month
      @param fullPhysical
      @param cycleSeq
   */  
export interface AddPCIDToCycle_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
   year:number,
   month:number,
   fullPhysical:boolean,
   cycleSeq:number,
}

export interface AddPCIDToCycle_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ds
      @param whseCode
      @param frBin
      @param toBin
      @param frZone
      @param toZone
   */  
export interface CreatePCIDSelected_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
   whseCode:string,
   frBin:string,
   toBin:string,
   frZone:string,
   toZone:string,
}

export interface CreatePCIDSelected_output{
   returnObj:Erp_Tablesets_CCPartSelectUpdTableset[],
}

   /** Required : 
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
   */  
export interface DeleteByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CCDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   AllocationVariance:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  Part Number selected for counting.  */  
   PartNum:string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   TotFrozenVal:number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   TotFrozenQOH:number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   PostStatus:number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   CDRCode:string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   TotCountVal:number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   TotCountQOH:number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   DateRemoved:string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   RemovedBy:string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   MoveToCycle:string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   PcntTolerance:number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCCode:string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyToleranceUsed:boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   PcntToleranceUsed:boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   ValToleranceUsed:boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   QtyAdjTolerance:number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   VarToleranceStat:number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   PostAdjustment:number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyTolerance:number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   ValueTolerance:number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   BaseUOM:string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   TotActivityBeforeCount:number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   TotActivityBeforeVal:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   AddedByBlankTag:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCSeq:number,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   EnableCDRCode:boolean,
      /**  Moved To Cycle Seq  */  
   MovedToCycleSeq:number,
      /**  Moved to Month  */  
   MovedToMonth:number,
      /**  Moved to Year  */  
   MovedToYear:number,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   MovePart:boolean,
      /**  Month name of MonthToMonth field  */  
   MoveToMonthName:string,
      /**  Post Status Description  */  
   PostStatusDesc:string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   QtyAdjustmentStatus:string,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   QtyVariance:number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   ValueVariance:number,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   VarToleranceStatDesc:string,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   VoidPartTags:boolean,
      /**  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  */  
   AddAllAttributeSets:boolean,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   EnableAttributeSetSearch:boolean,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   BitFlag:number,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodEnd:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   ReasonDescription:string,
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCHdrListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   CycleDate:string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   CycleStatus:number,
      /**  This is the date the tags were generated  */  
   TagGenDate:string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   SeqStartDate:string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   TimeSeqStarted:number,
      /**  This is the date the cycle was completed or cancelled.  */  
   CompleteDate:string,
      /**  This is the time the cycle was completed or cancelled.  */  
   CompleteTime:number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   AdjustPosted:boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   SheetOrTag:number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   TotalParts:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   TotalPCIDSelected:number,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   NumOfBlankTags:number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   BlankTagsOnly:boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   TagSortOption:number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   PostTransDate:string,
      /**  External field used to hold the Post Counts log filename.  */  
   LogFileName:string,
   EnablePrintTags:boolean,
   EnableReprintTags:boolean,
   EnableVoidTagsByPart:boolean,
   EnableVoidBlankTags:boolean,
   EnableStartCountSeq:boolean,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   RemoveAllParts:boolean,
   CycleDateString:string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   CycleStatusDesc:string,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   CancelPI:boolean,
      /**  Month Name  */  
   MonthName:string,
      /**  Description.  */  
   CCHdrWarehseDescription:string,
      /**  Defines the end date of the period  */  
   CCPeriodDefnPeriodEnd:string,
      /**  Defines the start date of the count period  */  
   CCPeriodDefnPeriodStart:string,
      /**  Unique period description assigned by the user.  */  
   CCPeriodDefnPeriodDesc:string,
   WhseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCHdrListTableset{
   CCHdrList:Erp_Tablesets_CCHdrListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CCHdrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   CycleDate:string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   CycleStatus:number,
      /**  This is the date the tags were generated  */  
   TagGenDate:string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   SeqStartDate:string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   TimeSeqStarted:number,
      /**  This is the date the cycle was completed or cancelled.  */  
   CompleteDate:string,
      /**  This is the time the cycle was completed or cancelled.  */  
   CompleteTime:number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   AdjustPosted:boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   SheetOrTag:number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   TotalParts:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IncludeNonNettable  */  
   IncludeNonNettable:boolean,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   TotalPCIDSelected:number,
      /**  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  */  
   NestedPCID:boolean,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   CancelPI:boolean,
   CycleDateString:string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   CycleStatusDesc:string,
   EnablePrintTags:boolean,
   EnableReprintTags:boolean,
   EnableStartCountSeq:boolean,
   EnableVoidBlankTags:boolean,
   EnableVoidTagsByPart:boolean,
      /**  External field used to hold the Post Counts log filename.  */  
   LogFileName:string,
      /**  Month Name  */  
   MonthName:string,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   NumOfBlankTags:number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   PostTransDate:string,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   RemoveAllParts:boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   TagSortOption:number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   BlankTagsOnly:boolean,
      /**  field used by GenerateTags to indicate how many blank PCID tags should be generated  */  
   NumOfBlankPCIDTags:number,
   PartPostedExists:boolean,
   TrackedNumberSerialPart:boolean,
      /**  Indicates that any PartNumTrackSerialNum = true exist in details  */  
   PartNumTrackSerialNum:boolean,
   BitFlag:number,
   CCHdrWarehseDescription:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodEnd:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCPCIDRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Site Identifier  */  
   Plant:string,
      /**  Warehouse identifier  */  
   WarehouseCode:string,
      /**  Calendar year that this cycle count is for  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  True = full physical inventory count cycle, false = cycle count cycle  */  
   FullPhysical:boolean,
      /**  Cycle Sequence  */  
   CycleSeq:number,
      /**  Equates to a PkgControlHeader PCID. It could be top level or a nested PCID.  */  
   PCID:string,
      /**  The Parent PCID defined for this CCPCID.PCID  */  
   ParentPCID:string,
      /**  The outermost PCID that contains this CCPCID.PCID  */  
   TopLevelPCID:string,
      /**  True indicates this PCID was added to the cycle during count entry using a blank tag.  */  
   AddedByBlankTag:boolean,
      /**  If any ItemPartNum count of this PCID has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE. For consistency with CCDtl, not currently used  */  
   AllocationVariance:boolean,
      /**  Bin number defaulted from PkgControlHeader or entered on a blank tag  */  
   BinNum:string,
      /**  There will be data here only if PostStatus =3 and the PCID was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   MoveToCycle:string,
      /**  The date the PCID was removed from  the cycle. (PostStatus=3)  */  
   DateRemoved:string,
      /**  This is the user id of the person that removed the PCID from the cycle (PostStatus=3)  */  
   RemovedBy:string,
      /**  This data is created by the cycle count variance report process.  Used by the posting process to determine whether to post adjustments to inventory.  Code Desc: 0`Not Yet Evaluated~1`Adjustment Will Not Post~2`Adjustment Will Post  */  
   PostAdjustment:number,
      /**  The posting status of the PCID. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made. 2= the count for this PCID has been processed by the post final counts process and inventory adjustments were not made 3= PCID was removed from the cycle after tags were generated, no posting required Code Desc: 0`Not Posted~1`Adjustment Posted~2`No Adjustment  Required~3`Voided  */  
   PostStatus:number,
      /**  Reserved for development use.  */  
   CCPCIDBoolean01:boolean,
      /**  Reserved for development use.  */  
   CCPCIDBoolean02:boolean,
      /**  Reserved for development use.  */  
   CCPCIDCharacter01:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter02:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter03:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter04:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter05:string,
      /**  Reserved for development use.  */  
   CCPCIDDate01:string,
      /**  Reserved for development use.  */  
   CCPCIDDate02:string,
      /**  Reserved for development use.  */  
   CCPCIDDecimal01:number,
      /**  Reserved for development use.  */  
   CCPCIDDecimal02:number,
      /**  Used for indicating the level at which this PCIDis nested below the top level it is associated to  */  
   CCPCIDInteger01:number,
      /**  Reserved for development use.  */  
   CCPCIDInteger02:number,
      /**  The warehouse to which the PCID should be moved during posting.  */  
   MoveToWarehouseCode:string,
      /**  The warehouse bin to which the PCID should be moved during posting.  */  
   MoveToBinNum:string,
      /**  The PCID to which this PCID should be added during posting.  */  
   AddToPCID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates if the CCPCID was selected for move or delete in Cycle Count Part / PCID Selection Update.  */  
   MovePCID:boolean,
      /**  Needed if the user will be able to move PCID from one cycle to another in Part Selection Update  */  
   MovetoMonthName:string,
      /**  Used to indicate that the VoidTagsByPCID processing should be done for this PCID.  */  
   VoidPCIDTags:boolean,
      /**  The Month that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodSeq.  */  
   MovedToMonth:number,
      /**  The Year that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodYear.  */  
   MovedToYear:number,
      /**  The Cycle that this PCID was moved to during posting.  Format consistent with CCHdr.CycleSeq.  */  
   MovedToCycleSeq:number,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   QtyAdjustmentStatus:string,
   BitFlag:number,
   CCPeriodDefnPeriodEnd:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodDesc:string,
   WarehseDescription:string,
   WhseBinDescription:string,
   WhseBinAisle:string,
   WhseBinZoneID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCPCIDSelectedRow{
      /**  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  */  
   Aisle:string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   BinNum:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  */  
   Elevation:number,
      /**  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  */  
   Face:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Site where the PCID is currently located.  */  
   Plant:string,
      /**  Set to true if selected by the user.  */  
   Selected:boolean,
      /**  Warehouse where the PCID is currently located.  */  
   WarehouseCode:string,
      /**  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  */  
   ZoneID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCPartSelectUpdTableset{
   CCHdr:Erp_Tablesets_CCHdrRow[],
   CCDtl:Erp_Tablesets_CCDtlRow[],
   CCPCID:Erp_Tablesets_CCPCIDRow[],
   CCPCIDSelected:Erp_Tablesets_CCPCIDSelectedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCCPartSelectUpdTableset{
   CCHdr:Erp_Tablesets_CCHdrRow[],
   CCDtl:Erp_Tablesets_CCDtlRow[],
   CCPCID:Erp_Tablesets_CCPCIDRow[],
   CCPCIDSelected:Erp_Tablesets_CCPCIDSelectedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
   */  
export interface GetByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CCPartSelectUpdTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CCPartSelectUpdTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CCPartSelectUpdTableset[],
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
   returnObj:Erp_Tablesets_CCHdrListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
      @param partNum
   */  
export interface GetNewCCDtl_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
   partNum:string,
}

export interface GetNewCCDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
   */  
export interface GetNewCCHdr_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
}

export interface GetNewCCHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
   */  
export interface GetNewCCPCID_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
}

export interface GetNewCCPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param whereClauseCCHdr
      @param whereClauseCCDtl
      @param whereClauseCCPCID
      @param whereClauseCCPCIDSelected
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCCHdr:string,
   whereClauseCCDtl:string,
   whereClauseCCPCID:string,
   whereClauseCCPCIDSelected:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CCPartSelectUpdTableset[],
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
      @param ccHdrSysRowID
      @param partNum
   */  
export interface MassAddPartAttributeSets_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
   ccHdrSysRowID:string,
   partNum:string,
}

export interface MassAddPartAttributeSets_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param moveToMonth
      @param moveToYear
      @param moveToCycle
      @param ds
   */  
export interface MovePCIDs_input{
   moveToMonth:number,
   moveToYear:number,
   moveToCycle:number,
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface MovePCIDs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param moveToMonth
      @param moveToYear
      @param moveToCycle
      @param ds
   */  
export interface MoveParts_input{
   moveToMonth:number,
   moveToYear:number,
   moveToCycle:number,
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface MoveParts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ipPCID
      @param ds
   */  
export interface OnChangePCID_input{
   ipPCID:string,
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface OnChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ipPartNum
      @param ds
   */  
export interface OnChangePartNum_input{
   ipPartNum:string,
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface RemovePCIDs_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface RemovePCIDs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface RemoveParts_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface RemoveParts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCCPartSelectUpdTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCCPartSelectUpdTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdatePCIDSelected_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface UpdatePCIDSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CCPartSelectUpdTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCPartSelectUpdTableset,
}
}

