import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.LookupDataSvc
// Description: Object to manage Lookup data: LookupTable, LookupLink, SourceValueField, TargetValueField
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/$metadata", {
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
   Description: Get LookupDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LookupDatas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupTableRow
   */  
export function get_LookupDatas(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LookupDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LookupTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LookupTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LookupDatas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LookupData item
   Description: Calls GetByID to retrieve the LookupData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LookupData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LookupTableRow
   */  
export function get_LookupDatas_Company_MapUID(Company:string, MapUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LookupTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LookupTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LookupData for the service
   Description: Calls UpdateExt to update LookupData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LookupData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LookupTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LookupDatas_Company_MapUID(Company:string, MapUID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")", {
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
   Summary: Call UpdateExt to delete LookupData item
   Description: Call UpdateExt to delete LookupData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LookupData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LookupDatas_Company_MapUID(Company:string, MapUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")", {
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
   Description: Get LookupLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LookupLinks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupLinkRow
   */  
export function get_LookupDatas_Company_MapUID_LookupLinks(Company:string, MapUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/LookupLinks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LookupLink item
   Description: Calls GetByID to retrieve the LookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LookupLink1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param LinkUID Desc: LinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   */  
export function get_LookupDatas_Company_MapUID_LookupLinks_Company_MapUID_LinkUID(Company:string, MapUID:string, LinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SourceValueFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SourceValueFields1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SourceValueFieldRow
   */  
export function get_LookupDatas_Company_MapUID_SourceValueFields(Company:string, MapUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SourceValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/SourceValueFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SourceValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SourceValueField item
   Description: Calls GetByID to retrieve the SourceValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SourceValueField1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   */  
export function get_LookupDatas_Company_MapUID_SourceValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SourceValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SourceValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TargetValueFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TargetValueFields1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TargetValueFieldRow
   */  
export function get_LookupDatas_Company_MapUID_TargetValueFields(Company:string, MapUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TargetValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/TargetValueFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TargetValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TargetValueField item
   Description: Calls GetByID to retrieve the TargetValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TargetValueField1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   */  
export function get_LookupDatas_Company_MapUID_TargetValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TargetValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TargetValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LookupLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LookupLinks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupLinkRow
   */  
export function get_LookupLinks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LookupLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LookupLinks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LookupLink item
   Description: Calls GetByID to retrieve the LookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LookupLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param LinkUID Desc: LinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   */  
export function get_LookupLinks_Company_MapUID_LinkUID(Company:string, MapUID:string, LinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LookupLink for the service
   Description: Calls UpdateExt to update LookupLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LookupLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param LinkUID Desc: LinkUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LookupLinks_Company_MapUID_LinkUID(Company:string, MapUID:string, LinkUID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")", {
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
   Summary: Call UpdateExt to delete LookupLink item
   Description: Call UpdateExt to delete LookupLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LookupLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param LinkUID Desc: LinkUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LookupLinks_Company_MapUID_LinkUID(Company:string, MapUID:string, LinkUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")", {
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
   Description: Get SourceValueFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SourceValueFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SourceValueFieldRow
   */  
export function get_SourceValueFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SourceValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SourceValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SourceValueFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SourceValueFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SourceValueField item
   Description: Calls GetByID to retrieve the SourceValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SourceValueField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   */  
export function get_SourceValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SourceValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SourceValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SourceValueField for the service
   Description: Calls UpdateExt to update SourceValueField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SourceValueField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SourceValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
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
   Summary: Call UpdateExt to delete SourceValueField item
   Description: Call UpdateExt to delete SourceValueField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SourceValueField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SourceValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
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
   Description: Get TargetValueFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TargetValueFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TargetValueFieldRow
   */  
export function get_TargetValueFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TargetValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TargetValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TargetValueFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TargetValueFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TargetValueField item
   Description: Calls GetByID to retrieve the TargetValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TargetValueField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   */  
export function get_TargetValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TargetValueFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TargetValueFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TargetValueField for the service
   Description: Calls UpdateExt to update TargetValueField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TargetValueField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TargetValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
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
   Summary: Call UpdateExt to delete TargetValueField item
   Description: Call UpdateExt to delete TargetValueField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TargetValueField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MapUID Desc: MapUID   Required: True
      @param SequenceNumber Desc: SequenceNumber   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TargetValueFields_Company_MapUID_SequenceNumber(Company:string, MapUID:string, SequenceNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupTableListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableListRow)
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
export function get_GetRows(whereClauseLookupTable:string, whereClauseLookupLink:string, whereClauseSourceValueField:string, whereClauseTargetValueField:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLookupTable!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLookupTable=" + whereClauseLookupTable
   }
   if(typeof whereClauseLookupLink!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLookupLink=" + whereClauseLookupLink
   }
   if(typeof whereClauseSourceValueField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSourceValueField=" + whereClauseSourceValueField
   }
   if(typeof whereClauseTargetValueField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTargetValueField=" + whereClauseTargetValueField
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetRows" + params, {
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
export function get_GetByID(mapUID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof mapUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mapUID=" + mapUID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetList" + params, {
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
   Summary: Invoke method GetByDisplayName
   Description: This method returns LookupData dataset if display name is known
   OperationID: GetByDisplayName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByDisplayName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDisplayName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByDisplayName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetByDisplayName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCOASegments
   Description: This method returns list of COA segments
   OperationID: GetCOASegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOASegments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetCOASegments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCOASegmentVals
   Description: This method returns list of COA segments
   OperationID: GetCOASegmentVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegmentVals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegmentVals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOASegmentVals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetCOASegmentVals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFieldValueList2
   OperationID: GetFieldValueList2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldValueList2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldValueList2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldValueList2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetFieldValueList2", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDBStructure
   Description: This method returns dataset with schemas and tables info.
   OperationID: GetDBStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDBStructure(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetDBStructure", {
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
   Summary: Invoke method LoadTableFields
   Description: This method adds rows to the table DBLoadedField. The includes fields from peer tables and user defined tables.
   OperationID: LoadTableFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadTableFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadTableFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadTableFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LoadTableFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetColumnDataType
   Description: This method returns data type of the specified field.
   OperationID: GetColumnDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetColumnDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetColumnDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetColumnDataType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetColumnDataType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportToFile
   Description: This method generates the file according to extension.
   OperationID: ExportToFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportToFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/ExportToFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportFromFile
   Description: This method generates the file according to extension.
   OperationID: ImportFromFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportFromFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFromFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportFromFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/ImportFromFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDynamicData
   Description: GetDynamicData - returns an untyped dynamic dataset
   OperationID: GetDynamicData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynamicData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynamicData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDynamicData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetDynamicData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PopulateLookupLink
   OperationID: PopulateLookupLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateLookupLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateLookupLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PopulateLookupLink(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/PopulateLookupLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLookupTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLookupTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLookupTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLookupTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLookupTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetNewLookupTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLookupLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLookupLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLookupLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLookupLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLookupLink(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetNewLookupLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSourceValueField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSourceValueField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSourceValueField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSourceValueField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSourceValueField(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetNewSourceValueField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTargetValueField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTargetValueField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTargetValueField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTargetValueField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTargetValueField(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetNewTargetValueField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupLinkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LookupLinkRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LookupTableListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LookupTableRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SourceValueFieldRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SourceValueFieldRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TargetValueFieldRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TargetValueFieldRow[],
}

export interface Erp_Tablesets_LookupLinkRow{
      /**  Link unique ID.  */  
   "LinkUID":number,
      /**  Map unique ID.  */  
   "MapUID":number,
      /**  Field1  */  
   "Field1":string,
      /**  Field2  */  
   "Field2":string,
      /**  Field3  */  
   "Field3":string,
      /**  Field4  */  
   "Field4":string,
      /**  Field5  */  
   "Field5":string,
      /**  Field6  */  
   "Field6":string,
      /**  Field7  */  
   "Field7":string,
      /**  Field8  */  
   "Field8":string,
      /**  Field9  */  
   "Field9":string,
      /**  Field10  */  
   "Field10":string,
      /**  Field11  */  
   "Field11":string,
      /**  Field12  */  
   "Field12":string,
      /**  Field13  */  
   "Field13":string,
      /**  Field14  */  
   "Field14":string,
      /**  Field15  */  
   "Field15":string,
      /**  Field16  */  
   "Field16":string,
      /**  Field17  */  
   "Field17":string,
      /**  Field18  */  
   "Field18":string,
      /**  Field19  */  
   "Field19":string,
      /**  Field20  */  
   "Field20":string,
      /**  Field21  */  
   "Field21":string,
      /**  Field22  */  
   "Field22":string,
      /**  Field23  */  
   "Field23":string,
      /**  Field24  */  
   "Field24":string,
      /**  Field25  */  
   "Field25":string,
      /**  Field26  */  
   "Field26":string,
      /**  Field27  */  
   "Field27":string,
      /**  Field28  */  
   "Field28":string,
      /**  Field29  */  
   "Field29":string,
      /**  Field30  */  
   "Field30":string,
      /**  Value1  */  
   "Value1":string,
      /**  Value2  */  
   "Value2":string,
      /**  Value3  */  
   "Value3":string,
      /**  Value4  */  
   "Value4":string,
      /**  Value5  */  
   "Value5":string,
      /**  Value6  */  
   "Value6":string,
      /**  Value7  */  
   "Value7":string,
      /**  Value8  */  
   "Value8":string,
      /**  Value9  */  
   "Value9":string,
      /**  Value10  */  
   "Value10":string,
      /**  Value11  */  
   "Value11":string,
      /**  Value12  */  
   "Value12":string,
      /**  Value13  */  
   "Value13":string,
      /**  Value14  */  
   "Value14":string,
      /**  Value15  */  
   "Value15":string,
      /**  Value16  */  
   "Value16":string,
      /**  Value17  */  
   "Value17":string,
      /**  Value18  */  
   "Value18":string,
      /**  Value19  */  
   "Value19":string,
      /**  Value20  */  
   "Value20":string,
      /**  Value21  */  
   "Value21":string,
      /**  Value22  */  
   "Value22":string,
      /**  Value23  */  
   "Value23":string,
      /**  Value24  */  
   "Value24":string,
      /**  Value25  */  
   "Value25":string,
      /**  Value26  */  
   "Value26":string,
      /**  Value27  */  
   "Value27":string,
      /**  Value28  */  
   "Value28":string,
      /**  Value29  */  
   "Value29":string,
      /**  Value30  */  
   "Value30":string,
      /**  System date when the link was created.  */  
   "CreationDate":string,
      /**  System time when the link was created (seconds since midnight format).  */  
   "CreationTime":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Marks this LookupLink as global, available to be sent out to other companies.  */  
   "GlobalLookupLink":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DspField1":string,
   "DspField2":string,
   "DspField3":string,
   "DspField4":string,
   "DspField5":string,
   "DspField6":string,
   "DspField7":string,
   "DspField8":string,
   "DspField9":string,
   "DspField10":string,
   "DspField11":string,
   "DspField12":string,
   "DspField13":string,
   "DspField14":string,
   "DspField15":string,
   "DspField16":string,
   "DspField17":string,
   "DspField18":string,
   "DspField19":string,
   "DspField20":string,
   "DspField21":string,
   "DspField22":string,
   "DspField23":string,
   "DspField24":string,
   "DspField25":string,
   "DspField26":string,
   "DspField27":string,
   "DspField28":string,
   "DspField29":string,
   "DspField30":string,
   "DspValue1":string,
   "DspValue2":string,
   "DspValue3":string,
   "DspValue4":string,
   "DspValue5":string,
   "DspValue6":string,
   "DspValue7":string,
   "DspValue8":string,
   "DspValue9":string,
   "DspValue10":string,
   "DspValue11":string,
   "DspValue12":string,
   "DspValue13":string,
   "DspValue14":string,
   "DspValue15":string,
   "DspValue16":string,
   "DspValue17":string,
   "DspValue18":string,
   "DspValue19":string,
   "DspValue20":string,
   "DspValue21":string,
   "DspValue22":string,
   "DspValue23":string,
   "DspValue24":string,
   "DspValue25":string,
   "DspValue26":string,
   "DspValue27":string,
   "DspValue28":string,
   "DspValue29":string,
   "DspValue30":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LookupTableListRow{
      /**  Map unique ID.  */  
   "MapUID":number,
      /**  Lookup table name wich should be displayed in a tree view controls.  */  
   "DisplayName":string,
      /**  Lookup table name.  */  
   "LookupName":string,
      /**  Detailed description of the lookup table.  */  
   "DetailedDescription":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Marks this LookupTable as global, available to be sent out to other companies.  */  
   "GlobalLookupTable":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LookupTableRow{
      /**  Map unique ID.  */  
   "MapUID":number,
      /**  Lookup table name wich should be displayed in a tree view controls.  */  
   "DisplayName":string,
      /**  Lookup table name.  */  
   "LookupName":string,
      /**  Detailed description of the lookup table.  */  
   "DetailedDescription":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Marks this LookupTable as global, available to be sent out to other companies.  */  
   "GlobalLookupTable":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SourceValueFieldRow{
      /**  Source value field unique ID.  */  
   "SourceValueFieldUID":number,
      /**  Map unique ID.  */  
   "MapUID":number,
      /**  Field sequence number.  */  
   "SequenceNumber":number,
      /**  Source field name.  */  
   "FieldName":string,
      /**  Detailed description.  */  
   "DetailedDescription":string,
      /**  Database table which field linked to the source value field.  */  
   "DBTable":string,
      /**  Field which linked to the source value field.  */  
   "DBField":string,
      /**  Turns on the validation of the field.  */  
   "Validate":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Marks this SourceValueField as global, available to be sent out to other companies.  */  
   "GlobalSourceValueField":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DBSchemaName  */  
   "DBSchemaName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TargetValueFieldRow{
      /**  Target value field unique ID.  */  
   "TargetValueFieldUID":number,
      /**  Map unique ID.  */  
   "MapUID":number,
      /**  Field sequence number.  */  
   "SequenceNumber":number,
      /**  Target field name.  */  
   "FieldName":string,
      /**  Detailed description.  */  
   "DetailedDescription":string,
      /**  Value Type  */  
   "ValueType":string,
      /**  Chart of accounts. Like COA.COACode.  */  
   "COACode":string,
      /**  Accounting segment from selected chart of accounts. Like COASegment.SegmentNbr.  */  
   "SegmentNbr":number,
      /**  Turns on the validation of the field.  */  
   "Validate":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Marks this TargetValueField as global, available to be sent out to other companies.  */  
   "GlobalTargetValueField":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SegmentName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param mapUID
   */  
export interface DeleteByID_input{
   mapUID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DBLoadedFieldRow{
   DBSchemaName:string,
   DBTableName:string,
   DisplayFieldName:string,
   ExtSchemaName:string,
   ExtTableName:string,
   ExtFieldName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DBSchemaRow{
   DBSchemaName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DBStructureTableset{
   DBSchema:Erp_Tablesets_DBSchemaRow[],
   DBTable:Erp_Tablesets_DBTableRow[],
   DBLoadedField:Erp_Tablesets_DBLoadedFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DBTableRow{
      /**  Db Schema of the Database table from Ice.Table view  */  
   DBSchemaName:string,
   DBTableName:string,
      /**  DB = Database, TT = Temp Table from ZDataTable  */  
   DBTableType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_LookupDataTableset{
   LookupTable:Erp_Tablesets_LookupTableRow[],
   LookupLink:Erp_Tablesets_LookupLinkRow[],
   SourceValueField:Erp_Tablesets_SourceValueFieldRow[],
   TargetValueField:Erp_Tablesets_TargetValueFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LookupLinkRow{
      /**  Link unique ID.  */  
   LinkUID:number,
      /**  Map unique ID.  */  
   MapUID:number,
      /**  Field1  */  
   Field1:string,
      /**  Field2  */  
   Field2:string,
      /**  Field3  */  
   Field3:string,
      /**  Field4  */  
   Field4:string,
      /**  Field5  */  
   Field5:string,
      /**  Field6  */  
   Field6:string,
      /**  Field7  */  
   Field7:string,
      /**  Field8  */  
   Field8:string,
      /**  Field9  */  
   Field9:string,
      /**  Field10  */  
   Field10:string,
      /**  Field11  */  
   Field11:string,
      /**  Field12  */  
   Field12:string,
      /**  Field13  */  
   Field13:string,
      /**  Field14  */  
   Field14:string,
      /**  Field15  */  
   Field15:string,
      /**  Field16  */  
   Field16:string,
      /**  Field17  */  
   Field17:string,
      /**  Field18  */  
   Field18:string,
      /**  Field19  */  
   Field19:string,
      /**  Field20  */  
   Field20:string,
      /**  Field21  */  
   Field21:string,
      /**  Field22  */  
   Field22:string,
      /**  Field23  */  
   Field23:string,
      /**  Field24  */  
   Field24:string,
      /**  Field25  */  
   Field25:string,
      /**  Field26  */  
   Field26:string,
      /**  Field27  */  
   Field27:string,
      /**  Field28  */  
   Field28:string,
      /**  Field29  */  
   Field29:string,
      /**  Field30  */  
   Field30:string,
      /**  Value1  */  
   Value1:string,
      /**  Value2  */  
   Value2:string,
      /**  Value3  */  
   Value3:string,
      /**  Value4  */  
   Value4:string,
      /**  Value5  */  
   Value5:string,
      /**  Value6  */  
   Value6:string,
      /**  Value7  */  
   Value7:string,
      /**  Value8  */  
   Value8:string,
      /**  Value9  */  
   Value9:string,
      /**  Value10  */  
   Value10:string,
      /**  Value11  */  
   Value11:string,
      /**  Value12  */  
   Value12:string,
      /**  Value13  */  
   Value13:string,
      /**  Value14  */  
   Value14:string,
      /**  Value15  */  
   Value15:string,
      /**  Value16  */  
   Value16:string,
      /**  Value17  */  
   Value17:string,
      /**  Value18  */  
   Value18:string,
      /**  Value19  */  
   Value19:string,
      /**  Value20  */  
   Value20:string,
      /**  Value21  */  
   Value21:string,
      /**  Value22  */  
   Value22:string,
      /**  Value23  */  
   Value23:string,
      /**  Value24  */  
   Value24:string,
      /**  Value25  */  
   Value25:string,
      /**  Value26  */  
   Value26:string,
      /**  Value27  */  
   Value27:string,
      /**  Value28  */  
   Value28:string,
      /**  Value29  */  
   Value29:string,
      /**  Value30  */  
   Value30:string,
      /**  System date when the link was created.  */  
   CreationDate:string,
      /**  System time when the link was created (seconds since midnight format).  */  
   CreationTime:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Marks this LookupLink as global, available to be sent out to other companies.  */  
   GlobalLookupLink:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DspField1:string,
   DspField2:string,
   DspField3:string,
   DspField4:string,
   DspField5:string,
   DspField6:string,
   DspField7:string,
   DspField8:string,
   DspField9:string,
   DspField10:string,
   DspField11:string,
   DspField12:string,
   DspField13:string,
   DspField14:string,
   DspField15:string,
   DspField16:string,
   DspField17:string,
   DspField18:string,
   DspField19:string,
   DspField20:string,
   DspField21:string,
   DspField22:string,
   DspField23:string,
   DspField24:string,
   DspField25:string,
   DspField26:string,
   DspField27:string,
   DspField28:string,
   DspField29:string,
   DspField30:string,
   DspValue1:string,
   DspValue2:string,
   DspValue3:string,
   DspValue4:string,
   DspValue5:string,
   DspValue6:string,
   DspValue7:string,
   DspValue8:string,
   DspValue9:string,
   DspValue10:string,
   DspValue11:string,
   DspValue12:string,
   DspValue13:string,
   DspValue14:string,
   DspValue15:string,
   DspValue16:string,
   DspValue17:string,
   DspValue18:string,
   DspValue19:string,
   DspValue20:string,
   DspValue21:string,
   DspValue22:string,
   DspValue23:string,
   DspValue24:string,
   DspValue25:string,
   DspValue26:string,
   DspValue27:string,
   DspValue28:string,
   DspValue29:string,
   DspValue30:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LookupTableListRow{
      /**  Map unique ID.  */  
   MapUID:number,
      /**  Lookup table name wich should be displayed in a tree view controls.  */  
   DisplayName:string,
      /**  Lookup table name.  */  
   LookupName:string,
      /**  Detailed description of the lookup table.  */  
   DetailedDescription:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Marks this LookupTable as global, available to be sent out to other companies.  */  
   GlobalLookupTable:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LookupTableListTableset{
   LookupTableList:Erp_Tablesets_LookupTableListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LookupTableRow{
      /**  Map unique ID.  */  
   MapUID:number,
      /**  Lookup table name wich should be displayed in a tree view controls.  */  
   DisplayName:string,
      /**  Lookup table name.  */  
   LookupName:string,
      /**  Detailed description of the lookup table.  */  
   DetailedDescription:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Marks this LookupTable as global, available to be sent out to other companies.  */  
   GlobalLookupTable:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SourceValueFieldRow{
      /**  Source value field unique ID.  */  
   SourceValueFieldUID:number,
      /**  Map unique ID.  */  
   MapUID:number,
      /**  Field sequence number.  */  
   SequenceNumber:number,
      /**  Source field name.  */  
   FieldName:string,
      /**  Detailed description.  */  
   DetailedDescription:string,
      /**  Database table which field linked to the source value field.  */  
   DBTable:string,
      /**  Field which linked to the source value field.  */  
   DBField:string,
      /**  Turns on the validation of the field.  */  
   Validate:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Marks this SourceValueField as global, available to be sent out to other companies.  */  
   GlobalSourceValueField:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DBSchemaName  */  
   DBSchemaName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TargetValueFieldRow{
      /**  Target value field unique ID.  */  
   TargetValueFieldUID:number,
      /**  Map unique ID.  */  
   MapUID:number,
      /**  Field sequence number.  */  
   SequenceNumber:number,
      /**  Target field name.  */  
   FieldName:string,
      /**  Detailed description.  */  
   DetailedDescription:string,
      /**  Value Type  */  
   ValueType:string,
      /**  Chart of accounts. Like COA.COACode.  */  
   COACode:string,
      /**  Accounting segment from selected chart of accounts. Like COASegment.SegmentNbr.  */  
   SegmentNbr:number,
      /**  Turns on the validation of the field.  */  
   Validate:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Marks this TargetValueField as global, available to be sent out to other companies.  */  
   GlobalTargetValueField:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SegmentName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtLookupDataTableset{
   LookupTable:Erp_Tablesets_LookupTableRow[],
   LookupLink:Erp_Tablesets_LookupLinkRow[],
   SourceValueField:Erp_Tablesets_SourceValueFieldRow[],
   TargetValueField:Erp_Tablesets_TargetValueFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param mapUidList
      @param fileName
      @param format
   */  
export interface ExportToFile_input{
   mapUidList:string,
   fileName:string,
   format:string,
}

export interface ExportToFile_output{
parameters : {
      /**  output parameters  */  
   errorMessage:string,
   exportedItemsNumber:number,
   serverFileName:string,
}
}

   /** Required : 
      @param displayName
   */  
export interface GetByDisplayName_input{
      /**  Display Name  */  
   displayName:string,
}

export interface GetByDisplayName_output{
   returnObj:Erp_Tablesets_LookupDataTableset[],
}

   /** Required : 
      @param mapUID
   */  
export interface GetByID_input{
   mapUID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LookupDataTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LookupDataTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LookupDataTableset[],
}

   /** Required : 
      @param coaCode
      @param segNum
   */  
export interface GetCOASegmentVals_input{
      /**  COA code  */  
   coaCode:string,
      /**  Segment number  */  
   segNum:number,
}

export interface GetCOASegmentVals_output{
parameters : {
      /**  output parameters  */  
   segValList:string,
}
}

   /** Required : 
      @param coaCode
   */  
export interface GetCOASegments_input{
      /**  COA code  */  
   coaCode:string,
}

export interface GetCOASegments_output{
parameters : {
      /**  output parameters  */  
   segList:string,
}
}

   /** Required : 
      @param schema
      @param table
      @param field
   */  
export interface GetColumnDataType_input{
      /**  Schema Name  */  
   schema:string,
      /**  Table Name  */  
   table:string,
      /**  Field Name  */  
   field:string,
}

export interface GetColumnDataType_output{
      /**  Field Data Type  */  
   returnObj:string,
}

export interface GetDBStructure_output{
   returnObj:Erp_Tablesets_DBStructureTableset[],
}

   /** Required : 
      @param mapUID
   */  
export interface GetDynamicData_input{
   mapUID:number,
}

export interface GetDynamicData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param schemaName
      @param tableName
      @param fieldName
      @param ds
      @param itemsList
   */  
export interface GetFieldValueList2_input{
   schemaName:string,
   tableName:string,
   fieldName:string,
   ds:Erp_Tablesets_DBStructureTableset[],
   itemsList:string,
}

export interface GetFieldValueList2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DBStructureTableset[],
   itemsList:any[],
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
   returnObj:Erp_Tablesets_LookupTableListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param mapUID
   */  
export interface GetNewLookupLink_input{
   ds:Erp_Tablesets_LookupDataTableset[],
   mapUID:number,
}

export interface GetNewLookupLink_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LookupDataTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewLookupTable_input{
   ds:Erp_Tablesets_LookupDataTableset[],
}

export interface GetNewLookupTable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LookupDataTableset[],
}
}

   /** Required : 
      @param ds
      @param mapUID
   */  
export interface GetNewSourceValueField_input{
   ds:Erp_Tablesets_LookupDataTableset[],
   mapUID:number,
}

export interface GetNewSourceValueField_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LookupDataTableset[],
}
}

   /** Required : 
      @param ds
      @param mapUID
   */  
export interface GetNewTargetValueField_input{
   ds:Erp_Tablesets_LookupDataTableset[],
   mapUID:number,
}

export interface GetNewTargetValueField_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LookupDataTableset[],
}
}

   /** Required : 
      @param whereClauseLookupTable
      @param whereClauseLookupLink
      @param whereClauseSourceValueField
      @param whereClauseTargetValueField
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLookupTable:string,
   whereClauseLookupLink:string,
   whereClauseSourceValueField:string,
   whereClauseTargetValueField:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LookupDataTableset[],
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
      @param fileName
   */  
export interface ImportFromFile_input{
   fileName:string,
}

export interface ImportFromFile_output{
parameters : {
      /**  output parameters  */  
   mapUID:number,
   errorMessage:string,
}
}

   /** Required : 
      @param schema
      @param table
      @param ds
   */  
export interface LoadTableFields_input{
      /**  DB schema name  */  
   schema:string,
      /**  DB table name  */  
   table:string,
   ds:Erp_Tablesets_DBStructureTableset[],
}

export interface LoadTableFields_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DBStructureTableset[],
}
}

   /** Required : 
      @param mapUID
      @param columnName
   */  
export interface PopulateLookupLink_input{
   mapUID:number,
   columnName:string,
}

export interface PopulateLookupLink_output{
   returnObj:Erp_Tablesets_LookupDataTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLookupDataTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLookupDataTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LookupDataTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LookupDataTableset[],
}
}

