import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.FAssetSvc
// Description: Fixed Asset module
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/$metadata", {
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
   Description: Get FAssets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetRow
   */  
export function get_FAssets(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAssets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets", {
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
   Summary: Calls GetByID to retrieve the FAsset item
   Description: Calls GetByID to retrieve the FAsset item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAsset
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetRow
   */  
export function get_FAssets_Company_AssetNum(Company:string, AssetNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAssetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAssetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAsset for the service
   Description: Calls UpdateExt to update FAsset. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAsset
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAssets_Company_AssetNum(Company:string, AssetNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")", {
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
   Summary: Call UpdateExt to delete FAsset item
   Description: Call UpdateExt to delete FAsset item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAsset
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAssets_Company_AssetNum(Company:string, AssetNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")", {
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
   Description: Get ChildAssets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ChildAssets1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ChildAssetsRow
   */  
export function get_FAssets_Company_AssetNum_ChildAssets(Company:string, AssetNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ChildAssetsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/ChildAssets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ChildAssetsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ChildAsset item
   Description: Calls GetByID to retrieve the ChildAsset item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ChildAsset1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   */  
export function get_FAssets_Company_AssetNum_ChildAssets_Company_AssetNum(Company:string, AssetNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ChildAssetsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/ChildAssets(" + Company + "," + AssetNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ChildAssetsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FAssetDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAssetDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlRow
   */  
export function get_FAssets_Company_AssetNum_FAssetDtls(Company:string, AssetNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FAssetDtl item
   Description: Calls GetByID to retrieve the FAssetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   */  
export function get_FAssets_Company_AssetNum_FAssetDtls_Company_AssetNum_AssetRegID(Company:string, AssetNum:string, AssetRegID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAssetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAssetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FAssetAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAssetAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetAttchRow
   */  
export function get_FAssets_Company_AssetNum_FAssetAttches(Company:string, AssetNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FAssetAttch item
   Description: Calls GetByID to retrieve the FAssetAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   */  
export function get_FAssets_Company_AssetNum_FAssetAttches_Company_AssetNum_DrawingSeq(Company:string, AssetNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAssetAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAssetAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ChildAssets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ChildAssets
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ChildAssetsRow
   */  
export function get_ChildAssets(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ChildAssetsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ChildAssetsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ChildAssets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChildAssets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets", {
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
   Summary: Calls GetByID to retrieve the ChildAsset item
   Description: Calls GetByID to retrieve the ChildAsset item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ChildAsset
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   */  
export function get_ChildAssets_Company_AssetNum(Company:string, AssetNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ChildAssetsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets(" + Company + "," + AssetNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ChildAssetsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ChildAsset for the service
   Description: Calls UpdateExt to update ChildAsset. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ChildAsset
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ChildAssets_Company_AssetNum(Company:string, AssetNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets(" + Company + "," + AssetNum + ")", {
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
   Summary: Call UpdateExt to delete ChildAsset item
   Description: Call UpdateExt to delete ChildAsset item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ChildAsset
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ChildAssets_Company_AssetNum(Company:string, AssetNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets(" + Company + "," + AssetNum + ")", {
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
   Description: Get FAssetDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssetDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlRow
   */  
export function get_FAssetDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssetDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAssetDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls", {
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
   Summary: Calls GetByID to retrieve the FAssetDtl item
   Description: Calls GetByID to retrieve the FAssetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   */  
export function get_FAssetDtls_Company_AssetNum_AssetRegID(Company:string, AssetNum:string, AssetRegID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAssetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAssetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAssetDtl for the service
   Description: Calls UpdateExt to update FAssetDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAssetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAssetDtls_Company_AssetNum_AssetRegID(Company:string, AssetNum:string, AssetRegID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")", {
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
   Summary: Call UpdateExt to delete FAssetDtl item
   Description: Call UpdateExt to delete FAssetDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAssetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAssetDtls_Company_AssetNum_AssetRegID(Company:string, AssetNum:string, AssetRegID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")", {
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
   Description: Get FAssetDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAssetDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlAttchRow
   */  
export function get_FAssetDtls_Company_AssetNum_AssetRegID_FAssetDtlAttches(Company:string, AssetNum:string, AssetRegID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")/FAssetDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FAssetDtlAttch item
   Description: Calls GetByID to retrieve the FAssetDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   */  
export function get_FAssetDtls_Company_AssetNum_AssetRegID_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company:string, AssetNum:string, AssetRegID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAssetDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAssetDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FAssetDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssetDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlAttchRow
   */  
export function get_FAssetDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssetDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAssetDtlAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches", {
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
   Summary: Calls GetByID to retrieve the FAssetDtlAttch item
   Description: Calls GetByID to retrieve the FAssetDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   */  
export function get_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company:string, AssetNum:string, AssetRegID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAssetDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAssetDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAssetDtlAttch for the service
   Description: Calls UpdateExt to update FAssetDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAssetDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company:string, AssetNum:string, AssetRegID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FAssetDtlAttch item
   Description: Call UpdateExt to delete FAssetDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAssetDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company:string, AssetNum:string, AssetRegID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")", {
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
   Description: Get FAssetAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssetAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetAttchRow
   */  
export function get_FAssetAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssetAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAssetAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches", {
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
   Summary: Calls GetByID to retrieve the FAssetAttch item
   Description: Calls GetByID to retrieve the FAssetAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   */  
export function get_FAssetAttches_Company_AssetNum_DrawingSeq(Company:string, AssetNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAssetAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAssetAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAssetAttch for the service
   Description: Calls UpdateExt to update FAssetAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAssetAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAssetAttches_Company_AssetNum_DrawingSeq(Company:string, AssetNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FAssetAttch item
   Description: Call UpdateExt to delete FAssetAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAssetAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAssetAttches_Company_AssetNum_DrawingSeq(Company:string, AssetNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseFAsset:string, whereClauseFAssetAttch:string, whereClauseChildAssets:string, whereClauseFAssetDtl:string, whereClauseFAssetDtlAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFAsset!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAsset=" + whereClauseFAsset
   }
   if(typeof whereClauseFAssetAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAssetAttch=" + whereClauseFAssetAttch
   }
   if(typeof whereClauseChildAssets!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseChildAssets=" + whereClauseChildAssets
   }
   if(typeof whereClauseFAssetDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAssetDtl=" + whereClauseFAssetDtl
   }
   if(typeof whereClauseFAssetDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAssetDtlAttch=" + whereClauseFAssetDtlAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(assetNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof assetNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assetNum=" + assetNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetList" + params, {
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
   Summary: Invoke method GetClientFileName
   OperationID: GetClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetClientFileName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetClientFileName", {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetCodeDescList", {
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
   Summary: Invoke method CalcTaxAmtLine
   Description: Called to calculate the Tax for the AP Invoice Line
   OperationID: CalcTaxAmtLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcTaxAmtLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcTaxAmtLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcTaxAmtLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/CalcTaxAmtLine", {
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
   Summary: Invoke method ChangeAssetMethod
   Description: Update AssetMethod when a different AssetMethod is selected.
   OperationID: ChangeAssetMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssetMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssetMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAssetMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChangeAssetMethod", {
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
   Summary: Invoke method ChangeAssetRegister
   Description: Update AssetRegister when a different AssetRegister is selected.
   OperationID: ChangeAssetRegister
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssetRegister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssetRegister_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAssetRegister(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChangeAssetRegister", {
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
   Summary: Invoke method PreDuplicate
   Description: Performs validations before Asset duplication
   OperationID: PreDuplicate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDuplicate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDuplicate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreDuplicate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/PreDuplicate", {
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
   Summary: Invoke method Duplicate
   Description: Duplicate fixed asset.
   OperationID: Duplicate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Duplicate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Duplicate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Duplicate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/Duplicate", {
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
   Summary: Invoke method ExportData
   Description: ExportData
   OperationID: ExportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportData(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ExportData", {
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
   Summary: Invoke method GetChildAssets
   Description: Get the ChildAsset records for a parent asset.
   OperationID: GetChildAssets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChildAssets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChildAssets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetChildAssets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetChildAssets", {
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
   Summary: Invoke method GetFAssetByID
   Description: Get Fixed Asset by ID
   OperationID: GetFAssetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFAssetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFAssetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFAssetByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetFAssetByID", {
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
   Summary: Invoke method GetNewChildAsset
   Description: To be called when a new ChildAssets row is needed.
   OperationID: GetNewChildAsset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewChildAsset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewChildAsset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewChildAsset(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetNewChildAsset", {
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
   Summary: Invoke method ImportData
   OperationID: ImportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ImportData", {
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
   Summary: Invoke method LeaveAcquiredDate
   Description: The purpose of this code is to assign the commissioned date to the
acquired date for a new fixed asset. (Only run this code on a new fixed asset)
Called on leave of Acquired Date field.
   OperationID: LeaveAcquiredDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAcquiredDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAcquiredDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveAcquiredDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveAcquiredDate", {
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
   Summary: Invoke method LeaveChildAssetNum
   Description: To be called on leave of (Child) AssetNum field.
   OperationID: LeaveChildAssetNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveChildAssetNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveChildAssetNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveChildAssetNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveChildAssetNum", {
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
   Summary: Invoke method LeaveInsPremium
   Description: To be called on leave of FAsset.InsurancePremium field
   OperationID: LeaveInsPremium
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInsPremium_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInsPremium_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveInsPremium(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveInsPremium", {
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
   Summary: Invoke method LeaveInsValue
   Description: To be called on leave of FAsset.InsuranceValue field
   OperationID: LeaveInsValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInsValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInsValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveInsValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveInsValue", {
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
   Summary: Invoke method LeaveInvoiceLine
   Description: Called on the leave of Invoice Line
   OperationID: LeaveInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveInvoiceLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveInvoiceLine", {
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
   Summary: Invoke method LeaveInvoiceNum
   Description: Called on the leave of Invoice Number
   OperationID: LeaveInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveInvoiceNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveInvoiceNum", {
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
   Summary: Invoke method LeaveJobNum
   Description: To be called on leave of Job Number field
   OperationID: LeaveJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveJobNum", {
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
   Summary: Invoke method LeaveLeaseValue
   Description: To be called on leave of FAsset.LeaseValue field
   OperationID: LeaveLeaseValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveLeaseValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveLeaseValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveLeaseValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveLeaseValue", {
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
   Summary: Invoke method LeavePONum
   Description: To be called on leave of VendorID field
   OperationID: LeavePONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeavePONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeavePONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeavePONum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeavePONum", {
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
   Summary: Invoke method LeaveReplaceValue
   Description: To be called on leave of ReplaceValue field
   OperationID: LeaveReplaceValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveReplaceValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveReplaceValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveReplaceValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveReplaceValue", {
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
   Summary: Invoke method LeaveResidualValue
   Description: To be called on leave of ResidualValue field
   OperationID: LeaveResidualValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveResidualValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveResidualValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveResidualValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveResidualValue", {
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
   Summary: Invoke method LeaveVendorID
   Description: To be called on leave of VendorID field
   OperationID: LeaveVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/LeaveVendorID", {
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
   Summary: Invoke method PostedDepExist
   Description: Returns true if the asset registry has posted depreciation transactions.
   OperationID: PostedDepExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostedDepExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostedDepExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostedDepExist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/PostedDepExist", {
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
   Summary: Invoke method TestAllowDelete
   Description: This procedure is to provide a check before deleting the records
You can use this method to provide a message to the user of this fact and provide a confirmation dialog. This is
intended to be called before the delete procedure.
If there are existing records SureMsg will contain a translated text message
which can be used to display in your message dialog.  Otherwise it returns blanks and there is no need to provide a
dialog.
   OperationID: TestAllowDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestAllowDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestAllowDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestAllowDelete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/TestAllowDelete", {
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
   Summary: Invoke method TestParentChildIntegrity
   Description: This procedure should be called to check for parent\child integrity.
The procedure throws an exception if the relation is invalid.
   OperationID: TestParentChildIntegrity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestParentChildIntegrity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestParentChildIntegrity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestParentChildIntegrity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/TestParentChildIntegrity", {
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
   Summary: Invoke method OnChangeCommodityCode
   Description: Validate entered Commodity Code
   OperationID: OnChangeCommodityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCommodityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCommodityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCommodityCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/OnChangeCommodityCode", {
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
   Summary: Invoke method ImportToDS
   Description: Import Logic
   OperationID: ImportToDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportToDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportToDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportToDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ImportToDS", {
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
   Summary: Invoke method ExportProcess
   Description: Export Process
   OperationID: ExportProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportProcess(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ExportProcess", {
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
   Summary: Invoke method GetNewFAsset
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAsset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAsset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAsset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAsset(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetNewFAsset", {
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
   Summary: Invoke method GetNewFAssetAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAssetAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAssetAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAssetAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAssetAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetNewFAssetAttch", {
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
   Summary: Invoke method GetNewFAssetDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAssetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAssetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAssetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAssetDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetNewFAssetDtl", {
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
   Summary: Invoke method GetNewFAssetDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAssetDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAssetDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAssetDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAssetDtlAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetNewFAssetDtlAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ChildAssetsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ChildAssetsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAssetAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAssetDtlAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAssetDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAssetListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAssetRow[],
}

export interface Erp_Tablesets_ChildAssetsRow{
      /**  Company  */  
   "Company":string,
      /**  Asset Number  */  
   "AssetNum":string,
      /**  Asset Description  */  
   "AssetDescription":string,
      /**  Parent Asset Number  */  
   "ParentAsset":string,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  Asset Sequence  */  
   "AssetSeq":number,
      /**  Parent Asset Sequence  */  
   "ParentAssetSeq":number,
   "AssetStatus":string,
   "TagNum":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAssetAttchRow{
   "Company":string,
   "AssetNum":string,
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

export interface Erp_Tablesets_FAssetDtlAttchRow{
   "Company":string,
   "AssetNum":string,
   "AssetRegID":string,
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

export interface Erp_Tablesets_FAssetDtlRow{
      /**  Company of the asset.  */  
   "Company":string,
      /**  Identifier of the asset  */  
   "AssetNum":string,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  */  
   "AdditionSpread":boolean,
      /**  Identifier of the spread code table that will be used for the Addition Spread option.  */  
   "SpreadCode":string,
      /**  In case of life depreciation method the life modifier expresses the unit of measure of life. Values are: Periods and Years.  */  
   "LifeModifier":string,
      /**  The Depreciation Rate that will be used to calculate the Annual Charge.  */  
   "AnnualDepRate":number,
      /**  Number of periods or years - unit defined in the Life Modifier.  */  
   "AssetLife":number,
      /**  Current year opening depreciation  */  
   "CYOpenDepn":number,
      /**  Current year opening bookvalue  */  
   "CYOpenBookValue":number,
      /**  Current year opening grant depreciation  */  
   "CYOpenGrantDepn":number,
      /**  Current year opening grant bookvalue  */  
   "CYOpenGrantBookValue":number,
      /**  Depreciation applied in previous years through addition this year.  */  
   "CYAddPrevDepn":number,
      /**  Current year depreciation  */  
   "CYAddCurrDepn":number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   "CYAddBookvalue":number,
      /**  Depreciation applied in previous years through disposal this year.  */  
   "CYDispPrevDepn":number,
      /**  Depreciation applied this year through addition this year.  */  
   "CYDispCurrDepn":number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   "CYDispBookValue":number,
      /**  Depreciated in previous years  */  
   "CurrentPrevYearDepn":number,
      /**  Depreciated (and posted) in the current year.  */  
   "CurrentPostedDepn":number,
      /**  The current bookvalue.  */  
   "CurrentBookvalue":number,
      /**  Depreciations open for this year.  */  
   "CurrentUnpostedDepn":number,
      /**  The projected bookvalue at the end of this year.  */  
   "CurrentYEBookvalue":number,
      /**  Identifier of the depreciation method table.  */  
   "AssetMethod":string,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   "BookID":string,
      /**  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  */  
   "CalendarID":string,
      /**  Convention used for the depreciation calculation of the asset.  This will determine how depreciation is prorated for the year in which the asset is placed in service.  Valid values are: "HY" (Half Year); "MM" (Mid Month); "QR" (Quarter); "MQ" (Mid Quarter); "FM" (Full Month); "EM" (Entire Month); "SD" (Service Date), "NM" (Next Month), and "AD" (Acquisition Date).  This field can be blank.  */  
   "DepConvention":string,
      /**  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  */  
   "RetroAdjust":boolean,
      /**  Production Unit Spread Code.  */  
   "ProdUnitSpread":string,
      /**  Total Production Units.  This could be the total production units per Year or per Period depending on the depreciation charge basis of the asset depreciation method.  */  
   "TotalProdUnit":number,
      /**  The Fixed Value that will be used as the Annual Charge amount during the asset depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the annual charge calculation.  */  
   "AnnualFixedValue":number,
      /**  Annual Charge Spread Code  */  
   "AnnualSpread":string,
      /**  The Fixed Value that will be used as the Period Charge amount during the asset period depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the period charge calculation.  */  
   "PeriodFixedValue":number,
      /**  Period Charge Spread  */  
   "PeriodSpread":string,
      /**  Spread Code used to determine the spread values used when prorating Annual Charge.  */  
   "PeriodRateSpread":string,
      /**  Final Spread Code  */  
   "FinalSpread":string,
      /**  Indicates if this asset register detail has already switched or used the alternate depreciation method. An asset register is only allowed to switch to an alternate depreciation method once and cannot switch back to original method.  */  
   "MethodSwitched":boolean,
      /**  Alternate Depreciation Method  */  
   "AltAssetMethod":string,
      /**  Depreciated in previous years  */  
   "DocCurrentPrevYearDepn":number,
      /**  Depreciated (and posted) in the current year.  */  
   "DocCurrentPostedDepn":number,
      /**  The current bookvalue.  */  
   "DocCurrentBookvalue":number,
      /**  Depreciations open for this year.  */  
   "DocCurrentUnpostedDepn":number,
      /**  The projected bookvalue at the end of this year.  */  
   "DocCurrentYEBookvalue":number,
      /**  Depreciated in previous years  */  
   "Rpt1CurrentPrevYearDepn":number,
      /**  Depreciated (and posted) in the current year.  */  
   "Rpt1CurrentPostedDepn":number,
      /**  The current bookvalue.  */  
   "Rpt1CurrentBookvalue":number,
      /**  Depreciations open for this year.  */  
   "Rpt1CurrentUnpostedDepn":number,
      /**  The projected bookvalue at the end of this year.  */  
   "Rpt1CurrentYEBookvalue":number,
      /**  Depreciated in previous years  */  
   "Rpt2CurrentPrevYearDepn":number,
      /**  Depreciated (and posted) in the current year.  */  
   "Rpt2CurrentPostedDepn":number,
      /**  The current bookvalue.  */  
   "Rpt2CurrentBookvalue":number,
      /**  Depreciations open for this year.  */  
   "Rpt2CurrentUnpostedDepn":number,
      /**  The projected bookvalue at the end of this year.  */  
   "Rpt2CurrentYEBookvalue":number,
      /**  Depreciated in previous years  */  
   "Rpt3CurrentPrevYearDepn":number,
      /**  Depreciated (and posted) in the current year.  */  
   "Rpt3CurrentPostedDepn":number,
      /**  The current bookvalue.  */  
   "Rpt3CurrentBookvalue":number,
      /**  Depreciations open for this year.  */  
   "Rpt3CurrentUnpostedDepn":number,
      /**  The projected bookvalue at the end of this year.  */  
   "Rpt3CurrentYEBookvalue":number,
      /**  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  */  
   "UseFinalSpread":boolean,
      /**  System maintained field.  Indicates that asset depreciation needs to be recalculated for this depreciation method.  */  
   "DepRecalcNeeded":boolean,
      /**  Grant Depreciation in previous years  */  
   "CurrentGrantPYDepn":number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   "CurrentGrantPostedDepn":number,
      /**  The current grant book value.  */  
   "CurrentGrantBookValue":number,
      /**  Grant Depreciations open for this year.  */  
   "CurrentGrantUnpostedDepn":number,
      /**  The projected grant bookvalue at the end of this year.  */  
   "CurrentGrantYEBookValue":number,
      /**  Grant Depreciation in previous years  */  
   "DocCurrentGrantPYDepn":number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   "DocCurrentGrantPostedDepn":number,
      /**  The current grant book value.  */  
   "DocCurrentGrantBookValue":number,
      /**  Grant Depreciations open for this year.  */  
   "DocCurrentGrantUnpostedDepn":number,
      /**  The projected grant bookvalue at the end of this year.  */  
   "DocCurrentGrantYEBookValue":number,
      /**  Grant Depreciation in previous years  */  
   "Rpt1CurrentGrantPYDepn":number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   "Rpt1CurrentGrantPostedDepn":number,
      /**  The current grant book value.  */  
   "Rpt1CurrentGrantBookValue":number,
      /**  Grant Depreciations open for this year.  */  
   "Rpt1CurrentGrantUnpostedDepn":number,
      /**  The projected grant bookvalue at the end of this year.  */  
   "Rpt1CurrentGrantYEBookValue":number,
      /**  Grant Depreciation in previous years  */  
   "Rpt2CurrentGrantPYDepn":number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   "Rpt2CurrentGrantPostedDepn":number,
      /**  The current grant book value.  */  
   "Rpt2CurrentGrantBookValue":number,
      /**  Grant Depreciations open for this year.  */  
   "Rpt2CurrentGrantUnpostedDepn":number,
      /**  The projected grant bookvalue at the end of this year.  */  
   "Rpt2CurrentGrantYEBookValue":number,
      /**  Grant Depreciation in previous years  */  
   "Rpt3CurrentGrantPYDepn":number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   "Rpt3CurrentGrantPostedDepn":number,
      /**  The current grant book value.  */  
   "Rpt3CurrentGrantBookValue":number,
      /**  Grant Depreciations open for this year.  */  
   "Rpt3CurrentGrantUnpostedDepn":number,
      /**  The projected grant bookvalue at the end of this year.  */  
   "Rpt3CurrentGrantYEBookValue":number,
      /**  Current year opening bookvalue  */  
   "DocCYOpenBookValue":number,
      /**  Previous years addition depreciation  */  
   "DocCYAddPrevDepn":number,
      /**  Current year addition depreciation  */  
   "DocCYAddCurrDepn":number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   "DocCYAddBookValue":number,
      /**  Previous years Disposal depreciation  */  
   "DocCYDispPrevDepn":number,
      /**  Current year Disposal depreciation  */  
   "DocCYDispCurrDepn":number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   "DocCYDispBookValue":number,
      /**  Current year opening bookvalue  */  
   "Rpt1CYOpenBookValue":number,
      /**  Previous years Addition depreciation  */  
   "Rpt1CYAddPrevDepn":number,
      /**  Current year Addition depreciation  */  
   "Rpt1CYAddCurrDepn":number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   "Rpt1CYAddBookValue":number,
      /**  Previous years Disposal depreciation  */  
   "Rpt1CYDispPrevDepn":number,
      /**  Current year Disposal depreciation  */  
   "Rpt1CYDispCurrDepn":number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   "Rpt1CYDispBookValue":number,
      /**  Current year opening bookvalue  */  
   "Rpt2CYOpenBookValue":number,
      /**  Previous years Addition depreciation  */  
   "Rpt2CYAddPrevDepn":number,
      /**  Current year Addition depreciation  */  
   "Rpt2CYAddCurrDepn":number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   "Rpt2CYAddBookValue":number,
      /**  Previous years Disposal depreciation  */  
   "Rpt2CYDispPrevDepn":number,
      /**  Current year Disposal depreciation  */  
   "Rpt2CYDispCurrDepn":number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   "Rpt2CYDispBookValue":number,
      /**  Current year opening bookvalue  */  
   "Rpt3CYOpenBookValue":number,
      /**  Previous years Addition depreciation  */  
   "Rpt3CYAddPrevDepn":number,
      /**  Current year Addition depreciation  */  
   "Rpt3CYAddCurrDepn":number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   "Rpt3CYAddBookValue":number,
      /**  Previous years Disposal depreciation  */  
   "Rpt3CYDispPrevDepn":number,
      /**  Current year Disposal depreciation  */  
   "Rpt3CYDispCurrDepn":number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   "Rpt3CYDispBookValue":number,
      /**  Current year opening grant depreciation  */  
   "DocCYOpenGrantDepn":number,
      /**  Current year opening grant depreciation  */  
   "Rpt1CYOpenGrantDepn":number,
      /**  Current year opening grant depreciation  */  
   "Rpt2CYOpenGrantDepn":number,
      /**  Current year opening grant depreciation  */  
   "Rpt3CYOpenGrantDepn":number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   "DepRecalcDate":string,
      /**  This is the initial book value of the entire asset depreciation schedule.  */  
   "InitBookValue":number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   "DocInitBookValue":number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   "Rpt1InitBookValue":number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   "Rpt2InitBookValue":number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   "Rpt3InitBookValue":number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   "InitGrantBookValue":number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   "DocInitGrantBookValue":number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   "Rpt1InitGrantBookValue":number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   "Rpt2InitGrantBookValue":number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   "Rpt3InitGrantBookValue":number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   "CYImpBookValue":number,
      /**  Previous years Disposal Grant depreciation  */  
   "CYDispGrantPrevDepn":number,
      /**  Current year Disposal Grant depreciation  */  
   "CYDispGrantCurrDepn":number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   "CYDispGrantBookValue":number,
      /**  Current year opening grant bookvalue  */  
   "DocCYOpenGrantBookValue":number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   "DocCYImpBookValue":number,
      /**  Previous years Disposal Grant depreciation  */  
   "DocCYDispGrantPrevDepn":number,
      /**  Current year Disposal Grant depreciation  */  
   "DocCYDispGrantCurrDepn":number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   "DocCYDispGrantBookValue":number,
      /**  Current year opening grant bookvalue  */  
   "Rpt1CYOpenGrantBookValue":number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   "Rpt1CYImpBookValue":number,
      /**  Previous years Disposal Grant depreciation  */  
   "Rpt1CYDispGrantPrevDepn":number,
      /**  Current year Disposal Grant depreciation  */  
   "Rpt1CYDispGrantCurrDepn":number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   "Rpt1CYDispGrantBookValue":number,
      /**  Current year opening grant bookvalue  */  
   "Rpt2CYOpenGrantBookValue":number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   "Rpt2CYImpBookValue":number,
      /**  Previous years Disposal Grant depreciation  */  
   "Rpt2CYDispGrantPrevDepn":number,
      /**  Current year Disposal Grant depreciation  */  
   "Rpt2CYDispGrantCurrDepn":number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   "Rpt2CYDispGrantBookValue":number,
      /**  Current year opening grant bookvalue  */  
   "Rpt3CYOpenGrantBookValue":number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   "Rpt3CYImpBookValue":number,
      /**  Previous years Disposal Grant depreciation  */  
   "Rpt3CYDispGrantPrevDepn":number,
      /**  Current year Disposal Grant depreciation  */  
   "Rpt3CYDispGrantCurrDepn":number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   "Rpt3CYDispGrantBookValue":number,
      /**  Current year opening depreciation  */  
   "DocCYOpenDepn":number,
      /**  Current year opening depreciation  */  
   "Rpt1CYOpenDepn":number,
      /**  Current year opening depreciation  */  
   "Rpt2CYOpenDepn":number,
      /**  Current year opening depreciation  */  
   "Rpt3CYOpenDepn":number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   "CurrentActPrevDepn":number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   "CurrentActPostedDepn":number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   "DocCurrentActPrevDepn":number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   "DocCurrentActPostedDepn":number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   "Rpt1CurrentActPrevDepn":number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   "Rpt1CurrentActPostedDepn":number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   "Rpt2CurrentActPrevDepn":number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   "Rpt2CurrentActPostedDepn":number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   "Rpt3CurrentActPrevDepn":number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   "Rpt3CurrentActPostedDepn":number,
      /**  Previous years Addition Grant depreciation  */  
   "CYAddGrantPrevDepn":number,
      /**  Previous years Addition Grant depreciation  */  
   "CYAddGrantCurrDepn":number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   "CYAddGrantBookValue":number,
      /**  Previous years Addition Grant depreciation  */  
   "DocCYAddGrantPrevDepn":number,
      /**  Current year Addition Grant depreciation  */  
   "DocCYAddGrantCurrDepn":number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   "DocCYAddGrantBookValue":number,
      /**  Previous years Addition Grant depreciation  */  
   "Rpt1CYAddGrantPrevDepn":number,
      /**  Current year Addition Grant depreciation  */  
   "Rpt1CYAddGrantCurrDepn":number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   "Rpt1CYAddGrantBookValue":number,
      /**  Previous years Addition Grant depreciation  */  
   "Rpt2CYAddGrantPrevDepn":number,
      /**  Current year Addition Grant depreciation  */  
   "Rpt2CYAddGrantCurrDepn":number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   "Rpt2CYAddGrantBookValue":number,
      /**  Previous years Addition Grant depreciation  */  
   "Rpt3CYAddGrantPrevDepn":number,
      /**  Current year Addition Grant depreciation  */  
   "Rpt3CYAddGrantCurrDepn":number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   "Rpt3CYAddGrantBookValue":number,
      /**  Depreciation Flag. When true then the asset register will be processed in the depreciation recalculation process and the depreciation posting process.  If set to false then all depreciation parameters are blank and not updatable.  */  
   "Depreciate":boolean,
      /**  Current year opening cost  */  
   "CYOpenCost":number,
      /**  Current year opening cost  */  
   "DocCYOpenCost":number,
      /**  Current year opening cost  */  
   "Rpt1CYOpenCost":number,
      /**  Current year opening cost  */  
   "Rpt2CYOpenCost":number,
      /**  Current year opening cost  */  
   "Rpt3CYOpenCost":number,
      /**  Current year opening grant amount  */  
   "CYOpenGrant":number,
      /**  Current year opening cost  */  
   "DocCYOpenGrant":number,
      /**  Current year opening cost  */  
   "Rpt1CYOpenGrant":number,
      /**  Current year opening cost  */  
   "Rpt2CYOpenGrant":number,
      /**  Current year opening cost  */  
   "Rpt3CYOpenGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "CYAddCost":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "DocCYAddCost":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt1CYAddCost":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt2CYAddCost":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt3CYAddCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "CYImpCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "DocCYImpCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt1CYImpCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt2CYImpCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt3CYImpCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "CYDispCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "DocCYDispCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt1CYDispCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt2CYDispCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt3CYDispCost":number,
      /**  Disposal proceed amount.  */  
   "CYDispProceeds":number,
      /**  Disposal proceed amount.  */  
   "DocCYDispProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt1CYDispProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt2CYDispProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt3CYDispProceeds":number,
      /**  Disposal profit/loss amount.  */  
   "CYDispProfit":number,
      /**  Disposal profit/loss amount.  */  
   "DocCYDispProfit":number,
      /**  Disposal profit/loss amount.  */  
   "Rpt1CYDispProfit":number,
      /**  Disposal profit/loss amount.  */  
   "Rpt2CYDispProfit":number,
      /**  Disposal profit/loss amount.  */  
   "Rpt3CYDispProfit":number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   "CYAddGrant":number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   "DocCYAddGrant":number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   "Rpt1CYAddGrant":number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   "Rpt2CYAddGrant":number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   "Rpt3CYAddGrant":number,
      /**  Current cost value of the asset.  */  
   "CurrentCostvalue":number,
      /**  Current cost value of the asset.  */  
   "DocCurrentCostvalue":number,
      /**  Current cost value of the asset.  */  
   "Rpt1CurrentCostvalue":number,
      /**  Current cost value of the asset.  */  
   "Rpt2CurrentCostvalue":number,
      /**  Current cost value of the asset.  */  
   "Rpt3CurrentCostvalue":number,
      /**  Current Grant Amount of the asset.  */  
   "CurrentGrantAmt":number,
      /**  Current Grant Amount of the asset.  */  
   "DocCurrentGrantAmt":number,
      /**  Current Grant Amount of the asset.  */  
   "Rpt1CurrentGrantAmt":number,
      /**  Current Grant Amount of the asset.  */  
   "Rpt2CurrentGrantAmt":number,
      /**  Current Grant Amount of the asset.  */  
   "Rpt3CurrentGrantAmt":number,
      /**  The Rate Factor is used as a multiplier when calculating Annual Depreciation Charge using the Declining Balance formula.  */  
   "RateFactor":number,
      /**  Residual value of the asset  */  
   "ResidualValue":number,
      /**  Residual value of the asset in document currency  */  
   "DocResidualValue":number,
      /**  Residual value of the asset in reporting currency  */  
   "Rpt1ResidualValue":number,
      /**  Residual value of the asset in reporting currency  */  
   "Rpt2ResidualValue":number,
      /**  Residual value of the asset in reporting currency  */  
   "Rpt3ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "ReplaceValue":number,
      /**  Replacement value of the asset in document currency. For information purposes only.  */  
   "DocReplaceValue":number,
      /**  Replacement value of the asset in reporting currency. For information purposes only.  */  
   "Rpt1ReplaceValue":number,
      /**  Replacement value of the asset in reporting currency. For information purposes only.  */  
   "Rpt2ReplaceValue":number,
      /**  Replacement value of the asset in reporting currency. For information purposes only.  */  
   "Rpt3ReplaceValue":number,
      /**  The end date of the last posted depreciation period that has affected the book value of this asset register detail.  */  
   "BookValueDate":string,
      /**  This is the starting date of the fiscal year or fiscal period when the actual switch of the depreciation method to the alternative method happened.  */  
   "DateSwitched":string,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   "CurrActGrantPostedDepn":number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   "DocCurrActGrantPostedDepn":number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   "Rpt1CurrActGrantPostedDepn":number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   "Rpt2CurrActGrantPostedDepn":number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   "Rpt3CurrActGrantPostedDepn":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "AcquisitionCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "DocAcquisitionCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt1AcquisitionCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt2AcquisitionCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt3AcquisitionCost":number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   "CYDispGrant":number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   "DocCYDispGrant":number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   "Rpt1CYDispGrant":number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   "Rpt2CYDispGrant":number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   "Rpt3CYDispGrant":number,
      /**  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  */  
   "DynamicDepYear":boolean,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "CYRevalueGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "DocCYRevalueGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt1CYRevalueGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt2CYRevalueGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt3CYRevalueGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "CYDepRevalGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "DocCYDepRevalGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt1CYDepRevalGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt2CYDepRevalGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt3CYDepRevalGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "CYRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "DocCYRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt1CYRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt2CYRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt3CYRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "CYDepRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "DocCYDepRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt1CYDepRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt2CYDepRevGrantGainLoss":number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   "Rpt3CYDepRevGrantGainLoss":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Determines how depreciation is calculated in the period of disposal or revaluation.  */  
   "DepOnDisposal":number,
      /**  Date of actual depreciation schedule start.  */  
   "ActDepStartDate":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
   "CurrencySymbol":string,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   "CYDispTotalDepn":number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   "DocCYDispTotalDepn":number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   "DocRevalueGainLoss":number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   "DocYTDAccumDepn":number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   "DocYTDAddCost":number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   "DocYTDDispCost":number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   "DocYTDGrantDepn":number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   "DocYTDImpCost":number,
   "EnableAnnualDepRate":boolean,
   "EnableAssetLife":boolean,
   "EnableProdUnitsSpread":boolean,
   "EnableRateFactor":boolean,
   "EnableTotalProductionUnits":boolean,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   "RevalueGainLoss":number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   "Rpt1CYDispTotalDepn":number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   "Rpt1RevalueGainLoss":number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   "Rpt1YTDAccumDepn":number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt1YTDAddCost":number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt1YTDDispCost":number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   "Rpt1YTDGrantDepn":number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt1YTDImpCost":number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   "Rpt2CYDispTotalDepn":number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   "Rpt2RevalueGainLoss":number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   "Rpt2YTDAccumDepn":number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt2YTDAddCost":number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt2YTDDispCost":number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   "Rpt2YTDGrantDepn":number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt2YTDImpCost":number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   "Rpt3CYDispTotalDepn":number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   "Rpt3RevalueGainLoss":number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   "Rpt3YTDAccumDepn":number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt3YTDAddCost":number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt3YTDDispCost":number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   "Rpt3YTDGrantDepn":number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   "Rpt3YTDImpCost":number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   "YTDAccumDepn":number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   "YTDAddCost":number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   "YTDDispCost":number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   "YTDGrantDepn":number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   "YTDImpCost":number,
   "CurrencyCode":string,
   "BitFlag":number,
   "AddSpreadDescription":string,
   "AltAssetMethodProrateType":string,
   "AltAssetMethodFinalspread":boolean,
   "AltAssetMethodDescription":string,
   "AltAssetMethodAnnualChargeType":string,
   "AltAssetMethodPeriodChargeType":string,
   "AltAssetMethodDepChargeBasis":string,
   "AnnualSpreadDescription":string,
   "FAMethodFinalspread":boolean,
   "FAMethodDescription":string,
   "FAMethodAnnualChargeType":string,
   "FAMethodProrateType":string,
   "FAMethodDepChargeBasis":string,
   "FAMethodPeriodChargeType":string,
   "FAssetRegDescription":string,
   "FinalSpreadDescription":string,
   "FiscalCalDescription":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
   "PeriodSpreadDescription":string,
   "ProdSpreadDescription":string,
   "RateSpreadDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAssetListRow{
      /**  Company of the asset.  */  
   "Company":string,
      /**  Identifier of the asset  */  
   "AssetNum":string,
      /**  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  */  
   "AssetSeq":number,
      /**  Mandatory description of the asset.  */  
   "AssetDescription":string,
      /**  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  */  
   "InActive":boolean,
      /**  Asset parent of this asset  */  
   "ParentAsset":string,
      /**  Informational indication of a newly bought asset.  */  
   "NewAssetFlag":boolean,
      /**  The code of the mandatory asset group.  */  
   "GroupCode":string,
      /**  Identifier of the asset class.  */  
   "ClassCode":string,
      /**  Identifier of the Resource Group of the asset. For informational purposes only.  */  
   "ResourceGroupID":string,
      /**  The Resource identifier of the asset. For informational purposes only.  */  
   "ResourceID":string,
      /**  Date of acquisition of the asset.  */  
   "AcquiredDate":string,
      /**  Date of placing the asset in service. Also the start date of depreciation.  */  
   "CommissionedDate":string,
      /**  Identifier of the vendor of the asset.  */  
   "VendorNum":number,
      /**  The name of the vendor. The name can be entered without entering a vendor.  */  
   "VendorName":string,
      /**  The po number the asset purchase order.  */  
   "PONum":number,
      /**  The invoice number of asset invoice.  */  
   "InvoiceNum":string,
      /**  The job that created the asset.  */  
   "JobNum":string,
      /**  The serial number of the asset.  */  
   "Serialno":string,
      /**  The original manufacturer of the asset.  */  
   "Manufacturer":string,
      /**  The model of the asset.  */  
   "Model":string,
      /**  Insurance policy for the asset.  */  
   "InsurancePolicy":string,
      /**  The insurance company.  */  
   "InsuranceCompany":string,
      /**  Insurance premium  */  
   "InsurancePremium":number,
      /**  Insurance RenewalDate  */  
   "InsuranceRenewalDate":string,
      /**  The insurer.  */  
   "InsuranceInsurer":string,
      /**  Flag the asset as leased.  */  
   "LeaseFlag":boolean,
      /**  Lease amount  */  
   "LeaseValue":number,
      /**  Mileage limit of lease  */  
   "LeaseMileage":number,
      /**  End date of lease.  */  
   "LeaseEndDate":string,
      /**  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   "WarehouseCode":string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   "BinNum":string,
      /**  Freeform field for the location of tha aaset.  */  
   "Location":string,
      /**  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  */  
   "OverideCost":number,
      /**  Residual value of the asset  */  
   "ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "CYDisposalCost":number,
      /**  Disposal proceed amount.  */  
   "CYDisposalProceeds":number,
      /**  Current cost value of the asset.  */  
   "CurrentCostvalue":number,
      /**  The amount the asset is acquired for.  */  
   "Acquire":number,
      /**  Path and filename of asset image file.  */  
   "ImageFileName":string,
      /**  A unique code that identifies the Company currency.  */  
   "CurrencyCode":string,
      /**  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  */  
   "AssetStatus":string,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "AcquisitionCost":number,
      /**  Associates the Asset with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  Tag number. This will keep the asset label.  */  
   "TagNum":string,
      /**  The total Grant amount recorded for this Asset.  */  
   "CurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "DocResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "DocReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "DocCYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "DocCYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "DocAcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in document currency.  */  
   "DocCurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "Rpt1ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "Rpt1ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt1CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt1CYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt1AcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   "Rpt1CurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "Rpt2ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "Rpt2ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt2CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt2CYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt2AcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   "Rpt2CurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "Rpt3ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "Rpt3ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt3CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt3CYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt3AcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   "Rpt3CurrentGrantAmt":number,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  Tax Code (Mexico Localization field)  */  
   "MXTaxCode":string,
      /**  Tax Rate (Mexico Localization field)  */  
   "MXTaxRate":string,
      /**  Investment Value (Mexico Localization field)  */  
   "MXInvestAmount":number,
      /**  Mexico Tax Amount (Mexico Localization field)  */  
   "MXTaxAmount":number,
      /**  Annual depreciation Percentage (Mexico Localization field)  */  
   "MXAnnualDepre":number,
      /**  Invoice Line  (Mexico Localization field)  */  
   "InvoiceLine":number,
      /**  Mexico Asset Life (Mexico Localization field)  */  
   "MXAssetLife":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "CYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "DocCYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt1CYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt2CYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt3CYImpairCost":number,
      /**  Current cost value of the asset in document currency.  */  
   "DocCurrentCostValue":number,
      /**  Current cost value of the asset in reporting currency.  */  
   "Rpt1CurrentCostvalue":number,
      /**  Current cost value of the asset in reporting currency.  */  
   "Rpt2CurrentCostvalue":number,
      /**  Current cost value of the asset in reporting currency.  */  
   "Rpt3CurrentCostValue":number,
      /**  Location ID.  */  
   "LocID":string,
      /**  Disposal proceed amount.  */  
   "DocCYDisposalProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt1CYDisposalProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt2CYDisposalProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt3CYDisposalProceeds":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "CYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "DocCYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt1CYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt2CYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt3CYAdditionGrant":number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   "InspPlanPartNum":string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   "SpecID":string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   "LastCalDate":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  */  
   "DepRecalcNeeded":boolean,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   "EquipID":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  */  
   "AssetUnits":number,
      /**  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   "Lineage":string,
      /**  Insurance premium in document currency.  */  
   "DocInsurancePremium":number,
      /**  Insurance premium in Reporting Currency.  */  
   "Rpt1InsurancePremium":number,
      /**  Insurance premium in Reporting Currency.  */  
   "Rpt2InsurancePremium":number,
      /**  Insurance premium in Reporting Currency.  */  
   "Rpt3InsurancePremium":number,
      /**  Lease amount in document currency.  */  
   "DocLeaseValue":number,
      /**  Lease amount in Reporting Currency.  */  
   "Rpt1LeaseValue":number,
      /**  Lease amount in Rocument Currency.  */  
   "Rpt2LeaseValue":number,
      /**  Lease amount in Reporting Currency.  */  
   "Rpt3LeaseValue":number,
      /**  Insurance Value  */  
   "InsuranceValue":number,
      /**  Insurance Value in document currency.  */  
   "DocInsuranceValue":number,
      /**  Insurance Value in Reporting Currency.  */  
   "Rpt1InsuranceValue":number,
      /**  Insurance Value in Reporting Currency.  */  
   "Rpt2InsuranceValue":number,
      /**  Insurance Value in Reporting Currency.  */  
   "Rpt3InsuranceValue":number,
      /**  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  */  
   "InsPremiumModifier":string,
      /**  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  */  
   "LeaseModifier":string,
      /**  The Project Phase ID of this asset.  */  
   "PhaseID":string,
      /**  Lease Number of the asset.  */  
   "LeaseNum":string,
      /**  The Leasing Company.  */  
   "LeaseCompany":string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpAnnualCharge":number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpPeriodCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleAnnualCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRulePeriodCharge":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Department  */  
   "Department":string,
   "IsPosted":boolean,
   "FinalSpread":boolean,
   "AdditionSpread":boolean,
   "BinDescription":string,
      /**  Mexico Localization Field  */  
   "MXTaxCatID":string,
   "BaseCurrencyID":string,
      /**  Path name of the Asset Image or Photo  */  
   "ImagePath":string,
   "EquipCreate":boolean,
   "PhaseDescription":string,
      /**  The description of the asset group.  */  
   "AssetGrpDescDescription":string,
      /**  Class description.  */  
   "ClassDescription":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description the Location.  Cannot be blank.  */  
   "LocIDDescription":string,
      /**  Full description of Resource.  */  
   "MachineDescDescription":string,
      /**  Long description of the Resource Group.  */  
   "ResrceGrpDescDescription":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Description.  */  
   "WarehouseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAssetRow{
      /**  Company of the asset.  */  
   "Company":string,
      /**  Identifier of the asset  */  
   "AssetNum":string,
      /**  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  */  
   "AssetSeq":number,
      /**  Mandatory description of the asset.  */  
   "AssetDescription":string,
      /**  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  */  
   "InActive":boolean,
      /**  Asset parent of this asset  */  
   "ParentAsset":string,
      /**  Informational indication of a newly bought asset.  */  
   "NewAssetFlag":boolean,
      /**  The code of the mandatory asset group.  */  
   "GroupCode":string,
      /**  Identifier of the asset class.  */  
   "ClassCode":string,
      /**  Identifier of the Resource Group of the asset. For informational purposes only.  */  
   "ResourceGroupID":string,
      /**  The Resource identifier of the asset. For informational purposes only.  */  
   "ResourceID":string,
      /**  Date of acquisition of the asset.  */  
   "AcquiredDate":string,
      /**  Date of placing the asset in service. Also the start date of depreciation.  */  
   "CommissionedDate":string,
      /**  Identifier of the vendor of the asset.  */  
   "VendorNum":number,
      /**  The name of the vendor. The name can be entered without entering a vendor.  */  
   "VendorName":string,
      /**  The po number the asset purchase order.  */  
   "PONum":number,
      /**  The invoice number of asset invoice.  */  
   "InvoiceNum":string,
      /**  The job that created the asset.  */  
   "JobNum":string,
      /**  The serial number of the asset.  */  
   "Serialno":string,
      /**  The original manufacturer of the asset.  */  
   "Manufacturer":string,
      /**  The model of the asset.  */  
   "Model":string,
      /**  Insurance policy for the asset.  */  
   "InsurancePolicy":string,
      /**  The insurance company.  */  
   "InsuranceCompany":string,
      /**  Insurance premium  */  
   "InsurancePremium":number,
      /**  Insurance RenewalDate  */  
   "InsuranceRenewalDate":string,
      /**  The insurer.  */  
   "InsuranceInsurer":string,
      /**  Flag the asset as leased.  */  
   "LeaseFlag":boolean,
      /**  Lease amount  */  
   "LeaseValue":number,
      /**  Mileage limit of lease  */  
   "LeaseMileage":number,
      /**  End date of lease.  */  
   "LeaseEndDate":string,
      /**  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   "WarehouseCode":string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   "BinNum":string,
      /**  Freeform field for the location of tha aaset.  */  
   "Location":string,
      /**  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  */  
   "OverideCost":number,
      /**  Residual value of the asset  */  
   "ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "CYDisposalCost":number,
      /**  Disposal proceed amount.  */  
   "CYDisposalProceeds":number,
      /**  Current cost value of the asset.  */  
   "CurrentCostvalue":number,
      /**  The amount the asset is acquired for.  */  
   "Acquire":number,
      /**  Path and filename of asset image file.  */  
   "ImageFileName":string,
      /**  A unique code that identifies the Company currency.  */  
   "CurrencyCode":string,
      /**  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  */  
   "AssetStatus":string,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "AcquisitionCost":number,
      /**  Associates the Asset with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  Tag number. This will keep the asset label.  */  
   "TagNum":string,
      /**  The total Grant amount recorded for this Asset.  */  
   "CurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "DocResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "DocReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "DocCYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "DocCYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "DocAcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in document currency.  */  
   "DocCurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "Rpt1ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "Rpt1ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt1CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt1CYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt1AcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   "Rpt1CurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "Rpt2ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "Rpt2ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt2CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt2CYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt2AcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   "Rpt2CurrentGrantAmt":number,
      /**  Residual value of the asset  */  
   "Rpt3ResidualValue":number,
      /**  Replacement value of the asset. For information purposes only.  */  
   "Rpt3ReplaceValue":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt3CYAdditionCost":number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   "Rpt3CYDisposalCost":number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   "Rpt3AcquisitionCost":number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   "Rpt3CurrentGrantAmt":number,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  Tax Code (Mexico Localization field)  */  
   "MXTaxCode":string,
      /**  Tax Rate (Mexico Localization field)  */  
   "MXTaxRate":string,
      /**  Investment Value (Mexico Localization field)  */  
   "MXInvestAmount":number,
      /**  Mexico Tax Amount (Mexico Localization field)  */  
   "MXTaxAmount":number,
      /**  Annual depreciation Percentage (Mexico Localization field)  */  
   "MXAnnualDepre":number,
      /**  Invoice Line  (Mexico Localization field)  */  
   "InvoiceLine":number,
      /**  Mexico Asset Life (Mexico Localization field)  */  
   "MXAssetLife":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "CYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "DocCYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt1CYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt2CYImpairCost":number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   "Rpt3CYImpairCost":number,
      /**  Current cost value of the asset in document currency.  */  
   "DocCurrentCostValue":number,
      /**  Current cost value of the asset in reporting currency.  */  
   "Rpt1CurrentCostvalue":number,
      /**  Current cost value of the asset in reporting currency.  */  
   "Rpt2CurrentCostvalue":number,
      /**  Current cost value of the asset in reporting currency.  */  
   "Rpt3CurrentCostValue":number,
      /**  Location ID.  */  
   "LocID":string,
      /**  Disposal proceed amount.  */  
   "DocCYDisposalProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt1CYDisposalProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt2CYDisposalProceeds":number,
      /**  Disposal proceed amount.  */  
   "Rpt3CYDisposalProceeds":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "CYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "DocCYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt1CYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt2CYAdditionGrant":number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   "Rpt3CYAdditionGrant":number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   "InspPlanPartNum":string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   "SpecID":string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   "LastCalDate":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  */  
   "DepRecalcNeeded":boolean,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   "EquipID":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  */  
   "AssetUnits":number,
      /**  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   "Lineage":string,
      /**  Insurance premium in document currency.  */  
   "DocInsurancePremium":number,
      /**  Insurance premium in Reporting Currency.  */  
   "Rpt1InsurancePremium":number,
      /**  Insurance premium in Reporting Currency.  */  
   "Rpt2InsurancePremium":number,
      /**  Insurance premium in Reporting Currency.  */  
   "Rpt3InsurancePremium":number,
      /**  Lease amount in document currency.  */  
   "DocLeaseValue":number,
      /**  Lease amount in Reporting Currency.  */  
   "Rpt1LeaseValue":number,
      /**  Lease amount in Rocument Currency.  */  
   "Rpt2LeaseValue":number,
      /**  Lease amount in Reporting Currency.  */  
   "Rpt3LeaseValue":number,
      /**  Insurance Value  */  
   "InsuranceValue":number,
      /**  Insurance Value in document currency.  */  
   "DocInsuranceValue":number,
      /**  Insurance Value in Reporting Currency.  */  
   "Rpt1InsuranceValue":number,
      /**  Insurance Value in Reporting Currency.  */  
   "Rpt2InsuranceValue":number,
      /**  Insurance Value in Reporting Currency.  */  
   "Rpt3InsuranceValue":number,
      /**  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  */  
   "InsPremiumModifier":string,
      /**  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  */  
   "LeaseModifier":string,
      /**  The Project Phase ID of this asset.  */  
   "PhaseID":string,
      /**  Lease Number of the asset.  */  
   "LeaseNum":string,
      /**  The Leasing Company.  */  
   "LeaseCompany":string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpAnnualCharge":number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpPeriodCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleAnnualCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRulePeriodCharge":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ImageID  */  
   "ImageID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  Department  */  
   "Department":string,
      /**  UOM  */  
   "UOM":string,
      /**  CNUsageStatus  */  
   "CNUsageStatus":string,
      /**  CNUsagePercent  */  
   "CNUsagePercent":number,
      /**  Imported for Processing Trade  */  
   "CNImportedForProcessingTrade":boolean,
      /**  Declaration Bill  */  
   "CNDeclarationBill":string,
      /**  HS Commodity Code  */  
   "CommodityCode":string,
      /**  Declaration Date  */  
   "CNDeclarationDate":string,
      /**  Control Due Date  */  
   "CNControlDueDate":string,
      /**  Manufacturing Date  */  
   "CNManufacturingDate":string,
      /**  Country of Origin  */  
   "CNOrigCountryNum":number,
      /**  Specification  */  
   "CNSpecification":string,
   "BaseCurrencyID":string,
   "BinDescription":string,
      /**  CNDeptChangeReason  */  
   "CNDeptChangeReason":string,
      /**  CNLocChangeReason  */  
   "CNLocChangeReason":string,
   "IsPosted":boolean,
      /**  Mexico Localization Field  */  
   "MXTaxCatID":string,
   "PhaseDescription":string,
   "AdditionSpread":boolean,
   "EquipCreate":boolean,
   "FinalSpread":boolean,
      /**  Path name of the Asset Image or Photo  */  
   "ImagePath":string,
   "BitFlag":number,
   "AssetGrpDescDescription":string,
   "ClassDescription":string,
   "CommodityCodeDescription":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrencyID":string,
   "LocIDDescription":string,
   "MachineDescDescription":string,
   "ResrceGrpDescDescription":string,
   "VendorNumVendorID":string,
   "VendorNumCity":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "WarehouseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipSupplier
      @param ipInvoiceNum
      @param ipInvoiceLine
      @param ipTaxCode
      @param ipRateCode
   */  
export interface CalcTaxAmtLine_input{
      /**  Supplier Invoice Line that was entered.  */  
   ipSupplier:number,
      /**  Invoice Num that was entered.  */  
   ipInvoiceNum:string,
      /**  Invoice Line that was entered.  */  
   ipInvoiceLine:number,
      /**  Tax Code Invoice Line that was entered.  */  
   ipTaxCode:string,
      /**  Rate Code Invoice Line that was entered.  */  
   ipRateCode:string,
}

export interface CalcTaxAmtLine_output{
parameters : {
      /**  output parameters  */  
   opInvestAmount:number,
   opTaxAmount:number,
}
}

   /** Required : 
      @param ipAssetMethod
      @param ds
   */  
export interface ChangeAssetMethod_input{
      /**  The Method proposed value  */  
   ipAssetMethod:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface ChangeAssetMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipAssetRegister
      @param ds
   */  
export interface ChangeAssetRegister_input{
      /**  The Register proposed value  */  
   ipAssetRegister:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface ChangeAssetRegister_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param assetNum
   */  
export interface DeleteByID_input{
   assetNum:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param sourceAssetNum
      @param assetNum
      @param assetDesc
      @param acquiredDate
      @param commissionedDate
      @param dupCost
      @param additionDate
      @param dateKind
   */  
export interface Duplicate_input{
      /**  Source Asset ID  */  
   sourceAssetNum:string,
      /**  New Asset Number  */  
   assetNum:string,
      /**  New Asset Description  */  
   assetDesc:string,
      /**  New Acquisition Date  */  
   acquiredDate:string,
      /**  New Placed In Service Date  */  
   commissionedDate:string,
      /**  Indicates whether an Addition is to be created. When true, Source Asset Cost is used as Addition Cost  */  
   dupCost:boolean,
      /**  Addition Date. Used when ipDupCost is true  */  
   additionDate:string,
      /**  Date Kind. When ACQ, additionDate is used for Acquisition and Placed In Service Dates; when PSD, additionDate is used for Placed in Service Date  */  
   dateKind:string,
}

export interface Duplicate_output{
   returnObj:Erp_Tablesets_FAssetTableset[],
parameters : {
      /**  output parameters  */  
   warning:string,
}
}

export interface Erp_Tablesets_ChildAssetsRow{
      /**  Company  */  
   Company:string,
      /**  Asset Number  */  
   AssetNum:string,
      /**  Asset Description  */  
   AssetDescription:string,
      /**  Parent Asset Number  */  
   ParentAsset:string,
      /**  Inactive  */  
   Inactive:boolean,
      /**  Asset Sequence  */  
   AssetSeq:number,
      /**  Parent Asset Sequence  */  
   ParentAssetSeq:number,
   AssetStatus:string,
   TagNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAssetAttchRow{
   Company:string,
   AssetNum:string,
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

export interface Erp_Tablesets_FAssetDtlAttchRow{
   Company:string,
   AssetNum:string,
   AssetRegID:string,
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

export interface Erp_Tablesets_FAssetDtlRow{
      /**  Company of the asset.  */  
   Company:string,
      /**  Identifier of the asset  */  
   AssetNum:string,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  */  
   AdditionSpread:boolean,
      /**  Identifier of the spread code table that will be used for the Addition Spread option.  */  
   SpreadCode:string,
      /**  In case of life depreciation method the life modifier expresses the unit of measure of life. Values are: Periods and Years.  */  
   LifeModifier:string,
      /**  The Depreciation Rate that will be used to calculate the Annual Charge.  */  
   AnnualDepRate:number,
      /**  Number of periods or years - unit defined in the Life Modifier.  */  
   AssetLife:number,
      /**  Current year opening depreciation  */  
   CYOpenDepn:number,
      /**  Current year opening bookvalue  */  
   CYOpenBookValue:number,
      /**  Current year opening grant depreciation  */  
   CYOpenGrantDepn:number,
      /**  Current year opening grant bookvalue  */  
   CYOpenGrantBookValue:number,
      /**  Depreciation applied in previous years through addition this year.  */  
   CYAddPrevDepn:number,
      /**  Current year depreciation  */  
   CYAddCurrDepn:number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   CYAddBookvalue:number,
      /**  Depreciation applied in previous years through disposal this year.  */  
   CYDispPrevDepn:number,
      /**  Depreciation applied this year through addition this year.  */  
   CYDispCurrDepn:number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   CYDispBookValue:number,
      /**  Depreciated in previous years  */  
   CurrentPrevYearDepn:number,
      /**  Depreciated (and posted) in the current year.  */  
   CurrentPostedDepn:number,
      /**  The current bookvalue.  */  
   CurrentBookvalue:number,
      /**  Depreciations open for this year.  */  
   CurrentUnpostedDepn:number,
      /**  The projected bookvalue at the end of this year.  */  
   CurrentYEBookvalue:number,
      /**  Identifier of the depreciation method table.  */  
   AssetMethod:string,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   BookID:string,
      /**  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  */  
   CalendarID:string,
      /**  Convention used for the depreciation calculation of the asset.  This will determine how depreciation is prorated for the year in which the asset is placed in service.  Valid values are: "HY" (Half Year); "MM" (Mid Month); "QR" (Quarter); "MQ" (Mid Quarter); "FM" (Full Month); "EM" (Entire Month); "SD" (Service Date), "NM" (Next Month), and "AD" (Acquisition Date).  This field can be blank.  */  
   DepConvention:string,
      /**  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  */  
   RetroAdjust:boolean,
      /**  Production Unit Spread Code.  */  
   ProdUnitSpread:string,
      /**  Total Production Units.  This could be the total production units per Year or per Period depending on the depreciation charge basis of the asset depreciation method.  */  
   TotalProdUnit:number,
      /**  The Fixed Value that will be used as the Annual Charge amount during the asset depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the annual charge calculation.  */  
   AnnualFixedValue:number,
      /**  Annual Charge Spread Code  */  
   AnnualSpread:string,
      /**  The Fixed Value that will be used as the Period Charge amount during the asset period depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the period charge calculation.  */  
   PeriodFixedValue:number,
      /**  Period Charge Spread  */  
   PeriodSpread:string,
      /**  Spread Code used to determine the spread values used when prorating Annual Charge.  */  
   PeriodRateSpread:string,
      /**  Final Spread Code  */  
   FinalSpread:string,
      /**  Indicates if this asset register detail has already switched or used the alternate depreciation method. An asset register is only allowed to switch to an alternate depreciation method once and cannot switch back to original method.  */  
   MethodSwitched:boolean,
      /**  Alternate Depreciation Method  */  
   AltAssetMethod:string,
      /**  Depreciated in previous years  */  
   DocCurrentPrevYearDepn:number,
      /**  Depreciated (and posted) in the current year.  */  
   DocCurrentPostedDepn:number,
      /**  The current bookvalue.  */  
   DocCurrentBookvalue:number,
      /**  Depreciations open for this year.  */  
   DocCurrentUnpostedDepn:number,
      /**  The projected bookvalue at the end of this year.  */  
   DocCurrentYEBookvalue:number,
      /**  Depreciated in previous years  */  
   Rpt1CurrentPrevYearDepn:number,
      /**  Depreciated (and posted) in the current year.  */  
   Rpt1CurrentPostedDepn:number,
      /**  The current bookvalue.  */  
   Rpt1CurrentBookvalue:number,
      /**  Depreciations open for this year.  */  
   Rpt1CurrentUnpostedDepn:number,
      /**  The projected bookvalue at the end of this year.  */  
   Rpt1CurrentYEBookvalue:number,
      /**  Depreciated in previous years  */  
   Rpt2CurrentPrevYearDepn:number,
      /**  Depreciated (and posted) in the current year.  */  
   Rpt2CurrentPostedDepn:number,
      /**  The current bookvalue.  */  
   Rpt2CurrentBookvalue:number,
      /**  Depreciations open for this year.  */  
   Rpt2CurrentUnpostedDepn:number,
      /**  The projected bookvalue at the end of this year.  */  
   Rpt2CurrentYEBookvalue:number,
      /**  Depreciated in previous years  */  
   Rpt3CurrentPrevYearDepn:number,
      /**  Depreciated (and posted) in the current year.  */  
   Rpt3CurrentPostedDepn:number,
      /**  The current bookvalue.  */  
   Rpt3CurrentBookvalue:number,
      /**  Depreciations open for this year.  */  
   Rpt3CurrentUnpostedDepn:number,
      /**  The projected bookvalue at the end of this year.  */  
   Rpt3CurrentYEBookvalue:number,
      /**  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  */  
   UseFinalSpread:boolean,
      /**  System maintained field.  Indicates that asset depreciation needs to be recalculated for this depreciation method.  */  
   DepRecalcNeeded:boolean,
      /**  Grant Depreciation in previous years  */  
   CurrentGrantPYDepn:number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   CurrentGrantPostedDepn:number,
      /**  The current grant book value.  */  
   CurrentGrantBookValue:number,
      /**  Grant Depreciations open for this year.  */  
   CurrentGrantUnpostedDepn:number,
      /**  The projected grant bookvalue at the end of this year.  */  
   CurrentGrantYEBookValue:number,
      /**  Grant Depreciation in previous years  */  
   DocCurrentGrantPYDepn:number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   DocCurrentGrantPostedDepn:number,
      /**  The current grant book value.  */  
   DocCurrentGrantBookValue:number,
      /**  Grant Depreciations open for this year.  */  
   DocCurrentGrantUnpostedDepn:number,
      /**  The projected grant bookvalue at the end of this year.  */  
   DocCurrentGrantYEBookValue:number,
      /**  Grant Depreciation in previous years  */  
   Rpt1CurrentGrantPYDepn:number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   Rpt1CurrentGrantPostedDepn:number,
      /**  The current grant book value.  */  
   Rpt1CurrentGrantBookValue:number,
      /**  Grant Depreciations open for this year.  */  
   Rpt1CurrentGrantUnpostedDepn:number,
      /**  The projected grant bookvalue at the end of this year.  */  
   Rpt1CurrentGrantYEBookValue:number,
      /**  Grant Depreciation in previous years  */  
   Rpt2CurrentGrantPYDepn:number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   Rpt2CurrentGrantPostedDepn:number,
      /**  The current grant book value.  */  
   Rpt2CurrentGrantBookValue:number,
      /**  Grant Depreciations open for this year.  */  
   Rpt2CurrentGrantUnpostedDepn:number,
      /**  The projected grant bookvalue at the end of this year.  */  
   Rpt2CurrentGrantYEBookValue:number,
      /**  Grant Depreciation in previous years  */  
   Rpt3CurrentGrantPYDepn:number,
      /**  Grant Depreciation (and posted) in the current year.  */  
   Rpt3CurrentGrantPostedDepn:number,
      /**  The current grant book value.  */  
   Rpt3CurrentGrantBookValue:number,
      /**  Grant Depreciations open for this year.  */  
   Rpt3CurrentGrantUnpostedDepn:number,
      /**  The projected grant bookvalue at the end of this year.  */  
   Rpt3CurrentGrantYEBookValue:number,
      /**  Current year opening bookvalue  */  
   DocCYOpenBookValue:number,
      /**  Previous years addition depreciation  */  
   DocCYAddPrevDepn:number,
      /**  Current year addition depreciation  */  
   DocCYAddCurrDepn:number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   DocCYAddBookValue:number,
      /**  Previous years Disposal depreciation  */  
   DocCYDispPrevDepn:number,
      /**  Current year Disposal depreciation  */  
   DocCYDispCurrDepn:number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   DocCYDispBookValue:number,
      /**  Current year opening bookvalue  */  
   Rpt1CYOpenBookValue:number,
      /**  Previous years Addition depreciation  */  
   Rpt1CYAddPrevDepn:number,
      /**  Current year Addition depreciation  */  
   Rpt1CYAddCurrDepn:number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   Rpt1CYAddBookValue:number,
      /**  Previous years Disposal depreciation  */  
   Rpt1CYDispPrevDepn:number,
      /**  Current year Disposal depreciation  */  
   Rpt1CYDispCurrDepn:number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   Rpt1CYDispBookValue:number,
      /**  Current year opening bookvalue  */  
   Rpt2CYOpenBookValue:number,
      /**  Previous years Addition depreciation  */  
   Rpt2CYAddPrevDepn:number,
      /**  Current year Addition depreciation  */  
   Rpt2CYAddCurrDepn:number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   Rpt2CYAddBookValue:number,
      /**  Previous years Disposal depreciation  */  
   Rpt2CYDispPrevDepn:number,
      /**  Current year Disposal depreciation  */  
   Rpt2CYDispCurrDepn:number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   Rpt2CYDispBookValue:number,
      /**  Current year opening bookvalue  */  
   Rpt3CYOpenBookValue:number,
      /**  Previous years Addition depreciation  */  
   Rpt3CYAddPrevDepn:number,
      /**  Current year Addition depreciation  */  
   Rpt3CYAddCurrDepn:number,
      /**  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  */  
   Rpt3CYAddBookValue:number,
      /**  Previous years Disposal depreciation  */  
   Rpt3CYDispPrevDepn:number,
      /**  Current year Disposal depreciation  */  
   Rpt3CYDispCurrDepn:number,
      /**  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  */  
   Rpt3CYDispBookValue:number,
      /**  Current year opening grant depreciation  */  
   DocCYOpenGrantDepn:number,
      /**  Current year opening grant depreciation  */  
   Rpt1CYOpenGrantDepn:number,
      /**  Current year opening grant depreciation  */  
   Rpt2CYOpenGrantDepn:number,
      /**  Current year opening grant depreciation  */  
   Rpt3CYOpenGrantDepn:number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   DepRecalcDate:string,
      /**  This is the initial book value of the entire asset depreciation schedule.  */  
   InitBookValue:number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   DocInitBookValue:number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   Rpt1InitBookValue:number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   Rpt2InitBookValue:number,
      /**  This is the Initial book value of the entire asset depreciation schedule.  */  
   Rpt3InitBookValue:number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   InitGrantBookValue:number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   DocInitGrantBookValue:number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   Rpt1InitGrantBookValue:number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   Rpt2InitGrantBookValue:number,
      /**  This is the Initial grant book value of the entire asset depreciation schedule.  */  
   Rpt3InitGrantBookValue:number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   CYImpBookValue:number,
      /**  Previous years Disposal Grant depreciation  */  
   CYDispGrantPrevDepn:number,
      /**  Current year Disposal Grant depreciation  */  
   CYDispGrantCurrDepn:number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   CYDispGrantBookValue:number,
      /**  Current year opening grant bookvalue  */  
   DocCYOpenGrantBookValue:number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   DocCYImpBookValue:number,
      /**  Previous years Disposal Grant depreciation  */  
   DocCYDispGrantPrevDepn:number,
      /**  Current year Disposal Grant depreciation  */  
   DocCYDispGrantCurrDepn:number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   DocCYDispGrantBookValue:number,
      /**  Current year opening grant bookvalue  */  
   Rpt1CYOpenGrantBookValue:number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   Rpt1CYImpBookValue:number,
      /**  Previous years Disposal Grant depreciation  */  
   Rpt1CYDispGrantPrevDepn:number,
      /**  Current year Disposal Grant depreciation  */  
   Rpt1CYDispGrantCurrDepn:number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   Rpt1CYDispGrantBookValue:number,
      /**  Current year opening grant bookvalue  */  
   Rpt2CYOpenGrantBookValue:number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   Rpt2CYImpBookValue:number,
      /**  Previous years Disposal Grant depreciation  */  
   Rpt2CYDispGrantPrevDepn:number,
      /**  Current year Disposal Grant depreciation  */  
   Rpt2CYDispGrantCurrDepn:number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   Rpt2CYDispGrantBookValue:number,
      /**  Current year opening grant bookvalue  */  
   Rpt3CYOpenGrantBookValue:number,
      /**  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  */  
   Rpt3CYImpBookValue:number,
      /**  Previous years Disposal Grant depreciation  */  
   Rpt3CYDispGrantPrevDepn:number,
      /**  Current year Disposal Grant depreciation  */  
   Rpt3CYDispGrantCurrDepn:number,
      /**  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  */  
   Rpt3CYDispGrantBookValue:number,
      /**  Current year opening depreciation  */  
   DocCYOpenDepn:number,
      /**  Current year opening depreciation  */  
   Rpt1CYOpenDepn:number,
      /**  Current year opening depreciation  */  
   Rpt2CYOpenDepn:number,
      /**  Current year opening depreciation  */  
   Rpt3CYOpenDepn:number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   CurrentActPrevDepn:number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   CurrentActPostedDepn:number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   DocCurrentActPrevDepn:number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   DocCurrentActPostedDepn:number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   Rpt1CurrentActPrevDepn:number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   Rpt1CurrentActPostedDepn:number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   Rpt2CurrentActPrevDepn:number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   Rpt2CurrentActPostedDepn:number,
      /**  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  */  
   Rpt3CurrentActPrevDepn:number,
      /**  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  */  
   Rpt3CurrentActPostedDepn:number,
      /**  Previous years Addition Grant depreciation  */  
   CYAddGrantPrevDepn:number,
      /**  Previous years Addition Grant depreciation  */  
   CYAddGrantCurrDepn:number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   CYAddGrantBookValue:number,
      /**  Previous years Addition Grant depreciation  */  
   DocCYAddGrantPrevDepn:number,
      /**  Current year Addition Grant depreciation  */  
   DocCYAddGrantCurrDepn:number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   DocCYAddGrantBookValue:number,
      /**  Previous years Addition Grant depreciation  */  
   Rpt1CYAddGrantPrevDepn:number,
      /**  Current year Addition Grant depreciation  */  
   Rpt1CYAddGrantCurrDepn:number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   Rpt1CYAddGrantBookValue:number,
      /**  Previous years Addition Grant depreciation  */  
   Rpt2CYAddGrantPrevDepn:number,
      /**  Current year Addition Grant depreciation  */  
   Rpt2CYAddGrantCurrDepn:number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   Rpt2CYAddGrantBookValue:number,
      /**  Previous years Addition Grant depreciation  */  
   Rpt3CYAddGrantPrevDepn:number,
      /**  Current year Addition Grant depreciation  */  
   Rpt3CYAddGrantCurrDepn:number,
      /**  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  */  
   Rpt3CYAddGrantBookValue:number,
      /**  Depreciation Flag. When true then the asset register will be processed in the depreciation recalculation process and the depreciation posting process.  If set to false then all depreciation parameters are blank and not updatable.  */  
   Depreciate:boolean,
      /**  Current year opening cost  */  
   CYOpenCost:number,
      /**  Current year opening cost  */  
   DocCYOpenCost:number,
      /**  Current year opening cost  */  
   Rpt1CYOpenCost:number,
      /**  Current year opening cost  */  
   Rpt2CYOpenCost:number,
      /**  Current year opening cost  */  
   Rpt3CYOpenCost:number,
      /**  Current year opening grant amount  */  
   CYOpenGrant:number,
      /**  Current year opening cost  */  
   DocCYOpenGrant:number,
      /**  Current year opening cost  */  
   Rpt1CYOpenGrant:number,
      /**  Current year opening cost  */  
   Rpt2CYOpenGrant:number,
      /**  Current year opening cost  */  
   Rpt3CYOpenGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   CYAddCost:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   DocCYAddCost:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt1CYAddCost:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt2CYAddCost:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt3CYAddCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   CYImpCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   DocCYImpCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt1CYImpCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt2CYImpCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt3CYImpCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   CYDispCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   DocCYDispCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt1CYDispCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt2CYDispCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt3CYDispCost:number,
      /**  Disposal proceed amount.  */  
   CYDispProceeds:number,
      /**  Disposal proceed amount.  */  
   DocCYDispProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt1CYDispProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt2CYDispProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt3CYDispProceeds:number,
      /**  Disposal profit/loss amount.  */  
   CYDispProfit:number,
      /**  Disposal profit/loss amount.  */  
   DocCYDispProfit:number,
      /**  Disposal profit/loss amount.  */  
   Rpt1CYDispProfit:number,
      /**  Disposal profit/loss amount.  */  
   Rpt2CYDispProfit:number,
      /**  Disposal profit/loss amount.  */  
   Rpt3CYDispProfit:number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   CYAddGrant:number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   DocCYAddGrant:number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   Rpt1CYAddGrant:number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   Rpt2CYAddGrant:number,
      /**  Current Addition Grant is the grant amount added to the asset  this year.  */  
   Rpt3CYAddGrant:number,
      /**  Current cost value of the asset.  */  
   CurrentCostvalue:number,
      /**  Current cost value of the asset.  */  
   DocCurrentCostvalue:number,
      /**  Current cost value of the asset.  */  
   Rpt1CurrentCostvalue:number,
      /**  Current cost value of the asset.  */  
   Rpt2CurrentCostvalue:number,
      /**  Current cost value of the asset.  */  
   Rpt3CurrentCostvalue:number,
      /**  Current Grant Amount of the asset.  */  
   CurrentGrantAmt:number,
      /**  Current Grant Amount of the asset.  */  
   DocCurrentGrantAmt:number,
      /**  Current Grant Amount of the asset.  */  
   Rpt1CurrentGrantAmt:number,
      /**  Current Grant Amount of the asset.  */  
   Rpt2CurrentGrantAmt:number,
      /**  Current Grant Amount of the asset.  */  
   Rpt3CurrentGrantAmt:number,
      /**  The Rate Factor is used as a multiplier when calculating Annual Depreciation Charge using the Declining Balance formula.  */  
   RateFactor:number,
      /**  Residual value of the asset  */  
   ResidualValue:number,
      /**  Residual value of the asset in document currency  */  
   DocResidualValue:number,
      /**  Residual value of the asset in reporting currency  */  
   Rpt1ResidualValue:number,
      /**  Residual value of the asset in reporting currency  */  
   Rpt2ResidualValue:number,
      /**  Residual value of the asset in reporting currency  */  
   Rpt3ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   ReplaceValue:number,
      /**  Replacement value of the asset in document currency. For information purposes only.  */  
   DocReplaceValue:number,
      /**  Replacement value of the asset in reporting currency. For information purposes only.  */  
   Rpt1ReplaceValue:number,
      /**  Replacement value of the asset in reporting currency. For information purposes only.  */  
   Rpt2ReplaceValue:number,
      /**  Replacement value of the asset in reporting currency. For information purposes only.  */  
   Rpt3ReplaceValue:number,
      /**  The end date of the last posted depreciation period that has affected the book value of this asset register detail.  */  
   BookValueDate:string,
      /**  This is the starting date of the fiscal year or fiscal period when the actual switch of the depreciation method to the alternative method happened.  */  
   DateSwitched:string,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   CurrActGrantPostedDepn:number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   DocCurrActGrantPostedDepn:number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   Rpt1CurrActGrantPostedDepn:number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   Rpt2CurrActGrantPostedDepn:number,
      /**  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  */  
   Rpt3CurrActGrantPostedDepn:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   AcquisitionCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   DocAcquisitionCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt1AcquisitionCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt2AcquisitionCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt3AcquisitionCost:number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   CYDispGrant:number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   DocCYDispGrant:number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   Rpt1CYDispGrant:number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   Rpt2CYDispGrant:number,
      /**  Current Disposal Grant is the grant amount disposed from the asset  this year.  */  
   Rpt3CYDispGrant:number,
      /**  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  */  
   DynamicDepYear:boolean,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   CYRevalueGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   DocCYRevalueGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt1CYRevalueGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt2CYRevalueGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt3CYRevalueGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   CYDepRevalGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   DocCYDepRevalGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt1CYDepRevalGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt2CYDepRevalGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt3CYDepRevalGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   CYRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   DocCYRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt1CYRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt2CYRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt3CYRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   CYDepRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   DocCYDepRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt1CYDepRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt2CYDepRevGrantGainLoss:number,
      /**  The original Current Asset Cost before running the Asset Revaluation process.  */  
   Rpt3CYDepRevGrantGainLoss:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Determines how depreciation is calculated in the period of disposal or revaluation.  */  
   DepOnDisposal:number,
      /**  Date of actual depreciation schedule start.  */  
   ActDepStartDate:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
   CurrencySymbol:string,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   CYDispTotalDepn:number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   DocCYDispTotalDepn:number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   DocRevalueGainLoss:number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   DocYTDAccumDepn:number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   DocYTDAddCost:number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   DocYTDDispCost:number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   DocYTDGrantDepn:number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   DocYTDImpCost:number,
   EnableAnnualDepRate:boolean,
   EnableAssetLife:boolean,
   EnableProdUnitsSpread:boolean,
   EnableRateFactor:boolean,
   EnableTotalProductionUnits:boolean,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   RevalueGainLoss:number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   Rpt1CYDispTotalDepn:number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   Rpt1RevalueGainLoss:number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   Rpt1YTDAccumDepn:number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   Rpt1YTDAddCost:number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   Rpt1YTDDispCost:number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   Rpt1YTDGrantDepn:number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   Rpt1YTDImpCost:number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   Rpt2CYDispTotalDepn:number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   Rpt2RevalueGainLoss:number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   Rpt2YTDAccumDepn:number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   Rpt2YTDAddCost:number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   Rpt2YTDDispCost:number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   Rpt2YTDGrantDepn:number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   Rpt2YTDImpCost:number,
      /**  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  */  
   Rpt3CYDispTotalDepn:number,
      /**  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  */  
   Rpt3RevalueGainLoss:number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   Rpt3YTDAccumDepn:number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   Rpt3YTDAddCost:number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   Rpt3YTDDispCost:number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   Rpt3YTDGrantDepn:number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   Rpt3YTDImpCost:number,
      /**  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  */  
   YTDAccumDepn:number,
      /**  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  */  
   YTDAddCost:number,
      /**  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  */  
   YTDDispCost:number,
      /**  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  */  
   YTDGrantDepn:number,
      /**  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  */  
   YTDImpCost:number,
   CurrencyCode:string,
   BitFlag:number,
   AddSpreadDescription:string,
   AltAssetMethodProrateType:string,
   AltAssetMethodFinalspread:boolean,
   AltAssetMethodDescription:string,
   AltAssetMethodAnnualChargeType:string,
   AltAssetMethodPeriodChargeType:string,
   AltAssetMethodDepChargeBasis:string,
   AnnualSpreadDescription:string,
   FAMethodFinalspread:boolean,
   FAMethodDescription:string,
   FAMethodAnnualChargeType:string,
   FAMethodProrateType:string,
   FAMethodDepChargeBasis:string,
   FAMethodPeriodChargeType:string,
   FAssetRegDescription:string,
   FinalSpreadDescription:string,
   FiscalCalDescription:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
   PeriodSpreadDescription:string,
   ProdSpreadDescription:string,
   RateSpreadDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAssetListRow{
      /**  Company of the asset.  */  
   Company:string,
      /**  Identifier of the asset  */  
   AssetNum:string,
      /**  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  */  
   AssetSeq:number,
      /**  Mandatory description of the asset.  */  
   AssetDescription:string,
      /**  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  */  
   InActive:boolean,
      /**  Asset parent of this asset  */  
   ParentAsset:string,
      /**  Informational indication of a newly bought asset.  */  
   NewAssetFlag:boolean,
      /**  The code of the mandatory asset group.  */  
   GroupCode:string,
      /**  Identifier of the asset class.  */  
   ClassCode:string,
      /**  Identifier of the Resource Group of the asset. For informational purposes only.  */  
   ResourceGroupID:string,
      /**  The Resource identifier of the asset. For informational purposes only.  */  
   ResourceID:string,
      /**  Date of acquisition of the asset.  */  
   AcquiredDate:string,
      /**  Date of placing the asset in service. Also the start date of depreciation.  */  
   CommissionedDate:string,
      /**  Identifier of the vendor of the asset.  */  
   VendorNum:number,
      /**  The name of the vendor. The name can be entered without entering a vendor.  */  
   VendorName:string,
      /**  The po number the asset purchase order.  */  
   PONum:number,
      /**  The invoice number of asset invoice.  */  
   InvoiceNum:string,
      /**  The job that created the asset.  */  
   JobNum:string,
      /**  The serial number of the asset.  */  
   Serialno:string,
      /**  The original manufacturer of the asset.  */  
   Manufacturer:string,
      /**  The model of the asset.  */  
   Model:string,
      /**  Insurance policy for the asset.  */  
   InsurancePolicy:string,
      /**  The insurance company.  */  
   InsuranceCompany:string,
      /**  Insurance premium  */  
   InsurancePremium:number,
      /**  Insurance RenewalDate  */  
   InsuranceRenewalDate:string,
      /**  The insurer.  */  
   InsuranceInsurer:string,
      /**  Flag the asset as leased.  */  
   LeaseFlag:boolean,
      /**  Lease amount  */  
   LeaseValue:number,
      /**  Mileage limit of lease  */  
   LeaseMileage:number,
      /**  End date of lease.  */  
   LeaseEndDate:string,
      /**  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   WarehouseCode:string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   BinNum:string,
      /**  Freeform field for the location of tha aaset.  */  
   Location:string,
      /**  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  */  
   OverideCost:number,
      /**  Residual value of the asset  */  
   ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   CYDisposalCost:number,
      /**  Disposal proceed amount.  */  
   CYDisposalProceeds:number,
      /**  Current cost value of the asset.  */  
   CurrentCostvalue:number,
      /**  The amount the asset is acquired for.  */  
   Acquire:number,
      /**  Path and filename of asset image file.  */  
   ImageFileName:string,
      /**  A unique code that identifies the Company currency.  */  
   CurrencyCode:string,
      /**  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  */  
   AssetStatus:string,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   AcquisitionCost:number,
      /**  Associates the Asset with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  Tag number. This will keep the asset label.  */  
   TagNum:string,
      /**  The total Grant amount recorded for this Asset.  */  
   CurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   DocResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   DocReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   DocCYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   DocCYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   DocAcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in document currency.  */  
   DocCurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   Rpt1ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   Rpt1ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt1CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt1CYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt1AcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   Rpt1CurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   Rpt2ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   Rpt2ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt2CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt2CYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt2AcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   Rpt2CurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   Rpt3ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   Rpt3ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt3CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt3CYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt3AcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   Rpt3CurrentGrantAmt:number,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  Tax Code (Mexico Localization field)  */  
   MXTaxCode:string,
      /**  Tax Rate (Mexico Localization field)  */  
   MXTaxRate:string,
      /**  Investment Value (Mexico Localization field)  */  
   MXInvestAmount:number,
      /**  Mexico Tax Amount (Mexico Localization field)  */  
   MXTaxAmount:number,
      /**  Annual depreciation Percentage (Mexico Localization field)  */  
   MXAnnualDepre:number,
      /**  Invoice Line  (Mexico Localization field)  */  
   InvoiceLine:number,
      /**  Mexico Asset Life (Mexico Localization field)  */  
   MXAssetLife:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   CYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   DocCYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt1CYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt2CYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt3CYImpairCost:number,
      /**  Current cost value of the asset in document currency.  */  
   DocCurrentCostValue:number,
      /**  Current cost value of the asset in reporting currency.  */  
   Rpt1CurrentCostvalue:number,
      /**  Current cost value of the asset in reporting currency.  */  
   Rpt2CurrentCostvalue:number,
      /**  Current cost value of the asset in reporting currency.  */  
   Rpt3CurrentCostValue:number,
      /**  Location ID.  */  
   LocID:string,
      /**  Disposal proceed amount.  */  
   DocCYDisposalProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt1CYDisposalProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt2CYDisposalProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt3CYDisposalProceeds:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   CYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   DocCYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt1CYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt2CYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt3CYAdditionGrant:number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   InspPlanPartNum:string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   SpecID:string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   LastCalDate:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  */  
   DepRecalcNeeded:boolean,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   EquipID:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  */  
   AssetUnits:number,
      /**  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   Lineage:string,
      /**  Insurance premium in document currency.  */  
   DocInsurancePremium:number,
      /**  Insurance premium in Reporting Currency.  */  
   Rpt1InsurancePremium:number,
      /**  Insurance premium in Reporting Currency.  */  
   Rpt2InsurancePremium:number,
      /**  Insurance premium in Reporting Currency.  */  
   Rpt3InsurancePremium:number,
      /**  Lease amount in document currency.  */  
   DocLeaseValue:number,
      /**  Lease amount in Reporting Currency.  */  
   Rpt1LeaseValue:number,
      /**  Lease amount in Rocument Currency.  */  
   Rpt2LeaseValue:number,
      /**  Lease amount in Reporting Currency.  */  
   Rpt3LeaseValue:number,
      /**  Insurance Value  */  
   InsuranceValue:number,
      /**  Insurance Value in document currency.  */  
   DocInsuranceValue:number,
      /**  Insurance Value in Reporting Currency.  */  
   Rpt1InsuranceValue:number,
      /**  Insurance Value in Reporting Currency.  */  
   Rpt2InsuranceValue:number,
      /**  Insurance Value in Reporting Currency.  */  
   Rpt3InsuranceValue:number,
      /**  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  */  
   InsPremiumModifier:string,
      /**  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  */  
   LeaseModifier:string,
      /**  The Project Phase ID of this asset.  */  
   PhaseID:string,
      /**  Lease Number of the asset.  */  
   LeaseNum:string,
      /**  The Leasing Company.  */  
   LeaseCompany:string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpAnnualCharge:number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpPeriodCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleAnnualCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRulePeriodCharge:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Department  */  
   Department:string,
   IsPosted:boolean,
   FinalSpread:boolean,
   AdditionSpread:boolean,
   BinDescription:string,
      /**  Mexico Localization Field  */  
   MXTaxCatID:string,
   BaseCurrencyID:string,
      /**  Path name of the Asset Image or Photo  */  
   ImagePath:string,
   EquipCreate:boolean,
   PhaseDescription:string,
      /**  The description of the asset group.  */  
   AssetGrpDescDescription:string,
      /**  Class description.  */  
   ClassDescription:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description the Location.  Cannot be blank.  */  
   LocIDDescription:string,
      /**  Full description of Resource.  */  
   MachineDescDescription:string,
      /**  Long description of the Resource Group.  */  
   ResrceGrpDescDescription:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Description.  */  
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAssetListTableset{
   FAssetList:Erp_Tablesets_FAssetListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FAssetRow{
      /**  Company of the asset.  */  
   Company:string,
      /**  Identifier of the asset  */  
   AssetNum:string,
      /**  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  */  
   AssetSeq:number,
      /**  Mandatory description of the asset.  */  
   AssetDescription:string,
      /**  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  */  
   InActive:boolean,
      /**  Asset parent of this asset  */  
   ParentAsset:string,
      /**  Informational indication of a newly bought asset.  */  
   NewAssetFlag:boolean,
      /**  The code of the mandatory asset group.  */  
   GroupCode:string,
      /**  Identifier of the asset class.  */  
   ClassCode:string,
      /**  Identifier of the Resource Group of the asset. For informational purposes only.  */  
   ResourceGroupID:string,
      /**  The Resource identifier of the asset. For informational purposes only.  */  
   ResourceID:string,
      /**  Date of acquisition of the asset.  */  
   AcquiredDate:string,
      /**  Date of placing the asset in service. Also the start date of depreciation.  */  
   CommissionedDate:string,
      /**  Identifier of the vendor of the asset.  */  
   VendorNum:number,
      /**  The name of the vendor. The name can be entered without entering a vendor.  */  
   VendorName:string,
      /**  The po number the asset purchase order.  */  
   PONum:number,
      /**  The invoice number of asset invoice.  */  
   InvoiceNum:string,
      /**  The job that created the asset.  */  
   JobNum:string,
      /**  The serial number of the asset.  */  
   Serialno:string,
      /**  The original manufacturer of the asset.  */  
   Manufacturer:string,
      /**  The model of the asset.  */  
   Model:string,
      /**  Insurance policy for the asset.  */  
   InsurancePolicy:string,
      /**  The insurance company.  */  
   InsuranceCompany:string,
      /**  Insurance premium  */  
   InsurancePremium:number,
      /**  Insurance RenewalDate  */  
   InsuranceRenewalDate:string,
      /**  The insurer.  */  
   InsuranceInsurer:string,
      /**  Flag the asset as leased.  */  
   LeaseFlag:boolean,
      /**  Lease amount  */  
   LeaseValue:number,
      /**  Mileage limit of lease  */  
   LeaseMileage:number,
      /**  End date of lease.  */  
   LeaseEndDate:string,
      /**  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   WarehouseCode:string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   BinNum:string,
      /**  Freeform field for the location of tha aaset.  */  
   Location:string,
      /**  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  */  
   OverideCost:number,
      /**  Residual value of the asset  */  
   ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   CYDisposalCost:number,
      /**  Disposal proceed amount.  */  
   CYDisposalProceeds:number,
      /**  Current cost value of the asset.  */  
   CurrentCostvalue:number,
      /**  The amount the asset is acquired for.  */  
   Acquire:number,
      /**  Path and filename of asset image file.  */  
   ImageFileName:string,
      /**  A unique code that identifies the Company currency.  */  
   CurrencyCode:string,
      /**  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  */  
   AssetStatus:string,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   AcquisitionCost:number,
      /**  Associates the Asset with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  Tag number. This will keep the asset label.  */  
   TagNum:string,
      /**  The total Grant amount recorded for this Asset.  */  
   CurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   DocResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   DocReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   DocCYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   DocCYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   DocAcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in document currency.  */  
   DocCurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   Rpt1ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   Rpt1ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt1CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt1CYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt1AcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   Rpt1CurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   Rpt2ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   Rpt2ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt2CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt2CYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt2AcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   Rpt2CurrentGrantAmt:number,
      /**  Residual value of the asset  */  
   Rpt3ResidualValue:number,
      /**  Replacement value of the asset. For information purposes only.  */  
   Rpt3ReplaceValue:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt3CYAdditionCost:number,
      /**  Current year disposal cost is the disposal cost  disposed from the asset this year.  */  
   Rpt3CYDisposalCost:number,
      /**  This is the very first Addition Cost recorded for this asset.  */  
   Rpt3AcquisitionCost:number,
      /**  The total Grant amount recorded for this Asset in reporting currency.  */  
   Rpt3CurrentGrantAmt:number,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  Tax Code (Mexico Localization field)  */  
   MXTaxCode:string,
      /**  Tax Rate (Mexico Localization field)  */  
   MXTaxRate:string,
      /**  Investment Value (Mexico Localization field)  */  
   MXInvestAmount:number,
      /**  Mexico Tax Amount (Mexico Localization field)  */  
   MXTaxAmount:number,
      /**  Annual depreciation Percentage (Mexico Localization field)  */  
   MXAnnualDepre:number,
      /**  Invoice Line  (Mexico Localization field)  */  
   InvoiceLine:number,
      /**  Mexico Asset Life (Mexico Localization field)  */  
   MXAssetLife:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   CYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   DocCYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt1CYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt2CYImpairCost:number,
      /**  Current year impairment cost is the cost subtracted from the asset this year.  */  
   Rpt3CYImpairCost:number,
      /**  Current cost value of the asset in document currency.  */  
   DocCurrentCostValue:number,
      /**  Current cost value of the asset in reporting currency.  */  
   Rpt1CurrentCostvalue:number,
      /**  Current cost value of the asset in reporting currency.  */  
   Rpt2CurrentCostvalue:number,
      /**  Current cost value of the asset in reporting currency.  */  
   Rpt3CurrentCostValue:number,
      /**  Location ID.  */  
   LocID:string,
      /**  Disposal proceed amount.  */  
   DocCYDisposalProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt1CYDisposalProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt2CYDisposalProceeds:number,
      /**  Disposal proceed amount.  */  
   Rpt3CYDisposalProceeds:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   CYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   DocCYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt1CYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt2CYAdditionGrant:number,
      /**  Current Addition Cost is the addition cost  added to the asset  this year.  */  
   Rpt3CYAdditionGrant:number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   InspPlanPartNum:string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   SpecID:string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   LastCalDate:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  */  
   DepRecalcNeeded:boolean,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   EquipID:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  */  
   AssetUnits:number,
      /**  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   Lineage:string,
      /**  Insurance premium in document currency.  */  
   DocInsurancePremium:number,
      /**  Insurance premium in Reporting Currency.  */  
   Rpt1InsurancePremium:number,
      /**  Insurance premium in Reporting Currency.  */  
   Rpt2InsurancePremium:number,
      /**  Insurance premium in Reporting Currency.  */  
   Rpt3InsurancePremium:number,
      /**  Lease amount in document currency.  */  
   DocLeaseValue:number,
      /**  Lease amount in Reporting Currency.  */  
   Rpt1LeaseValue:number,
      /**  Lease amount in Rocument Currency.  */  
   Rpt2LeaseValue:number,
      /**  Lease amount in Reporting Currency.  */  
   Rpt3LeaseValue:number,
      /**  Insurance Value  */  
   InsuranceValue:number,
      /**  Insurance Value in document currency.  */  
   DocInsuranceValue:number,
      /**  Insurance Value in Reporting Currency.  */  
   Rpt1InsuranceValue:number,
      /**  Insurance Value in Reporting Currency.  */  
   Rpt2InsuranceValue:number,
      /**  Insurance Value in Reporting Currency.  */  
   Rpt3InsuranceValue:number,
      /**  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  */  
   InsPremiumModifier:string,
      /**  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  */  
   LeaseModifier:string,
      /**  The Project Phase ID of this asset.  */  
   PhaseID:string,
      /**  Lease Number of the asset.  */  
   LeaseNum:string,
      /**  The Leasing Company.  */  
   LeaseCompany:string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpAnnualCharge:number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpPeriodCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleAnnualCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRulePeriodCharge:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ImageID  */  
   ImageID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  Department  */  
   Department:string,
      /**  UOM  */  
   UOM:string,
      /**  CNUsageStatus  */  
   CNUsageStatus:string,
      /**  CNUsagePercent  */  
   CNUsagePercent:number,
      /**  Imported for Processing Trade  */  
   CNImportedForProcessingTrade:boolean,
      /**  Declaration Bill  */  
   CNDeclarationBill:string,
      /**  HS Commodity Code  */  
   CommodityCode:string,
      /**  Declaration Date  */  
   CNDeclarationDate:string,
      /**  Control Due Date  */  
   CNControlDueDate:string,
      /**  Manufacturing Date  */  
   CNManufacturingDate:string,
      /**  Country of Origin  */  
   CNOrigCountryNum:number,
      /**  Specification  */  
   CNSpecification:string,
   BaseCurrencyID:string,
   BinDescription:string,
      /**  CNDeptChangeReason  */  
   CNDeptChangeReason:string,
      /**  CNLocChangeReason  */  
   CNLocChangeReason:string,
   IsPosted:boolean,
      /**  Mexico Localization Field  */  
   MXTaxCatID:string,
   PhaseDescription:string,
   AdditionSpread:boolean,
   EquipCreate:boolean,
   FinalSpread:boolean,
      /**  Path name of the Asset Image or Photo  */  
   ImagePath:string,
   BitFlag:number,
   AssetGrpDescDescription:string,
   ClassDescription:string,
   CommodityCodeDescription:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrencyID:string,
   LocIDDescription:string,
   MachineDescDescription:string,
   ResrceGrpDescDescription:string,
   VendorNumVendorID:string,
   VendorNumCity:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAssetTableset{
   FAsset:Erp_Tablesets_FAssetRow[],
   FAssetAttch:Erp_Tablesets_FAssetAttchRow[],
   ChildAssets:Erp_Tablesets_ChildAssetsRow[],
   FAssetDtl:Erp_Tablesets_FAssetDtlRow[],
   FAssetDtlAttch:Erp_Tablesets_FAssetDtlAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFAssetTableset{
   FAsset:Erp_Tablesets_FAssetRow[],
   FAssetAttch:Erp_Tablesets_FAssetAttchRow[],
   ChildAssets:Erp_Tablesets_ChildAssetsRow[],
   FAssetDtl:Erp_Tablesets_FAssetDtlRow[],
   FAssetDtlAttch:Erp_Tablesets_FAssetDtlAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface ExportData_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param fileName
   */  
export interface ExportProcess_input{
   fileName:string,
}

export interface ExportProcess_output{
parameters : {
      /**  output parameters  */  
   msg:string,
}
}

   /** Required : 
      @param assetNum
   */  
export interface GetByID_input{
   assetNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FAssetTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FAssetTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FAssetTableset[],
}

   /** Required : 
      @param ds
      @param parentAssetNum
   */  
export interface GetChildAssets_input{
   ds:Erp_Tablesets_FAssetTableset[],
      /**  The Parent Asset Number  */  
   parentAssetNum:string,
}

export interface GetChildAssets_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param IP_ServerFileName
   */  
export interface GetClientFileName_input{
   IP_ServerFileName:string,
}

export interface GetClientFileName_output{
   returnObj:string,
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
      @param ipAssetNum
   */  
export interface GetFAssetByID_input{
      /**  New Asset Number  */  
   ipAssetNum:string,
}

export interface GetFAssetByID_output{
   returnObj:Erp_Tablesets_FAssetTableset[],
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
   returnObj:Erp_Tablesets_FAssetListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipParentAssetNum
      @param ds
   */  
export interface GetNewChildAsset_input{
      /**  AssetNum of the current asset.  */  
   ipParentAssetNum:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface GetNewChildAsset_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
   */  
export interface GetNewFAssetAttch_input{
   ds:Erp_Tablesets_FAssetTableset[],
   assetNum:string,
}

export interface GetNewFAssetAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param assetRegID
   */  
export interface GetNewFAssetDtlAttch_input{
   ds:Erp_Tablesets_FAssetTableset[],
   assetNum:string,
   assetRegID:string,
}

export interface GetNewFAssetDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
   */  
export interface GetNewFAssetDtl_input{
   ds:Erp_Tablesets_FAssetTableset[],
   assetNum:string,
}

export interface GetNewFAssetDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFAsset_input{
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface GetNewFAsset_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param whereClauseFAsset
      @param whereClauseFAssetAttch
      @param whereClauseChildAssets
      @param whereClauseFAssetDtl
      @param whereClauseFAssetDtlAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFAsset:string,
   whereClauseFAssetAttch:string,
   whereClauseChildAssets:string,
   whereClauseFAssetDtl:string,
   whereClauseFAssetDtlAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FAssetTableset[],
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
      @param ImportData
      @param ErrorList
   */  
export interface ImportData_input{
   ImportData:any,      //schema had no properties on an object.
   ErrorList:string,
}

export interface ImportData_output{
   returnObj:Erp_Tablesets_FAssetTableset[],
parameters : {
      /**  output parameters  */  
   ErrorList:any[],
}
}

   /** Required : 
      @param fileName
   */  
export interface ImportToDS_input{
   fileName:string,
}

export interface ImportToDS_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMsg:string,
}
}

   /** Required : 
      @param ipAcquiredDate
      @param ds
   */  
export interface LeaveAcquiredDate_input{
      /**  AcquiredDate was entered.  */  
   ipAcquiredDate:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveAcquiredDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipChildAssetNum
      @param ipParentAssetNum
      @param ds
   */  
export interface LeaveChildAssetNum_input{
      /**  AssetNum that was entered.  */  
   ipChildAssetNum:string,
      /**  The current Asset AssetNum.  */  
   ipParentAssetNum:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveChildAssetNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipInsPremium
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveInsPremium_input{
      /**  InsurancePremium that was entered.  */  
   ipInsPremium:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveInsPremium_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipInsValue
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveInsValue_input{
      /**  InsuranceValue that was entered.  */  
   ipInsValue:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveInsValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipInvoiceLine
      @param ds
   */  
export interface LeaveInvoiceLine_input{
      /**  Invoice Line that was entered.  */  
   ipInvoiceLine:number,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipInvoiceNum
      @param ds
   */  
export interface LeaveInvoiceNum_input{
      /**  Invoice Number that was entered.  */  
   ipInvoiceNum:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipJobNum
      @param ds
   */  
export interface LeaveJobNum_input{
      /**  Job Number that was entered.  */  
   ipJobNum:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipLeaseValue
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveLeaseValue_input{
      /**  LeaseValue that was entered.  */  
   ipLeaseValue:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveLeaseValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipPONum
      @param ds
   */  
export interface LeavePONum_input{
      /**  PO Number that is entered.  */  
   ipPONum:number,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeavePONum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipReplaceValue
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveReplaceValue_input{
      /**  ReplaceValue that was entered.  */  
   ipReplaceValue:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveReplaceValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipResidualValue
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveResidualValue_input{
      /**  ResidualValue that was entered.  */  
   ipResidualValue:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveResidualValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param ipVendorID
      @param ds
   */  
export interface LeaveVendorID_input{
      /**  VendorID or SupplierID that was entered.  */  
   ipVendorID:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface LeaveVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param newCommodityCode
      @param ds
   */  
export interface OnChangeCommodityCode_input{
      /**  New Commodity Code  */  
   newCommodityCode:string,
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface OnChangeCommodityCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

   /** Required : 
      @param assetNum
      @param assetRegID
   */  
export interface PostedDepExist_input{
      /**  Asset number  */  
   assetNum:string,
      /**  Asset registry ID  */  
   assetRegID:string,
}

export interface PostedDepExist_output{
parameters : {
      /**  output parameters  */  
   depExist:boolean,
}
}

   /** Required : 
      @param oldAssetNum
      @param acquiredDate
      @param commissionedDate
      @param dupCost
      @param additionDate
   */  
export interface PreDuplicate_input{
      /**  Original Asset ID  */  
   oldAssetNum:string,
      /**  New Acquisition Date  */  
   acquiredDate:string,
      /**  New Placed In Service Date  */  
   commissionedDate:string,
      /**  Identifies whether Addition must be created  */  
   dupCost:boolean,
      /**  New Addition Date  */  
   additionDate:string,
}

export interface PreDuplicate_output{
      /**  Warning message  */  
   returnObj:string,
}

   /** Required : 
      @param assetNum
   */  
export interface TestAllowDelete_input{
      /**  AssetNum of record that is being updated.  */  
   assetNum:string,
}

export interface TestAllowDelete_output{
parameters : {
      /**  output parameters  */  
   sureMsg:string,
}
}

   /** Required : 
      @param ipOrgAssetNum
      @param ipAssetNum
      @param ippAssetType
   */  
export interface TestParentChildIntegrity_input{
      /**  Orig. Asset Number  */  
   ipOrgAssetNum:string,
      /**  New Asset Number  */  
   ipAssetNum:string,
      /**  Asset Type  */  
   ippAssetType:string,
}

export interface TestParentChildIntegrity_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtFAssetTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFAssetTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FAssetTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAssetTableset[],
}
}

