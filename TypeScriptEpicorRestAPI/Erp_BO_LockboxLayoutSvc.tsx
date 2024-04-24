import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.LockboxLayoutSvc
// Description: Main BO for Lockbox Layout UI.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/$metadata", {
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
   Description: Get LockboxLayouts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LockboxLayouts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutHeadRow
   */  
export function get_LockboxLayouts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LockboxLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockboxLayouts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts", {
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
   Summary: Calls GetByID to retrieve the LockboxLayout item
   Description: Calls GetByID to retrieve the LockboxLayout item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LockboxLayout
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
   */  
export function get_LockboxLayouts_Company_LayoutID(Company:string, LayoutID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LockboxLayoutHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LockboxLayoutHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LockboxLayout for the service
   Description: Calls UpdateExt to update LockboxLayout. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LockboxLayout
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LockboxLayouts_Company_LayoutID(Company:string, LayoutID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")", {
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
   Summary: Call UpdateExt to delete LockboxLayout item
   Description: Call UpdateExt to delete LockboxLayout item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LockboxLayout
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LockboxLayouts_Company_LayoutID(Company:string, LayoutID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")", {
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
   Description: Get LockboxLayoutDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LockboxLayoutDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutDtlRow
   */  
export function get_LockboxLayouts_Company_LayoutID_LockboxLayoutDtls(Company:string, LayoutID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")/LockboxLayoutDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LockboxLayoutDtl item
   Description: Calls GetByID to retrieve the LockboxLayoutDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LockboxLayoutDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      @param RecordTypeID Desc: RecordTypeID   Required: True   Allow empty value : True
      @param FieldID Desc: FieldID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   */  
export function get_LockboxLayouts_Company_LayoutID_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company:string, LayoutID:string, RecordTypeID:string, FieldID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LockboxLayoutDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LockboxLayoutDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LockboxLayoutDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LockboxLayoutDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutDtlRow
   */  
export function get_LockboxLayoutDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LockboxLayoutDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockboxLayoutDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls", {
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
   Summary: Calls GetByID to retrieve the LockboxLayoutDtl item
   Description: Calls GetByID to retrieve the LockboxLayoutDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LockboxLayoutDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      @param RecordTypeID Desc: RecordTypeID   Required: True   Allow empty value : True
      @param FieldID Desc: FieldID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   */  
export function get_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company:string, LayoutID:string, RecordTypeID:string, FieldID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LockboxLayoutDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LockboxLayoutDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LockboxLayoutDtl for the service
   Description: Calls UpdateExt to update LockboxLayoutDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LockboxLayoutDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      @param RecordTypeID Desc: RecordTypeID   Required: True   Allow empty value : True
      @param FieldID Desc: FieldID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company:string, LayoutID:string, RecordTypeID:string, FieldID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")", {
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
   Summary: Call UpdateExt to delete LockboxLayoutDtl item
   Description: Call UpdateExt to delete LockboxLayoutDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LockboxLayoutDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      @param RecordTypeID Desc: RecordTypeID   Required: True   Allow empty value : True
      @param FieldID Desc: FieldID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company:string, LayoutID:string, RecordTypeID:string, FieldID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadListRow)
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
export function get_GetRows(whereClauseLockboxLayoutHead:string, whereClauseLockboxLayoutDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLockboxLayoutHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLockboxLayoutHead=" + whereClauseLockboxLayoutHead
   }
   if(typeof whereClauseLockboxLayoutDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLockboxLayoutDtl=" + whereClauseLockboxLayoutDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/GetRows" + params, {
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
export function get_GetByID(layoutID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof layoutID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "layoutID=" + layoutID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/GetList" + params, {
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
   Summary: Invoke method OnReadyToUseChange
   Description: This method is called when the layout is set as Ready
   OperationID: OnReadyToUseChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnReadyToUseChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnReadyToUseChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnReadyToUseChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/OnReadyToUseChange", {
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
   Summary: Invoke method GetNewLockboxLayoutHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLockboxLayoutHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLockboxLayoutHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLockboxLayoutHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLockboxLayoutHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/GetNewLockboxLayoutHead", {
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
   Summary: Invoke method GetNewLockboxLayoutDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLockboxLayoutDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLockboxLayoutDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLockboxLayoutDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLockboxLayoutDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/GetNewLockboxLayoutDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LockboxLayoutDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LockboxLayoutHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LockboxLayoutHeadRow[],
}

export interface Erp_Tablesets_LockboxLayoutDtlRow{
      /**  Company  */  
   "Company":string,
      /**  Read-only Layout ID  */  
   "LayoutID":string,
      /**  Value for record type selection  */  
   "RecordTypeID":string,
      /**  Read-only Field ID for field selection  */  
   "FieldID":string,
      /**  The position in the Lockbox record where the field data starts.  */  
   "Offset":number,
      /**  Default is zero. Available are positive values not exceeding length of record.  */  
   "Length":number,
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
      /**   Ending position within the record string.
This is the sum of offset and length.  */  
   "EndingPos":number,
      /**  This field will show the format for the given field.  */  
   "FieldFormat":string,
   "BitFlag":number,
   "LayoutFldSchemaName":string,
   "LayoutFldTableName":string,
   "LayoutFldColumnName":string,
   "LayoutFldFieldName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LockboxLayoutHeadListRow{
      /**  Company  */  
   "Company":string,
      /**  Initiates Lockbox Layout ID search.  */  
   "LayoutID":string,
      /**  Layout Description  */  
   "LayoutDescription":string,
      /**  Number of decimals in amount, acceptable values 0 to 3, Default is 2  */  
   "DecPointPos":number,
      /**  Indicates that the Layout is ready to be used in Lockbox Processing.  */  
   "ReadyToUse":boolean,
      /**  Default value  is ‘YYMMDD’ User can enter any value.  */  
   "DateFormat":string,
      /**  Identifies if ‘postable’ Cash Receipt group is posted.  */  
   "AutoPost":boolean,
      /**  Depreciated  */  
   "UnderPayAutoPost":boolean,
      /**  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  */  
   "ValidateTotals":boolean,
      /**  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  */  
   "ErrorBatchDiscard":boolean,
      /**  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  */  
   "AllowOnAcc":boolean,
      /**  Determine if lockbox should automatically accept an invoice payment with errors into the customer’s account, allowing the payment to be processed into the system without manual intervention.  */  
   "OnInvoiceErrorSetOnAcc":boolean,
      /**  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  */  
   "AllowOverpayOnAcc":boolean,
      /**  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  */  
   "AllowOverpaidInv":boolean,
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

export interface Erp_Tablesets_LockboxLayoutHeadRow{
      /**  Company  */  
   "Company":string,
      /**  Initiates Lockbox Layout ID search.  */  
   "LayoutID":string,
      /**  Layout Description  */  
   "LayoutDescription":string,
      /**  Number of decimals in amount, acceptable values 0 to 3, Default is 2  */  
   "DecPointPos":number,
      /**  Indicates that the Layout is ready to be used in Lockbox Processing.  */  
   "ReadyToUse":boolean,
      /**  Default value  is ‘YYMMDD’ User can enter any value.  */  
   "DateFormat":string,
      /**  Identifies if ‘postable’ Cash Receipt group is posted.  */  
   "AutoPost":boolean,
      /**  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  */  
   "ValidateTotals":boolean,
      /**  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  */  
   "ErrorBatchDiscard":boolean,
      /**  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  */  
   "AllowOnAcc":boolean,
      /**  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  */  
   "AllowOverpayOnAcc":boolean,
      /**  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  */  
   "AllowOverpaidInv":boolean,
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
   "RecordTypeID":string,
      /**  Location of the file to test the layout.  */  
   "TestFile":string,
   "BitFlag":number,
   "ARSystAllowOverpaidInv":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param layoutID
   */  
export interface DeleteByID_input{
   layoutID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_LockboxLayoutDtlRow{
      /**  Company  */  
   Company:string,
      /**  Read-only Layout ID  */  
   LayoutID:string,
      /**  Value for record type selection  */  
   RecordTypeID:string,
      /**  Read-only Field ID for field selection  */  
   FieldID:string,
      /**  The position in the Lockbox record where the field data starts.  */  
   Offset:number,
      /**  Default is zero. Available are positive values not exceeding length of record.  */  
   Length:number,
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
      /**   Ending position within the record string.
This is the sum of offset and length.  */  
   EndingPos:number,
      /**  This field will show the format for the given field.  */  
   FieldFormat:string,
   BitFlag:number,
   LayoutFldSchemaName:string,
   LayoutFldTableName:string,
   LayoutFldColumnName:string,
   LayoutFldFieldName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LockboxLayoutHeadListRow{
      /**  Company  */  
   Company:string,
      /**  Initiates Lockbox Layout ID search.  */  
   LayoutID:string,
      /**  Layout Description  */  
   LayoutDescription:string,
      /**  Number of decimals in amount, acceptable values 0 to 3, Default is 2  */  
   DecPointPos:number,
      /**  Indicates that the Layout is ready to be used in Lockbox Processing.  */  
   ReadyToUse:boolean,
      /**  Default value  is ‘YYMMDD’ User can enter any value.  */  
   DateFormat:string,
      /**  Identifies if ‘postable’ Cash Receipt group is posted.  */  
   AutoPost:boolean,
      /**  Depreciated  */  
   UnderPayAutoPost:boolean,
      /**  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  */  
   ValidateTotals:boolean,
      /**  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  */  
   ErrorBatchDiscard:boolean,
      /**  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  */  
   AllowOnAcc:boolean,
      /**  Determine if lockbox should automatically accept an invoice payment with errors into the customer’s account, allowing the payment to be processed into the system without manual intervention.  */  
   OnInvoiceErrorSetOnAcc:boolean,
      /**  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  */  
   AllowOverpayOnAcc:boolean,
      /**  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  */  
   AllowOverpaidInv:boolean,
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

export interface Erp_Tablesets_LockboxLayoutHeadRow{
      /**  Company  */  
   Company:string,
      /**  Initiates Lockbox Layout ID search.  */  
   LayoutID:string,
      /**  Layout Description  */  
   LayoutDescription:string,
      /**  Number of decimals in amount, acceptable values 0 to 3, Default is 2  */  
   DecPointPos:number,
      /**  Indicates that the Layout is ready to be used in Lockbox Processing.  */  
   ReadyToUse:boolean,
      /**  Default value  is ‘YYMMDD’ User can enter any value.  */  
   DateFormat:string,
      /**  Identifies if ‘postable’ Cash Receipt group is posted.  */  
   AutoPost:boolean,
      /**  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  */  
   ValidateTotals:boolean,
      /**  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  */  
   ErrorBatchDiscard:boolean,
      /**  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  */  
   AllowOnAcc:boolean,
      /**  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  */  
   AllowOverpayOnAcc:boolean,
      /**  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  */  
   AllowOverpaidInv:boolean,
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
   RecordTypeID:string,
      /**  Location of the file to test the layout.  */  
   TestFile:string,
   BitFlag:number,
   ARSystAllowOverpaidInv:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LockboxLayoutListTableset{
   LockboxLayoutHeadList:Erp_Tablesets_LockboxLayoutHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LockboxLayoutTableset{
   LockboxLayoutHead:Erp_Tablesets_LockboxLayoutHeadRow[],
   LockboxLayoutDtl:Erp_Tablesets_LockboxLayoutDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtLockboxLayoutTableset{
   LockboxLayoutHead:Erp_Tablesets_LockboxLayoutHeadRow[],
   LockboxLayoutDtl:Erp_Tablesets_LockboxLayoutDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param layoutID
   */  
export interface GetByID_input{
   layoutID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LockboxLayoutTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LockboxLayoutTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LockboxLayoutTableset[],
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
   returnObj:Erp_Tablesets_LockboxLayoutListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param layoutID
      @param recordTypeID
   */  
export interface GetNewLockboxLayoutDtl_input{
   ds:Erp_Tablesets_LockboxLayoutTableset[],
   layoutID:string,
   recordTypeID:string,
}

export interface GetNewLockboxLayoutDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LockboxLayoutTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewLockboxLayoutHead_input{
   ds:Erp_Tablesets_LockboxLayoutTableset[],
}

export interface GetNewLockboxLayoutHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LockboxLayoutTableset[],
}
}

   /** Required : 
      @param whereClauseLockboxLayoutHead
      @param whereClauseLockboxLayoutDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLockboxLayoutHead:string,
   whereClauseLockboxLayoutDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LockboxLayoutTableset[],
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
   */  
export interface OnReadyToUseChange_input{
   ds:Erp_Tablesets_LockboxLayoutTableset[],
}

export interface OnReadyToUseChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LockboxLayoutTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLockboxLayoutTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLockboxLayoutTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LockboxLayoutTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LockboxLayoutTableset[],
}
}

