import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.BAQExtDsTypeSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/$metadata", {
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
   Description: Get BAQExtDsTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsTypes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTypeRow
   */  
export function get_BAQExtDsTypes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQExtDsTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsType item
   Description: Calls GetByID to retrieve the BAQExtDsType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
   */  
export function get_BAQExtDsTypes_Company_DatasourceType(Company:string, DatasourceType:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQExtDsType for the service
   Description: Calls UpdateExt to update BAQExtDsType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQExtDsTypes_Company_DatasourceType(Company:string, DatasourceType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")", {
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
   Summary: Call UpdateExt to delete BAQExtDsType item
   Description: Call UpdateExt to delete BAQExtDsType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQExtDsTypes_Company_DatasourceType(Company:string, DatasourceType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")", {
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
   Description: Get BAQExtDsColumnFilters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsColumnFilters1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsColumnFilterRow
   */  
export function get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsColumnFilters(Company:string, DatasourceType:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsColumnFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsColumnFilters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsColumnFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsColumnFilter item
   Description: Calls GetByID to retrieve the BAQExtDsColumnFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsColumnFilter1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   */  
export function get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsColumnFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsColumnFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsFilterGroups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsFilterGroups1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterGroupRow
   */  
export function get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsFilterGroups(Company:string, DatasourceType:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsFilterGroups", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterGroup item
   Description: Calls GetByID to retrieve the BAQExtDsFilterGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterGroup1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   */  
export function get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company:string, DatasourceType:string, FilterGroupName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsFilterGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsFilterGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsTableFilters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsTableFilters1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTableFilterRow
   */  
export function get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsTableFilters(Company:string, DatasourceType:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTableFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsTableFilters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTableFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsTableFilter item
   Description: Calls GetByID to retrieve the BAQExtDsTableFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsTableFilter1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   */  
export function get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsTableFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsTableFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsColumnFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsColumnFilters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsColumnFilterRow
   */  
export function get_BAQExtDsColumnFilters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsColumnFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsColumnFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsColumnFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQExtDsColumnFilters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsColumnFilter item
   Description: Calls GetByID to retrieve the BAQExtDsColumnFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsColumnFilter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   */  
export function get_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsColumnFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsColumnFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQExtDsColumnFilter for the service
   Description: Calls UpdateExt to update BAQExtDsColumnFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsColumnFilter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
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
   Summary: Call UpdateExt to delete BAQExtDsColumnFilter item
   Description: Call UpdateExt to delete BAQExtDsColumnFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsColumnFilter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
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
   Description: Get BAQExtDsFilterGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsFilterGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterGroupRow
   */  
export function get_BAQExtDsFilterGroups(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsFilterGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQExtDsFilterGroups(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterGroup item
   Description: Calls GetByID to retrieve the BAQExtDsFilterGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   */  
export function get_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company:string, DatasourceType:string, FilterGroupName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsFilterGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsFilterGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQExtDsFilterGroup for the service
   Description: Calls UpdateExt to update BAQExtDsFilterGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsFilterGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company:string, DatasourceType:string, FilterGroupName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")", {
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
   Summary: Call UpdateExt to delete BAQExtDsFilterGroup item
   Description: Call UpdateExt to delete BAQExtDsFilterGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsFilterGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company:string, DatasourceType:string, FilterGroupName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")", {
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
   Description: Get BAQExtDsFilterDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsFilterDefs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterDefRow
   */  
export function get_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName_BAQExtDsFilterDefs(Company:string, DatasourceType:string, FilterGroupName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")/BAQExtDsFilterDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterDef item
   Description: Calls GetByID to retrieve the BAQExtDsFilterDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterDef1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      @param FilterName Desc: FilterName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   */  
export function get_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company:string, DatasourceType:string, FilterGroupName:string, FilterName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsFilterDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsFilterDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsFilterDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsFilterDefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterDefRow
   */  
export function get_BAQExtDsFilterDefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsFilterDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQExtDsFilterDefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterDef item
   Description: Calls GetByID to retrieve the BAQExtDsFilterDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      @param FilterName Desc: FilterName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   */  
export function get_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company:string, DatasourceType:string, FilterGroupName:string, FilterName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsFilterDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsFilterDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQExtDsFilterDef for the service
   Description: Calls UpdateExt to update BAQExtDsFilterDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsFilterDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      @param FilterName Desc: FilterName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company:string, DatasourceType:string, FilterGroupName:string, FilterName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")", {
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
   Summary: Call UpdateExt to delete BAQExtDsFilterDef item
   Description: Call UpdateExt to delete BAQExtDsFilterDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsFilterDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterGroupName Desc: FilterGroupName   Required: True   Allow empty value : True
      @param FilterName Desc: FilterName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company:string, DatasourceType:string, FilterGroupName:string, FilterName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")", {
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
   Description: Get BAQExtDsTableFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsTableFilters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTableFilterRow
   */  
export function get_BAQExtDsTableFilters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTableFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTableFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsTableFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQExtDsTableFilters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQExtDsTableFilter item
   Description: Calls GetByID to retrieve the BAQExtDsTableFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsTableFilter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   */  
export function get_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQExtDsTableFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQExtDsTableFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQExtDsTableFilter for the service
   Description: Calls UpdateExt to update BAQExtDsTableFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsTableFilter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
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
   Summary: Call UpdateExt to delete BAQExtDsTableFilter item
   Description: Call UpdateExt to delete BAQExtDsTableFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsTableFilter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DatasourceType Desc: DatasourceType   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company:string, DatasourceType:string, FilterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTypeListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeListRow)
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
export function get_GetRows(whereClauseBAQExtDsType:string, whereClauseBAQExtDsColumnFilter:string, whereClauseBAQExtDsFilterGroup:string, whereClauseBAQExtDsFilterDef:string, whereClauseBAQExtDsTableFilter:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseBAQExtDsType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQExtDsType=" + whereClauseBAQExtDsType
   }
   if(typeof whereClauseBAQExtDsColumnFilter!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQExtDsColumnFilter=" + whereClauseBAQExtDsColumnFilter
   }
   if(typeof whereClauseBAQExtDsFilterGroup!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQExtDsFilterGroup=" + whereClauseBAQExtDsFilterGroup
   }
   if(typeof whereClauseBAQExtDsFilterDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQExtDsFilterDef=" + whereClauseBAQExtDsFilterDef
   }
   if(typeof whereClauseBAQExtDsTableFilter!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQExtDsTableFilter=" + whereClauseBAQExtDsTableFilter
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetRows" + params, {
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
export function get_GetByID(datasourceType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof datasourceType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "datasourceType=" + datasourceType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetList" + params, {
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
   Summary: Invoke method GetGlobalConstantList
   Description: Build a list of global constants
   OperationID: GetGlobalConstantList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlobalConstantList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlobalConstantList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetGlobalConstantList", {
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
   Summary: Invoke method MoveTableFilter
   Description: Move record up or down
   OperationID: MoveTableFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveTableFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveTableFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveTableFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/MoveTableFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveColumnFilter
   Description: Move BAQExtDsColumnFilter record up or down
   OperationID: MoveColumnFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveColumnFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveColumnFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveColumnFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/MoveColumnFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveFilterDef
   Description: Move BAQExtDsFilterDef record up or down
   OperationID: MoveFilterDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveFilterDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFilterDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveFilterDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/MoveFilterDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBAQExtDsType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQExtDsType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetNewBAQExtDsType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBAQExtDsColumnFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsColumnFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsColumnFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsColumnFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQExtDsColumnFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetNewBAQExtDsColumnFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBAQExtDsFilterGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsFilterGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsFilterGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsFilterGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQExtDsFilterGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetNewBAQExtDsFilterGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBAQExtDsFilterDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsFilterDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsFilterDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsFilterDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQExtDsFilterDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetNewBAQExtDsFilterDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBAQExtDsTableFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsTableFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsTableFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsTableFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQExtDsTableFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetNewBAQExtDsTableFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsColumnFilterRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQExtDsColumnFilterRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterDefRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQExtDsFilterDefRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterGroupRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQExtDsFilterGroupRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTableFilterRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQExtDsTableFilterRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQExtDsTypeListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQExtDsTypeRow[],
}

export interface Ice_Tablesets_BAQExtDsColumnFilterRow{
      /**  Company  */  
   "Company":string,
      /**  DatasourceType  */  
   "DatasourceType":string,
      /**  FilterID  */  
   "FilterID":string,
      /**  Seq  */  
   "Seq":number,
      /**  AndOr  */  
   "AndOr":string,
      /**  Neg  */  
   "Neg":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  TableName  */  
   "TableName":string,
      /**  FieldName  */  
   "FieldName":string,
      /**  RightP  */  
   "RightP":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQExtDsFilterDefRow{
      /**  Company  */  
   "Company":string,
      /**  DatasourceType  */  
   "DatasourceType":string,
      /**  FilterGroupName  */  
   "FilterGroupName":string,
      /**  FilterName  */  
   "FilterName":string,
      /**  Seq  */  
   "Seq":number,
      /**  AndOr  */  
   "AndOr":string,
      /**  Neg  */  
   "Neg":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  TableName  */  
   "TableName":string,
      /**  FieldName  */  
   "FieldName":string,
      /**  DefaultConstant  */  
   "DefaultConstant":string,
      /**  RightP  */  
   "RightP":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQExtDsFilterGroupRow{
      /**  Company  */  
   "Company":string,
      /**  DatasourceType  */  
   "DatasourceType":string,
      /**  FilterGroupName  */  
   "FilterGroupName":string,
      /**  Description  */  
   "Description":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQExtDsTableFilterRow{
      /**  Company  */  
   "Company":string,
      /**  DatasourceType  */  
   "DatasourceType":string,
      /**  FilterID  */  
   "FilterID":string,
      /**  Seq  */  
   "Seq":number,
      /**  AndOr  */  
   "AndOr":string,
      /**  Neg  */  
   "Neg":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  TableName  */  
   "TableName":string,
      /**  RightP  */  
   "RightP":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQExtDsTypeListRow{
      /**  Company  */  
   "Company":string,
      /**  DatasourceType  */  
   "DatasourceType":string,
      /**  Description  */  
   "Description":string,
      /**  ApplicationType  */  
   "ApplicationType":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQExtDsTypeRow{
      /**  Company  */  
   "Company":string,
      /**  DatasourceType  */  
   "DatasourceType":string,
      /**  Description  */  
   "Description":string,
      /**  SampleDatasourceName  */  
   "SampleDatasourceName":string,
      /**  ApplicationType  */  
   "ApplicationType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "AllCompanies":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param datasourceType
   */  
export interface DeleteByID_input{
   datasourceType:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param datasourceType
   */  
export interface GetByID_input{
   datasourceType:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_BAQExtDsTypeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_BAQExtDsTypeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_BAQExtDsTypeTableset[],
}

export interface GetGlobalConstantList_output{
      /**  delimited list of global constants  */  
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
   returnObj:Ice_Tablesets_BAQExtDsTypeListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param datasourceType
   */  
export interface GetNewBAQExtDsColumnFilter_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
   datasourceType:string,
}

export interface GetNewBAQExtDsColumnFilter_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param ds
      @param datasourceType
      @param filterGroupName
   */  
export interface GetNewBAQExtDsFilterDef_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
   datasourceType:string,
   filterGroupName:string,
}

export interface GetNewBAQExtDsFilterDef_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param ds
      @param datasourceType
   */  
export interface GetNewBAQExtDsFilterGroup_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
   datasourceType:string,
}

export interface GetNewBAQExtDsFilterGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param ds
      @param datasourceType
   */  
export interface GetNewBAQExtDsTableFilter_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
   datasourceType:string,
}

export interface GetNewBAQExtDsTableFilter_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewBAQExtDsType_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}

export interface GetNewBAQExtDsType_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param whereClauseBAQExtDsType
      @param whereClauseBAQExtDsColumnFilter
      @param whereClauseBAQExtDsFilterGroup
      @param whereClauseBAQExtDsFilterDef
      @param whereClauseBAQExtDsTableFilter
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseBAQExtDsType:string,
   whereClauseBAQExtDsColumnFilter:string,
   whereClauseBAQExtDsFilterGroup:string,
   whereClauseBAQExtDsFilterDef:string,
   whereClauseBAQExtDsTableFilter:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_BAQExtDsTypeTableset[],
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

export interface Ice_Tablesets_BAQExtDsColumnFilterRow{
      /**  Company  */  
   Company:string,
      /**  DatasourceType  */  
   DatasourceType:string,
      /**  FilterID  */  
   FilterID:string,
      /**  Seq  */  
   Seq:number,
      /**  AndOr  */  
   AndOr:string,
      /**  Neg  */  
   Neg:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  TableName  */  
   TableName:string,
      /**  FieldName  */  
   FieldName:string,
      /**  RightP  */  
   RightP:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDsFilterDefRow{
      /**  Company  */  
   Company:string,
      /**  DatasourceType  */  
   DatasourceType:string,
      /**  FilterGroupName  */  
   FilterGroupName:string,
      /**  FilterName  */  
   FilterName:string,
      /**  Seq  */  
   Seq:number,
      /**  AndOr  */  
   AndOr:string,
      /**  Neg  */  
   Neg:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  TableName  */  
   TableName:string,
      /**  FieldName  */  
   FieldName:string,
      /**  DefaultConstant  */  
   DefaultConstant:string,
      /**  RightP  */  
   RightP:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDsFilterGroupRow{
      /**  Company  */  
   Company:string,
      /**  DatasourceType  */  
   DatasourceType:string,
      /**  FilterGroupName  */  
   FilterGroupName:string,
      /**  Description  */  
   Description:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDsTableFilterRow{
      /**  Company  */  
   Company:string,
      /**  DatasourceType  */  
   DatasourceType:string,
      /**  FilterID  */  
   FilterID:string,
      /**  Seq  */  
   Seq:number,
      /**  AndOr  */  
   AndOr:string,
      /**  Neg  */  
   Neg:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  TableName  */  
   TableName:string,
      /**  RightP  */  
   RightP:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDsTypeListRow{
      /**  Company  */  
   Company:string,
      /**  DatasourceType  */  
   DatasourceType:string,
      /**  Description  */  
   Description:string,
      /**  ApplicationType  */  
   ApplicationType:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDsTypeListTableset{
   BAQExtDsTypeList:Ice_Tablesets_BAQExtDsTypeListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtDsTypeRow{
      /**  Company  */  
   Company:string,
      /**  DatasourceType  */  
   DatasourceType:string,
      /**  Description  */  
   Description:string,
      /**  SampleDatasourceName  */  
   SampleDatasourceName:string,
      /**  ApplicationType  */  
   ApplicationType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   AllCompanies:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDsTypeTableset{
   BAQExtDsType:Ice_Tablesets_BAQExtDsTypeRow[],
   BAQExtDsColumnFilter:Ice_Tablesets_BAQExtDsColumnFilterRow[],
   BAQExtDsFilterGroup:Ice_Tablesets_BAQExtDsFilterGroupRow[],
   BAQExtDsFilterDef:Ice_Tablesets_BAQExtDsFilterDefRow[],
   BAQExtDsTableFilter:Ice_Tablesets_BAQExtDsTableFilterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtBAQExtDsTypeTableset{
   BAQExtDsType:Ice_Tablesets_BAQExtDsTypeRow[],
   BAQExtDsColumnFilter:Ice_Tablesets_BAQExtDsColumnFilterRow[],
   BAQExtDsFilterGroup:Ice_Tablesets_BAQExtDsFilterGroupRow[],
   BAQExtDsFilterDef:Ice_Tablesets_BAQExtDsFilterDefRow[],
   BAQExtDsTableFilter:Ice_Tablesets_BAQExtDsTableFilterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param currentSysRowID
      @param direction
   */  
export interface MoveColumnFilter_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
   currentSysRowID:string,
   direction:string,
}

export interface MoveColumnFilter_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param ds
      @param currentSysRowID
      @param filterGroupName
      @param direction
   */  
export interface MoveFilterDef_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
   currentSysRowID:string,
   filterGroupName:string,
   direction:string,
}

export interface MoveFilterDef_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param ds
      @param currentSysRowID
      @param direction
   */  
export interface MoveTableFilter_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
   currentSysRowID:string,
   direction:string,
}

export interface MoveTableFilter_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtBAQExtDsTypeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtBAQExtDsTypeTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQExtDsTypeTableset[],
}
}

