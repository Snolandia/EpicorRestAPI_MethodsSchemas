import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PriceLstGroupsSvc
// Description: The PriceLstGroups Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/$metadata", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstGroupsListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePriceLstGroups:string, whereClausePLGrupBrk:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(listCode:string, prodCode:string, uoMCode:string, epicorHeaders?:Headers){
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
   if(typeof prodCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "prodCode=" + prodCode
   }
   if(typeof uoMCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "uoMCode=" + uoMCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetList" + params, {
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
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the PriceLstGroups records which will be a subset
of the PriceLstGroups records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFromSelectedKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetListFromSelectedKeys", {
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
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the PriceLstGroups records which will be a subset
of the PriceLstGroups records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromSelectedKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetRowsFromSelectedKeys", {
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
   Summary: Invoke method GetCurrencyCode
   OperationID: GetCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetCurrencyCode", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetNewPriceLstGroups", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetNewPLGrupBrk", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/UpdateExt", {
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

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstGroupsListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstGroupsRow[],
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

export interface Erp_Tablesets_PriceLstGroupsListRow{
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
      /**  Description of the price list.  */  
   "ListCodeListDescription":string,
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
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




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param listCode
      @param prodCode
      @param uoMCode
   */  
export interface DeleteByID_input{
   listCode:string,
   prodCode:string,
   uoMCode:string,
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

export interface Erp_Tablesets_PriceLstGroupsListRow{
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
      /**  Description of the price list.  */  
   ListCodeListDescription:string,
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceLstGroupsListTableset{
   PriceLstGroupsList:Erp_Tablesets_PriceLstGroupsListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_PriceLstGroupsTableset{
   PriceLstGroups:Erp_Tablesets_PriceLstGroupsRow[],
   PLGrupBrk:Erp_Tablesets_PLGrupBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPriceLstGroupsTableset{
   PriceLstGroups:Erp_Tablesets_PriceLstGroupsRow[],
   PLGrupBrk:Erp_Tablesets_PLGrupBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param listCode
      @param prodCode
      @param uoMCode
   */  
export interface GetByID_input{
   listCode:string,
   prodCode:string,
   uoMCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PriceLstGroupsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PriceLstGroupsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PriceLstGroupsTableset[],
}

   /** Required : 
      @param ipListCode
   */  
export interface GetCurrencyCode_input{
   ipListCode:string,
}

export interface GetCurrencyCode_output{
   returnObj:string,
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetListFromSelectedKeys_input{
   ds:Erp_Tablesets_PriceLstGroupsListTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetListFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstGroupsListTableset[],
   morePages:boolean,
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
   returnObj:Erp_Tablesets_PriceLstGroupsListTableset[],
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
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
   listCode:string,
   prodCode:string,
   uoMCode:string,
}

export interface GetNewPLGrupBrk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
}
}

   /** Required : 
      @param ds
      @param listCode
      @param prodCode
   */  
export interface GetNewPriceLstGroups_input{
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
   listCode:string,
   prodCode:string,
}

export interface GetNewPriceLstGroups_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsFromSelectedKeys_input{
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRowsFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePriceLstGroups
      @param whereClausePLGrupBrk
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePriceLstGroups:string,
   whereClausePLGrupBrk:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PriceLstGroupsTableset[],
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
   ds:Erp_Tablesets_UpdExtPriceLstGroupsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPriceLstGroupsTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstGroupsTableset[],
}
}

