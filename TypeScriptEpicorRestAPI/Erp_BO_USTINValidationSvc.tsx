import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.USTINValidationSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/$metadata", {
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
   Description: Get USTINValidations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationRow
   */  
export function get_USTINValidations(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_USTINValidations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations", {
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
   Summary: Calls GetByID to retrieve the USTINValidation item
   Description: Calls GetByID to retrieve the USTINValidation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
   */  
export function get_USTINValidations_Company_TINValidationID(Company:string, TINValidationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_USTINValidationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_USTINValidationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update USTINValidation for the service
   Description: Calls UpdateExt to update USTINValidation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_USTINValidations_Company_TINValidationID(Company:string, TINValidationID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")", {
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
   Summary: Call UpdateExt to delete USTINValidation item
   Description: Call UpdateExt to delete USTINValidation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_USTINValidations_Company_TINValidationID(Company:string, TINValidationID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")", {
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
   Description: Get USTINValidationVendors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_USTINValidationVendors1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationVendorRow
   */  
export function get_USTINValidations_Company_TINValidationID_USTINValidationVendors(Company:string, TINValidationID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationVendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationVendors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationVendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the USTINValidationVendor item
   Description: Calls GetByID to retrieve the USTINValidationVendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationVendor1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   */  
export function get_USTINValidations_Company_TINValidationID_USTINValidationVendors_Company_TINValidationID_VendorNum(Company:string, TINValidationID:string, VendorNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_USTINValidationVendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_USTINValidationVendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get USTINValidationAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_USTINValidationAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationAttchRow
   */  
export function get_USTINValidations_Company_TINValidationID_USTINValidationAttches(Company:string, TINValidationID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the USTINValidationAttch item
   Description: Calls GetByID to retrieve the USTINValidationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   */  
export function get_USTINValidations_Company_TINValidationID_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company:string, TINValidationID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_USTINValidationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_USTINValidationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get USTINValidationVendors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidationVendors
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationVendorRow
   */  
export function get_USTINValidationVendors(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationVendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationVendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidationVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_USTINValidationVendors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors", {
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
   Summary: Calls GetByID to retrieve the USTINValidationVendor item
   Description: Calls GetByID to retrieve the USTINValidationVendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationVendor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   */  
export function get_USTINValidationVendors_Company_TINValidationID_VendorNum(Company:string, TINValidationID:string, VendorNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_USTINValidationVendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_USTINValidationVendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update USTINValidationVendor for the service
   Description: Calls UpdateExt to update USTINValidationVendor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidationVendor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_USTINValidationVendors_Company_TINValidationID_VendorNum(Company:string, TINValidationID:string, VendorNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")", {
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
   Summary: Call UpdateExt to delete USTINValidationVendor item
   Description: Call UpdateExt to delete USTINValidationVendor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidationVendor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_USTINValidationVendors_Company_TINValidationID_VendorNum(Company:string, TINValidationID:string, VendorNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")", {
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
   Description: Get USTINValidationAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidationAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationAttchRow
   */  
export function get_USTINValidationAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidationAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_USTINValidationAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches", {
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
   Summary: Calls GetByID to retrieve the USTINValidationAttch item
   Description: Calls GetByID to retrieve the USTINValidationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   */  
export function get_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company:string, TINValidationID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_USTINValidationAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_USTINValidationAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update USTINValidationAttch for the service
   Description: Calls UpdateExt to update USTINValidationAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidationAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company:string, TINValidationID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete USTINValidationAttch item
   Description: Call UpdateExt to delete USTINValidationAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidationAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TINValidationID Desc: TINValidationID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company:string, TINValidationID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationListRow)
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
export function get_GetRows(whereClauseUSTINValidation:string, whereClauseUSTINValidationAttch:string, whereClauseUSTINValidationVendor:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseUSTINValidation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUSTINValidation=" + whereClauseUSTINValidation
   }
   if(typeof whereClauseUSTINValidationAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUSTINValidationAttch=" + whereClauseUSTINValidationAttch
   }
   if(typeof whereClauseUSTINValidationVendor!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUSTINValidationVendor=" + whereClauseUSTINValidationVendor
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetRows" + params, {
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
export function get_GetByID(tiNValidationID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tiNValidationID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tiNValidationID=" + tiNValidationID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetList" + params, {
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
   Summary: Invoke method RemoveUSTINValidationVendors
   OperationID: RemoveUSTINValidationVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveUSTINValidationVendors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveUSTINValidationVendors_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveUSTINValidationVendors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/RemoveUSTINValidationVendors", {
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
   Summary: Invoke method GetDescriptionList
   Description: Get Description list for field
   OperationID: GetDescriptionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDescriptionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDescriptionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDescriptionList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetDescriptionList", {
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
   Summary: Invoke method GenExportFile
   Description: Generate Export File for TIN Validation
   OperationID: GenExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenExportFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GenExportFile", {
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
   Summary: Invoke method CancelExport
   Description: Cancel Export
   OperationID: CancelExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelExport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/CancelExport", {
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
   Summary: Invoke method LookupVendor
   Description: Lookup Vendor
   OperationID: LookupVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookupVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookupVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LookupVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/LookupVendor", {
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
   Summary: Invoke method UpdateUSTINValidationVendor
   Description: Update USTINValidationVendor table. Standard update not worked for keyed field
   OperationID: UpdateUSTINValidationVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateUSTINValidationVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateUSTINValidationVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateUSTINValidationVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/UpdateUSTINValidationVendor", {
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
   Summary: Invoke method CheckVendor
   Description: CheckVendor
   OperationID: CheckVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/CheckVendor", {
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
   Summary: Invoke method MarkAsSubmitted
   Description: Mark valiation as submitted
   OperationID: MarkAsSubmitted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkAsSubmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkAsSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MarkAsSubmitted(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/MarkAsSubmitted", {
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
   Summary: Invoke method AddUSTINValidationVendors
   OperationID: AddUSTINValidationVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUSTINValidationVendors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUSTINValidationVendors_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUSTINValidationVendors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/AddUSTINValidationVendors", {
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
   Summary: Invoke method GetNewUSTINValidation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUSTINValidation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetNewUSTINValidation", {
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
   Summary: Invoke method GetNewUSTINValidationAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidationAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidationAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidationAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUSTINValidationAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetNewUSTINValidationAttch", {
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
   Summary: Invoke method GetNewUSTINValidationVendor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidationVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidationVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidationVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUSTINValidationVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetNewUSTINValidationVendor", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_USTINValidationAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_USTINValidationListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationRow{
   "odatametadata":string,
   "value":Erp_Tablesets_USTINValidationRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationVendorRow{
   "odatametadata":string,
   "value":Erp_Tablesets_USTINValidationVendorRow[],
}

export interface Erp_Tablesets_USTINValidationAttchRow{
   "Company":string,
   "TINValidationID":string,
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

export interface Erp_Tablesets_USTINValidationListRow{
      /**  Company  */  
   "Company":string,
      /**  TIN Validation ID  */  
   "TINValidationID":string,
      /**  Description  */  
   "Description":string,
      /**  Export File  */  
   "ExportFile":string,
      /**  Submitted  */  
   "Submitted":boolean,
      /**  Exported  */  
   "Exported":boolean,
      /**  Tracking Number  */  
   "TrackingNumber":string,
      /**  Result Received  */  
   "ResultReceived":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_USTINValidationRow{
      /**  Company  */  
   "Company":string,
      /**  TIN Validation ID  */  
   "TINValidationID":string,
      /**  Description  */  
   "Description":string,
      /**  EFTHeadUID  */  
   "EFTHeadUID":number,
      /**  Export File  */  
   "ExportFile":string,
      /**  Submitted  */  
   "Submitted":boolean,
      /**  Exported  */  
   "Exported":boolean,
      /**  Include Valid Status New  */  
   "IncludeValidStatusNew":boolean,
      /**  Include Valid Status Invalid  */  
   "IncludeValidStatusInvalid":boolean,
      /**  Include Valid Status Pending  */  
   "IncludeValidStatusPending":boolean,
      /**  Include Valid Status Matched  */  
   "IncludeValidStatusMatched":boolean,
      /**  Tracking Number  */  
   "TrackingNumber":string,
      /**  Result Received  */  
   "ResultReceived":boolean,
      /**  Created By  */  
   "CreatedBy":string,
      /**  Created On  */  
   "CreatedOn":string,
      /**  Changed By  */  
   "ChangedBy":string,
      /**  Changed On  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "ValidationResultsDescription":string,
   "ValidationResultsID":string,
   "ExportFileNameDisplay":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_USTINValidationVendorRow{
      /**  Company  */  
   "Company":string,
      /**  TINValidationID  */  
   "TINValidationID":string,
      /**  VendorNum  */  
   "VendorNum":number,
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
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "City":string,
   "Country":string,
   "Inactive":boolean,
   "Name":string,
   "PayHold":boolean,
   "PhoneNum":string,
   "State":string,
   "TaxPayerID":string,
   "TIN":string,
   "TINType":string,
   "VendorID":string,
   "ZIP":string,
   "TINValidationStatus":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param tinValidationID
      @param vendorNumList
      @param vendorIDList
   */  
export interface AddUSTINValidationVendors_input{
   tinValidationID:string,
   vendorNumList:string,
   vendorIDList:string,
}

export interface AddUSTINValidationVendors_output{
   returnObj:Erp_Tablesets_USTINValidationTableset[],
}

   /** Required : 
      @param tinValidationID
   */  
export interface CancelExport_input{
   tinValidationID:string,
}

export interface CancelExport_output{
parameters : {
      /**  output parameters  */  
   errMessage:string,
}
}

   /** Required : 
      @param tinValidationID
      @param vendorID
   */  
export interface CheckVendor_input{
   tinValidationID:string,
   vendorID:string,
}

export interface CheckVendor_output{
   returnObj:boolean,
}

   /** Required : 
      @param tiNValidationID
   */  
export interface DeleteByID_input{
   tiNValidationID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_USTINValidationAttchRow{
   Company:string,
   TINValidationID:string,
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

export interface Erp_Tablesets_USTINValidationListRow{
      /**  Company  */  
   Company:string,
      /**  TIN Validation ID  */  
   TINValidationID:string,
      /**  Description  */  
   Description:string,
      /**  Export File  */  
   ExportFile:string,
      /**  Submitted  */  
   Submitted:boolean,
      /**  Exported  */  
   Exported:boolean,
      /**  Tracking Number  */  
   TrackingNumber:string,
      /**  Result Received  */  
   ResultReceived:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_USTINValidationListTableset{
   USTINValidationList:Erp_Tablesets_USTINValidationListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_USTINValidationRow{
      /**  Company  */  
   Company:string,
      /**  TIN Validation ID  */  
   TINValidationID:string,
      /**  Description  */  
   Description:string,
      /**  EFTHeadUID  */  
   EFTHeadUID:number,
      /**  Export File  */  
   ExportFile:string,
      /**  Submitted  */  
   Submitted:boolean,
      /**  Exported  */  
   Exported:boolean,
      /**  Include Valid Status New  */  
   IncludeValidStatusNew:boolean,
      /**  Include Valid Status Invalid  */  
   IncludeValidStatusInvalid:boolean,
      /**  Include Valid Status Pending  */  
   IncludeValidStatusPending:boolean,
      /**  Include Valid Status Matched  */  
   IncludeValidStatusMatched:boolean,
      /**  Tracking Number  */  
   TrackingNumber:string,
      /**  Result Received  */  
   ResultReceived:boolean,
      /**  Created By  */  
   CreatedBy:string,
      /**  Created On  */  
   CreatedOn:string,
      /**  Changed By  */  
   ChangedBy:string,
      /**  Changed On  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   ValidationResultsDescription:string,
   ValidationResultsID:string,
   ExportFileNameDisplay:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_USTINValidationTableset{
   USTINValidation:Erp_Tablesets_USTINValidationRow[],
   USTINValidationAttch:Erp_Tablesets_USTINValidationAttchRow[],
   USTINValidationVendor:Erp_Tablesets_USTINValidationVendorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_USTINValidationVendorRow{
      /**  Company  */  
   Company:string,
      /**  TINValidationID  */  
   TINValidationID:string,
      /**  VendorNum  */  
   VendorNum:number,
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
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
   Country:string,
   Inactive:boolean,
   Name:string,
   PayHold:boolean,
   PhoneNum:string,
   State:string,
   TaxPayerID:string,
   TIN:string,
   TINType:string,
   VendorID:string,
   ZIP:string,
   TINValidationStatus:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtUSTINValidationTableset{
   USTINValidation:Erp_Tablesets_USTINValidationRow[],
   USTINValidationAttch:Erp_Tablesets_USTINValidationAttchRow[],
   USTINValidationVendor:Erp_Tablesets_USTINValidationVendorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param tinValidationID
      @param eftHeadUID
      @param exportFileName
   */  
export interface GenExportFile_input{
      /**  Report ID  */  
   tinValidationID:string,
      /**  Electronic Interface ID  */  
   eftHeadUID:number,
      /**  Export File Name  */  
   exportFileName:string,
}

export interface GenExportFile_output{
      /**  Generated File Name  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   opMessage:string,
   CountRecordsExported:number,
}
}

   /** Required : 
      @param tiNValidationID
   */  
export interface GetByID_input{
   tiNValidationID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_USTINValidationTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_USTINValidationTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_USTINValidationTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetDescriptionList_input{
   tableName:string,
   fieldName:string,
}

export interface GetDescriptionList_output{
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
   returnObj:Erp_Tablesets_USTINValidationListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param tiNValidationID
   */  
export interface GetNewUSTINValidationAttch_input{
   ds:Erp_Tablesets_USTINValidationTableset[],
   tiNValidationID:string,
}

export interface GetNewUSTINValidationAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_USTINValidationTableset[],
}
}

   /** Required : 
      @param ds
      @param tiNValidationID
   */  
export interface GetNewUSTINValidationVendor_input{
   ds:Erp_Tablesets_USTINValidationTableset[],
   tiNValidationID:string,
}

export interface GetNewUSTINValidationVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_USTINValidationTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewUSTINValidation_input{
   ds:Erp_Tablesets_USTINValidationTableset[],
}

export interface GetNewUSTINValidation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_USTINValidationTableset[],
}
}

   /** Required : 
      @param whereClauseUSTINValidation
      @param whereClauseUSTINValidationAttch
      @param whereClauseUSTINValidationVendor
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseUSTINValidation:string,
   whereClauseUSTINValidationAttch:string,
   whereClauseUSTINValidationVendor:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_USTINValidationTableset[],
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
      @param tinValidationID
      @param vendorID
      @param ds
   */  
export interface LookupVendor_input{
   tinValidationID:string,
   vendorID:string,
   ds:Erp_Tablesets_USTINValidationTableset[],
}

export interface LookupVendor_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_USTINValidationTableset[],
}
}

   /** Required : 
      @param tinValidationID
   */  
export interface MarkAsSubmitted_input{
   tinValidationID:string,
}

export interface MarkAsSubmitted_output{
}

   /** Required : 
      @param tinValidationID
   */  
export interface RemoveUSTINValidationVendors_input{
   tinValidationID:string,
}

export interface RemoveUSTINValidationVendors_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtUSTINValidationTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtUSTINValidationTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateUSTINValidationVendor_input{
   ds:Erp_Tablesets_USTINValidationTableset[],
}

export interface UpdateUSTINValidationVendor_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_USTINValidationTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_USTINValidationTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_USTINValidationTableset[],
}
}

