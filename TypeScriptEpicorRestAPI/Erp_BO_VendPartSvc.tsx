import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.VendPartSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/$metadata", {
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
   Description: Get VendParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendParts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRow
   */  
export function get_VendParts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts", {
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
   Summary: Calls GetByID to retrieve the VendPart item
   Description: Calls GetByID to retrieve the VendPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRow
   */  
export function get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendPart for the service
   Description: Calls UpdateExt to update VendPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")", {
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
   Summary: Call UpdateExt to delete VendPart item
   Description: Call UpdateExt to delete VendPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")", {
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
   Description: Get VendPBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPBrks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPBrkRow
   */  
export function get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPBrks(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendPBrk item
   Description: Calls GetByID to retrieve the VendPBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPBrk1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param BreakQty Desc: BreakQty   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   */  
export function get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, BreakQty:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VendPartAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPartAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartAttchRow
   */  
export function get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPartAttches(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPartAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VendPartAttch item
   Description: Calls GetByID to retrieve the VendPartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   */  
export function get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get VendPBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPBrks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPBrkRow
   */  
export function get_VendPBrks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendPBrks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks", {
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
   Summary: Calls GetByID to retrieve the VendPBrk item
   Description: Calls GetByID to retrieve the VendPBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param BreakQty Desc: BreakQty   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   */  
export function get_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, BreakQty:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendPBrk for the service
   Description: Calls UpdateExt to update VendPBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param BreakQty Desc: BreakQty   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, BreakQty:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")", {
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
   Summary: Call UpdateExt to delete VendPBrk item
   Description: Call UpdateExt to delete VendPBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param BreakQty Desc: BreakQty   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, BreakQty:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get VendPartAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPartAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartAttchRow
   */  
export function get_VendPartAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPartAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendPartAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches", {
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
   Summary: Calls GetByID to retrieve the VendPartAttch item
   Description: Calls GetByID to retrieve the VendPartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   */  
export function get_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendPartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendPartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendPartAttch for the service
   Description: Calls UpdateExt to update VendPartAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPartAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete VendPartAttch item
   Description: Call UpdateExt to delete VendPartAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPartAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param PUM Desc: PUM   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company:string, PartNum:string, OpCode:string, PUM:string, VendorNum:string, EffectiveDate:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseVendPart:string, whereClauseVendPartAttch:string, whereClauseVendPBrk:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseVendPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendPart=" + whereClauseVendPart
   }
   if(typeof whereClauseVendPartAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendPartAttch=" + whereClauseVendPartAttch
   }
   if(typeof whereClauseVendPBrk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendPBrk=" + whereClauseVendPBrk
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetRows" + params, {
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
export function get_GetByID(partNum:string, opCode:string, puM:string, vendorNum:string, effectiveDate:string, epicorHeaders?:Headers){
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
   if(typeof effectiveDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "effectiveDate=" + effectiveDate
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetList" + params, {
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
   Summary: Invoke method ChangeAprvSupplier
   OperationID: ChangeAprvSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAprvSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAprvSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAprvSupplier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangeAprvSupplier", {
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
   Summary: Invoke method ChangeConvOverride
   Description: This should be called on change of VendPart.ConvOverride
when false it will refresh the Conversion fields to UOM Master values.
   OperationID: ChangeConvOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConvOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConvOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConvOverride(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangeConvOverride", {
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
   Summary: Invoke method ChangeEffectiveDays
   Description: Method to call when changing the EffectiveDays, EffectiveDate, or ExpirationDate changes.
This method will recalculate the ExpirationDate if the EffectiveDate or EffectiveDays
change; it will recalculate the EffectiveDays if the ExpirationDate changes.
   OperationID: ChangeEffectiveDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEffectiveDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEffectiveDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEffectiveDays(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangeEffectiveDays", {
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
   Summary: Invoke method ChangeImportExportVendorID
   Description: This assigns the vendor name in the SupListImpExpParams datatable.
   OperationID: ChangeImportExportVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeImportExportVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeImportExportVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeImportExportVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangeImportExportVendorID", {
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
   Summary: Invoke method ChangePart
   Description: Run this method when Part Number on the detail screen changes (copied from SO)
   OperationID: ChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangePart", {
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
   Summary: Invoke method UpdateAprvSupplier
   OperationID: UpdateAprvSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAprvSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAprvSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAprvSupplier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/UpdateAprvSupplier", {
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
   Summary: Invoke method ChangePriceModifier
   Description: Method to call when changing the price modifier on the vendor part break record.
Recalculates the effective price based on the new price modifier.
   OperationID: ChangePriceModifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePriceModifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePriceModifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePriceModifier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangePriceModifier", {
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
   Summary: Invoke method ChangeVendPartPUM
   Description: This method creates a new ttVendPart record and deletes the existing one when
changing this component of the primary unique index and update the VendPart.PUM.
This method should run before changing the VendPart.PUM.
   OperationID: ChangeVendPartPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendPartPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPartPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendPartPUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangeVendPartPUM", {
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
   Summary: Invoke method ChangeConvOperator
   Description: This should be called on change of VendPart.ConvOperator
for recalculation of the ConvFactor
   OperationID: ChangeConvOperator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConvOperator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConvOperator_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConvOperator(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangeConvOperator", {
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
   Summary: Invoke method ChangeConvFactor
   Description: This should be called on change of VendPart.ConvFactor
for recalculation of the ConvFactor
   OperationID: ChangeConvFactor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConvFactor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConvFactor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConvFactor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ChangeConvFactor", {
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
   Summary: Invoke method GetDefaultRFQInfo
   Description: This method is called when the Supplier Price List object is called from
Supplier Response.  After a new VendPart record has been created, this method
needs to be called to default the specific RFQ information
   OperationID: GetDefaultRFQInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultRFQInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultRFQInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultRFQInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetDefaultRFQInfo", {
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
   Summary: Invoke method DefaultRFQInfo
   Description: This method is called when the Supplier Price List object is called from
Supplier Response.  After a new VendPart record has been created, this method
needs to be called to default the specific RFQ information
   OperationID: DefaultRFQInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultRFQInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultRFQInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultRFQInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/DefaultRFQInfo", {
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
   Summary: Invoke method ExportSupplierList
   Description: This method conditionally adds/overwrites supplier part records from an import file.
   OperationID: ExportSupplierList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSupplierList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSupplierList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportSupplierList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ExportSupplierList", {
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
   Summary: Invoke method ExportSupplierListToServerFile
   Description: This method conditionally adds/overwrites supplier part records from an import file.
   OperationID: ExportSupplierListToServerFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSupplierListToServerFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSupplierListToServerFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportSupplierListToServerFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ExportSupplierListToServerFile", {
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
   Summary: Invoke method GetImportSupplierListFromServerFile
   Description: This method loads supplier part records from an import file for reviewing/editing.
   OperationID: GetImportSupplierListFromServerFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetImportSupplierListFromServerFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetImportSupplierListFromServerFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetImportSupplierListFromServerFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetImportSupplierListFromServerFile", {
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
   Summary: Invoke method GetLastEffectiveVendPart
   Description: Method to get the last effective VendPart record.
   OperationID: GetLastEffectiveVendPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLastEffectiveVendPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLastEffectiveVendPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLastEffectiveVendPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetLastEffectiveVendPart", {
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
   Summary: Invoke method GetNewSupListImpExpParams
   Description: This method creates a record in SupListImpExpParams.  This record is used
to store the import/export parameters.
   OperationID: GetNewSupListImpExpParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSupListImpExpParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSupListImpExpParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSupListImpExpParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetNewSupListImpExpParams", {
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
   Summary: Invoke method GetVendorNum
   Description: Method to call get a VendorNum given a VendorID.
   OperationID: GetVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetVendorNum", {
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
   Summary: Invoke method GetPrimaryVendorNum
   Description: Method to get the Primary VendorNum given a PartNum.
   OperationID: GetPrimaryVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPrimaryVendorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetPrimaryVendorNum", {
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
   Summary: Invoke method GetVendPartByPart
   Description: Method to call to get the dataset based on a specific part.
   OperationID: GetVendPartByPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendPartByPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetVendPartByPart", {
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
   Summary: Invoke method GetVendPartByVendNumPart
   Description: Method to call to get the dataset based on a specific vendor and part.
   OperationID: GetVendPartByVendNumPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartByVendNumPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartByVendNumPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendPartByVendNumPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetVendPartByVendNumPart", {
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
   Summary: Invoke method GetVendPartByVendor
   Description: Method to call to get the dataset based on a specific vendor.
   OperationID: GetVendPartByVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartByVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartByVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendPartByVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetVendPartByVendor", {
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
   Summary: Invoke method ImportSupplierList
   Description: This method conditionally adds/overwrites supplier part records from an import file.
   OperationID: ImportSupplierList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportSupplierList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSupplierList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportSupplierList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/ImportSupplierList", {
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
   Summary: Invoke method GetVendPartIndexEffectiveRecord
   OperationID: GetVendPartIndexEffectiveRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartIndexEffectiveRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartIndexEffectiveRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendPartIndexEffectiveRecord(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetVendPartIndexEffectiveRecord", {
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
   Summary: Invoke method GetActiveParts
   OperationID: GetActiveParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActiveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActiveParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetActiveParts", {
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
   Summary: Invoke method GetNewVendPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetNewVendPart", {
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
   Summary: Invoke method GetNewVendPartAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPartAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPartAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPartAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendPartAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetNewVendPartAttch", {
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
   Summary: Invoke method GetNewVendPBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendPBrk(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetNewVendPBrk", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPBrkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPBrkRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPartAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPartListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendPartRow[],
}

export interface Erp_Tablesets_VendPBrkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies our Part.  */  
   "PartNum":string,
      /**   Operation Code - of the related parent VendPart record.
(See VendPart.OpCode).  */  
   "OpCode":string,
      /**  Purchasing Unit of measure.  A component of the unique key and parent table (VendPart) relationship.  */  
   "PUM":string,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  The date which this vendor/part information is effective.  */  
   "EffectiveDate":string,
      /**  Minimum Quantity required to obtain the related UnitPrice.  This is in Vendor's unit of measure.  */  
   "BreakQty":number,
      /**   This field represents the value used to determine a effective unit price for the related BreakQty.  It can be expressed as a Flat Amount or Percent of Base Price which is determined by the VendPart.PriceFormat field. Negatives are allowed to enter deductions to the base cost.
Effective Unit Price = BasePrice + PriceModifier  */  
   "PriceModifier":number,
      /**  Hours required is calculated as days * 8.  */  
   "DaysOut":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "EffectivePrice":number,
   "BitFlag":number,
   "OpCodeOpDesc":string,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "VendorNumDefaultFOB":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress3":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress2":string,
   "VendorNumName":string,
   "VendorNumCountry":string,
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendPartAttchRow{
   "Company":string,
   "PartNum":string,
   "OpCode":string,
   "PUM":string,
   "VendorNum":number,
   "EffectiveDate":string,
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

export interface Erp_Tablesets_VendPartListRow{
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
      /**  The date which this vendor/part information is effective.  */  
   "EffectiveDate":string,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "LeadTime":number,
      /**   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  */  
   "BaseUnitPrice":number,
      /**  Part number that the Vendor uses to identify the item.  */  
   "VenPartNum":string,
      /**  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  */  
   "PriceFormat":string,
      /**   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  */  
   "PricePerCode":string,
      /**   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  */  
   "MinimumPrice":number,
      /**  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  */  
   "ExpirationDate":string,
      /**  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  */  
   "Reference":string,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   "MiscAmt":number,
      /**  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  */  
   "MiscCode":string,
      /**  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  */  
   "CommentText":string,
      /**   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  */  
   "DiscountPercent":number,
      /**  Description of Part. Used only for Non Part master parts.  */  
   "PartDescription":string,
      /**   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  */  
   "RFQNum":number,
      /**   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  */  
   "RFQLine":number,
      /**   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  */  
   "CurrencyCode":string,
      /**  Suppliers Quantity on Hand  */  
   "OnhandQty":number,
      /**  Date Suppliers Quantity was updated  */  
   "OnHandDate":string,
      /**  Time Suppliers Quantity was updated  */  
   "OnHandTime":number,
      /**  Supplier contact linked to this Price  */  
   "ConNum":number,
      /**  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  */  
   "SupplierResponseReady":boolean,
      /**  Indicates if this Supplier Price List will be the default to select a PUM.  */  
   "DefaultPUM":boolean,
      /**   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  */  
   "ConvOperator":string,
      /**   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  */  
   "ConvFactor":number,
      /**  Purchase Point  */  
   "ConvOverRide":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OpCodeDescription":string,
   "VendorName":string,
   "CurrencyCodeDescription":string,
   "PrimaryVendor":boolean,
   "EffectiveDays":number,
   "VendorID":string,
      /**  RFQVend ID  */  
   "FromRFQ":string,
      /**  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  */  
   "NonPartMaster":boolean,
      /**  Approved Supplier  */  
   "AprvSupplier":boolean,
      /**  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  */  
   "AprvForACustomer":boolean,
      /**  Base UOM  */  
   "ConvBaseUOM":string,
      /**  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  */  
   "ConvFromUOM":string,
      /**  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  */  
   "ConvToUOM":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   "MiscCodeDescription":string,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   "MiscCodeLCDisburseMethod":string,
      /**  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  */  
   "MiscCodeLCAmount":number,
      /**  The Landed Cost Currency Code for this miscellaneous charge.  */  
   "MiscCodeLCCurrencyCode":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpCodeOpDesc":string,
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
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNameTermsCode":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNameCountry":string,
      /**  Second address line of the Supplier  */  
   "VendorNameAddress2":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNameName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNameVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNameAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNameCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNameState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNameZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNameAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNameCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNameDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendPartRow{
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
      /**  The date which this vendor/part information is effective.  */  
   "EffectiveDate":string,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "LeadTime":number,
      /**   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  */  
   "BaseUnitPrice":number,
      /**  Part number that the Vendor uses to identify the item.  */  
   "VenPartNum":string,
      /**  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  */  
   "PriceFormat":string,
      /**   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  */  
   "PricePerCode":string,
      /**   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  */  
   "MinimumPrice":number,
      /**  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  */  
   "ExpirationDate":string,
      /**  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  */  
   "Reference":string,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   "MiscAmt":number,
      /**  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  */  
   "MiscCode":string,
      /**  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  */  
   "CommentText":string,
      /**   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  */  
   "DiscountPercent":number,
      /**  Description of Part. Used only for Non Part master parts.  */  
   "PartDescription":string,
      /**   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  */  
   "RFQNum":number,
      /**   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  */  
   "RFQLine":number,
      /**   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  */  
   "CurrencyCode":string,
      /**  Suppliers Quantity on Hand  */  
   "OnhandQty":number,
      /**  Date Suppliers Quantity was updated  */  
   "OnHandDate":string,
      /**  Time Suppliers Quantity was updated  */  
   "OnHandTime":number,
      /**  Supplier contact linked to this Price  */  
   "ConNum":number,
      /**  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  */  
   "SupplierResponseReady":boolean,
      /**  Indicates if this Supplier Price List will be the default to select a PUM.  */  
   "DefaultPUM":boolean,
      /**   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  */  
   "ConvOperator":string,
      /**   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  */  
   "ConvFactor":number,
      /**  Purchase Point  */  
   "ConvOverRide":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OpCodeDescription":string,
   "VendorName":string,
   "CurrencyCodeDescription":string,
   "PrimaryVendor":boolean,
   "EffectiveDays":number,
   "VendorID":string,
      /**  RFQVend ID  */  
   "FromRFQ":string,
      /**  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  */  
   "NonPartMaster":boolean,
      /**  Approved Supplier  */  
   "AprvSupplier":boolean,
      /**  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  */  
   "AprvForACustomer":boolean,
      /**  Base UOM  */  
   "ConvBaseUOM":string,
      /**  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  */  
   "ConvFromUOM":string,
      /**  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  */  
   "ConvToUOM":string,
      /**  Supplier Part for a Supplier. This is used to assign a Supplier Part to a given Part row.  */  
   "VendSuppPart":string,
   "BitFlag":number,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "MiscCodeLCAmount":number,
   "MiscCodeLCDisburseMethod":string,
   "MiscCodeLCCurrencyCode":string,
   "MiscCodeDescription":string,
   "OpCodeOpDesc":string,
   "PartNumTrackDimension":boolean,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "VendorNameAddress3":string,
   "VendorNameVendorID":string,
   "VendorNameCity":string,
   "VendorNameAddress1":string,
   "VendorNameCurrencyCode":string,
   "VendorNameCountry":string,
   "VendorNameAddress2":string,
   "VendorNameName":string,
   "VendorNameZIP":string,
   "VendorNameTermsCode":string,
   "VendorNameState":string,
   "VendorNameDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
      @param ipAprvSupplier
   */  
export interface ChangeAprvSupplier_input{
   ds:Erp_Tablesets_VendPartTableset[],
      /**  Proposed part number  */  
   ipAprvSupplier:boolean,
}

export interface ChangeAprvSupplier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
   opExistApprovedSupplier:boolean,
}
}

   /** Required : 
      @param pConvFactor
      @param ds
   */  
export interface ChangeConvFactor_input{
      /**  Proposed value for ConvFactor  */  
   pConvFactor:number,
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface ChangeConvFactor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param pConvOperator
      @param ds
   */  
export interface ChangeConvOperator_input{
      /**  Proposed value for ConvOperator  */  
   pConvOperator:string,
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface ChangeConvOperator_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param pConvOverride
      @param ds
   */  
export interface ChangeConvOverride_input{
      /**  Proposed value for ConvOverride  */  
   pConvOverride:boolean,
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface ChangeConvOverride_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param ds
      @param cFieldModified
   */  
export interface ChangeEffectiveDays_input{
   ds:Erp_Tablesets_VendPartTableset[],
      /**  cFieldModified indicates which field was updated.  Possible values are:
            blank  - indicates we are just getting a value for days
            "days" - indicates the number of days changed; recalculate expiration date
            "eff"  - indicates effective date changed; recalculate expiration date
            "exp"  - indicates expiration date changed; recalculate effective date  */  
   cFieldModified:string,
}

export interface ChangeEffectiveDays_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param cProposedSupplierID
      @param ds
   */  
export interface ChangeImportExportVendorID_input{
   cProposedSupplierID:string,
   ds:Erp_Tablesets_SupListImpExpParamsTableset[],
}

export interface ChangeImportExportVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SupListImpExpParamsTableset[],
}
}

   /** Required : 
      @param partNum
      @param SysRowID
      @param rowType
      @param uomCode
      @param ds
   */  
export interface ChangePart_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface ChangePart_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePriceModifier_input{
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface ChangePriceModifier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param ds
      @param inPUM
   */  
export interface ChangeVendPartPUM_input{
   ds:Erp_Tablesets_VendPartTableset[],
      /**  Proposed PUM  */  
   inPUM:string,
}

export interface ChangeVendPartPUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param rfqRowIDent
   */  
export interface DefaultRFQInfo_input{
      /**  Supplier Response RowIDent  */  
   rfqRowIDent:string,
}

export interface DefaultRFQInfo_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
}

   /** Required : 
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
      @param effectiveDate
   */  
export interface DeleteByID_input{
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
   effectiveDate:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_SupListImpExpParamsRow{
   Company:string,
   EffectiveDate:string,
   VendorID:string,
   VendorName:string,
   FileName:string,
   VendorNum:number,
      /**  The delimiter to use in the CSV file.  */  
   ListSeparator:string,
      /**  The decimal separator used in numerics.  Either a comma(,) or a point(.).  */  
   NumberDecimalSeparator:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SupListImpExpParamsTableset{
   SupListImpExpParams:Erp_Tablesets_SupListImpExpParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SupplierListImportExportRow{
   Company:string,
   PartNum:string,
   PartDescription:string,
   VenPartNum:string,
   MinimumPrice:number,
   BaseUnitPrice:number,
   DiscountPercent:number,
   BreakQty:number,
   BreakPrice:number,
   PriceFormat:string,
   PricePerCode:string,
   LeadTime:number,
   PUM:string,
   Reference:string,
   CommentText:string,
      /**  Reason import of this record failed.  Blank implies no error occurred.  */  
   ImportErrorMsg:string,
   ImportSeq:number,
      /**  Manufacturer's ID  */  
   MfgID:string,
      /**  Manufacturer's Part Number.  */  
   MfgPartNum:string,
      /**  Supplier's Part Number.  */  
   SupplierPartNum:string,
      /**  Vendor's ID  */  
   VendorID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SupplierListImportExportTableset{
   SupplierListImportExport:Erp_Tablesets_SupplierListImportExportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtVendPartTableset{
   VendPart:Erp_Tablesets_VendPartRow[],
   VendPartAttch:Erp_Tablesets_VendPartAttchRow[],
   VendPBrk:Erp_Tablesets_VendPBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendPBrkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies our Part.  */  
   PartNum:string,
      /**   Operation Code - of the related parent VendPart record.
(See VendPart.OpCode).  */  
   OpCode:string,
      /**  Purchasing Unit of measure.  A component of the unique key and parent table (VendPart) relationship.  */  
   PUM:string,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  The date which this vendor/part information is effective.  */  
   EffectiveDate:string,
      /**  Minimum Quantity required to obtain the related UnitPrice.  This is in Vendor's unit of measure.  */  
   BreakQty:number,
      /**   This field represents the value used to determine a effective unit price for the related BreakQty.  It can be expressed as a Flat Amount or Percent of Base Price which is determined by the VendPart.PriceFormat field. Negatives are allowed to enter deductions to the base cost.
Effective Unit Price = BasePrice + PriceModifier  */  
   PriceModifier:number,
      /**  Hours required is calculated as days * 8.  */  
   DaysOut:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   EffectivePrice:number,
   BitFlag:number,
   OpCodeOpDesc:string,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   VendorNumDefaultFOB:string,
   VendorNumZIP:string,
   VendorNumCity:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress3:string,
   VendorNumTermsCode:string,
   VendorNumAddress2:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendPartAttchRow{
   Company:string,
   PartNum:string,
   OpCode:string,
   PUM:string,
   VendorNum:number,
   EffectiveDate:string,
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

export interface Erp_Tablesets_VendPartListRow{
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
      /**  The date which this vendor/part information is effective.  */  
   EffectiveDate:string,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   LeadTime:number,
      /**   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  */  
   BaseUnitPrice:number,
      /**  Part number that the Vendor uses to identify the item.  */  
   VenPartNum:string,
      /**  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  */  
   PriceFormat:string,
      /**   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  */  
   PricePerCode:string,
      /**   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  */  
   MinimumPrice:number,
      /**  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  */  
   ExpirationDate:string,
      /**  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  */  
   Reference:string,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  */  
   MiscCode:string,
      /**  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  */  
   CommentText:string,
      /**   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  */  
   DiscountPercent:number,
      /**  Description of Part. Used only for Non Part master parts.  */  
   PartDescription:string,
      /**   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  */  
   RFQNum:number,
      /**   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  */  
   RFQLine:number,
      /**   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  */  
   CurrencyCode:string,
      /**  Suppliers Quantity on Hand  */  
   OnhandQty:number,
      /**  Date Suppliers Quantity was updated  */  
   OnHandDate:string,
      /**  Time Suppliers Quantity was updated  */  
   OnHandTime:number,
      /**  Supplier contact linked to this Price  */  
   ConNum:number,
      /**  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  */  
   SupplierResponseReady:boolean,
      /**  Indicates if this Supplier Price List will be the default to select a PUM.  */  
   DefaultPUM:boolean,
      /**   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  */  
   ConvOperator:string,
      /**   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  */  
   ConvFactor:number,
      /**  Purchase Point  */  
   ConvOverRide:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OpCodeDescription:string,
   VendorName:string,
   CurrencyCodeDescription:string,
   PrimaryVendor:boolean,
   EffectiveDays:number,
   VendorID:string,
      /**  RFQVend ID  */  
   FromRFQ:string,
      /**  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  */  
   NonPartMaster:boolean,
      /**  Approved Supplier  */  
   AprvSupplier:boolean,
      /**  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  */  
   AprvForACustomer:boolean,
      /**  Base UOM  */  
   ConvBaseUOM:string,
      /**  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  */  
   ConvFromUOM:string,
      /**  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  */  
   ConvToUOM:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   MiscCodeDescription:string,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   MiscCodeLCDisburseMethod:string,
      /**  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  */  
   MiscCodeLCAmount:number,
      /**  The Landed Cost Currency Code for this miscellaneous charge.  */  
   MiscCodeLCCurrencyCode:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpCodeOpDesc:string,
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
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNameTermsCode:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNameCountry:string,
      /**  Second address line of the Supplier  */  
   VendorNameAddress2:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNameName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNameVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNameAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNameCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNameState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNameZIP:string,
      /**  First address line of the Supplier  */  
   VendorNameAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNameCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNameDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendPartListTableset{
   VendPartList:Erp_Tablesets_VendPartListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendPartRow{
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
      /**  The date which this vendor/part information is effective.  */  
   EffectiveDate:string,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   LeadTime:number,
      /**   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  */  
   BaseUnitPrice:number,
      /**  Part number that the Vendor uses to identify the item.  */  
   VenPartNum:string,
      /**  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  */  
   PriceFormat:string,
      /**   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  */  
   PricePerCode:string,
      /**   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  */  
   MinimumPrice:number,
      /**  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  */  
   ExpirationDate:string,
      /**  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  */  
   Reference:string,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  */  
   MiscCode:string,
      /**  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  */  
   CommentText:string,
      /**   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  */  
   DiscountPercent:number,
      /**  Description of Part. Used only for Non Part master parts.  */  
   PartDescription:string,
      /**   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  */  
   RFQNum:number,
      /**   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  */  
   RFQLine:number,
      /**   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  */  
   CurrencyCode:string,
      /**  Suppliers Quantity on Hand  */  
   OnhandQty:number,
      /**  Date Suppliers Quantity was updated  */  
   OnHandDate:string,
      /**  Time Suppliers Quantity was updated  */  
   OnHandTime:number,
      /**  Supplier contact linked to this Price  */  
   ConNum:number,
      /**  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  */  
   SupplierResponseReady:boolean,
      /**  Indicates if this Supplier Price List will be the default to select a PUM.  */  
   DefaultPUM:boolean,
      /**   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  */  
   ConvOperator:string,
      /**   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  */  
   ConvFactor:number,
      /**  Purchase Point  */  
   ConvOverRide:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OpCodeDescription:string,
   VendorName:string,
   CurrencyCodeDescription:string,
   PrimaryVendor:boolean,
   EffectiveDays:number,
   VendorID:string,
      /**  RFQVend ID  */  
   FromRFQ:string,
      /**  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  */  
   NonPartMaster:boolean,
      /**  Approved Supplier  */  
   AprvSupplier:boolean,
      /**  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  */  
   AprvForACustomer:boolean,
      /**  Base UOM  */  
   ConvBaseUOM:string,
      /**  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  */  
   ConvFromUOM:string,
      /**  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  */  
   ConvToUOM:string,
      /**  Supplier Part for a Supplier. This is used to assign a Supplier Part to a given Part row.  */  
   VendSuppPart:string,
   BitFlag:number,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   MiscCodeLCAmount:number,
   MiscCodeLCDisburseMethod:string,
   MiscCodeLCCurrencyCode:string,
   MiscCodeDescription:string,
   OpCodeOpDesc:string,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   VendorNameAddress3:string,
   VendorNameVendorID:string,
   VendorNameCity:string,
   VendorNameAddress1:string,
   VendorNameCurrencyCode:string,
   VendorNameCountry:string,
   VendorNameAddress2:string,
   VendorNameName:string,
   VendorNameZIP:string,
   VendorNameTermsCode:string,
   VendorNameState:string,
   VendorNameDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendPartTableset{
   VendPart:Erp_Tablesets_VendPartRow[],
   VendPartAttch:Erp_Tablesets_VendPartAttchRow[],
   VendPBrk:Erp_Tablesets_VendPBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param dsParams
      @param dtEffectiveDate
      @param cSupplierID
      @param serverFileName
   */  
export interface ExportSupplierListToServerFile_input{
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
   dsParams:Erp_Tablesets_SupListImpExpParamsTableset[],
      /**  Effective Date  */  
   dtEffectiveDate:string,
      /**  Supplier Code  */  
   cSupplierID:string,
   serverFileName:string,
}

export interface ExportSupplierListToServerFile_output{
      /**  returns the name of the saved file on the server  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
}
}

   /** Required : 
      @param ds
      @param dtEffectiveDate
      @param cSupplierID
   */  
export interface ExportSupplierList_input{
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
      /**  Effective Date  */  
   dtEffectiveDate:string,
      /**  Supplier Code  */  
   cSupplierID:string,
}

export interface ExportSupplierList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
}
}

   /** Required : 
      @param vendorNum
   */  
export interface GetActiveParts_input{
   vendorNum:number,
}

export interface GetActiveParts_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
}

   /** Required : 
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
      @param effectiveDate
   */  
export interface GetByID_input{
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
   effectiveDate:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
}

   /** Required : 
      @param ds
      @param rfqRowIDent
   */  
export interface GetDefaultRFQInfo_input{
   ds:Erp_Tablesets_VendPartTableset[],
      /**  Supplier Response RowIDent  */  
   rfqRowIDent:string,
}

export interface GetDefaultRFQInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param ds
      @param dsParams
      @param serverFileName
   */  
export interface GetImportSupplierListFromServerFile_input{
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
   dsParams:Erp_Tablesets_SupListImpExpParamsTableset[],
   serverFileName:string,
}

export interface GetImportSupplierListFromServerFile_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
}
}

   /** Required : 
      @param iVendorNum
      @param cPartNum
      @param cOpCode
      @param cPUM
      @param dtEffDate
   */  
export interface GetLastEffectiveVendPart_input{
      /**  The Vendor Number to retrieve the dataset for  */  
   iVendorNum:number,
      /**  The Part Number to retrieve the dataset for  */  
   cPartNum:string,
      /**  The OpCode to retrieve the dataset for  */  
   cOpCode:string,
      /**  The UOM to retrieve the dataset for  */  
   cPUM:string,
      /**  The Date to retrieve the dataset for  */  
   dtEffDate:string,
}

export interface GetLastEffectiveVendPart_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
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
   returnObj:Erp_Tablesets_VendPartListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param cSupplierID
   */  
export interface GetNewSupListImpExpParams_input{
   cSupplierID:string,
}

export interface GetNewSupListImpExpParams_output{
   returnObj:Erp_Tablesets_SupListImpExpParamsTableset[],
}

   /** Required : 
      @param ds
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
      @param effectiveDate
   */  
export interface GetNewVendPBrk_input{
   ds:Erp_Tablesets_VendPartTableset[],
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
   effectiveDate:string,
}

export interface GetNewVendPBrk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
      @param effectiveDate
   */  
export interface GetNewVendPartAttch_input{
   ds:Erp_Tablesets_VendPartTableset[],
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
   effectiveDate:string,
}

export interface GetNewVendPartAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
      @param opCode
      @param puM
      @param vendorNum
   */  
export interface GetNewVendPart_input{
   ds:Erp_Tablesets_VendPartTableset[],
   partNum:string,
   opCode:string,
   puM:string,
   vendorNum:number,
}

export interface GetNewVendPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param iPartNum
   */  
export interface GetPrimaryVendorNum_input{
      /**  Input: The part num  */  
   iPartNum:string,
}

export interface GetPrimaryVendorNum_output{
parameters : {
      /**  output parameters  */  
   oVendorNum:number,
}
}

   /** Required : 
      @param whereClauseVendPart
      @param whereClauseVendPartAttch
      @param whereClauseVendPBrk
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseVendPart:string,
   whereClauseVendPartAttch:string,
   whereClauseVendPBrk:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param cPartNum
   */  
export interface GetVendPartByPart_input{
      /**  The Part Number to retrieve the dataset for  */  
   cPartNum:string,
}

export interface GetVendPartByPart_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
}

   /** Required : 
      @param iVendorNum
      @param cPartNum
   */  
export interface GetVendPartByVendNumPart_input{
      /**  The Vendor Number to retrieve the dataset for  */  
   iVendorNum:number,
      /**  The Part Number to retrieve the dataset for  */  
   cPartNum:string,
}

export interface GetVendPartByVendNumPart_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
}

   /** Required : 
      @param VendNum
      @param ds
   */  
export interface GetVendPartByVendor_input{
   VendNum:number,
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface GetVendPartByVendor_output{
      /**  The VendPart data set  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param VendorNum
      @param PartNum
   */  
export interface GetVendPartIndexEffectiveRecord_input{
   VendorNum:number,
   PartNum:string,
}

export interface GetVendPartIndexEffectiveRecord_output{
   returnObj:Erp_Tablesets_VendPartTableset[],
parameters : {
      /**  output parameters  */  
   VendPartIndex:number,
}
}

   /** Required : 
      @param cVendorID
   */  
export interface GetVendorNum_input{
      /**  The Vendor ID  */  
   cVendorID:string,
}

export interface GetVendorNum_output{
parameters : {
      /**  output parameters  */  
   iVendorNum:number,
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
      @param dtEffectiveDate
      @param cSupplierID
   */  
export interface ImportSupplierList_input{
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
      /**  Effective Date  */  
   dtEffectiveDate:string,
      /**  Supplier Code  */  
   cSupplierID:string,
}

export interface ImportSupplierList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SupplierListImportExportTableset[],
   numRecsImported:number,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateAprvSupplier_input{
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface UpdateAprvSupplier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtVendPartTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVendPartTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VendPartTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendPartTableset[],
}
}

