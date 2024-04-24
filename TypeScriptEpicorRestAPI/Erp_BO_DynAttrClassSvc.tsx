import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DynAttrClassSvc
// Description: Dynamic Attribute Class Maintenance
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/$metadata", {
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
   Description: Get DynAttrClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClasses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassRow
   */  
export function get_DynAttrClasses(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrClasses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynAttrClass item
   Description: Calls GetByID to retrieve the DynAttrClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
   */  
export function get_DynAttrClasses_Company_AttrClassID(Company:string, AttrClassID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrClass for the service
   Description: Calls UpdateExt to update DynAttrClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrClasses_Company_AttrClassID(Company:string, AttrClassID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")", {
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
   Summary: Call UpdateExt to delete DynAttrClass item
   Description: Call UpdateExt to delete DynAttrClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrClasses_Company_AttrClassID(Company:string, AttrClassID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")", {
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
   Description: Get DynAttrClassDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DynAttrClassDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlRow
   */  
export function get_DynAttrClasses_Company_AttrClassID_DynAttrClassDtls(Company:string, AttrClassID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")/DynAttrClassDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynAttrClassDtl item
   Description: Calls GetByID to retrieve the DynAttrClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   */  
export function get_DynAttrClasses_Company_AttrClassID_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company:string, AttrClassID:string, AttributeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClassDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlRow
   */  
export function get_DynAttrClassDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrClassDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynAttrClassDtl item
   Description: Calls GetByID to retrieve the DynAttrClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   */  
export function get_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company:string, AttrClassID:string, AttributeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrClassDtl for the service
   Description: Calls UpdateExt to update DynAttrClassDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company:string, AttrClassID:string, AttributeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")", {
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
   Summary: Call UpdateExt to delete DynAttrClassDtl item
   Description: Call UpdateExt to delete DynAttrClassDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company:string, AttrClassID:string, AttributeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")", {
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
   Description: Get DynAttrClassDtlListVals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DynAttrClassDtlListVals1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlListValRow
   */  
export function get_DynAttrClassDtls_Company_AttrClassID_AttributeID_DynAttrClassDtlListVals(Company:string, AttrClassID:string, AttributeID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListValRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")/DynAttrClassDtlListVals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListValRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlListVal item
   Description: Calls GetByID to retrieve the DynAttrClassDtlListVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlListVal1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param Code Desc: Code   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   */  
export function get_DynAttrClassDtls_Company_AttrClassID_AttributeID_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company:string, AttrClassID:string, AttributeID:string, Code:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrClassDtlListValRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrClassDtlListValRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClassDtlListVals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtlListVals
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlListValRow
   */  
export function get_DynAttrClassDtlListVals(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListValRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListValRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtlListVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrClassDtlListVals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlListVal item
   Description: Calls GetByID to retrieve the DynAttrClassDtlListVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlListVal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param Code Desc: Code   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   */  
export function get_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company:string, AttrClassID:string, AttributeID:string, Code:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrClassDtlListValRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrClassDtlListValRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrClassDtlListVal for the service
   Description: Calls UpdateExt to update DynAttrClassDtlListVal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtlListVal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param Code Desc: Code   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company:string, AttrClassID:string, AttributeID:string, Code:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")", {
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
   Summary: Call UpdateExt to delete DynAttrClassDtlListVal item
   Description: Call UpdateExt to delete DynAttrClassDtlListVal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtlListVal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param Code Desc: Code   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company:string, AttrClassID:string, AttributeID:string, Code:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassListRow)
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
export function get_GetRows(whereClauseDynAttrClass:string, whereClauseDynAttrClassDtl:string, whereClauseDynAttrClassDtlListVal:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDynAttrClass!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrClass=" + whereClauseDynAttrClass
   }
   if(typeof whereClauseDynAttrClassDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrClassDtl=" + whereClauseDynAttrClassDtl
   }
   if(typeof whereClauseDynAttrClassDtlListVal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrClassDtlListVal=" + whereClauseDynAttrClassDtlListVal
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetRows" + params, {
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
export function get_GetByID(attrClassID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof attrClassID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attrClassID=" + attrClassID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetByID" + params, {
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
   Summary: Invoke method DuplicateDynAttrClass
   Description: Duplicates the current Dynamic Attribute Class
   OperationID: DuplicateDynAttrClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateDynAttrClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateDynAttrClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateDynAttrClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DuplicateDynAttrClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFieldDataType
   Description: Used when the Data Type field of DynAttrClassDtl has been changed to a new value.
Resets all possible fields.
   OperationID: OnChangeFieldDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFieldDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFieldDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFieldDataType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/OnChangeFieldDataType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAttributeID
   Description: Used when the AttributeID field has changed on DynAttrClassDtl record.
   OperationID: OnChangeAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttributeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/OnChangeAttributeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAttributeID
   Description: Used to check if the entered AttributeID is in the DynAttrMasterDtl record
   OperationID: CheckAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAttributeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/CheckAttributeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBizType
   Description: Handles require changes to Attribute when the Business Type changes: sets the Required At list picker
   OperationID: ChangeBizType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBizType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBizType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBizType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/ChangeBizType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUsedInPlanning
   Description: Handles require changes to Attribute when the MRP changes: sets the Required At list picker
   OperationID: ChangeUsedInPlanning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUsedInPlanning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUsedInPlanning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUsedInPlanning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/ChangeUsedInPlanning", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRelatedToTableName
   Description: Used when the RelatedToTableName field of DynAttrClass has been changed to a new value.
Resets all possible fields.
   OperationID: OnChangeRelatedToTableName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRelatedToTableName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRelatedToTableName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRelatedToTableName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/OnChangeRelatedToTableName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetDynAttrClassDtlIsExpressionDefined
   Description: Indicates if calculated expression has been entered.
   OperationID: SetDynAttrClassDtlIsExpressionDefined
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDynAttrClassDtlIsExpressionDefined_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDynAttrClassDtlIsExpressionDefined_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetDynAttrClassDtlIsExpressionDefined(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/SetDynAttrClassDtlIsExpressionDefined", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFormat
   Description: Validates data format
   OperationID: ValidateFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFormat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/ValidateFormat", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RegenerateAttributeSetHash
   Description: Regenerates AttributeSetHash - specific for sets with calculated fields
   OperationID: RegenerateAttributeSetHash
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenerateAttributeSetHash_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateAttributeSetHash_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegenerateAttributeSetHash(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/RegenerateAttributeSetHash", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelatedToTableNameListFromLandingPage
   Description: This method returns the list of Related To Table Names plus the value 'All' for use in the Landing Page.
   OperationID: GetRelatedToTableNameListFromLandingPage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedToTableNameListFromLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedToTableNameListFromLandingPage(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetRelatedToTableNameListFromLandingPage", {
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
   Summary: Invoke method GetRelatedToTableNameList
   Description: This method returns the list of Related To Table Names.
   OperationID: GetRelatedToTableNameList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedToTableNameList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedToTableNameList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetRelatedToTableNameList", {
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
   Summary: Invoke method GetNewDynAttrClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetNewDynAttrClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDynAttrClassDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClassDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClassDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClassDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrClassDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetNewDynAttrClassDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDynAttrClassDtlListVal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClassDtlListVal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClassDtlListVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClassDtlListVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrClassDtlListVal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetNewDynAttrClassDtlListVal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListValRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrClassDtlListValRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrClassDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrClassListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrClassRow[],
}

export interface Erp_Tablesets_DynAttrClassDtlListValRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ID of parent attribute class.  */  
   "AttrClassID":string,
      /**  Unique ID of attribute for this class.  */  
   "AttributeID":string,
      /**  Code value that will be store in the DynAttrValue.  */  
   "Code":string,
      /**  Schema name for the related table.  */  
   "RelatedToSchemaName":string,
      /**  Table name for the related table.  */  
   "RelatedToTableName":string,
      /**  Description of list value that will show in list.  */  
   "Description":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Indicates if the Attribute List Value is Active. Default is false.  Once Active, the system will allow it to be used.  */  
   "Active":boolean,
      /**  Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).  */  
   "PlanningConvOperator":string,
      /**  Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.  */  
   "PlanningConvFactor":number,
      /**  Indicates when this list value will be available for selecting during entry: Planning, Supply, Demand.  */  
   "WhereAvailable":number,
      /**  Theoretical UOM used by MRP for conversions to the related Actual quantity.  */  
   "TheoreticalUOM":string,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevDecimal01":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrClassDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ID of parent Attribute Class  */  
   "AttrClassID":string,
      /**  Unique ID of attribute for this class  */  
   "AttributeID":string,
      /**  Schema name for the related table.  */  
   "RelatedToSchemaName":string,
      /**  Table name for the related table.  */  
   "RelatedToTableName":string,
      /**  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  */  
   "Active":boolean,
      /**  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  */  
   "Description":string,
      /**  Date type for this attribute field.  */  
   "FieldDataType":string,
      /**  Format for the given date type for this attribute field.  */  
   "FieldFormat":string,
      /**  Defines the field lablel for this attribute.  */  
   "FieldLabel":string,
      /**  The value that determines the increments used when linked to a numeric input.  */  
   "IncrPrec":number,
      /**  Initial character value.  */  
   "InitialCharacter":string,
      /**  Initial date value.  */  
   "InitialDate":string,
      /**  Initial decimal value.  */  
   "InitialDecimal":number,
      /**  Initial integer value.  */  
   "InitialInteger":number,
      /**  Initial logical value.  */  
   "InitialLogical":boolean,
      /**  The user defined maximum acceptable value when linked to a date input.  */  
   "MaxDate":string,
      /**  The user defined maximum acceptable value when linked to a decimal input.  */  
   "MaxDecimal":number,
      /**  The user defined maximum acceptable value when linked to an integer input.  */  
   "MaxInteger":number,
      /**  The user defined minimum acceptable value when linked to a date input.  */  
   "MinDate":string,
      /**  The user defined minimum acceptable value when linked to a decimal input.  */  
   "MinDecimal":number,
      /**  The user defined minimum acceptable value when linked to an integer input.  */  
   "MinInteger":number,
      /**  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  */  
   "WebAttribute":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Further defines the business use of the field, valid values are "Quantity,UOM"  */  
   "BizType":string,
      /**  Attribute ID of related UOM linked to quantity.  */  
   "UOMAttributeID":string,
      /**  Controls the order attributes are displayed and updated.  */  
   "SortSeq":number,
      /**  If attribute is used in planning.  */  
   "UsedInPlanning":boolean,
      /**  Indicated this attribute will be used as a calculated field.  */  
   "IsCalculated":boolean,
      /**  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  */  
   "PlanningBaseUOM":string,
      /**  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  */  
   "PlanningType":string,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevDecimal01":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  The actual transaction value for the attribute set.  */  
   "IsActual":boolean,
      /**  Indicates if this attribute will be visible in attribute entry.  */  
   "IsViewable":boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  */  
   "IsReadOnly":boolean,
      /**  Resuable Attribute linked to this class attribute.  */  
   "MasterDtlLinked":string,
      /**  Indicates if changes made to Reusable Attributes are synch to this class attribute.  */  
   "MasterDtlSync":boolean,
      /**  Indicates a pre-defined System Attribute Class.  */  
   "SystemFlag":boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  */  
   "IncludeListValueCodeInShortDesc":boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  */  
   "IncludeListValueDescriptionInShortDesc":boolean,
      /**  Used for setting Epi Shape to highlight attribute has been used.  */  
   "InUse":boolean,
      /**  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  */  
   "ListValues":string,
      /**  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  */  
   "IsFinalExpression":boolean,
      /**  The UOM used with final expression, used to calculate inventory quantity.  */  
   "FinalExpressionUOM":string,
      /**  List of available Required At codes.  */  
   "RequiredAtAvailableCodes":string,
      /**  List of available Required at descriptions.  */  
   "RequiredAtAvailableDesc":string,
      /**  List of Required At codes selected.  */  
   "RequiredAtSelectedCodes":string,
      /**  List of Required At descriptions selected.  */  
   "RequiredAtSelectedDesc":string,
      /**  Indicates if this calculated field has a Formula Expression already been added or not.  */  
   "IsExpressionDefined":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrClassListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Determines how this class is used: Attributes, Characteristics.  */  
   "AttrClassID":string,
      /**  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  */  
   "Active":boolean,
      /**  Description.  */  
   "Description":string,
      /**  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  */  
   "WebAttrClass":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  */  
   "FullExpression":string,
      /**  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  */  
   "CalculationType":string,
      /**  Determines whether or not this Attribute Class is shared between more than one company.  */  
   "GlobalAttrClassID":boolean,
      /**  Determines whether or not this Attribute Class record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  */  
   "AttrClassType":string,
      /**  Indicates a pre-defined System Attribute Class.  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrClassRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Determines how this class is used: Attributes, Characteristics.  */  
   "AttrClassID":string,
      /**  Schema name for the related table.  */  
   "RelatedToSchemaName":string,
      /**  Table name for the related table.  */  
   "RelatedToTableName":string,
      /**  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  */  
   "Active":boolean,
      /**  Description.  */  
   "Description":string,
      /**  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  */  
   "WebAttrClass":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  */  
   "FullExpression":string,
      /**  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  */  
   "CalculationType":string,
      /**  Action to be taken when Number of Pieces Tolerance is not adhered to.  Valid values are STOP and NONE.  */  
   "NumberOfPiecesAction":string,
      /**  Acceptable tolerance both negative and positive when calculating Total Quantity from Number of Pieces results in a rounding variance.  */  
   "NumberOfPiecesTolerance":number,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevDecimal01":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  Determines whether or not this Attribute Class is shared between more than one company.  */  
   "GlobalAttrClassID":boolean,
      /**  Determines whether or not this Attribute Class record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  */  
   "AttrClassType":string,
      /**  Indicates a pre-defined System Attribute Class.  */  
   "SystemFlag":boolean,
      /**  Contols when class inventory tracking can be changed.  */  
   "EnableInventoryTracking":boolean,
      /**  Controls when Global checkbox on an Attribute Class should be enabled so it may be modified.  */  
   "EnableGlobalAttrClassID":boolean,
      /**  Indicates if the Dynamic Attribute Class is Global (master or linked)  */  
   "GlbFlag":boolean,
   "EnableWebAttrClass":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param bizType
      @param ds
   */  
export interface ChangeBizType_input{
   bizType:string,
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface ChangeBizType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param usedInPlanning
      @param ds
   */  
export interface ChangeUsedInPlanning_input{
   usedInPlanning:boolean,
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface ChangeUsedInPlanning_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param attributeID
   */  
export interface CheckAttributeID_input{
      /**  The AttributeID to check.  */  
   attributeID:string,
}

export interface CheckAttributeID_output{
parameters : {
      /**  output parameters  */  
   promptMessage:string,
   activeFlag:boolean,
}
}

   /** Required : 
      @param attrClassID
   */  
export interface DeleteByID_input{
   attrClassID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param sourceDynAttrClassID
      @param targetDynAttrClassID
      @param targetDynAttrClassDescription
      @param targetRelatedToTableName
   */  
export interface DuplicateDynAttrClass_input{
   sourceDynAttrClassID:string,
   targetDynAttrClassID:string,
   targetDynAttrClassDescription:string,
   targetRelatedToTableName:string,
}

export interface DuplicateDynAttrClass_output{
   returnObj:Erp_Tablesets_DynAttrClassTableset[],
}

export interface Erp_Tablesets_DynAttrClassDtlListValRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ID of parent attribute class.  */  
   AttrClassID:string,
      /**  Unique ID of attribute for this class.  */  
   AttributeID:string,
      /**  Code value that will be store in the DynAttrValue.  */  
   Code:string,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
      /**  Description of list value that will show in list.  */  
   Description:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates if the Attribute List Value is Active. Default is false.  Once Active, the system will allow it to be used.  */  
   Active:boolean,
      /**  Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).  */  
   PlanningConvOperator:string,
      /**  Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.  */  
   PlanningConvFactor:number,
      /**  Indicates when this list value will be available for selecting during entry: Planning, Supply, Demand.  */  
   WhereAvailable:number,
      /**  Theoretical UOM used by MRP for conversions to the related Actual quantity.  */  
   TheoreticalUOM:string,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevDecimal01:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrClassDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ID of parent Attribute Class  */  
   AttrClassID:string,
      /**  Unique ID of attribute for this class  */  
   AttributeID:string,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
      /**  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  */  
   Active:boolean,
      /**  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  */  
   Description:string,
      /**  Date type for this attribute field.  */  
   FieldDataType:string,
      /**  Format for the given date type for this attribute field.  */  
   FieldFormat:string,
      /**  Defines the field lablel for this attribute.  */  
   FieldLabel:string,
      /**  The value that determines the increments used when linked to a numeric input.  */  
   IncrPrec:number,
      /**  Initial character value.  */  
   InitialCharacter:string,
      /**  Initial date value.  */  
   InitialDate:string,
      /**  Initial decimal value.  */  
   InitialDecimal:number,
      /**  Initial integer value.  */  
   InitialInteger:number,
      /**  Initial logical value.  */  
   InitialLogical:boolean,
      /**  The user defined maximum acceptable value when linked to a date input.  */  
   MaxDate:string,
      /**  The user defined maximum acceptable value when linked to a decimal input.  */  
   MaxDecimal:number,
      /**  The user defined maximum acceptable value when linked to an integer input.  */  
   MaxInteger:number,
      /**  The user defined minimum acceptable value when linked to a date input.  */  
   MinDate:string,
      /**  The user defined minimum acceptable value when linked to a decimal input.  */  
   MinDecimal:number,
      /**  The user defined minimum acceptable value when linked to an integer input.  */  
   MinInteger:number,
      /**  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  */  
   WebAttribute:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Further defines the business use of the field, valid values are "Quantity,UOM"  */  
   BizType:string,
      /**  Attribute ID of related UOM linked to quantity.  */  
   UOMAttributeID:string,
      /**  Controls the order attributes are displayed and updated.  */  
   SortSeq:number,
      /**  If attribute is used in planning.  */  
   UsedInPlanning:boolean,
      /**  Indicated this attribute will be used as a calculated field.  */  
   IsCalculated:boolean,
      /**  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  */  
   PlanningBaseUOM:string,
      /**  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  */  
   PlanningType:string,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevDecimal01:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  The actual transaction value for the attribute set.  */  
   IsActual:boolean,
      /**  Indicates if this attribute will be visible in attribute entry.  */  
   IsViewable:boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  */  
   IsReadOnly:boolean,
      /**  Resuable Attribute linked to this class attribute.  */  
   MasterDtlLinked:string,
      /**  Indicates if changes made to Reusable Attributes are synch to this class attribute.  */  
   MasterDtlSync:boolean,
      /**  Indicates a pre-defined System Attribute Class.  */  
   SystemFlag:boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  */  
   IncludeListValueCodeInShortDesc:boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  */  
   IncludeListValueDescriptionInShortDesc:boolean,
      /**  Used for setting Epi Shape to highlight attribute has been used.  */  
   InUse:boolean,
      /**  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  */  
   ListValues:string,
      /**  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  */  
   IsFinalExpression:boolean,
      /**  The UOM used with final expression, used to calculate inventory quantity.  */  
   FinalExpressionUOM:string,
      /**  List of available Required At codes.  */  
   RequiredAtAvailableCodes:string,
      /**  List of available Required at descriptions.  */  
   RequiredAtAvailableDesc:string,
      /**  List of Required At codes selected.  */  
   RequiredAtSelectedCodes:string,
      /**  List of Required At descriptions selected.  */  
   RequiredAtSelectedDesc:string,
      /**  Indicates if this calculated field has a Formula Expression already been added or not.  */  
   IsExpressionDefined:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrClassListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Determines how this class is used: Attributes, Characteristics.  */  
   AttrClassID:string,
      /**  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  */  
   Active:boolean,
      /**  Description.  */  
   Description:string,
      /**  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  */  
   WebAttrClass:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  */  
   FullExpression:string,
      /**  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  */  
   CalculationType:string,
      /**  Determines whether or not this Attribute Class is shared between more than one company.  */  
   GlobalAttrClassID:boolean,
      /**  Determines whether or not this Attribute Class record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  */  
   AttrClassType:string,
      /**  Indicates a pre-defined System Attribute Class.  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrClassListTableset{
   DynAttrClassList:Erp_Tablesets_DynAttrClassListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DynAttrClassRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Determines how this class is used: Attributes, Characteristics.  */  
   AttrClassID:string,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
      /**  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  */  
   Active:boolean,
      /**  Description.  */  
   Description:string,
      /**  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  */  
   WebAttrClass:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  */  
   FullExpression:string,
      /**  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  */  
   CalculationType:string,
      /**  Action to be taken when Number of Pieces Tolerance is not adhered to.  Valid values are STOP and NONE.  */  
   NumberOfPiecesAction:string,
      /**  Acceptable tolerance both negative and positive when calculating Total Quantity from Number of Pieces results in a rounding variance.  */  
   NumberOfPiecesTolerance:number,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevDecimal01:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  Determines whether or not this Attribute Class is shared between more than one company.  */  
   GlobalAttrClassID:boolean,
      /**  Determines whether or not this Attribute Class record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  */  
   AttrClassType:string,
      /**  Indicates a pre-defined System Attribute Class.  */  
   SystemFlag:boolean,
      /**  Contols when class inventory tracking can be changed.  */  
   EnableInventoryTracking:boolean,
      /**  Controls when Global checkbox on an Attribute Class should be enabled so it may be modified.  */  
   EnableGlobalAttrClassID:boolean,
      /**  Indicates if the Dynamic Attribute Class is Global (master or linked)  */  
   GlbFlag:boolean,
   EnableWebAttrClass:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrClassTableset{
   DynAttrClass:Erp_Tablesets_DynAttrClassRow[],
   DynAttrClassDtl:Erp_Tablesets_DynAttrClassDtlRow[],
   DynAttrClassDtlListVal:Erp_Tablesets_DynAttrClassDtlListValRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RelatedToTableNameListRow{
   Company:string,
   RelatedToSchemaName:string,
   RelatedToTableName:string,
   DisplaySeq:number,
      /**  Display name for RelatedToTableName  */  
   DspRelatedToTableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RelatedToTableNameListTableset{
   RelatedToTableNameList:Erp_Tablesets_RelatedToTableNameListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtDynAttrClassTableset{
   DynAttrClass:Erp_Tablesets_DynAttrClassRow[],
   DynAttrClassDtl:Erp_Tablesets_DynAttrClassDtlRow[],
   DynAttrClassDtlListVal:Erp_Tablesets_DynAttrClassDtlListValRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param attrClassID
   */  
export interface GetByID_input{
   attrClassID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DynAttrClassTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DynAttrClassTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DynAttrClassTableset[],
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
   returnObj:Erp_Tablesets_DynAttrClassListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param attrClassID
      @param attributeID
   */  
export interface GetNewDynAttrClassDtlListVal_input{
   ds:Erp_Tablesets_DynAttrClassTableset[],
   attrClassID:string,
   attributeID:string,
}

export interface GetNewDynAttrClassDtlListVal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param ds
      @param attrClassID
   */  
export interface GetNewDynAttrClassDtl_input{
   ds:Erp_Tablesets_DynAttrClassTableset[],
   attrClassID:string,
}

export interface GetNewDynAttrClassDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDynAttrClass_input{
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface GetNewDynAttrClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

export interface GetRelatedToTableNameListFromLandingPage_output{
   returnObj:Erp_Tablesets_RelatedToTableNameListTableset[],
}

export interface GetRelatedToTableNameList_output{
   returnObj:Erp_Tablesets_RelatedToTableNameListTableset[],
}

   /** Required : 
      @param whereClauseDynAttrClass
      @param whereClauseDynAttrClassDtl
      @param whereClauseDynAttrClassDtlListVal
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDynAttrClass:string,
   whereClauseDynAttrClassDtl:string,
   whereClauseDynAttrClassDtlListVal:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DynAttrClassTableset[],
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
      @param attributeID
      @param ds
   */  
export interface OnChangeAttributeID_input{
   attributeID:string,
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface OnChangeAttributeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param newDataType
      @param ds
   */  
export interface OnChangeFieldDataType_input{
      /**  The new data type value.  */  
   newDataType:string,
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface OnChangeFieldDataType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param newRelatedToTableName
      @param ds
   */  
export interface OnChangeRelatedToTableName_input{
      /**  The new RelatedToTableName value.  */  
   newRelatedToTableName:string,
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface OnChangeRelatedToTableName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param attrClassID
   */  
export interface RegenerateAttributeSetHash_input{
   attrClassID:string,
}

export interface RegenerateAttributeSetHash_output{
}

   /** Required : 
      @param ds
   */  
export interface SetDynAttrClassDtlIsExpressionDefined_input{
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface SetDynAttrClassDtlIsExpressionDefined_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDynAttrClassTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDynAttrClassTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

   /** Required : 
      @param newFieldFormat
      @param ds
   */  
export interface ValidateFormat_input{
      /**  newFieldFormat  */  
   newFieldFormat:string,
   ds:Erp_Tablesets_DynAttrClassTableset[],
}

export interface ValidateFormat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassTableset[],
}
}

