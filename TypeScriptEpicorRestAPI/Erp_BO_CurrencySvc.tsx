import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CurrencySvc
// Description: Currency Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/$metadata", {
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
   Description: Get Currencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Currencies
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyRow
   */  
export function get_Currencies(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Currencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Currencies(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Currency item
   Description: Calls GetByID to retrieve the Currency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Currency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   */  
export function get_Currencies_Company_CurrencyCode(Company:string, CurrencyCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Currency for the service
   Description: Calls UpdateExt to update Currency. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Currency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Currencies_Company_CurrencyCode(Company:string, CurrencyCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")", {
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
   Summary: Call UpdateExt to delete Currency item
   Description: Call UpdateExt to delete Currency item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Currency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Currencies_Company_CurrencyCode(Company:string, CurrencyCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")", {
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
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_Currencies_Company_CurrencyCode_EntityGLCs(Company:string, CurrencyCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_Currencies_Company_CurrencyCode_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, CurrencyCode:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CurrencyAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrencyAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyAttchRow
   */  
export function get_Currencies_Company_CurrencyCode_CurrencyAttches(Company:string, CurrencyCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/CurrencyAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CurrencyAttch item
   Description: Calls GetByID to retrieve the CurrencyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrencyAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   */  
export function get_Currencies_Company_CurrencyCode_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company:string, CurrencyCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrencyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrencyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get CurrencyAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrencyAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyAttchRow
   */  
export function get_CurrencyAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrencyAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrencyAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CurrencyAttch item
   Description: Calls GetByID to retrieve the CurrencyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrencyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   */  
export function get_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company:string, CurrencyCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrencyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrencyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CurrencyAttch for the service
   Description: Calls UpdateExt to update CurrencyAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrencyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company:string, CurrencyCode:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CurrencyAttch item
   Description: Call UpdateExt to delete CurrencyAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrencyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company:string, CurrencyCode:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyListRow)
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
export function get_GetRows(whereClauseCurrency:string, whereClauseCurrencyAttch:string, whereClauseEntityGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCurrency!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrency=" + whereClauseCurrency
   }
   if(typeof whereClauseCurrencyAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrencyAttch=" + whereClauseCurrencyAttch
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetRows" + params, {
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
export function get_GetByID(currencyCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof currencyCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "currencyCode=" + currencyCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetByID" + params, {
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
   Summary: Invoke method ConvertCurrAmt
   Description: This method will take the source currency, date, rate group and return the
amount in the target currency
   OperationID: ConvertCurrAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertCurrAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertCurrAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertCurrAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/ConvertCurrAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetCurrencyBase", {
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
   Summary: Invoke method GetCurrencyForLink
   Description: This returns the Currency dataset for linking.
   OperationID: GetCurrencyForLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyForLink(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetCurrencyForLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InvokeLinkSearch
   Description: This method returns the delimited list of glbCurrCode values
   OperationID: InvokeLinkSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvokeLinkSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeLinkSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvokeLinkSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/InvokeLinkSearch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGlbCurrencyList
   Description: This method returns the GlbCurrency dataset based on a delimited list of
GlbCurrCode values passed in.
   OperationID: GetGlbCurrencyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlbCurrencyList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCurrencyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlbCurrencyList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetGlbCurrencyList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportCurrList
   Description: This method returns a list of reporting currency positions and the the currencies
that are currently populating each slot
   OperationID: GetReportCurrList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportCurrList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportCurrList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetReportCurrList", {
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
   Summary: Invoke method GlbCurrenciesExist
   Description: This method checks if GlbCurrency records exist or not.  Can be used
to determine if the option to link/unlink customers is available.
   OperationID: GlbCurrenciesExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlbCurrenciesExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCurrenciesExist(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GlbCurrenciesExist", {
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
   Summary: Invoke method LinkGlbCurrency
   Description: This method performs the actual logic behind linking a currency.  It is run after
the PreLinkGlbCurrency method which determines the Currency Code to link to.
If the Currency Code is for a Currency that already exists, the GlbCurrency information is
translated and then copied to the CurrencyDataSet as an update.
If the Currency Code is for a new Currency, the GlbCurrency information is translated and then
copied to the CurrencyDataSet as an Add.  Until the update method is run on Currency record
the Link process is not completed.
   OperationID: LinkGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbCurrency(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/LinkGlbCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbCurrency2
   Description: This method performs the actual logic behind linking a currency.  It is run after
the PreLinkGlbCurrency method which determines the Currency Code to link to.
If the Currency Code is for a Currency that already exists, the GlbCurrency information is
translated and then copied to the CurrencyDataSet as an update.
If the Currency Code is for a new Currency, the GlbCurrency information is translated and then
copied to the CurrencyDataSet as an Add.  Until the update method is run on Currency record
the Link process is not completed.
   OperationID: LinkGlbCurrency2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbCurrency2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCurrency2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbCurrency2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/LinkGlbCurrency2", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreLinkGlbCurrency
   Description: Linking a GlbCurrency record ties a global record to a new or existing Currency record so
that any changes made to the GlbCurrency record in another company are automatically copied
to any linked Currencies.
This method performs the pre link logic to check of okay to link or get the new currencyid
to create/link to.  Will be run before LinkGlbCurrency which actually creates/updates a
Currency record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkCurrencyID will be defaulted to the GlbCurrencyId field.  It will then
check to see if this ID is available for Use.  If available for use the system will return a
question asking the user if they want to use this number.  If the answer is no, then the user
either needs to select an existing currency's ID to link to or enter a brand new ID.  You will
run this method until the user answer is yes.  Then the LinkGlbCurrency method is called.
   OperationID: PreLinkGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreLinkGlbCurrency(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/PreLinkGlbCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreLinkGlbCurrencyAuto
   Description: This method performs the pre-link validation and logic to link local currency ID automatically when Rate type is linked.
   OperationID: PreLinkGlbCurrencyAuto
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbCurrencyAuto_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbCurrencyAuto_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreLinkGlbCurrencyAuto(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/PreLinkGlbCurrencyAuto", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipGlbCurrency
   Description: This method performs the logic behind the skip option for GlbCurrency
Skip - sets the Skipped flag to true.
If the CurrencyCode field is not blank will error out
   OperationID: SkipGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipGlbCurrency(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/SkipGlbCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlinkGlbCurrency
   Description: This method performs the logic behind the unlink option for GlbCurrency
Unlink - clears the CurrencyCode and CustId field in GlbCurrency.  Returns the Currency DataSet
   OperationID: UnlinkGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlinkGlbCurrency(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/UnlinkGlbCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateMaster
   Description: This method is called instead of the standard Update
   OperationID: UpdateMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMaster(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/UpdateMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method onChangeDecimals
   Description: This method is called when General Decimals number is changed.
   OperationID: onChangeDecimals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/onChangeDecimals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/onChangeDecimals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_onChangeDecimals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/onChangeDecimals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeProcessorNum
   Description: This method is called when Credit Card Processor is changed.
   OperationID: OnChangeProcessorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProcessorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProcessorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeProcessorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/OnChangeProcessorNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetActiveSessionsList
   Description: Look for currently Actctive Sessions.
   OperationID: GetActiveSessionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveSessionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActiveSessionsList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetActiveSessionsList", {
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
   Summary: Invoke method GetRoundRuleList
   Description: This method is called for Round Rules list's building.
   OperationID: GetRoundRuleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRoundRuleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRoundRuleList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetRoundRuleList", {
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
   Summary: Invoke method GetLinkOptsList
   Description: This method is called for LinkOpts list's building.
   OperationID: GetLinkOptsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkOptsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLinkOptsList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetLinkOptsList", {
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
   Summary: Invoke method GetNewCurrency
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrency(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetNewCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCurrencyAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrencyAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrencyAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrencyAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrencyAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetNewCurrencyAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrencyAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrencyListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrencyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow[],
}

export interface Erp_Tablesets_CurrencyAttchRow{
   "Company":string,
   "CurrencyCode":string,
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

export interface Erp_Tablesets_CurrencyListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Description of the currency  */  
   "CurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyID":string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   "DecimalsGeneral":number,
      /**  Indicates if the currency is active  */  
   "Inactive":boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   "DecimalsPrice":number,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   "DecimalsCost":number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "BaseCurr":boolean,
      /**  Indicates if this is a reporting currency  */  
   "ReportCurr":boolean,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   "ReportCurrPos":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CurrencyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Description of the currency  */  
   "CurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "DocumentDesc":string,
      /**  Notes the about the Currency.  */  
   "Note":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrName":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyID":string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   "DecimalsGeneral":number,
      /**  Indicates if the currency is active  */  
   "Inactive":boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   "DecimalsPrice":number,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   "MaintRate":boolean,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   "DecimalsCost":number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "BaseCurr":boolean,
      /**  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpUnitPrice":number,
      /**  Indicates if this is a reporting currency  */  
   "ReportCurr":boolean,
      /**  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpUnitTax":number,
      /**  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpExtPrice":number,
      /**  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpExtTax":number,
      /**  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpTotalAmt":number,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   "GlobalCurr":boolean,
      /**  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpTotalTax":number,
      /**  Determines whether or not this currency record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleUnitPrice":number,
      /**  Display factor for exchange rates  */  
   "ScaleFactor":number,
      /**  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleUnitTax":number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "CountryNum":number,
      /**  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleExtPrice":number,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   "ReportCurrPos":number,
      /**  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleExtTax":number,
      /**  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleTotalAmt":number,
      /**  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleTotalTax":number,
      /**  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  */  
   "RoundTolerance":number,
      /**  ISO unique identifier  */  
   "ISONumber":number,
      /**  Store ID for Credit Card Processing  */  
   "StoreID":string,
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
      /**  AGAFIPCode  */  
   "AGAFIPCode":string,
      /**  This Currency Code is used for CRE Processors.  */  
   "ISOCurrCode":string,
      /**  ProcessorNum  */  
   "ProcessorNum":number,
   "BookCurr":boolean,
   "CompanyBase":boolean,
      /**  Name of Country.  */  
   "CountryName":string,
      /**  Control when the Base Currency should be enable.  */  
   "EnableBaseCurr":boolean,
      /**  If currency exist in any transaction the decimals fields should be disables.  */  
   "EnableDecimals":boolean,
      /**  control when the Global Currency field should be enable.  */  
   "EnableGlobalCurr":boolean,
      /**  Control when the GlobalLock field should be enable.  */  
   "EnableGlobalLock":boolean,
      /**  Control when the Inactive field should be enable.  */  
   "EnableInactive":boolean,
      /**  GlbCompany that is linked to this currency  */  
   "GlbCompany":string,
      /**  GlbCompany Name that is linked to this currency  */  
   "GlbCompanyName":string,
      /**  GlbCurrency Description that is linked to this currency  */  
   "GlbCurrDesc":string,
      /**  GlbCurrency Code that is linked to this currency  */  
   "GlbCurrencyCode":string,
      /**  GlbCurrency ID that is linked to this currency  */  
   "GlbCurrencyID":string,
      /**  GlbCurrency Symbol that is linked to this currency  */  
   "GlbCurrSymbol":string,
      /**  Indicates if the Currency is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbCurrencyCode that is linking to this currency  */  
   "GlbLink":string,
   "HasCCInterface":boolean,
      /**  This field store the RowID of the record that is marked as Base Currency.  */  
   "BaseRowRowID":string,
   "BitFlag":number,
   "CountryDescription":string,
   "CreditCardProcessorDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipSourceCurrCode
      @param ipSourceAmt
      @param ipTargetCurrCode
      @param ipRateGrpCode
      @param ipDate
      @param ipTableName
      @param ipFieldName
      @param ipKeyTable
      @param ipKey1
      @param ipKey2
      @param ipKey3
      @param ipKey4
      @param ipKey5
   */  
export interface ConvertCurrAmt_input{
      /**  Source Currency Code  */  
   ipSourceCurrCode:string,
      /**  Delimited List of Amounts to convert  */  
   ipSourceAmt:string,
      /**  Target Currency Code  */  
   ipTargetCurrCode:string,
      /**  Rate Type to get the exchange rate from  */  
   ipRateGrpCode:string,
      /**  Date to use to find the exchange rate  */  
   ipDate:string,
      /**  Used to find any rounding rules, no rounding applied if left blank, if not blank must contain the same amount of entries as the ipSourceAmt  */  
   ipTableName:string,
      /**  Used to find any rounding rules, no rounding applied if left blank, if not blank must contain the same amount of entries as the ipSourceAmt  */  
   ipFieldName:string,
      /**  Used to find the exchange rate tied to a specific record  */  
   ipKeyTable:string,
      /**  Used to find a specific record's Exchange Rate along with ipKeyTable  */  
   ipKey1:string,
      /**  Used to find a specific record's Exchange Rate along with ipKeyTable  */  
   ipKey2:string,
      /**  Used to find a specific record's Exchange Rate along with ipKeyTable  */  
   ipKey3:string,
      /**  Used to find a specific record's Exchange Rate along with ipKeyTable  */  
   ipKey4:string,
      /**  Used to find a specific record's Exchange Rate along with ipKeyTable  */  
   ipKey5:string,
}

export interface ConvertCurrAmt_output{
parameters : {
      /**  output parameters  */  
   opTargetAmt:string,
}
}

   /** Required : 
      @param currencyCode
   */  
export interface DeleteByID_input{
   currencyCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CurrencyAttchRow{
   Company:string,
   CurrencyCode:string,
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

export interface Erp_Tablesets_CurrencyListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   DecimalsGeneral:number,
      /**  Indicates if the currency is active  */  
   Inactive:boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   DecimalsPrice:number,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   DecimalsCost:number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   BaseCurr:boolean,
      /**  Indicates if this is a reporting currency  */  
   ReportCurr:boolean,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   ReportCurrPos:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrencyListTableset{
   CurrencyList:Erp_Tablesets_CurrencyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CurrencyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   DocumentDesc:string,
      /**  Notes the about the Currency.  */  
   Note:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   DecimalsGeneral:number,
      /**  Indicates if the currency is active  */  
   Inactive:boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   DecimalsPrice:number,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   MaintRate:boolean,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   DecimalsCost:number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   BaseCurr:boolean,
      /**  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpUnitPrice:number,
      /**  Indicates if this is a reporting currency  */  
   ReportCurr:boolean,
      /**  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpUnitTax:number,
      /**  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpExtPrice:number,
      /**  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpExtTax:number,
      /**  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpTotalAmt:number,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   GlobalCurr:boolean,
      /**  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpTotalTax:number,
      /**  Determines whether or not this currency record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleUnitPrice:number,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleUnitTax:number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleExtPrice:number,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   ReportCurrPos:number,
      /**  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleExtTax:number,
      /**  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleTotalAmt:number,
      /**  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleTotalTax:number,
      /**  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  */  
   RoundTolerance:number,
      /**  ISO unique identifier  */  
   ISONumber:number,
      /**  Store ID for Credit Card Processing  */  
   StoreID:string,
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
      /**  AGAFIPCode  */  
   AGAFIPCode:string,
      /**  This Currency Code is used for CRE Processors.  */  
   ISOCurrCode:string,
      /**  ProcessorNum  */  
   ProcessorNum:number,
   BookCurr:boolean,
   CompanyBase:boolean,
      /**  Name of Country.  */  
   CountryName:string,
      /**  Control when the Base Currency should be enable.  */  
   EnableBaseCurr:boolean,
      /**  If currency exist in any transaction the decimals fields should be disables.  */  
   EnableDecimals:boolean,
      /**  control when the Global Currency field should be enable.  */  
   EnableGlobalCurr:boolean,
      /**  Control when the GlobalLock field should be enable.  */  
   EnableGlobalLock:boolean,
      /**  Control when the Inactive field should be enable.  */  
   EnableInactive:boolean,
      /**  GlbCompany that is linked to this currency  */  
   GlbCompany:string,
      /**  GlbCompany Name that is linked to this currency  */  
   GlbCompanyName:string,
      /**  GlbCurrency Description that is linked to this currency  */  
   GlbCurrDesc:string,
      /**  GlbCurrency Code that is linked to this currency  */  
   GlbCurrencyCode:string,
      /**  GlbCurrency ID that is linked to this currency  */  
   GlbCurrencyID:string,
      /**  GlbCurrency Symbol that is linked to this currency  */  
   GlbCurrSymbol:string,
      /**  Indicates if the Currency is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbCurrencyCode that is linking to this currency  */  
   GlbLink:string,
   HasCCInterface:boolean,
      /**  This field store the RowID of the record that is marked as Base Currency.  */  
   BaseRowRowID:string,
   BitFlag:number,
   CountryDescription:string,
   CreditCardProcessorDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrencyTableset{
   Currency:Erp_Tablesets_CurrencyRow[],
   CurrencyAttch:Erp_Tablesets_CurrencyAttchRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrencyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   DocumentDesc:string,
      /**  Notes the about the Currency.  */  
   Note:string,
      /**   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  */  
   UnRealLossDiv:string,
      /**   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   UnRealLossDept:string,
      /**   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   UnRealLossChart:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**  Indicates if the currency is active  */  
   Inactive:boolean,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   MaintRate:boolean,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   BaseCurr:boolean,
      /**  Indicates if this is a reporting currency  */  
   ReportCurr:boolean,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   GlobalCurr:boolean,
      /**  Determines whether or not this currency record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Currency Code from Source Company  */  
   GlbCurrencyCode:string,
      /**  Currency ID from Source Company  */  
   GlbCurrencyID:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   Skipped:boolean,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   ReportCurrPos:number,
   DecimalsCost:number,
   DecimalsGeneral:number,
   DecimalsPrice:number,
   RoundMltpExtPrice:number,
   RoundMltpExtTax:number,
   RoundMltpTotalAmt:number,
   RoundMltpTotalTax:number,
   RoundMltpUnitPrice:number,
   RoundMltpUnitTax:number,
   RoundRuleExtPrice:number,
   RoundRuleExtTax:number,
   RoundRuleTotalAmt:number,
   RoundRuleTotalTax:number,
   RoundRuleUnitPrice:number,
   RoundRuleUnitTax:number,
   RoundTolerance:number,
   ISONumber:number,
   StoreID:string,
   RoundMltpAnnualCharge:number,
   RoundMltpPeriodCharge:number,
   RoundRuleAnnualCharge:number,
   RoundRulePeriodCharge:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAFIPCode  */  
   AGAFIPCode:string,
      /**  ISOCurrCode  */  
   ISOCurrCode:string,
      /**  ProcessorNum  */  
   ProcessorNum:number,
      /**  Currency.CurrencyCode to link to (new or existing)  */  
   LinkCurrencyCode:string,
      /**  Currency.CurrencyID to link to (new or existing)  */  
   LinkCurrencyID:string,
      /**  Description of the local Currency  */  
   LocalDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrencyTableset{
   GlbCurrency:Erp_Tablesets_GlbCurrencyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ReportCurrListRow{
   CurrencyID:string,
   CurrencyCode:string,
   CurrDesc:string,
   ReportCurrPos:number,
   ReportSlot:string,
   Company:string,
   CurrSymbol:string,
   Include:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReportCurrListTableset{
   ReportCurrList:Erp_Tablesets_ReportCurrListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCurrencyTableset{
   Currency:Erp_Tablesets_CurrencyRow[],
   CurrencyAttch:Erp_Tablesets_CurrencyAttchRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetActiveSessionsList_output{
parameters : {
      /**  output parameters  */  
   SessionList:string,
}
}

   /** Required : 
      @param currencyCode
   */  
export interface GetByID_input{
   currencyCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CurrencyTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CurrencyTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CurrencyTableset[],
}

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
}
}

   /** Required : 
      @param currencyCode
   */  
export interface GetCurrencyForLink_input{
      /**  Global currency code field on the Glbcurrency record to link  */  
   currencyCode:string,
}

export interface GetCurrencyForLink_output{
   returnObj:Erp_Tablesets_CurrencyTableset[],
}

   /** Required : 
      @param glbCurrCodeList
   */  
export interface GetGlbCurrencyList_input{
      /**  Delimited list of glbCurrCode values  */  
   glbCurrCodeList:string,
}

export interface GetGlbCurrencyList_output{
   returnObj:Erp_Tablesets_GlbCurrencyTableset[],
}

export interface GetLinkOptsList_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_CurrencyListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param currencyCode
   */  
export interface GetNewCurrencyAttch_input{
   ds:Erp_Tablesets_CurrencyTableset[],
   currencyCode:string,
}

export interface GetNewCurrencyAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCurrency_input{
   ds:Erp_Tablesets_CurrencyTableset[],
}

export interface GetNewCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_CurrencyTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
}
}

export interface GetReportCurrList_output{
   returnObj:Erp_Tablesets_ReportCurrListTableset[],
}

export interface GetRoundRuleList_output{
   returnObj:string,
}

   /** Required : 
      @param whereClauseCurrency
      @param whereClauseCurrencyAttch
      @param whereClauseEntityGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCurrency:string,
   whereClauseCurrencyAttch:string,
   whereClauseEntityGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CurrencyTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GlbCurrenciesExist_output{
parameters : {
      /**  output parameters  */  
   GlbCurrenciesExist:boolean,
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
      @param linkOpts
      @param externalCompany
   */  
export interface InvokeLinkSearch_input{
      /**  Link Options  */  
   linkOpts:string,
      /**  External Company  */  
   externalCompany:string,
}

export interface InvokeLinkSearch_output{
      /**  Delimited list of glbCurrCode values  */  
   returnObj:string,
}

   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
      @param ds
      @param ds1
   */  
export interface LinkGlbCurrency2_input{
      /**  Global Company field on the GlbCurrency record to link  */  
   glbCompany:string,
      /**  Global Currency Code field on the GlbCurrency record to link  */  
   glbCurrencyCode:string,
   ds:Erp_Tablesets_CurrencyTableset[],
   ds1:Erp_Tablesets_GlbCurrencyTableset[],
}

export interface LinkGlbCurrency2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
   ds1:Erp_Tablesets_GlbCurrencyTableset[],
}
}

   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
      @param ds
      @param ds1
   */  
export interface LinkGlbCurrency_input{
      /**  Global Company field on the GlbCurrency record to link  */  
   glbCompany:string,
      /**  Global Currency Code field on the GlbCurrency record to link  */  
   glbCurrencyCode:string,
   ds:Erp_Tablesets_GlbCurrencyTableset[],
   ds1:Erp_Tablesets_CurrencyTableset[],
}

export interface LinkGlbCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrencyTableset[],
   ds1:Erp_Tablesets_CurrencyTableset[],
}
}

   /** Required : 
      @param ds
      @param newProcessorNum
   */  
export interface OnChangeProcessorNum_input{
   ds:Erp_Tablesets_CurrencyTableset[],
      /**  Proposed value for ProcessorNum  */  
   newProcessorNum:number,
}

export interface OnChangeProcessorNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
   message:string,
}
}

   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
   */  
export interface PreLinkGlbCurrencyAuto_input{
      /**  Global Company field on the GlbCurrency record to link  */  
   glbCompany:string,
      /**  Global Currency Code field on the GlbCurrency record to link  */  
   glbCurrencyCode:string,
}

export interface PreLinkGlbCurrencyAuto_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
      @param ds
   */  
export interface PreLinkGlbCurrency_input{
      /**  Global Company field on the GlbCurrency record to link  */  
   glbCompany:string,
      /**  Global Currency Code field on the GlbCurrency record to link  */  
   glbCurrencyCode:string,
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}

export interface PreLinkGlbCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrencyTableset[],
   vMessage:string,
}
}

   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
      @param ds
   */  
export interface SkipGlbCurrency_input{
      /**  Global Company field on the GlbCurrency record to skip  */  
   glbCompany:string,
      /**  Global CurrencyCode field on the GlbCurrency record to skip  */  
   glbCurrencyCode:string,
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}

export interface SkipGlbCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}
}

   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
      @param ds
   */  
export interface UnlinkGlbCurrency_input{
      /**  Global Company field on the GlbCurrency record to unlink  */  
   glbCompany:string,
      /**  Global CurrencyCode field on the GlbCurrency record to unlink  */  
   glbCurrencyCode:string,
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}

export interface UnlinkGlbCurrency_output{
   returnObj:Erp_Tablesets_CurrencyTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCurrencyTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCurrencyTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateMaster_input{
   ds:Erp_Tablesets_CurrencyTableset[],
}

export interface UpdateMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
   UpdateMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CurrencyTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
}
}

   /** Required : 
      @param ds
      @param fromUpd
      @param generalDecimals
   */  
export interface onChangeDecimals_input{
   ds:Erp_Tablesets_CurrencyTableset[],
      /**  If is coming from Update  */  
   fromUpd:boolean,
      /**  Decimals to be changed  */  
   generalDecimals:number,
}

export interface onChangeDecimals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyTableset[],
   message:string,
}
}

