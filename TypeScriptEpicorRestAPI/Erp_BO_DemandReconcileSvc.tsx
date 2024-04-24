import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DemandReconcileSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/$metadata", {
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
   Description: Get DemandReconciles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandReconciles
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandReconcileRow
   */  
export function get_DemandReconciles(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandReconciles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandReconciles(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles", {
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
   Summary: Calls GetByID to retrieve the DemandReconcile item
   Description: Calls GetByID to retrieve the DemandReconcile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandReconcile
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
   */  
export function get_DemandReconciles_Company_ReconcileNum(Company:string, ReconcileNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandReconcileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandReconcileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandReconcile for the service
   Description: Calls UpdateExt to update DemandReconcile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandReconcile
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandReconciles_Company_ReconcileNum(Company:string, ReconcileNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")", {
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
   Summary: Call UpdateExt to delete DemandReconcile item
   Description: Call UpdateExt to delete DemandReconcile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandReconcile
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandReconciles_Company_ReconcileNum(Company:string, ReconcileNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")", {
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
   Description: Get DemReconAdjusts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemReconAdjusts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconAdjustRow
   */  
export function get_DemandReconciles_Company_ReconcileNum_DemReconAdjusts(Company:string, ReconcileNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconAdjustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconAdjusts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconAdjustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemReconAdjust item
   Description: Calls GetByID to retrieve the DemReconAdjust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconAdjust1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   */  
export function get_DemandReconciles_Company_ReconcileNum_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company:string, ReconcileNum:string, SysDate:string, SysTime:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemReconAdjustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemReconAdjustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DemReconcileShipments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemReconcileShipments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconcileShipmentsRow
   */  
export function get_DemandReconciles_Company_ReconcileNum_DemReconcileShipments(Company:string, ReconcileNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconcileShipmentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconcileShipments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconcileShipmentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemReconcileShipment item
   Description: Calls GetByID to retrieve the DemReconcileShipment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconcileShipment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   */  
export function get_DemandReconciles_Company_ReconcileNum_DemReconcileShipments_Company_ReconcileNum_PackNum(Company:string, ReconcileNum:string, PackNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemReconcileShipmentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemReconcileShipmentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DemReconAdjusts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemReconAdjusts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconAdjustRow
   */  
export function get_DemReconAdjusts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconAdjustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconAdjustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemReconAdjusts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemReconAdjusts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts", {
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
   Summary: Calls GetByID to retrieve the DemReconAdjust item
   Description: Calls GetByID to retrieve the DemReconAdjust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconAdjust
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   */  
export function get_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company:string, ReconcileNum:string, SysDate:string, SysTime:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemReconAdjustRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemReconAdjustRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemReconAdjust for the service
   Description: Calls UpdateExt to update DemReconAdjust. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemReconAdjust
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company:string, ReconcileNum:string, SysDate:string, SysTime:string, TranNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete DemReconAdjust item
   Description: Call UpdateExt to delete DemReconAdjust item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemReconAdjust
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company:string, ReconcileNum:string, SysDate:string, SysTime:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
   Description: Get DemReconcileShipments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemReconcileShipments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconcileShipmentsRow
   */  
export function get_DemReconcileShipments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconcileShipmentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconcileShipmentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemReconcileShipments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemReconcileShipments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments", {
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
   Summary: Calls GetByID to retrieve the DemReconcileShipment item
   Description: Calls GetByID to retrieve the DemReconcileShipment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconcileShipment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   */  
export function get_DemReconcileShipments_Company_ReconcileNum_PackNum(Company:string, ReconcileNum:string, PackNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemReconcileShipmentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemReconcileShipmentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemReconcileShipment for the service
   Description: Calls UpdateExt to update DemReconcileShipment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemReconcileShipment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemReconcileShipments_Company_ReconcileNum_PackNum(Company:string, ReconcileNum:string, PackNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")", {
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
   Summary: Call UpdateExt to delete DemReconcileShipment item
   Description: Call UpdateExt to delete DemReconcileShipment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemReconcileShipment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReconcileNum Desc: ReconcileNum   Required: True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemReconcileShipments_Company_ReconcileNum_PackNum(Company:string, ReconcileNum:string, PackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandReconcileListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileListRow)
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
export function get_GetRows(whereClauseDemandReconcile:string, whereClauseDemReconAdjust:string, whereClauseDemReconcileShipments:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDemandReconcile!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandReconcile=" + whereClauseDemandReconcile
   }
   if(typeof whereClauseDemReconAdjust!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemReconAdjust=" + whereClauseDemReconAdjust
   }
   if(typeof whereClauseDemReconcileShipments!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemReconcileShipments=" + whereClauseDemReconcileShipments
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/GetRows" + params, {
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
export function get_GetByID(reconcileNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof reconcileNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reconcileNum=" + reconcileNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/GetList" + params, {
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
   Summary: Invoke method ChangeDRAdjustmentQty
   Description: Recalc Variance when the Adjustment Quantity changes.
   OperationID: ChangeDRAdjustmentQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRAdjustmentQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRAdjustmentQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRAdjustmentQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRAdjustmentQty", {
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
   Summary: Invoke method ChangeDRCustID
   Description: Used when the CustID field is being changed to a new value.
   OperationID: ChangeDRCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRCustID", {
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
   Summary: Invoke method ChangeDRDemandContract
   Description: Used when the DemandContract field is being changed to a new value.
   OperationID: ChangeDRDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRDemandContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRDemandContract", {
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
   Summary: Invoke method ChangeDRPartNum
   Description: Used when the PartNum field is being changed to a new value.
   OperationID: ChangeDRPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRPartNum", {
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
   Summary: Invoke method ChangeDRReconcileCUMMQty
   Description: Recalc Adjust Quantity when the Reconcile Quantity changes.
   OperationID: ChangeDRReconcileCUMMQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRReconcileCUMMQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRReconcileCUMMQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRReconcileCUMMQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRReconcileCUMMQty", {
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
   Summary: Invoke method ChangeDRReconcileStartCumQty
   Description: Recalc Adjust Quantity and set Company Cumulative Quantity when the Start Cumulative Quantity changes.
   OperationID: ChangeDRReconcileStartCumQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRReconcileStartCumQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRReconcileStartCumQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRReconcileStartCumQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRReconcileStartCumQty", {
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
   Summary: Invoke method ChangeDRShippedCUMMQty
   Description: Changed event of Company Cumulative Quantity field.
   OperationID: ChangeDRShippedCUMMQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRShippedCUMMQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRShippedCUMMQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRShippedCUMMQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRShippedCUMMQty", {
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
   Summary: Invoke method ChangeDRSReconcileQty
   Description: Updates the Reconcile Qty for the selected PackNum.
   OperationID: ChangeDRSReconcileQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRSReconcileQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRSReconcileQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRSReconcileQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRSReconcileQty", {
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
   Summary: Invoke method ChangeDRTPCUMMQty
   Description: Changed event of Trading Partner Quantity field.
   OperationID: ChangeDRTPCUMMQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRTPCUMMQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRTPCUMMQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDRTPCUMMQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/ChangeDRTPCUMMQty", {
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
   Summary: Invoke method CreateAdjustmentCredit
   OperationID: CreateAdjustmentCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateAdjustmentCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateAdjustmentCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateAdjustmentCredit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/CreateAdjustmentCredit", {
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
   Summary: Invoke method RestartCumInfo
   Description: Restart the cumulative info stored for the company. B
   OperationID: RestartCumInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RestartCumInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestartCumInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RestartCumInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/RestartCumInfo", {
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
   Summary: Invoke method GetRowsSearch
   Description: Returns Demand Reconcile records for search
   OperationID: GetRowsSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/GetRowsSearch", {
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
   Summary: Invoke method GetNewDemandReconcile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandReconcile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandReconcile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandReconcile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandReconcile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/GetNewDemandReconcile", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconAdjustRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemReconAdjustRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconcileShipmentsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemReconcileShipmentsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandReconcileListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandReconcileRow[],
}

export interface Erp_Tablesets_DemReconAdjustRow{
   "Company":string,
   "ReconcileNum":number,
   "TranNum":number,
   "SysDate":string,
   "SysTime":number,
   "TranQty":number,
   "TranDate":string,
   "DispSysTime":string,
   "IUM":string,
   "AvailPackNum":boolean,
   "InvoiceLine":number,
   "InvoiceNum":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemReconcileShipmentsRow{
   "Company":string,
   "ReconcileNum":number,
   "PackNum":number,
   "Invoiced":boolean,
   "ReadyToInvoice":boolean,
   "SellingInventoryShipQty":number,
   "SalesUM":string,
   "ShipDate":string,
      /**  The reconciled qty should be populated as the last shipped qty received in the inbound file for that specific packing slip.  */  
   "ReconcileQty":number,
   "ScheduleNumber":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandReconcileListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  */  
   "ReconcileNum":number,
      /**  The demand contract this reconcilliation is for.  */  
   "DemandContractNum":number,
      /**  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  The customers Purchase Order Number the reconcilliation is for.  */  
   "PONum":string,
      /**  The part number the reconcilliation is for.  */  
   "PartNum":string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  The ShipTo the reconcilliation is for.  */  
   "ShipToNum":string,
      /**  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  */  
   "ShippedCUMMQty":number,
      /**  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  */  
   "TPCUMMQty":number,
      /**  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  */  
   "ReconcileCUMMQty":number,
      /**  The date the ShippedCUMMQty field was last updated.  */  
   "ShippedCUMMDate":string,
      /**  The date the TPCUMMQty field was last updated.  */  
   "TPCUMMDate":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter01":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter02":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter03":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter04":string,
      /**  For Epicor Development Use Only  */  
   "DemandNumber01":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber02":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber03":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber04":number,
      /**  For Epicor Development Use Only  */  
   "DemandDate01":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate02":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate03":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate04":string,
      /**  For Epicor Development Use Only  */  
   "DemandLogical01":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical02":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical03":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical04":boolean,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   "TPLastShipmentID":number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   "TPLastShipmentQty":number,
      /**  The date when of the last shipment according to the trading partner information  */  
   "TPLastShipmentDate":string,
      /**  The current schedule number of the file where the cumulative info was received  */  
   "TPScheduleNumber":string,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   "CILastShipmentID":number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   "CILastShipmentQty":number,
      /**  The date when of the last shipment according to the trading partner information  */  
   "CILastShipmentDate":string,
      /**  Date when the Restart process is executed on this Reconcile record.  */  
   "RestartDate":string,
      /**  Last Schedule Number before restart Cumulative Information.  */  
   "RestartSchedNum":string,
      /**  PO Number that executed the Restart Cumulative Information process.  */  
   "RestartPONum":string,
      /**  Trading partner Last Master Pack.  */  
   "TPLastMasterPack":number,
      /**  Company Information Last Master Pack.  */  
   "CILastMasterPack":number,
      /**  Starting Cumulative Quantity.  */  
   "StartCumQty":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The UOM code that represents the unit of measure in which the quantity is expressed.  */  
   "DemandUOM":string,
   "AdjustmentQty":number,
      /**  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  */  
   "Variance":number,
      /**  The setting for reconciling cumulative shipping quantities.  */  
   "CUMMSetting":string,
      /**  The demand contract this reconcilliation is for.  */  
   "DemandContract":string,
      /**  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  */  
   "CustID":string,
      /**  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  */  
   "AllowDelete":boolean,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   "DemandContractDemandContract":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartIUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartTrackLots":boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartSalesUM":string,
      /**  Describes the Part.  */  
   "PartPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartTrackDimension":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandReconcileRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  */  
   "ReconcileNum":number,
      /**  The demand contract this reconcilliation is for.  */  
   "DemandContractNum":number,
      /**  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  The customers Purchase Order Number the reconcilliation is for.  */  
   "PONum":string,
      /**  The part number the reconcilliation is for.  */  
   "PartNum":string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  The ShipTo the reconcilliation is for.  */  
   "ShipToNum":string,
      /**  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  */  
   "ShippedCUMMQty":number,
      /**  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  */  
   "TPCUMMQty":number,
      /**  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  */  
   "ReconcileCUMMQty":number,
      /**  The date the ShippedCUMMQty field was last updated.  */  
   "ShippedCUMMDate":string,
      /**  The date the TPCUMMQty field was last updated.  */  
   "TPCUMMDate":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter01":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter02":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter03":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter04":string,
      /**  For Epicor Development Use Only  */  
   "DemandNumber01":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber02":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber03":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber04":number,
      /**  For Epicor Development Use Only  */  
   "DemandDate01":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate02":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate03":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate04":string,
      /**  For Epicor Development Use Only  */  
   "DemandLogical01":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical02":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical03":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical04":boolean,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   "TPLastShipmentID":number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   "TPLastShipmentQty":number,
      /**  The date when of the last shipment according to the trading partner information  */  
   "TPLastShipmentDate":string,
      /**  The current schedule number of the file where the cumulative info was received  */  
   "TPScheduleNumber":string,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   "CILastShipmentID":number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   "CILastShipmentQty":number,
      /**  The date when of the last shipment according to the trading partner information  */  
   "CILastShipmentDate":string,
      /**  Date when the Restart process is executed on this Reconcile record.  */  
   "RestartDate":string,
      /**  Last Schedule Number before restart Cumulative Information.  */  
   "RestartSchedNum":string,
      /**  PO Number that executed the Restart Cumulative Information process.  */  
   "RestartPONum":string,
      /**  Trading partner Last Master Pack.  */  
   "TPLastMasterPack":number,
      /**  Company Information Last Master Pack.  */  
   "CILastMasterPack":number,
      /**  Starting Cumulative Quantity.  */  
   "StartCumQty":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The UOM code that represents the unit of measure in which the quantity is expressed.  */  
   "DemandUOM":string,
   "AdjustmentQty":number,
      /**  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  */  
   "Variance":number,
      /**  The setting for reconciling cumulative shipping quantities.  */  
   "CUMMSetting":string,
      /**  The demand contract this reconcilliation is for.  */  
   "DemandContract":string,
      /**  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  */  
   "CustID":string,
      /**  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  */  
   "AllowDelete":boolean,
   "BitFlag":number,
   "CustomerCustID":string,
   "CustomerName":string,
   "CustomerBTName":string,
   "DemandContractDemandContract":string,
   "PartSellingFactor":number,
   "PartPricePerCode":string,
   "PartIUM":string,
   "PartSalesUM":string,
   "PartTrackLots":boolean,
   "PartPartDescription":string,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param proposedQty
      @param ds
   */  
export interface ChangeDRAdjustmentQty_input{
      /**  The proposed Adjustment Quantity  */  
   proposedQty:number,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRAdjustmentQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedCustID
      @param ds
   */  
export interface ChangeDRCustID_input{
      /**  The proposed Customer ID  */  
   proposedCustID:string,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedDemandContract
      @param ds
   */  
export interface ChangeDRDemandContract_input{
      /**  The proposed Demand Contract  */  
   proposedDemandContract:string,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRDemandContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedPartNum
      @param ds
   */  
export interface ChangeDRPartNum_input{
      /**  The proposed Part Number  */  
   proposedPartNum:string,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedQty
      @param ds
   */  
export interface ChangeDRReconcileCUMMQty_input{
      /**  The proposed Reconcile Quantity  */  
   proposedQty:number,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRReconcileCUMMQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedQty
      @param ds
   */  
export interface ChangeDRReconcileStartCumQty_input{
      /**  The proposed Start Cumulative Quantity  */  
   proposedQty:number,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRReconcileStartCumQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedQty
      @param ds
   */  
export interface ChangeDRSReconcileQty_input{
      /**  The proposed Reconcile Quantity  */  
   proposedQty:number,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRSReconcileQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedQty
      @param ds
   */  
export interface ChangeDRShippedCUMMQty_input{
      /**  The proposed Shipped Cumulative Quantity  */  
   proposedQty:number,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRShippedCUMMQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param proposedQty
      @param ds
   */  
export interface ChangeDRTPCUMMQty_input{
      /**  The proposed Trading Partner Cumulative Quantity  */  
   proposedQty:number,
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface ChangeDRTPCUMMQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param iReconcileNum
      @param iPackNum
      @param iTranNum
      @param iSysDate
      @param iSysTime
   */  
export interface CreateAdjustmentCredit_input{
   iReconcileNum:number,
   iPackNum:number,
   iTranNum:number,
   iSysDate:string,
   iSysTime:number,
}

export interface CreateAdjustmentCredit_output{
parameters : {
      /**  output parameters  */  
   iInvoiceNum:number,
   iInvoiceLine:number,
   opErrMsg:string,
}
}

   /** Required : 
      @param reconcileNum
   */  
export interface DeleteByID_input{
   reconcileNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DemReconAdjustRow{
   Company:string,
   ReconcileNum:number,
   TranNum:number,
   SysDate:string,
   SysTime:number,
   TranQty:number,
   TranDate:string,
   DispSysTime:string,
   IUM:string,
   AvailPackNum:boolean,
   InvoiceLine:number,
   InvoiceNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemReconcileShipmentsRow{
   Company:string,
   ReconcileNum:number,
   PackNum:number,
   Invoiced:boolean,
   ReadyToInvoice:boolean,
   SellingInventoryShipQty:number,
   SalesUM:string,
   ShipDate:string,
      /**  The reconciled qty should be populated as the last shipped qty received in the inbound file for that specific packing slip.  */  
   ReconcileQty:number,
   ScheduleNumber:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandReconcileListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  */  
   ReconcileNum:number,
      /**  The demand contract this reconcilliation is for.  */  
   DemandContractNum:number,
      /**  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The customers Purchase Order Number the reconcilliation is for.  */  
   PONum:string,
      /**  The part number the reconcilliation is for.  */  
   PartNum:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  The ShipTo the reconcilliation is for.  */  
   ShipToNum:string,
      /**  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  */  
   ShippedCUMMQty:number,
      /**  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  */  
   TPCUMMQty:number,
      /**  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  */  
   ReconcileCUMMQty:number,
      /**  The date the ShippedCUMMQty field was last updated.  */  
   ShippedCUMMDate:string,
      /**  The date the TPCUMMQty field was last updated.  */  
   TPCUMMDate:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter01:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter02:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter03:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter04:string,
      /**  For Epicor Development Use Only  */  
   DemandNumber01:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber02:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber03:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber04:number,
      /**  For Epicor Development Use Only  */  
   DemandDate01:string,
      /**  For Epicor Development Use Only  */  
   DemandDate02:string,
      /**  For Epicor Development Use Only  */  
   DemandDate03:string,
      /**  For Epicor Development Use Only  */  
   DemandDate04:string,
      /**  For Epicor Development Use Only  */  
   DemandLogical01:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical02:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical03:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical04:boolean,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   TPLastShipmentID:number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   TPLastShipmentQty:number,
      /**  The date when of the last shipment according to the trading partner information  */  
   TPLastShipmentDate:string,
      /**  The current schedule number of the file where the cumulative info was received  */  
   TPScheduleNumber:string,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   CILastShipmentID:number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   CILastShipmentQty:number,
      /**  The date when of the last shipment according to the trading partner information  */  
   CILastShipmentDate:string,
      /**  Date when the Restart process is executed on this Reconcile record.  */  
   RestartDate:string,
      /**  Last Schedule Number before restart Cumulative Information.  */  
   RestartSchedNum:string,
      /**  PO Number that executed the Restart Cumulative Information process.  */  
   RestartPONum:string,
      /**  Trading partner Last Master Pack.  */  
   TPLastMasterPack:number,
      /**  Company Information Last Master Pack.  */  
   CILastMasterPack:number,
      /**  Starting Cumulative Quantity.  */  
   StartCumQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The UOM code that represents the unit of measure in which the quantity is expressed.  */  
   DemandUOM:string,
   AdjustmentQty:number,
      /**  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  */  
   Variance:number,
      /**  The setting for reconciling cumulative shipping quantities.  */  
   CUMMSetting:string,
      /**  The demand contract this reconcilliation is for.  */  
   DemandContract:string,
      /**  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  */  
   CustID:string,
      /**  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  */  
   AllowDelete:boolean,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   DemandContractDemandContract:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartIUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartTrackLots:boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartSalesUM:string,
      /**  Describes the Part.  */  
   PartPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartTrackDimension:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandReconcileListTableset{
   DemandReconcileList:Erp_Tablesets_DemandReconcileListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandReconcileRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  */  
   ReconcileNum:number,
      /**  The demand contract this reconcilliation is for.  */  
   DemandContractNum:number,
      /**  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The customers Purchase Order Number the reconcilliation is for.  */  
   PONum:string,
      /**  The part number the reconcilliation is for.  */  
   PartNum:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  The ShipTo the reconcilliation is for.  */  
   ShipToNum:string,
      /**  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  */  
   ShippedCUMMQty:number,
      /**  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  */  
   TPCUMMQty:number,
      /**  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  */  
   ReconcileCUMMQty:number,
      /**  The date the ShippedCUMMQty field was last updated.  */  
   ShippedCUMMDate:string,
      /**  The date the TPCUMMQty field was last updated.  */  
   TPCUMMDate:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter01:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter02:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter03:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter04:string,
      /**  For Epicor Development Use Only  */  
   DemandNumber01:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber02:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber03:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber04:number,
      /**  For Epicor Development Use Only  */  
   DemandDate01:string,
      /**  For Epicor Development Use Only  */  
   DemandDate02:string,
      /**  For Epicor Development Use Only  */  
   DemandDate03:string,
      /**  For Epicor Development Use Only  */  
   DemandDate04:string,
      /**  For Epicor Development Use Only  */  
   DemandLogical01:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical02:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical03:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical04:boolean,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   TPLastShipmentID:number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   TPLastShipmentQty:number,
      /**  The date when of the last shipment according to the trading partner information  */  
   TPLastShipmentDate:string,
      /**  The current schedule number of the file where the cumulative info was received  */  
   TPScheduleNumber:string,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   CILastShipmentID:number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   CILastShipmentQty:number,
      /**  The date when of the last shipment according to the trading partner information  */  
   CILastShipmentDate:string,
      /**  Date when the Restart process is executed on this Reconcile record.  */  
   RestartDate:string,
      /**  Last Schedule Number before restart Cumulative Information.  */  
   RestartSchedNum:string,
      /**  PO Number that executed the Restart Cumulative Information process.  */  
   RestartPONum:string,
      /**  Trading partner Last Master Pack.  */  
   TPLastMasterPack:number,
      /**  Company Information Last Master Pack.  */  
   CILastMasterPack:number,
      /**  Starting Cumulative Quantity.  */  
   StartCumQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The UOM code that represents the unit of measure in which the quantity is expressed.  */  
   DemandUOM:string,
   AdjustmentQty:number,
      /**  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  */  
   Variance:number,
      /**  The setting for reconciling cumulative shipping quantities.  */  
   CUMMSetting:string,
      /**  The demand contract this reconcilliation is for.  */  
   DemandContract:string,
      /**  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  */  
   CustID:string,
      /**  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  */  
   AllowDelete:boolean,
   BitFlag:number,
   CustomerCustID:string,
   CustomerName:string,
   CustomerBTName:string,
   DemandContractDemandContract:string,
   PartSellingFactor:number,
   PartPricePerCode:string,
   PartIUM:string,
   PartSalesUM:string,
   PartTrackLots:boolean,
   PartPartDescription:string,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandReconcileTableset{
   DemandReconcile:Erp_Tablesets_DemandReconcileRow[],
   DemReconAdjust:Erp_Tablesets_DemReconAdjustRow[],
   DemReconcileShipments:Erp_Tablesets_DemReconcileShipmentsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtDemandReconcileTableset{
   DemandReconcile:Erp_Tablesets_DemandReconcileRow[],
   DemReconAdjust:Erp_Tablesets_DemReconAdjustRow[],
   DemReconcileShipments:Erp_Tablesets_DemReconcileShipmentsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param reconcileNum
   */  
export interface GetByID_input{
   reconcileNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DemandReconcileTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DemandReconcileTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DemandReconcileTableset[],
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
   returnObj:Erp_Tablesets_DemandReconcileListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDemandReconcile_input{
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface GetNewDemandReconcile_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsSearch_input{
      /**  Where clause  */  
   whereClause:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
}

export interface GetRowsSearch_output{
   returnObj:Erp_Tablesets_DemandReconcileTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseDemandReconcile
      @param whereClauseDemReconAdjust
      @param whereClauseDemReconcileShipments
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDemandReconcile:string,
   whereClauseDemReconAdjust:string,
   whereClauseDemReconcileShipments:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DemandReconcileTableset[],
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
      @param iReconcileNum
   */  
export interface RestartCumInfo_input{
      /**  Reconcile Number  */  
   iReconcileNum:number,
}

export interface RestartCumInfo_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDemandReconcileTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDemandReconcileTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DemandReconcileTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandReconcileTableset[],
}
}

