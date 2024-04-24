import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.ContextMenuDataSvc
// Description: Represents the ContextMenuDataSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/$metadata", {
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
   Description: Get ContextMenuDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuDatas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuRow
   */  
export function get_ContextMenuDatas(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContextMenuDatas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas", {
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
   Summary: Calls GetByID to retrieve the ContextMenuData item
   Description: Calls GetByID to retrieve the ContextMenuData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuData
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
   */  
export function get_ContextMenuDatas_LikeID_ContextTypeCode(LikeID:string, ContextTypeCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ContextMenuRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ContextMenuRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContextMenuData for the service
   Description: Calls UpdateExt to update ContextMenuData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuData
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContextMenuDatas_LikeID_ContextTypeCode(LikeID:string, ContextTypeCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")", {
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
   Summary: Call UpdateExt to delete ContextMenuData item
   Description: Call UpdateExt to delete ContextMenuData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuData
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContextMenuDatas_LikeID_ContextTypeCode(LikeID:string, ContextTypeCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")", {
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
   Description: Get ContextMenuItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContextMenuItems1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuItemRow
   */  
export function get_ContextMenuDatas_LikeID_ContextTypeCode_ContextMenuItems(LikeID:string, ContextTypeCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")/ContextMenuItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContextMenuItem item
   Description: Calls GetByID to retrieve the ContextMenuItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuItem1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   */  
export function get_ContextMenuDatas_LikeID_ContextTypeCode_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID:string, ContextTypeCode:string, ContextMenuID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ContextMenuItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ContextMenuItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ContextMenuItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuItems
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuItemRow
   */  
export function get_ContextMenuItems(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContextMenuItems(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems", {
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
   Summary: Calls GetByID to retrieve the ContextMenuItem item
   Description: Calls GetByID to retrieve the ContextMenuItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuItem
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   */  
export function get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID:string, ContextTypeCode:string, ContextMenuID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ContextMenuItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ContextMenuItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContextMenuItem for the service
   Description: Calls UpdateExt to update ContextMenuItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuItem
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID:string, ContextTypeCode:string, ContextMenuID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")", {
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
   Summary: Call UpdateExt to delete ContextMenuItem item
   Description: Call UpdateExt to delete ContextMenuItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuItem
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID:string, ContextTypeCode:string, ContextMenuID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")", {
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
   Description: Get AlternateKeyLikes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlternateKeyLikes1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyLikeRow
   */  
export function get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_AlternateKeyLikes(LikeID:string, ContextTypeCode:string, ContextMenuID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/AlternateKeyLikes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlternateKeyLike item
   Description: Calls GetByID to retrieve the AlternateKeyLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyLike1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   */  
export function get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID:string, ContextTypeCode:string, ContextMenuID:string, LikeField:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AlternateKeyLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AlternateKeyLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LaunchOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaunchOptions1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LaunchOptionRow
   */  
export function get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_LaunchOptions(LikeID:string, ContextTypeCode:string, ContextMenuID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LaunchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/LaunchOptions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LaunchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaunchOption item
   Description: Calls GetByID to retrieve the LaunchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaunchOption1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   */  
export function get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_LaunchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_LaunchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SearchOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SearchOptions1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SearchOptionRow
   */  
export function get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_SearchOptions(LikeID:string, ContextTypeCode:string, ContextMenuID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SearchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/SearchOptions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SearchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SearchOption item
   Description: Calls GetByID to retrieve the SearchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SearchOption1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   */  
export function get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SearchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SearchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlternateKeyLikes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlternateKeyLikes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyLikeRow
   */  
export function get_AlternateKeyLikes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlternateKeyLikes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlternateKeyLikes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes", {
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
   Summary: Calls GetByID to retrieve the AlternateKeyLike item
   Description: Calls GetByID to retrieve the AlternateKeyLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyLike
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   */  
export function get_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID:string, ContextTypeCode:string, ContextMenuID:string, LikeField:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AlternateKeyLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AlternateKeyLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlternateKeyLike for the service
   Description: Calls UpdateExt to update AlternateKeyLike. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlternateKeyLike
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID:string, ContextTypeCode:string, ContextMenuID:string, LikeField:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")", {
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
   Summary: Call UpdateExt to delete AlternateKeyLike item
   Description: Call UpdateExt to delete AlternateKeyLike item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlternateKeyLike
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID:string, ContextTypeCode:string, ContextMenuID:string, LikeField:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")", {
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
   Description: Get LaunchOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaunchOptions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LaunchOptionRow
   */  
export function get_LaunchOptions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LaunchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LaunchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaunchOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaunchOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions", {
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
   Summary: Calls GetByID to retrieve the LaunchOption item
   Description: Calls GetByID to retrieve the LaunchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaunchOption
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   */  
export function get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_LaunchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_LaunchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaunchOption for the service
   Description: Calls UpdateExt to update LaunchOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaunchOption
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
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
   Summary: Call UpdateExt to delete LaunchOption item
   Description: Call UpdateExt to delete LaunchOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaunchOption
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
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
   Description: Get AlternateKeyBindings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlternateKeyBindings1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyBindingRow
   */  
export function get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeyBindings(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeyBindings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlternateKeyBinding item
   Description: Calls GetByID to retrieve the AlternateKeyBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyBinding1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param AlternateKeyBinding1 Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   */  
export function get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, AlternateKeyBinding1:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AlternateKeyBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AlternateKeyBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlternateKeys items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlternateKeys1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyRow
   */  
export function get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeys(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeys", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlternateKey item
   Description: Calls GetByID to retrieve the AlternateKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKey1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   */  
export function get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AlternateKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AlternateKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlternateKeyBindings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlternateKeyBindings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyBindingRow
   */  
export function get_AlternateKeyBindings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlternateKeyBindings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlternateKeyBindings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings", {
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
   Summary: Calls GetByID to retrieve the AlternateKeyBinding item
   Description: Calls GetByID to retrieve the AlternateKeyBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyBinding
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param AlternateKeyBinding1 Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   */  
export function get_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, AlternateKeyBinding1:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AlternateKeyBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AlternateKeyBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlternateKeyBinding for the service
   Description: Calls UpdateExt to update AlternateKeyBinding. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlternateKeyBinding
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param AlternateKeyBinding1 Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, AlternateKeyBinding1:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")", {
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
   Summary: Call UpdateExt to delete AlternateKeyBinding item
   Description: Call UpdateExt to delete AlternateKeyBinding item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlternateKeyBinding
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param AlternateKeyBinding1 Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, AlternateKeyBinding1:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")", {
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
   Description: Get AlternateKeys items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlternateKeys
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyRow
   */  
export function get_AlternateKeys(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlternateKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlternateKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys", {
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
   Summary: Calls GetByID to retrieve the AlternateKey item
   Description: Calls GetByID to retrieve the AlternateKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKey
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   */  
export function get_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AlternateKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AlternateKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlternateKey for the service
   Description: Calls UpdateExt to update AlternateKey. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlternateKey
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
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
   Summary: Call UpdateExt to delete AlternateKey item
   Description: Call UpdateExt to delete AlternateKey item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlternateKey
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
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
   Description: Get SearchOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SearchOptions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SearchOptionRow
   */  
export function get_SearchOptions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SearchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SearchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SearchOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SearchOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions", {
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
   Summary: Calls GetByID to retrieve the SearchOption item
   Description: Calls GetByID to retrieve the SearchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SearchOption
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   */  
export function get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SearchOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SearchOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SearchOption for the service
   Description: Calls UpdateExt to update SearchOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SearchOption
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
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
   Summary: Call UpdateExt to delete SearchOption item
   Description: Call UpdateExt to delete SearchOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SearchOption
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", {
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
   Description: Get WhereClauseBindings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhereClauseBindings1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseBindingRow
   */  
export function get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseBindings(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseBindings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WhereClauseBinding item
   Description: Calls GetByID to retrieve the WhereClauseBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseBinding1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   */  
export function get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_WhereClauseBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_WhereClauseBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get WhereClauseTokens items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhereClauseTokens1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseTokenRow
   */  
export function get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseTokens(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseTokenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseTokens", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseTokenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WhereClauseToken item
   Description: Calls GetByID to retrieve the WhereClauseToken item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseToken1
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param BindingToken Desc: BindingToken   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   */  
export function get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, BindingToken:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_WhereClauseTokenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_WhereClauseTokenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get WhereClauseBindings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhereClauseBindings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseBindingRow
   */  
export function get_WhereClauseBindings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhereClauseBindings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhereClauseBindings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings", {
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
   Summary: Calls GetByID to retrieve the WhereClauseBinding item
   Description: Calls GetByID to retrieve the WhereClauseBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseBinding
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   */  
export function get_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_WhereClauseBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_WhereClauseBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WhereClauseBinding for the service
   Description: Calls UpdateExt to update WhereClauseBinding. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhereClauseBinding
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
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
   Summary: Call UpdateExt to delete WhereClauseBinding item
   Description: Call UpdateExt to delete WhereClauseBinding item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhereClauseBinding
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", {
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
   Description: Get WhereClauseTokens items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhereClauseTokens
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseTokenRow
   */  
export function get_WhereClauseTokens(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseTokenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseTokenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhereClauseTokens
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhereClauseTokens(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens", {
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
   Summary: Calls GetByID to retrieve the WhereClauseToken item
   Description: Calls GetByID to retrieve the WhereClauseToken item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseToken
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param BindingToken Desc: BindingToken   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   */  
export function get_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, BindingToken:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_WhereClauseTokenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_WhereClauseTokenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WhereClauseToken for the service
   Description: Calls UpdateExt to update WhereClauseToken. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhereClauseToken
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param BindingToken Desc: BindingToken   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, BindingToken:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")", {
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
   Summary: Call UpdateExt to delete WhereClauseToken item
   Description: Call UpdateExt to delete WhereClauseToken item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhereClauseToken
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ContextMenuID Desc: ContextMenuID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param CurrentBinding Desc: CurrentBinding   Required: True   Allow empty value : True
      @param BindingToken Desc: BindingToken   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID:string, ContextTypeCode:string, ContextMenuID:string, CalledFrom:string, CurrentBinding:string, BindingToken:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")", {
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
   Description: Get ContextMenuItemTemps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuItemTemps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuItemTempRow
   */  
export function get_ContextMenuItemTemps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuItemTemps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContextMenuItemTemps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps", {
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
   Summary: Calls GetByID to retrieve the ContextMenuItemTemp item
   Description: Calls GetByID to retrieve the ContextMenuItemTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuItemTemp
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
   */  
export function get_ContextMenuItemTemps_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ContextMenuItemTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ContextMenuItemTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContextMenuItemTemp for the service
   Description: Calls UpdateExt to update ContextMenuItemTemp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuItemTemp
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContextMenuItemTemps_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ContextMenuItemTemp item
   Description: Call UpdateExt to delete ContextMenuItemTemp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuItemTemp
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContextMenuItemTemps_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps(" + SysRowID + ")", {
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
   Description: Get ContextMenuTemps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuTemps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuTempRow
   */  
export function get_ContextMenuTemps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuTemps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContextMenuTemps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps", {
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
   Summary: Calls GetByID to retrieve the ContextMenuTemp item
   Description: Calls GetByID to retrieve the ContextMenuTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuTemp
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
   */  
export function get_ContextMenuTemps_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ContextMenuTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ContextMenuTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContextMenuTemp for the service
   Description: Calls UpdateExt to update ContextMenuTemp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuTemp
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContextMenuTemps_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ContextMenuTemp item
   Description: Call UpdateExt to delete ContextMenuTemp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuTemp
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContextMenuTemps_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps(" + SysRowID + ")", {
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
   Description: Get ContextValidations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextValidations
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextValidationRow
   */  
export function get_ContextValidations(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextValidationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextValidationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContextValidations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations", {
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
   Summary: Calls GetByID to retrieve the ContextValidation item
   Description: Calls GetByID to retrieve the ContextValidation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextValidation
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ValidationAdapter Desc: ValidationAdapter   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
   */  
export function get_ContextValidations_LikeID_ContextTypeCode_ValidationAdapter(LikeID:string, ContextTypeCode:string, ValidationAdapter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ContextValidationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations(" + LikeID + "," + ContextTypeCode + "," + ValidationAdapter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ContextValidationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContextValidation for the service
   Description: Calls UpdateExt to update ContextValidation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextValidation
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ValidationAdapter Desc: ValidationAdapter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContextValidations_LikeID_ContextTypeCode_ValidationAdapter(LikeID:string, ContextTypeCode:string, ValidationAdapter:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations(" + LikeID + "," + ContextTypeCode + "," + ValidationAdapter + ")", {
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
   Summary: Call UpdateExt to delete ContextValidation item
   Description: Call UpdateExt to delete ContextValidation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextValidation
      @param LikeID Desc: LikeID   Required: True   Allow empty value : True
      @param ContextTypeCode Desc: ContextTypeCode   Required: True   Allow empty value : True
      @param ValidationAdapter Desc: ValidationAdapter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContextValidations_LikeID_ContextTypeCode_ValidationAdapter(LikeID:string, ContextTypeCode:string, ValidationAdapter:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations(" + LikeID + "," + ContextTypeCode + "," + ValidationAdapter + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuListRow)
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
export function get_GetRows(whereClauseContextMenu:string, whereClauseContextMenuItem:string, whereClauseAlternateKeyLike:string, whereClauseLaunchOption:string, whereClauseAlternateKeyBinding:string, whereClauseAlternateKey:string, whereClauseSearchOption:string, whereClauseWhereClauseBinding:string, whereClauseWhereClauseToken:string, whereClauseContextMenuItemTemp:string, whereClauseContextMenuTemp:string, whereClauseContextValidation:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseContextMenu!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContextMenu=" + whereClauseContextMenu
   }
   if(typeof whereClauseContextMenuItem!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContextMenuItem=" + whereClauseContextMenuItem
   }
   if(typeof whereClauseAlternateKeyLike!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlternateKeyLike=" + whereClauseAlternateKeyLike
   }
   if(typeof whereClauseLaunchOption!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaunchOption=" + whereClauseLaunchOption
   }
   if(typeof whereClauseAlternateKeyBinding!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlternateKeyBinding=" + whereClauseAlternateKeyBinding
   }
   if(typeof whereClauseAlternateKey!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlternateKey=" + whereClauseAlternateKey
   }
   if(typeof whereClauseSearchOption!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSearchOption=" + whereClauseSearchOption
   }
   if(typeof whereClauseWhereClauseBinding!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWhereClauseBinding=" + whereClauseWhereClauseBinding
   }
   if(typeof whereClauseWhereClauseToken!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWhereClauseToken=" + whereClauseWhereClauseToken
   }
   if(typeof whereClauseContextMenuItemTemp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContextMenuItemTemp=" + whereClauseContextMenuItemTemp
   }
   if(typeof whereClauseContextMenuTemp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContextMenuTemp=" + whereClauseContextMenuTemp
   }
   if(typeof whereClauseContextValidation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContextValidation=" + whereClauseContextValidation
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetRows" + params, {
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
export function get_GetByID(likeID:string, contextTypeCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof likeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "likeID=" + likeID
   }
   if(typeof contextTypeCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contextTypeCode=" + contextTypeCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetList" + params, {
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
   Summary: Invoke method GetCustomRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: GetCustomRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomRows(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetCustomRows", {
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
   Summary: Invoke method GetContextMenuLikeList
   Description: Get the Context Menu as Collection of LikeListInfo records
   OperationID: GetContextMenuLikeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeList", {
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
   Summary: Invoke method GetContextMenuLikeListItem
   Description: Get the LikeListInfo item that represents the Context Menu Item
   OperationID: GetContextMenuLikeListItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeListItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeListItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeListItem(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeListItem", {
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
   Summary: Invoke method GetContextMenuLikeListItems
   Description: Get the list of LikeListInfo items that represent the Context Menu Items
   OperationID: GetContextMenuLikeListItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeListItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeListItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeListItems(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeListItems", {
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
   Summary: Invoke method GetContextMenuLikeDetailItem
   Description: Get the LikeListInfo item that represents the Detailed Context Menu Item with search
   OperationID: GetContextMenuLikeDetailItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeDetailItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeDetailItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeDetailItem(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeDetailItem", {
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
   Summary: Invoke method GetContextMenuLikeDetailItems
   Description: Get the list of LikeListInfo items that represent the Detailed Context Menu Item with search
   OperationID: GetContextMenuLikeDetailItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeDetailItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeDetailItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeDetailItems(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeDetailItems", {
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
   Summary: Invoke method UpdateContextMenuLikeItems
   Description: Updates the context menu XML document based upon the update mode.
   OperationID: UpdateContextMenuLikeItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateContextMenuLikeItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateContextMenuLikeItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateContextMenuLikeItems(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/UpdateContextMenuLikeItems", {
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
   Summary: Invoke method GetContextMenuLikeItemForLayer
   Description: Gets the context menu item for the given like and all it's child nodes for the specified layer.
   OperationID: GetContextMenuLikeItemForLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeItemForLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeItemForLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeItemForLayer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeItemForLayer", {
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
   Summary: Invoke method GetContextMenuLikeHeaderByLikeID
   Description: Gets the context menu item for the given like and all it's child nodes for the specified layer.
   OperationID: GetContextMenuLikeHeaderByLikeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeHeaderByLikeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeHeaderByLikeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeHeaderByLikeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeHeaderByLikeID", {
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
   Summary: Invoke method GetContextMenuLikeHeader
   Description: Gets the context menu item for the given like and all it's child nodes for the specified layer.
   OperationID: GetContextMenuLikeHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuLikeHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuLikeHeader", {
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
   Summary: Invoke method AddNewQuickSearch
   Description: Adds a QS context menu item to the context menu XML stored in XXXDef.
   OperationID: AddNewQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddNewQuickSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AddNewQuickSearch", {
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
   Summary: Invoke method DeleteQuickSearchOption
   Description: Deletes the specified Quick Search from the context menu XML stored in XXXDef.
   OperationID: DeleteQuickSearchOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteQuickSearchOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQuickSearchOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteQuickSearchOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/DeleteQuickSearchOption", {
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
   Summary: Invoke method GetContextMenuDataList
   Description: Get List of existing Context Menu data.
   OperationID: GetContextMenuDataList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuDataList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuDataList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuDataList", {
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
   Summary: Invoke method CustomGetByID
   Description: Get By ID of existing ContextMenu from Temp.
   OperationID: CustomGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomGetByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/CustomGetByID", {
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
   Summary: Invoke method CustomGetByIDorError
   Description: Get By ID of existing ContextMenu from Temp.
   OperationID: CustomGetByIDorError
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomGetByIDorError_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByIDorError_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomGetByIDorError(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/CustomGetByIDorError", {
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
   Summary: Invoke method LikeIDChanging
   Description: Likeid changing validataion.
   OperationID: LikeIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LikeIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LikeIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LikeIDChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LikeIDChanging", {
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
   Summary: Invoke method ValidateLikeID
   Description: Checks if the LikeID string would make a valid XML node name
   OperationID: ValidateLikeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLikeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLikeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateLikeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ValidateLikeID", {
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
   Summary: Invoke method IsValidLikeID
   Description: Checks if the given LikeID does not start with a reserved key word used in the base Context Menu
   OperationID: IsValidLikeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidLikeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidLikeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsValidLikeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/IsValidLikeID", {
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
   Summary: Invoke method GetContextMenuRows
   OperationID: GetContextMenuRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextMenuRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetContextMenuRows", {
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
   Summary: Invoke method CustomizationRights
   Description: Return if user can customize.
   OperationID: CustomizationRights
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizationRights_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomizationRights(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/CustomizationRights", {
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
   Summary: Invoke method GetNewContextMenu
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContextMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContextMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContextMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContextMenu(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewContextMenu", {
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
   Summary: Invoke method GetNewContextMenuItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContextMenuItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContextMenuItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContextMenuItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContextMenuItem(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewContextMenuItem", {
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
   Summary: Invoke method GetNewAlternateKeyLike
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlternateKeyLike
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlternateKeyLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlternateKeyLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlternateKeyLike(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewAlternateKeyLike", {
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
   Summary: Invoke method GetNewLaunchOption
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaunchOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaunchOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaunchOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaunchOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewLaunchOption", {
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
   Summary: Invoke method GetNewAlternateKeyBinding
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlternateKeyBinding
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlternateKeyBinding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlternateKeyBinding_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlternateKeyBinding(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewAlternateKeyBinding", {
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
   Summary: Invoke method GetNewAlternateKey
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlternateKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlternateKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlternateKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlternateKey(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewAlternateKey", {
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
   Summary: Invoke method GetNewSearchOption
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSearchOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSearchOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSearchOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSearchOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewSearchOption", {
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
   Summary: Invoke method GetNewWhereClauseBinding
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhereClauseBinding
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhereClauseBinding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhereClauseBinding_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWhereClauseBinding(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewWhereClauseBinding", {
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
   Summary: Invoke method GetNewWhereClauseToken
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhereClauseToken
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhereClauseToken_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhereClauseToken_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWhereClauseToken(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewWhereClauseToken", {
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
   Summary: Invoke method GetNewContextValidation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContextValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContextValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContextValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContextValidation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetNewContextValidation", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyBindingRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AlternateKeyBindingRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyLikeRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AlternateKeyLikeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AlternateKeyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ContextMenuItemRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemTempRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ContextMenuItemTempRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ContextMenuListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ContextMenuRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuTempRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ContextMenuTempRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextValidationRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ContextValidationRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LaunchOptionRow{
   "odatametadata":string,
   "value":Ice_Tablesets_LaunchOptionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SearchOptionRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SearchOptionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseBindingRow{
   "odatametadata":string,
   "value":Ice_Tablesets_WhereClauseBindingRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseTokenRow{
   "odatametadata":string,
   "value":Ice_Tablesets_WhereClauseTokenRow[],
}

export interface Ice_Tablesets_AlternateKeyBindingRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  CalledFrom  */  
   "CalledFrom":string,
      /**  CurrentBinding  */  
   "CurrentBinding":string,
   "AlternateKeyBinding1":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_AlternateKeyLikeRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  LikeField  */  
   "LikeField":string,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_AlternateKeyRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  CalledFrom  */  
   "CalledFrom":string,
      /**  CurrentBinding  */  
   "CurrentBinding":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  ContextValue  */  
   "ContextValue":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ContextMenuItemRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  ContextMenuText  */  
   "ContextMenuText":string,
      /**  ProcessCall  */  
   "ProcessCall":string,
      /**  ProcessType  */  
   "ProcessType":string,
      /**  MenuID  */  
   "MenuID":string,
      /**  AdapterID  */  
   "AdapterID":string,
      /**  SearchMode  */  
   "SearchMode":string,
      /**  TrackerID  */  
   "TrackerID":string,
      /**  QSValidation  */  
   "QSValidation":boolean,
      /**  QSBaseDefault  */  
   "QSBaseDefault":boolean,
      /**  QSContextDefault  */  
   "QSContextDefault":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  MenuOrder  */  
   "MenuOrder":number,
      /**  MenuEnabled  */  
   "MenuEnabled":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  QueryID  */  
   "QueryID":string,
      /**  Temporary ID to identify row.  */  
   "TempID":string,
   "ProcessCallOrg":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ContextMenuItemTempRow{
      /**  AdapterID  */  
   "AdapterID":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  ContextMenuText  */  
   "ContextMenuText":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  LikeID  */  
   "LikeID":string,
      /**  MenuEnabled  */  
   "MenuEnabled":boolean,
      /**  MenuID  */  
   "MenuID":string,
      /**  MenuOrder  */  
   "MenuOrder":number,
      /**  ProcessCall  */  
   "ProcessCall":string,
      /**  ProcessType  */  
   "ProcessType":string,
      /**  QSBaseDefault  */  
   "QSBaseDefault":boolean,
      /**  QSContextDefault  */  
   "QSContextDefault":boolean,
      /**  QSValidation  */  
   "QSValidation":boolean,
      /**  QueryID  */  
   "QueryID":string,
      /**  SearchMode  */  
   "SearchMode":string,
      /**  SysRevID  */  
   "SysRevID":number,
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  TrackerID  */  
   "TrackerID":string,
      /**  UpdateType  */  
   "UpdateType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ContextMenuListRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  Description  */  
   "Description":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ContextMenuRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  Description  */  
   "Description":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ContextMenuTempRow{
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  Description  */  
   "Description":string,
      /**  LikeID  */  
   "LikeID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  UpdateType  */  
   "UpdateType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ContextValidationRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ValidationAdapter  */  
   "ValidationAdapter":string,
      /**  ValidationType  */  
   "ValidationType":string,
      /**  RetrieverCombo  */  
   "RetrieverCombo":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_LaunchOptionRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  CalledFrom  */  
   "CalledFrom":string,
      /**  LaunchModal  */  
   "LaunchModal":boolean,
      /**  EpiReadOnly  */  
   "EpiReadOnly":boolean,
      /**  SuppressPublisher  */  
   "SuppressPublisher":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  ContextValue  */  
   "ContextValue":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SearchOptionRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  CalledFrom  */  
   "CalledFrom":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_WhereClauseBindingRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  CalledFrom  */  
   "CalledFrom":string,
      /**  CurrentBinding  */  
   "CurrentBinding":string,
      /**  SearchTable  */  
   "SearchTable":string,
      /**  SearchTitle  */  
   "SearchTitle":string,
      /**  WhereClauseString  */  
   "WhereClauseString":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_WhereClauseTokenRow{
      /**  LikeID  */  
   "LikeID":string,
      /**  ContextTypeCode  */  
   "ContextTypeCode":string,
      /**  ContextMenuID  */  
   "ContextMenuID":string,
      /**  CalledFrom  */  
   "CalledFrom":string,
      /**  CurrentBinding  */  
   "CurrentBinding":string,
      /**  BindingToken  */  
   "BindingToken":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param likeField
      @param quickSearchID
      @param description
      @param calledFrom
      @param isShared
      @param forValidation
      @param baseDefault
      @param contextDefault
   */  
export interface AddNewQuickSearch_input{
   likeField:string,
   quickSearchID:string,
   description:string,
   calledFrom:string,
   isShared:boolean,
   forValidation:boolean,
   baseDefault:boolean,
   contextDefault:boolean,
}

export interface AddNewQuickSearch_output{
}

   /** Required : 
      @param likeID
      @param contextTypeCode
   */  
export interface CustomGetByID_input{
   likeID:string,
   contextTypeCode:string,
}

export interface CustomGetByID_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

   /** Required : 
      @param likeID
      @param contextTypeCode
   */  
export interface CustomGetByIDorError_input{
   likeID:string,
   contextTypeCode:string,
}

export interface CustomGetByIDorError_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

export interface CustomizationRights_output{
   returnObj:boolean,
}

   /** Required : 
      @param likeID
      @param contextTypeCode
   */  
export interface DeleteByID_input{
   likeID:string,
   contextTypeCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param likeField
      @param quickSearchID
      @param description
      @param isShared
   */  
export interface DeleteQuickSearchOption_input{
   likeField:string,
   quickSearchID:string,
   description:string,
   isShared:boolean,
}

export interface DeleteQuickSearchOption_output{
}

   /** Required : 
      @param likeID
      @param contextTypeCode
   */  
export interface GetByID_input{
   likeID:string,
   contextTypeCode:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

export interface GetContextMenuDataList_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

   /** Required : 
      @param LikeId
      @param isEwa
      @param properties
   */  
export interface GetContextMenuLikeDetailItem_input{
      /**  The Like Id for the requested Context Menu Item  */  
   LikeId:string,
      /**  true when getting list for EWA  */  
   isEwa:boolean,
   properties:Ice_BO_ContextMenuData_LikeSearchProperties[],
}

export interface GetContextMenuLikeDetailItem_output{
   returnObj:Ice_BO_ContextMenuData_LikeListInfo[],
}

   /** Required : 
      @param LikeIds
      @param isEwa
      @param properties
   */  
export interface GetContextMenuLikeDetailItems_input{
      /**  The list of Like Ids for the requested Context Menu Items  */  
   LikeIds:string,
      /**  true when getting list for EWA  */  
   isEwa:boolean,
   properties:Ice_BO_ContextMenuData_LikeSearchProperties[],
}

export interface GetContextMenuLikeDetailItems_output{
      /**  LikeListInfo record that represents the list of nodes from ContextMenu.xml  */  
   returnObj:Ice_BO_ContextMenuData_LikeListInfo[],
}

   /** Required : 
      @param likeID
      @param customized
   */  
export interface GetContextMenuLikeHeaderByLikeID_input{
   likeID:string,
      /**  True to only return base or customized, false returns all layers available (base, customized, personalized).  */  
   customized:boolean,
}

export interface GetContextMenuLikeHeaderByLikeID_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

   /** Required : 
      @param likeID
      @param customized
   */  
export interface GetContextMenuLikeHeader_input{
   likeID:string,
      /**  True to only return base or customized, false returns all layers available (base, customized, personalized).  */  
   customized:boolean,
}

export interface GetContextMenuLikeHeader_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

   /** Required : 
      @param likeID
      @param customized
   */  
export interface GetContextMenuLikeItemForLayer_input{
   likeID:string,
      /**  True to only return base or customized, false returns all layers available (base, customized, personalized).  */  
   customized:boolean,
}

export interface GetContextMenuLikeItemForLayer_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

   /** Required : 
      @param LikeId
      @param isEwa
   */  
export interface GetContextMenuLikeListItem_input{
      /**  The Like Id for the requested Context Menu Item  */  
   LikeId:string,
      /**  true when getting list for EWA  */  
   isEwa:boolean,
}

export interface GetContextMenuLikeListItem_output{
   returnObj:Ice_BO_ContextMenuData_LikeListInfo[],
}

   /** Required : 
      @param LikeIds
      @param isEwa
   */  
export interface GetContextMenuLikeListItems_input{
      /**  The list of Like Ids for the requested Context Menu Items  */  
   LikeIds:string,
      /**  true when getting list for EWA  */  
   isEwa:boolean,
}

export interface GetContextMenuLikeListItems_output{
      /**  LikeListInfo record that represents the list of nodes from ContextMenu.xml  */  
   returnObj:Ice_BO_ContextMenuData_LikeListInfo[],
}

   /** Required : 
      @param isEwa
   */  
export interface GetContextMenuLikeList_input{
      /**  true when getting list for EWA  */  
   isEwa:boolean,
}

export interface GetContextMenuLikeList_output{
      /**  Collection of LikeListInfo records that represents the ContextMenu.xml  */  
   returnObj:Ice_BO_ContextMenuData_LikeListInfo[],
}

   /** Required : 
      @param whereClause
   */  
export interface GetContextMenuRows_input{
   whereClause:string,
}

export interface GetContextMenuRows_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
}

export interface GetCustomRows_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
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
   returnObj:Ice_Tablesets_ContextMenuDataListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
      @param contextMenuID
      @param calledFrom
      @param currentBinding
   */  
export interface GetNewAlternateKeyBinding_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
   contextMenuID:string,
   calledFrom:string,
   currentBinding:string,
}

export interface GetNewAlternateKeyBinding_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
      @param contextMenuID
   */  
export interface GetNewAlternateKeyLike_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
   contextMenuID:string,
}

export interface GetNewAlternateKeyLike_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
      @param contextMenuID
      @param calledFrom
   */  
export interface GetNewAlternateKey_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
   contextMenuID:string,
   calledFrom:string,
}

export interface GetNewAlternateKey_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
   */  
export interface GetNewContextMenuItem_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
}

export interface GetNewContextMenuItem_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
   */  
export interface GetNewContextMenu_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
}

export interface GetNewContextMenu_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
   */  
export interface GetNewContextValidation_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
}

export interface GetNewContextValidation_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
      @param contextMenuID
   */  
export interface GetNewLaunchOption_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
   contextMenuID:string,
}

export interface GetNewLaunchOption_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
      @param contextMenuID
   */  
export interface GetNewSearchOption_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
   contextMenuID:string,
}

export interface GetNewSearchOption_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
      @param contextMenuID
      @param calledFrom
   */  
export interface GetNewWhereClauseBinding_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
   contextMenuID:string,
   calledFrom:string,
}

export interface GetNewWhereClauseBinding_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param ds
      @param likeID
      @param contextTypeCode
      @param contextMenuID
      @param calledFrom
      @param currentBinding
   */  
export interface GetNewWhereClauseToken_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
   likeID:string,
   contextTypeCode:string,
   contextMenuID:string,
   calledFrom:string,
   currentBinding:string,
}

export interface GetNewWhereClauseToken_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param whereClauseContextMenu
      @param whereClauseContextMenuItem
      @param whereClauseAlternateKeyLike
      @param whereClauseLaunchOption
      @param whereClauseAlternateKeyBinding
      @param whereClauseAlternateKey
      @param whereClauseSearchOption
      @param whereClauseWhereClauseBinding
      @param whereClauseWhereClauseToken
      @param whereClauseContextMenuItemTemp
      @param whereClauseContextMenuTemp
      @param whereClauseContextValidation
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseContextMenu:string,
   whereClauseContextMenuItem:string,
   whereClauseAlternateKeyLike:string,
   whereClauseLaunchOption:string,
   whereClauseAlternateKeyBinding:string,
   whereClauseAlternateKey:string,
   whereClauseSearchOption:string,
   whereClauseWhereClauseBinding:string,
   whereClauseWhereClauseToken:string,
   whereClauseContextMenuItemTemp:string,
   whereClauseContextMenuTemp:string,
   whereClauseContextValidation:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ContextMenuDataTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BO_ContextMenuData_LikeListInfo{
   Id:string,
   UpdateType:string,
   ContextTypeCode:string,
   Items:Ice_BO_ContextMenuData_LikeListItem[],
   Validation:Ice_BO_ContextMenuData_LikeValidation[],
}

export interface Ice_BO_ContextMenuData_LikeListItem{
   Caption:string,
   ProcessCall:string,
   SearchMode:string,
   Guid:string,
   ProcessType:string,
   SystemFlag:boolean,
   QueryID:string,
   UpdateType:string,
   ContextTypeCode:string,
   AdapterID:string,
   ProcessCallOrg:string,
}

export interface Ice_BO_ContextMenuData_LikeSearchProperties{
   searchForm:string,
   deviceType:string,
   mode:string,
   layers:string,
}

export interface Ice_BO_ContextMenuData_LikeValidation{
   ValidationAdapter:string,
   ValidationType:string,
   RetrieverCombo:string,
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

export interface Ice_Tablesets_AlternateKeyBindingRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  CalledFrom  */  
   CalledFrom:string,
      /**  CurrentBinding  */  
   CurrentBinding:string,
      /**  AlternateKeyBinding  */  
   AlternateKeyBinding:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AlternateKeyLikeRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  LikeField  */  
   LikeField:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AlternateKeyRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  CalledFrom  */  
   CalledFrom:string,
      /**  CurrentBinding  */  
   CurrentBinding:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SeqNum  */  
   SeqNum:number,
      /**  ContextValue  */  
   ContextValue:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ContextMenuDataListTableset{
   ContextMenuList:Ice_Tablesets_ContextMenuListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ContextMenuDataTableset{
   ContextMenu:Ice_Tablesets_ContextMenuRow[],
   ContextMenuItem:Ice_Tablesets_ContextMenuItemRow[],
   AlternateKeyLike:Ice_Tablesets_AlternateKeyLikeRow[],
   LaunchOption:Ice_Tablesets_LaunchOptionRow[],
   AlternateKeyBinding:Ice_Tablesets_AlternateKeyBindingRow[],
   AlternateKey:Ice_Tablesets_AlternateKeyRow[],
   SearchOption:Ice_Tablesets_SearchOptionRow[],
   WhereClauseBinding:Ice_Tablesets_WhereClauseBindingRow[],
   WhereClauseToken:Ice_Tablesets_WhereClauseTokenRow[],
   ContextMenuItemTemp:Ice_Tablesets_ContextMenuItemTempRow[],
   ContextMenuTemp:Ice_Tablesets_ContextMenuTempRow[],
   ContextValidation:Ice_Tablesets_ContextValidationRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ContextMenuItemRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  ContextMenuText  */  
   ContextMenuText:string,
      /**  ProcessCall  */  
   ProcessCall:string,
      /**  ProcessType  */  
   ProcessType:string,
      /**  MenuID  */  
   MenuID:string,
      /**  AdapterID  */  
   AdapterID:string,
      /**  SearchMode  */  
   SearchMode:string,
      /**  TrackerID  */  
   TrackerID:string,
      /**  QSValidation  */  
   QSValidation:boolean,
      /**  QSBaseDefault  */  
   QSBaseDefault:boolean,
      /**  QSContextDefault  */  
   QSContextDefault:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  MenuOrder  */  
   MenuOrder:number,
      /**  MenuEnabled  */  
   MenuEnabled:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  QueryID  */  
   QueryID:string,
      /**  Temporary ID to identify row.  */  
   TempID:string,
   ProcessCallOrg:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ContextMenuItemTempRow{
      /**  AdapterID  */  
   AdapterID:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  ContextMenuText  */  
   ContextMenuText:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  LikeID  */  
   LikeID:string,
      /**  MenuEnabled  */  
   MenuEnabled:boolean,
      /**  MenuID  */  
   MenuID:string,
      /**  MenuOrder  */  
   MenuOrder:number,
      /**  ProcessCall  */  
   ProcessCall:string,
      /**  ProcessType  */  
   ProcessType:string,
      /**  QSBaseDefault  */  
   QSBaseDefault:boolean,
      /**  QSContextDefault  */  
   QSContextDefault:boolean,
      /**  QSValidation  */  
   QSValidation:boolean,
      /**  QueryID  */  
   QueryID:string,
      /**  SearchMode  */  
   SearchMode:string,
      /**  SysRevID  */  
   SysRevID:number,
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  TrackerID  */  
   TrackerID:string,
      /**  UpdateType  */  
   UpdateType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ContextMenuListRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  Description  */  
   Description:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ContextMenuRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  Description  */  
   Description:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ContextMenuTempRow{
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  Description  */  
   Description:string,
      /**  LikeID  */  
   LikeID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  UpdateType  */  
   UpdateType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ContextValidationRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ValidationAdapter  */  
   ValidationAdapter:string,
      /**  ValidationType  */  
   ValidationType:string,
      /**  RetrieverCombo  */  
   RetrieverCombo:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_LaunchOptionRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  CalledFrom  */  
   CalledFrom:string,
      /**  LaunchModal  */  
   LaunchModal:boolean,
      /**  EpiReadOnly  */  
   EpiReadOnly:boolean,
      /**  SuppressPublisher  */  
   SuppressPublisher:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SeqNum  */  
   SeqNum:number,
      /**  ContextValue  */  
   ContextValue:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SearchOptionRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  CalledFrom  */  
   CalledFrom:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtContextMenuDataTableset{
   ContextMenu:Ice_Tablesets_ContextMenuRow[],
   ContextMenuItem:Ice_Tablesets_ContextMenuItemRow[],
   AlternateKeyLike:Ice_Tablesets_AlternateKeyLikeRow[],
   LaunchOption:Ice_Tablesets_LaunchOptionRow[],
   AlternateKeyBinding:Ice_Tablesets_AlternateKeyBindingRow[],
   AlternateKey:Ice_Tablesets_AlternateKeyRow[],
   SearchOption:Ice_Tablesets_SearchOptionRow[],
   WhereClauseBinding:Ice_Tablesets_WhereClauseBindingRow[],
   WhereClauseToken:Ice_Tablesets_WhereClauseTokenRow[],
   ContextMenuItemTemp:Ice_Tablesets_ContextMenuItemTempRow[],
   ContextMenuTemp:Ice_Tablesets_ContextMenuTempRow[],
   ContextValidation:Ice_Tablesets_ContextValidationRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_WhereClauseBindingRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  CalledFrom  */  
   CalledFrom:string,
      /**  CurrentBinding  */  
   CurrentBinding:string,
      /**  SearchTable  */  
   SearchTable:string,
      /**  SearchTitle  */  
   SearchTitle:string,
      /**  WhereClauseString  */  
   WhereClauseString:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_WhereClauseTokenRow{
      /**  LikeID  */  
   LikeID:string,
      /**  ContextTypeCode  */  
   ContextTypeCode:string,
      /**  ContextMenuID  */  
   ContextMenuID:string,
      /**  CalledFrom  */  
   CalledFrom:string,
      /**  CurrentBinding  */  
   CurrentBinding:string,
      /**  BindingToken  */  
   BindingToken:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param likeID
   */  
export interface IsValidLikeID_input{
      /**  LikeID  */  
   likeID:string,
}

export interface IsValidLikeID_output{
      /**  true if not reserved, false otherwise  */  
   returnObj:boolean,
}

   /** Required : 
      @param likeID
   */  
export interface LikeIDChanging_input{
   likeID:string,
}

export interface LikeIDChanging_output{
}

   /** Required : 
      @param contextMenuData
      @param updateMode
   */  
export interface UpdateContextMenuLikeItems_input{
   contextMenuData:Ice_Tablesets_ContextMenuDataTableset[],
      /**  Valid options are 'Customize' and 'Personalize'  */  
   updateMode:string,
}

export interface UpdateContextMenuLikeItems_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtContextMenuDataTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtContextMenuDataTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ContextMenuDataTableset[],
}
}

   /** Required : 
      @param likeID
   */  
export interface ValidateLikeID_input{
      /**  LikeID  */  
   likeID:string,
}

export interface ValidateLikeID_output{
      /**  true if valid, false otherwise  */  
   returnObj:boolean,
}

