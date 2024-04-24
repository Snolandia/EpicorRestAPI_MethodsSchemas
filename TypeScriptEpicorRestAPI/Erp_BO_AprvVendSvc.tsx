import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AprvVendSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/$metadata", {
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
   Description: Get AprvVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AprvVends
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AprvVendRow
   */  
export function get_AprvVends(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AprvVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AprvVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AprvVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AprvVends(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends", {
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
   Summary: Calls GetByID to retrieve the AprvVend item
   Description: Calls GetByID to retrieve the AprvVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AprvVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param APVType Desc: APVType   Required: True   Allow empty value : True
      @param ClassID Desc: ClassID   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AprvVendRow
   */  
export function get_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum(Company:string, VendorNum:string, PartNum:string, APVType:string, ClassID:string, OpCode:string, CustNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AprvVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AprvVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AprvVend for the service
   Description: Calls UpdateExt to update AprvVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AprvVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param APVType Desc: APVType   Required: True   Allow empty value : True
      @param ClassID Desc: ClassID   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AprvVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum(Company:string, VendorNum:string, PartNum:string, APVType:string, ClassID:string, OpCode:string, CustNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")", {
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
   Summary: Call UpdateExt to delete AprvVend item
   Description: Call UpdateExt to delete AprvVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AprvVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param APVType Desc: APVType   Required: True   Allow empty value : True
      @param ClassID Desc: ClassID   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum(Company:string, VendorNum:string, PartNum:string, APVType:string, ClassID:string, OpCode:string, CustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")", {
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
   Description: Get PartXRefVends items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartXRefVends1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param APVType Desc: APVType   Required: True   Allow empty value : True
      @param ClassID Desc: ClassID   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartXRefVendRow
   */  
export function get_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum_PartXRefVends(Company:string, VendorNum:string, PartNum:string, APVType:string, ClassID:string, OpCode:string, CustNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartXRefVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")/PartXRefVends", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartXRefVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartXRefVend item
   Description: Calls GetByID to retrieve the PartXRefVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartXRefVend1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param APVType Desc: APVType   Required: True   Allow empty value : True
      @param ClassID Desc: ClassID   Required: True   Allow empty value : True
      @param OpCode Desc: OpCode   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   */  
export function get_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company:string, VendorNum:string, PartNum:string, APVType:string, ClassID:string, OpCode:string, CustNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartXRefVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartXRefVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PartXRefVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartXRefVends
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartXRefVendRow
   */  
export function get_PartXRefVends(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartXRefVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartXRefVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartXRefVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartXRefVends(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends", {
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
   Summary: Calls GetByID to retrieve the PartXRefVend item
   Description: Calls GetByID to retrieve the PartXRefVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartXRefVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   */  
export function get_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company:string, PartNum:string, VendorNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartXRefVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartXRefVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartXRefVend for the service
   Description: Calls UpdateExt to update PartXRefVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartXRefVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company:string, PartNum:string, VendorNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
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
   Summary: Call UpdateExt to delete PartXRefVend item
   Description: Call UpdateExt to delete PartXRefVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartXRefVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company:string, PartNum:string, VendorNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AprvVendListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendListRow)
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
export function get_GetRows(whereClauseAprvVend:string, whereClausePartXRefVend:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAprvVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAprvVend=" + whereClauseAprvVend
   }
   if(typeof whereClausePartXRefVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartXRefVend=" + whereClausePartXRefVend
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, partNum:string, apVType:string, classID:string, opCode:string, custNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof apVType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "apVType=" + apVType
   }
   if(typeof classID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "classID=" + classID
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
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetList" + params, {
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
   Summary: Invoke method GetAprvData
   Description: .
   OperationID: GetAprvData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAprvData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAprvData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAprvData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetAprvData", {
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
   Summary: Invoke method GetListbyVendorName
   Description: Search suppliers by Vendor Name. Call normal GetList method.
   OperationID: GetListbyVendorName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListbyVendorName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListbyVendorName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListbyVendorName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetListbyVendorName", {
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
   Summary: Invoke method GetRowsForLandingPage
   Description: Search suppliers by Vendor Name. Method created to call from Kinetic because of incorrect/inconsistent parameter names in GetRowCustom.
   OperationID: Get_GetRowsForLandingPage
      @param whereClauseAprvVend Desc: Where Clause for AprvVend.   Required: True   Allow empty value : True
      @param whereClausePartXRefVend Desc: Where Clause for PartXRefVend.   Required: True   Allow empty value : True
      @param VendorID Desc: Vendor Name.   Required: True   Allow empty value : True
      @param pageSize Desc: Page size.   Required: True
      @param absolutePage Desc: Absolute page.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsForLandingPage(whereClauseAprvVend:string, whereClausePartXRefVend:string, VendorID:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAprvVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAprvVend=" + whereClauseAprvVend
   }
   if(typeof whereClausePartXRefVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartXRefVend=" + whereClausePartXRefVend
   }
   if(typeof VendorID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "VendorID=" + VendorID
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetRowsForLandingPage" + params, {
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
   Summary: Invoke method GetRowsCustom
   Description: Search suppliers by Vendor Name. Call normal GetList method.
   OperationID: Get_GetRowsCustom
      @param whereClauseAprvVend Desc: Where Clause for AprvVend.   Required: True   Allow empty value : True
      @param whereClausePartXRefVend Desc: Where Clause for PartXRefVend.   Required: True   Allow empty value : True
      @param PageSize Desc: Page size.   Required: True
      @param AbsolutePage Desc: Absolute page.   Required: True
      @param VendorID Desc: Vendor Name.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsCustom(whereClauseAprvVend:string, whereClausePartXRefVend:string, PageSize:string, AbsolutePage:string, VendorID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAprvVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAprvVend=" + whereClauseAprvVend
   }
   if(typeof whereClausePartXRefVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartXRefVend=" + whereClausePartXRefVend
   }
   if(typeof PageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "PageSize=" + PageSize
   }
   if(typeof AbsolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "AbsolutePage=" + AbsolutePage
   }
   if(typeof VendorID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "VendorID=" + VendorID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetRowsCustom" + params, {
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
   Summary: Invoke method OnChangeClassID
   Description: .
   OperationID: OnChangeClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeClassID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeClassID", {
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
   Summary: Invoke method OnChangeCustID
   Description: .
   OperationID: OnChangeCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeCustID", {
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
   Summary: Invoke method OnChangeCustNum
   Description: .
   OperationID: OnChangeCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCustNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeCustNum", {
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
   Summary: Invoke method OnChangeMfgNum
   Description: .
   OperationID: OnChangeMfgNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMfgNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeMfgNum", {
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
   Summary: Invoke method OnChangeMfgPartNum
   Description: .
   OperationID: OnChangeMfgPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMfgPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeMfgPartNum", {
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
   Summary: Invoke method OnChangeOpCode
   Description: .
   OperationID: OnChangeOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeOpCode", {
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
   Summary: Invoke method OnChangePartNum
   Description: .
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangePartNum", {
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
   Summary: Invoke method OnChangeVendorID
   Description: .
   OperationID: OnChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeVendorID", {
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
   Summary: Invoke method OnChangeVendorNum
   Description: .
   OperationID: OnChangeVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeVendorNum", {
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
   Summary: Invoke method OnChangeVendPartNum
   Description: Run when the PartXRefVend.VendPartNum is changing.
   OperationID: OnChangeVendPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/OnChangeVendPartNum", {
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
   Summary: Invoke method GetNewAprvVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAprvVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAprvVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAprvVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAprvVend(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetNewAprvVend", {
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
   Summary: Invoke method GetNewPartXRefVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartXRefVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartXRefVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartXRefVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartXRefVend(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetNewPartXRefVend", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AprvVendListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AprvVendRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartXRefVendRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartXRefVendRow[],
}

export interface Erp_Tablesets_AprvVendListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  "MTL" Material Suppliers or "Sub" Subcontractors.  */  
   "APVType":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  */  
   "ClassID":string,
      /**  The unique key  of the Parent Customer record for the ShipTo.  */  
   "CustNum":number,
      /**  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  */  
   "OpCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  APVTypeX  */  
   "APVTypeX":string,
   "CalledFrom":string,
      /**  Full description of the part class.  */  
   "ClassIDDescription":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpCodeOpDesc":string,
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
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
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
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AprvVendRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  "MTL" Material Suppliers or "Sub" Subcontractors.  */  
   "APVType":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  */  
   "ClassID":string,
      /**  The unique key  of the Parent Customer record for the ShipTo.  */  
   "CustNum":number,
      /**  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  */  
   "OpCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  APVTypeX  */  
   "APVTypeX":string,
   "CalledFrom":string,
   "BitFlag":number,
   "ClassIDDescription":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "OpCodeOpDesc":string,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumCountry":string,
   "VendorNumVendorID":string,
   "VendorNumAddress1":string,
   "VendorNumName":string,
   "VendorNumState":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumTermsCode":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartXRefVendRow{
      /**  Company  */  
   "Company":string,
      /**  PartNum  */  
   "PartNum":string,
      /**  VendNum  */  
   "VendorNum":number,
      /**  VendPartNum  */  
   "VendPartNum":string,
      /**  MfgNum  */  
   "MfgNum":number,
      /**  MfgPartNum  */  
   "MfgPartNum":string,
      /**  Reference  */  
   "Reference":string,
      /**  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  */  
   "LeadTime":number,
      /**  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  */  
   "PurchaseDefault":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Used to mantain relation with AprvVend.  */  
   "APVType":string,
      /**  Used to mantain relation with AprvVend.  */  
   "CustNum":number,
      /**  Used to mantain relation with AprvVend.  */  
   "ClassID":string,
      /**  Used to mantain relation with AprvVend.  */  
   "OpCode":string,
      /**  Lifecycle status description  */  
   "Description":string,
   "BitFlag":number,
   "MfgNumName":string,
   "MfgNumMfgID":string,
   "MfgPartNumLifecycleStatus":string,
   "MfgPartNumLeadTime":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param vendorNum
      @param partNum
      @param apVType
      @param classID
      @param opCode
      @param custNum
   */  
export interface DeleteByID_input{
   vendorNum:number,
   partNum:string,
   apVType:string,
   classID:string,
   opCode:string,
   custNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AprvVendListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  "MTL" Material Suppliers or "Sub" Subcontractors.  */  
   APVType:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  */  
   ClassID:string,
      /**  The unique key  of the Parent Customer record for the ShipTo.  */  
   CustNum:number,
      /**  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  */  
   OpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  APVTypeX  */  
   APVTypeX:string,
   CalledFrom:string,
      /**  Full description of the part class.  */  
   ClassIDDescription:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpCodeOpDesc:string,
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
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
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
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AprvVendListTableset{
   AprvVendList:Erp_Tablesets_AprvVendListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AprvVendRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  "MTL" Material Suppliers or "Sub" Subcontractors.  */  
   APVType:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  */  
   ClassID:string,
      /**  The unique key  of the Parent Customer record for the ShipTo.  */  
   CustNum:number,
      /**  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  */  
   OpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  APVTypeX  */  
   APVTypeX:string,
   CalledFrom:string,
   BitFlag:number,
   ClassIDDescription:string,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   OpCodeOpDesc:string,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
   VendorNumVendorID:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumState:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumTermsCode:string,
   VendorNumZIP:string,
   VendorNumCity:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AprvVendTableset{
   AprvVend:Erp_Tablesets_AprvVendRow[],
   PartXRefVend:Erp_Tablesets_PartXRefVendRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartXRefVendRow{
      /**  Company  */  
   Company:string,
      /**  PartNum  */  
   PartNum:string,
      /**  VendNum  */  
   VendorNum:number,
      /**  VendPartNum  */  
   VendPartNum:string,
      /**  MfgNum  */  
   MfgNum:number,
      /**  MfgPartNum  */  
   MfgPartNum:string,
      /**  Reference  */  
   Reference:string,
      /**  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  */  
   LeadTime:number,
      /**  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  */  
   PurchaseDefault:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Used to mantain relation with AprvVend.  */  
   APVType:string,
      /**  Used to mantain relation with AprvVend.  */  
   CustNum:number,
      /**  Used to mantain relation with AprvVend.  */  
   ClassID:string,
      /**  Used to mantain relation with AprvVend.  */  
   OpCode:string,
      /**  Lifecycle status description  */  
   Description:string,
   BitFlag:number,
   MfgNumName:string,
   MfgNumMfgID:string,
   MfgPartNumLifecycleStatus:string,
   MfgPartNumLeadTime:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAprvVendTableset{
   AprvVend:Erp_Tablesets_AprvVendRow[],
   PartXRefVend:Erp_Tablesets_PartXRefVendRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipCalledFrom
      @param whereClauze
   */  
export interface GetAprvData_input{
      /**  Called From  */  
   ipCalledFrom:string,
      /**  WhereClauze  */  
   whereClauze:string,
}

export interface GetAprvData_output{
   returnObj:Erp_Tablesets_AprvVendTableset[],
}

   /** Required : 
      @param vendorNum
      @param partNum
      @param apVType
      @param classID
      @param opCode
      @param custNum
   */  
export interface GetByID_input{
   vendorNum:number,
   partNum:string,
   apVType:string,
   classID:string,
   opCode:string,
   custNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AprvVendTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AprvVendTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AprvVendTableset[],
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
   returnObj:Erp_Tablesets_AprvVendListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param WhereClause
      @param PageSize
      @param AbsolutePage
      @param VendorName
   */  
export interface GetListbyVendorName_input{
      /**  Whereclause.  */  
   WhereClause:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
      /**  Vendor Name.  */  
   VendorName:string,
}

export interface GetListbyVendorName_output{
   returnObj:Erp_Tablesets_AprvVendListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param partNum
      @param apVType
      @param classID
      @param opCode
   */  
export interface GetNewAprvVend_input{
   ds:Erp_Tablesets_AprvVendTableset[],
   vendorNum:number,
   partNum:string,
   apVType:string,
   classID:string,
   opCode:string,
}

export interface GetNewAprvVend_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
      @param vendorNum
      @param vendPartNum
      @param mfgNum
   */  
export interface GetNewPartXRefVend_input{
   ds:Erp_Tablesets_AprvVendTableset[],
   partNum:string,
   vendorNum:number,
   vendPartNum:string,
   mfgNum:number,
}

export interface GetNewPartXRefVend_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param whereClauseAprvVend
      @param whereClausePartXRefVend
      @param PageSize
      @param AbsolutePage
      @param VendorID
   */  
export interface GetRowsCustom_input{
      /**  Where Clause for AprvVend.  */  
   whereClauseAprvVend:string,
      /**  Where Clause for PartXRefVend.  */  
   whereClausePartXRefVend:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
      /**  Vendor Name.  */  
   VendorID:string,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_AprvVendTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
}

   /** Required : 
      @param whereClauseAprvVend
      @param whereClausePartXRefVend
      @param VendorID
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForLandingPage_input{
      /**  Where Clause for AprvVend.  */  
   whereClauseAprvVend:string,
      /**  Where Clause for PartXRefVend.  */  
   whereClausePartXRefVend:string,
      /**  Vendor Name.  */  
   VendorID:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsForLandingPage_output{
   returnObj:Erp_Tablesets_AprvVendTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseAprvVend
      @param whereClausePartXRefVend
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAprvVend:string,
   whereClausePartXRefVend:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AprvVendTableset[],
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
      @param ipClassID
      @param ds
   */  
export interface OnChangeClassID_input{
      /**  The new value for VendorID.  */  
   ipClassID:string,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeClassID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipCustID
      @param ds
   */  
export interface OnChangeCustID_input{
      /**  The new value for VendorID.  */  
   ipCustID:string,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipCustNum
      @param ds
   */  
export interface OnChangeCustNum_input{
      /**  The new value for VendorID.  */  
   ipCustNum:number,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeCustNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipMfgNum
      @param ds
   */  
export interface OnChangeMfgNum_input{
      /**  The new value for VendorID.  */  
   ipMfgNum:number,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeMfgNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipMfgPartNum
      @param ds
   */  
export interface OnChangeMfgPartNum_input{
      /**  The new value for VendorID.  */  
   ipMfgPartNum:string,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeMfgPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipOpCode
      @param ds
   */  
export interface OnChangeOpCode_input{
      /**  The new value for VendorID.  */  
   ipOpCode:string,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeOpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  The new value for VendorID.  */  
   ipPartNum:string,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipVendPartNum
      @param ds
   */  
export interface OnChangeVendPartNum_input{
      /**  The new value for VendPartNum.  */  
   ipVendPartNum:string,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeVendPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipVendorID
      @param ds
   */  
export interface OnChangeVendorID_input{
      /**  The new value for VendorID.  */  
   ipVendorID:string,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ipVendorNum
      @param ds
   */  
export interface OnChangeVendorNum_input{
      /**  The new value for VendorID.  */  
   ipVendorNum:number,
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface OnChangeVendorNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAprvVendTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAprvVendTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AprvVendTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AprvVendTableset[],
}
}

