import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.VendPartRestrictionSvc
// Description: Vendor Part Price - Restriction Substances
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get VendPartRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPartRestrictions
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictionRow
   */  
export function get_VendPartRestrictions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPartRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendPartRestrictions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendPartRestriction item
   Description: Calls GetByID to retrieve the VendPartRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
   */  
export function get_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPartRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPartRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendPartRestriction for the service
   Description: Calls UpdateExt to update VendPartRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPartRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete VendPartRestriction item
   Description: Call UpdateExt to delete VendPartRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPartRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get VendPartRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPartRestrictSubsts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictSubstRow
   */  
export function get_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_VendPartRestrictSubsts(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")/VendPartRestrictSubsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendPartRestrictSubst item
   Description: Calls GetByID to retrieve the VendPartRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartRestrictSubst1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   */  
export function get_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPartRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPartRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get VendPartRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPartRestrictSubsts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictSubstRow
   */  
export function get_VendPartRestrictSubsts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPartRestrictSubsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendPartRestrictSubsts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendPartRestrictSubst item
   Description: Calls GetByID to retrieve the VendPartRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   */  
export function get_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPartRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPartRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendPartRestrictSubst for the service
   Description: Calls UpdateExt to update VendPartRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPartRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, SubstanceID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete VendPartRestrictSubst item
   Description: Call UpdateExt to delete VendPartRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPartRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, RestrictionTypeID:string, SubstanceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictionListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseVendPartRestriction:string, whereClauseVendPartRestrictSubst:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseVendPartRestriction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendPartRestriction=" + whereClauseVendPartRestriction
   }
   if(typeof whereClauseVendPartRestrictSubst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendPartRestrictSubst=" + whereClauseVendPartRestrictSubst
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, opCode:string, puM:string, vendorNum:string, restrictionTypeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof opCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "opCode=" + opCode
   }
   if(typeof puM!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "puM=" + puM
   }
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof restrictionTypeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "restrictionTypeID=" + restrictionTypeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeManual
   Description: Used when Manual field of VendPartRestriction is being changed to a new value.
   OperationID: ChangeManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeManual(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/ChangeManual", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRestrictionSubstance
   Description: This methods assigns associated fields when VendPartRestrictSubst.SubstanceID changes.
   OperationID: ChangeRestrictionSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRestrictionSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRestrictionSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRestrictionSubstance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/ChangeRestrictionSubstance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRestrictionType
   Description: This methods assigns associated fields when VendPartRestriction.RestrictionTypeID changes.
   OperationID: ChangeRestrictionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRestrictionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRestrictionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRestrictionType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/ChangeRestrictionType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRestrictionType
   Description: Used when RestrictionTypeID field of VendPartRestriction is being changging to a new value.
   OperationID: OnChangingRestrictionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRestrictionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRestrictionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRestrictionType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/OnChangingRestrictionType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendPartRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPartRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPartRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPartRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendPartRestriction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/GetNewVendPartRestriction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendPartRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPartRestrictSubst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPartRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPartRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendPartRestrictSubst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/GetNewVendPartRestrictSubst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictSubstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPartRestrictSubstRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPartRestrictionListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPartRestrictionRow[],
}

export interface Erp_Tablesets_VendPartRestrictSubstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies our Part.  */  
   "PartNum":string,
      /**   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  */  
   "OpCode":string,
      /**   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  */  
   "PUM":string,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  Substance identification.  */  
   "SubstanceID":string,
      /**  Default weight of the substance per primary part of UOM  */  
   "Weight":number,
      /**  By default the primary UOM of the part.  */  
   "WeightUOM":string,
      /**  When true then weight is disregarded in compliance roll-up.  */  
   "Manual":boolean,
      /**  The date when exempt status for this substance expires.  */  
   "ExemptDate":string,
      /**  Optional. Exemption certificate.  */  
   "ExemptCertificate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Exempt":boolean,
   "BitFlag":number,
   "OpCodeOpDesc":string,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "RestrictionTypeDescription":string,
   "SubstanceDescription":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumName":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress1":string,
   "VendorNumAddress2":string,
   "VendorNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendPartRestrictionListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies our Part.  */  
   "PartNum":string,
      /**   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  */  
   "OpCode":string,
      /**   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  */  
   "PUM":string,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  */  
   "Manual":boolean,
      /**   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  */  
   "RollUp":boolean,
      /**  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  */  
   "Compliance":string,
      /**  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  */  
   "ComplianceDate":string,
      /**  Set after compliance roll-up  */  
   "LastRollUp":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpCodeOpDesc":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Restriction Type Description  */  
   "RestrictionTypeDescription":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendPartRestrictionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies our Part.  */  
   "PartNum":string,
      /**   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  */  
   "OpCode":string,
      /**   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  */  
   "PUM":string,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  */  
   "Manual":boolean,
      /**   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  */  
   "RollUp":boolean,
      /**  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  */  
   "Compliance":string,
      /**  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  */  
   "ComplianceDate":string,
      /**  Set after compliance roll-up  */  
   "LastRollUp":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "OpCodeOpDesc":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "RestrictionTypeDescription":string,
   "VendorNumAddress2":string,
   "VendorNumZIP":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress1":string,
   "VendorNumName":string,
   "VendorNumAddress3":string,
   "VendorNumState":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param checkManual
      @param ds
   */  
export interface ChangeManual_input{
      /**  Manual value  */  
   checkManual:boolean,
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}

export interface ChangeManual_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeRestrictionSubstance_input{
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}

export interface ChangeRestrictionSubstance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeRestrictionType_input{
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}

export interface ChangeRestrictionType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}
}

   /** Required : 
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
      @param restrictionTypeID
   */  
export interface DeleteByID_input{
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
   restrictionTypeID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtVendPartRestrictionTableset{
   VendPartRestriction:Erp_Tablesets_VendPartRestrictionRow[],
   VendPartRestrictSubst:Erp_Tablesets_VendPartRestrictSubstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendPartRestrictSubstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies our Part.  */  
   PartNum:string,
      /**   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  */  
   OpCode:string,
      /**   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  */  
   PUM:string,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  Substance identification.  */  
   SubstanceID:string,
      /**  Default weight of the substance per primary part of UOM  */  
   Weight:number,
      /**  By default the primary UOM of the part.  */  
   WeightUOM:string,
      /**  When true then weight is disregarded in compliance roll-up.  */  
   Manual:boolean,
      /**  The date when exempt status for this substance expires.  */  
   ExemptDate:string,
      /**  Optional. Exemption certificate.  */  
   ExemptCertificate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Exempt:boolean,
   BitFlag:number,
   OpCodeOpDesc:string,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   RestrictionTypeDescription:string,
   SubstanceDescription:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumZIP:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumName:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendPartRestrictionListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies our Part.  */  
   PartNum:string,
      /**   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  */  
   OpCode:string,
      /**   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  */  
   PUM:string,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  */  
   Manual:boolean,
      /**   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  */  
   RollUp:boolean,
      /**  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  */  
   Compliance:string,
      /**  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  */  
   ComplianceDate:string,
      /**  Set after compliance roll-up  */  
   LastRollUp:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpCodeOpDesc:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Restriction Type Description  */  
   RestrictionTypeDescription:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendPartRestrictionListTableset{
   VendPartRestrictionList:Erp_Tablesets_VendPartRestrictionListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendPartRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies our Part.  */  
   PartNum:string,
      /**   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  */  
   OpCode:string,
      /**   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  */  
   PUM:string,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  */  
   Manual:boolean,
      /**   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  */  
   RollUp:boolean,
      /**  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  */  
   Compliance:string,
      /**  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  */  
   ComplianceDate:string,
      /**  Set after compliance roll-up  */  
   LastRollUp:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   OpCodeOpDesc:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   RestrictionTypeDescription:string,
   VendorNumAddress2:string,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumAddress3:string,
   VendorNumState:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendPartRestrictionTableset{
   VendPartRestriction:Erp_Tablesets_VendPartRestrictionRow[],
   VendPartRestrictSubst:Erp_Tablesets_VendPartRestrictSubstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
      @param restrictionTypeID
   */  
export interface GetByID_input{
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
   restrictionTypeID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VendPartRestrictionTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VendPartRestrictionTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VendPartRestrictionTableset[],
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
   returnObj:Erp_Tablesets_VendPartRestrictionListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
      @param restrictionTypeID
   */  
export interface GetNewVendPartRestrictSubst_input{
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
   restrictionTypeID:string,
}

export interface GetNewVendPartRestrictSubst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
   */  
export interface GetNewVendPartRestriction_input{
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
}

export interface GetNewVendPartRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}
}

   /** Required : 
      @param whereClauseVendPartRestriction
      @param whereClauseVendPartRestrictSubst
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseVendPartRestriction:string,
   whereClauseVendPartRestrictSubst:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VendPartRestrictionTableset[],
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
      @param checkRestrictionTypeID
      @param ds
   */  
export interface OnChangingRestrictionType_input{
      /**  RestrictionTypeID value  */  
   checkRestrictionTypeID:string,
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}

export interface OnChangingRestrictionType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtVendPartRestrictionTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVendPartRestrictionTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartRestrictionTableset[],
}
}

