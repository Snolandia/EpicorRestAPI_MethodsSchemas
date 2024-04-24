import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PriceLstPartsSvc
// Description: The PriceLstParts Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/$metadata", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstPartsListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsListRow)
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
export function get_GetRows(whereClausePriceLstParts:string, whereClausePLPartBrk:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetRows" + params, {
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
export function get_GetByID(listCode:string, partNum:string, uoMCode:string, epicorHeaders?:Headers){
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
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetList" + params, {
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
   Description: This methods will return all of the PriceLstParts records which will be a subset
of the PriceLstParts records that meet the selection criteria.  This method will try
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetListFromSelectedKeys", {
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
   Description: This methods will return all of the PriceLstParts records which will be a subset
of the PriceLstParts records that meet the selection criteria.  This method will try
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetRowsFromSelectedKeys", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetCurrencyCode", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetNewPriceLstParts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetNewPLPartBrk", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PLPartBrkRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstPartsListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PriceLstPartsRow[],
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

export interface Erp_Tablesets_PriceLstPartsListRow{
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
      /**  Description of the price list.  */  
   "ListCodeListDescription":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
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




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param listCode
      @param partNum
      @param uoMCode
   */  
export interface DeleteByID_input{
   listCode:string,
   partNum:string,
   uoMCode:string,
}

export interface DeleteByID_output{
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

export interface Erp_Tablesets_PriceLstPartsListRow{
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
      /**  Description of the price list.  */  
   ListCodeListDescription:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceLstPartsListTableset{
   PriceLstPartsList:Erp_Tablesets_PriceLstPartsListRow[],
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

export interface Erp_Tablesets_PriceLstPartsTableset{
   PriceLstParts:Erp_Tablesets_PriceLstPartsRow[],
   PLPartBrk:Erp_Tablesets_PLPartBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPriceLstPartsTableset{
   PriceLstParts:Erp_Tablesets_PriceLstPartsRow[],
   PLPartBrk:Erp_Tablesets_PLPartBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param listCode
      @param partNum
      @param uoMCode
   */  
export interface GetByID_input{
   listCode:string,
   partNum:string,
   uoMCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PriceLstPartsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PriceLstPartsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PriceLstPartsTableset[],
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
   ds:Erp_Tablesets_PriceLstPartsListTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetListFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstPartsListTableset[],
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
   returnObj:Erp_Tablesets_PriceLstPartsListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param listCode
      @param partNum
      @param uoMCode
   */  
export interface GetNewPLPartBrk_input{
   ds:Erp_Tablesets_PriceLstPartsTableset[],
   listCode:string,
   partNum:string,
   uoMCode:string,
}

export interface GetNewPLPartBrk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstPartsTableset[],
}
}

   /** Required : 
      @param ds
      @param listCode
      @param partNum
   */  
export interface GetNewPriceLstParts_input{
   ds:Erp_Tablesets_PriceLstPartsTableset[],
   listCode:string,
   partNum:string,
}

export interface GetNewPriceLstParts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstPartsTableset[],
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsFromSelectedKeys_input{
   ds:Erp_Tablesets_PriceLstPartsTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRowsFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstPartsTableset[],
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePriceLstParts
      @param whereClausePLPartBrk
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePriceLstParts:string,
   whereClausePLPartBrk:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PriceLstPartsTableset[],
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
   ds:Erp_Tablesets_UpdExtPriceLstPartsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPriceLstPartsTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PriceLstPartsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceLstPartsTableset[],
}
}

