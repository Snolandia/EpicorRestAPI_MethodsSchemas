import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DynAttrValueSetSvc
// Description: Dynamic Attributes Set core service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/$metadata", {
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
   Description: Get DynAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrValueSets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetRow
   */  
export function get_DynAttrValueSets(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrValueSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrValueSets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets", {
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
   Summary: Calls GetByID to retrieve the DynAttrValueSet item
   Description: Calls GetByID to retrieve the DynAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
   */  
export function get_DynAttrValueSets_Company_AttributeSetID(Company:string, AttributeSetID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrValueSet for the service
   Description: Calls UpdateExt to update DynAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrValueSets_Company_AttributeSetID(Company:string, AttributeSetID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")", {
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
   Summary: Call UpdateExt to delete DynAttrValueSet item
   Description: Call UpdateExt to delete DynAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrValueSets_Company_AttributeSetID(Company:string, AttributeSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")", {
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
   Description: Get DynAttrValueSetLangDescs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DynAttrValueSetLangDescs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetLangDescRow
   */  
export function get_DynAttrValueSets_Company_AttributeSetID_DynAttrValueSetLangDescs(Company:string, AttributeSetID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetLangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")/DynAttrValueSetLangDescs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetLangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynAttrValueSetLangDesc item
   Description: Calls GetByID to retrieve the DynAttrValueSetLangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValueSetLangDesc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   */  
export function get_DynAttrValueSets_Company_AttributeSetID_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company:string, AttributeSetID:string, LangNameID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrValueSetLangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrValueSetLangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DynAttrValueSetLangDescs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrValueSetLangDescs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetLangDescRow
   */  
export function get_DynAttrValueSetLangDescs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetLangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetLangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrValueSetLangDescs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrValueSetLangDescs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs", {
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
   Summary: Calls GetByID to retrieve the DynAttrValueSetLangDesc item
   Description: Calls GetByID to retrieve the DynAttrValueSetLangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValueSetLangDesc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   */  
export function get_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company:string, AttributeSetID:string, LangNameID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrValueSetLangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrValueSetLangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrValueSetLangDesc for the service
   Description: Calls UpdateExt to update DynAttrValueSetLangDesc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrValueSetLangDesc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company:string, AttributeSetID:string, LangNameID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")", {
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
   Summary: Call UpdateExt to delete DynAttrValueSetLangDesc item
   Description: Call UpdateExt to delete DynAttrValueSetLangDesc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrValueSetLangDesc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company:string, AttributeSetID:string, LangNameID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")", {
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
   Description: Get DynAttrValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrValues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueRow
   */  
export function get_DynAttrValues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues", {
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
   Summary: Calls GetByID to retrieve the DynAttrValue item
   Description: Calls GetByID to retrieve the DynAttrValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToSchemaName Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      @param RelatedToTableName Desc: RelatedToTableName   Required: True   Allow empty value : True
      @param RelatedToSysRowID Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   */  
export function get_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company:string, RelatedToSchemaName:string, RelatedToTableName:string, RelatedToSysRowID:string, AttrClassID:string, AttributeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrValueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrValueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrValue for the service
   Description: Calls UpdateExt to update DynAttrValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToSchemaName Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      @param RelatedToTableName Desc: RelatedToTableName   Required: True   Allow empty value : True
      @param RelatedToSysRowID Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company:string, RelatedToSchemaName:string, RelatedToTableName:string, RelatedToSysRowID:string, AttrClassID:string, AttributeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")", {
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
   Summary: Call UpdateExt to delete DynAttrValue item
   Description: Call UpdateExt to delete DynAttrValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToSchemaName Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      @param RelatedToTableName Desc: RelatedToTableName   Required: True   Allow empty value : True
      @param RelatedToSysRowID Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company:string, RelatedToSchemaName:string, RelatedToTableName:string, RelatedToSysRowID:string, AttrClassID:string, AttributeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")", {
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
   Description: Get DynAttrClassDtlComboValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtlComboValues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlComboValuesRow
   */  
export function get_DynAttrClassDtlComboValues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlComboValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlComboValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtlComboValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrClassDtlComboValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues", {
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
   Summary: Calls GetByID to retrieve the DynAttrClassDtlComboValue item
   Description: Calls GetByID to retrieve the DynAttrClassDtlComboValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlComboValue
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   */  
export function get_DynAttrClassDtlComboValues_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrClassDtlComboValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrClassDtlComboValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrClassDtlComboValue for the service
   Description: Calls UpdateExt to update DynAttrClassDtlComboValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtlComboValue
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrClassDtlComboValues_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete DynAttrClassDtlComboValue item
   Description: Call UpdateExt to delete DynAttrClassDtlComboValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtlComboValue
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrClassDtlComboValues_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDynAttrValueSet:string, whereClauseDynAttrValue:string, whereClauseDynAttrValueSetLangDesc:string, whereClauseDynAttrClassDtlComboValues:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDynAttrValueSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrValueSet=" + whereClauseDynAttrValueSet
   }
   if(typeof whereClauseDynAttrValue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrValue=" + whereClauseDynAttrValue
   }
   if(typeof whereClauseDynAttrValueSetLangDesc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrValueSetLangDesc=" + whereClauseDynAttrValueSetLangDesc
   }
   if(typeof whereClauseDynAttrClassDtlComboValues!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrClassDtlComboValues=" + whereClauseDynAttrClassDtlComboValues
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetRows" + params, {
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
export function get_GetByID(attributeSetID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof attributeSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attributeSetID=" + attributeSetID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetList" + params, {
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
   Summary: Invoke method GetNewAttributeValuesRow
   Description: Gets new inverted row of a full set of DynAttrValue, returns both types of attributes: dynamic attributes, inventory dynamic attributes.
Method is dependent on a populated InventoryDynAttrValueSummaryRow with minimum populated values: AttrClassID, RelatedToSchemaName, RelatedToTableName.
If used for Inventory Attributes then either RelatedToSysRowID or PartNum must be supplied.
   OperationID: GetNewAttributeValuesRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAttributeValuesRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAttributeValuesRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAttributeValuesRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewAttributeValuesRow", {
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
   Summary: Invoke method GetNewAttributeValuesRowWithOutDynamicMetaDataDS
   Description: Gets new inverted row of a full set of DynAttrValue, returns both types of attributes: dynamic attributes, inventory dynamic attributes.
Method is dependent on a populated InventoryDynAttrValueSummaryRow with minimum populated values: AttrClassID, RelatedToSchemaName, RelatedToTableName.
If used for Inventory Attributes then either RelatedToSysRowID or PartNum must be supplied.
   OperationID: GetNewAttributeValuesRowWithOutDynamicMetaDataDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAttributeValuesRowWithOutDynamicMetaDataDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAttributeValuesRowWithOutDynamicMetaDataDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAttributeValuesRowWithOutDynamicMetaDataDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewAttributeValuesRowWithOutDynamicMetaDataDS", {
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
   Summary: Invoke method GetNewInventoryDynAttrValuesRow
   Description: Used with Inventory Attributes Entry to create full set of DynAttrValue as inverted table.
   OperationID: GetNewInventoryDynAttrValuesRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInventoryDynAttrValuesRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInventoryDynAttrValuesRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInventoryDynAttrValuesRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewInventoryDynAttrValuesRow", {
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
   Summary: Invoke method GetNewInventoryDynAttrValueSummary
   Description: Gets new InventoryDynAttrValueSummary that can be used in later request for any additional parameters required.  Helper for summary totals.
   OperationID: GetNewInventoryDynAttrValueSummary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInventoryDynAttrValueSummary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInventoryDynAttrValueSummary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInventoryDynAttrValueSummary(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewInventoryDynAttrValueSummary", {
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
   Summary: Invoke method GetByIDDynAttrValueSetDataSet
   Description: Returns the DynAttrValueSetTableset as an inverted dynamic Dataset
   OperationID: GetByIDDynAttrValueSetDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDDynAttrValueSetDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDDynAttrValueSetDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDDynAttrValueSetDataSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetByIDDynAttrValueSetDataSet", {
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
   Summary: Invoke method GetNewDynAttrValueSetDataSet
   Description: Used with Dynamic Attribute Set Maintenance to create full dataset with all needed DynAttrValue columns.  The DynAttrValue rows have been inverted to columns.
For new sets the whole set most be created at the same time, a valid attribute class ID must be supplied.
   OperationID: GetNewDynAttrValueSetDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSetDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSetDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrValueSetDataSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewDynAttrValueSetDataSet", {
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
   Summary: Invoke method GetNewDynAttrValueSetTableset
   Description: Used with Dynamic Attribute Set Maintenance to create full dataset with all needed DynAttrValue rows.
For new sets the whole set most be created at the same time, a valid attribute class ID must be supplied.
   OperationID: GetNewDynAttrValueSetTableset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSetTableset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSetTableset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrValueSetTableset(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewDynAttrValueSetTableset", {
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
   Summary: Invoke method GetFullDynAttrValueSetDataSetByAttrClassID
   Description: Returns dynamically built DataSet for all DynAttrValueSet for given attribute class.
   OperationID: GetFullDynAttrValueSetDataSetByAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullDynAttrValueSetDataSetByAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullDynAttrValueSetDataSetByAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFullDynAttrValueSetDataSetByAttrClassID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetFullDynAttrValueSetDataSetByAttrClassID", {
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
   Summary: Invoke method GetFullDynAttrValueSetDataSetByList
   Description: Returns dynamically built DataSet for all DynAttrValueSet for given AttributeSetID list.
   OperationID: GetFullDynAttrValueSetDataSetByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullDynAttrValueSetDataSetByList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullDynAttrValueSetDataSetByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFullDynAttrValueSetDataSetByList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetFullDynAttrValueSetDataSetByList", {
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
   Summary: Invoke method DynAttrValueColumnChanging
   Description: Column value change for dynamic attribute.
   OperationID: DynAttrValueColumnChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DynAttrValueColumnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DynAttrValueColumnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrValueColumnChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueColumnChanging", {
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
   Summary: Invoke method OnChangeDynAttrValueColumn
   Description: Column value change for dynamic attribute.
This method does NOT support BPM.
   OperationID: OnChangeDynAttrValueColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDynAttrValueColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDynAttrValueColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDynAttrValueColumn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/OnChangeDynAttrValueColumn", {
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
   Summary: Invoke method OnChangeAttributeValuesColumnObject
   Description: Column value change for dynamic attribute where we are passing the dataset as an object such that we can apply the schema attributes
and avoid data type inferrance causing passed decimal values to become Integers.
This method does NOT support BPM, write BPM against OnChangeDynAttrValueColumn.
This method used by Dynamic Attribute Value Entry.
   OperationID: OnChangeAttributeValuesColumnObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeValuesColumnObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeValuesColumnObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttributeValuesColumnObject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/OnChangeAttributeValuesColumnObject", {
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
   Summary: Invoke method OnChangeDynAttrValueSetColumnObject
   Description: Column value change for dynamic attribute where we are passing the dataset as an object such that we can apply the schema attributes
and avoid data type inferrance causing passed decimal values to become Integers.
This method does NOT support BPM, write BPM against OnChangeDynAttrValueColumn.
This method used by Dynamic Attribute Value Set Maintenance.
   OperationID: OnChangeDynAttrValueSetColumnObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDynAttrValueSetColumnObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDynAttrValueSetColumnObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDynAttrValueSetColumnObject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/OnChangeDynAttrValueSetColumnObject", {
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
   Summary: Invoke method GetAttributeValues
   Description: Returns dataset of all related attribute values.
This method is used to return both types of attributes: dynamic attributes, inventory dynamic attributes.
   OperationID: GetAttributeValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributeValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributeValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributeValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetAttributeValues", {
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
   Summary: Invoke method GetAttributeValuesWithOutDynamicMetaDataDS
   Description: Returns dataset of all related attribute values.
This method is used to return both types of attributes: dynamic attributes, inventory dynamic attributes.
   OperationID: GetAttributeValuesWithOutDynamicMetaDataDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributeValuesWithOutDynamicMetaDataDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributeValuesWithOutDynamicMetaDataDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributeValuesWithOutDynamicMetaDataDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetAttributeValuesWithOutDynamicMetaDataDS", {
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
   Summary: Invoke method GetInventoryDynAttrValueParams
   Description: Returns dataset of inventory detail information and all related inventory dynamic attribute values.
   OperationID: GetInventoryDynAttrValueParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryDynAttrValueParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryDynAttrValueParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryDynAttrValueParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetInventoryDynAttrValueParams", {
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
   Summary: Invoke method GetDefaultsFromSelectedTemplate
   Description: Defaults attribute values from the selected template attribute set
   OperationID: GetDefaultsFromSelectedTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultsFromSelectedTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultsFromSelectedTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultsFromSelectedTemplate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetDefaultsFromSelectedTemplate", {
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
   Summary: Invoke method RefreshDynAttrValuesRow
   Description: Refreshes inverted dynamic attribute row
   OperationID: RefreshDynAttrValuesRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshDynAttrValuesRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshDynAttrValuesRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshDynAttrValuesRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/RefreshDynAttrValuesRow", {
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
   Summary: Invoke method MasterUpdate
   Description: Update which takes a whole dataset and first tries to find existing attribute set based on exact match of all attribute values and if found returns the id.
If one is not found will create the parent DynAttrValueSet and all child DynAttrValue records.
   OperationID: MasterUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/MasterUpdate", {
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
   Summary: Invoke method MasterUpdateFromMultiCompany
   Description: To be called from Multi-Company (Direct) Server Process exclusively
Update which takes a whole dataset and first tries to find existing attribute set based on exact match of all attribute values.
If an existing attribute set is not found, one will be created with the parent DynAttrValueSet and all child DynAttrValue records.
Regardless whether an existing attribute set is found or a new one is created, the related AttributeSetID is returned.
   OperationID: MasterUpdateFromMultiCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterUpdateFromMultiCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterUpdateFromMultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterUpdateFromMultiCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/MasterUpdateFromMultiCompany", {
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
   Summary: Invoke method MasterUpdateDynAttrValueSet
   Description: Update which takes a whole dataset and first tries to find existing attribute set based on exact match of all attribute values.
If an existing attribute set is not found, one will be created with the parent DynAttrValueSet and all child DynAttrValue records.
Regardless whether an existing attribute set is found or a new one is created, the related AttributeSetID is returned.
Set will be marked as Active and HasBeenUsed.
   OperationID: MasterUpdateDynAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterUpdateDynAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterUpdateDynAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterUpdateDynAttrValueSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/MasterUpdateDynAttrValueSet", {
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
   Summary: Invoke method UpdateDynAttrValueSetDataSet
   Description: Update Dynamic Attribute Value Set using a dynamically built DataTable
   OperationID: UpdateDynAttrValueSetDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDynAttrValueSetDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDynAttrValueSetDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDynAttrValueSetDataSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateDynAttrValueSetDataSet", {
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
   Summary: Invoke method UpdateDynAttrValueSetDataSetObject
   Description: Update Dynamic Attribute Value Set using a dynamically built DataTable
Passing dataset as an object such that we can apply the dynamic schema attributes and void dataType inferrance causing decimal values to become integers
   OperationID: UpdateDynAttrValueSetDataSetObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDynAttrValueSetDataSetObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDynAttrValueSetDataSetObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDynAttrValueSetDataSetObject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateDynAttrValueSetDataSetObject", {
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
   Summary: Invoke method UpdateAttributeValues
   Description: Update dynamic attribute values using a dynamically built inverted DataTable
This method is used to modify both types of attributes: dynamic attributes, inventory dynamic attributes.
   OperationID: UpdateAttributeValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAttributeValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateAttributeValues", {
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
   Summary: Invoke method UpdateAttributeValuesObject
   Description: Update dynamic attribute values using a dynamically built inverted DataTable
This method is used to modify both types of attributes: dynamic attributes, inventory dynamic attributes.
Passing dataset as an object such that we can apply the dynamic schema attributes and void dataType inferrance causing decimal values to become integers
   OperationID: UpdateAttributeValuesObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeValuesObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeValuesObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAttributeValuesObject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateAttributeValuesObject", {
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
   Summary: Invoke method GetDynAttrValueSetPlanningKeys
   Description: Returns PlanningAttributeSetSeq and PlanningAttributeSetHash based on attribute values
   OperationID: GetDynAttrValueSetPlanningKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynAttrValueSetPlanningKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynAttrValueSetPlanningKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDynAttrValueSetPlanningKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetDynAttrValueSetPlanningKeys", {
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
   Summary: Invoke method UpdateEntityAttributeSetFromConfigurator
   Description: Updates the target entity attribute set from a product configuration.
   OperationID: UpdateEntityAttributeSetFromConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateEntityAttributeSetFromConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateEntityAttributeSetFromConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateEntityAttributeSetFromConfigurator(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateEntityAttributeSetFromConfigurator", {
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
   Summary: Invoke method UpdateInventoryAttributes
   Description: Updates attribute set and line detail using dynamically built DataTable
   OperationID: UpdateInventoryAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateInventoryAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateInventoryAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateInventoryAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateInventoryAttributes", {
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
   Summary: Invoke method AssignDataFields
   Description: Assigns all data fields for related data type and perform validation on the field value.
   OperationID: AssignDataFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignDataFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignDataFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignDataFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/AssignDataFields", {
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
   Summary: Invoke method CheckAttributeChange
   Description: Method to return message if attributes or qty don't match linked SO on PO for BTO sales order.
   OperationID: CheckAttributeChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAttributeChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAttributeChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAttributeChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/CheckAttributeChange", {
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
   Summary: Invoke method UpdateSalesOrderComponentAttribute
   Description: Method to update the Quantity per Kit if the Quantity is modified in Attribute screen for Sales Kit Components in Sales Order.
   OperationID: UpdateSalesOrderComponentAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSalesOrderComponentAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSalesOrderComponentAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSalesOrderComponentAttribute(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateSalesOrderComponentAttribute", {
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
   Summary: Invoke method ValidateShortDescription
   Description: Used to validate a new attribute set based on AttrClassIS and ShortDescription.
This is only used by the UI when creating new set and not used when creating by an inventory transaction.
   OperationID: ValidateShortDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShortDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShortDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShortDescription(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/ValidateShortDescription", {
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
   Summary: Invoke method ValidateUniqueDynAttrValueSetByShortDescription
   Description: Validates and returns the AttributeSetID if unique set based on short description
   OperationID: ValidateUniqueDynAttrValueSetByShortDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUniqueDynAttrValueSetByShortDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUniqueDynAttrValueSetByShortDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUniqueDynAttrValueSetByShortDescription(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/ValidateUniqueDynAttrValueSetByShortDescription", {
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
   Summary: Invoke method GetNewDynAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrValueSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewDynAttrValueSet", {
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
   Summary: Invoke method GetNewDynAttrValue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewDynAttrValue", {
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
   Summary: Invoke method GetNewDynAttrValueSetLangDesc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrValueSetLangDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSetLangDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSetLangDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrValueSetLangDesc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetNewDynAttrValueSetLangDesc", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlComboValuesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrClassDtlComboValuesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrValueRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetLangDescRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrValueSetLangDescRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrValueSetListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrValueSetRow[],
}

export interface Erp_Tablesets_DynAttrClassDtlComboValuesRow{
   "AttrClassID":string,
   "AttributeID":string,
   "Code":string,
   "Description":string,
   "RelatedToSchemaName":string,
   "RelatedToTableName":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrValueRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Schema name for the related table.  */  
   "RelatedToSchemaName":string,
      /**  Table name for the related table.  */  
   "RelatedToTableName":string,
      /**  SysRowID for the related to table.  */  
   "RelatedToSysRowID":string,
      /**  ID of parent Attribute Class  */  
   "AttrClassID":string,
      /**  Attribute ID.  */  
   "AttributeID":string,
      /**  Character Data.  */  
   "DataCharacter":string,
      /**  Date Data.  */  
   "DataDate":string,
      /**  Decimal Data.  */  
   "DataDecimal":number,
      /**  Integer Data.  */  
   "DataInteger":number,
      /**  Logical Data.  */  
   "DataLogical":boolean,
      /**  Date Type.  */  
   "FieldDataType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Indicates this value is a result of a calculation.  */  
   "IsCalculated":boolean,
      /**  Used for planning to indicates for the set that this was the Actual quantity at that point in time.  */  
   "IsActual":boolean,
   "FieldValue":string,
   "TransportValue":string,
   "Active":boolean,
   "FieldLabel":string,
   "FieldFormat":string,
   "AttributeValueSeq":number,
      /**  Controls the order attributes are displayed and updated.  */  
   "SortSeq":number,
      /**  System controlled to validate all dynamic attribute values against the set hash key.  If the value has been verified it will not perform the validation again.  */  
   "HasBeenVerified":boolean,
      /**  Indicates if this calculated field will be visible in attribute entry.  */  
   "IsViewable":boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  Controlled by setup on attribute detail in Dynamic Attribute Class Maintenance.  */  
   "IsReadOnly":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrValueSetLangDescRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Language ID.  */  
   "LangNameID":string,
      /**  Language Description for Attribute Set.  */  
   "Description":string,
      /**  Language Short Description for Attribute Set.  */  
   "ShortDescription":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "LangNameIDDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrValueSetListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Description of values in set.  */  
   "Description":string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  */  
   "ShortDescription":string,
      /**  ID of parent Attribute Class  */  
   "AttrClassID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrValueSetRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Description of values in set.  */  
   "Description":string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  */  
   "ShortDescription":string,
      /**  ID of parent Attribute Class  */  
   "AttrClassID":string,
      /**  Hash key of Attribute IDs and values (excluding calculated attributes), and Full Expression.  */  
   "AttributeSetHash":string,
      /**  Set to true when the user has determined that the Attribute Set is active.  */  
   "Active":boolean,
      /**  Set to true with the system has determined that the Attribute Set has been used, indicating that it cannot be modified except for the user-defined short description.  */  
   "HasBeenUsed":boolean,
      /**  Result quantity calculated from a user created expression.  */  
   "ExpressionResultQty":number,
      /**  The UOM related to the Expression Result Qty.  */  
   "ExpressionResultUOM":string,
      /**  Full user maintained expression  */  
   "FullExpression":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  The unique identifier of the Dynamic Attribute Planning Set.  */  
   "PlanningAttributeSetSeq":number,
      /**  Hash key of the Company, AttrClassID, Planning Attributes and Planning Attribute Values.  */  
   "PlanningAttributeSetHash":string,
      /**  Indicates the set is used by planning.  */  
   "IsPlanningAttributeSet":boolean,
      /**  Indicates when this attribute set will be available for selecting during entry: Planning, Supply, Demand.  This is system maintained based on changes made in Dynamic Attribute Class Maintenance and is not directly user maintainable.  */  
   "WhereAvailable":number,
      /**  Development use only.  Used in 11.1.100 for additional Hash Key including calculated fields.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevDecimal01":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  Indicates where this Attribute Set is required.  */  
   "RequiredAt":number,
      /**  Indicates when this set is available as a template for selecting during Attribute Entry: Supply, Demand, Both.  */  
   "TemplateWhereAvailable":number,
      /**  Hash key of all the Attribute IDs and values, without Full Expression.  */  
   "AttributeSetHashAllValues":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "BitFlag":number,
   "AttrClassIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param relatedToEntity
      @param fieldValue
      @param ttDynAttrValue
   */  
export interface AssignDataFields_input{
   relatedToEntity:string,
   fieldValue:any,      //schema had no properties on an object.
   ttDynAttrValue:Erp_Tablesets_DynAttrValueRow[],
}

export interface AssignDataFields_output{
parameters : {
      /**  output parameters  */  
   ttDynAttrValue:Erp_Tablesets_DynAttrValueRow[],
}
}

   /** Required : 
      @param remainingQty
      @param attributeSetID
      @param poRelSysRowID
   */  
export interface CheckAttributeChange_input{
      /**  remainingQty  */  
   remainingQty:number,
      /**  attributeSetID  */  
   attributeSetID:number,
      /**  PO to validate  */  
   poRelSysRowID:string,
}

export interface CheckAttributeChange_output{
parameters : {
      /**  output parameters  */  
   notifySalesQtyMsg:string,
   notifySalesAttributeMsg:string,
}
}

   /** Required : 
      @param attributeSetID
   */  
export interface DeleteByID_input{
   attributeSetID:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param attrClassID
      @param attributeChanging
      @param ds
   */  
export interface DynAttrValueColumnChanging_input{
   attrClassID:string,
   attributeChanging:string,
   ds:Erp_Tablesets_AttributeChangingTableset[],
}

export interface DynAttrValueColumnChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AttributeChangingTableset[],
}
}

export interface Erp_Tablesets_AttributeChangingParamsRow{
      /**  ID of parent Attribute Class  */  
   AttrClassID:string,
      /**  Attribute that is changing initiating the on change event.  */  
   AttributeChanging:string,
      /**  Unique identifier of set of attributes.  */  
   AttributeChangingID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number of related table being modified.  */  
   PartNum:string,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  SysRowID for the related to table.  */  
   RelatedToSysRowID:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AttributeChangingTableset{
   AttributeChangingParams:Erp_Tablesets_AttributeChangingParamsRow[],
   AttributeChangingValues:Erp_Tablesets_AttributeChangingValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AttributeChangingValuesRow{
      /**  Unique identifier of set of attributes.  */  
   AttributeChangingID:number,
      /**  Attribute ID.  */  
   AttributeID:string,
      /**  Value of attribute converted to string.  */  
   AttributeValue:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Date Type.  */  
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrClassDtlComboValuesRow{
   AttrClassID:string,
   AttributeID:string,
   Code:string,
   Description:string,
   RelatedToSchemaName:string,
   RelatedToTableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrValueRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
      /**  SysRowID for the related to table.  */  
   RelatedToSysRowID:string,
      /**  ID of parent Attribute Class  */  
   AttrClassID:string,
      /**  Attribute ID.  */  
   AttributeID:string,
      /**  Character Data.  */  
   DataCharacter:string,
      /**  Date Data.  */  
   DataDate:string,
      /**  Decimal Data.  */  
   DataDecimal:number,
      /**  Integer Data.  */  
   DataInteger:number,
      /**  Logical Data.  */  
   DataLogical:boolean,
      /**  Date Type.  */  
   FieldDataType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates this value is a result of a calculation.  */  
   IsCalculated:boolean,
      /**  Used for planning to indicates for the set that this was the Actual quantity at that point in time.  */  
   IsActual:boolean,
   FieldValue:string,
   TransportValue:string,
   Active:boolean,
   FieldLabel:string,
   FieldFormat:string,
   AttributeValueSeq:number,
      /**  Controls the order attributes are displayed and updated.  */  
   SortSeq:number,
      /**  System controlled to validate all dynamic attribute values against the set hash key.  If the value has been verified it will not perform the validation again.  */  
   HasBeenVerified:boolean,
      /**  Indicates if this calculated field will be visible in attribute entry.  */  
   IsViewable:boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  Controlled by setup on attribute detail in Dynamic Attribute Class Maintenance.  */  
   IsReadOnly:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrValueSetLangDescRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Language ID.  */  
   LangNameID:string,
      /**  Language Description for Attribute Set.  */  
   Description:string,
      /**  Language Short Description for Attribute Set.  */  
   ShortDescription:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   LangNameIDDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrValueSetListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Description of values in set.  */  
   Description:string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  */  
   ShortDescription:string,
      /**  ID of parent Attribute Class  */  
   AttrClassID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrValueSetListTableset{
   DynAttrValueSetList:Erp_Tablesets_DynAttrValueSetListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DynAttrValueSetRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Description of values in set.  */  
   Description:string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  */  
   ShortDescription:string,
      /**  ID of parent Attribute Class  */  
   AttrClassID:string,
      /**  Hash key of Attribute IDs and values (excluding calculated attributes), and Full Expression.  */  
   AttributeSetHash:string,
      /**  Set to true when the user has determined that the Attribute Set is active.  */  
   Active:boolean,
      /**  Set to true with the system has determined that the Attribute Set has been used, indicating that it cannot be modified except for the user-defined short description.  */  
   HasBeenUsed:boolean,
      /**  Result quantity calculated from a user created expression.  */  
   ExpressionResultQty:number,
      /**  The UOM related to the Expression Result Qty.  */  
   ExpressionResultUOM:string,
      /**  Full user maintained expression  */  
   FullExpression:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  The unique identifier of the Dynamic Attribute Planning Set.  */  
   PlanningAttributeSetSeq:number,
      /**  Hash key of the Company, AttrClassID, Planning Attributes and Planning Attribute Values.  */  
   PlanningAttributeSetHash:string,
      /**  Indicates the set is used by planning.  */  
   IsPlanningAttributeSet:boolean,
      /**  Indicates when this attribute set will be available for selecting during entry: Planning, Supply, Demand.  This is system maintained based on changes made in Dynamic Attribute Class Maintenance and is not directly user maintainable.  */  
   WhereAvailable:number,
      /**  Development use only.  Used in 11.1.100 for additional Hash Key including calculated fields.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevDecimal01:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  Indicates where this Attribute Set is required.  */  
   RequiredAt:number,
      /**  Indicates when this set is available as a template for selecting during Attribute Entry: Supply, Demand, Both.  */  
   TemplateWhereAvailable:number,
      /**  Hash key of all the Attribute IDs and values, without Full Expression.  */  
   AttributeSetHashAllValues:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   BitFlag:number,
   AttrClassIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrValueSetTableset{
   DynAttrValueSet:Erp_Tablesets_DynAttrValueSetRow[],
   DynAttrValue:Erp_Tablesets_DynAttrValueRow[],
   DynAttrValueSetLangDesc:Erp_Tablesets_DynAttrValueSetLangDescRow[],
   DynAttrClassDtlComboValues:Erp_Tablesets_DynAttrClassDtlComboValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DynFieldAttributesRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   DataType:string,
   Required:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   BizType:string,
   CGCCode:string,
   UomColumn:string,
   CodeDescriptionList:string,
   Seq:number,
   IsHidden:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynFieldHelpRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   Description:string,
   DBTableName:string,
   DBFieldName:string,
   External:boolean,
   InitialValue:string,
   IsDescriptionField:boolean,
   SystemFlag:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynTableAttributesRow{
   SystemCode:string,
      /**  The actual generic table name used by the BL  */  
   DataTableID:string,
      /**  Unique identifier for the virtual schema  */  
   UniqueTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynamicMetadataTableset{
   DynTableAttributes:Erp_Tablesets_DynTableAttributesRow[],
   DynFieldAttributes:Erp_Tablesets_DynFieldAttributesRow[],
   DynFieldHelp:Erp_Tablesets_DynFieldHelpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvTransParamsTableset{
   InvTransfer:Erp_Tablesets_InvTransferRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvTransferRow{
      /**  Date of transaction.  */  
   TranDate:string,
   FromOnHandQty:number,
   ToOnHandQty:number,
      /**  Transfer Quantity entered for this inventory transfer.  */  
   TransferQty:number,
   Company:string,
      /**  The Warehouse the part is being transferred From.  */  
   FromWarehouseCode:string,
      /**  The Warehouse the part is being transferred To.  */  
   ToWarehouseCode:string,
      /**  The Warehouse Bin the part is being transferred From.  */  
   FromBinNum:string,
      /**  The Warehouse Bin the part is being transferred To.  */  
   ToBinNum:string,
      /**  The Lot number that is being transferred.  */  
   FromLotNumber:string,
      /**  The Lot number that is being transferred to.  */  
   ToLotNumber:string,
      /**  The Part Number selected for inventory transfer.  */  
   PartNum:string,
      /**  Plant than owns the FromWarehouseCode  */  
   FromPlant:string,
      /**  Plant that owns the ToWarehouseCode  */  
   ToPlant:string,
   FromOnHandUOM:string,
      /**  The unit of measure the quantify of this transfer is specified in.  */  
   TransferQtyUOM:string,
   ToOnHandUOM:string,
   Plant:string,
   Plant2:string,
   AttributeSetID:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InventoryDynAttrValueParamsTableset{
   InventoryDynAttrValueSummary:Erp_Tablesets_InventoryDynAttrValueSummaryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InventoryDynAttrValueSummaryRow{
   AttrClassID:string,
   Company:string,
   DualQty:number,
   DualUM:string,
   IUM:string,
   OurQty:number,
   LineDesc:string,
   PartNum:string,
   RemainingDualQty:number,
   RemainingOurQty:number,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  SysRowID for the related to table.  */  
   RelatedToSysRowID:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
   EnteredDualQty:number,
   EnteredOurQty:number,
      /**  Indicates if this Attribute Class has an MRP tracking attribute.  */  
   UsedInPlanning:boolean,
      /**  Error number  */  
   ErrorType:number,
      /**  Error message  */  
   ErrorMsg:string,
      /**  True if need to update  */  
   NeedToUpdate:boolean,
      /**  Indicates what level sets are available as a template for selecting during Attribute Entry: Supply, Demand, Both.  */  
   TemplateWhereAvailable:number,
      /**  Exception was thrown when calling a service.  */  
   ServiceError:boolean,
      /**  Exception message that thrown when calling a service.  */  
   ServiceErrorMessage:string,
      /**  Action specific to an entity, which will control how Inventory Attribute Entry closes and action to follow.  */  
   EntityAction1:string,
      /**  Action specific to an entity, which will control how Inventory Attribute Entry closes and action to follow.  */  
   EntityAction2:string,
      /**  Action Message specific to an entity, which will show at closing of the Inventory Attribute Entry.  */  
   EntityActionMessage1:string,
      /**  Action Message specific to an entity, which will show at closing of the Inventory Attribute Entry.  */  
   EntityActionMessage2:string,
      /**  Action Message Title specific to an entity, can be blank and standard defaults will be used.  */  
   EntityActionMessageTitle1:string,
      /**  Action Message Title specific to an entity, can be blank and standard defaults will be used.  */  
   EntityActionMessageTitle2:string,
      /**  Final update needs to be performed on window close.  */  
   PerformUpdateOnClose:boolean,
      /**  Show summary information for part and totals  */  
   ShowSummaryInformation:boolean,
      /**  Perform attribute changing events.  It is determined if executed if approved BPMs exist.  */  
   PerformAttributeOnChangeEvent:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  This is only used when using single update.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  This is only used when using single update.  */  
   NumberOfPieces:number,
      /**  Split quantity that was successfully posted.  */  
   CommittedSplitQty:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Indicates if inventory for this part is tracked at the attribute level.  */  
   TrackInventoryAttributes:boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtDynAttrValueSetTableset{
   DynAttrValueSet:Erp_Tablesets_DynAttrValueSetRow[],
   DynAttrValue:Erp_Tablesets_DynAttrValueRow[],
   DynAttrValueSetLangDesc:Erp_Tablesets_DynAttrValueSetLangDescRow[],
   DynAttrClassDtlComboValues:Erp_Tablesets_DynAttrClassDtlComboValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param attrClassID
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param invTransferParams
      @param inventoryDynAttrValueParamsTS
   */  
export interface GetAttributeValuesWithOutDynamicMetaDataDS_input{
   attrClassID:string,
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   invTransferParams:Erp_Tablesets_InvTransParamsTableset[],
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
}

export interface GetAttributeValuesWithOutDynamicMetaDataDS_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
}
}

   /** Required : 
      @param attrClassID
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param invTransferParams
      @param inventoryDynAttrValueParamsTS
   */  
export interface GetAttributeValues_input{
   attrClassID:string,
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   invTransferParams:Erp_Tablesets_InvTransParamsTableset[],
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
}

export interface GetAttributeValues_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param dynamicMetadataDS
   */  
export interface GetByIDDynAttrValueSetDataSet_input{
   attributeSetID:number,
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}

export interface GetByIDDynAttrValueSetDataSet_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param attributeSetID
   */  
export interface GetByID_input{
   attributeSetID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DynAttrValueSetTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DynAttrValueSetTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DynAttrValueSetTableset[],
}

   /** Required : 
      @param dynAttrValueDS
      @param templateAttributeSetID
   */  
export interface GetDefaultsFromSelectedTemplate_input{
   dynAttrValueDS:any,      //schema had no properties on an object.
   templateAttributeSetID:number,
}

export interface GetDefaultsFromSelectedTemplate_output{
parameters : {
      /**  output parameters  */  
   dynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param attrClassID
      @param attributeIDs
      @param attributeValues
   */  
export interface GetDynAttrValueSetPlanningKeys_input{
   attrClassID:string,
   attributeIDs:string,
   attributeValues:string,
}

export interface GetDynAttrValueSetPlanningKeys_output{
parameters : {
      /**  output parameters  */  
   planningAttributeSetSeq:number,
   planningAttributeSetHash:string,
}
}

   /** Required : 
      @param attrClassID
      @param schemaOnly
      @param dynamicMetadataDS
   */  
export interface GetFullDynAttrValueSetDataSetByAttrClassID_input{
   attrClassID:string,
   schemaOnly:boolean,
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}

export interface GetFullDynAttrValueSetDataSetByAttrClassID_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param attrClassID
      @param attributeIDList
      @param dynamicMetadataDS
   */  
export interface GetFullDynAttrValueSetDataSetByList_input{
   attrClassID:string,
   attributeIDList:number,
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}

export interface GetFullDynAttrValueSetDataSetByList_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param attrClassID
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param invTransferParams
      @param inventoryDynAttrValueParamsTS
   */  
export interface GetInventoryDynAttrValueParams_input{
   attrClassID:string,
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   invTransferParams:Erp_Tablesets_InvTransParamsTableset[],
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
}

export interface GetInventoryDynAttrValueParams_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   inventoryDynAttrValueDS: UNKNOW TYPE(error 2338),
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
   returnObj:Erp_Tablesets_DynAttrValueSetListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param inventoryDynAttrValueParamsTS
      @param inventoryDynAttrValueDS
   */  
export interface GetNewAttributeValuesRowWithOutDynamicMetaDataDS_input{
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   inventoryDynAttrValueDS:any,      //schema had no properties on an object.
}

export interface GetNewAttributeValuesRowWithOutDynamicMetaDataDS_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   inventoryDynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param inventoryDynAttrValueParamsTS
      @param inventoryDynAttrValueDS
   */  
export interface GetNewAttributeValuesRow_input{
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   inventoryDynAttrValueDS:any,      //schema had no properties on an object.
}

export interface GetNewAttributeValuesRow_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   inventoryDynAttrValueDS: UNKNOW TYPE(error 2338),
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param atrClassID
      @param ds
      @param dynamicMetadataDS
   */  
export interface GetNewDynAttrValueSetDataSet_input{
   atrClassID:string,
   ds:any,      //schema had no properties on an object.
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}

export interface GetNewDynAttrValueSetDataSet_output{
parameters : {
      /**  output parameters  */  
   ds: UNKNOW TYPE(error 2338),
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param ds
      @param attributeSetID
   */  
export interface GetNewDynAttrValueSetLangDesc_input{
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
   attributeSetID:number,
}

export interface GetNewDynAttrValueSetLangDesc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param attrClassID
      @param ds
   */  
export interface GetNewDynAttrValueSetTableset_input{
   attrClassID:string,
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}

export interface GetNewDynAttrValueSetTableset_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDynAttrValueSet_input{
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}

export interface GetNewDynAttrValueSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param attrClassID
   */  
export interface GetNewDynAttrValue_input{
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   attrClassID:string,
}

export interface GetNewDynAttrValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param attrClassID
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param inventoryDynAttrValueParamsTS
   */  
export interface GetNewInventoryDynAttrValueSummary_input{
   attrClassID:string,
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
}

export interface GetNewInventoryDynAttrValueSummary_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
}
}

   /** Required : 
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param inventoryDynAttrValueDS
   */  
export interface GetNewInventoryDynAttrValuesRow_input{
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   inventoryDynAttrValueDS:any,      //schema had no properties on an object.
}

export interface GetNewInventoryDynAttrValuesRow_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueDS: UNKNOW TYPE(error 2338),
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param whereClauseDynAttrValueSet
      @param whereClauseDynAttrValue
      @param whereClauseDynAttrValueSetLangDesc
      @param whereClauseDynAttrClassDtlComboValues
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDynAttrValueSet:string,
   whereClauseDynAttrValue:string,
   whereClauseDynAttrValueSetLangDesc:string,
   whereClauseDynAttrClassDtlComboValues:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DynAttrValueSetTableset[],
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
   */  
export interface MasterUpdateDynAttrValueSet_input{
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}

export interface MasterUpdateDynAttrValueSet_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface MasterUpdateFromMultiCompany_input{
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}

export interface MasterUpdateFromMultiCompany_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface MasterUpdate_input{
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}

export interface MasterUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param attrClassID
      @param columnName
      @param columnValue
      @param inventoryDynAttrValueParamsTS
      @param modifiedDynAttrValueDS
   */  
export interface OnChangeAttributeValuesColumnObject_input{
   attrClassID:string,
   columnName:string,
   columnValue:string,
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   modifiedDynAttrValueDS:any,      //schema had no properties on an object.
}

export interface OnChangeAttributeValuesColumnObject_output{
parameters : {
      /**  output parameters  */  
   modifiedDynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param columnName
      @param columnValue
      @param modifiedDynAttrValueDS
   */  
export interface OnChangeDynAttrValueColumn_input{
   columnName:string,
   columnValue:string,
   modifiedDynAttrValueDS:any,      //schema had no properties on an object.
}

export interface OnChangeDynAttrValueColumn_output{
parameters : {
      /**  output parameters  */  
   modifiedDynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param attrClassID
      @param columnName
      @param columnValue
      @param modifiedDynAttrValueDS
   */  
export interface OnChangeDynAttrValueSetColumnObject_input{
   attrClassID:string,
   columnName:string,
   columnValue:string,
   modifiedDynAttrValueDS:any,      //schema had no properties on an object.
}

export interface OnChangeDynAttrValueSetColumnObject_output{
parameters : {
      /**  output parameters  */  
   modifiedDynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param dynAttrValueDS
   */  
export interface RefreshDynAttrValuesRow_input{
   dynAttrValueDS:any,      //schema had no properties on an object.
}

export interface RefreshDynAttrValuesRow_output{
parameters : {
      /**  output parameters  */  
   dynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param attrClassID
      @param commitLineDtl
      @param invTrasferParams
      @param inventoryDynAttrValueParamsTS
      @param dynAttrValueDS
   */  
export interface UpdateAttributeValuesObject_input{
   attrClassID:string,
   commitLineDtl:boolean,
   invTrasferParams:Erp_Tablesets_InvTransParamsTableset[],
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   dynAttrValueDS:any,      //schema had no properties on an object.
}

export interface UpdateAttributeValuesObject_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   dynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param commitLineDtl
      @param invTrasferParams
      @param inventoryDynAttrValueParamsTS
      @param dynAttrValueDS
   */  
export interface UpdateAttributeValues_input{
   commitLineDtl:boolean,
   invTrasferParams:Erp_Tablesets_InvTransParamsTableset[],
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   dynAttrValueDS:any,      //schema had no properties on an object.
}

export interface UpdateAttributeValues_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   dynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param attrClassID
      @param ds
   */  
export interface UpdateDynAttrValueSetDataSetObject_input{
   attrClassID:string,
   ds:any,      //schema had no properties on an object.
}

export interface UpdateDynAttrValueSetDataSetObject_output{
parameters : {
      /**  output parameters  */  
   ds: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateDynAttrValueSetDataSet_input{
   ds:any,      //schema had no properties on an object.
}

export interface UpdateDynAttrValueSetDataSet_output{
parameters : {
      /**  output parameters  */  
   ds: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param targetEntityTableName
      @param targetEntitySysRowID
      @param dynAttrValueSetDS
   */  
export interface UpdateEntityAttributeSetFromConfigurator_input{
   targetEntityTableName:string,
   targetEntitySysRowID:string,
   dynAttrValueSetDS:Erp_Tablesets_DynAttrValueSetTableset[],
}

export interface UpdateEntityAttributeSetFromConfigurator_output{
parameters : {
      /**  output parameters  */  
   dynAttrValueSetDS:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDynAttrValueSetTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDynAttrValueSetTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param commitLineDtl
      @param inventoryDynAttrValueParamsTS
      @param modifiedDynAttrValueDS
      @param invTrasferParams
   */  
export interface UpdateInventoryAttributes_input{
   commitLineDtl:boolean,
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   modifiedDynAttrValueDS:any,      //schema had no properties on an object.
   invTrasferParams:Erp_Tablesets_InvTransParamsTableset[],
}

export interface UpdateInventoryAttributes_output{
parameters : {
      /**  output parameters  */  
   inventoryDynAttrValueParamsTS:Erp_Tablesets_InventoryDynAttrValueParamsTableset[],
   updatedDynAttrValueDS: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param orderDtlSysRowID
      @param orderQty
   */  
export interface UpdateSalesOrderComponentAttribute_input{
      /**  Order number to validate  */  
   orderDtlSysRowID:string,
      /**  New Order Quantity for Sales Kit Component  */  
   orderQty:number,
}

export interface UpdateSalesOrderComponentAttribute_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrValueSetTableset[],
}
}

   /** Required : 
      @param attrClassID
      @param shortDescription
      @param attributeSetID
   */  
export interface ValidateShortDescription_input{
   attrClassID:string,
   shortDescription:string,
   attributeSetID:number,
}

export interface ValidateShortDescription_output{
}

   /** Required : 
      @param attrClassID
      @param shortDescription
   */  
export interface ValidateUniqueDynAttrValueSetByShortDescription_input{
   attrClassID:string,
   shortDescription:string,
}

export interface ValidateUniqueDynAttrValueSetByShortDescription_output{
parameters : {
      /**  output parameters  */  
   attributeSetID:number,
}
}

