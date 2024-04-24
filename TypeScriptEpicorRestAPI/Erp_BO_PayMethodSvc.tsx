import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PayMethodSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/$metadata", {
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
   Description: Get PayMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayMethods
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodRow
   */  
export function get_PayMethods(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PayMethods(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods", {
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
   Summary: Calls GetByID to retrieve the PayMethod item
   Description: Calls GetByID to retrieve the PayMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   */  
export function get_PayMethods_Company_PMUID(Company:string, PMUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PayMethod for the service
   Description: Calls UpdateExt to update PayMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PayMethods_Company_PMUID(Company:string, PMUID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")", {
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
   Summary: Call UpdateExt to delete PayMethod item
   Description: Call UpdateExt to delete PayMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PayMethods_Company_PMUID(Company:string, PMUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")", {
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
   Description: Get PayMethodProps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PayMethodProps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodPropRow
   */  
export function get_PayMethods_Company_PMUID_PayMethodProps(Company:string, PMUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodPropRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")/PayMethodProps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodPropRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PayMethodProp item
   Description: Calls GetByID to retrieve the PayMethodProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethodProp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param EFTHeadUID Desc: EFTHeadUID   Required: True
      @param EFTPropUID Desc: EFTPropUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   */  
export function get_PayMethods_Company_PMUID_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company:string, PMUID:string, EFTHeadUID:string, EFTPropUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PayMethodPropRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethods(" + Company + "," + PMUID + ")/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PayMethodPropRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PayMethodProps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayMethodProps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodPropRow
   */  
export function get_PayMethodProps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodPropRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodPropRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayMethodProps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PayMethodProps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps", {
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
   Summary: Calls GetByID to retrieve the PayMethodProp item
   Description: Calls GetByID to retrieve the PayMethodProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethodProp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param EFTHeadUID Desc: EFTHeadUID   Required: True
      @param EFTPropUID Desc: EFTPropUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   */  
export function get_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company:string, PMUID:string, EFTHeadUID:string, EFTPropUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PayMethodPropRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PayMethodPropRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PayMethodProp for the service
   Description: Calls UpdateExt to update PayMethodProp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayMethodProp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param EFTHeadUID Desc: EFTHeadUID   Required: True
      @param EFTPropUID Desc: EFTPropUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PayMethodPropRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company:string, PMUID:string, EFTHeadUID:string, EFTPropUID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")", {
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
   Summary: Call UpdateExt to delete PayMethodProp item
   Description: Call UpdateExt to delete PayMethodProp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayMethodProp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param EFTHeadUID Desc: EFTHeadUID   Required: True
      @param EFTPropUID Desc: EFTPropUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PayMethodProps_Company_PMUID_EFTHeadUID_EFTPropUID(Company:string, PMUID:string, EFTHeadUID:string, EFTPropUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/PayMethodProps(" + Company + "," + PMUID + "," + EFTHeadUID + "," + EFTPropUID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow)
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
export function get_GetRows(whereClausePayMethod:string, whereClausePayMethodProp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePayMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePayMethod=" + whereClausePayMethod
   }
   if(typeof whereClausePayMethodProp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePayMethodProp=" + whereClausePayMethodProp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetRows" + params, {
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
export function get_GetByID(pmUID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pmUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pmUID=" + pmUID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetList" + params, {
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
   Summary: Invoke method GetPayMethods
   Description: Get the PayMethod List Tableset
   OperationID: GetPayMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayMethods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPayMethods(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetPayMethods", {
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
   Summary: Invoke method ChangePayMethodEFTHeadUID
   Description: Method to call when changing the paymethod electronic interface.
   OperationID: ChangePayMethodEFTHeadUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePayMethodEFTHeadUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePayMethodEFTHeadUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePayMethodEFTHeadUID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/ChangePayMethodEFTHeadUID", {
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
   Summary: Invoke method ChangePayMethodPMSource
   Description: Method to call when changing the paymethod source.
   OperationID: ChangePayMethodPMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePayMethodPMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePayMethodPMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePayMethodPMSource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/ChangePayMethodPMSource", {
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
   Summary: Invoke method ChangePayMethodType
   Description: Method to call when changing the paymethod source.
   OperationID: ChangePayMethodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePayMethodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePayMethodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePayMethodType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/ChangePayMethodType", {
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
   Summary: Invoke method ChangeMXSATCode
   Description: Performs required logic when PayMethod.MXSATCode is modified.
   OperationID: ChangeMXSATCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMXSATCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMXSATCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMXSATCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/ChangeMXSATCode", {
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
   Summary: Invoke method ChangeCOPayMethod
   Description: Performs required logic when PayMethod.COPayMethod is modified.
   OperationID: ChangeCOPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCOPayMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/ChangeCOPayMethod", {
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
   Summary: Invoke method DeleteOldPayMethodProps
   Description: This method should be called when the Scope or Electronic Interface is changed
   OperationID: DeleteOldPayMethodProps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteOldPayMethodProps_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOldPayMethodProps_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteOldPayMethodProps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/DeleteOldPayMethodProps", {
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
   Summary: Invoke method GetIdByName
   Description: Method for retrieving ID, PMUID using Payment Method Name.
   OperationID: GetIdByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIdByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIdByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIdByName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetIdByName", {
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
   Summary: Invoke method NameChanged
   Description: get by name only
   OperationID: NameChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NameChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NameChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NameChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/NameChanged", {
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
   Summary: Invoke method SetAPInfo
   Description: Enable APInfo Tab.
   OperationID: SetAPInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAPInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAPInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetAPInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/SetAPInfo", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetCodeDescList", {
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
   Summary: Invoke method GetDepositSlipsCodeDescList
   Description: Gets list of codes/descriptions for Deposit Slips combo-box
   OperationID: GetDepositSlipsCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDepositSlipsCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDepositSlipsCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDepositSlipsCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetDepositSlipsCodeDescList", {
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
   Summary: Invoke method GetListDepositSlips
   Description: Returns a List Dataset for DepositSlips
   OperationID: GetListDepositSlips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListDepositSlips_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListDepositSlips_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListDepositSlips(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetListDepositSlips", {
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
   Summary: Invoke method GetByNamePMSource
   Description: get by id alternate
   OperationID: GetByNamePMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByNamePMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByNamePMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByNamePMSource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetByNamePMSource", {
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
   Summary: Invoke method KChangePayMethodPMSource
   Description: Row changed event for PMSourceModule
   OperationID: KChangePayMethodPMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangePayMethodPMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangePayMethodPMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KChangePayMethodPMSource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/KChangePayMethodPMSource", {
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
   Summary: Invoke method KChangePayMethodEFTHeadUID
   Description: Row changed event for PMSourceModule
   OperationID: KChangePayMethodEFTHeadUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangePayMethodEFTHeadUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangePayMethodEFTHeadUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KChangePayMethodEFTHeadUID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/KChangePayMethodEFTHeadUID", {
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
   Summary: Invoke method KChangePayMethodType
   Description: Row changed event for Type
   OperationID: KChangePayMethodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangePayMethodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangePayMethodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KChangePayMethodType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/KChangePayMethodType", {
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
   Summary: Invoke method KChangedType
   Description: Row changed event for Type
   OperationID: KChangedType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangedType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangedType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KChangedType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/KChangedType", {
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
   Summary: Invoke method KChangedPMSource
   Description: Row changed event for PMSource
   OperationID: KChangedPMSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KChangedPMSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KChangedPMSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KChangedPMSource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/KChangedPMSource", {
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
   Summary: Invoke method OnChangeOfPayMethodType
   OperationID: OnChangeOfPayMethodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfPayMethodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfPayMethodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfPayMethodType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/OnChangeOfPayMethodType", {
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
   Summary: Invoke method GetNewPayMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPayMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetNewPayMethod", {
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
   Summary: Invoke method GetNewPayMethodProp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPayMethodProp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPayMethodProp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPayMethodProp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPayMethodProp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetNewPayMethodProp", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PayMethodListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodPropRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PayMethodPropRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PayMethodRow[],
}

export interface Erp_Tablesets_PayMethodListRow{
      /**  Company  */  
   "Company":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Name of the payment method  */  
   "Name":string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   "Type":number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   "EFTHeadUID":number,
      /**  Payment Instrument Type  */  
   "PIType":string,
      /**  Payment Instrument Approve flag  */  
   "PIApprove":boolean,
      /**  System Row ID - GUID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PayMethodPropRow{
      /**  Company  */  
   "Company":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   "EFTHeadUID":number,
      /**  Unique identifier of the electronic interface property  */  
   "EFTPropUID":number,
      /**  Property Value, always defined as string value  */  
   "PropValue":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  System row ID - GUID  */  
   "SysRowID":string,
      /**  String Column  */  
   "StringCol":string,
      /**  List Column  */  
   "ListCol":string,
      /**  Logical Column  */  
   "LogicalCol":boolean,
      /**  Decimal Col  */  
   "DecimalCol":number,
      /**  Date Column  */  
   "DateCol":string,
      /**  Pay Method Type - string, list, logical, decimal, date  */  
   "Type":string,
      /**  Pay Method Property Name  */  
   "Name":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PayMethodRow{
      /**  Company  */  
   "Company":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Name of the payment method  */  
   "Name":string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   "Type":number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   "EFTHeadUID":number,
      /**  This will be the default filename for the output file created by the electronic interface  */  
   "OutputFile":string,
      /**  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  */  
   "OnlyBankCurr":boolean,
      /**   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  */  
   "PMSource":number,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "SummarizePerCustomer":boolean,
      /**  Default Payment Code  */  
   "DefPayCode":string,
      /**  Auto Bank Reconciliation  */  
   "AutoBankRec":boolean,
      /**  Sender Reference  */  
   "SenderRef":string,
      /**  Registration Number  */  
   "RegNum":string,
      /**  Checkbox to indicate test transmissions  */  
   "Test":boolean,
      /**  Reimbursable  */  
   "Reimbursable":boolean,
      /**  Inactive flag  */  
   "Inactive":boolean,
      /**  Contains the overpayment threshold allowed for ar invoices in bank file import.  */  
   "OverPayPct":number,
      /**  Contains the underpayment threshold allowed for ar invoices in bank file import.  */  
   "UnderPayPct":number,
      /**  Payment Instrument Type  */  
   "PIType":string,
      /**  Payment Instrument Generation Method  */  
   "PIGenMethod":number,
      /**  Payment Instrument Approve flag  */  
   "PIApprove":boolean,
      /**  Marks this PayMethod as global, available to be sent out to other companies.  */  
   "GlobalPayMethod":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  System Row ID - GUID  */  
   "SysRowID":string,
      /**  DepositSlips  */  
   "DepositSlips":number,
      /**  IsPositiveBalance  */  
   "IsPositiveBalance":boolean,
      /**  Specifies how the payments are processed in a bank - individually or in a batch  */  
   "APGrouping":number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   "APIDGeneration":boolean,
      /**  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  */  
   "ARGrouping":number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   "ARIDGeneration":boolean,
      /**  Specify at what moment the application groups AR receipts in batches  */  
   "ARIDTiming":number,
      /**  EFTDebitMemoHandlingCode  */  
   "EFTDebitMemoHandlingCode":string,
      /**  EFTDebitMemoDueDate  */  
   "EFTDebitMemoDueDate":string,
      /**  EFTProductNumDate  */  
   "EFTProductNumDate":string,
      /**  EFTProductNumber  */  
   "EFTProductNumber":number,
      /**  SEPO3Payment  */  
   "SEPO3Payment":boolean,
      /**  SECrossBrdPayMethod  */  
   "SECrossBrdPayMethod":string,
      /**  SECurrPocket  */  
   "SECurrPocket":string,
      /**  SEErrorHandling  */  
   "SEErrorHandling":string,
      /**  SEUseIBAN  */  
   "SEUseIBAN":string,
      /**  SEPath  */  
   "SEPath":string,
      /**  SECreateErrorLog  */  
   "SECreateErrorLog":boolean,
      /**  SEFileForEachPayCurr  */  
   "SEFileForEachPayCurr":boolean,
      /**  NOPaymentList  */  
   "NOPaymentList":boolean,
      /**  NOTelepayPayment  */  
   "NOTelepayPayment":boolean,
      /**  NOTelepayReply  */  
   "NOTelepayReply":boolean,
      /**  DEFeeRule  */  
   "DEFeeRule":string,
      /**  DESerialNum  */  
   "DESerialNum":number,
      /**  DEStateNum  */  
   "DEStateNum":string,
      /**  DELastUseDate  */  
   "DELastUseDate":string,
      /**  MXPaidAs  */  
   "MXPaidAs":string,
      /**  MXPaymentNum  */  
   "MXPaymentNum":number,
      /**  MXTotalPayments  */  
   "MXTotalPayments":number,
      /**  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  */  
   "MXPaymentType":number,
      /**  MXSATCode  */  
   "MXSATCode":string,
      /**  MXSATDesc  */  
   "MXSATDesc":string,
      /**  PymtProposal  */  
   "PymtProposal":boolean,
      /**  AutoCheckNum  */  
   "AutoCheckNum":boolean,
      /**  EnterPymtTotal  */  
   "EnterPymtTotal":boolean,
      /**  CheckNumSeq  */  
   "CheckNumSeq":number,
      /**  Form 1099-K Transaction Type  */  
   "US1099KTranType":string,
      /**  Form 1099-K Third Party Network Amount Threshold  */  
   "US1099KAmtThreshold":number,
      /**  Form 1099-K Third Party Network Transaction Threshold  */  
   "US1099KTranThreshold":number,
      /**  COPayForm  */  
   "COPayForm":string,
      /**  COPayMethod  */  
   "COPayMethod":string,
      /**  UNCL4461  */  
   "TypeCode":string,
      /**  Indicates if the threshold fields are enabled  */  
   "EnableThresholds":boolean,
   "IsCZLocalization":boolean,
      /**  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  */  
   "PMSourceModule":string,
      /**  EnableAPInfo  */  
   "EnableAPInfo":boolean,
   "COPayMethodDesc":string,
   "TypeDescription":string,
   "BitFlag":number,
   "EFTHeadName":string,
   "EFTHeadType":number,
   "PITypeDescription":string,
   "XbSystELIEinvoice":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param coPayFormCode
      @param ds
   */  
export interface ChangeCOPayMethod_input{
      /**  Proposed input value  */  
   coPayFormCode:string,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface ChangeCOPayMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ipMXSATCode
      @param ds
   */  
export interface ChangeMXSATCode_input{
      /**  Proposed input value of SAT Code / "Form of Payment"  */  
   ipMXSATCode:string,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface ChangeMXSATCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ProposedEFTHeadUID
      @param ds
   */  
export interface ChangePayMethodEFTHeadUID_input{
      /**  The proposed paymethod electronic interface  */  
   ProposedEFTHeadUID:number,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface ChangePayMethodEFTHeadUID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ProposedPMSourceModule
      @param ds
   */  
export interface ChangePayMethodPMSource_input{
      /**  The proposed paymethod source  */  
   ProposedPMSourceModule:string,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface ChangePayMethodPMSource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ProposedType
      @param ds
   */  
export interface ChangePayMethodType_input{
      /**  The proposed paymethod type  */  
   ProposedType:number,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface ChangePayMethodType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param pmUID
   */  
export interface DeleteByID_input{
   pmUID:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param fieldChanged
      @param ds
   */  
export interface DeleteOldPayMethodProps_input{
      /**  Indicates which field was changed that caused the method to be called.  */  
   fieldChanged:string,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface DeleteOldPayMethodProps_output{
parameters : {
      /**  output parameters  */  
   returnMsg:string,
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

export interface Erp_Tablesets_PayMethodListRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Name of the payment method  */  
   Name:string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   Type:number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   EFTHeadUID:number,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Payment Instrument Approve flag  */  
   PIApprove:boolean,
      /**  System Row ID - GUID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayMethodListTableset{
   PayMethodList:Erp_Tablesets_PayMethodListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PayMethodPropRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   EFTHeadUID:number,
      /**  Unique identifier of the electronic interface property  */  
   EFTPropUID:number,
      /**  Property Value, always defined as string value  */  
   PropValue:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  System row ID - GUID  */  
   SysRowID:string,
      /**  String Column  */  
   StringCol:string,
      /**  List Column  */  
   ListCol:string,
      /**  Logical Column  */  
   LogicalCol:boolean,
      /**  Decimal Col  */  
   DecimalCol:number,
      /**  Date Column  */  
   DateCol:string,
      /**  Pay Method Type - string, list, logical, decimal, date  */  
   Type:string,
      /**  Pay Method Property Name  */  
   Name:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayMethodRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Name of the payment method  */  
   Name:string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   Type:number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   EFTHeadUID:number,
      /**  This will be the default filename for the output file created by the electronic interface  */  
   OutputFile:string,
      /**  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  */  
   OnlyBankCurr:boolean,
      /**   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  */  
   PMSource:number,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   SummarizePerCustomer:boolean,
      /**  Default Payment Code  */  
   DefPayCode:string,
      /**  Auto Bank Reconciliation  */  
   AutoBankRec:boolean,
      /**  Sender Reference  */  
   SenderRef:string,
      /**  Registration Number  */  
   RegNum:string,
      /**  Checkbox to indicate test transmissions  */  
   Test:boolean,
      /**  Reimbursable  */  
   Reimbursable:boolean,
      /**  Inactive flag  */  
   Inactive:boolean,
      /**  Contains the overpayment threshold allowed for ar invoices in bank file import.  */  
   OverPayPct:number,
      /**  Contains the underpayment threshold allowed for ar invoices in bank file import.  */  
   UnderPayPct:number,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Payment Instrument Generation Method  */  
   PIGenMethod:number,
      /**  Payment Instrument Approve flag  */  
   PIApprove:boolean,
      /**  Marks this PayMethod as global, available to be sent out to other companies.  */  
   GlobalPayMethod:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  System Row ID - GUID  */  
   SysRowID:string,
      /**  DepositSlips  */  
   DepositSlips:number,
      /**  IsPositiveBalance  */  
   IsPositiveBalance:boolean,
      /**  Specifies how the payments are processed in a bank - individually or in a batch  */  
   APGrouping:number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   APIDGeneration:boolean,
      /**  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  */  
   ARGrouping:number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   ARIDGeneration:boolean,
      /**  Specify at what moment the application groups AR receipts in batches  */  
   ARIDTiming:number,
      /**  EFTDebitMemoHandlingCode  */  
   EFTDebitMemoHandlingCode:string,
      /**  EFTDebitMemoDueDate  */  
   EFTDebitMemoDueDate:string,
      /**  EFTProductNumDate  */  
   EFTProductNumDate:string,
      /**  EFTProductNumber  */  
   EFTProductNumber:number,
      /**  SEPO3Payment  */  
   SEPO3Payment:boolean,
      /**  SECrossBrdPayMethod  */  
   SECrossBrdPayMethod:string,
      /**  SECurrPocket  */  
   SECurrPocket:string,
      /**  SEErrorHandling  */  
   SEErrorHandling:string,
      /**  SEUseIBAN  */  
   SEUseIBAN:string,
      /**  SEPath  */  
   SEPath:string,
      /**  SECreateErrorLog  */  
   SECreateErrorLog:boolean,
      /**  SEFileForEachPayCurr  */  
   SEFileForEachPayCurr:boolean,
      /**  NOPaymentList  */  
   NOPaymentList:boolean,
      /**  NOTelepayPayment  */  
   NOTelepayPayment:boolean,
      /**  NOTelepayReply  */  
   NOTelepayReply:boolean,
      /**  DEFeeRule  */  
   DEFeeRule:string,
      /**  DESerialNum  */  
   DESerialNum:number,
      /**  DEStateNum  */  
   DEStateNum:string,
      /**  DELastUseDate  */  
   DELastUseDate:string,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  */  
   MXPaymentType:number,
      /**  MXSATCode  */  
   MXSATCode:string,
      /**  MXSATDesc  */  
   MXSATDesc:string,
      /**  PymtProposal  */  
   PymtProposal:boolean,
      /**  AutoCheckNum  */  
   AutoCheckNum:boolean,
      /**  EnterPymtTotal  */  
   EnterPymtTotal:boolean,
      /**  CheckNumSeq  */  
   CheckNumSeq:number,
      /**  Form 1099-K Transaction Type  */  
   US1099KTranType:string,
      /**  Form 1099-K Third Party Network Amount Threshold  */  
   US1099KAmtThreshold:number,
      /**  Form 1099-K Third Party Network Transaction Threshold  */  
   US1099KTranThreshold:number,
      /**  COPayForm  */  
   COPayForm:string,
      /**  COPayMethod  */  
   COPayMethod:string,
      /**  UNCL4461  */  
   TypeCode:string,
      /**  Indicates if the threshold fields are enabled  */  
   EnableThresholds:boolean,
   IsCZLocalization:boolean,
      /**  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  */  
   PMSourceModule:string,
      /**  EnableAPInfo  */  
   EnableAPInfo:boolean,
   COPayMethodDesc:string,
   TypeDescription:string,
   BitFlag:number,
   EFTHeadName:string,
   EFTHeadType:number,
   PITypeDescription:string,
   XbSystELIEinvoice:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayMethodTableset{
   PayMethod:Erp_Tablesets_PayMethodRow[],
   PayMethodProp:Erp_Tablesets_PayMethodPropRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPayMethodTableset{
   PayMethod:Erp_Tablesets_PayMethodRow[],
   PayMethodProp:Erp_Tablesets_PayMethodPropRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param pmUID
   */  
export interface GetByID_input{
   pmUID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PayMethodTableset[],
}

   /** Required : 
      @param name
      @param pmSource
   */  
export interface GetByNamePMSource_input{
   name:string,
   pmSource:number,
}

export interface GetByNamePMSource_output{
   returnObj:Erp_Tablesets_PayMethodTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PayMethodTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PayMethodTableset[],
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
      @param sARIDTiming
   */  
export interface GetDepositSlipsCodeDescList_input{
   sARIDTiming:string,
}

export interface GetDepositSlipsCodeDescList_output{
      /**  List of Deposit Slips  codes/descriptions  */  
   returnObj:string,
}

   /** Required : 
      @param cName
   */  
export interface GetIdByName_input{
      /**  Name  */  
   cName:string,
}

export interface GetIdByName_output{
parameters : {
      /**  output parameters  */  
   iPMUID:number,
}
}

   /** Required : 
      @param whereClause
      @param bankAcctID
      @param pmName
      @param pmUIDs
      @param pageSize
      @param absolutePage
   */  
export interface GetListDepositSlips_input{
      /**  whereClause  */  
   whereClause:string,
   bankAcctID:string,
      /**  payment method name  */  
   pmName:string,
      /**  list of payment UIDs  */  
   pmUIDs:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListDepositSlips_output{
   returnObj:Erp_Tablesets_PayMethodListTableset[],
parameters : {
      /**  output parameters  */  
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
   returnObj:Erp_Tablesets_PayMethodListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pmUID
      @param efTHeadUID
   */  
export interface GetNewPayMethodProp_input{
   ds:Erp_Tablesets_PayMethodTableset[],
   pmUID:number,
   efTHeadUID:number,
}

export interface GetNewPayMethodProp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPayMethod_input{
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface GetNewPayMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

export interface GetPayMethods_output{
   returnObj:Erp_Tablesets_PayMethodListTableset[],
}

   /** Required : 
      @param whereClausePayMethod
      @param whereClausePayMethodProp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePayMethod:string,
   whereClausePayMethodProp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PayMethodTableset[],
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
      @param ProposedEFTHeadUID
      @param ds
   */  
export interface KChangePayMethodEFTHeadUID_input{
   ProposedEFTHeadUID:number,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface KChangePayMethodEFTHeadUID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ProposedPMSourceModule
      @param ds
   */  
export interface KChangePayMethodPMSource_input{
   ProposedPMSourceModule:string,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface KChangePayMethodPMSource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ProposedType
      @param ds
   */  
export interface KChangePayMethodType_input{
   ProposedType:number,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface KChangePayMethodType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface KChangedPMSource_input{
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface KChangedPMSource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface KChangedType_input{
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface KChangedType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param name
      @param ds
   */  
export interface NameChanged_input{
   name:string,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface NameChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param PMUID
      @param ds
   */  
export interface OnChangeOfPayMethodType_input{
      /**  Paymenth Method ID  */  
   PMUID:number,
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface OnChangeOfPayMethodType_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface SetAPInfo_input{
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface SetAPInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPayMethodTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPayMethodTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PayMethodTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodTableset[],
}
}

