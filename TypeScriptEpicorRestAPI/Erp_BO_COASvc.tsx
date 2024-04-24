import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.COASvc
// Description: Chart of Accounts structure maintenance application
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/$metadata", {
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
   Description: Get COAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COAs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COARow
   */  
export function get_COAs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COAs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COAs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs", {
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
   Summary: Calls GetByID to retrieve the COA item
   Description: Calls GetByID to retrieve the COA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COARow
   */  
export function get_COAs_Company_COACode(Company:string, COACode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COA for the service
   Description: Calls UpdateExt to update COA. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COAs_Company_COACode(Company:string, COACode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")", {
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
   Summary: Call UpdateExt to delete COA item
   Description: Call UpdateExt to delete COA item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COAs_Company_COACode(Company:string, COACode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")", {
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
   Description: Get COASegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentRow
   */  
export function get_COAs_Company_COACode_COASegments(Company:string, COACode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")/COASegments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the COASegment item
   Description: Calls GetByID to retrieve the COASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   */  
export function get_COAs_Company_COACode_COASegments_Company_COACode_SegmentNbr(Company:string, COACode:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get COASegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentRow
   */  
export function get_COASegments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COASegments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments", {
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
   Summary: Calls GetByID to retrieve the COASegment item
   Description: Calls GetByID to retrieve the COASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   */  
export function get_COASegments_Company_COACode_SegmentNbr(Company:string, COACode:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COASegment for the service
   Description: Calls UpdateExt to update COASegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COASegments_Company_COACode_SegmentNbr(Company:string, COACode:string, SegmentNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")", {
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
   Summary: Call UpdateExt to delete COASegment item
   Description: Call UpdateExt to delete COASegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COASegments_Company_COACode_SegmentNbr(Company:string, COACode:string, SegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")", {
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
   Description: Get COASegmentNotCreateds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegmentNotCreateds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentNotCreatedRow
   */  
export function get_COASegmentNotCreateds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentNotCreatedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentNotCreatedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegmentNotCreateds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COASegmentNotCreateds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds", {
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
   Summary: Calls GetByID to retrieve the COASegmentNotCreated item
   Description: Calls GetByID to retrieve the COASegmentNotCreated item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegmentNotCreated
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
   */  
export function get_COASegmentNotCreateds_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegmentNotCreatedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegmentNotCreatedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COASegmentNotCreated for the service
   Description: Calls UpdateExt to update COASegmentNotCreated. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegmentNotCreated
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COASegmentNotCreateds_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete COASegmentNotCreated item
   Description: Call UpdateExt to delete COASegmentNotCreated item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegmentNotCreated
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COASegmentNotCreateds_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow)
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
export function get_GetRows(whereClauseCOA:string, whereClauseCOASegment:string, whereClauseCOASegmentNotCreated:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCOA!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOA=" + whereClauseCOA
   }
   if(typeof whereClauseCOASegment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOASegment=" + whereClauseCOASegment
   }
   if(typeof whereClauseCOASegmentNotCreated!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOASegmentNotCreated=" + whereClauseCOASegmentNotCreated
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetRows" + params, {
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
export function get_GetByID(coACode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof coACode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "coACode=" + coACode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetByID" + params, {
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
   Summary: Invoke method GetCOAGlobalFields
   OperationID: GetCOAGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOAGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOAGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOAGlobalFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetCOAGlobalFields", {
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
   Summary: Invoke method GetCOASegmentGlobalFields
   OperationID: GetCOASegmentGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegmentGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegmentGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOASegmentGlobalFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetCOASegmentGlobalFields", {
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
   Summary: Invoke method BuildCOASegmentList
   Description: Build list of segment numbers/names
   OperationID: BuildCOASegmentList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCOASegmentList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCOASegmentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildCOASegmentList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/BuildCOASegmentList", {
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
   Summary: Invoke method GetByIDOrdered
   Description: Returns COATableset object by requested COACode for Kinetic
   OperationID: GetByIDOrdered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDOrdered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDOrdered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDOrdered(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetByIDOrdered", {
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
   Summary: Invoke method ChangeCOAGlobalCOA
   Description: Method to call when changing the global COA flag on a COA.
Assigns the GlbFlag base on the new value.
   OperationID: ChangeCOAGlobalCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOAGlobalCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOAGlobalCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCOAGlobalCOA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ChangeCOAGlobalCOA", {
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
   Summary: Invoke method ChangeCOASegmentGlobalCOASegment
   Description: Method to call when changing the global COA Segment flag on a COASegment.
Assigns the GlbFlag base on the new value.
   OperationID: ChangeCOASegmentGlobalCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOASegmentGlobalCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOASegmentGlobalCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCOASegmentGlobalCOASegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ChangeCOASegmentGlobalCOASegment", {
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
   Summary: Invoke method ChangeGlobalValuesLock
   Description: Method call when changing the Global Values Lock flag on a segment.
   OperationID: ChangeGlobalValuesLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGlobalValuesLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlobalValuesLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGlobalValuesLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ChangeGlobalValuesLock", {
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
   Summary: Invoke method ChangeSiteSegment
   Description: This method should be called when COASegment SiteSegment changes
   OperationID: ChangeSiteSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSiteSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSiteSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSiteSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ChangeSiteSegment", {
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
   Summary: Invoke method IsSegValInUse
   Description: Determine if a specific segment value has been used in either a GLAccount
or on a GLJrnDtl.
   OperationID: IsSegValInUse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsSegValInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsSegValInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsSegValInUse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/IsSegValInUse", {
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
   Summary: Invoke method CheckAllowAlpha
   Description: Check to see if the segment can have the alpha seg values set to no.
   OperationID: CheckAllowAlpha
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAllowAlpha_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAllowAlpha_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAllowAlpha(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckAllowAlpha", {
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
   Summary: Invoke method CheckCOALengthWithSegment
   Description: Calculate the total length of the COA (sum of the COASegment.Maxlength)
   OperationID: CheckCOALengthWithSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOALengthWithSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOALengthWithSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCOALengthWithSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckCOALengthWithSegment", {
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
   Summary: Invoke method CheckChartLength
   Description: Calculate the total length of the COA (sum of the COASegment.Maxlength)
   OperationID: CheckChartLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChartLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChartLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckChartLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckChartLength", {
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
   Summary: Invoke method CheckConsolidatedCOA
   Description: Determine if the COA has a consolidation definition
   OperationID: CheckConsolidatedCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConsolidatedCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsolidatedCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConsolidatedCOA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckConsolidatedCOA", {
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
   Summary: Invoke method IsCOAMasterCOA
   Description: Determine if the COA is the Master COA
   OperationID: IsCOAMasterCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsCOAMasterCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCOAMasterCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsCOAMasterCOA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/IsCOAMasterCOA", {
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
   Summary: Invoke method IsChartUsedInTransaction
   Description: Determine if the Chart has be used by a transaction
   OperationID: IsChartUsedInTransaction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsChartUsedInTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsChartUsedInTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsChartUsedInTransaction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/IsChartUsedInTransaction", {
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
   Summary: Invoke method IsChartInUse
   Description: Checks if COA is assigned to a GLBook or a GLAccount record exists for the COA.
   OperationID: IsChartInUse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsChartInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsChartInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsChartInUse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/IsChartInUse", {
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
   Summary: Invoke method CheckBalanceChange
   Description: Determines if a balance segment is changing, and if it is, checks
if a budget is setup.  If it is, and the number of balance segments are
being increased, informs the user the budgets may be invalid with this change.
   OperationID: CheckBalanceChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBalanceChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBalanceChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBalanceChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckBalanceChange", {
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
   Summary: Invoke method CheckDynamic
   Description: Ensure the natural account is not flagged as a dynamic segment
   OperationID: CheckDynamic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDynamic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDynamic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDynamic(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckDynamic", {
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
   Summary: Invoke method CheckIfDeletingLastSegment
   Description: Used to determine if the user is deleting the last defined segment or a previous one.
If the segment is not the last defined, then the delete process must resequence all existing
segment records and their associated records including the segment values.
The overhead that may be associated with this operation has the potential to be huge
so we will make sure this is what the user really wants.
   OperationID: CheckIfDeletingLastSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfDeletingLastSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfDeletingLastSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfDeletingLastSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckIfDeletingLastSegment", {
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
   Summary: Invoke method CheckIfSegmentHasValues
   Description: Used to determine if the user is deleting the segment having values.
   OperationID: CheckIfSegmentHasValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfSegmentHasValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfSegmentHasValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfSegmentHasValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckIfSegmentHasValues", {
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
   Summary: Invoke method CheckRebuildBalances
   OperationID: CheckRebuildBalances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRebuildBalances_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRebuildBalances_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRebuildBalances(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckRebuildBalances", {
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
   Summary: Invoke method CheckSeparatorChar
   Description: Validate the separator character
   OperationID: CheckSeparatorChar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSeparatorChar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSeparatorChar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSeparatorChar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckSeparatorChar", {
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
   Summary: Invoke method CheckUseRefEntity
   Description: Validates COASegment reference entity related fields
   OperationID: CheckUseRefEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckUseRefEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUseRefEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckUseRefEntity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckUseRefEntity", {
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
   Summary: Invoke method COAStructureChange
   Description: Resync the temp table due to a COA structure change
   OperationID: COAStructureChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COAStructureChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COAStructureChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COAStructureChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAStructureChange", {
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
   Summary: Invoke method COAExists
   OperationID: COAExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COAExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COAExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COAExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAExists", {
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
   Summary: Invoke method DeleteAndRenumberSegments
   Description: Deletes requested segment number and renumbers the remaining.  For example,
chart has 3 segments and segment 2 is deleted.  This method renumbers segment3 as
segment 2.  The segment write trigger updates subordinate tables.
   OperationID: DeleteAndRenumberSegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAndRenumberSegments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAndRenumberSegments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAndRenumberSegments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/DeleteAndRenumberSegments", {
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
   Summary: Invoke method MoveOnePosition
   Description: This method moves the COASegment Display Order Up/Down one position in the
grid and returns the whole updated datatable.
   OperationID: MoveOnePosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveOnePosition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/MoveOnePosition", {
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
   Summary: Invoke method PromptAutoCreateDynSegVals
   Description: Ask the user if the COASegValues entries are to be created when the
COASegment record is saved.
   OperationID: PromptAutoCreateDynSegVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PromptAutoCreateDynSegVals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptAutoCreateDynSegVals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PromptAutoCreateDynSegVals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/PromptAutoCreateDynSegVals", {
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
   Summary: Invoke method SetRefEntityFields
   Description: Set COASegment Reference Entity related fields based upon the value of COASegment.RefEntity
   OperationID: SetRefEntityFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetRefEntityFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetRefEntityFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetRefEntityFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/SetRefEntityFields", {
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
   Summary: Invoke method UpdateCOADynamicSegValues
   Description: Update the COASegValues for the requested dynamic segment
   OperationID: UpdateCOADynamicSegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCOADynamicSegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCOADynamicSegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCOADynamicSegValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/UpdateCOADynamicSegValues", {
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
   Summary: Invoke method UpdateDynamicSegment
   Description: Updates the fields associated with the Dynamic setting.
   OperationID: UpdateDynamicSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDynamicSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDynamicSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDynamicSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/UpdateDynamicSegment", {
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
   Summary: Invoke method UpdateNatural
   Description: Updates the fields associated with the Global COA setting.
   OperationID: UpdateNatural
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateNatural_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNatural_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateNatural(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/UpdateNatural", {
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
   Summary: Invoke method UpdateFieldLength
   Description: Updates SegValueFieldLength based on new SegValueField value.
   OperationID: UpdateFieldLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateFieldLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFieldLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateFieldLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/UpdateFieldLength", {
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
   Summary: Invoke method ValidateEntryControl
   Description: Validate entry control
   OperationID: ValidateEntryControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEntryControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEntryControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateEntryControl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ValidateEntryControl", {
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
   Summary: Invoke method ValidateRefEntity
   Description: Validate the reference entity against the BusEntity table.  If it
is valid send back a message asking users if they want the COASegValues
automatically created.
   OperationID: ValidateRefEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRefEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRefEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRefEntity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ValidateRefEntity", {
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
   Summary: Invoke method ValidateSegmentMaxLength
   Description: Enforce maximum length rules for a segment
   OperationID: ValidateSegmentMaxLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSegmentMaxLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSegmentMaxLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSegmentMaxLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ValidateSegmentMaxLength", {
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
   Summary: Invoke method ValidateSegmentMinLength
   Description: Enforce minimum length rules for a segment
   OperationID: ValidateSegmentMinLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSegmentMinLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSegmentMinLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSegmentMinLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/ValidateSegmentMinLength", {
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
   Summary: Invoke method WarnNewMandatorySegmentDynamic
   Description: Check whether new segment is mandatory before adding it into existing COA.
   OperationID: WarnNewMandatorySegmentDynamic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNewMandatorySegmentDynamic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNewMandatorySegmentDynamic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarnNewMandatorySegmentDynamic(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/WarnNewMandatorySegmentDynamic", {
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
   Summary: Invoke method WarnNewMandatorySegmentDynamicExt
   Description: Check whether segment is new and mandatory before import it into existing COA.
   OperationID: WarnNewMandatorySegmentDynamicExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNewMandatorySegmentDynamicExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNewMandatorySegmentDynamicExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarnNewMandatorySegmentDynamicExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/WarnNewMandatorySegmentDynamicExt", {
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
   Summary: Invoke method CheckGlobalCOASegment
   OperationID: CheckGlobalCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGlobalCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGlobalCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGlobalCOASegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/CheckGlobalCOASegment", {
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
   Summary: Invoke method UpdateMaxLength
   Description: Calc Chart length field
   OperationID: UpdateMaxLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaxLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaxLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMaxLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/UpdateMaxLength", {
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
   Summary: Invoke method GetMaxLength
   Description: Calc Chart length field
   OperationID: GetMaxLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMaxLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMaxLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMaxLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetMaxLength", {
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
   Summary: Invoke method MoveOnePositionReturnNewIndex
   Description: This method moves the COASegment Display Order Up/Down one position in the
grid and returns the whole updated datatable for Kinetic
   OperationID: MoveOnePositionReturnNewIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePositionReturnNewIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePositionReturnNewIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveOnePositionReturnNewIndex(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/MoveOnePositionReturnNewIndex", {
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
   Summary: Invoke method GetNewCOA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetNewCOA", {
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
   Summary: Invoke method GetNewCOASegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOASegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetNewCOASegment", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COAListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow{
   "odatametadata":string,
   "value":Erp_Tablesets_COARow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentNotCreatedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegmentNotCreatedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegmentRow[],
}

export interface Erp_Tablesets_COAListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "Description":string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   "SeparatorChar":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgDate":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgTime":number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   "CtrlSegList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Marks the COA as Global  */  
   "GlobalCOA":boolean,
      /**  Disables this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   "RebuildGLAccts":boolean,
      /**  Logical indicating if the chart has been used  */  
   "ChartInUse":boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   "ChartLength":number,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
      /**  Total number of segments defined for this COA  */  
   "NbrSegments":number,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   "HasRefSegment":boolean,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   "ConsInUse":boolean,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   "RebuildBalances":boolean,
      /**  Logical indicating if default categories are to be created  */  
   "CreateDefCat":boolean,
   "GlbFlag":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "Description":string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   "SeparatorChar":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgDate":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgTime":number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   "CtrlSegList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Marks the COA as Global  */  
   "GlobalCOA":boolean,
      /**  Disables this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   "RebuildGLAccts":boolean,
      /**  Peru CSF: SUNAT Chart of Accounts Code  */  
   "PESunatCOA":string,
      /**  Logical indicating if the chart has been used  */  
   "ChartInUse":boolean,
      /**  Logical indicating if default categories are to be created  */  
   "CreateDefCat":boolean,
   "EnableGlobalCOA":boolean,
   "EnableGlobalLock":boolean,
   "GlbFlag":boolean,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   "HasRefSegment":boolean,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
      /**  Total number of segments defined for this COA  */  
   "NbrSegments":number,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   "RebuildBalances":boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   "ChartLength":number,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   "ConsInUse":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COASegmentNotCreatedRow{
   "SegmentCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COASegmentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Name of Segment  */  
   "SegmentName":string,
      /**  Short name of segment.  */  
   "Abbreviation":string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   "MaxLength":number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   "MinLength":number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   "Dynamic":boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   "UseRefEntity":boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   "RefEntity":string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   "AllowAlpha":boolean,
      /**   Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegOpt table.
2 (two) - GL Reference Account Mask - only valid for segments defined as Use Ref Entity where the reference entity = 'Reference Entity'.
3 (three) - Optional.  The segment is not required to be entered.  */  
   "EntryControl":string,
      /**  Indicates if journal entries are automatically balanced.  */  
   "SegSelfBal":boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   "Level":number,
      /**  Indicates if this segment is included in the summary balance GL Account.  Only those segments that are flagged as detail balance segments are eligible to be included as a summary balance segment.  */  
   "SummaryBal":boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   "DetailBal":boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for project accounting where you want to keep the project date balance independent of the financial year.  */  
   "KeepOpenBal":boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   "DisplayOrder":number,
      /**  Indicates if segment values for segments defined as reference entity are to be created each time a new record is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   "AutoCreateSegVals":boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   "SelfBalAcct":string,
      /**  Balance Seg Value 1  */  
   "BalSegValue1":string,
      /**  Balance Seg Value 2  */  
   "BalSegValue2":string,
      /**  Balance Seg Value 3  */  
   "BalSegValue3":string,
      /**  Balance Seg Value 4  */  
   "BalSegValue4":string,
      /**  Balance Seg Value 5  */  
   "BalSegValue5":string,
      /**  Balance Seg Value 6  */  
   "BalSegValue6":string,
      /**  Balance Seg Value 7  */  
   "BalSegValue7":string,
      /**  Balance Seg Value 8  */  
   "BalSegValue8":string,
      /**  Balance Seg Value 9  */  
   "BalSegValue9":string,
      /**  Balance Seg Value 10  */  
   "BalSegValue10":string,
      /**  Balance Seg Value 11  */  
   "BalSegValue11":string,
      /**  Balance Seg Value 12  */  
   "BalSegValue12":string,
      /**  Balance Seg Value 13  */  
   "BalSegValue13":string,
      /**  Balance Seg Value 14  */  
   "BalSegValue14":string,
      /**  Balance Seg Value 15  */  
   "BalSegValue15":string,
      /**  Balance Seg Value 16  */  
   "BalSegValue16":string,
      /**  Balance Seg Value 17  */  
   "BalSegValue17":string,
      /**  Balance Seg Value 18  */  
   "BalSegValue18":string,
      /**  Balance Seg Value 19  */  
   "BalSegValue19":string,
      /**  Balance Seg Value 20  */  
   "BalSegValue20":string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   "SelfOffAcct":string,
      /**  Offset Segment Value 1  */  
   "OffSegValue1":string,
      /**  Offset Segment Value 2  */  
   "OffSegValue2":string,
      /**  Offset Segment Value 3  */  
   "OffSegValue3":string,
      /**  Offset Segment Value 4  */  
   "OffSegValue4":string,
      /**  Offset Segment Value 5  */  
   "OffSegValue5":string,
      /**  Offset Segment Value 6  */  
   "OffSegValue6":string,
      /**  Offset Segment Value 7  */  
   "OffSegValue7":string,
      /**  Offset Segment Value 8  */  
   "OffSegValue8":string,
      /**  Offset Segment Value 9  */  
   "OffSegValue9":string,
      /**  Offset Segment Value 10  */  
   "OffSegValue10":string,
      /**  Offset Segment Value 11  */  
   "OffSegValue11":string,
      /**  Offset Segment Value 12  */  
   "OffSegValue12":string,
      /**  Offset Segment Value 13  */  
   "OffSegValue13":string,
      /**  Offset Segment Value 14  */  
   "OffSegValue14":string,
      /**  Offset Segment Value 15  */  
   "OffSegValue15":string,
      /**  Offset Segment Value 16  */  
   "OffSegValue16":string,
      /**  Offset Segment Value 17  */  
   "OffSegValue17":string,
      /**  Offset Segment Value 18  */  
   "OffSegValue18":string,
      /**  Offset Segment Value 19  */  
   "OffSegValue19":string,
      /**  Offset Segment Value 20  */  
   "OffSegValue20":string,
      /**  Reverse Account Category.  */  
   "ReverseCategoryID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CNIsCFICode  */  
   "CNIsCFICode":boolean,
      /**  The name of Business Entity field that represents segment value.  */  
   "SegValueField":string,
      /**  The name of Business Entity field that represents description of segment value.  */  
   "DescFieldName":string,
      /**  Marks the COASegment as Global  */  
   "GlobalCOASegment":boolean,
      /**  Indicates COASegValues records for the COASegment will be used for Global  */  
   "GlobalCOASegmentValues":boolean,
      /**  Disables this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Disables Segment Values record from receiving global updates  */  
   "GlobalValuesLock":boolean,
      /**  Indicates this is a Site Segment  */  
   "SiteSegment":boolean,
      /**  Balancing Account Description  */  
   "BalancingAcctDesc":string,
      /**  Logical indicating if a chart is in use  */  
   "ChartInUse":boolean,
      /**  Internal field not meant for end user use.  Logical used by row rules to disable the move up/down buttons on the display order tab.  */  
   "DisplayedLast":boolean,
      /**  Offset Account Description  */  
   "OffsetAcctDesc":string,
      /**  Logical indicates if a COAsegment has been used in a GL Account.  */  
   "SegmentInUse":boolean,
      /**  Internal field not meant for end user use.  Logical indicating if a critical COA structure change has occurred.  */  
   "StructureFmtChg":boolean,
      /**  Dynamic Segment values using Business Entity will 'Updated Automatically'. Business Entity (DB table) should have additional code triggers. (e.g. Customer, Vendor)  */  
   "UpdatedAuto":boolean,
   "AutoCreateSegValsInfo":string,
   "EnableGlobalSeg":boolean,
   "EnableGlobalSegLock":boolean,
   "GlbFlag":boolean,
   "EnableGlobalSegValues":boolean,
   "EnableGlobalSegValuesLock":boolean,
   "GlbValuesFlag":boolean,
      /**  Length of Business Entity field that represents segment value.  */  
   "SegValueFieldLength":number,
      /**  Site is a Legal Entity  */  
   "SiteIsLegalEntity":boolean,
   "BitFlag":number,
   "BusEntityDescDescription":string,
   "BusEntityDescEntityType":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param coaCode
   */  
export interface BuildCOASegmentList_input{
      /**  COA Code  */  
   coaCode:string,
}

export interface BuildCOASegmentList_output{
      /**  List of segments  */  
   returnObj:string,
}

   /** Required : 
      @param ipCOACode
   */  
export interface COAExists_input{
   ipCOACode:string,
}

export interface COAExists_output{
}

   /** Required : 
      @param ds
   */  
export interface COAStructureChange_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface COAStructureChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ProposedGlobalCOA
      @param ds
   */  
export interface ChangeCOAGlobalCOA_input{
      /**  The proposed global COA value  */  
   ProposedGlobalCOA:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface ChangeCOAGlobalCOA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param flagtype
      @param ProposedGlobalFlag
      @param ds
   */  
export interface ChangeCOASegmentGlobalCOASegment_input{
      /**  Use 'Segment' to change GlobalCOASegment or any other to change GlobalCOASegmentValues  */  
   flagtype:string,
      /**  The proposed flag value  */  
   ProposedGlobalFlag:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface ChangeCOASegmentGlobalCOASegment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ProposedValue
      @param ds
   */  
export interface ChangeGlobalValuesLock_input{
      /**  The proposed Global Values Lock value  */  
   ProposedValue:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface ChangeGlobalValuesLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param siteSegment
      @param checkForResponse
      @param ds
   */  
export interface ChangeSiteSegment_input{
   siteSegment:boolean,
      /**  Continue process based on user response  */  
   checkForResponse:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface ChangeSiteSegment_output{
parameters : {
      /**  output parameters  */  
   responseMessage:string,
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
      @param ipProposedAlpha
   */  
export interface CheckAllowAlpha_input{
      /**  Chart of Account  */  
   ipCOACode:string,
      /**  SegmentNumber  */  
   ipSegmentNbr:number,
      /**  proposed alpha seg value  */  
   ipProposedAlpha:boolean,
}

export interface CheckAllowAlpha_output{
}

   /** Required : 
      @param ds
   */  
export interface CheckBalanceChange_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface CheckBalanceChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
   ipMessage:string,
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
      @param ipProposedlength
      @param ipInAddMode
   */  
export interface CheckCOALengthWithSegment_input{
      /**  Chart of Account  */  
   ipCOACode:string,
      /**  SegmentNumber  */  
   ipSegmentNbr:number,
      /**  segment maximum length  */  
   ipProposedlength:number,
      /**  indicates if segment is being added  */  
   ipInAddMode:boolean,
}

export interface CheckCOALengthWithSegment_output{
parameters : {
      /**  output parameters  */  
   opChartLength:number,
}
}

   /** Required : 
      @param ipCOACode
   */  
export interface CheckChartLength_input{
      /**  Chart of Account  */  
   ipCOACode:string,
}

export interface CheckChartLength_output{
parameters : {
      /**  output parameters  */  
   opChartLength:number,
}
}

   /** Required : 
      @param ipCOACode
   */  
export interface CheckConsolidatedCOA_input{
      /**  Chart of Account  */  
   ipCOACode:string,
}

export interface CheckConsolidatedCOA_output{
parameters : {
      /**  output parameters  */  
   opConsInUse:boolean,
}
}

   /** Required : 
      @param ipDynamic
      @param ds
   */  
export interface CheckDynamic_input{
      /**  Proposed value of COASegment.Dynamic  */  
   ipDynamic:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface CheckDynamic_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
      @param ipGlobalCOASegmentFlag
   */  
export interface CheckGlobalCOASegment_input{
   ipCOACode:string,
   ipSegmentNbr:number,
   ipGlobalCOASegmentFlag:boolean,
}

export interface CheckGlobalCOASegment_output{
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
   */  
export interface CheckIfDeletingLastSegment_input{
      /**  Chart of Accounts Code  */  
   ipCOACode:string,
      /**  Segment Number the user wants to delete  */  
   ipSegmentNbr:number,
}

export interface CheckIfDeletingLastSegment_output{
parameters : {
      /**  output parameters  */  
   opWarningMsg:string,
   opRenumberRequired:boolean,
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
   */  
export interface CheckIfSegmentHasValues_input{
      /**  Chart of Accounts Code  */  
   ipCOACode:string,
      /**  Segment Number the user wants to delete  */  
   ipSegmentNbr:number,
}

export interface CheckIfSegmentHasValues_output{
parameters : {
      /**  output parameters  */  
   opWarningMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckRebuildBalances_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface CheckRebuildBalances_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipSepChar
      @param ipCOACode
   */  
export interface CheckSeparatorChar_input{
      /**  proposed separator character  */  
   ipSepChar:string,
      /**  COA Code  */  
   ipCOACode:string,
}

export interface CheckSeparatorChar_output{
}

   /** Required : 
      @param ipUseRefEntity
      @param ds
   */  
export interface CheckUseRefEntity_input{
      /**  Proposed value of COASegment.UseRefEntity  */  
   ipUseRefEntity:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface CheckUseRefEntity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegDelete
   */  
export interface DeleteAndRenumberSegments_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  Segment Number to Delete  */  
   ipSegDelete:number,
}

export interface DeleteAndRenumberSegments_output{
   returnObj:Erp_Tablesets_COATableset[],
}

   /** Required : 
      @param coACode
   */  
export interface DeleteByID_input{
   coACode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_COAListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The description or Name of this Chart of Accounts.  */  
   Description:string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   SeparatorChar:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgDate:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgTime:number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   CtrlSegList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Marks the COA as Global  */  
   GlobalCOA:boolean,
      /**  Disables this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   RebuildGLAccts:boolean,
      /**  Logical indicating if the chart has been used  */  
   ChartInUse:boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   ChartLength:number,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
      /**  Total number of segments defined for this COA  */  
   NbrSegments:number,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   HasRefSegment:boolean,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   ConsInUse:boolean,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   RebuildBalances:boolean,
      /**  Logical indicating if default categories are to be created  */  
   CreateDefCat:boolean,
   GlbFlag:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COAListTableset{
   COAList:Erp_Tablesets_COAListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_COARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The description or Name of this Chart of Accounts.  */  
   Description:string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  */  
   SeparatorChar:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgDate:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgTime:number,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  */  
   CtrlSegList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Marks the COA as Global  */  
   GlobalCOA:boolean,
      /**  Disables this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   RebuildGLAccts:boolean,
      /**  Peru CSF: SUNAT Chart of Accounts Code  */  
   PESunatCOA:string,
      /**  Logical indicating if the chart has been used  */  
   ChartInUse:boolean,
      /**  Logical indicating if default categories are to be created  */  
   CreateDefCat:boolean,
   EnableGlobalCOA:boolean,
   EnableGlobalLock:boolean,
   GlbFlag:boolean,
      /**  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  */  
   HasRefSegment:boolean,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
      /**  Total number of segments defined for this COA  */  
   NbrSegments:number,
      /**  Logical indicating the balances are to be rebuilt due to a change in balance structure  */  
   RebuildBalances:boolean,
      /**  Sum of the COASegment.MaxLength entries.  */  
   ChartLength:number,
      /**  Logical indicating if this chart of accounts is subject to consolidation  */  
   ConsInUse:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegmentNotCreatedRow{
   SegmentCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegmentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Name of Segment  */  
   SegmentName:string,
      /**  Short name of segment.  */  
   Abbreviation:string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   MaxLength:number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   MinLength:number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   Dynamic:boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   UseRefEntity:boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   RefEntity:string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   AllowAlpha:boolean,
      /**   Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegOpt table.
2 (two) - GL Reference Account Mask - only valid for segments defined as Use Ref Entity where the reference entity = 'Reference Entity'.
3 (three) - Optional.  The segment is not required to be entered.  */  
   EntryControl:string,
      /**  Indicates if journal entries are automatically balanced.  */  
   SegSelfBal:boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   Level:number,
      /**  Indicates if this segment is included in the summary balance GL Account.  Only those segments that are flagged as detail balance segments are eligible to be included as a summary balance segment.  */  
   SummaryBal:boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   DetailBal:boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for project accounting where you want to keep the project date balance independent of the financial year.  */  
   KeepOpenBal:boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   DisplayOrder:number,
      /**  Indicates if segment values for segments defined as reference entity are to be created each time a new record is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   AutoCreateSegVals:boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   SelfBalAcct:string,
      /**  Balance Seg Value 1  */  
   BalSegValue1:string,
      /**  Balance Seg Value 2  */  
   BalSegValue2:string,
      /**  Balance Seg Value 3  */  
   BalSegValue3:string,
      /**  Balance Seg Value 4  */  
   BalSegValue4:string,
      /**  Balance Seg Value 5  */  
   BalSegValue5:string,
      /**  Balance Seg Value 6  */  
   BalSegValue6:string,
      /**  Balance Seg Value 7  */  
   BalSegValue7:string,
      /**  Balance Seg Value 8  */  
   BalSegValue8:string,
      /**  Balance Seg Value 9  */  
   BalSegValue9:string,
      /**  Balance Seg Value 10  */  
   BalSegValue10:string,
      /**  Balance Seg Value 11  */  
   BalSegValue11:string,
      /**  Balance Seg Value 12  */  
   BalSegValue12:string,
      /**  Balance Seg Value 13  */  
   BalSegValue13:string,
      /**  Balance Seg Value 14  */  
   BalSegValue14:string,
      /**  Balance Seg Value 15  */  
   BalSegValue15:string,
      /**  Balance Seg Value 16  */  
   BalSegValue16:string,
      /**  Balance Seg Value 17  */  
   BalSegValue17:string,
      /**  Balance Seg Value 18  */  
   BalSegValue18:string,
      /**  Balance Seg Value 19  */  
   BalSegValue19:string,
      /**  Balance Seg Value 20  */  
   BalSegValue20:string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   SelfOffAcct:string,
      /**  Offset Segment Value 1  */  
   OffSegValue1:string,
      /**  Offset Segment Value 2  */  
   OffSegValue2:string,
      /**  Offset Segment Value 3  */  
   OffSegValue3:string,
      /**  Offset Segment Value 4  */  
   OffSegValue4:string,
      /**  Offset Segment Value 5  */  
   OffSegValue5:string,
      /**  Offset Segment Value 6  */  
   OffSegValue6:string,
      /**  Offset Segment Value 7  */  
   OffSegValue7:string,
      /**  Offset Segment Value 8  */  
   OffSegValue8:string,
      /**  Offset Segment Value 9  */  
   OffSegValue9:string,
      /**  Offset Segment Value 10  */  
   OffSegValue10:string,
      /**  Offset Segment Value 11  */  
   OffSegValue11:string,
      /**  Offset Segment Value 12  */  
   OffSegValue12:string,
      /**  Offset Segment Value 13  */  
   OffSegValue13:string,
      /**  Offset Segment Value 14  */  
   OffSegValue14:string,
      /**  Offset Segment Value 15  */  
   OffSegValue15:string,
      /**  Offset Segment Value 16  */  
   OffSegValue16:string,
      /**  Offset Segment Value 17  */  
   OffSegValue17:string,
      /**  Offset Segment Value 18  */  
   OffSegValue18:string,
      /**  Offset Segment Value 19  */  
   OffSegValue19:string,
      /**  Offset Segment Value 20  */  
   OffSegValue20:string,
      /**  Reverse Account Category.  */  
   ReverseCategoryID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CNIsCFICode  */  
   CNIsCFICode:boolean,
      /**  The name of Business Entity field that represents segment value.  */  
   SegValueField:string,
      /**  The name of Business Entity field that represents description of segment value.  */  
   DescFieldName:string,
      /**  Marks the COASegment as Global  */  
   GlobalCOASegment:boolean,
      /**  Indicates COASegValues records for the COASegment will be used for Global  */  
   GlobalCOASegmentValues:boolean,
      /**  Disables this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Disables Segment Values record from receiving global updates  */  
   GlobalValuesLock:boolean,
      /**  Indicates this is a Site Segment  */  
   SiteSegment:boolean,
      /**  Balancing Account Description  */  
   BalancingAcctDesc:string,
      /**  Logical indicating if a chart is in use  */  
   ChartInUse:boolean,
      /**  Internal field not meant for end user use.  Logical used by row rules to disable the move up/down buttons on the display order tab.  */  
   DisplayedLast:boolean,
      /**  Offset Account Description  */  
   OffsetAcctDesc:string,
      /**  Logical indicates if a COAsegment has been used in a GL Account.  */  
   SegmentInUse:boolean,
      /**  Internal field not meant for end user use.  Logical indicating if a critical COA structure change has occurred.  */  
   StructureFmtChg:boolean,
      /**  Dynamic Segment values using Business Entity will 'Updated Automatically'. Business Entity (DB table) should have additional code triggers. (e.g. Customer, Vendor)  */  
   UpdatedAuto:boolean,
   AutoCreateSegValsInfo:string,
   EnableGlobalSeg:boolean,
   EnableGlobalSegLock:boolean,
   GlbFlag:boolean,
   EnableGlobalSegValues:boolean,
   EnableGlobalSegValuesLock:boolean,
   GlbValuesFlag:boolean,
      /**  Length of Business Entity field that represents segment value.  */  
   SegValueFieldLength:number,
      /**  Site is a Legal Entity  */  
   SiteIsLegalEntity:boolean,
   BitFlag:number,
   BusEntityDescDescription:string,
   BusEntityDescEntityType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COATableset{
   COA:Erp_Tablesets_COARow[],
   COASegment:Erp_Tablesets_COASegmentRow[],
   COASegmentNotCreated:Erp_Tablesets_COASegmentNotCreatedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCOATableset{
   COA:Erp_Tablesets_COARow[],
   COASegment:Erp_Tablesets_COASegmentRow[],
   COASegmentNotCreated:Erp_Tablesets_COASegmentNotCreatedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param COACode
   */  
export interface GetByIDOrdered_input{
   COACode:string,
}

export interface GetByIDOrdered_output{
   returnObj:Erp_Tablesets_COATableset[],
}

   /** Required : 
      @param coACode
   */  
export interface GetByID_input{
   coACode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_COATableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_COATableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_COATableset[],
}

   /** Required : 
      @param COACode
      @param GlobalLock
   */  
export interface GetCOAGlobalFields_input{
   COACode:string,
   GlobalLock:boolean,
}

export interface GetCOAGlobalFields_output{
   returnObj:string,
}

   /** Required : 
      @param COACode
      @param SegmentNbr
      @param GlobalLock
   */  
export interface GetCOASegmentGlobalFields_input{
   COACode:string,
   SegmentNbr:number,
   GlobalLock:boolean,
}

export interface GetCOASegmentGlobalFields_output{
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
   returnObj:Erp_Tablesets_COAListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetMaxLength_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface GetMaxLength_output{
   returnObj:number,
}

   /** Required : 
      @param ds
      @param coACode
   */  
export interface GetNewCOASegment_input{
   ds:Erp_Tablesets_COATableset[],
   coACode:string,
}

export interface GetNewCOASegment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCOA_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface GetNewCOA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param whereClauseCOA
      @param whereClauseCOASegment
      @param whereClauseCOASegmentNotCreated
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCOA:string,
   whereClauseCOASegment:string,
   whereClauseCOASegmentNotCreated:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_COATableset[],
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
      @param ipCOACode
   */  
export interface IsCOAMasterCOA_input{
   ipCOACode:string,
}

export interface IsCOAMasterCOA_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipCOACode
   */  
export interface IsChartInUse_input{
   ipCOACode:string,
}

export interface IsChartInUse_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipCOACode
   */  
export interface IsChartUsedInTransaction_input{
   ipCOACode:string,
}

export interface IsChartUsedInTransaction_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
      @param ipSegmentVal
   */  
export interface IsSegValInUse_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  Segment Number  */  
   ipSegmentNbr:number,
      /**  Segement Code/Value  */  
   ipSegmentVal:string,
}

export interface IsSegValInUse_output{
parameters : {
      /**  output parameters  */  
   opValInUse:boolean,
}
}

   /** Required : 
      @param COACode
      @param segmentNbr
      @param displayOrder
      @param moveDir
   */  
export interface MoveOnePositionReturnNewIndex_input{
   COACode:string,
   segmentNbr:number,
   displayOrder:number,
   moveDir:string,
}

export interface MoveOnePositionReturnNewIndex_output{
   returnObj:Erp_Tablesets_COATableset[],
parameters : {
      /**  output parameters  */  
   newRowPosition:number,
}
}

   /** Required : 
      @param coaCode
      @param segmentNbr
      @param dynamicOpt
      @param displayOrder
      @param moveDir
   */  
export interface MoveOnePosition_input{
      /**  Chart of Accounts Code  */  
   coaCode:string,
      /**  COA Segment Number  */  
   segmentNbr:number,
      /**  Indicates if a dynamic (yes) or controlled (no) segment (yes) is being moved  */  
   dynamicOpt:boolean,
      /**  Current display order  */  
   displayOrder:number,
      /**  Direction to move task, "Up" or "Down"  */  
   moveDir:string,
}

export interface MoveOnePosition_output{
   returnObj:Erp_Tablesets_COATableset[],
}

   /** Required : 
      @param ds
   */  
export interface PromptAutoCreateDynSegVals_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface PromptAutoCreateDynSegVals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
   opAutoCreateSegValMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SetRefEntityFields_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface SetRefEntityFields_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
   */  
export interface UpdateCOADynamicSegValues_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  Segment Number  */  
   ipSegmentNbr:number,
}

export interface UpdateCOADynamicSegValues_output{
}

   /** Required : 
      @param ipDynamic
      @param ds
   */  
export interface UpdateDynamicSegment_input{
      /**  Proposed value of COASegment.Dynamic  */  
   ipDynamic:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface UpdateDynamicSegment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCOATableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCOATableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateFieldLength_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface UpdateFieldLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateMaxLength_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface UpdateMaxLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipGlobal
      @param ds
   */  
export interface UpdateNatural_input{
      /**  Proposed value of COA.Global  */  
   ipGlobal:boolean,
   ds:Erp_Tablesets_COATableset[],
}

export interface UpdateNatural_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_COATableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipSegmentNbr
      @param ipRefEntity
      @param ipEntryControl
   */  
export interface ValidateEntryControl_input{
      /**  Segment Number  */  
   ipSegmentNbr:number,
      /**  Reference entity value  */  
   ipRefEntity:string,
      /**  Entry Control  */  
   ipEntryControl:string,
}

export interface ValidateEntryControl_output{
}

   /** Required : 
      @param ipRefEntity
      @param ds
   */  
export interface ValidateRefEntity_input{
      /**  Reference Entity to validate  */  
   ipRefEntity:string,
   ds:Erp_Tablesets_COATableset[],
}

export interface ValidateRefEntity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
   opAutoCreateSegValMsg:string,
   opValuesAlreadyExist:string,
}
}

   /** Required : 
      @param ipMaxLength
      @param ds
   */  
export interface ValidateSegmentMaxLength_input{
      /**  Proposed value of COASegment.MaxLength  */  
   ipMaxLength:number,
   ds:Erp_Tablesets_COATableset[],
}

export interface ValidateSegmentMaxLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param ipMinLength
      @param ds
   */  
export interface ValidateSegmentMinLength_input{
      /**  Proposed value of COASegment.MaxLength  */  
   ipMinLength:number,
   ds:Erp_Tablesets_COATableset[],
}

export interface ValidateSegmentMinLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COATableset[],
}
}

   /** Required : 
      @param coaCode
      @param segNbr
      @param entryControl
      @param dynamic
   */  
export interface WarnNewMandatorySegmentDynamicExt_input{
      /**  COA Code  */  
   coaCode:string,
      /**  Segment Number  */  
   segNbr:number,
      /**  Entry Control  */  
   entryControl:string,
      /**  Dynamic Segment flag  */  
   dynamic:boolean,
}

export interface WarnNewMandatorySegmentDynamicExt_output{
      /**  Returns warning if new mandatory segment has been added for the COA in use. Message depends on whether new segment is dynamic.  */  
   returnObj:string,
}

   /** Required : 
      @param coaCode
      @param entryControl
      @param dynamic
   */  
export interface WarnNewMandatorySegmentDynamic_input{
      /**  COA Code  */  
   coaCode:string,
      /**  Entry Control  */  
   entryControl:string,
      /**  Dynamic Segment flag  */  
   dynamic:boolean,
}

export interface WarnNewMandatorySegmentDynamic_output{
      /**  Returns warning if new mandatory segment has been added for the COA in use. Message depends on whether new segment is dynamic.  */  
   returnObj:string,
}

