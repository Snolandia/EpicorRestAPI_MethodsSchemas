import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PriceLstSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/$metadata", {
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
   Description: Get PriceLsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLsts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstRow
   */  
export function get_PriceLsts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PriceLsts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PriceLst item
   Description: Calls GetByID to retrieve the PriceLst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   */  
export function get_PriceLsts_Company_ListCode(Company:string, ListCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PriceLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PriceLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PriceLst for the service
   Description: Calls UpdateExt to update PriceLst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PriceLsts_Company_ListCode(Company:string, ListCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")", {
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
   Summary: Call UpdateExt to delete PriceLst item
   Description: Call UpdateExt to delete PriceLst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PriceLsts_Company_ListCode(Company:string, ListCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")", {
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
   Description: Get PriceLstGroups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceLstGroups1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstGroupsRow
   */  
export function get_PriceLsts_Company_ListCode_PriceLstGroups(Company:string, ListCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstGroups", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PriceLstGroup item
   Description: Calls GetByID to retrieve the PriceLstGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstGroup1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   */  
export function get_PriceLsts_Company_ListCode_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company:string, ListCode:string, ProdCode:string, UOMCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PriceLstGroupsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PriceLstGroupsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PriceLstParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceLstParts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstPartsRow
   */  
export function get_PriceLsts_Company_ListCode_PriceLstParts(Company:string, ListCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PriceLstPart item
   Description: Calls GetByID to retrieve the PriceLstPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstPart1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   */  
export function get_PriceLsts_Company_ListCode_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company:string, ListCode:string, PartNum:string, UOMCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PriceLstPartsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PriceLstPartsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PriceLstAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceLstAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstAttchRow
   */  
export function get_PriceLsts_Company_ListCode_PriceLstAttches(Company:string, ListCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PriceLstAttch item
   Description: Calls GetByID to retrieve the PriceLstAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   */  
export function get_PriceLsts_Company_ListCode_PriceLstAttches_Company_ListCode_DrawingSeq(Company:string, ListCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PriceLstAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PriceLstAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PriceLstGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstGroupsRow
   */  
export function get_PriceLstGroups(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PriceLstGroups(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PriceLstGroup item
   Description: Calls GetByID to retrieve the PriceLstGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   */  
export function get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company:string, ListCode:string, ProdCode:string, UOMCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PriceLstGroupsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PriceLstGroupsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PriceLstGroup for the service
   Description: Calls UpdateExt to update PriceLstGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company:string, ListCode:string, ProdCode:string, UOMCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", {
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
   Summary: Call UpdateExt to delete PriceLstGroup item
   Description: Call UpdateExt to delete PriceLstGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstGroup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company:string, ListCode:string, ProdCode:string, UOMCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", {
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
   Description: Get PLGrupBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLGrupBrks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLGrupBrkRow
   */  
export function get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode_PLGrupBrks(Company:string, ListCode:string, ProdCode:string, UOMCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLGrupBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLGrupBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PLGrupBrk item
   Description: Calls GetByID to retrieve the PLGrupBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLGrupBrk1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   */  
export function get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company:string, ListCode:string, ProdCode:string, UOMCode:string, Quantity:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PLGrupBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PLGrupBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PLGrupBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLGrupBrks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLGrupBrkRow
   */  
export function get_PLGrupBrks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLGrupBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLGrupBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLGrupBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PLGrupBrks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PLGrupBrk item
   Description: Calls GetByID to retrieve the PLGrupBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLGrupBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   */  
export function get_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company:string, ListCode:string, ProdCode:string, UOMCode:string, Quantity:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PLGrupBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PLGrupBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PLGrupBrk for the service
   Description: Calls UpdateExt to update PLGrupBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLGrupBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company:string, ListCode:string, ProdCode:string, UOMCode:string, Quantity:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
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
   Summary: Call UpdateExt to delete PLGrupBrk item
   Description: Call UpdateExt to delete PLGrupBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLGrupBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param ProdCode Desc: ProdCode   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company:string, ListCode:string, ProdCode:string, UOMCode:string, Quantity:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
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
   Description: Get PriceLstParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstParts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstPartsRow
   */  
export function get_PriceLstParts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PriceLstParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PriceLstPart item
   Description: Calls GetByID to retrieve the PriceLstPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   */  
export function get_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company:string, ListCode:string, PartNum:string, UOMCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PriceLstPartsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PriceLstPartsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PriceLstPart for the service
   Description: Calls UpdateExt to update PriceLstPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company:string, ListCode:string, PartNum:string, UOMCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", {
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
   Summary: Call UpdateExt to delete PriceLstPart item
   Description: Call UpdateExt to delete PriceLstPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company:string, ListCode:string, PartNum:string, UOMCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", {
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
   Description: Get PLPartBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLPartBrks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLPartBrkRow
   */  
export function get_PriceLstParts_Company_ListCode_PartNum_UOMCode_PLPartBrks(Company:string, ListCode:string, PartNum:string, UOMCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PLPartBrk item
   Description: Calls GetByID to retrieve the PLPartBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLPartBrk1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   */  
export function get_PriceLstParts_Company_ListCode_PartNum_UOMCode_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company:string, ListCode:string, PartNum:string, UOMCode:string, Quantity:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PLPartBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PLPartBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PLPartBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLPartBrks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLPartBrkRow
   */  
export function get_PLPartBrks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLPartBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PLPartBrks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PLPartBrk item
   Description: Calls GetByID to retrieve the PLPartBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLPartBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   */  
export function get_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company:string, ListCode:string, PartNum:string, UOMCode:string, Quantity:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PLPartBrkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PLPartBrkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PLPartBrk for the service
   Description: Calls UpdateExt to update PLPartBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLPartBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company:string, ListCode:string, PartNum:string, UOMCode:string, Quantity:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
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
   Summary: Call UpdateExt to delete PLPartBrk item
   Description: Call UpdateExt to delete PLPartBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLPartBrk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param Quantity Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company:string, ListCode:string, PartNum:string, UOMCode:string, Quantity:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
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
   Description: Get PriceLstAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstAttchRow
   */  
export function get_PriceLstAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PriceLstAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PriceLstAttch item
   Description: Calls GetByID to retrieve the PriceLstAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   */  
export function get_PriceLstAttches_Company_ListCode_DrawingSeq(Company:string, ListCode:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PriceLstAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PriceLstAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PriceLstAttch for the service
   Description: Calls UpdateExt to update PriceLstAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PriceLstAttches_Company_ListCode_DrawingSeq(Company:string, ListCode:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PriceLstAttch item
   Description: Call UpdateExt to delete PriceLstAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ListCode Desc: ListCode   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PriceLstAttches_Company_ListCode_DrawingSeq(Company:string, ListCode:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePriceLst:string, whereClausePriceLstAttch:string, whereClausePriceLstGroups:string, whereClausePLGrupBrk:string, whereClausePriceLstParts:string, whereClausePLPartBrk:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePriceLst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePriceLst=" + whereClausePriceLst
   }
   if(typeof whereClausePriceLstAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePriceLstAttch=" + whereClausePriceLstAttch
   }
   if(typeof whereClausePriceLstGroups!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePriceLstGroups=" + whereClausePriceLstGroups
   }
   if(typeof whereClausePLGrupBrk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePLGrupBrk=" + whereClausePLGrupBrk
   }
   if(typeof whereClausePriceLstParts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePriceLstParts=" + whereClausePriceLstParts
   }
   if(typeof whereClausePLPartBrk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePLPartBrk=" + whereClausePLPartBrk
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetRows" + params, {
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
export function get_GetByID(listCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof listCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "listCode=" + listCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetList" + params, {
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
   Summary: Invoke method BuildUOMList
   Description: Build a list of all the valid UOM's defined for all the parts within
the product group.
   OperationID: BuildUOMList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildUOMList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildUOMList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildUOMList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/BuildUOMList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartNum
   Description: Get the track multiple UOM setting when the part number changes.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/ChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangingKeyParts
   Description: Validate the entered part an UOM doesn't exist in the price list.
   OperationID: ChangingKeyParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingKeyParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingKeyParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangingKeyParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/ChangingKeyParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateUOM
   Description: Validate the sales UOM doesn't exist in the price list.
   OperationID: ValidateUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/ValidateUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListFilterPriceList
   Description: Filter parts by plant.  Call normal GetList method.
   OperationID: GetListFilterPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFilterPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFilterPriceList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetListFilterPriceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPriceLstGroupDefaults
   Description: Gets the following fields for the product group: Description.
   OperationID: GetPriceLstGroupDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceLstGroupDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceLstGroupDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPriceLstGroupDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetPriceLstGroupDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPriceLstPartsDefaults
   OperationID: GetPriceLstPartsDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceLstPartsDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceLstPartsDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPriceLstPartsDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetPriceLstPartsDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidUOM
   OperationID: ValidUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/ValidUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingFSMSendTo
   OperationID: OnChangingFSMSendTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingFSMSendTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingFSMSendTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingFSMSendTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/OnChangingFSMSendTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingEndDate
   OperationID: OnChangingEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingEndDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/OnChangingEndDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PriceLstGetValidRows
   Description: Method calls the PriceLst GetRows, then it validates if a record has been retrieved (Kinetic UI Purposes)
   OperationID: PriceLstGetValidRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PriceLstGetValidRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PriceLstGetValidRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PriceLstGetValidRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGetValidRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PLPartBrkGetRows
   Description: Get the PLPartBrk Records by ListCode ID  and PartNum
   OperationID: PLPartBrkGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PLPartBrkGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PLPartBrkGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PLPartBrkGetRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrkGetRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPriceLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPriceLst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetNewPriceLst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPriceLstAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPriceLstAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetNewPriceLstAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPriceLstGroups
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPriceLstGroups(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetNewPriceLstGroups", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPLGrupBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLGrupBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLGrupBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLGrupBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPLGrupBrk(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetNewPLGrupBrk", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPriceLstParts
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPriceLstParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetNewPriceLstParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPLPartBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLPartBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLPartBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLPartBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPLPartBrk(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetNewPLPartBrk", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLGrupBrkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PLGrupBrkRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PLPartBrkRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstGroupsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstPartsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstRow[],
}

export interface Erp_Tablesets_PLGrupBrkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique set of characters entered by the user to identify the Price List master within the company.  */  
   "ListCode":string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master.  */  
   "ProdCode":string,
      /**  The price break quantity  */  
   "Quantity":number,
      /**  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   "DiscountPercent":number,
      /**  The "Flat Unit Price" that is to be given for this price break quantity.  */  
   "UnitPrice":number,
      /**   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "UOMCode":string,
      /**  Marks this PLGrupBrk as global, available to be sent out to other companies.  */  
   "GlobalPLGrupBrk":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Value of radio button (P or D)  */  
   "RadioButtonValue":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
   "BitFlag":number,
   "ListCodeListDescription":string,
   "ProdCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PLPartBrkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Unique set of characters entered by the user to identify
the Price List master within the company.  */  
   "ListCode":string,
      /**  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  */  
   "PartNum":string,
      /**  The price break quantity  */  
   "Quantity":number,
      /**  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   "DiscountPercent":number,
      /**  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  */  
   "UnitPrice":number,
      /**   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "UOMCode":string,
      /**  Marks this PLPartBrk as global, available to be sent out to other companies.  */  
   "GlobalPLPartBrk":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Value of radio button. (D or P)  */  
   "RadioButtonValue":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
   "BitFlag":number,
   "ListCodeListDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackDimension":boolean,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Comments_c":string,
}

export interface Erp_Tablesets_PriceLstAttchRow{
   "Company":string,
   "ListCode":string,
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

export interface Erp_Tablesets_PriceLstGroupsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  PriceLst.ListCode value of the price list that this record is related to.  */  
   "ListCode":string,
      /**  ProdGrup.ProdCode value of the Product Group that this record is related to.  */  
   "ProdCode":string,
      /**  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  */  
   "BasePrice":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent1":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent2":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent3":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent4":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent5":number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak1":number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak2":number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak3":number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak4":number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak5":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice1":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice2":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice3":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice4":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice5":number,
      /**  Additional comments that will be used as a default for customer price lists.  */  
   "CommentText":string,
      /**   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "UOMCode":string,
      /**  Marks this PriceLstGroups as global, available to be sent out to other companies.  */  
   "GlobalPriceLstGroups":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Product group description  */  
   "ProdGrpDescription":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
   "BitFlag":number,
   "ListCodeListDescription":string,
   "ProdCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PriceLstListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the price list assigned by the user.  */  
   "ListCode":string,
      /**  Currency.CurrencyCode of the currency assigned to the price list.  */  
   "CurrencyCode":string,
      /**  Description of the price list.  */  
   "ListDescription":string,
      /**  Date the price list become effective.  */  
   "StartDate":string,
      /**  Date that the price list expires on.  */  
   "EndDate":string,
      /**  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  */  
   "WarehouseList":string,
      /**  Marks this PriceLst as global, available to be sent out to other companies.  */  
   "GlobalPriceLst":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  */  
   "ListType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  UseZeroPrice  */  
   "UseZeroPrice":boolean,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
   "DspWareHouseList":string,
   "WareHouseListDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PriceLstPartsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  PriceLst.ListCode value of the price list that this record is related to.  */  
   "ListCode":string,
      /**  Part.PartNum value of the Part that this record is related to.  */  
   "PartNum":string,
      /**  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  */  
   "BasePrice":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent1":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent2":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent3":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent4":number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   "DiscountPercent5":number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak1":number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak2":number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak3":number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak4":number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   "QtyBreak5":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice1":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice2":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice3":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice4":number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   "UnitPrice5":number,
      /**  Additional comments that will be used as a default for customer price lists.  */  
   "CommentText":string,
      /**   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "UOMCode":string,
      /**  Marks this PriceLstParts as global, available to be sent out to other companies.  */  
   "GlobalPriceLstParts":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Part sales unit of measure  */  
   "PartSalesUM":string,
      /**  Part selling factor  */  
   "PartSellingFactor":number,
      /**  Part price per code  */  
   "PartPricePerCode":string,
      /**  Part description  */  
   "PartDescription":string,
   "SellingFactorDirection":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
   "CurrencyCodeCurrSymbol":string,
   "BitFlag":number,
   "ListCodeListDescription":string,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PriceLstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the price list assigned by the user.  */  
   "ListCode":string,
      /**  Currency.CurrencyCode of the currency assigned to the price list.  */  
   "CurrencyCode":string,
      /**  Description of the price list.  */  
   "ListDescription":string,
      /**  Date the price list become effective.  */  
   "StartDate":string,
      /**  Date that the price list expires on.  */  
   "EndDate":string,
      /**  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  */  
   "WarehouseList":string,
      /**  Marks this PriceLst as global, available to be sent out to other companies.  */  
   "GlobalPriceLst":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  */  
   "ListType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  UseZeroPrice  */  
   "UseZeroPrice":boolean,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  List of WareHouse descriptions  */  
   "WareHouseListDescription":string,
      /**  Display Ware house list  */  
   "DspWareHouseList":string,
   "BitFlag":number,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "LinkedPriceList_c":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ProdCode
   */  
export interface BuildUOMList_input{
      /**  Order Number  */  
   ProdCode:string,
}

export interface BuildUOMList_output{
parameters : {
      /**  output parameters  */  
   UomList:string,
}
}

   /** Required : 
      @param ProposedPartNum
      @param pListCode
   */  
export interface ChangePartNum_input{
      /**  Proposed Part Number  */  
   ProposedPartNum:string,
      /**  ListCode  */  
   pListCode:string,
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   TrackMulti:boolean,
   opUOM:string,
}
}

   /** Required : 
      @param pPartNum
      @param pListCode
      @param pUOMcode
   */  
export interface ChangingKeyParts_input{
      /**  Part Number  */  
   pPartNum:string,
      /**  List Code  */  
   pListCode:string,
      /**  UOM Code  */  
   pUOMcode:string,
}

export interface ChangingKeyParts_output{
}

   /** Required : 
      @param listCode
   */  
export interface DeleteByID_input{
   listCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PLGrupBrkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique set of characters entered by the user to identify the Price List master within the company.  */  
   ListCode:string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master.  */  
   ProdCode:string,
      /**  The price break quantity  */  
   Quantity:number,
      /**  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   DiscountPercent:number,
      /**  The "Flat Unit Price" that is to be given for this price break quantity.  */  
   UnitPrice:number,
      /**   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PLGrupBrk as global, available to be sent out to other companies.  */  
   GlobalPLGrupBrk:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of radio button (P or D)  */  
   RadioButtonValue:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   BitFlag:number,
   ListCodeListDescription:string,
   ProdCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PLPartBrkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Unique set of characters entered by the user to identify
the Price List master within the company.  */  
   ListCode:string,
      /**  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  */  
   PartNum:string,
      /**  The price break quantity  */  
   Quantity:number,
      /**  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   DiscountPercent:number,
      /**  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  */  
   UnitPrice:number,
      /**   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PLPartBrk as global, available to be sent out to other companies.  */  
   GlobalPLPartBrk:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of radio button. (D or P)  */  
   RadioButtonValue:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   BitFlag:number,
   ListCodeListDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Comments_c:string,
}

export interface Erp_Tablesets_PriceLstAttchRow{
   Company:string,
   ListCode:string,
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

export interface Erp_Tablesets_PriceLstGroupsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  PriceLst.ListCode value of the price list that this record is related to.  */  
   ListCode:string,
      /**  ProdGrup.ProdCode value of the Product Group that this record is related to.  */  
   ProdCode:string,
      /**  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  */  
   BasePrice:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent1:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent2:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent3:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent4:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent5:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak1:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak2:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak3:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak4:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak5:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice1:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice2:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice3:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice4:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice5:number,
      /**  Additional comments that will be used as a default for customer price lists.  */  
   CommentText:string,
      /**   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PriceLstGroups as global, available to be sent out to other companies.  */  
   GlobalPriceLstGroups:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Product group description  */  
   ProdGrpDescription:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   BitFlag:number,
   ListCodeListDescription:string,
   ProdCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceLstListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the price list assigned by the user.  */  
   ListCode:string,
      /**  Currency.CurrencyCode of the currency assigned to the price list.  */  
   CurrencyCode:string,
      /**  Description of the price list.  */  
   ListDescription:string,
      /**  Date the price list become effective.  */  
   StartDate:string,
      /**  Date that the price list expires on.  */  
   EndDate:string,
      /**  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  */  
   WarehouseList:string,
      /**  Marks this PriceLst as global, available to be sent out to other companies.  */  
   GlobalPriceLst:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  */  
   ListType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  UseZeroPrice  */  
   UseZeroPrice:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
   DspWareHouseList:string,
   WareHouseListDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceLstListTableset{
   PriceLstList:Erp_Tablesets_PriceLstListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PriceLstPartsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  PriceLst.ListCode value of the price list that this record is related to.  */  
   ListCode:string,
      /**  Part.PartNum value of the Part that this record is related to.  */  
   PartNum:string,
      /**  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  */  
   BasePrice:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent1:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent2:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent3:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent4:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent5:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak1:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak2:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak3:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak4:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak5:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice1:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice2:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice3:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice4:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice5:number,
      /**  Additional comments that will be used as a default for customer price lists.  */  
   CommentText:string,
      /**   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PriceLstParts as global, available to be sent out to other companies.  */  
   GlobalPriceLstParts:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Part sales unit of measure  */  
   PartSalesUM:string,
      /**  Part selling factor  */  
   PartSellingFactor:number,
      /**  Part price per code  */  
   PartPricePerCode:string,
      /**  Part description  */  
   PartDescription:string,
   SellingFactorDirection:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   CurrencyCodeCurrSymbol:string,
   BitFlag:number,
   ListCodeListDescription:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceLstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the price list assigned by the user.  */  
   ListCode:string,
      /**  Currency.CurrencyCode of the currency assigned to the price list.  */  
   CurrencyCode:string,
      /**  Description of the price list.  */  
   ListDescription:string,
      /**  Date the price list become effective.  */  
   StartDate:string,
      /**  Date that the price list expires on.  */  
   EndDate:string,
      /**  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  */  
   WarehouseList:string,
      /**  Marks this PriceLst as global, available to be sent out to other companies.  */  
   GlobalPriceLst:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  */  
   ListType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  UseZeroPrice  */  
   UseZeroPrice:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  List of WareHouse descriptions  */  
   WareHouseListDescription:string,
      /**  Display Ware house list  */  
   DspWareHouseList:string,
   BitFlag:number,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   LinkedPriceList_c:string,
}

export interface Erp_Tablesets_PriceLstTableset{
   PriceLst:Erp_Tablesets_PriceLstRow[],
   PriceLstAttch:Erp_Tablesets_PriceLstAttchRow[],
   PriceLstGroups:Erp_Tablesets_PriceLstGroupsRow[],
   PLGrupBrk:Erp_Tablesets_PLGrupBrkRow[],
   PriceLstParts:Erp_Tablesets_PriceLstPartsRow[],
   PLPartBrk:Erp_Tablesets_PLPartBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPriceLstTableset{
   PriceLst:Erp_Tablesets_PriceLstRow[],
   PriceLstAttch:Erp_Tablesets_PriceLstAttchRow[],
   PriceLstGroups:Erp_Tablesets_PriceLstGroupsRow[],
   PLGrupBrk:Erp_Tablesets_PLGrupBrkRow[],
   PriceLstParts:Erp_Tablesets_PriceLstPartsRow[],
   PLPartBrk:Erp_Tablesets_PLPartBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param listCode
   */  
export interface GetByID_input{
   listCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PriceLstTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PriceLstTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PriceLstTableset[],
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
      @param OrderNum
      @param OrderLine
      @param PartNum
      @param ProdCode
      @param WhereClause
      @param PageSize
      @param AbsolutePage
   */  
export interface GetListFilterPriceList_input{
      /**  Order Number.  */  
   OrderNum:number,
      /**  Order Line.  */  
   OrderLine:number,
      /**  Part Number.  */  
   PartNum:string,
      /**  Product Code.  */  
   ProdCode:string,
      /**  Whereclause.  */  
   WhereClause:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
}

export interface GetListFilterPriceList_output{
   returnObj:Erp_Tablesets_PriceLstListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
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
   returnObj:Erp_Tablesets_PriceLstListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param listCode
      @param prodCode
      @param uoMCode
   */  
export interface GetNewPLGrupBrk_input{
   ds:Erp_Tablesets_PriceLstTableset[],
   listCode:string,
   prodCode:string,
   uoMCode:string,
}

export interface GetNewPLGrupBrk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param ds
      @param listCode
      @param partNum
      @param uoMCode
   */  
export interface GetNewPLPartBrk_input{
   ds:Erp_Tablesets_PriceLstTableset[],
   listCode:string,
   partNum:string,
   uoMCode:string,
}

export interface GetNewPLPartBrk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param ds
      @param listCode
   */  
export interface GetNewPriceLstAttch_input{
   ds:Erp_Tablesets_PriceLstTableset[],
   listCode:string,
}

export interface GetNewPriceLstAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param ds
      @param listCode
      @param prodCode
   */  
export interface GetNewPriceLstGroups_input{
   ds:Erp_Tablesets_PriceLstTableset[],
   listCode:string,
   prodCode:string,
}

export interface GetNewPriceLstGroups_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param ds
      @param listCode
      @param partNum
   */  
export interface GetNewPriceLstParts_input{
   ds:Erp_Tablesets_PriceLstTableset[],
   listCode:string,
   partNum:string,
}

export interface GetNewPriceLstParts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPriceLst_input{
   ds:Erp_Tablesets_PriceLstTableset[],
}

export interface GetNewPriceLst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param ProdCode
   */  
export interface GetPriceLstGroupDefaults_input{
      /**  Product group code to retrieve details for.  */  
   ProdCode:string,
}

export interface GetPriceLstGroupDefaults_output{
parameters : {
      /**  output parameters  */  
   ProdGrpDescription:string,
}
}

   /** Required : 
      @param PartNum
   */  
export interface GetPriceLstPartsDefaults_input{
   PartNum:string,
}

export interface GetPriceLstPartsDefaults_output{
parameters : {
      /**  output parameters  */  
   PartNum:string,
   SalesUM:string,
   SellingFactor:number,
   PricePerCode:string,
   PartDescription:string,
   SellingFactorDirection:string,
}
}

   /** Required : 
      @param whereClausePriceLst
      @param whereClausePriceLstAttch
      @param whereClausePriceLstGroups
      @param whereClausePLGrupBrk
      @param whereClausePriceLstParts
      @param whereClausePLPartBrk
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePriceLst:string,
   whereClausePriceLstAttch:string,
   whereClausePriceLstGroups:string,
   whereClausePLGrupBrk:string,
   whereClausePriceLstParts:string,
   whereClausePLPartBrk:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PriceLstTableset[],
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
      @param endDate
      @param ds
   */  
export interface OnChangingEndDate_input{
   endDate:string,
   ds:Erp_Tablesets_PriceLstTableset[],
}

export interface OnChangingEndDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param fsmSendTo
      @param ds
   */  
export interface OnChangingFSMSendTo_input{
   fsmSendTo:boolean,
   ds:Erp_Tablesets_PriceLstTableset[],
}

export interface OnChangingFSMSendTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param ListCode
      @param PartNum
      @param ds
   */  
export interface PLPartBrkGetRows_input{
   ListCode:string,
   PartNum:string,
   ds:Erp_Tablesets_PriceLstTableset[],
}

export interface PLPartBrkGetRows_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param whereClausePriceLst
      @param whereClausePriceLstAttch
      @param whereClausePriceLstGroups
      @param whereClausePLGrupBrk
      @param whereClausePriceLstParts
      @param whereClausePLPartBrk
      @param pageSize
      @param absolutePage
   */  
export interface PriceLstGetValidRows_input{
   whereClausePriceLst:string,
   whereClausePriceLstAttch:string,
   whereClausePriceLstGroups:string,
   whereClausePLGrupBrk:string,
   whereClausePriceLstParts:string,
   whereClausePLPartBrk:string,
   pageSize:number,
   absolutePage:number,
}

export interface PriceLstGetValidRows_output{
   returnObj:Erp_Tablesets_PriceLstTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPriceLstTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPriceLstTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PriceLstTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstTableset[],
}
}

   /** Required : 
      @param prodGroup
      @param iPartNum
      @param iUOM
   */  
export interface ValidUOM_input{
   prodGroup:string,
   iPartNum:string,
   iUOM:string,
}

export interface ValidUOM_output{
   returnObj:boolean,
}

   /** Required : 
      @param pPartNum
      @param pListCode
      @param pUOMcode
   */  
export interface ValidateUOM_input{
      /**  Part Number  */  
   pPartNum:string,
      /**  List Code  */  
   pListCode:string,
      /**  UOM Code  */  
   pUOMcode:string,
}

export interface ValidateUOM_output{
   returnObj:boolean,
}

