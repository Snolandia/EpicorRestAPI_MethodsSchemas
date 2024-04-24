import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ARLOCSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/$metadata", {
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
   Description: Get ARLOCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARLOCs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCRow
   */  
export function get_ARLOCs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARLOCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARLOCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARLOCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARLOCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs", {
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
   Summary: Calls GetByID to retrieve the ARLOC item
   Description: Calls GetByID to retrieve the ARLOC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARLOC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARLOCRow
   */  
export function get_ARLOCs_Company_LCID(Company:string, LCID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARLOCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARLOCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARLOC for the service
   Description: Calls UpdateExt to update ARLOC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARLOC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARLOCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARLOCs_Company_LCID(Company:string, LCID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")", {
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
   Summary: Call UpdateExt to delete ARLOC item
   Description: Call UpdateExt to delete ARLOC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARLOC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARLOCs_Company_LCID(Company:string, LCID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")", {
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
   Description: Get ARLOCAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARLOCAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCAttchRow
   */  
export function get_ARLOCs_Company_LCID_ARLOCAttches(Company:string, LCID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")/ARLOCAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARLOCAttch item
   Description: Calls GetByID to retrieve the ARLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARLOCAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   */  
export function get_ARLOCs_Company_LCID_ARLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ARLOCAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARLOCAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCAttchRow
   */  
export function get_ARLOCAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARLOCAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARLOCAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches", {
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
   Summary: Calls GetByID to retrieve the ARLOCAttch item
   Description: Calls GetByID to retrieve the ARLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARLOCAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   */  
export function get_ARLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARLOCAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARLOCAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARLOCAttch for the service
   Description: Calls UpdateExt to update ARLOCAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARLOCAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ARLOCAttch item
   Description: Call UpdateExt to delete ARLOCAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARLOCAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LCID Desc: LCID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARLOCAttches_Company_LCID_DrawingSeq(Company:string, LCID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCListRow)
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
export function get_GetRows(whereClauseARLOC:string, whereClauseARLOCAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseARLOC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARLOC=" + whereClauseARLOC
   }
   if(typeof whereClauseARLOCAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARLOCAttch=" + whereClauseARLOCAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetRows" + params, {
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
export function get_GetByID(lcID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof lcID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lcID=" + lcID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetList" + params, {
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
   Summary: Invoke method ChangeBTCustID
   Description: This method returns the Bill To customer info.
   OperationID: ChangeBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBTCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ChangeBTCustID", {
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
   Summary: Invoke method ChangeCurrencyCode
   Description: Called when the CurrencyCode field has been changed.
   OperationID: ChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ChangeCurrencyCode", {
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
   Summary: Invoke method ChangeDocLCValue
   Description: Called when the DocLCValue field has been changed.
   OperationID: ChangeDocLCValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDocLCValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDocLCValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDocLCValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ChangeDocLCValue", {
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
   Summary: Invoke method ChangeExchangeRate
   Description: Called when the ExchangeRate field has been changed.
   OperationID: ChangeExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeExchangeRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ChangeExchangeRate", {
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
   Summary: Invoke method ChangeIssueDate
   Description: Called when the IssueDate field has been changed.
   OperationID: ChangeIssueDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeIssueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIssueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeIssueDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ChangeIssueDate", {
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
   Summary: Invoke method GetARLOCInvoices
   Description: This method will retrieve all the information related to AR Invoices.
   OperationID: GetARLOCInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARLOCInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARLOCInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARLOCInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetARLOCInvoices", {
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
   Summary: Invoke method GetARLOCSOrders
   Description: This method will retrieve all the information related to Sales Orders.
   OperationID: GetARLOCSOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARLOCSOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARLOCSOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARLOCSOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetARLOCSOrders", {
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
   Summary: Invoke method GetAvailBTList
   Description: This procedure returns a list of Alternate Bill To Customer for a Customer.
   OperationID: GetAvailBTList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailBTList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailBTList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailBTList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetAvailBTList", {
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
   Summary: Invoke method OnChangeOfDocLCValue
   Description: Called when changing the DocLCValue field.
   OperationID: OnChangeOfDocLCValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfDocLCValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfDocLCValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfDocLCValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/OnChangeOfDocLCValue", {
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
   Summary: Invoke method OnChangeOfFromDate
   Description: Called when changing the FromDate field.
   OperationID: OnChangeOfFromDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfFromDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFromDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfFromDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/OnChangeOfFromDate", {
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
   Summary: Invoke method OnChangeOfToDate
   Description: Called when changing the ToDate field.
   OperationID: OnChangeOfToDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfToDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfToDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfToDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/OnChangeOfToDate", {
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
   Summary: Invoke method GetNewARLOC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARLOC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARLOC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetNewARLOC", {
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
   Summary: Invoke method GetNewARLOCAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARLOCAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARLOCAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARLOCAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARLOCAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetNewARLOCAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARLOCAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARLOCListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARLOCRow[],
}

export interface Erp_Tablesets_ARLOCAttchRow{
   "Company":string,
   "LCID":string,
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

export interface Erp_Tablesets_ARLOCListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Letter of Credit ID.  */  
   "LCID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Monetary value of the Letter of Credit.  */  
   "LCValue":number,
      /**  Monetary value of the Letter of Credit. Report Currency 1.  */  
   "Rpt1LCValue":number,
      /**  Monetary value of the Letter of Credit. Report Currency 2.  */  
   "Rpt2LCValue":number,
      /**  Monetary value of the Letter of Credit. Report Currency 3.  */  
   "Rpt3LCValue":number,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Exchange Rate Lock flag  */  
   "RateLocked":boolean,
      /**  Date that Letter of Credit was issued.  */  
   "IssueDate":string,
      /**  Valid From date.  */  
   "FromDate":string,
      /**  Valid To date.  */  
   "ToDate":string,
      /**  Letter of Credit Description.  */  
   "Description":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Name of the Letter of Credit Guarantor.  */  
   "GuarantorName":string,
      /**  Terms code  */  
   "TermsCode":string,
      /**  Ship Complete flag  */  
   "ShipComplete":boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   "Inactive":boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   "InactiveReason":string,
      /**  If true, Letter of Credit is closed.  */  
   "Closed":boolean,
      /**  Optional.  */  
   "FOB":string,
      /**  Free form text.  */  
   "IssuanceType":string,
      /**  Free form text.  */  
   "PackListCopies":string,
      /**  Free form text.  */  
   "PlaceOfLoading":string,
      /**  Free form text comments.  */  
   "Comment":string,
      /**  Unique identifier.  */  
   "RateGrpCode":string,
      /**  LC = Letter of Credit, ECG = Export Credit Guarantee  */  
   "Type":string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   "DocLCValue":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
      /**  Bill To Customer ID  */  
   "BTCustID":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
   "CurrencySwitch":boolean,
      /**  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  */  
   "InUse":boolean,
   "OpenLCCredit":number,
   "OpenOrderValue":number,
   "CumInvoices":number,
      /**  Cumulative Invoices  */  
   "DocCumInvoices":number,
      /**  Invoices Balance  */  
   "DocInvoiceBal":number,
      /**  Open LC Credit  */  
   "DocOpenLCCredit":number,
      /**  Open Order Value  */  
   "DocOpenOrderValue":number,
      /**  Paid Invoice Value  */  
   "DocPaidInvoiceValue":number,
      /**  Total Order Value  */  
   "DocTotalOrderValue":number,
      /**  Invoices Balance  */  
   "InvoiceBal":number,
      /**  Paid Invoice Value  */  
   "PaidInvoiceValue":number,
      /**  Total Order Value  */  
   "TotalOrderValue":number,
      /**  Cumulative Invoices  */  
   "Rpt1CumInvoices":number,
      /**  Cumulative Invoices  */  
   "Rpt2CumInvoices":number,
      /**  Cumulative Invoices  */  
   "Rpt3CumInvoices":number,
      /**  Invoices Balance  */  
   "Rpt1InvoiceBal":number,
      /**  Invoices Balance  */  
   "Rpt2InvoiceBal":number,
      /**  Invoices Balance  */  
   "Rpt3InvoiceBal":number,
      /**  Open LC Credit  */  
   "Rpt1OpenLCCredit":number,
      /**  Open LC Credit  */  
   "Rpt2OpenLCCredit":number,
      /**  Open LC Credit  */  
   "Rpt3OpenLCCredit":number,
      /**  Open Order Value  */  
   "Rpt2OpenOrderValue":number,
      /**  Open Order Value  */  
   "Rpt1OpenOrderValue":number,
      /**  Open Order Value  */  
   "Rpt3OpenOrderValue":number,
      /**  Paid Invoice Value  */  
   "Rpt1PaidInvoiceValue":number,
      /**  Paid Invoice Value  */  
   "Rpt2PaidInvoiceValue":number,
      /**  Paid Invoice Value  */  
   "Rpt3PaidInvoiceValue":number,
      /**  Total Order Value  */  
   "Rpt1TotalOrderValue":number,
      /**  Total Order Value  */  
   "Rpt2TotalOrderValue":number,
      /**  Total Order Value  */  
   "Rpt3TotalOrderValue":number,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrDocumentDesc":string,
      /**  Description of the currency  */  
   "BaseCurrCurrDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrCurrName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "BTCustNumCustID":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "BTCustNumBTName":string,
      /**  The full name of the customer.  */  
   "BTCustNumName":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   "TermsCodeDescription":string,
   "CumInvoicesCurrent":number,
      /**  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  */  
   "LCValueCurrent":number,
   "OpenLCCreditCurrent":number,
   "OpenOrderValueCurrent":number,
   "UseExchangeRate":string,
      /**  Invoices Balance converted from document cuurency using current (today) exchange rate  */  
   "InvoiceBalCurrent":number,
      /**  Paid Invoice Value in base currency converted from the amount in doc currency using current (now) exchange rate  */  
   "PaidInvoiceValueCurrent":number,
      /**  Total Order value converted from amount in doc currency using current (now) exchange rate  */  
   "TotalOrderValueCurrent":number,
      /**  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  */  
   "Rpt1LCValueCurrent":number,
      /**  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  */  
   "Rpt2LCValueCurrent":number,
      /**  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  */  
   "Rpt3LCValueCurrent":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARLOCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Letter of Credit ID.  */  
   "LCID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Monetary value of the Letter of Credit.  */  
   "LCValue":number,
      /**  Monetary value of the Letter of Credit. Report Currency 1.  */  
   "Rpt1LCValue":number,
      /**  Monetary value of the Letter of Credit. Report Currency 2.  */  
   "Rpt2LCValue":number,
      /**  Monetary value of the Letter of Credit. Report Currency 3.  */  
   "Rpt3LCValue":number,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Exchange Rate Lock flag  */  
   "RateLocked":boolean,
      /**  Date that Letter of Credit was issued.  */  
   "IssueDate":string,
      /**  Valid From date.  */  
   "FromDate":string,
      /**  Valid To date.  */  
   "ToDate":string,
      /**  Letter of Credit Description.  */  
   "Description":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Name of the Letter of Credit Guarantor.  */  
   "GuarantorName":string,
      /**  Terms code  */  
   "TermsCode":string,
      /**  Ship Complete flag  */  
   "ShipComplete":boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   "Inactive":boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   "InactiveReason":string,
      /**  If true, Letter of Credit is closed.  */  
   "Closed":boolean,
      /**  Optional.  */  
   "FOB":string,
      /**  Free form text.  */  
   "IssuanceType":string,
      /**  Free form text.  */  
   "PackListCopies":string,
      /**  Free form text.  */  
   "PlaceOfLoading":string,
      /**  Free form text comments.  */  
   "Comment":string,
      /**  Unique identifier.  */  
   "RateGrpCode":string,
      /**  LC = Letter of Credit, ECG = Export Credit Guarantee  */  
   "Type":string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   "DocLCValue":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
      /**  Bill To Customer ID  */  
   "BTCustID":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
   "CurrencySwitch":boolean,
      /**  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  */  
   "InUse":boolean,
   "OpenLCCredit":number,
   "OpenOrderValue":number,
   "CumInvoices":number,
      /**  Cumulative Invoices  */  
   "DocCumInvoices":number,
      /**  Invoices Balance  */  
   "DocInvoiceBal":number,
      /**  Open LC Credit  */  
   "DocOpenLCCredit":number,
      /**  Open Order Value  */  
   "DocOpenOrderValue":number,
      /**  Paid Invoice Value  */  
   "DocPaidInvoiceValue":number,
      /**  Total Order Value  */  
   "DocTotalOrderValue":number,
      /**  Invoices Balance  */  
   "InvoiceBal":number,
      /**  Paid Invoice Value  */  
   "PaidInvoiceValue":number,
      /**  Total Order Value  */  
   "TotalOrderValue":number,
      /**  Cumulative Invoices  */  
   "Rpt1CumInvoices":number,
      /**  Cumulative Invoices  */  
   "Rpt2CumInvoices":number,
      /**  Cumulative Invoices  */  
   "Rpt3CumInvoices":number,
      /**  Invoices Balance  */  
   "Rpt1InvoiceBal":number,
      /**  Invoices Balance  */  
   "Rpt2InvoiceBal":number,
      /**  Invoices Balance  */  
   "Rpt3InvoiceBal":number,
      /**  Open LC Credit  */  
   "Rpt1OpenLCCredit":number,
      /**  Open LC Credit  */  
   "Rpt2OpenLCCredit":number,
      /**  Open LC Credit  */  
   "Rpt3OpenLCCredit":number,
      /**  Open Order Value  */  
   "Rpt2OpenOrderValue":number,
      /**  Open Order Value  */  
   "Rpt1OpenOrderValue":number,
      /**  Open Order Value  */  
   "Rpt3OpenOrderValue":number,
      /**  Paid Invoice Value  */  
   "Rpt1PaidInvoiceValue":number,
      /**  Paid Invoice Value  */  
   "Rpt2PaidInvoiceValue":number,
      /**  Paid Invoice Value  */  
   "Rpt3PaidInvoiceValue":number,
      /**  Total Order Value  */  
   "Rpt1TotalOrderValue":number,
      /**  Total Order Value  */  
   "Rpt2TotalOrderValue":number,
      /**  Total Order Value  */  
   "Rpt3TotalOrderValue":number,
   "TermsCodeDescription":string,
   "Currency":string,
   "UseExchangeRate":string,
      /**  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  */  
   "LCValueCurrent":number,
      /**  Open LOC Credit in base currency converted from Open LOC Credit in Document currency using current (today) exchange rate  */  
   "OpenLCCreditCurrent":number,
      /**  Open Order Value in base currency converted from the amount in document currency using the current (now) exchange rate  */  
   "OpenOrderValueCurrent":number,
   "CumInvoicesCurrent":number,
      /**  Invoices Balance converted from document cuurency using current (today) exchange rate  */  
   "InvoiceBalCurrent":number,
      /**  Paid Invoice Value in base currency converted from amount in doc currency using the current (now) exchange rate  */  
   "PaidInvoiceValueCurrent":number,
      /**  Total Order value converted from amount in doc currency using current (now) exchange rate  */  
   "TotalOrderValueCurrent":number,
      /**  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  */  
   "Rpt1LCValueCurrent":number,
      /**  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  */  
   "Rpt2LCValueCurrent":number,
      /**  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  */  
   "Rpt3LCValueCurrent":number,
   "BitFlag":number,
   "BaseCurrCurrSymbol":string,
   "BaseCurrCurrName":string,
   "BaseCurrDocumentDesc":string,
   "BaseCurrCurrencyID":string,
   "BaseCurrCurrDesc":string,
   "BTCustNumBTName":string,
   "BTCustNumCustID":string,
   "BTCustNumName":string,
   "CurrencyCodeBaseCurr":boolean,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrencyID":string,
   "CustomerCustID":string,
   "CustomerName":string,
   "FOBDescription":string,
   "ReasonDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param newBillToCustID
      @param ds
   */  
export interface ChangeBTCustID_input{
      /**  Proposed bill to custid  */  
   newBillToCustID:string,
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface ChangeBTCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeCurrencyCode_input{
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface ChangeCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDocLCValue_input{
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface ChangeDocLCValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeExchangeRate_input{
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface ChangeExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeIssueDate_input{
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface ChangeIssueDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param lcID
   */  
export interface DeleteByID_input{
   lcID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ARLOCAttchRow{
   Company:string,
   LCID:string,
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

export interface Erp_Tablesets_ARLOCInvcRow{
   ApplyDate:string,
   CurrencyCode:string,
   CurrencyName:string,
   DocInvoiceAmt:number,
   DocInvoiceBal:number,
   InvoiceAmt:number,
   InvoiceBal:number,
   InvoiceDate:string,
   InvoiceNum:number,
   LegalNumber:string,
   OpenInvoice:boolean,
   OrderNum:number,
   PONum:string,
   Rpt1InvoiceAmt:number,
   Rpt1InvoiceBal:number,
   Rpt2InvoiceAmt:number,
   Rpt2InvoiceBal:number,
   Rpt3InvoiceAmt:number,
   Rpt3InvoiceBal:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARLOCListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Letter of Credit ID.  */  
   LCID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Monetary value of the Letter of Credit.  */  
   LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 1.  */  
   Rpt1LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 2.  */  
   Rpt2LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 3.  */  
   Rpt3LCValue:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Exchange Rate Lock flag  */  
   RateLocked:boolean,
      /**  Date that Letter of Credit was issued.  */  
   IssueDate:string,
      /**  Valid From date.  */  
   FromDate:string,
      /**  Valid To date.  */  
   ToDate:string,
      /**  Letter of Credit Description.  */  
   Description:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Name of the Letter of Credit Guarantor.  */  
   GuarantorName:string,
      /**  Terms code  */  
   TermsCode:string,
      /**  Ship Complete flag  */  
   ShipComplete:boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   Inactive:boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   InactiveReason:string,
      /**  If true, Letter of Credit is closed.  */  
   Closed:boolean,
      /**  Optional.  */  
   FOB:string,
      /**  Free form text.  */  
   IssuanceType:string,
      /**  Free form text.  */  
   PackListCopies:string,
      /**  Free form text.  */  
   PlaceOfLoading:string,
      /**  Free form text comments.  */  
   Comment:string,
      /**  Unique identifier.  */  
   RateGrpCode:string,
      /**  LC = Letter of Credit, ECG = Export Credit Guarantee  */  
   Type:string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   DocLCValue:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
      /**  Bill To Customer ID  */  
   BTCustID:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
   CurrencySwitch:boolean,
      /**  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  */  
   InUse:boolean,
   OpenLCCredit:number,
   OpenOrderValue:number,
   CumInvoices:number,
      /**  Cumulative Invoices  */  
   DocCumInvoices:number,
      /**  Invoices Balance  */  
   DocInvoiceBal:number,
      /**  Open LC Credit  */  
   DocOpenLCCredit:number,
      /**  Open Order Value  */  
   DocOpenOrderValue:number,
      /**  Paid Invoice Value  */  
   DocPaidInvoiceValue:number,
      /**  Total Order Value  */  
   DocTotalOrderValue:number,
      /**  Invoices Balance  */  
   InvoiceBal:number,
      /**  Paid Invoice Value  */  
   PaidInvoiceValue:number,
      /**  Total Order Value  */  
   TotalOrderValue:number,
      /**  Cumulative Invoices  */  
   Rpt1CumInvoices:number,
      /**  Cumulative Invoices  */  
   Rpt2CumInvoices:number,
      /**  Cumulative Invoices  */  
   Rpt3CumInvoices:number,
      /**  Invoices Balance  */  
   Rpt1InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt2InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt3InvoiceBal:number,
      /**  Open LC Credit  */  
   Rpt1OpenLCCredit:number,
      /**  Open LC Credit  */  
   Rpt2OpenLCCredit:number,
      /**  Open LC Credit  */  
   Rpt3OpenLCCredit:number,
      /**  Open Order Value  */  
   Rpt2OpenOrderValue:number,
      /**  Open Order Value  */  
   Rpt1OpenOrderValue:number,
      /**  Open Order Value  */  
   Rpt3OpenOrderValue:number,
      /**  Paid Invoice Value  */  
   Rpt1PaidInvoiceValue:number,
      /**  Paid Invoice Value  */  
   Rpt2PaidInvoiceValue:number,
      /**  Paid Invoice Value  */  
   Rpt3PaidInvoiceValue:number,
      /**  Total Order Value  */  
   Rpt1TotalOrderValue:number,
      /**  Total Order Value  */  
   Rpt2TotalOrderValue:number,
      /**  Total Order Value  */  
   Rpt3TotalOrderValue:number,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrDocumentDesc:string,
      /**  Description of the currency  */  
   BaseCurrCurrDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrCurrName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   BTCustNumCustID:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   BTCustNumBTName:string,
      /**  The full name of the customer.  */  
   BTCustNumName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   TermsCodeDescription:string,
   CumInvoicesCurrent:number,
      /**  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  */  
   LCValueCurrent:number,
   OpenLCCreditCurrent:number,
   OpenOrderValueCurrent:number,
   UseExchangeRate:string,
      /**  Invoices Balance converted from document cuurency using current (today) exchange rate  */  
   InvoiceBalCurrent:number,
      /**  Paid Invoice Value in base currency converted from the amount in doc currency using current (now) exchange rate  */  
   PaidInvoiceValueCurrent:number,
      /**  Total Order value converted from amount in doc currency using current (now) exchange rate  */  
   TotalOrderValueCurrent:number,
      /**  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  */  
   Rpt1LCValueCurrent:number,
      /**  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  */  
   Rpt2LCValueCurrent:number,
      /**  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  */  
   Rpt3LCValueCurrent:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARLOCListTableset{
   ARLOCList:Erp_Tablesets_ARLOCListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARLOCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Letter of Credit ID.  */  
   LCID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Monetary value of the Letter of Credit.  */  
   LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 1.  */  
   Rpt1LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 2.  */  
   Rpt2LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 3.  */  
   Rpt3LCValue:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Exchange Rate Lock flag  */  
   RateLocked:boolean,
      /**  Date that Letter of Credit was issued.  */  
   IssueDate:string,
      /**  Valid From date.  */  
   FromDate:string,
      /**  Valid To date.  */  
   ToDate:string,
      /**  Letter of Credit Description.  */  
   Description:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Name of the Letter of Credit Guarantor.  */  
   GuarantorName:string,
      /**  Terms code  */  
   TermsCode:string,
      /**  Ship Complete flag  */  
   ShipComplete:boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   Inactive:boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   InactiveReason:string,
      /**  If true, Letter of Credit is closed.  */  
   Closed:boolean,
      /**  Optional.  */  
   FOB:string,
      /**  Free form text.  */  
   IssuanceType:string,
      /**  Free form text.  */  
   PackListCopies:string,
      /**  Free form text.  */  
   PlaceOfLoading:string,
      /**  Free form text comments.  */  
   Comment:string,
      /**  Unique identifier.  */  
   RateGrpCode:string,
      /**  LC = Letter of Credit, ECG = Export Credit Guarantee  */  
   Type:string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   DocLCValue:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
      /**  Bill To Customer ID  */  
   BTCustID:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
   CurrencySwitch:boolean,
      /**  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  */  
   InUse:boolean,
   OpenLCCredit:number,
   OpenOrderValue:number,
   CumInvoices:number,
      /**  Cumulative Invoices  */  
   DocCumInvoices:number,
      /**  Invoices Balance  */  
   DocInvoiceBal:number,
      /**  Open LC Credit  */  
   DocOpenLCCredit:number,
      /**  Open Order Value  */  
   DocOpenOrderValue:number,
      /**  Paid Invoice Value  */  
   DocPaidInvoiceValue:number,
      /**  Total Order Value  */  
   DocTotalOrderValue:number,
      /**  Invoices Balance  */  
   InvoiceBal:number,
      /**  Paid Invoice Value  */  
   PaidInvoiceValue:number,
      /**  Total Order Value  */  
   TotalOrderValue:number,
      /**  Cumulative Invoices  */  
   Rpt1CumInvoices:number,
      /**  Cumulative Invoices  */  
   Rpt2CumInvoices:number,
      /**  Cumulative Invoices  */  
   Rpt3CumInvoices:number,
      /**  Invoices Balance  */  
   Rpt1InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt2InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt3InvoiceBal:number,
      /**  Open LC Credit  */  
   Rpt1OpenLCCredit:number,
      /**  Open LC Credit  */  
   Rpt2OpenLCCredit:number,
      /**  Open LC Credit  */  
   Rpt3OpenLCCredit:number,
      /**  Open Order Value  */  
   Rpt2OpenOrderValue:number,
      /**  Open Order Value  */  
   Rpt1OpenOrderValue:number,
      /**  Open Order Value  */  
   Rpt3OpenOrderValue:number,
      /**  Paid Invoice Value  */  
   Rpt1PaidInvoiceValue:number,
      /**  Paid Invoice Value  */  
   Rpt2PaidInvoiceValue:number,
      /**  Paid Invoice Value  */  
   Rpt3PaidInvoiceValue:number,
      /**  Total Order Value  */  
   Rpt1TotalOrderValue:number,
      /**  Total Order Value  */  
   Rpt2TotalOrderValue:number,
      /**  Total Order Value  */  
   Rpt3TotalOrderValue:number,
   TermsCodeDescription:string,
   Currency:string,
   UseExchangeRate:string,
      /**  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  */  
   LCValueCurrent:number,
      /**  Open LOC Credit in base currency converted from Open LOC Credit in Document currency using current (today) exchange rate  */  
   OpenLCCreditCurrent:number,
      /**  Open Order Value in base currency converted from the amount in document currency using the current (now) exchange rate  */  
   OpenOrderValueCurrent:number,
   CumInvoicesCurrent:number,
      /**  Invoices Balance converted from document cuurency using current (today) exchange rate  */  
   InvoiceBalCurrent:number,
      /**  Paid Invoice Value in base currency converted from amount in doc currency using the current (now) exchange rate  */  
   PaidInvoiceValueCurrent:number,
      /**  Total Order value converted from amount in doc currency using current (now) exchange rate  */  
   TotalOrderValueCurrent:number,
      /**  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  */  
   Rpt1LCValueCurrent:number,
      /**  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  */  
   Rpt2LCValueCurrent:number,
      /**  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  */  
   Rpt3LCValueCurrent:number,
   BitFlag:number,
   BaseCurrCurrSymbol:string,
   BaseCurrCurrName:string,
   BaseCurrDocumentDesc:string,
   BaseCurrCurrencyID:string,
   BaseCurrCurrDesc:string,
   BTCustNumBTName:string,
   BTCustNumCustID:string,
   BTCustNumName:string,
   CurrencyCodeBaseCurr:boolean,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrencyID:string,
   CustomerCustID:string,
   CustomerName:string,
   FOBDescription:string,
   ReasonDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARLOCSORow{
   CurrencyCode:string,
   CurrencyName:string,
   DocOutSOValue:number,
   OpenOrder:boolean,
   OrderDate:string,
   OrderNum:number,
   OutSOValue:number,
   PoNum:string,
   Rpt1OutSOValue:number,
   Rpt2OutSOValue:number,
   Rpt3OutSOValue:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARLOCTableset{
   ARLOC:Erp_Tablesets_ARLOCRow[],
   ARLOCAttch:Erp_Tablesets_ARLOCAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARLOCTrackerTableset{
   ARLOCInvc:Erp_Tablesets_ARLOCInvcRow[],
   ARLOCSO:Erp_Tablesets_ARLOCSORow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtARLOCTableset{
   ARLOC:Erp_Tablesets_ARLOCRow[],
   ARLOCAttch:Erp_Tablesets_ARLOCAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param arlocid
   */  
export interface GetARLOCInvoices_input{
      /**  AR Letters Of Credit ID  */  
   arlocid:string,
}

export interface GetARLOCInvoices_output{
   returnObj:Erp_Tablesets_ARLOCTrackerTableset[],
}

   /** Required : 
      @param arlocid
   */  
export interface GetARLOCSOrders_input{
      /**  AR Letters Of Credit ID  */  
   arlocid:string,
}

export interface GetARLOCSOrders_output{
   returnObj:Erp_Tablesets_ARLOCTrackerTableset[],
}

   /** Required : 
      @param pcCurComp
      @param piCustNum
      @param pcCustID
   */  
export interface GetAvailBTList_input{
      /**  Current Company  */  
   pcCurComp:string,
      /**  Customer Number  */  
   piCustNum:number,
      /**  Customer ID  */  
   pcCustID:string,
}

export interface GetAvailBTList_output{
parameters : {
      /**  output parameters  */  
   cBillToList:string,
}
}

   /** Required : 
      @param lcID
   */  
export interface GetByID_input{
   lcID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARLOCTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARLOCTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARLOCTableset[],
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
   returnObj:Erp_Tablesets_ARLOCListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param lcID
   */  
export interface GetNewARLOCAttch_input{
   ds:Erp_Tablesets_ARLOCTableset[],
   lcID:string,
}

export interface GetNewARLOCAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewARLOC_input{
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface GetNewARLOC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param whereClauseARLOC
      @param whereClauseARLOCAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseARLOC:string,
   whereClauseARLOCAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARLOCTableset[],
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
      @param proposedLCValue
      @param ds
   */  
export interface OnChangeOfDocLCValue_input{
      /**  Proposed From Date  */  
   proposedLCValue:number,
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface OnChangeOfDocLCValue_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param proposedFromDate
      @param ds
   */  
export interface OnChangeOfFromDate_input{
      /**  Proposed From Date  */  
   proposedFromDate:string,
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface OnChangeOfFromDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param proposedToDate
      @param ds
   */  
export interface OnChangeOfToDate_input{
      /**  Proposed To Date  */  
   proposedToDate:string,
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface OnChangeOfToDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtARLOCTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARLOCTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARLOCTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARLOCTableset[],
}
}

