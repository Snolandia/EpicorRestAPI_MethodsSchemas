import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TransOrderReceiptSvc
// Description: Dataset to receive items shipped to another plant using Transfer Order Shipment Process
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/$metadata", {
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
   Description: Get TransOrderReceipts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransOrderReceipts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadRow
   */  
export function get_TransOrderReceipts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransOrderReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransOrderReceipts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts", {
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
   Summary: Calls GetByID to retrieve the TransOrderReceipt item
   Description: Calls GetByID to retrieve the TransOrderReceipt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransOrderReceipt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   */  
export function get_TransOrderReceipts_Company_PackNum(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TransOrderReceipt for the service
   Description: Calls UpdateExt to update TransOrderReceipt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransOrderReceipt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TransOrderReceipts_Company_PackNum(Company:string, PackNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")", {
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
   Summary: Call UpdateExt to delete TransOrderReceipt item
   Description: Call UpdateExt to delete TransOrderReceipt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransOrderReceipt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TransOrderReceipts_Company_PackNum(Company:string, PackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")", {
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
   Description: Get TFShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   */  
export function get_TransOrderReceipts_Company_PackNum_TFShipDtls(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")/TFShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   */  
export function get_TransOrderReceipts_Company_PackNum_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TFShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   */  
export function get_TFShipDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFShipDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls", {
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
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   */  
export function get_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFShipDtl for the service
   Description: Calls UpdateExt to update TFShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete TFShipDtl item
   Description: Call UpdateExt to delete TFShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Description: Get PlantTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantTrans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranRow
   */  
export function get_TFShipDtls_Company_PackNum_PackLine_PlantTrans(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/PlantTrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantTran item
   Description: Calls GetByID to retrieve the PlantTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantTran1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   */  
export function get_TFShipDtls_Company_PackNum_PackLine_PlantTrans_Company_TranNum(Company:string, PackNum:string, PackLine:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/PlantTrans(" + Company + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PlantTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranRow
   */  
export function get_PlantTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantTrans(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans", {
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
   Summary: Calls GetByID to retrieve the PlantTran item
   Description: Calls GetByID to retrieve the PlantTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   */  
export function get_PlantTrans_Company_TranNum(Company:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans(" + Company + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantTran for the service
   Description: Calls UpdateExt to update PlantTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantTrans_Company_TranNum(Company:string, TranNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans(" + Company + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete PlantTran item
   Description: Call UpdateExt to delete PlantTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantTrans_Company_TranNum(Company:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans(" + Company + "," + TranNum + ")", {
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
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts", {
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
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers", {
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
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SNFormats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats", {
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
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow)
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
export function get_GetRows(whereClauseTFShipHead:string, whereClauseTFShipDtl:string, whereClausePlantTran:string, whereClauseLegalNumGenOpts:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTFShipHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipHead=" + whereClauseTFShipHead
   }
   if(typeof whereClauseTFShipDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipDtl=" + whereClauseTFShipDtl
   }
   if(typeof whereClausePlantTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantTran=" + whereClausePlantTran
   }
   if(typeof whereClauseLegalNumGenOpts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   }
   if(typeof whereClauseSelectedSerialNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   }
   if(typeof whereClauseSNFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNFormat=" + whereClauseSNFormat
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(packNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetList" + params, {
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
   Summary: Invoke method ChangePlantTranAssemblySeq
   Description: This methods updates fields associated with PlantTran.AssemblySeq field.
This method should run when the PlantTran.AssemblySeq field changes.
   OperationID: ChangePlantTranAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantTranAssemblySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/ChangePlantTranAssemblySeq", {
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
   Summary: Invoke method ChangePlantTranJobMtl
   Description: This methods assigns fields associated with PlantTran.JobMtl changing.
This method should run before the PlantTran.JobMtl field changes.
   OperationID: ChangePlantTranJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantTranJobMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/ChangePlantTranJobMtl", {
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
   Summary: Invoke method ChangePlantTranJobNum
   Description: This methods assigns fields associated with PlantTran.JobNum changing.
This method should run before the PlantTran.JobNum field changes.
   OperationID: ChangePlantTranJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantTranJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/ChangePlantTranJobNum", {
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
   Summary: Invoke method ChangePlantTranReceivedTo
   Description: This methods updates fields associated with PlantTran.ReceiveTo field.
This method should run when the PlantTran.ReceiveTo field changes.
   OperationID: ChangePlantTranReceivedTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranReceivedTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranReceivedTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantTranReceivedTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/ChangePlantTranReceivedTo", {
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
   Summary: Invoke method ChangePlantTranReceivedToBinNum
   Description: This methods changes the BinNumDescription when changing the PlantTran.BinNum
This method should run before the PlantTran.BinNum field changes.
   OperationID: ChangePlantTranReceivedToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranReceivedToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranReceivedToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantTranReceivedToBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/ChangePlantTranReceivedToBinNum", {
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
   Summary: Invoke method ChangePlantTranReceivedToWhseCode
   Description: This methods changes the ReceiveToBinNum when changing the PlantTran.ReceiveToWhseCode
This method should run before the PlantTran.ReceiveToWhseCode field changes.
   OperationID: ChangePlantTranReceivedToWhseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranReceivedToWhseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranReceivedToWhseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantTranReceivedToWhseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/ChangePlantTranReceivedToWhseCode", {
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
   Summary: Invoke method CheckPlantTranJobMtl
   Description: This methods validates the JobMtl when changing the PlantTran.JobMtl
This method should run before the PlantTran.JobMtl field changes.
   OperationID: CheckPlantTranJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlantTranJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlantTranJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPlantTranJobMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/CheckPlantTranJobMtl", {
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
   Summary: Invoke method CheckPlantTranJobNum
   Description: This methods validates the JobNum when changing the PlantTran.JobNum
This method should run before the PlantTran.JobNum field changes.
   OperationID: CheckPlantTranJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlantTranJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlantTranJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPlantTranJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/CheckPlantTranJobNum", {
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
   Summary: Invoke method CheckPlantTranReceivedToBinNum
   Description: This methods validates the BinNum when changing the PlantTran.BinNum
This method should run before the PlantTran.BinNum field changes.
   OperationID: CheckPlantTranReceivedToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlantTranReceivedToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlantTranReceivedToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPlantTranReceivedToBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/CheckPlantTranReceivedToBinNum", {
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
   Summary: Invoke method CustomUpdate
   Description: This is a custom version of the standard Update method.
   OperationID: CustomUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/CustomUpdate", {
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
   Summary: Invoke method GetListBasicSearch
   Description: Returns the Transfer Orders as the GetList does but filtering them out by received or unreceived ones.
   OperationID: GetListBasicSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBasicSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBasicSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListBasicSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetListBasicSearch", {
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
   Summary: Invoke method GetListBasicSearchWhereClause
   Description: Returns the Transfer Orders as the GetListBasicSearch does after getting the receipt status from a where clause.
   OperationID: GetListBasicSearchWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBasicSearchWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBasicSearchWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListBasicSearchWhereClause(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetListBasicSearchWhereClause", {
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
   Summary: Invoke method GetRowsLandingPage
   Description: Returns all Transfer Orders filtered by ToPlant and set their TransStatusDescription.
   OperationID: GetRowsLandingPage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsLandingPage(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetRowsLandingPage", {
          method: 'post',
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
   Summary: Invoke method SetReceiptDates
   Description: Set or clear Receipt Date
   OperationID: SetReceiptDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReceiptDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReceiptDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetReceiptDates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SetReceiptDates", {
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
   Summary: Invoke method GetPartPlantPKs
   Description: Returns a string with the PartTranPKs list to send to the report screen.
   OperationID: GetPartPlantPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartPlantPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartPlantPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartPlantPKs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetPartPlantPKs", {
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
   Summary: Invoke method SetAllLinesSameWhseBin
   Description: Set the same warehouse bin for all the lines.
   OperationID: SetAllLinesSameWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAllLinesSameWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAllLinesSameWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetAllLinesSameWhseBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SetAllLinesSameWhseBin", {
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
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="attributeSetID"></param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipOrderNum">ipOrderNum</param><param name="ipOrderLine">ipOrderLine</param><param name="ipPackSlip">ipPackSlip</param><param name="ipPackSlipLine">ipPackSlipLine</param><param name="ipReceivedTo">ipReceivedTo</param><returns></returns>
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method GetTransferOrders
   Description: Returns the Transfer Orders as the GetRows does but filtering them out by received or unreceived ones.
   OperationID: GetTransferOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransferOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransferOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetTransferOrders", {
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
   Summary: Invoke method CheckPlanningContractBin
   Description: Method to check Contract bin.
   OperationID: CheckPlanningContractBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlanningContractBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlanningContractBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPlanningContractBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/CheckPlanningContractBin", {
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
   Summary: Invoke method PreReceiptPCID
   Description: This method will return true if ParentFromPCID has more that one child
   OperationID: PreReceiptPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreReceiptPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreReceiptPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreReceiptPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PreReceiptPCID", {
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
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PreUpdate", {
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
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/ValidateSN", {
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
   Summary: Invoke method GetNewTFShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetNewTFShipHead", {
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
   Summary: Invoke method GetNewTFShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetNewTFShipDtl", {
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
   Summary: Invoke method GetNewPlantTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetNewPlantTran", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantTranRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipHeadRow[],
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) the record was created.  */  
   "SysTime":number,
      /**  Unique ID  */  
   "TranNum":number,
      /**   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   "TranStatus":string,
      /**  Part Number that this transfer is for.  */  
   "PartNum":string,
      /**  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   "RevisionNum":string,
      /**  Site that the transfer is from.  */  
   "FromPlant":string,
      /**  Site that the transfer is to.  */  
   "ToPlant":string,
      /**  The Warehouse the part is being transferred From.  */  
   "FromWarehouseCode":string,
      /**  Identifies the "From" Bin location that this transfer affected.  */  
   "BinNum":string,
      /**  The Job that the material is being transferred from.  */  
   "FromJobNum":string,
      /**  The Job Assembly (zero for final assembly) that the material is being transferred from.  */  
   "FromAssemblySeq":number,
      /**  The Warehouse the part is being transferred To.  */  
   "WarehseCodeTo":string,
      /**  "To" Job Number that this transfer is associated with, if any.  */  
   "JobNum":string,
      /**  Assembly Sequence associated with the JobNum.  */  
   "AssemblySeq":number,
      /**  Sequence number of the specific Job Material record.  */  
   "JobMtl":number,
      /**  Transfer Quantity.  */  
   "TranQty":number,
      /**  Date of transaction.  */  
   "TranDate":string,
      /**  Unit of Measure.  */  
   "UM":string,
      /**  From Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Used to hold a short comment on the Site transfer.  */  
   "PlntTranReference":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  */  
   "EntryPerson":string,
      /**   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  */  
   "TranType":string,
      /**   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  */  
   "InternalPrice":number,
      /**  Pack ID  */  
   "PackNum":number,
      /**  System date at time that record was received.  */  
   "RecSysDate":string,
      /**  System Time (hr-min-sec) when transaction was received.  */  
   "RecSysTime":number,
      /**  date of receipt transaction.  */  
   "RecTranDate":string,
      /**  This field is set equal to the Login ID variable.  It cannot be overridden.  */  
   "RecEntryPerson":string,
      /**  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  */  
   "RecIssuedComplete":boolean,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlMtlBurUnitCost":number,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlUnitCost":number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltLbrUnitCost":number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltBurUnitCost":number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltSubUnitCost":number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlBurUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlMtlUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlLabUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlSubUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlBurdenUnitCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  PCID to receive from  */  
   "FromPCID":string,
      /**  PCID to receive to  */  
   "ToPCID":string,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
   "calcDimTranQty":number,
   "calcRequiredQty":number,
      /**  The generated legal number  */  
   "LegalNumber":string,
   "LegalNumberMessage":string,
      /**  Part tran record's primary key - for the later use in the report  */  
   "PartTranPKs":string,
   "ReceiveIssueComplete":boolean,
      /**  Where to receive item to? (Values:  Stock or Job)  */  
   "ReceiveTo":string,
      /**  The bin num to receive to.  */  
   "ReceiveToBinNum":string,
      /**  ReceiveToDescription  */  
   "ReceiveToDescription":string,
      /**  The warehouse code to receive to.  */  
   "ReceiveToWhseCode":string,
      /**  ReceiveToWhseDescription  */  
   "ReceiveToWhseDescription":string,
      /**  The required quantity  */  
   "RequiredQty":number,
   "SerialNumTranType":string,
   "SerialProcessing":boolean,
   "TFRequestedQty":number,
   "TFRequestedQtyUOM":string,
   "ThisInvtyUOM":string,
   "ThisTranQty":number,
      /**  Transaction Document Type ID  */  
   "TranDocTypeID":string,
      /**  Parent PCID to the FromPCID field.  */  
   "ParentFromPCID":string,
      /**  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  */  
   "SystemTranType":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "DimCodeDimCodeDescription":string,
   "PackNumName":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumAttrClassID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Number of digits in the serial number  */  
   "NumberOfDigits":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
   "SNFormat1":string,
      /**  Whether or not to have leading zeroes  */  
   "LeadingZeroes":boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
   "HasSerialNumbers":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PartPricePerCode":string,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartPartDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskMask":string,
   "SerialMaskExample":string,
   "SerialMaskDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   "Company":string,
      /**  SerialNumber  */  
   "SerialNumber":string,
      /**  Scrapped flag  */  
   "Scrapped":boolean,
      /**  Scrapped reason code  */  
   "ScrappedReasonCode":string,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Reference field  */  
   "Reference":string,
      /**  Reason code type = s  */  
   "ReasonCodeType":string,
      /**  Reason code description  */  
   "ReasonCodeDesc":string,
      /**  PartNumber  */  
   "PartNum":string,
      /**  Serial number prefix  */  
   "SNPrefix":string,
      /**  Base number used to create the serial number  */  
   "SNBaseNumber":string,
      /**  RowID of the source record for this serial number  */  
   "SourceRowID":string,
      /**  TransType of the record that created this serial number  */  
   "TransType":string,
      /**  True if this serial numbered part passed inspection  */  
   "PassedInspection":boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   "Deselected":boolean,
   "KitWhseList":string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   "KBLbrAction":number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   "KBLbrActionDesc":string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   "PreventDeselect":boolean,
      /**  Used only by SN Assignment  */  
   "XRefPartNum":string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   "XRefPartType":string,
   "PreDeselected":boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   "poLinkValues":string,
      /**  The mask the was used to generate the serial number  */  
   "SNMask":string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   "NotSavedToDB":boolean,
   "RowSelected":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFShipDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**  Number of Packages  */  
   "Packages":number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   "PartNum":string,
      /**  Line Description  */  
   "LineDesc":string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   "IUM":string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   "RevisionNum":string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   "ShipCmpl":boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   "UpdatedInventory":boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  */  
   "NetWeightUOM":string,
      /**  Lot Number is defaulted as Job Number.  */  
   "LotNum":string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   "TotalNetWeight":number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   "WIPWarehouseCode":string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   "WIPBinNum":string,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "OurStockQty":number,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   "OurStockShippedQty":number,
      /**  requestdate  */  
   "requestdate":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  Unit price discount percent.  */  
   "DiscountPercent":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   "Discount":number,
      /**  A flat discount amount for the line item.  */  
   "DocDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Extended Price for the invoice line item.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  */  
   "DocExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Calculated price for the item being transferred.  */  
   "UnitPrice":number,
      /**  Unit Price.  */  
   "DocUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  */  
   "PickedAutoAllocatedQty":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  */  
   "AllocatedShippedQty":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Estimated Value  */  
   "MXEstValue":number,
      /**  Estimated Value Currency  */  
   "MXEstValueCurrencyCode":string,
      /**  Hazardous Shipment  */  
   "MXHazardousShipment":boolean,
      /**  Hazardous Type  */  
   "MXHazardousType":string,
      /**  Package Type  */  
   "MXPackageType":string,
      /**  Are there available serial numbers?  */  
   "AvailSerialNumbers":boolean,
      /**  direct-transfer  */  
   "direct_transfer":boolean,
      /**  OurStockShippedQty * DimConvFactor  */  
   "DisplayShipQty":number,
      /**  Indicates if the Shipment line has been shipped  */  
   "LineShipped":boolean,
      /**  Current Shipment in OrderUOM  */  
   "OrderShipmentQty":number,
      /**  UOM from Transfer Order  */  
   "OrderUOM":string,
      /**  Used by the freight web service  */  
   "PartAESExp":string,
      /**  Used by the freight web service  */  
   "PartECNNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicNumber":string,
      /**  used by freight web service  */  
   "PartExpLicType":string,
      /**  Used by the freight web service  */  
   "PartHazClass":string,
      /**  Used by the freight web service  */  
   "PartHazGvrnmtID":string,
      /**  Used by the freight web service  */  
   "PartHazItem":boolean,
      /**  Used by the freight web service  */  
   "PartHazPackInstr":string,
      /**  Used by the freight web service  */  
   "PartHazSub":string,
      /**  Used by the freight web service  */  
   "PartHazTechName":string,
      /**  Used by the freight web service  */  
   "PartHTS":string,
      /**  Used by the freight web service  */  
   "PartNAFTAOrigCountry":string,
      /**  Used by the freight web service  */  
   "PartNAFTAPref":string,
      /**  Used by the freight web service  */  
   "PartNAFTAProd":string,
      /**  Used by the freight web service  */  
   "PartOrigCountry":string,
      /**  Used by the freight web service  */  
   "PartSchedBcode":string,
      /**  Used by the freight web service  */  
   "PartUseHTSDesc":boolean,
      /**  Indicates if the Shipment line has been received  */  
   "Received":boolean,
      /**  The remaining quantity  */  
   "RemainingQty":number,
      /**  The request quantity  */  
   "RequestQty":number,
      /**  The shipped quantity  */  
   "ShippedQty":number,
      /**  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  */  
   "ShipStatus":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Enable Attribute Set Search  */  
   "EnableAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFShipHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External  ID  */  
   "ExternalID":string,
      /**  directtransfer  */  
   "directtransfer":boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Package Code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Third address line  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountryNum":number,
      /**  Payer Bill To Third Address line  */  
   "PayBTAddress3":string,
      /**  Payer Bill To Country Number  */  
   "PayBTCountryNum":number,
      /**  Payer Bill To Phone Number  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   "WarehouseCode":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Display for the Ship From Address  */  
   "DspFromAddr":string,
      /**  Display for the Ship To Address  */  
   "DspShipAddr":string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   "TranStatus":string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   "TranStatusDescription":string,
      /**  Carton Height  */  
   "CartonHeight":number,
      /**  Carton length  */  
   "CartonLength":number,
      /**  Carton Width  */  
   "CartonWidth":number,
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   "CartonContentValue":number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   "LastCartonFlag":boolean,
      /**  Carton Stage number.  */  
   "CartonStageNbr":string,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   "EnableShipped":boolean,
      /**  Translated field of ShipStatus  */  
   "SlipStatus":string,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   "EnableWeight":boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Zero indicates the length is enabled.  */  
   "PkgLenEnable":number,
      /**  Zero indicates the width is enabled.  */  
   "PkgWidthEnable":number,
      /**  1 = disable / 0 = enable  */  
   "PkgSizeUOMEnable":number,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   "CalcPSPrices":boolean,
      /**  Indicates if the transaction document type is available for input  */  
   "EnableTranDocType":boolean,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  Full description for the shipping company (carrier).  */  
   "FreightedShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "FreightedShipViaCodeWebDesc":string,
      /**  Full description of the Packaging Classification.  */  
   "PackClssDescription":string,
      /**  Full description of Packing Code.  */  
   "PackingDescription":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaWebDesc":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFShipHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External  ID  */  
   "ExternalID":string,
      /**  directtransfer  */  
   "directtransfer":boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Package Code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Third address line  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountryNum":number,
      /**  Payer Bill To Third Address line  */  
   "PayBTAddress3":string,
      /**  Payer Bill To Country Number  */  
   "PayBTCountryNum":number,
      /**  Payer Bill To Phone Number  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   "WarehouseCode":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAuthorizationCode  */  
   "AGAuthorizationCode":string,
      /**  AGAuthorizationDate  */  
   "AGAuthorizationDate":string,
      /**  AGCarrierCUIT  */  
   "AGCarrierCUIT":string,
      /**  AGDocumentLetter  */  
   "AGDocumentLetter":string,
      /**  AGInvoicingPoint  */  
   "AGInvoicingPoint":string,
      /**  AGLegalNumber  */  
   "AGLegalNumber":string,
      /**  AGPrintingControlType  */  
   "AGPrintingControlType":string,
      /**  AGTrackLicense  */  
   "AGTrackLicense":string,
      /**  AGShippingWay  */  
   "AGShippingWay":string,
      /**  AGCOTMark  */  
   "AGCOTMark":boolean,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  DigitalSignature  */  
   "DigitalSignature":string,
      /**  SignedOn  */  
   "SignedOn":string,
      /**  SignedBy  */  
   "SignedBy":string,
      /**  FirstPrintDate  */  
   "FirstPrintDate":string,
      /**  DocCopyNum  */  
   "DocCopyNum":number,
      /**  Creation date and time  */  
   "MXCertifiedTimestamp":string,
      /**  Certificate Serial Number  */  
   "MXCertificateSN":string,
      /**  Certificate  */  
   "MXCertificate":string,
      /**  Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  SAT Certificate Serial Number  */  
   "MXSATCertificateSN":string,
      /**  Digital Seal  */  
   "MXDigitalSeal":string,
      /**  SAT Seal  */  
   "MXSATSeal":string,
      /**  Original String  */  
   "MXOriginalString":string,
      /**  TFD Original String  */  
   "MXOriginalStringTFD":string,
      /**  Serie  */  
   "MXSerie":string,
      /**  Folio  */  
   "MXFolio":string,
      /**  Estimated Date and Time of Departure  */  
   "MXETD":string,
      /**  Estimated Date and Time of Arrival  */  
   "MXETA":string,
      /**  Distance in Km  */  
   "MXDistance":number,
      /**  Permit Type  */  
   "MXPermitType":string,
      /**  Permit Number  */  
   "MXPermitNum":string,
      /**  Carta Porte Status  */  
   "MXCartaPorteStatus":string,
      /**  Vehicle License Plate  */  
   "VehicleLicensePlate":string,
      /**  Vehicle Type  */  
   "VehicleType":string,
      /**  Vehicle Year  */  
   "VehicleYear":number,
      /**  Driver  */  
   "DriverID":string,
      /**  MXCancelFiscalFolio  */  
   "MXCancelFiscalFolio":string,
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   "CartonContentValue":number,
      /**  Carton Height  */  
   "CartonHeight":number,
      /**  Carton length  */  
   "CartonLength":number,
      /**  Carton Stage number.  */  
   "CartonStageNbr":string,
      /**  Carton Width  */  
   "CartonWidth":number,
      /**  Display for the Ship From Address  */  
   "DspFromAddr":string,
      /**  Display for the Ship To Address  */  
   "DspShipAddr":string,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   "EnableShipped":boolean,
      /**  Indicates if the transaction document type is available for input  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   "EnableWeight":boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   "LastCartonFlag":boolean,
   "LegalNumberMessage":string,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Zero indicates the length is enabled.  */  
   "PkgLenEnable":number,
      /**  1 = disable / 0 = enable  */  
   "PkgSizeUOMEnable":number,
      /**  Zero indicates the width is enabled.  */  
   "PkgWidthEnable":number,
      /**  Translated field of ShipStatus  */  
   "SlipStatus":string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   "TranStatus":string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   "TranStatusDescription":string,
   "VNAccordingToDemand":string,
   "VNCarrier":string,
   "VNContractNumber":string,
   "VNDate":string,
   "VNFor":string,
   "VNFrom":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   "CalcPSPrices":boolean,
   "DspDigitalSignature":string,
   "QSUseBOL":boolean,
   "QSUseIntl":boolean,
   "QSUseCO":boolean,
      /**  PCID  */  
   "PCID":string,
      /**  Logical indicating if the package control functionality should be enabled.  */  
   "EnablePackageControl":boolean,
      /**  Transfer order number  */  
   "TFOrdNum":string,
      /**  Estimated Date of Arrival  */  
   "MXETADate":string,
      /**  Estimated Time of Arrival  */  
   "MXETATime":number,
      /**  Estimated Date of Departure  */  
   "MXETDDate":string,
      /**  Estimated Time of Departure  */  
   "MXETDTime":number,
   "EnablePhantom":boolean,
   "PhantomCasesExist":boolean,
   "BitFlag":number,
   "AGInvoicingPointDescription":string,
   "AGLegalNumCnfgDescription":string,
   "DeliveryTypeDescription":string,
   "FreightedShipViaCodeDescription":string,
   "FreightedShipViaCodeWebDesc":string,
   "PackClssDescription":string,
   "PackingDescription":string,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param TranNum
      @param ipProposedAssemblySeq
      @param ds
   */  
export interface ChangePlantTranAssemblySeq_input{
      /**  Transaction line to check  */  
   TranNum:number,
      /**  The new proposed PlantTran.AssemblySeq value  */  
   ipProposedAssemblySeq:number,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface ChangePlantTranAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param tranNum
      @param ds
   */  
export interface ChangePlantTranJobMtl_input{
      /**  Transaction line to check  */  
   tranNum:number,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface ChangePlantTranJobMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param tranNum
      @param ds
   */  
export interface ChangePlantTranJobNum_input{
      /**  Transaction line to check  */  
   tranNum:number,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface ChangePlantTranJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param tranNum
      @param ds
   */  
export interface ChangePlantTranReceivedToBinNum_input{
      /**  Transaction line to check  */  
   tranNum:number,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface ChangePlantTranReceivedToBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param tranNum
      @param ipProposedWhseCode
      @param ds
   */  
export interface ChangePlantTranReceivedToWhseCode_input{
      /**  Transaction line to check  */  
   tranNum:number,
      /**  The new proposed PlantTran.WhseCode value  */  
   ipProposedWhseCode:string,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface ChangePlantTranReceivedToWhseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param tranNum
      @param ipProposedReceiveTo
      @param ds
   */  
export interface ChangePlantTranReceivedTo_input{
      /**  Transaction line to check  */  
   tranNum:number,
      /**  The new proposed PlantTran.ReceiveTo value
            (values: STOCK or JOB)  */  
   ipProposedReceiveTo:string,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface ChangePlantTranReceivedTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CheckPlanningContractBin_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface CheckPlanningContractBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
   pcPCBinAction:string,
   pcPCBinMessage:string,
}
}

   /** Required : 
      @param tranNum
      @param ipProposedJobMtl
      @param ds
   */  
export interface CheckPlantTranJobMtl_input{
      /**  Transaction line to check  */  
   tranNum:number,
      /**  The new proposed PlantTran.JobMtl value  */  
   ipProposedJobMtl:number,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface CheckPlantTranJobMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param tranNum
      @param ipProposedJobNum
      @param ds
   */  
export interface CheckPlantTranJobNum_input{
      /**  Transaction line to check  */  
   tranNum:number,
      /**  The new proposed PlantTran.JobNum value  */  
   ipProposedJobNum:string,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface CheckPlantTranJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param tranNum
      @param ipProposedBinNum
      @param ds
   */  
export interface CheckPlantTranReceivedToBinNum_input{
      /**  Transaction line to check  */  
   tranNum:number,
      /**  The new proposed PlantTran.BinNum value  */  
   ipProposedBinNum:string,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface CheckPlantTranReceivedToBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CustomUpdate_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface CustomUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
   opLegalNumberMessage:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface DeleteByID_input{
   packNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) the record was created.  */  
   SysTime:number,
      /**  Unique ID  */  
   TranNum:number,
      /**   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   TranStatus:string,
      /**  Part Number that this transfer is for.  */  
   PartNum:string,
      /**  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Site that the transfer is from.  */  
   FromPlant:string,
      /**  Site that the transfer is to.  */  
   ToPlant:string,
      /**  The Warehouse the part is being transferred From.  */  
   FromWarehouseCode:string,
      /**  Identifies the "From" Bin location that this transfer affected.  */  
   BinNum:string,
      /**  The Job that the material is being transferred from.  */  
   FromJobNum:string,
      /**  The Job Assembly (zero for final assembly) that the material is being transferred from.  */  
   FromAssemblySeq:number,
      /**  The Warehouse the part is being transferred To.  */  
   WarehseCodeTo:string,
      /**  "To" Job Number that this transfer is associated with, if any.  */  
   JobNum:string,
      /**  Assembly Sequence associated with the JobNum.  */  
   AssemblySeq:number,
      /**  Sequence number of the specific Job Material record.  */  
   JobMtl:number,
      /**  Transfer Quantity.  */  
   TranQty:number,
      /**  Date of transaction.  */  
   TranDate:string,
      /**  Unit of Measure.  */  
   UM:string,
      /**  From Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Used to hold a short comment on the Site transfer.  */  
   PlntTranReference:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  */  
   EntryPerson:string,
      /**   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  */  
   TranType:string,
      /**   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  */  
   InternalPrice:number,
      /**  Pack ID  */  
   PackNum:number,
      /**  System date at time that record was received.  */  
   RecSysDate:string,
      /**  System Time (hr-min-sec) when transaction was received.  */  
   RecSysTime:number,
      /**  date of receipt transaction.  */  
   RecTranDate:string,
      /**  This field is set equal to the Login ID variable.  It cannot be overridden.  */  
   RecEntryPerson:string,
      /**  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  */  
   RecIssuedComplete:boolean,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlMtlBurUnitCost:number,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  PCID to receive from  */  
   FromPCID:string,
      /**  PCID to receive to  */  
   ToPCID:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
   calcDimTranQty:number,
   calcRequiredQty:number,
      /**  The generated legal number  */  
   LegalNumber:string,
   LegalNumberMessage:string,
      /**  Part tran record's primary key - for the later use in the report  */  
   PartTranPKs:string,
   ReceiveIssueComplete:boolean,
      /**  Where to receive item to? (Values:  Stock or Job)  */  
   ReceiveTo:string,
      /**  The bin num to receive to.  */  
   ReceiveToBinNum:string,
      /**  ReceiveToDescription  */  
   ReceiveToDescription:string,
      /**  The warehouse code to receive to.  */  
   ReceiveToWhseCode:string,
      /**  ReceiveToWhseDescription  */  
   ReceiveToWhseDescription:string,
      /**  The required quantity  */  
   RequiredQty:number,
   SerialNumTranType:string,
   SerialProcessing:boolean,
   TFRequestedQty:number,
   TFRequestedQtyUOM:string,
   ThisInvtyUOM:string,
   ThisTranQty:number,
      /**  Transaction Document Type ID  */  
   TranDocTypeID:string,
      /**  Parent PCID to the FromPCID field.  */  
   ParentFromPCID:string,
      /**  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  */  
   SystemTranType:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   DimCodeDimCodeDescription:string,
   PackNumName:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumAttrClassID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFShipDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  Number of Packages  */  
   Packages:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   PartNum:string,
      /**  Line Description  */  
   LineDesc:string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   IUM:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   ShipCmpl:boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   UpdatedInventory:boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  */  
   NetWeightUOM:string,
      /**  Lot Number is defaulted as Job Number.  */  
   LotNum:string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   TotalNetWeight:number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   WIPWarehouseCode:string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   WIPBinNum:string,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  requestdate  */  
   requestdate:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Unit price discount percent.  */  
   DiscountPercent:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   Discount:number,
      /**  A flat discount amount for the line item.  */  
   DocDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Extended Price for the invoice line item.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  */  
   DocExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Calculated price for the item being transferred.  */  
   UnitPrice:number,
      /**  Unit Price.  */  
   DocUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  */  
   PickedAutoAllocatedQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  */  
   AllocatedShippedQty:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Estimated Value  */  
   MXEstValue:number,
      /**  Estimated Value Currency  */  
   MXEstValueCurrencyCode:string,
      /**  Hazardous Shipment  */  
   MXHazardousShipment:boolean,
      /**  Hazardous Type  */  
   MXHazardousType:string,
      /**  Package Type  */  
   MXPackageType:string,
      /**  Are there available serial numbers?  */  
   AvailSerialNumbers:boolean,
      /**  direct-transfer  */  
   direct_transfer:boolean,
      /**  OurStockShippedQty * DimConvFactor  */  
   DisplayShipQty:number,
      /**  Indicates if the Shipment line has been shipped  */  
   LineShipped:boolean,
      /**  Current Shipment in OrderUOM  */  
   OrderShipmentQty:number,
      /**  UOM from Transfer Order  */  
   OrderUOM:string,
      /**  Used by the freight web service  */  
   PartAESExp:string,
      /**  Used by the freight web service  */  
   PartECNNumber:string,
      /**  Used by freight web service  */  
   PartExpLicNumber:string,
      /**  used by freight web service  */  
   PartExpLicType:string,
      /**  Used by the freight web service  */  
   PartHazClass:string,
      /**  Used by the freight web service  */  
   PartHazGvrnmtID:string,
      /**  Used by the freight web service  */  
   PartHazItem:boolean,
      /**  Used by the freight web service  */  
   PartHazPackInstr:string,
      /**  Used by the freight web service  */  
   PartHazSub:string,
      /**  Used by the freight web service  */  
   PartHazTechName:string,
      /**  Used by the freight web service  */  
   PartHTS:string,
      /**  Used by the freight web service  */  
   PartNAFTAOrigCountry:string,
      /**  Used by the freight web service  */  
   PartNAFTAPref:string,
      /**  Used by the freight web service  */  
   PartNAFTAProd:string,
      /**  Used by the freight web service  */  
   PartOrigCountry:string,
      /**  Used by the freight web service  */  
   PartSchedBcode:string,
      /**  Used by the freight web service  */  
   PartUseHTSDesc:boolean,
      /**  Indicates if the Shipment line has been received  */  
   Received:boolean,
      /**  The remaining quantity  */  
   RemainingQty:number,
      /**  The request quantity  */  
   RequestQty:number,
      /**  The shipped quantity  */  
   ShippedQty:number,
      /**  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  */  
   ShipStatus:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Enable Attribute Set Search  */  
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFShipHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External  ID  */  
   ExternalID:string,
      /**  directtransfer  */  
   directtransfer:boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Package Code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Third address line  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountryNum:number,
      /**  Payer Bill To Third Address line  */  
   PayBTAddress3:string,
      /**  Payer Bill To Country Number  */  
   PayBTCountryNum:number,
      /**  Payer Bill To Phone Number  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   WarehouseCode:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Display for the Ship From Address  */  
   DspFromAddr:string,
      /**  Display for the Ship To Address  */  
   DspShipAddr:string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   TranStatus:string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   TranStatusDescription:string,
      /**  Carton Height  */  
   CartonHeight:number,
      /**  Carton length  */  
   CartonLength:number,
      /**  Carton Width  */  
   CartonWidth:number,
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   CartonContentValue:number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   LastCartonFlag:boolean,
      /**  Carton Stage number.  */  
   CartonStageNbr:string,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   EnableShipped:boolean,
      /**  Translated field of ShipStatus  */  
   SlipStatus:string,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Zero indicates the length is enabled.  */  
   PkgLenEnable:number,
      /**  Zero indicates the width is enabled.  */  
   PkgWidthEnable:number,
      /**  1 = disable / 0 = enable  */  
   PkgSizeUOMEnable:number,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   HasLegNumCnfg:boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   CalcPSPrices:boolean,
      /**  Indicates if the transaction document type is available for input  */  
   EnableTranDocType:boolean,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  Full description for the shipping company (carrier).  */  
   FreightedShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   FreightedShipViaCodeWebDesc:string,
      /**  Full description of the Packaging Classification.  */  
   PackClssDescription:string,
      /**  Full description of Packing Code.  */  
   PackingDescription:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaWebDesc:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFShipHeadListTableset{
   TFShipHeadList:Erp_Tablesets_TFShipHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TFShipHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External  ID  */  
   ExternalID:string,
      /**  directtransfer  */  
   directtransfer:boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Package Code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Third address line  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountryNum:number,
      /**  Payer Bill To Third Address line  */  
   PayBTAddress3:string,
      /**  Payer Bill To Country Number  */  
   PayBTCountryNum:number,
      /**  Payer Bill To Phone Number  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   WarehouseCode:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGCarrierCUIT  */  
   AGCarrierCUIT:string,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  AGTrackLicense  */  
   AGTrackLicense:string,
      /**  AGShippingWay  */  
   AGShippingWay:string,
      /**  AGCOTMark  */  
   AGCOTMark:boolean,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
      /**  Creation date and time  */  
   MXCertifiedTimestamp:string,
      /**  Certificate Serial Number  */  
   MXCertificateSN:string,
      /**  Certificate  */  
   MXCertificate:string,
      /**  Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  SAT Certificate Serial Number  */  
   MXSATCertificateSN:string,
      /**  Digital Seal  */  
   MXDigitalSeal:string,
      /**  SAT Seal  */  
   MXSATSeal:string,
      /**  Original String  */  
   MXOriginalString:string,
      /**  TFD Original String  */  
   MXOriginalStringTFD:string,
      /**  Serie  */  
   MXSerie:string,
      /**  Folio  */  
   MXFolio:string,
      /**  Estimated Date and Time of Departure  */  
   MXETD:string,
      /**  Estimated Date and Time of Arrival  */  
   MXETA:string,
      /**  Distance in Km  */  
   MXDistance:number,
      /**  Permit Type  */  
   MXPermitType:string,
      /**  Permit Number  */  
   MXPermitNum:string,
      /**  Carta Porte Status  */  
   MXCartaPorteStatus:string,
      /**  Vehicle License Plate  */  
   VehicleLicensePlate:string,
      /**  Vehicle Type  */  
   VehicleType:string,
      /**  Vehicle Year  */  
   VehicleYear:number,
      /**  Driver  */  
   DriverID:string,
      /**  MXCancelFiscalFolio  */  
   MXCancelFiscalFolio:string,
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   CartonContentValue:number,
      /**  Carton Height  */  
   CartonHeight:number,
      /**  Carton length  */  
   CartonLength:number,
      /**  Carton Stage number.  */  
   CartonStageNbr:string,
      /**  Carton Width  */  
   CartonWidth:number,
      /**  Display for the Ship From Address  */  
   DspFromAddr:string,
      /**  Display for the Ship To Address  */  
   DspShipAddr:string,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   EnableShipped:boolean,
      /**  Indicates if the transaction document type is available for input  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   HasLegNumCnfg:boolean,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   LastCartonFlag:boolean,
   LegalNumberMessage:string,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Zero indicates the length is enabled.  */  
   PkgLenEnable:number,
      /**  1 = disable / 0 = enable  */  
   PkgSizeUOMEnable:number,
      /**  Zero indicates the width is enabled.  */  
   PkgWidthEnable:number,
      /**  Translated field of ShipStatus  */  
   SlipStatus:string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   TranStatus:string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   TranStatusDescription:string,
   VNAccordingToDemand:string,
   VNCarrier:string,
   VNContractNumber:string,
   VNDate:string,
   VNFor:string,
   VNFrom:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   CalcPSPrices:boolean,
   DspDigitalSignature:string,
   QSUseBOL:boolean,
   QSUseIntl:boolean,
   QSUseCO:boolean,
      /**  PCID  */  
   PCID:string,
      /**  Logical indicating if the package control functionality should be enabled.  */  
   EnablePackageControl:boolean,
      /**  Transfer order number  */  
   TFOrdNum:string,
      /**  Estimated Date of Arrival  */  
   MXETADate:string,
      /**  Estimated Time of Arrival  */  
   MXETATime:number,
      /**  Estimated Date of Departure  */  
   MXETDDate:string,
      /**  Estimated Time of Departure  */  
   MXETDTime:number,
   EnablePhantom:boolean,
   PhantomCasesExist:boolean,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   AGLegalNumCnfgDescription:string,
   DeliveryTypeDescription:string,
   FreightedShipViaCodeDescription:string,
   FreightedShipViaCodeWebDesc:string,
   PackClssDescription:string,
   PackingDescription:string,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TransOrderReceiptTableset{
   TFShipHead:Erp_Tablesets_TFShipHeadRow[],
   TFShipDtl:Erp_Tablesets_TFShipDtlRow[],
   PlantTran:Erp_Tablesets_PlantTranRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTransOrderReceiptTableset{
   TFShipHead:Erp_Tablesets_TFShipHeadRow[],
   TFShipDtl:Erp_Tablesets_TFShipDtlRow[],
   PlantTran:Erp_Tablesets_PlantTranRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param packNum
   */  
export interface GetByID_input{
   packNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TransOrderReceiptTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TransOrderReceiptTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TransOrderReceiptTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListBasicSearchWhereClause_input{
      /**  WhereClause containing the receipt status  */  
   whereClause:string,
      /**  Number of records to retrieve.  */  
   pageSize:number,
      /**  Page Number.  */  
   absolutePage:number,
}

export interface GetListBasicSearchWhereClause_output{
   returnObj:Erp_Tablesets_TFShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param Received
      @param pageSize
      @param absolutePage
      @param startsWith
   */  
export interface GetListBasicSearch_input{
      /**  Flag to specify if we want to return Received Transfer Orders, false to return the Unreceived ones.  */  
   Received:boolean,
      /**  Number of records to retrieve.  */  
   pageSize:number,
      /**  Page Number.  */  
   absolutePage:number,
      /**  Filter out PackNums lesser than this number.  */  
   startsWith:number,
}

export interface GetListBasicSearch_output{
   returnObj:Erp_Tablesets_TFShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   returnObj:Erp_Tablesets_TFShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPlantTran_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface GetNewPlantTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewTFShipDtl_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
   packNum:number,
}

export interface GetNewTFShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTFShipHead_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface GetNewTFShipHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetPartPlantPKs_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface GetPartPlantPKs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
   partTranPKs:string,
}
}

export interface GetRowsLandingPage_output{
   returnObj:Erp_Tablesets_TransOrderReceiptTableset[],
}

   /** Required : 
      @param whereClauseTFShipHead
      @param whereClauseTFShipDtl
      @param whereClausePlantTran
      @param whereClauseLegalNumGenOpts
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTFShipHead:string,
   whereClauseTFShipDtl:string,
   whereClausePlantTran:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TransOrderReceiptTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPartNum
      @param attributeSetID
      @param ipQuantity
      @param ipUOM
      @param ipOrderNum
      @param ipOrderLine
      @param ipPackSlip
      @param ipPackSlipLine
      @param ipReceivedTo
   */  
export interface GetSelectSerialNumbersParams_input{
   ipPartNum:string,
   attributeSetID:number,
   ipQuantity:number,
   ipUOM:string,
   ipOrderNum:string,
   ipOrderLine:number,
   ipPackSlip:number,
   ipPackSlipLine:number,
   ipReceivedTo:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param Received
      @param WhereClauseTFShipHead
      @param WhereClauseTFShipDtl
      @param WhereClausePlantTran
      @param WhereClauseLegalNumGenOpts
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param PageSize
      @param AbsolutePage
   */  
export interface GetTransferOrders_input{
      /**  Flag to specify if we want to return Received Transfer Orders, false to return the Unreceived ones.  */  
   Received:boolean,
      /**  Where clause to filter the TFShipHead table.  */  
   WhereClauseTFShipHead:string,
      /**  Where clause to filter the TFShipDtl table.  */  
   WhereClauseTFShipDtl:string,
      /**  Where clause to filter the PlantTran table.  */  
   WhereClausePlantTran:string,
      /**  Where clause to filter the LegalNumGenOpts table.  */  
   WhereClauseLegalNumGenOpts:string,
      /**  Where clause to filter the SelectedSerialNumbers table.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Where clause to filter the SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  Number of records to retrieve.  */  
   PageSize:number,
      /**  Page Number.  */  
   AbsolutePage:number,
}

export interface GetTransferOrders_output{
   returnObj:Erp_Tablesets_TransOrderReceiptTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
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
export interface PreReceiptPCID_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface PreReceiptPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
   RequiresAllChildPCIDUpdateInput:boolean,
   errorMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param tranNum
      @param ds
   */  
export interface SetAllLinesSameWhseBin_input{
      /**  Transaction number  */  
   tranNum:number,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface SetAllLinesSameWhseBin_output{
   returnObj:Erp_Tablesets_TransOrderReceiptTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param packNum
      @param setDate
      @param ds
   */  
export interface SetReceiptDates_input{
      /**  Current Pack  */  
   packNum:number,
      /**  Bool to set or clear the receipt date  */  
   setDate:boolean,
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface SetReceiptDates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTransOrderReceiptTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTransOrderReceiptTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderReceiptTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ipSerialNumber
   */  
export interface ValidateSN_input{
      /**  Part number to validate.  */  
   ipPartNum:string,
      /**  Serial number to validate.  */  
   ipSerialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   isVoided:boolean,
}
}

