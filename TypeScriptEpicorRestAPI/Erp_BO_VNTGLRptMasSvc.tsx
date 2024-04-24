import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.VNTGLRptMasSvc
// Description: VNTGLRptMas service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/$metadata", {
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
   Description: Get VNTGLRptMas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptMas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptMasRow
   */  
export function get_VNTGLRptMas(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VNTGLRptMas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptMa item
   Description: Calls GetByID to retrieve the VNTGLRptMa item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptMa
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
   */  
export function get_VNTGLRptMas_Company_LocalName_Key2(Company:string, LocalName:string, Key2:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VNTGLRptMa for the service
   Description: Calls UpdateExt to update VNTGLRptMa. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptMa
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VNTGLRptMas_Company_LocalName_Key2(Company:string, LocalName:string, Key2:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")", {
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
   Summary: Call UpdateExt to delete VNTGLRptMa item
   Description: Call UpdateExt to delete VNTGLRptMa item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptMa
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VNTGLRptMas_Company_LocalName_Key2(Company:string, LocalName:string, Key2:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")", {
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
   Description: Get VNTGLRptRows items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRows1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowRow
   */  
export function get_VNTGLRptMas_Company_LocalName_Key2_VNTGLRptRows(Company:string, LocalName:string, Key2:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")/VNTGLRptRows", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRow item
   Description: Calls GetByID to retrieve the VNTGLRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRow1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   */  
export function get_VNTGLRptMas_Company_LocalName_Key2_VNTGLRptRows_Company_LocalName_Key2_Key3(Company:string, LocalName:string, Key2:string, Key3:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRows items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRows
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowRow
   */  
export function get_VNTGLRptRows(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VNTGLRptRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRow item
   Description: Calls GetByID to retrieve the VNTGLRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRow
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3(Company:string, LocalName:string, Key2:string, Key3:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VNTGLRptRow for the service
   Description: Calls UpdateExt to update VNTGLRptRow. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRow
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VNTGLRptRows_Company_LocalName_Key2_Key3(Company:string, LocalName:string, Key2:string, Key3:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")", {
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
   Summary: Call UpdateExt to delete VNTGLRptRow item
   Description: Call UpdateExt to delete VNTGLRptRow item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRow
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VNTGLRptRows_Company_LocalName_Key2_Key3(Company:string, LocalName:string, Key2:string, Key3:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")", {
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
   Description: Get VNTGLRptRowAcctCorrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctCorrs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctCorrRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctCorrs(Company:string, LocalName:string, Key2:string, Key3:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctCorrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctCorrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctCorrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctCorr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctCorrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctCorrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAcctObjs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctObjs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctObjRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctObjs(Company:string, LocalName:string, Key2:string, Key3:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctObjs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctObj item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctObj1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAccts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAccts(Company:string, LocalName:string, Key2:string, Key3:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcct item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcct1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAcctSegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctSegs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSegRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSegs(Company:string, LocalName:string, Key2:string, Key3:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSeg1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctSegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctSegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAcctSums items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctSums1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSumRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSums(Company:string, LocalName:string, Key2:string, Key3:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSums", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSum item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSum1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   */  
export function get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRowAcctCorrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctCorrs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctCorrRow
   */  
export function get_VNTGLRptRowAcctCorrs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctCorrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctCorrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctCorrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VNTGLRptRowAcctCorrs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctCorr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   */  
export function get_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctCorrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctCorrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctCorr for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctCorr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctCorr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Summary: Call UpdateExt to delete VNTGLRptRowAcctCorr item
   Description: Call UpdateExt to delete VNTGLRptRowAcctCorr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctCorr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Description: Get VNTGLRptRowAcctObjs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctObjs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctObjRow
   */  
export function get_VNTGLRptRowAcctObjs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctObjs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VNTGLRptRowAcctObjs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctObj item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctObj
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   */  
export function get_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctObj for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctObj. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctObj
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Summary: Call UpdateExt to delete VNTGLRptRowAcctObj item
   Description: Call UpdateExt to delete VNTGLRptRowAcctObj item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctObj
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Description: Get VNTGLRptRowAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAccts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctRow
   */  
export function get_VNTGLRptRowAccts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VNTGLRptRowAccts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcct item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   */  
export function get_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VNTGLRptRowAcct for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Summary: Call UpdateExt to delete VNTGLRptRowAcct item
   Description: Call UpdateExt to delete VNTGLRptRowAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Description: Get VNTGLRptRowAcctSegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctSegs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSegRow
   */  
export function get_VNTGLRptRowAcctSegs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctSegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VNTGLRptRowAcctSegs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSeg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   */  
export function get_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctSegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctSegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctSeg for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctSeg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctSeg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Summary: Call UpdateExt to delete VNTGLRptRowAcctSeg item
   Description: Call UpdateExt to delete VNTGLRptRowAcctSeg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctSeg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Description: Get VNTGLRptRowAcctSums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctSums
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSumRow
   */  
export function get_VNTGLRptRowAcctSums(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctSums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VNTGLRptRowAcctSums(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSum item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   */  
export function get_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VNTGLRptRowAcctSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VNTGLRptRowAcctSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctSum for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctSum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Summary: Call UpdateExt to delete VNTGLRptRowAcctSum item
   Description: Call UpdateExt to delete VNTGLRptRowAcctSum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company:string, LocalName:string, Key2:string, Key3:string, Key4:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptMasListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseVNTGLRptMas:string, whereClauseVNTGLRptRow:string, whereClauseVNTGLRptRowAcctCorr:string, whereClauseVNTGLRptRowAcctObj:string, whereClauseVNTGLRptRowAcct:string, whereClauseVNTGLRptRowAcctSeg:string, whereClauseVNTGLRptRowAcctSum:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseVNTGLRptMas!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVNTGLRptMas=" + whereClauseVNTGLRptMas
   }
   if(typeof whereClauseVNTGLRptRow!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVNTGLRptRow=" + whereClauseVNTGLRptRow
   }
   if(typeof whereClauseVNTGLRptRowAcctCorr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVNTGLRptRowAcctCorr=" + whereClauseVNTGLRptRowAcctCorr
   }
   if(typeof whereClauseVNTGLRptRowAcctObj!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVNTGLRptRowAcctObj=" + whereClauseVNTGLRptRowAcctObj
   }
   if(typeof whereClauseVNTGLRptRowAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVNTGLRptRowAcct=" + whereClauseVNTGLRptRowAcct
   }
   if(typeof whereClauseVNTGLRptRowAcctSeg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVNTGLRptRowAcctSeg=" + whereClauseVNTGLRptRowAcctSeg
   }
   if(typeof whereClauseVNTGLRptRowAcctSum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVNTGLRptRowAcctSum=" + whereClauseVNTGLRptRowAcctSum
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetRows" + params, {
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
export function get_GetByID(localName:string, key2:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof localName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "localName=" + localName
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetList" + params, {
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
   Summary: Invoke method GetDataComboAttributeFont
   Description: <param name="listDataAttributeFont">The list of options for Attribute font </param>
   OperationID: GetDataComboAttributeFont
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboAttributeFont_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataComboAttributeFont(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetDataComboAttributeFont", {
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
   Summary: Invoke method GetDataComboItemValue
   Description: <param name="listDataItemValue">The list of options for Item Value </param>
   OperationID: GetDataComboItemValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboItemValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataComboItemValue(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetDataComboItemValue", {
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
   Summary: Invoke method GetDataComboReportTemplate
   Description: <param name="listDataReportTemplate">The list of options for RowAccountType </param>
   OperationID: GetDataComboReportTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboReportTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataComboReportTemplate(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetDataComboReportTemplate", {
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
   Summary: Invoke method GetDataComboRowAccountType
   Description: <param name="listDataRowAcctType">The list of options for RowAccountType </param>
   OperationID: GetDataComboRowAccountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboRowAccountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataComboRowAccountType(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetDataComboRowAccountType", {
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
   Summary: Invoke method GetNewVNTGLRptMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVNTGLRptMas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetNewVNTGLRptMas", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVNTGLRptRow
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVNTGLRptRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetNewVNTGLRptRow", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVNTGLRptRowAcctCorr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctCorr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctCorr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctCorr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVNTGLRptRowAcctCorr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetNewVNTGLRptRowAcctCorr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVNTGLRptRowAcctObj
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctObj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctObj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctObj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVNTGLRptRowAcctObj(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetNewVNTGLRptRowAcctObj", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVNTGLRptRowAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVNTGLRptRowAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetNewVNTGLRptRowAcct", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVNTGLRptRowAcctSeg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctSeg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctSeg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctSeg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVNTGLRptRowAcctSeg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetNewVNTGLRptRowAcctSeg", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVNTGLRptRowAcctSum
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctSum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctSum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctSum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVNTGLRptRowAcctSum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetNewVNTGLRptRowAcctSum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptMasListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptMasRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctCorrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptRowAcctCorrRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctObjRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptRowAcctObjRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptRowAcctRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSegRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptRowAcctSegRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSumRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptRowAcctSumRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VNTGLRptRowRow[],
}

export interface Erp_Tablesets_VNTGLRptMasListRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Description  */  
   "Description":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "CheckBox06":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VNTGLRptMasRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctCorrRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctObjRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctSegRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctSumRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VNTGLRptRowRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param localName
      @param key2
   */  
export interface DeleteByID_input{
   localName:string,
   key2:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtVNTGLRptMasTableset{
   VNTGLRptMas:Erp_Tablesets_VNTGLRptMasRow[],
   VNTGLRptRow:Erp_Tablesets_VNTGLRptRowRow[],
   VNTGLRptRowAcctCorr:Erp_Tablesets_VNTGLRptRowAcctCorrRow[],
   VNTGLRptRowAcctObj:Erp_Tablesets_VNTGLRptRowAcctObjRow[],
   VNTGLRptRowAcct:Erp_Tablesets_VNTGLRptRowAcctRow[],
   VNTGLRptRowAcctSeg:Erp_Tablesets_VNTGLRptRowAcctSegRow[],
   VNTGLRptRowAcctSum:Erp_Tablesets_VNTGLRptRowAcctSumRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VNTGLRptMasListRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Description  */  
   Description:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Number01:number,
   Number02:number,
   Number03:number,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   ShortChar01:string,
   ShortChar02:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VNTGLRptMasListTableset{
   VNTGLRptMasList:Erp_Tablesets_VNTGLRptMasListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VNTGLRptMasRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   COADescription:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VNTGLRptMasTableset{
   VNTGLRptMas:Erp_Tablesets_VNTGLRptMasRow[],
   VNTGLRptRow:Erp_Tablesets_VNTGLRptRowRow[],
   VNTGLRptRowAcctCorr:Erp_Tablesets_VNTGLRptRowAcctCorrRow[],
   VNTGLRptRowAcctObj:Erp_Tablesets_VNTGLRptRowAcctObjRow[],
   VNTGLRptRowAcct:Erp_Tablesets_VNTGLRptRowAcctRow[],
   VNTGLRptRowAcctSeg:Erp_Tablesets_VNTGLRptRowAcctSegRow[],
   VNTGLRptRowAcctSum:Erp_Tablesets_VNTGLRptRowAcctSumRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VNTGLRptRowAcctCorrRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctObjRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctSegRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VNTGLRptRowAcctSumRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VNTGLRptRowRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param localName
      @param key2
   */  
export interface GetByID_input{
   localName:string,
   key2:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VNTGLRptMasTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VNTGLRptMasTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VNTGLRptMasTableset[],
}

export interface GetDataComboAttributeFont_output{
parameters : {
      /**  output parameters  */  
   listDataAttributeFont:string,
}
}

export interface GetDataComboItemValue_output{
parameters : {
      /**  output parameters  */  
   listDataItemValue:string,
}
}

export interface GetDataComboReportTemplate_output{
parameters : {
      /**  output parameters  */  
   listDataReportTemplate:string,
}
}

export interface GetDataComboRowAccountType_output{
parameters : {
      /**  output parameters  */  
   listDataRowAcctType:string,
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
   returnObj:Erp_Tablesets_VNTGLRptMasListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param localName
   */  
export interface GetNewVNTGLRptMas_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
   localName:string,
}

export interface GetNewVNTGLRptMas_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

   /** Required : 
      @param ds
      @param localName
      @param key2
      @param key3
   */  
export interface GetNewVNTGLRptRowAcctCorr_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
   localName:string,
   key2:string,
   key3:string,
}

export interface GetNewVNTGLRptRowAcctCorr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

   /** Required : 
      @param ds
      @param localName
      @param key2
      @param key3
   */  
export interface GetNewVNTGLRptRowAcctObj_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
   localName:string,
   key2:string,
   key3:string,
}

export interface GetNewVNTGLRptRowAcctObj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

   /** Required : 
      @param ds
      @param localName
      @param key2
      @param key3
   */  
export interface GetNewVNTGLRptRowAcctSeg_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
   localName:string,
   key2:string,
   key3:string,
}

export interface GetNewVNTGLRptRowAcctSeg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

   /** Required : 
      @param ds
      @param localName
      @param key2
      @param key3
   */  
export interface GetNewVNTGLRptRowAcctSum_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
   localName:string,
   key2:string,
   key3:string,
}

export interface GetNewVNTGLRptRowAcctSum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

   /** Required : 
      @param ds
      @param localName
      @param key2
      @param key3
   */  
export interface GetNewVNTGLRptRowAcct_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
   localName:string,
   key2:string,
   key3:string,
}

export interface GetNewVNTGLRptRowAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

   /** Required : 
      @param ds
      @param localName
      @param key2
   */  
export interface GetNewVNTGLRptRow_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
   localName:string,
   key2:string,
}

export interface GetNewVNTGLRptRow_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

   /** Required : 
      @param whereClauseVNTGLRptMas
      @param whereClauseVNTGLRptRow
      @param whereClauseVNTGLRptRowAcctCorr
      @param whereClauseVNTGLRptRowAcctObj
      @param whereClauseVNTGLRptRowAcct
      @param whereClauseVNTGLRptRowAcctSeg
      @param whereClauseVNTGLRptRowAcctSum
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseVNTGLRptMas:string,
   whereClauseVNTGLRptRow:string,
   whereClauseVNTGLRptRowAcctCorr:string,
   whereClauseVNTGLRptRowAcctObj:string,
   whereClauseVNTGLRptRowAcct:string,
   whereClauseVNTGLRptRowAcctSeg:string,
   whereClauseVNTGLRptRowAcctSum:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VNTGLRptMasTableset[],
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
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtVNTGLRptMasTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVNTGLRptMasTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VNTGLRptMasTableset[],
}
}

