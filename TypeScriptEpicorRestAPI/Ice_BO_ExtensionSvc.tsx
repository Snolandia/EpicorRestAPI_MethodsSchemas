import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.ExtensionSvc
// Description: Extensions.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/$metadata", {
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
   Description: Get Extensions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Extensions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRow
   */  
export function get_Extensions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Extensions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Extensions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Extension item
   Description: Calls GetByID to retrieve the Extension item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Extension
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRow
   */  
export function get_Extensions_ExtensionSetID(ExtensionSetID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Extension for the service
   Description: Calls UpdateExt to update Extension. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Extension
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Extensions_ExtensionSetID(ExtensionSetID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")", {
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
   Summary: Call UpdateExt to delete Extension item
   Description: Call UpdateExt to delete Extension item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Extension
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Extensions_ExtensionSetID(ExtensionSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")", {
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
   Description: Get ExtensionSetMappings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionSetMappings1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionSetMappingRow
   */  
export function get_Extensions_ExtensionSetID_ExtensionSetMappings(ExtensionSetID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionSetMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionSetMappings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionSetMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionSetMapping item
   Description: Calls GetByID to retrieve the ExtensionSetMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionSetMapping1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   */  
export function get_Extensions_ExtensionSetID_ExtensionSetMappings_Company_ExtensionSetID(ExtensionSetID:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionSetMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionSetMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ExtensionTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionTables1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableRow
   */  
export function get_Extensions_ExtensionSetID_ExtensionTables(ExtensionSetID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionTable item
   Description: Calls GetByID to retrieve the ExtensionTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTable1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   */  
export function get_Extensions_ExtensionSetID_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID:string, SystemCode:string, DataTableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ExtensionSetMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionSetMappings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionSetMappingRow
   */  
export function get_ExtensionSetMappings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionSetMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionSetMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionSetMappings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtensionSetMappings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionSetMapping item
   Description: Calls GetByID to retrieve the ExtensionSetMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionSetMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   */  
export function get_ExtensionSetMappings_Company_ExtensionSetID(Company:string, ExtensionSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionSetMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionSetMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtensionSetMapping for the service
   Description: Calls UpdateExt to update ExtensionSetMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionSetMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtensionSetMappings_Company_ExtensionSetID(Company:string, ExtensionSetID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")", {
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
   Summary: Call UpdateExt to delete ExtensionSetMapping item
   Description: Call UpdateExt to delete ExtensionSetMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionSetMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtensionSetMappings_Company_ExtensionSetID(Company:string, ExtensionSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")", {
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
   Description: Get ExtensionTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableRow
   */  
export function get_ExtensionTables(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtensionTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionTable item
   Description: Calls GetByID to retrieve the ExtensionTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTable
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   */  
export function get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID:string, SystemCode:string, DataTableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtensionTable for the service
   Description: Calls UpdateExt to update ExtensionTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionTable
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID:string, SystemCode:string, DataTableID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")", {
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
   Summary: Call UpdateExt to delete ExtensionTable item
   Description: Call UpdateExt to delete ExtensionTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionTable
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID:string, SystemCode:string, DataTableID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")", {
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
   Description: Get ExtensionColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionColumns1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionColumnRow
   */  
export function get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionColumns(ExtensionSetID:string, SystemCode:string, DataTableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionColumn item
   Description: Calls GetByID to retrieve the ExtensionColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionColumn1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   */  
export function get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID:string, SystemCode:string, DataTableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ExtensionTableKeys items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionTableKeys1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableKeyRow
   */  
export function get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionTableKeys(ExtensionSetID:string, SystemCode:string, DataTableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionTableKeys", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionTableKey item
   Description: Calls GetByID to retrieve the ExtensionTableKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTableKey1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   */  
export function get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID:string, SystemCode:string, DataTableID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionTableKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionTableKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ExtensionColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionColumns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionColumnRow
   */  
export function get_ExtensionColumns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtensionColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionColumn item
   Description: Calls GetByID to retrieve the ExtensionColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionColumn
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   */  
export function get_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID:string, SystemCode:string, DataTableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtensionColumn for the service
   Description: Calls UpdateExt to update ExtensionColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionColumn
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID:string, SystemCode:string, DataTableID:string, FieldName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")", {
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
   Summary: Call UpdateExt to delete ExtensionColumn item
   Description: Call UpdateExt to delete ExtensionColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionColumn
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID:string, SystemCode:string, DataTableID:string, FieldName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")", {
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
   Description: Get ExtensionTableKeys items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionTableKeys
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableKeyRow
   */  
export function get_ExtensionTableKeys(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionTableKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtensionTableKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionTableKey item
   Description: Calls GetByID to retrieve the ExtensionTableKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTableKey
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   */  
export function get_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID:string, SystemCode:string, DataTableID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionTableKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionTableKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtensionTableKey for the service
   Description: Calls UpdateExt to update ExtensionTableKey. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionTableKey
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID:string, SystemCode:string, DataTableID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete ExtensionTableKey item
   Description: Call UpdateExt to delete ExtensionTableKey item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionTableKey
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID:string, SystemCode:string, DataTableID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")", {
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
   Description: Get ExtensionRelations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionRelations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRelationRow
   */  
export function get_ExtensionRelations(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionRelations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtensionRelations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionRelation item
   Description: Calls GetByID to retrieve the ExtensionRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionRelation
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
   */  
export function get_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtensionRelation for the service
   Description: Calls UpdateExt to update ExtensionRelation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionRelation
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")", {
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
   Summary: Call UpdateExt to delete ExtensionRelation item
   Description: Call UpdateExt to delete ExtensionRelation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionRelation
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")", {
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
   Description: Get ExtensionRelationColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionRelationColumns1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRelationColumnRow
   */  
export function get_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID_ExtensionRelationColumns(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")/ExtensionRelationColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionRelationColumn item
   Description: Calls GetByID to retrieve the ExtensionRelationColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionRelationColumn1
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   */  
export function get_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionRelationColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionRelationColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ExtensionRelationColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionRelationColumns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRelationColumnRow
   */  
export function get_ExtensionRelationColumns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionRelationColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtensionRelationColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtensionRelationColumn item
   Description: Calls GetByID to retrieve the ExtensionRelationColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionRelationColumn
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   */  
export function get_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExtensionRelationColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExtensionRelationColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtensionRelationColumn for the service
   Description: Calls UpdateExt to update ExtensionRelationColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionRelationColumn
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete ExtensionRelationColumn item
   Description: Call UpdateExt to delete ExtensionRelationColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionRelationColumn
      @param ExtensionSetID Desc: ExtensionSetID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataSetID Desc: DataSetID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID:string, SystemCode:string, DataSetID:string, RelationID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionListRow)
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
export function get_GetRows(whereClauseExtension:string, whereClauseExtensionSetMapping:string, whereClauseExtensionTable:string, whereClauseExtensionColumn:string, whereClauseExtensionRelation:string, whereClauseExtensionRelationColumn:string, whereClauseExtensionTableKey:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseExtension!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtension=" + whereClauseExtension
   }
   if(typeof whereClauseExtensionSetMapping!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtensionSetMapping=" + whereClauseExtensionSetMapping
   }
   if(typeof whereClauseExtensionTable!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtensionTable=" + whereClauseExtensionTable
   }
   if(typeof whereClauseExtensionColumn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtensionColumn=" + whereClauseExtensionColumn
   }
   if(typeof whereClauseExtensionRelation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtensionRelation=" + whereClauseExtensionRelation
   }
   if(typeof whereClauseExtensionRelationColumn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtensionRelationColumn=" + whereClauseExtensionRelationColumn
   }
   if(typeof whereClauseExtensionTableKey!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtensionTableKey=" + whereClauseExtensionTableKey
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetRows" + params, {
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
export function get_GetByID(extensionSetID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof extensionSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "extensionSetID=" + extensionSetID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetList" + params, {
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
   Summary: Invoke method GetExtensionSetAssembly
   Description: Returns object representing extension set assembly body with optional debug symbols.
   OperationID: GetExtensionSetAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtensionSetAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtensionSetAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExtensionSetAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetExtensionSetAssembly", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtensionTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtensionTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetNewExtensionTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtensionColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtensionColumn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetNewExtensionColumn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtensionTableKey
   Description: Creates a new pk row for the extension table
   OperationID: GetNewExtensionTableKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionTableKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionTableKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtensionTableKey(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetNewExtensionTableKey", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetupPeerTable
   Description: Create structure for peer table - primary key and relationship
   OperationID: SetupPeerTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetupPeerTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetupPeerTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetupPeerTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/SetupPeerTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExtensionSetExists
   Description: Checks whether extension set with provided ID exists.
   OperationID: ExtensionSetExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExtensionSetExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExtensionSetExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtensionSetExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetExists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsRestrictedSystemCode
   Description: Checks whether SystemCode is Epicor Delivered SystemCode.
   OperationID: IsRestrictedSystemCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsRestrictedSystemCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsRestrictedSystemCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsRestrictedSystemCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/IsRestrictedSystemCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InstallExtensionSet
   Description: Installs provided assembly alongside with optional symbols info.
   OperationID: InstallExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InstallExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InstallExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InstallExtensionSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/InstallExtensionSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MapExtensionSetToCompany
   Description: Associates extension set related to the specified ID to the specified company.
   OperationID: MapExtensionSetToCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MapExtensionSetToCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MapExtensionSetToCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MapExtensionSetToCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/MapExtensionSetToCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMapping
   Description: Returns extensions registered in companies as well as productizations from global level
   OperationID: GetMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMapping(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetMapping", {
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
   Summary: Invoke method RemoveExtensionSet
   Description: Removes extension set assembly alongside with related metadata
   OperationID: RemoveExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveExtensionSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/RemoveExtensionSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataSetTables
   Description: Gets the list of tables (both base and extension) in a dataset.
   OperationID: GetDataSetTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataSetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataSetTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetDataSetTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportExtensionSet
   Description: Returns byte[] representing extension set tableset and assembly body with optional debug symbols.
   OperationID: ExportExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportExtensionSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExportExtensionSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportExtensionSet
   Description: Returns byte[] representing extension set tableset and assembly body with optional debug symbols.
   OperationID: ImportExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportExtensionSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ImportExtensionSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckExtensionTable
   Description: Validates the structure of the extension table definition.
   OperationID: CheckExtensionTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckExtensionTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExtensionTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckExtensionTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/CheckExtensionTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckExtensionTableStatus
   Description: Validates the structure of the extension table definition.
   OperationID: CheckExtensionTableStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckExtensionTableStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExtensionTableStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckExtensionTableStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/CheckExtensionTableStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompaniesUsingTheExtension
   Description: Gets the companies using the extensionSetID.
   OperationID: GetCompaniesUsingTheExtension
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompaniesUsingTheExtension_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompaniesUsingTheExtension_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompaniesUsingTheExtension(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetCompaniesUsingTheExtension", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteExtensionSetMappingForCurrentCompany
   Description: Deletes the extension set mapping for company in session.
   OperationID: DeleteExtensionSetMappingForCurrentCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteExtensionSetMappingForCurrentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteExtensionSetMappingForCurrentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteExtensionSetMappingForCurrentCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/DeleteExtensionSetMappingForCurrentCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExtensionSetID
   Description: Generates the Extension ID for a given provider, level and product
   OperationID: GetExtensionSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtensionSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtensionSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExtensionSetID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetExtensionSetID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPeerTable
   Description: Validates or check the status of a peer table relation.
   OperationID: CheckPeerTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPeerTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPeerTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPeerTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/CheckPeerTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtension
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtension
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtension_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtension_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtension(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetNewExtension", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtensionSetMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionSetMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionSetMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionSetMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtensionSetMapping(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetNewExtensionSetMapping", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtensionRelation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionRelation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionRelation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionRelation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtensionRelation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetNewExtensionRelation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtensionRelationColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionRelationColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionRelationColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionRelationColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtensionRelationColumn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetNewExtensionRelationColumn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionColumnRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionColumnRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationColumnRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionRelationColumnRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionRelationRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionSetMappingRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionSetMappingRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableKeyRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionTableKeyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExtensionTableRow[],
}

export interface Ice_Tablesets_ExtensionColumnRow{
   "DataTableID":string,
   "ExtensionSetID":string,
   "SystemCode":string,
   "FieldName":string,
   "DataType":string,
   "Seq":number,
   "Description":string,
   "FieldScale":number,
   "FieldFormat":string,
   "FieldLabel":string,
   "InitialValue":string,
   "Required":boolean,
   "LikeDataFieldSystemCode":string,
   "LikeDataFieldTableID":string,
   "LikeDataFieldName":string,
   "IsHidden":boolean,
      /**  Code and Description value list  */  
   "CodeDescriptionList":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExtensionListRow{
      /**  ExtensionSetID  */  
   "ExtensionSetID":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExtensionRelationColumnRow{
      /**  ExtensionSetID  */  
   "ExtensionSetID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataSetID  */  
   "DataSetID":string,
      /**  RelationID  */  
   "RelationID":string,
      /**  Seq  */  
   "Seq":number,
      /**  ParentFieldName  */  
   "ParentFieldName":string,
      /**  ChildFieldName  */  
   "ChildFieldName":string,
      /**  CompOp  */  
   "CompOp":string,
      /**  IsConst  */  
   "IsConst":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExtensionRelationRow{
      /**  ExtensionSetID  */  
   "ExtensionSetID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataSetID  */  
   "DataSetID":string,
      /**  RelationID  */  
   "RelationID":string,
      /**  ParentSystemCode  */  
   "ParentSystemCode":string,
      /**  ParentDataTableID  */  
   "ParentDataTableID":string,
      /**  ChildSystemCode  */  
   "ChildSystemCode":string,
      /**  ChildDataTableID  */  
   "ChildDataTableID":string,
      /**  KeyID  */  
   "KeyID":string,
      /**  Description  */  
   "Description":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Type  */  
   "Type":number,
      /**  TreatAsPeer  */  
   "TreatAsPeer":boolean,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "FullParentTableName":string,
   "FullChildTableName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExtensionRow{
      /**  ExtensionSetID  */  
   "ExtensionSetID":string,
      /**  Provider  */  
   "Provider":string,
      /**  Product  */  
   "Product":string,
      /**  Assembly  */  
   "Assembly":string,
      /**  Version  */  
   "Version":string,
      /**  Level  */  
   "Level":number,
      /**  Disabled  */  
   "Disabled":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "GenIMTable":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExtensionSetMappingRow{
      /**  Company  */  
   "Company":string,
      /**  ExtensionSetID  */  
   "ExtensionSetID":string,
      /**  Order  */  
   "Order":number,
      /**  Disabled  */  
   "Disabled":boolean,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExtensionTableKeyRow{
   "DataTableID":string,
   "ExtensionSetID":string,
   "SystemCode":string,
   "Seq":number,
   "FieldName":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExtensionTableRow{
   "DataTableID":string,
   "Description":string,
   "ExtensionSetID":string,
   "SystemCode":string,
   "DataSetID":string,
   "DataSetSystemCode":string,
   "TableType":string,
   "GenIMTable":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param systemCode
      @param tableName
      @param createFullReport
   */  
export interface CheckExtensionTableStatus_input{
      /**  Table system code  */  
   systemCode:string,
      /**  Table name  */  
   tableName:string,
      /**  If true, generate full report, otherwise only until first discrepancy in the column definition  */  
   createFullReport:boolean,
}

export interface CheckExtensionTableStatus_output{
   returnObj:Ice_Tablesets_ExtensionValidationTableset[],
}

   /** Required : 
      @param systemCode
      @param tableName
      @param createFullReport
   */  
export interface CheckExtensionTable_input{
      /**  Table system code  */  
   systemCode:string,
      /**  Table name  */  
   tableName:string,
      /**  If true, generate full report, otherwise only until first discrepancy in the column definition  */  
   createFullReport:boolean,
}

export interface CheckExtensionTable_output{
      /**  List of errors found  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   validationFlag:number,
}
}

   /** Required : 
      @param extensionSetID
      @param parentDataSetID
      @param parentSystemCode
      @param systemCode
      @param tableName
   */  
export interface CheckPeerTable_input{
      /**  Extension ID  */  
   extensionSetID:string,
      /**  Parent table (or base table) dataset ID.  */  
   parentDataSetID:string,
      /**  Parent table (or base table) system code.  */  
   parentSystemCode:string,
      /**  Peer (extension) table dataset ID.  */  
   systemCode:string,
      /**  Peer (extension) table table ID.  */  
   tableName:string,
}

export interface CheckPeerTable_output{
   returnObj:Ice_Tablesets_ExtensionValidationTableset[],
}

   /** Required : 
      @param extensionSetID
   */  
export interface DeleteByID_input{
   extensionSetID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param extensionSetID
   */  
export interface DeleteExtensionSetMappingForCurrentCompany_input{
      /**  The extension set identifier.  */  
   extensionSetID:string,
}

export interface DeleteExtensionSetMappingForCurrentCompany_output{
}

   /** Required : 
      @param extensionSetID
   */  
export interface ExportExtensionSet_input{
      /**  ID of the extension set  */  
   extensionSetID:string,
}

export interface ExportExtensionSet_output{
      /**  null - when no extension set assembly found for the ID, otherwise - instance of the byte[]  */  
   returnObj:string,
}

   /** Required : 
      @param extensionSetID
   */  
export interface ExtensionSetExists_input{
      /**  ID of the extension set  */  
   extensionSetID:string,
}

export interface ExtensionSetExists_output{
      /**  true - when extension set is installed, otherwise - false  */  
   returnObj:boolean,
}

   /** Required : 
      @param extensionSetID
   */  
export interface GetByID_input{
   extensionSetID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ExtensionTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ExtensionTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ExtensionTableset[],
}

   /** Required : 
      @param extensionSetID
   */  
export interface GetCompaniesUsingTheExtension_input{
      /**  The extension set identifier.  */  
   extensionSetID:string,
}

export interface GetCompaniesUsingTheExtension_output{
      /**  Array of company identifier using the extensionSetID.  */  
   returnObj:string,
}

   /** Required : 
      @param systemCode
      @param dataSetID
   */  
export interface GetDataSetTables_input{
   systemCode:string,
   dataSetID:string,
}

export interface GetDataSetTables_output{
   returnObj:Ice_Tablesets_ExtensionDatasetTableListTableset[],
}

   /** Required : 
      @param extensionSetID
   */  
export interface GetExtensionSetAssembly_input{
      /**  ID of the extension set  */  
   extensionSetID:string,
}

export interface GetExtensionSetAssembly_output{
   returnObj:Ice_Contracts_ExtensionSetAssembly[],
}

   /** Required : 
      @param provider
      @param level
      @param product
   */  
export interface GetExtensionSetID_input{
      /**  provider  */  
   provider:string,
      /**  level  */  
   level:number,
      /**  product  */  
   product:string,
}

export interface GetExtensionSetID_output{
      /**  the Extension ID  */  
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
   returnObj:Ice_Tablesets_ExtensionListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetMapping_output{
   returnObj:Ice_Tablesets_ExtensionSetMappingTableset[],
}

   /** Required : 
      @param ds
      @param extensionSetID
      @param systemCode
      @param dataTableID
   */  
export interface GetNewExtensionColumn_input{
   ds:Ice_Tablesets_ExtensionTableset[],
   extensionSetID:string,
   systemCode:string,
   dataTableID:string,
}

export interface GetNewExtensionColumn_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

   /** Required : 
      @param ds
      @param extensionSetID
      @param systemCode
      @param dataSetID
      @param relationID
   */  
export interface GetNewExtensionRelationColumn_input{
   ds:Ice_Tablesets_ExtensionTableset[],
   extensionSetID:string,
   systemCode:string,
   dataSetID:string,
   relationID:string,
}

export interface GetNewExtensionRelationColumn_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

   /** Required : 
      @param ds
      @param extensionSetID
      @param systemCode
      @param dataSetID
   */  
export interface GetNewExtensionRelation_input{
   ds:Ice_Tablesets_ExtensionTableset[],
   extensionSetID:string,
   systemCode:string,
   dataSetID:string,
}

export interface GetNewExtensionRelation_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewExtensionSetMapping_input{
   ds:Ice_Tablesets_ExtensionTableset[],
   company:string,
}

export interface GetNewExtensionSetMapping_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

   /** Required : 
      @param ds
      @param extensionSetID
      @param systemCode
      @param dataTableID
   */  
export interface GetNewExtensionTableKey_input{
   ds:Ice_Tablesets_ExtensionTableset[],
   extensionSetID:string,
   systemCode:string,
   dataTableID:string,
}

export interface GetNewExtensionTableKey_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

   /** Required : 
      @param ds
      @param extensionSetID
      @param systemCode
   */  
export interface GetNewExtensionTable_input{
   ds:Ice_Tablesets_ExtensionTableset[],
   extensionSetID:string,
   systemCode:string,
}

export interface GetNewExtensionTable_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewExtension_input{
   ds:Ice_Tablesets_ExtensionTableset[],
}

export interface GetNewExtension_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

   /** Required : 
      @param whereClauseExtension
      @param whereClauseExtensionSetMapping
      @param whereClauseExtensionTable
      @param whereClauseExtensionColumn
      @param whereClauseExtensionRelation
      @param whereClauseExtensionRelationColumn
      @param whereClauseExtensionTableKey
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseExtension:string,
   whereClauseExtensionSetMapping:string,
   whereClauseExtensionTable:string,
   whereClauseExtensionColumn:string,
   whereClauseExtensionRelation:string,
   whereClauseExtensionRelationColumn:string,
   whereClauseExtensionTableKey:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ExtensionTableset[],
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

export interface Ice_Contracts_ExtensionSetAssembly{
   Assembly:string,
   Symbols:string,
   SystemFlag:number,
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

export interface Ice_Tablesets_ExtensionColumnRow{
   DataTableID:string,
   ExtensionSetID:string,
   SystemCode:string,
   FieldName:string,
   DataType:string,
   Seq:number,
   Description:string,
   FieldScale:number,
   FieldFormat:string,
   FieldLabel:string,
   InitialValue:string,
   Required:boolean,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   IsHidden:boolean,
      /**  Code and Description value list  */  
   CodeDescriptionList:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionDatasetTableListRow{
   SystemCode:string,
   DataTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionDatasetTableListTableset{
   ExtensionDatasetTableList:Ice_Tablesets_ExtensionDatasetTableListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExtensionErrorMessageRow{
      /**  Error message.  */  
   Message:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionListRow{
      /**  ExtensionSetID  */  
   ExtensionSetID:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionListTableset{
   ExtensionList:Ice_Tablesets_ExtensionListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExtensionRelationColumnRow{
      /**  ExtensionSetID  */  
   ExtensionSetID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataSetID  */  
   DataSetID:string,
      /**  RelationID  */  
   RelationID:string,
      /**  Seq  */  
   Seq:number,
      /**  ParentFieldName  */  
   ParentFieldName:string,
      /**  ChildFieldName  */  
   ChildFieldName:string,
      /**  CompOp  */  
   CompOp:string,
      /**  IsConst  */  
   IsConst:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionRelationRow{
      /**  ExtensionSetID  */  
   ExtensionSetID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataSetID  */  
   DataSetID:string,
      /**  RelationID  */  
   RelationID:string,
      /**  ParentSystemCode  */  
   ParentSystemCode:string,
      /**  ParentDataTableID  */  
   ParentDataTableID:string,
      /**  ChildSystemCode  */  
   ChildSystemCode:string,
      /**  ChildDataTableID  */  
   ChildDataTableID:string,
      /**  KeyID  */  
   KeyID:string,
      /**  Description  */  
   Description:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Type  */  
   Type:number,
      /**  TreatAsPeer  */  
   TreatAsPeer:boolean,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   FullParentTableName:string,
   FullChildTableName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionRow{
      /**  ExtensionSetID  */  
   ExtensionSetID:string,
      /**  Provider  */  
   Provider:string,
      /**  Product  */  
   Product:string,
      /**  Assembly  */  
   Assembly:string,
      /**  Version  */  
   Version:string,
      /**  Level  */  
   Level:number,
      /**  Disabled  */  
   Disabled:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   GenIMTable:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionSetMappingRow{
      /**  Company  */  
   Company:string,
      /**  ExtensionSetID  */  
   ExtensionSetID:string,
      /**  Order  */  
   Order:number,
      /**  Disabled  */  
   Disabled:boolean,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionSetMappingTableset{
   ExtensionSetMapping:Ice_Tablesets_ExtensionSetMappingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExtensionTableKeyRow{
   DataTableID:string,
   ExtensionSetID:string,
   SystemCode:string,
   Seq:number,
   FieldName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionTableRow{
   DataTableID:string,
   Description:string,
   ExtensionSetID:string,
   SystemCode:string,
   DataSetID:string,
   DataSetSystemCode:string,
   TableType:string,
   GenIMTable:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionTableStatusRow{
   PrimaryKeyIsNotDefined:boolean,
   TableDoesNotExistInDb:boolean,
   ColumnCountDiffers:boolean,
   ColumnOrderDiffers:boolean,
   DescriptionDiffers:boolean,
   FieldScaleDiffers:boolean,
   FieldFormatDiffers:boolean,
   FieldLabelDiffers:boolean,
   DefaultValueDiffers:boolean,
   DataTypeDiffers:boolean,
   NullabilityDiffers:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExtensionTableset{
   Extension:Ice_Tablesets_ExtensionRow[],
   ExtensionSetMapping:Ice_Tablesets_ExtensionSetMappingRow[],
   ExtensionTable:Ice_Tablesets_ExtensionTableRow[],
   ExtensionColumn:Ice_Tablesets_ExtensionColumnRow[],
   ExtensionRelation:Ice_Tablesets_ExtensionRelationRow[],
   ExtensionRelationColumn:Ice_Tablesets_ExtensionRelationColumnRow[],
   ExtensionTableKey:Ice_Tablesets_ExtensionTableKeyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExtensionValidationTableset{
   ExtensionTableStatus:Ice_Tablesets_ExtensionTableStatusRow[],
   ExtensionErrorMessage:Ice_Tablesets_ExtensionErrorMessageRow[],
   PeerTableStatus:Ice_Tablesets_PeerTableStatusRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_PeerTableStatusRow{
      /**  Peer table status - 0 (Unknown), 1 (OK), 2 (Not Found).  */  
   Status:number,
      /**  The status message.  */  
   StatusMessage:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtExtensionTableset{
   Extension:Ice_Tablesets_ExtensionRow[],
   ExtensionSetMapping:Ice_Tablesets_ExtensionSetMappingRow[],
   ExtensionTable:Ice_Tablesets_ExtensionTableRow[],
   ExtensionColumn:Ice_Tablesets_ExtensionColumnRow[],
   ExtensionRelation:Ice_Tablesets_ExtensionRelationRow[],
   ExtensionRelationColumn:Ice_Tablesets_ExtensionRelationColumnRow[],
   ExtensionTableKey:Ice_Tablesets_ExtensionTableKeyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param extBytes
   */  
export interface ImportExtensionSet_input{
      /**  Byte [] of extension set  */  
   extBytes:string,
}

export interface ImportExtensionSet_output{
}

   /** Required : 
      @param assembly
   */  
export interface InstallExtensionSet_input{
   assembly:Ice_Contracts_ExtensionSetAssembly[],
}

export interface InstallExtensionSet_output{
      /**  ID of the installed extension set  */  
   returnObj:string,
}

   /** Required : 
      @param systemCode
   */  
export interface IsRestrictedSystemCode_input{
      /**  System Code  */  
   systemCode:string,
}

export interface IsRestrictedSystemCode_output{
      /**  true - when SystemCode is Epicor DeliveredSystemCode or dbo, otherwise - false  */  
   returnObj:boolean,
}

   /** Required : 
      @param extensionSetId
      @param company
   */  
export interface MapExtensionSetToCompany_input{
      /**  ID of the installed extension set  */  
   extensionSetId:string,
      /**  Company ID  */  
   company:string,
}

export interface MapExtensionSetToCompany_output{
   returnObj:boolean,
}

   /** Required : 
      @param extensionSetID
   */  
export interface RemoveExtensionSet_input{
      /**  ID of the installed extension set  */  
   extensionSetID:string,
}

export interface RemoveExtensionSet_output{
}

   /** Required : 
      @param extensionSetID
      @param parentDataSetID
      @param parentSystemCode
      @param parentTable
      @param systemCode
      @param tableName
   */  
export interface SetupPeerTable_input{
      /**  ID of the extension set  */  
   extensionSetID:string,
      /**  Parent dataset where parent table belong  */  
   parentDataSetID:string,
      /**  Parent table system code  */  
   parentSystemCode:string,
      /**  Parent table name  */  
   parentTable:string,
      /**  Extension table system code  */  
   systemCode:string,
      /**  Extension table name  */  
   tableName:string,
}

export interface SetupPeerTable_output{
      /**  true - if changes were made, otherwise - false  */  
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtExtensionTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtExtensionTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ExtensionTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExtensionTableset[],
}
}

