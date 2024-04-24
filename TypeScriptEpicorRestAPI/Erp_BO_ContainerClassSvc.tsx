import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ContainerClassSvc
// Description: Master file maintenance business logic for ContainerClass
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/$metadata", {
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
   Description: Get ContainerClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerClasses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerClassRow
   */  
export function get_ContainerClasses(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerClasses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses", {
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
   Summary: Calls GetByID to retrieve the ContainerClass item
   Description: Calls GetByID to retrieve the ContainerClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
   */  
export function get_ContainerClasses_Company_ClassCode(Company:string, ClassCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContainerClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ContainerClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContainerClass for the service
   Description: Calls UpdateExt to update ContainerClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContainerClasses_Company_ClassCode(Company:string, ClassCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")", {
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
   Summary: Call UpdateExt to delete ContainerClass item
   Description: Call UpdateExt to delete ContainerClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContainerClasses_Company_ClassCode(Company:string, ClassCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")", {
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
   Description: Get ContClassMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContClassMiscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContClassMiscRow
   */  
export function get_ContainerClasses_Company_ClassCode_ContClassMiscs(Company:string, ClassCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContClassMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")/ContClassMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContClassMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContClassMisc item
   Description: Calls GetByID to retrieve the ContClassMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContClassMisc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param MiscCode Desc: MiscCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   */  
export function get_ContainerClasses_Company_ClassCode_ContClassMiscs_Company_ClassCode_MiscCode(Company:string, ClassCode:string, MiscCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContClassMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContainerClasses(" + Company + "," + ClassCode + ")/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ContClassMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ContClassMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContClassMiscs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContClassMiscRow
   */  
export function get_ContClassMiscs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContClassMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContClassMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContClassMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContClassMiscs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs", {
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
   Summary: Calls GetByID to retrieve the ContClassMisc item
   Description: Calls GetByID to retrieve the ContClassMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContClassMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param MiscCode Desc: MiscCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   */  
export function get_ContClassMiscs_Company_ClassCode_MiscCode(Company:string, ClassCode:string, MiscCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContClassMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ContClassMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContClassMisc for the service
   Description: Calls UpdateExt to update ContClassMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContClassMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param MiscCode Desc: MiscCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContClassMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContClassMiscs_Company_ClassCode_MiscCode(Company:string, ClassCode:string, MiscCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")", {
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
   Summary: Call UpdateExt to delete ContClassMisc item
   Description: Call UpdateExt to delete ContClassMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContClassMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param MiscCode Desc: MiscCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContClassMiscs_Company_ClassCode_MiscCode(Company:string, ClassCode:string, MiscCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/ContClassMiscs(" + Company + "," + ClassCode + "," + MiscCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerClassListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassListRow)
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
export function get_GetRows(whereClauseContainerClass:string, whereClauseContClassMisc:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseContainerClass!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContainerClass=" + whereClauseContainerClass
   }
   if(typeof whereClauseContClassMisc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContClassMisc=" + whereClauseContClassMisc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/GetRows" + params, {
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
export function get_GetByID(classCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof classCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "classCode=" + classCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/GetList" + params, {
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
   Summary: Invoke method DefaultContainerCost
   Description: Calculates container cost when CostPerVolume or Volume change.
   OperationID: DefaultContainerCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultContainerCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultContainerCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultContainerCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/DefaultContainerCost", {
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
   Summary: Invoke method DefaultCostPerVolume
   Description: Calculates the CostPerVolume.
   OperationID: DefaultCostPerVolume
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultCostPerVolume_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultCostPerVolume_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultCostPerVolume(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/DefaultCostPerVolume", {
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
   Summary: Invoke method OnContactChange
   Description: Verifies if proposed Vendor Contact number is valid. If so, loads Vendor Contact Information.
   OperationID: OnContactChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnContactChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnContactChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnContactChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/OnContactChange", {
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
   Summary: Invoke method OnIndirectCostChange
   Description: Verifies if proposed Landed Cost Indirect Cost Code is valid. If so, loads Indirect Cost Amount and Currency code.
   OperationID: OnIndirectCostChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnIndirectCostChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnIndirectCostChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnIndirectCostChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/OnIndirectCostChange", {
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
   Summary: Invoke method OnSupplierChange
   Description: Verifies if proposed Supplier ID is valid. If so, loads Supplier's name.
   OperationID: OnSupplierChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnSupplierChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnSupplierChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnSupplierChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/OnSupplierChange", {
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
   Summary: Invoke method GetNewContainerClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContainerClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/GetNewContainerClass", {
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
   Summary: Invoke method GetNewContClassMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContClassMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContClassMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContClassMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContClassMisc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/GetNewContClassMisc", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContainerClassSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContClassMiscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContClassMiscRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerClassListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerClassRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContainerClassRow[],
}

export interface Erp_Tablesets_ContClassMiscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Container Shipment Class ID  */  
   "ClassCode":string,
      /**  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "MiscCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "MiscCodeLCAmount":number,
   "MiscCodeDescription":string,
   "MiscCodeLCDisburseMethod":string,
   "MiscCodeLCCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerClassListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Container Class Code ID  */  
   "ClassCode":string,
      /**  Descriptive text identifying the Container Class  */  
   "Description":string,
      /**  Total cost to ship this container  */  
   "ContainerCost":number,
      /**  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  */  
   "ShippingDays":number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   "Volume":number,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   "CostPerVolume":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  */  
   "VolumeUOM":string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   "LoadPortID":string,
      /**  Valid port location where goods are unloaded.  */  
   "DechargePortID":string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   "ShipViaCode":string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   "FOB":string,
      /**  Number of Containers in this shipment.  */  
   "ContainerCount":number,
      /**  Number of Packages in this shipment.  */  
   "PackageCount":number,
      /**  Total Weight of the shipment.  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   "WeightUOM":string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  This key links the record to the Vendor file.  */  
   "VendorNum":number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   "ConNum":number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   "PurPoint":string,
      /**  Marks this ContainerClass as global, available to be sent out to other companies.  */  
   "GlobalContainerClass":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Contact name.  */  
   "ConNumName":string,
      /**  Contact email address.  */  
   "ConNumEmailAddress":string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   "ConNumPhoneNum":string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   "ConNumFaxNum":string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   "DechargePortIDDescription":string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   "DechargePortIDPortID":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   "LoadPortIDDescription":string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   "LoadPortIDPortID":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContainerClassRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Container Class Code ID  */  
   "ClassCode":string,
      /**  Descriptive text identifying the Container Class  */  
   "Description":string,
      /**  Total cost to ship this container  */  
   "ContainerCost":number,
      /**  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  */  
   "ShippingDays":number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   "Volume":number,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   "CostPerVolume":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  */  
   "VolumeUOM":string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   "LoadPortID":string,
      /**  Valid port location where goods are unloaded.  */  
   "DechargePortID":string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   "ShipViaCode":string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   "FOB":string,
      /**  Number of Containers in this shipment.  */  
   "ContainerCount":number,
      /**  Number of Packages in this shipment.  */  
   "PackageCount":number,
      /**  Total Weight of the shipment.  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   "WeightUOM":string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  This key links the record to the Vendor file.  */  
   "VendorNum":number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   "ConNum":number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   "PurPoint":string,
      /**  Marks this ContainerClass as global, available to be sent out to other companies.  */  
   "GlobalContainerClass":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "ConNumName":string,
   "ConNumFaxNum":string,
   "ConNumPhoneNum":string,
   "ConNumEmailAddress":string,
   "DechargePortIDDescription":string,
   "DechargePortIDPortID":string,
   "FOBDescription":string,
   "LoadPortIDDescription":string,
   "LoadPortIDPortID":string,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumZIP":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumVendorID":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumDefaultFOB":string,
   "VendorNumName":string,
   "VendorNumCity":string,
   "VendorNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface DefaultContainerCost_input{
   ds:Erp_Tablesets_ContainerClassTableset[],
}

export interface DefaultContainerCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultCostPerVolume_input{
   ds:Erp_Tablesets_ContainerClassTableset[],
}

export interface DefaultCostPerVolume_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

   /** Required : 
      @param classCode
   */  
export interface DeleteByID_input{
   classCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ContClassMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Container Shipment Class ID  */  
   ClassCode:string,
      /**  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   MiscCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   MiscCodeLCAmount:number,
   MiscCodeDescription:string,
   MiscCodeLCDisburseMethod:string,
   MiscCodeLCCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerClassListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Container Class Code ID  */  
   ClassCode:string,
      /**  Descriptive text identifying the Container Class  */  
   Description:string,
      /**  Total cost to ship this container  */  
   ContainerCost:number,
      /**  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  */  
   ShippingDays:number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   CostPerVolume:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  */  
   VolumeUOM:string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   LoadPortID:string,
      /**  Valid port location where goods are unloaded.  */  
   DechargePortID:string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   ShipViaCode:string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   FOB:string,
      /**  Number of Containers in this shipment.  */  
   ContainerCount:number,
      /**  Number of Packages in this shipment.  */  
   PackageCount:number,
      /**  Total Weight of the shipment.  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  Marks this ContainerClass as global, available to be sent out to other companies.  */  
   GlobalContainerClass:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Contact name.  */  
   ConNumName:string,
      /**  Contact email address.  */  
   ConNumEmailAddress:string,
      /**  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  */  
   ConNumPhoneNum:string,
      /**  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  */  
   ConNumFaxNum:string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   DechargePortIDDescription:string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   DechargePortIDPortID:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  Country Port Description.  This must be a unique port description within the Company.  */  
   LoadPortIDDescription:string,
      /**  A unique PortID within the Company and must always be associated with a Country.  */  
   LoadPortIDPortID:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerClassListTableset{
   ContainerClassList:Erp_Tablesets_ContainerClassListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ContainerClassRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Container Class Code ID  */  
   ClassCode:string,
      /**  Descriptive text identifying the Container Class  */  
   Description:string,
      /**  Total cost to ship this container  */  
   ContainerCost:number,
      /**  Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.  */  
   ShippingDays:number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   CostPerVolume:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Unit of measure used to qualify the Volume.
If entered, must be valid in the standard "Volume" UOMs  (UOMClass.ClassType = "Volume")  */  
   VolumeUOM:string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   LoadPortID:string,
      /**  Valid port location where goods are unloaded.  */  
   DechargePortID:string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   ShipViaCode:string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   FOB:string,
      /**  Number of Containers in this shipment.  */  
   ContainerCount:number,
      /**  Number of Packages in this shipment.  */  
   PackageCount:number,
      /**  Total Weight of the shipment.  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  Marks this ContainerClass as global, available to be sent out to other companies.  */  
   GlobalContainerClass:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   ConNumName:string,
   ConNumFaxNum:string,
   ConNumPhoneNum:string,
   ConNumEmailAddress:string,
   DechargePortIDDescription:string,
   DechargePortIDPortID:string,
   FOBDescription:string,
   LoadPortIDDescription:string,
   LoadPortIDPortID:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumZIP:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumDefaultFOB:string,
   VendorNumName:string,
   VendorNumCity:string,
   VendorNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerClassTableset{
   ContainerClass:Erp_Tablesets_ContainerClassRow[],
   ContClassMisc:Erp_Tablesets_ContClassMiscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtContainerClassTableset{
   ContainerClass:Erp_Tablesets_ContainerClassRow[],
   ContClassMisc:Erp_Tablesets_ContClassMiscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param classCode
   */  
export interface GetByID_input{
   classCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ContainerClassTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ContainerClassTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ContainerClassTableset[],
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
   returnObj:Erp_Tablesets_ContainerClassListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param classCode
   */  
export interface GetNewContClassMisc_input{
   ds:Erp_Tablesets_ContainerClassTableset[],
   classCode:string,
}

export interface GetNewContClassMisc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewContainerClass_input{
   ds:Erp_Tablesets_ContainerClassTableset[],
}

export interface GetNewContainerClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

   /** Required : 
      @param whereClauseContainerClass
      @param whereClauseContClassMisc
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseContainerClass:string,
   whereClauseContClassMisc:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ContainerClassTableset[],
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
      @param ipContactNum
      @param ds
   */  
export interface OnContactChange_input{
      /**  The Contact Number  */  
   ipContactNum:number,
   ds:Erp_Tablesets_ContainerClassTableset[],
}

export interface OnContactChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

   /** Required : 
      @param ipMiscCode
      @param ds
   */  
export interface OnIndirectCostChange_input{
      /**  The Supplier ID  */  
   ipMiscCode:string,
   ds:Erp_Tablesets_ContainerClassTableset[],
}

export interface OnIndirectCostChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

   /** Required : 
      @param ipSupplierID
      @param ds
   */  
export interface OnSupplierChange_input{
      /**  The Supplier ID  */  
   ipSupplierID:string,
   ds:Erp_Tablesets_ContainerClassTableset[],
}

export interface OnSupplierChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtContainerClassTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtContainerClassTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ContainerClassTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContainerClassTableset[],
}
}

