import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.WhseBinSvc
// Description: Warehouse Bin
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/$metadata", {
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
   Description: Get WhseBins items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseBins
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinRow
   */  
export function get_WhseBins(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseBinRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseBinRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhseBins(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins", {
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
   Summary: Calls GetByID to retrieve the WhseBin item
   Description: Calls GetByID to retrieve the WhseBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseBin
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseBinRow
   */  
export function get_WhseBins_Company_WarehouseCode_BinNum(Company:string, WarehouseCode:string, BinNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WhseBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WhseBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WhseBin for the service
   Description: Calls UpdateExt to update WhseBin. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseBin
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseBinRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WhseBins_Company_WarehouseCode_BinNum(Company:string, WarehouseCode:string, BinNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")", {
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
   Summary: Call UpdateExt to delete WhseBin item
   Description: Call UpdateExt to delete WhseBin item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseBin
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WhseBins_Company_WarehouseCode_BinNum(Company:string, WarehouseCode:string, BinNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")", {
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
   Description: Get WhseBinAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseBinAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinAttchRow
   */  
export function get_WhseBins_Company_WarehouseCode_BinNum_WhseBinAttches(Company:string, WarehouseCode:string, BinNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")/WhseBinAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WhseBinAttch item
   Description: Calls GetByID to retrieve the WhseBinAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseBinAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   */  
export function get_WhseBins_Company_WarehouseCode_BinNum_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company:string, WarehouseCode:string, BinNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WhseBinAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WhseBinAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get WhseBinAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseBinAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinAttchRow
   */  
export function get_WhseBinAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseBinAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhseBinAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches", {
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
   Summary: Calls GetByID to retrieve the WhseBinAttch item
   Description: Calls GetByID to retrieve the WhseBinAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseBinAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   */  
export function get_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company:string, WarehouseCode:string, BinNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WhseBinAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WhseBinAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WhseBinAttch for the service
   Description: Calls UpdateExt to update WhseBinAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseBinAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company:string, WarehouseCode:string, BinNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete WhseBinAttch item
   Description: Call UpdateExt to delete WhseBinAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseBinAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company:string, WarehouseCode:string, BinNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinListRow)
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
export function get_GetRows(whereClauseWhseBin:string, whereClauseWhseBinAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseWhseBin!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWhseBin=" + whereClauseWhseBin
   }
   if(typeof whereClauseWhseBinAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWhseBinAttch=" + whereClauseWhseBinAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(warehouseCode:string, binNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof warehouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warehouseCode=" + warehouseCode
   }
   if(typeof binNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "binNum=" + binNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GetList" + params, {
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
   Summary: Invoke method AddNewWhseBinFormat
   Description: Add a New record in WhseBinFormat table
   OperationID: AddNewWhseBinFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewWhseBinFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewWhseBinFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddNewWhseBinFormat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/AddNewWhseBinFormat", {
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
   Summary: Invoke method CommitGeneratedBins
   Description: Commit to database the proposed Bin Numbers selected
   OperationID: CommitGeneratedBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitGeneratedBins_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitGeneratedBins_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitGeneratedBins(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/CommitGeneratedBins", {
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
   Summary: Invoke method GenerateBinFormat
   Description: Generates the Bin format according to the segments defined
   OperationID: GenerateBinFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBinFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBinFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateBinFormat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GenerateBinFormat", {
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
   Summary: Invoke method GenerateBins
   Description: Create Bin numbers according to the specified format
   OperationID: GenerateBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBins_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBins_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateBins(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GenerateBins", {
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
   Description: OnChangeCustId
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangeCustID", {
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
   Summary: Invoke method InActiveFlag
   Description: OnChangeInActive
   OperationID: InActiveFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InActiveFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InActiveFlag(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/InActiveFlag", {
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
   Summary: Invoke method OnChangeSuppID
   Description: OnChangeSuppId
   OperationID: OnChangeSuppID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSuppID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSuppID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSuppID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangeSuppID", {
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
   Summary: Invoke method OnChangeWhseBinWizardCustId
   Description: OnChangeWhseBinWizardCustId
   OperationID: OnChangeWhseBinWizardCustId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinWizardCustId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinWizardCustId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseBinWizardCustId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangeWhseBinWizardCustId", {
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
   Summary: Invoke method OnChangeWhseBinWizardSuppId
   Description: OnChangeWhseBinWizardSuppId
   OperationID: OnChangeWhseBinWizardSuppId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinWizardSuppId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinWizardSuppId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseBinWizardSuppId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangeWhseBinWizardSuppId", {
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
   Summary: Invoke method OnChangingSegmentMaximum
   Description: Execute necessary modifications when Maximum value is changed for the segment
   OperationID: OnChangingSegmentMaximum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentMaximum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentMaximum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSegmentMaximum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangingSegmentMaximum", {
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
   Summary: Invoke method OnChangingSegmentMinimum
   Description: Execute necessary modifications when Minimum value is changed for the segment
   OperationID: OnChangingSegmentMinimum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentMinimum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentMinimum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSegmentMinimum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangingSegmentMinimum", {
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
   Summary: Invoke method OnChangingSegmentPositions
   Description: Execute necessary modifications when Number of Positions is changed for the Segment
   OperationID: OnChangingSegmentPositions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentPositions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentPositions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSegmentPositions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangingSegmentPositions", {
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
   Summary: Invoke method OnChangingSegmentType
   Description: Execute necessary modifications when Segment Type is changed
   OperationID: OnChangingSegmentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSegmentType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/OnChangingSegmentType", {
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
   Summary: Invoke method GetNewWhseBin
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWhseBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GetNewWhseBin", {
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
   Summary: Invoke method GetNewWhseBinAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseBinAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseBinAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseBinAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWhseBinAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GetNewWhseBinAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WhseBinAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WhseBinListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WhseBinRow[],
}

export interface Erp_Tablesets_WhseBinAttchRow{
   "Company":string,
   "WarehouseCode":string,
   "BinNum":string,
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

export interface Erp_Tablesets_WhseBinListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   "WarehouseCode":string,
      /**  The user defined bin number within the warehouse.  */  
   "BinNum":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "Description":string,
      /**   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  */  
   "BinType":string,
      /**  Replenishable  */  
   "Replenishable":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WhseBinRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   "WarehouseCode":string,
      /**  The user defined bin number within the warehouse.  */  
   "BinNum":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "Description":string,
      /**  Indicates if the quantity of the warehouse bin should be considered towards the available quantity of the part.  */  
   "NonNettable":boolean,
      /**  The SizeID is the reference to the BinSize record which defines the physical size. Optional, but if entered must be valid.  */  
   "SizeID":string,
      /**  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  */  
   "ZoneID":string,
      /**  allows the warhhouse manager to assing sequences to Bins used during the picking process. The pick ticked can be sorted in Bin Sequence ordr allowing the picker to traverse thru an aisle systematically. Also allows the Queue transactions to be sorted systematically.  */  
   "BinSeq":number,
      /**   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  */  
   "BinType":string,
      /**  For BinType = Cust, this is the Customer number of the Customer that owns the contents stored in this bin. If BinType = "Cust" then must be a valid Customer reference.  */  
   "CustNum":number,
      /**  For BinType = Supl, this is the Supplier (vendor) number of the Supplier that owns the contents stored in this bin. If BinType = "Supl" then must be a valid Vendor reference.  */  
   "VendorNum":number,
      /**  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  */  
   "Aisle":string,
      /**  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  */  
   "Face":string,
      /**  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  */  
   "Elevation":number,
      /**  Maximum Fill  */  
   "MaxFill":number,
      /**  Percentage Fillable  */  
   "PctFillable":number,
      /**  Can only be set to True if the bin is empty. If inactive, then is should not be valid in any future transactions.  */  
   "InActive":boolean,
      /**  Indicates if the bin is not in a fixed location.  */  
   "Portable":boolean,
      /**  Replenishable  */  
   "Replenishable":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Determines if the warehouse bin has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  Delimited list of Warehouse Bin Attributes  */  
   "AttrBinList":string,
      /**  Used to prevent change of BinType if bin has OnhandQty.  */  
   "IsEmpty":boolean,
      /**  Determines if the plant (retrieved from parent warehouse) has to be synchronized with Epicor FSA application.  */  
   "PlantSendToFSA":boolean,
   "BitFlag":number,
   "CompanySendToFSA":boolean,
   "CustomerInactive":boolean,
   "CustomerName":string,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "SizeIDDescription":string,
   "VendorName":string,
   "VendorTermsCode":string,
   "VendorAddress2":string,
   "VendorDefaultFOB":string,
   "VendorCurrencyCode":string,
   "VendorZIP":string,
   "VendorCity":string,
   "VendorAddress3":string,
   "VendorVendorID":string,
   "VendorAddress1":string,
   "VendorState":string,
   "VendorCountry":string,
   "WarehouseCodePlant":string,
   "WarehouseCodeDescription":string,
   "ZoneIDZoneDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface AddNewWhseBinFormat_input{
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface AddNewWhseBinFormat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CommitGeneratedBins_input{
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface CommitGeneratedBins_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param warehouseCode
      @param binNum
   */  
export interface DeleteByID_input{
   warehouseCode:string,
   binNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtWhseBinTableset{
   WhseBin:Erp_Tablesets_WhseBinRow[],
   WhseBinAttch:Erp_Tablesets_WhseBinAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WhseBinAttchRow{
   Company:string,
   WarehouseCode:string,
   BinNum:string,
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

export interface Erp_Tablesets_WhseBinFormatRow{
      /**  Sequence of the Segment  */  
   Seq:number,
      /**  Segment type  */  
   Type:string,
      /**  Number of digits in the segment  */  
   Positions:number,
      /**  Lowest value allowed for the segment  */  
   Minimum:string,
      /**  Top value that the segment can have  */  
   Maximum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WhseBinListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   WarehouseCode:string,
      /**  The user defined bin number within the warehouse.  */  
   BinNum:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   Description:string,
      /**   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  */  
   BinType:string,
      /**  Replenishable  */  
   Replenishable:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WhseBinListTableset{
   WhseBinList:Erp_Tablesets_WhseBinListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WhseBinRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   WarehouseCode:string,
      /**  The user defined bin number within the warehouse.  */  
   BinNum:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   Description:string,
      /**  Indicates if the quantity of the warehouse bin should be considered towards the available quantity of the part.  */  
   NonNettable:boolean,
      /**  The SizeID is the reference to the BinSize record which defines the physical size. Optional, but if entered must be valid.  */  
   SizeID:string,
      /**  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  */  
   ZoneID:string,
      /**  allows the warhhouse manager to assing sequences to Bins used during the picking process. The pick ticked can be sorted in Bin Sequence ordr allowing the picker to traverse thru an aisle systematically. Also allows the Queue transactions to be sorted systematically.  */  
   BinSeq:number,
      /**   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  */  
   BinType:string,
      /**  For BinType = Cust, this is the Customer number of the Customer that owns the contents stored in this bin. If BinType = "Cust" then must be a valid Customer reference.  */  
   CustNum:number,
      /**  For BinType = Supl, this is the Supplier (vendor) number of the Supplier that owns the contents stored in this bin. If BinType = "Supl" then must be a valid Vendor reference.  */  
   VendorNum:number,
      /**  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  */  
   Aisle:string,
      /**  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  */  
   Face:string,
      /**  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  */  
   Elevation:number,
      /**  Maximum Fill  */  
   MaxFill:number,
      /**  Percentage Fillable  */  
   PctFillable:number,
      /**  Can only be set to True if the bin is empty. If inactive, then is should not be valid in any future transactions.  */  
   InActive:boolean,
      /**  Indicates if the bin is not in a fixed location.  */  
   Portable:boolean,
      /**  Replenishable  */  
   Replenishable:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Determines if the warehouse bin has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Delimited list of Warehouse Bin Attributes  */  
   AttrBinList:string,
      /**  Used to prevent change of BinType if bin has OnhandQty.  */  
   IsEmpty:boolean,
      /**  Determines if the plant (retrieved from parent warehouse) has to be synchronized with Epicor FSA application.  */  
   PlantSendToFSA:boolean,
   BitFlag:number,
   CompanySendToFSA:boolean,
   CustomerInactive:boolean,
   CustomerName:string,
   CustomerBTName:string,
   CustomerCustID:string,
   SizeIDDescription:string,
   VendorName:string,
   VendorTermsCode:string,
   VendorAddress2:string,
   VendorDefaultFOB:string,
   VendorCurrencyCode:string,
   VendorZIP:string,
   VendorCity:string,
   VendorAddress3:string,
   VendorVendorID:string,
   VendorAddress1:string,
   VendorState:string,
   VendorCountry:string,
   WarehouseCodePlant:string,
   WarehouseCodeDescription:string,
   ZoneIDZoneDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WhseBinTableset{
   WhseBin:Erp_Tablesets_WhseBinRow[],
   WhseBinAttch:Erp_Tablesets_WhseBinAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WhseBinWizardRow{
      /**  Company where the Bin belongs  */  
   Company:string,
      /**  Wharehouse where the Bin belongs  */  
   WarehouseCode:string,
      /**  Bin Number  */  
   BinNum:string,
      /**  Bin Description  */  
   Description:string,
      /**  Zone Id  */  
   ZoneId:string,
      /**  Size Id  */  
   SizeID:string,
      /**  Bin Sequence  */  
   BinSeq:number,
      /**  Bin Type  */  
   BinType:string,
      /**  Max Fill  */  
   MaxFill:number,
      /**  Percentage Fillable  */  
   PctFillable:number,
      /**  Inactive  */  
   Inactive:boolean,
      /**  Non Nettable  */  
   NonNettable:boolean,
      /**  Portable  */  
   Portable:boolean,
      /**  Replenishable  */  
   Replenishable:boolean,
      /**  Aisle  */  
   Aisle:string,
      /**  Face  */  
   Face:string,
      /**  Elevation  */  
   Elevation:number,
      /**  Bin Numbers Format  */  
   BinNumFormat:string,
      /**  True when the Bin Number is selected  */  
   Selected:boolean,
      /**  True when the Bin Number already exists  */  
   Exist:boolean,
      /**  True when sequence will automatically increased  */  
   AutoSeq:boolean,
      /**  Warehouse description  */  
   WhseDescription:string,
      /**  Zone Description  */  
   ZoneDescription:string,
      /**  Bin Size description  */  
   SizeDescription:string,
      /**  CustID  */  
   CustID:string,
      /**  CustNum  */  
   CustNum:number,
   CustomerName:string,
      /**  VendorID  */  
   VendorID:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  VendorName  */  
   VendorName:string,
      /**  Determines if the warehouse bin has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WhseBinWizardTableset{
   WhseBinFormat:Erp_Tablesets_WhseBinFormatRow[],
   WhseBinWizard:Erp_Tablesets_WhseBinWizardRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateBinFormat_input{
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface GenerateBinFormat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param totalBins
      @param ds
   */  
export interface GenerateBins_input{
      /**  Number of Bin Numbers to be generated  */  
   totalBins:number,
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface GenerateBins_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param warehouseCode
      @param binNum
   */  
export interface GetByID_input{
   warehouseCode:string,
   binNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_WhseBinTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_WhseBinTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_WhseBinTableset[],
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
   returnObj:Erp_Tablesets_WhseBinListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param warehouseCode
      @param binNum
   */  
export interface GetNewWhseBinAttch_input{
   ds:Erp_Tablesets_WhseBinTableset[],
   warehouseCode:string,
   binNum:string,
}

export interface GetNewWhseBinAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinTableset[],
}
}

   /** Required : 
      @param ds
      @param warehouseCode
   */  
export interface GetNewWhseBin_input{
   ds:Erp_Tablesets_WhseBinTableset[],
   warehouseCode:string,
}

export interface GetNewWhseBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinTableset[],
}
}

   /** Required : 
      @param whereClauseWhseBin
      @param whereClauseWhseBinAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseWhseBin:string,
   whereClauseWhseBinAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_WhseBinTableset[],
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

export interface InActiveFlag_output{
parameters : {
      /**  output parameters  */  
   cWarning:string,
}
}

   /** Required : 
      @param newCustID
      @param ds
   */  
export interface OnChangeCustID_input{
      /**  Customer.CustID  */  
   newCustID:string,
   ds:Erp_Tablesets_WhseBinTableset[],
}

export interface OnChangeCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinTableset[],
}
}

   /** Required : 
      @param newVendorID
      @param ds
   */  
export interface OnChangeSuppID_input{
      /**  Vendor.VendorID  */  
   newVendorID:string,
   ds:Erp_Tablesets_WhseBinTableset[],
}

export interface OnChangeSuppID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinTableset[],
}
}

   /** Required : 
      @param newCustID
      @param ds
   */  
export interface OnChangeWhseBinWizardCustId_input{
      /**  Customer.CustID  */  
   newCustID:string,
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface OnChangeWhseBinWizardCustId_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param newVendorID
      @param ds
   */  
export interface OnChangeWhseBinWizardSuppId_input{
      /**  Vendor.VendorID  */  
   newVendorID:string,
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface OnChangeWhseBinWizardSuppId_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param iSegment
      @param newValue
      @param ds
   */  
export interface OnChangingSegmentMaximum_input{
      /**  Segment that is being modified  */  
   iSegment:number,
      /**  New Maximum value  */  
   newValue:string,
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface OnChangingSegmentMaximum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param iSegment
      @param newValue
      @param ds
   */  
export interface OnChangingSegmentMinimum_input{
      /**  Segment that is being modified  */  
   iSegment:number,
      /**  New Minimum value  */  
   newValue:string,
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface OnChangingSegmentMinimum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param iSegment
      @param newValue
      @param ds
   */  
export interface OnChangingSegmentPositions_input{
      /**  Segment that is being modified  */  
   iSegment:number,
      /**  New Positions value  */  
   newValue:number,
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface OnChangingSegmentPositions_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param iSegment
      @param newValue
      @param ds
   */  
export interface OnChangingSegmentType_input{
      /**  Segment that is being modified  */  
   iSegment:number,
      /**  New Type value  */  
   newValue:string,
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}

export interface OnChangingSegmentType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinWizardTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtWhseBinTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtWhseBinTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_WhseBinTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WhseBinTableset[],
}
}

