import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PlantFromSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/$metadata", {
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
   Description: Get PlantFromSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantFromSearches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantRow
   */  
export function get_PlantFromSearches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantFromSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantFromSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantFromSearch item
   Description: Calls GetByID to retrieve the PlantFromSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantFromSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantRow
   */  
export function get_PlantFromSearches_Company_Plant(Company:string, Plant:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantFromSearch for the service
   Description: Calls UpdateExt to update PlantFromSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantFromSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantFromSearches_Company_Plant(Company:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete PlantFromSearch item
   Description: Call UpdateExt to delete PlantFromSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantFromSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantFromSearches_Company_Plant(Company:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")", {
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
   Description: Get PlantEGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantEGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantEGLCRow
   */  
export function get_PlantFromSearches_Company_Plant_PlantEGLCs(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantEGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantEGLC item
   Description: Calls GetByID to retrieve the PlantEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantEGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   */  
export function get_PlantFromSearches_Company_Plant_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, Plant:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlantAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantAttchRow
   */  
export function get_PlantFromSearches_Company_Plant_PlantAttches(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantAttch item
   Description: Calls GetByID to retrieve the PlantAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   */  
export function get_PlantFromSearches_Company_Plant_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PlantEGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantEGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantEGLCRow
   */  
export function get_PlantEGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantEGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantEGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantEGLC item
   Description: Calls GetByID to retrieve the PlantEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantEGLC
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   */  
export function get_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantEGLC for the service
   Description: Calls UpdateExt to update PlantEGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantEGLC
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete PlantEGLC item
   Description: Call UpdateExt to delete PlantEGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantEGLC
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
export function delete_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get PlantAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantAttchRow
   */  
export function get_PlantAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantAttch item
   Description: Calls GetByID to retrieve the PlantAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   */  
export function get_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantAttch for the service
   Description: Calls UpdateExt to update PlantAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PlantAttch item
   Description: Call UpdateExt to delete PlantAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantListRow)
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
export function get_GetRows(whereClausePlant:string, whereClausePlantAttch:string, whereClausePlantEGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePlant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlant=" + whereClausePlant
   }
   if(typeof whereClausePlantAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantAttch=" + whereClausePlantAttch
   }
   if(typeof whereClausePlantEGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantEGLC=" + whereClausePlantEGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/GetRows" + params, {
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
export function get_GetByID(plant:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPlantAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/GetNewPlantAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantEGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantEGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantEGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantEGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantEGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/GetNewPlantEGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantEGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantRow[],
}

export interface Erp_Tablesets_PlantAttchRow{
   "Company":string,
   "Plant":string,
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

export interface Erp_Tablesets_PlantEGLCRow{
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
      /**  Plant  */  
   "Plant":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  The Site name. Used on shipping reports.  */  
   "Name":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  The Site name. Used on shipping reports.  */  
   "Name":string,
      /**  Site address line 1.  */  
   "Address1":string,
      /**  Site address line 2.  */  
   "Address2":string,
      /**  Site address line 3.  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Main phone number of the Site.  */  
   "PhoneNum":string,
      /**  Main fax number of the Site.  */  
   "FaxNum":string,
      /**  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  */  
   "CommentText":string,
      /**  Number of days early that a supply source (Job or PO) can be without MRP suggesting to postpone the supply.  */  
   "PlanningExceptionDays":number,
      /**  Intrastat Region  */  
   "ISRegion":string,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   "PlantCostID":string,
      /**  Lead Time added to the mfg item to determine the start date.  */  
   "PrepTime":number,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   "KitTime":number,
      /**  If checked, then Transfer Orders will be created when the requirement is marked as "firm".  */  
   "ReqTransferHeader":boolean,
      /**  Identifies the default Production Calendar for this Site.   If this equals "", then the ProdCal record is the Company level production calendar.  */  
   "CalendarID":string,
      /**  Transfer Shipment entry action to a Transfer Order.  Valid values are "WARN", "STOP" or "NONE" .  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the shipment and transfer request does not have a header.  STOP means that the request cannot be added to the shipment.  NONE allows the request to be added to the shipment with no warnings.  */  
   "AllowShipAction":string,
      /**  Number of days before a sugestion is automatically converted to a firmed requirement.  */  
   "AutoConfirmWindow":number,
      /**  When this field is checked then if transfer orders are being created automatically then each suggestion will create a separate transfer order  */  
   "SingleLineOrder":boolean,
      /**  Maximum Operation Start Delay  */  
   "MaxOpStartDelay":number,
      /**  Maximum Operation Length  */  
   "MaxOpLength":number,
      /**  Default Station ID for the Site  */  
   "DefStationID":string,
      /**  Number of days to the end of the finite horizon window  */  
   "FiniteHorz":number,
      /**  Used by MRP.  */  
   "NextUnfirmJob":string,
      /**  Used by MRP.  */  
   "NextUnfirmTFLine":string,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  Number of days to the beginning of the rough cut scheduling horizon window  */  
   "RCutHorz":number,
      /**  Include lead time in manufacturing lead time calculation  */  
   "IncLeadTime":boolean,
      /**  Include transfer lead time in manufacturing lead time calculation  */  
   "IncTransLeadTime":boolean,
      /**  Include receive time in manufacturing lead time calculation  */  
   "IncReceiveTime":boolean,
      /**  Include kit time in manufacturing lead time calculation  */  
   "IncKitTime":boolean,
      /**  Include rough cut parameters in manufacturing lead time calculation  */  
   "IncRCParams":boolean,
      /**  Defines the number of days from the current date the scheduling uses to create job records within the Shop Load table.  */  
   "OverloadHorz":number,
      /**   Determines if the start-to-start job operation offset will be used for production or setup time.  If setup

is chosen, a secondary operation with a start to start relationship will schedule setup to begin xxx 

minutes (defined in the operation) after the production starts on the primary operation.  If production is 

chosen then the production time of the secondary operation will be scheduled to start xxx minutes after the 

production starts on the primary operation.  */  
   "SchedulingSendAhead":string,
      /**  Unfirm Series Horizon  */  
   "UnfirmSeriesHorizon":number,
      /**  AutoFirmHorizon  */  
   "AutoFirmHorizon":number,
      /**  Name of the person responsible for delivery  */  
   "ManagerName":string,
      /**  Branch ID (Used Primary for Thailand Localization)  */  
   "BranchID":string,
      /**  Pertains to Maintenance Management. Site which performs Equipment Maintenance for the this Site.  Note; Maintenance will be allowed in Equipments Site or MaintSite of it's Site.  */  
   "MaintPlant":string,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Site Description 1  */  
   "SiteDesc1":string,
      /**  Site Description 2  */  
   "SiteDesc2":string,
      /**  Site Type: 0-Normal, 2-Main Site, 3-Sub Site, 5-Consolidated  */  
   "SiteType":string,
      /**  Business Type Code  */  
   "BusinessTypeCode":string,
      /**  Business Type Description 1  */  
   "BusTypeDesc1":string,
      /**  Business Type Description 2  */  
   "BusTypeDesc2":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGDefaultInvoicingPoint  */  
   "AGDefaultInvoicingPoint":string,
      /**  It will force the times to be Start to Start when scheduling this kind of operations.  */  
   "ForceSSTime":boolean,
      /**  It will force the times to be Finish to Finish when scheduling this kind of operations  */  
   "ForceFFTime":boolean,
      /**  Within the leadtime window (MRP Start Date + Lead Time) use Lead Time Days of supply logic in place of standard days of supply  */  
   "UseLeadTimeDOS":boolean,
      /**  Within the lead time window, allow consumption of minimum qty until below safety  */  
   "AllowMinQty":boolean,
      /**  It will allow the user to move the job in regardless of material constraints and Subcontract PO?s  */  
   "IgnoreMtlConstraints":boolean,
      /**  AGProvinceCode  */  
   "AGProvinceCode":string,
      /**  AGLocationCode  */  
   "AGLocationCode":string,
      /**  AGNeighborhood  */  
   "AGNeighborhood":string,
      /**  AGStreet  */  
   "AGStreet":string,
      /**  AGStreetNumber  */  
   "AGStreetNumber":string,
      /**  AGExtraStreetNumber  */  
   "AGExtraStreetNumber":string,
      /**  AGFloor  */  
   "AGFloor":string,
      /**  AGApartment  */  
   "AGApartment":string,
      /**  MXMunicipio  */  
   "MXMunicipio":string,
      /**  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  */  
   "MaxLateDaysPORel":number,
      /**  Obsolete  */  
   "INECCNumber":string,
      /**  Obsolete  */  
   "INExciseRange":string,
      /**  Obsolete  */  
   "INExciseDivision":string,
      /**  Obsolete  */  
   "INExCommissionRate":string,
      /**  INTINNumber  */  
   "INTINNumber":string,
      /**  Obsolete  */  
   "INCSTNumber":string,
      /**  Obsolete  */  
   "INSTRegistration":string,
      /**  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  */  
   "UseSchedulingMultiJob":boolean,
      /**  Will allow to auto load all child jobs related to the selected job at the Job Scheduling Board.  */  
   "AutoLoadChildJobs":boolean,
      /**  Will allow to auto load all parent jobs related to the selected job at the Job Scheduling Board.  */  
   "AutoLoadParentJobs":boolean,
      /**  Indicate to schedule engine to get the final date of the parent job and do backwards all the group of jobs to minimize gaps.  */  
   "MinimizeWIP":boolean,
      /**  Time Zone of the site.  */  
   "TimeZoneID":string,
      /**  Not used.  */  
   "TimeZoneAdjustForDST":boolean,
      /**  SyncReqBy  */  
   "SyncReqBy":boolean,
      /**  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  */  
   "ACWPercentage":number,
      /**  It is the time used for schedule engine when scheduling backwards automatically. In some screens it is just a default and can be modified before scheduling.  */  
   "BWSchedStartTime":number,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  Determines if the Plant has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  Determines the schedule direction that will default when manually scheduling a job. The following screens will be impacted by this setting: Job Entry, Service Job Entry, Maintenance Job Entry, Job Scheduling Board, Multi Resource Scheduling Board, Resource Scheduling Board, Job Manager, Project Entry.  */  
   "SchedulingDirection":string,
      /**  US1099PayersTIN  */  
   "US1099PayersTIN":string,
      /**  US1099NameControl  */  
   "US1099NameControl":string,
      /**  US1099OfficeCode  */  
   "US1099OfficeCode":string,
      /**  US1099ContactPerson  */  
   "US1099ContactPerson":string,
      /**  US1099EmailAddress  */  
   "US1099EMailAddress":string,
      /**  US1099FaxNum  */  
   "US1099FaxNum":string,
      /**  US1099PhoneNum  */  
   "US1099PhoneNum":string,
      /**  US1099TransControlCode  */  
   "US1099TransControlCode":string,
      /**  US1099Name1  */  
   "US1099Name1":string,
      /**  US1099Name2  */  
   "US1099Name2":string,
      /**  US1099Address1  */  
   "US1099Address1":string,
      /**  US1099Address2  */  
   "US1099Address2":string,
      /**  US1099Address3  */  
   "US1099Address3":string,
      /**  US1099City  */  
   "US1099City":string,
      /**  US1099State  */  
   "US1099State":string,
      /**  US1099ZIP  */  
   "US1099ZIP":string,
      /**  TaxID  */  
   "TaxID":string,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
      /**  Reason code for cost code change.  */  
   "ReasonCode":string,
      /**  Reason code required flag.  */  
   "ReasonReq":boolean,
      /**  Reason type  */  
   "ReasonType":string,
      /**  Indicates if the scheduling logic in the system is not used because a third party scheduling.  */  
   "Use3rdPartySched":boolean,
      /**  Reason Code Description  */  
   "ReasonCodeDescription":string,
      /**  Background color for site (Kinetic UI).  */  
   "KineticColor":string,
   "LogoFileName":string,
   "LogoImageContent":string,
   "BitFlag":number,
   "AGLocationDescription":string,
   "AGProvinceCodeDescription":string,
   "CalendarIDDescription":string,
   "CompanySendToFSA":boolean,
   "CountryNumDescription":string,
   "MaintPlantName":string,
   "PlantCostDescription":string,
   "XbSystSiteIsLegalEntity":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_PlantAttchRow{
   Company:string,
   Plant:string,
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

export interface Erp_Tablesets_PlantEGLCRow{
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
      /**  Plant  */  
   Plant:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  The Site name. Used on shipping reports.  */  
   Name:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantListTableset{
   PlantList:Erp_Tablesets_PlantListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PlantRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  The Site name. Used on shipping reports.  */  
   Name:string,
      /**  Site address line 1.  */  
   Address1:string,
      /**  Site address line 2.  */  
   Address2:string,
      /**  Site address line 3.  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Main phone number of the Site.  */  
   PhoneNum:string,
      /**  Main fax number of the Site.  */  
   FaxNum:string,
      /**  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  */  
   CommentText:string,
      /**  Number of days early that a supply source (Job or PO) can be without MRP suggesting to postpone the supply.  */  
   PlanningExceptionDays:number,
      /**  Intrastat Region  */  
   ISRegion:string,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   PlantCostID:string,
      /**  Lead Time added to the mfg item to determine the start date.  */  
   PrepTime:number,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   KitTime:number,
      /**  If checked, then Transfer Orders will be created when the requirement is marked as "firm".  */  
   ReqTransferHeader:boolean,
      /**  Identifies the default Production Calendar for this Site.   If this equals "", then the ProdCal record is the Company level production calendar.  */  
   CalendarID:string,
      /**  Transfer Shipment entry action to a Transfer Order.  Valid values are "WARN", "STOP" or "NONE" .  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the shipment and transfer request does not have a header.  STOP means that the request cannot be added to the shipment.  NONE allows the request to be added to the shipment with no warnings.  */  
   AllowShipAction:string,
      /**  Number of days before a sugestion is automatically converted to a firmed requirement.  */  
   AutoConfirmWindow:number,
      /**  When this field is checked then if transfer orders are being created automatically then each suggestion will create a separate transfer order  */  
   SingleLineOrder:boolean,
      /**  Maximum Operation Start Delay  */  
   MaxOpStartDelay:number,
      /**  Maximum Operation Length  */  
   MaxOpLength:number,
      /**  Default Station ID for the Site  */  
   DefStationID:string,
      /**  Number of days to the end of the finite horizon window  */  
   FiniteHorz:number,
      /**  Used by MRP.  */  
   NextUnfirmJob:string,
      /**  Used by MRP.  */  
   NextUnfirmTFLine:string,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  Number of days to the beginning of the rough cut scheduling horizon window  */  
   RCutHorz:number,
      /**  Include lead time in manufacturing lead time calculation  */  
   IncLeadTime:boolean,
      /**  Include transfer lead time in manufacturing lead time calculation  */  
   IncTransLeadTime:boolean,
      /**  Include receive time in manufacturing lead time calculation  */  
   IncReceiveTime:boolean,
      /**  Include kit time in manufacturing lead time calculation  */  
   IncKitTime:boolean,
      /**  Include rough cut parameters in manufacturing lead time calculation  */  
   IncRCParams:boolean,
      /**  Defines the number of days from the current date the scheduling uses to create job records within the Shop Load table.  */  
   OverloadHorz:number,
      /**   Determines if the start-to-start job operation offset will be used for production or setup time.  If setup

is chosen, a secondary operation with a start to start relationship will schedule setup to begin xxx 

minutes (defined in the operation) after the production starts on the primary operation.  If production is 

chosen then the production time of the secondary operation will be scheduled to start xxx minutes after the 

production starts on the primary operation.  */  
   SchedulingSendAhead:string,
      /**  Unfirm Series Horizon  */  
   UnfirmSeriesHorizon:number,
      /**  AutoFirmHorizon  */  
   AutoFirmHorizon:number,
      /**  Name of the person responsible for delivery  */  
   ManagerName:string,
      /**  Branch ID (Used Primary for Thailand Localization)  */  
   BranchID:string,
      /**  Pertains to Maintenance Management. Site which performs Equipment Maintenance for the this Site.  Note; Maintenance will be allowed in Equipments Site or MaintSite of it's Site.  */  
   MaintPlant:string,
      /**  Site Code  */  
   SiteCode:string,
      /**  Site Description 1  */  
   SiteDesc1:string,
      /**  Site Description 2  */  
   SiteDesc2:string,
      /**  Site Type: 0-Normal, 2-Main Site, 3-Sub Site, 5-Consolidated  */  
   SiteType:string,
      /**  Business Type Code  */  
   BusinessTypeCode:string,
      /**  Business Type Description 1  */  
   BusTypeDesc1:string,
      /**  Business Type Description 2  */  
   BusTypeDesc2:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGDefaultInvoicingPoint  */  
   AGDefaultInvoicingPoint:string,
      /**  It will force the times to be Start to Start when scheduling this kind of operations.  */  
   ForceSSTime:boolean,
      /**  It will force the times to be Finish to Finish when scheduling this kind of operations  */  
   ForceFFTime:boolean,
      /**  Within the leadtime window (MRP Start Date + Lead Time) use Lead Time Days of supply logic in place of standard days of supply  */  
   UseLeadTimeDOS:boolean,
      /**  Within the lead time window, allow consumption of minimum qty until below safety  */  
   AllowMinQty:boolean,
      /**  It will allow the user to move the job in regardless of material constraints and Subcontract PO?s  */  
   IgnoreMtlConstraints:boolean,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGLocationCode  */  
   AGLocationCode:string,
      /**  AGNeighborhood  */  
   AGNeighborhood:string,
      /**  AGStreet  */  
   AGStreet:string,
      /**  AGStreetNumber  */  
   AGStreetNumber:string,
      /**  AGExtraStreetNumber  */  
   AGExtraStreetNumber:string,
      /**  AGFloor  */  
   AGFloor:string,
      /**  AGApartment  */  
   AGApartment:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  */  
   MaxLateDaysPORel:number,
      /**  Obsolete  */  
   INECCNumber:string,
      /**  Obsolete  */  
   INExciseRange:string,
      /**  Obsolete  */  
   INExciseDivision:string,
      /**  Obsolete  */  
   INExCommissionRate:string,
      /**  INTINNumber  */  
   INTINNumber:string,
      /**  Obsolete  */  
   INCSTNumber:string,
      /**  Obsolete  */  
   INSTRegistration:string,
      /**  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  */  
   UseSchedulingMultiJob:boolean,
      /**  Will allow to auto load all child jobs related to the selected job at the Job Scheduling Board.  */  
   AutoLoadChildJobs:boolean,
      /**  Will allow to auto load all parent jobs related to the selected job at the Job Scheduling Board.  */  
   AutoLoadParentJobs:boolean,
      /**  Indicate to schedule engine to get the final date of the parent job and do backwards all the group of jobs to minimize gaps.  */  
   MinimizeWIP:boolean,
      /**  Time Zone of the site.  */  
   TimeZoneID:string,
      /**  Not used.  */  
   TimeZoneAdjustForDST:boolean,
      /**  SyncReqBy  */  
   SyncReqBy:boolean,
      /**  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  */  
   ACWPercentage:number,
      /**  It is the time used for schedule engine when scheduling backwards automatically. In some screens it is just a default and can be modified before scheduling.  */  
   BWSchedStartTime:number,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Determines if the Plant has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Determines the schedule direction that will default when manually scheduling a job. The following screens will be impacted by this setting: Job Entry, Service Job Entry, Maintenance Job Entry, Job Scheduling Board, Multi Resource Scheduling Board, Resource Scheduling Board, Job Manager, Project Entry.  */  
   SchedulingDirection:string,
      /**  US1099PayersTIN  */  
   US1099PayersTIN:string,
      /**  US1099NameControl  */  
   US1099NameControl:string,
      /**  US1099OfficeCode  */  
   US1099OfficeCode:string,
      /**  US1099ContactPerson  */  
   US1099ContactPerson:string,
      /**  US1099EmailAddress  */  
   US1099EMailAddress:string,
      /**  US1099FaxNum  */  
   US1099FaxNum:string,
      /**  US1099PhoneNum  */  
   US1099PhoneNum:string,
      /**  US1099TransControlCode  */  
   US1099TransControlCode:string,
      /**  US1099Name1  */  
   US1099Name1:string,
      /**  US1099Name2  */  
   US1099Name2:string,
      /**  US1099Address1  */  
   US1099Address1:string,
      /**  US1099Address2  */  
   US1099Address2:string,
      /**  US1099Address3  */  
   US1099Address3:string,
      /**  US1099City  */  
   US1099City:string,
      /**  US1099State  */  
   US1099State:string,
      /**  US1099ZIP  */  
   US1099ZIP:string,
      /**  TaxID  */  
   TaxID:string,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
      /**  Reason code for cost code change.  */  
   ReasonCode:string,
      /**  Reason code required flag.  */  
   ReasonReq:boolean,
      /**  Reason type  */  
   ReasonType:string,
      /**  Indicates if the scheduling logic in the system is not used because a third party scheduling.  */  
   Use3rdPartySched:boolean,
      /**  Reason Code Description  */  
   ReasonCodeDescription:string,
      /**  Background color for site (Kinetic UI).  */  
   KineticColor:string,
   LogoFileName:string,
   LogoImageContent:string,
   BitFlag:number,
   AGLocationDescription:string,
   AGProvinceCodeDescription:string,
   CalendarIDDescription:string,
   CompanySendToFSA:boolean,
   CountryNumDescription:string,
   MaintPlantName:string,
   PlantCostDescription:string,
   XbSystSiteIsLegalEntity:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantTableset{
   Plant:Erp_Tablesets_PlantRow[],
   PlantAttch:Erp_Tablesets_PlantAttchRow[],
   PlantEGLC:Erp_Tablesets_PlantEGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPlantTableset{
   Plant:Erp_Tablesets_PlantRow[],
   PlantAttch:Erp_Tablesets_PlantAttchRow[],
   PlantEGLC:Erp_Tablesets_PlantEGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
   */  
export interface GetByID_input{
   plant:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PlantTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PlantTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PlantTableset[],
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
   returnObj:Erp_Tablesets_PlantListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewPlantAttch_input{
   ds:Erp_Tablesets_PlantTableset[],
   plant:string,
}

export interface GetNewPlantAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset[],
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
export interface GetNewPlantEGLC_input{
   ds:Erp_Tablesets_PlantTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewPlantEGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset[],
}
}

   /** Required : 
      @param whereClausePlant
      @param whereClausePlantAttch
      @param whereClausePlantEGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePlant:string,
   whereClausePlantAttch:string,
   whereClausePlantEGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PlantTableset[],
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
   ds:Erp_Tablesets_UpdExtPlantTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPlantTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PlantTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTableset[],
}
}

