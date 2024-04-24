import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.UOMClassSvc
// Description: UOM class BL
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/$metadata", {
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
   Description: Get UOMClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UOMClasses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMClassRow
   */  
export function get_UOMClasses(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UOMClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UOMClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UOMClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UOMClasses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses", {
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
   Summary: Calls GetByID to retrieve the UOMClass item
   Description: Calls GetByID to retrieve the UOMClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UOMClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UOMClassRow
   */  
export function get_UOMClasses_Company_UOMClassID(Company:string, UOMClassID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UOMClassRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_UOMClassRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UOMClass for the service
   Description: Calls UpdateExt to update UOMClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UOMClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UOMClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UOMClasses_Company_UOMClassID(Company:string, UOMClassID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")", {
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
   Summary: Call UpdateExt to delete UOMClass item
   Description: Call UpdateExt to delete UOMClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UOMClass
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UOMClasses_Company_UOMClassID(Company:string, UOMClassID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")", {
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
   Description: Get UOMConvs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UOMConvs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMConvRow
   */  
export function get_UOMClasses_Company_UOMClassID_UOMConvs(Company:string, UOMClassID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMConvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")/UOMConvs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMConvRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the UOMConv item
   Description: Calls GetByID to retrieve the UOMConv item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UOMConv1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   */  
export function get_UOMClasses_Company_UOMClassID_UOMConvs_Company_UOMClassID_UOMCode(Company:string, UOMClassID:string, UOMCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UOMConvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_UOMConvRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get UOMConvs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UOMConvs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMConvRow
   */  
export function get_UOMConvs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMConvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMConvRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UOMConvs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UOMConvRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UOMConvs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs", {
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
   Summary: Calls GetByID to retrieve the UOMConv item
   Description: Calls GetByID to retrieve the UOMConv item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UOMConv
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   */  
export function get_UOMConvs_Company_UOMClassID_UOMCode(Company:string, UOMClassID:string, UOMCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UOMConvRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_UOMConvRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UOMConv for the service
   Description: Calls UpdateExt to update UOMConv. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UOMConv
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UOMConvs_Company_UOMClassID_UOMCode(Company:string, UOMClassID:string, UOMCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")", {
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
   Summary: Call UpdateExt to delete UOMConv item
   Description: Call UpdateExt to delete UOMConv item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UOMConv
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UOMClassID Desc: UOMClassID   Required: True   Allow empty value : True
      @param UOMCode Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UOMConvs_Company_UOMClassID_UOMCode(Company:string, UOMClassID:string, UOMCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMClassListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassListRow)
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
export function get_GetRows(whereClauseUOMClass:string, whereClauseUOMConv:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseUOMClass!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUOMClass=" + whereClauseUOMClass
   }
   if(typeof whereClauseUOMConv!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUOMConv=" + whereClauseUOMConv
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetRows" + params, {
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
export function get_GetByID(uoMClassID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof uoMClassID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "uoMClassID=" + uoMClassID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetList" + params, {
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
   Summary: Invoke method OnChangeAllowDecimal
   Description: This method should be called when AllowDecimal changes.
   OperationID: OnChangeAllowDecimal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAllowDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllowDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAllowDecimal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/OnChangeAllowDecimal", {
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
   Summary: Invoke method OnChangeBaseUOM
   Description: This method should be called when Base UOM changes.
   OperationID: OnChangeBaseUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBaseUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBaseUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBaseUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/OnChangeBaseUOM", {
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
   Summary: Invoke method OnChangeClassType
   Description: This method should be called when the ClassType changes.
   OperationID: OnChangeClassType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClassType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClassType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeClassType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/OnChangeClassType", {
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
   Summary: Invoke method OnChangeDispPkgDisplaySeq
   Description: This method should be called when UOMConv PkgCode changes.
   OperationID: OnChangeDispPkgDisplaySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDispPkgDisplaySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDispPkgDisplaySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDispPkgDisplaySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/OnChangeDispPkgDisplaySeq", {
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
   Summary: Invoke method OnChangePkgCode
   Description: This method should be called when UOMConv PkgCode changes.
   OperationID: OnChangePkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePkgCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/OnChangePkgCode", {
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
   Summary: Invoke method OnChangeUOMCode
   Description: Called when the UOMCode is changed when creating a new UOMConv Record.
Refreshes UOMConv.UOMDesc UOMSymbol AllowDecimals NumOfDec Rounding
   OperationID: OnChangeUOMCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUOMCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/OnChangeUOMCode", {
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
   Description: An override to the standard GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetCodeDescList", {
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
   Summary: Invoke method ValidateUOMClassId
   Description: Called when the UOMClassId is changed when creating a new UOMClassId Record.
   OperationID: ValidateUOMClassId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUOMClassId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUOMClassId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUOMClassId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/ValidateUOMClassId", {
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
   Summary: Invoke method GetNewUOMClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUOMClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUOMClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUOMClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUOMClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetNewUOMClass", {
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
   Summary: Invoke method GetNewUOMConv
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUOMConv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUOMConv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUOMConv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUOMConv(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetNewUOMConv", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UOMClassListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UOMClassRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMConvRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UOMConvRow[],
}

export interface Erp_Tablesets_UOMClassListRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  */  
   "UOMClassID":string,
      /**  A decription for the UOMClass.  Mandatory.  */  
   "Description":string,
      /**   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  */  
   "ClassType":string,
      /**  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  */  
   "BaseUOMCode":string,
      /**   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  */  
   "DefUomCode":string,
      /**  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  */  
   "Active":boolean,
      /**  Marks this UOMClass as global, available to be sent out to other companies.  */  
   "GlobalUOMClass":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  */  
   "DefaultUOMClass":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_UOMClassRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  */  
   "UOMClassID":string,
      /**  A decription for the UOMClass.  Mandatory.  */  
   "Description":string,
      /**   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  */  
   "ClassType":string,
      /**  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  */  
   "BaseUOMCode":string,
      /**   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  */  
   "DefUomCode":string,
      /**  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  */  
   "Active":boolean,
      /**  Marks this UOMClass as global, available to be sent out to other companies.  */  
   "GlobalUOMClass":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  */  
   "DefaultUOMClass":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_UOMConvRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  The UOM Class ID that this unit of measure belongs to.  */  
   "UOMClassID":string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   "UOMCode":string,
      /**   Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.

Factors defined in UOMConv are not specific to any individual part and are considered standard  conversions. The relationship between Inches (in), and  Feet (ft) is a good example. 
Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table.  */  
   "ConvFactor":number,
      /**  Long Description of a unit of measure. Mandatory.  */  
   "UOMDesc":string,
      /**  used only during the 8.3 to 9.0 conversion process.  */  
   "BaseUOM83":boolean,
      /**  Used only for the 8.3 to 9.0 conversion. Holds the original code that was used in 8.3. By changing the UOMCode the user can instruct the system to  convert the old 8.3 value to the new UOMCode value.  Example Ea to EACH or E to EACH.  */  
   "UOMCode83":string,
      /**  Indicates if the UOM is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  */  
   "Active":boolean,
      /**  Optional Symbol that can be used in place of the UOMCode such as when printing external documents or certain displays. Especially useful to express a UOM using subscripts or superscripts which would be hard to use as a UOMCode due to difficultly of keying into transactions.  */  
   "UOMSymbol":string,
      /**   Indicates if fractional quantities are allowed with this unit of measure.
If true, then NumOfDec and Rounding fields will be enabled and Precison must have a value greater than zero. 
Replaces the 8.03.400 Part.WholeUnit.  */  
   "AllowDecimals":boolean,
      /**   Defines how many decimal points are allowed with this UOM.
Disabled and set to zero if UOMConv.AllowDecimals = False. Enabled and must be > 0 if UOMConv.AllowDecimals = True. Not only does this validate quantity entered but also used in UOM quantity conversion logic.  */  
   "NumOfDec":number,
      /**  If AllowDec = True,  then the following options are available; RND-  Round, Up-Round UP, DWN-Round Down.  */  
   "Rounding":string,
      /**  System set, indicates if this UOMConv exists in a Standard UOMClass. (UOMClass.ClassType <> "Other"). Used to provide list of UOMs when a UOMClass, or Target UOMCode is not known. Ex: Creating a JobMtl record against a non-part item. In this case all UOMConv where StdUOM = true are valid. It is also used during the UOMConv maint process.  Not allowed to create a UOMConv with with a UOMCode that exists in another standard UOMClass.  */  
   "StdUOM":boolean,
      /**   Indicates if Part Specific Conversion factors are required. This can only set to true with ClassType = "Other". Setting this to true, disables entry of the UOM Conversion factors from within the UOM maint. In this case conversion factors of the uoms are relative to the Part and will be enter in Part maint.
Example: You stock in Sheets, Purchase in Lbs, and consume in Square Feet.  Since the number of Lbs and SqFt in a sheet are relative to a part they would be marked as PartSpecific = true.  */  
   "PartSpecific":boolean,
      /**  This indicates that this UOM Conv has been used somewhere.  Therefore we do not want to allow the associated conversion to change.  */  
   "HasBeenUsed":boolean,
      /**   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  */  
   "ConvOperator":string,
      /**  Marks this UOMConv as global, available to be sent out to other companies.  */  
   "GlobalUOMConv":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Signifies this is the Base UOM for this Class  */  
   "BaseUOM":boolean,
      /**  Qualifies that 1 of this uom = ConvFactor in ConvToUOM. Example: 12in = 1ft or 1ft = 12in  */  
   "ConvFromUOM":string,
      /**  Qualifies UOM of the ConvFactor. This either the UOMClass.BaseUOM or the UOMConv.UOMCode depending on the value of ConvOperator.  */  
   "ConvToUOM":string,
      /**  Sets a flag to determine whether this is the default UOM for this Class.  */  
   "DefaultUOM":boolean,
      /**  Display field for BaseUOMCode  */  
   "DispBaseUOMCode":string,
      /**  Flag which determines whether we should enable the BaseUOM field.  The rule is, if the current BaseUOM has the field HasBeenUsed = true, we shouldn't allow them to change the BaseUOM.  */  
   "EnableBaseUOM":boolean,
      /**  Used to input/display the package code related to the UOMClass/UOM (stored in table PackingUOM).  */  
   "DispPkgCode":string,
      /**  Description of the PkgCode  */  
   "DispPkgCodeDesc":string,
      /**  Indicates the display sequence of the packaging in relation to the other packaging for the UOMClass  */  
   "DispPkgDisplaySeq":number,
      /**  Indicates if the PkgCode is the default.  */  
   "DispPkgIsDefault":boolean,
      /**  Indicates if the package code will be displayed in the application.If false, the package codes that are not valid for the MFG process on the shop floor (MES) are hidden.  */  
   "DispPkgDisplayHidden":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param uoMClassID
   */  
export interface DeleteByID_input{
   uoMClassID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UOMClassListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  */  
   UOMClassID:string,
      /**  A decription for the UOMClass.  Mandatory.  */  
   Description:string,
      /**   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  */  
   ClassType:string,
      /**  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  */  
   BaseUOMCode:string,
      /**   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  */  
   DefUomCode:string,
      /**  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  */  
   Active:boolean,
      /**  Marks this UOMClass as global, available to be sent out to other companies.  */  
   GlobalUOMClass:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  */  
   DefaultUOMClass:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UOMClassListTableset{
   UOMClassList:Erp_Tablesets_UOMClassListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UOMClassRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  */  
   UOMClassID:string,
      /**  A decription for the UOMClass.  Mandatory.  */  
   Description:string,
      /**   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  */  
   ClassType:string,
      /**  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  */  
   BaseUOMCode:string,
      /**   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  */  
   DefUomCode:string,
      /**  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  */  
   Active:boolean,
      /**  Marks this UOMClass as global, available to be sent out to other companies.  */  
   GlobalUOMClass:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  */  
   DefaultUOMClass:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UOMClassTableset{
   UOMClass:Erp_Tablesets_UOMClassRow[],
   UOMConv:Erp_Tablesets_UOMConvRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UOMConvRow{
      /**  Company Identifier  */  
   Company:string,
      /**  The UOM Class ID that this unit of measure belongs to.  */  
   UOMClassID:string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   UOMCode:string,
      /**   Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.

Factors defined in UOMConv are not specific to any individual part and are considered standard  conversions. The relationship between Inches (in), and  Feet (ft) is a good example. 
Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table.  */  
   ConvFactor:number,
      /**  Long Description of a unit of measure. Mandatory.  */  
   UOMDesc:string,
      /**  used only during the 8.3 to 9.0 conversion process.  */  
   BaseUOM83:boolean,
      /**  Used only for the 8.3 to 9.0 conversion. Holds the original code that was used in 8.3. By changing the UOMCode the user can instruct the system to  convert the old 8.3 value to the new UOMCode value.  Example Ea to EACH or E to EACH.  */  
   UOMCode83:string,
      /**  Indicates if the UOM is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  */  
   Active:boolean,
      /**  Optional Symbol that can be used in place of the UOMCode such as when printing external documents or certain displays. Especially useful to express a UOM using subscripts or superscripts which would be hard to use as a UOMCode due to difficultly of keying into transactions.  */  
   UOMSymbol:string,
      /**   Indicates if fractional quantities are allowed with this unit of measure.
If true, then NumOfDec and Rounding fields will be enabled and Precison must have a value greater than zero. 
Replaces the 8.03.400 Part.WholeUnit.  */  
   AllowDecimals:boolean,
      /**   Defines how many decimal points are allowed with this UOM.
Disabled and set to zero if UOMConv.AllowDecimals = False. Enabled and must be > 0 if UOMConv.AllowDecimals = True. Not only does this validate quantity entered but also used in UOM quantity conversion logic.  */  
   NumOfDec:number,
      /**  If AllowDec = True,  then the following options are available; RND-  Round, Up-Round UP, DWN-Round Down.  */  
   Rounding:string,
      /**  System set, indicates if this UOMConv exists in a Standard UOMClass. (UOMClass.ClassType <> "Other"). Used to provide list of UOMs when a UOMClass, or Target UOMCode is not known. Ex: Creating a JobMtl record against a non-part item. In this case all UOMConv where StdUOM = true are valid. It is also used during the UOMConv maint process.  Not allowed to create a UOMConv with with a UOMCode that exists in another standard UOMClass.  */  
   StdUOM:boolean,
      /**   Indicates if Part Specific Conversion factors are required. This can only set to true with ClassType = "Other". Setting this to true, disables entry of the UOM Conversion factors from within the UOM maint. In this case conversion factors of the uoms are relative to the Part and will be enter in Part maint.
Example: You stock in Sheets, Purchase in Lbs, and consume in Square Feet.  Since the number of Lbs and SqFt in a sheet are relative to a part they would be marked as PartSpecific = true.  */  
   PartSpecific:boolean,
      /**  This indicates that this UOM Conv has been used somewhere.  Therefore we do not want to allow the associated conversion to change.  */  
   HasBeenUsed:boolean,
      /**   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  */  
   ConvOperator:string,
      /**  Marks this UOMConv as global, available to be sent out to other companies.  */  
   GlobalUOMConv:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Signifies this is the Base UOM for this Class  */  
   BaseUOM:boolean,
      /**  Qualifies that 1 of this uom = ConvFactor in ConvToUOM. Example: 12in = 1ft or 1ft = 12in  */  
   ConvFromUOM:string,
      /**  Qualifies UOM of the ConvFactor. This either the UOMClass.BaseUOM or the UOMConv.UOMCode depending on the value of ConvOperator.  */  
   ConvToUOM:string,
      /**  Sets a flag to determine whether this is the default UOM for this Class.  */  
   DefaultUOM:boolean,
      /**  Display field for BaseUOMCode  */  
   DispBaseUOMCode:string,
      /**  Flag which determines whether we should enable the BaseUOM field.  The rule is, if the current BaseUOM has the field HasBeenUsed = true, we shouldn't allow them to change the BaseUOM.  */  
   EnableBaseUOM:boolean,
      /**  Used to input/display the package code related to the UOMClass/UOM (stored in table PackingUOM).  */  
   DispPkgCode:string,
      /**  Description of the PkgCode  */  
   DispPkgCodeDesc:string,
      /**  Indicates the display sequence of the packaging in relation to the other packaging for the UOMClass  */  
   DispPkgDisplaySeq:number,
      /**  Indicates if the PkgCode is the default.  */  
   DispPkgIsDefault:boolean,
      /**  Indicates if the package code will be displayed in the application.If false, the package codes that are not valid for the MFG process on the shop floor (MES) are hidden.  */  
   DispPkgDisplayHidden:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtUOMClassTableset{
   UOMClass:Erp_Tablesets_UOMClassRow[],
   UOMConv:Erp_Tablesets_UOMConvRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param uoMClassID
   */  
export interface GetByID_input{
   uoMClassID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_UOMClassTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_UOMClassTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_UOMClassTableset[],
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
   returnObj:Erp_Tablesets_UOMClassListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewUOMClass_input{
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface GetNewUOMClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param ds
      @param uoMClassID
   */  
export interface GetNewUOMConv_input{
   ds:Erp_Tablesets_UOMClassTableset[],
   uoMClassID:string,
}

export interface GetNewUOMConv_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param whereClauseUOMClass
      @param whereClauseUOMConv
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseUOMClass:string,
   whereClauseUOMConv:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_UOMClassTableset[],
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
      @param uomClassID
      @param uomCode
      @param newAllowDec
      @param ds
   */  
export interface OnChangeAllowDecimal_input{
      /**  UOMClassID  */  
   uomClassID:string,
      /**  UOMCode  */  
   uomCode:string,
      /**  Proposed value for AllowDec  */  
   newAllowDec:boolean,
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface OnChangeAllowDecimal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param uomClassID
      @param uomCode
      @param newBaseUOM
      @param ds
   */  
export interface OnChangeBaseUOM_input{
      /**  UOMClassID.  */  
   uomClassID:string,
      /**  Old UOMCode  */  
   uomCode:string,
      /**  Proposed BaseUOMCode  */  
   newBaseUOM:boolean,
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface OnChangeBaseUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param uomClassID
      @param newClassType
      @param ds
   */  
export interface OnChangeClassType_input{
      /**  UOMClassID.  */  
   uomClassID:string,
      /**  Proposed ClassType.  */  
   newClassType:string,
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface OnChangeClassType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param uomClassID
      @param uomCode
      @param newDispPkgDisplaySeq
      @param ds
   */  
export interface OnChangeDispPkgDisplaySeq_input{
      /**  UOMClassID.  */  
   uomClassID:string,
      /**  UOMCode  */  
   uomCode:string,
   newDispPkgDisplaySeq:number,
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface OnChangeDispPkgDisplaySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param uomClassID
      @param uomCode
      @param pkgCode
      @param ds
   */  
export interface OnChangePkgCode_input{
      /**  UOMClassID.  */  
   uomClassID:string,
      /**  UOMCode  */  
   uomCode:string,
   pkgCode:string,
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface OnChangePkgCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param uomCode
      @param ds
   */  
export interface OnChangeUOMCode_input{
      /**  Proposed UOMCode.  */  
   uomCode:string,
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface OnChangeUOMCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtUOMClassTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtUOMClassTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_UOMClassTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UOMClassTableset[],
}
}

   /** Required : 
      @param ipUOMClassID
      @param OP_Result
   */  
export interface ValidateUOMClassId_input{
   ipUOMClassID:string,
   OP_Result:boolean,
}

export interface ValidateUOMClassId_output{
parameters : {
      /**  output parameters  */  
   OP_Result:boolean,
}
}

