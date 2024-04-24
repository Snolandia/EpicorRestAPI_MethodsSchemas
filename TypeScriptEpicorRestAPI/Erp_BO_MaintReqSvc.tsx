import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MaintReqSvc
// Description: Maintenance Request Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/$metadata", {
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
   Description: Get MaintReqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MaintReqs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqRow
   */  
export function get_MaintReqs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MaintReqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MaintReqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MaintReqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MaintReqs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs", {
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
   Summary: Calls GetByID to retrieve the MaintReq item
   Description: Calls GetByID to retrieve the MaintReq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaintReq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MaintReqRow
   */  
export function get_MaintReqs_Company_Plant_ReqID(Company:string, Plant:string, ReqID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MaintReqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MaintReqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MaintReq for the service
   Description: Calls UpdateExt to update MaintReq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MaintReq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MaintReqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MaintReqs_Company_Plant_ReqID(Company:string, Plant:string, ReqID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")", {
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
   Summary: Call UpdateExt to delete MaintReq item
   Description: Call UpdateExt to delete MaintReq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MaintReq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MaintReqs_Company_Plant_ReqID(Company:string, Plant:string, ReqID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")", {
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
   Description: Get MaintReqAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MaintReqAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqAttchRow
   */  
export function get_MaintReqs_Company_Plant_ReqID_MaintReqAttches(Company:string, Plant:string, ReqID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")/MaintReqAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MaintReqAttch item
   Description: Calls GetByID to retrieve the MaintReqAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaintReqAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   */  
export function get_MaintReqs_Company_Plant_ReqID_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company:string, Plant:string, ReqID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MaintReqAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MaintReqAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MaintReqAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MaintReqAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqAttchRow
   */  
export function get_MaintReqAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MaintReqAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MaintReqAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches", {
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
   Summary: Calls GetByID to retrieve the MaintReqAttch item
   Description: Calls GetByID to retrieve the MaintReqAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaintReqAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   */  
export function get_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company:string, Plant:string, ReqID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MaintReqAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MaintReqAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MaintReqAttch for the service
   Description: Calls UpdateExt to update MaintReqAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MaintReqAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company:string, Plant:string, ReqID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete MaintReqAttch item
   Description: Call UpdateExt to delete MaintReqAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MaintReqAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ReqID Desc: ReqID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company:string, Plant:string, ReqID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqListRow)
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
export function get_GetRows(whereClauseMaintReq:string, whereClauseMaintReqAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMaintReq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMaintReq=" + whereClauseMaintReq
   }
   if(typeof whereClauseMaintReqAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMaintReqAttch=" + whereClauseMaintReqAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, reqID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }
   if(typeof reqID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reqID=" + reqID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/GetList" + params, {
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
   Summary: Invoke method OnApproveJob
   Description: This method should be called when request is approved.
   OperationID: OnApproveJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnApproveJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnApproveJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnApproveJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/OnApproveJob", {
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
   Summary: Invoke method OnChangeEquipID
   Description: This method should be called when EquipID change.
   OperationID: OnChangeEquipID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEquipID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/OnChangeEquipID", {
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
   Summary: Invoke method OnChangeIssueTopics
   Description: This method should be invoked when the IssueTopics changes.
Validates and sets the individual IssueTopic fields.
   OperationID: OnChangeIssueTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIssueTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIssueTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIssueTopics(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/OnChangeIssueTopics", {
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
   Summary: Invoke method OnChangeResTopics
   Description: This method should be invoked when the ResTopics changes.
Validates and sets the individual ResTopic fields.
   OperationID: OnChangeResTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeResTopics(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/OnChangeResTopics", {
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
   Summary: Invoke method StatusRequest
   Description: This method should be called when Status Request is changed.
   OperationID: StatusRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StatusRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StatusRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StatusRequest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/StatusRequest", {
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
   Summary: Invoke method ValidateMaintPlant
   Description: Purpose: Rejecting or Approving a Maintenance Request requires that it is done from
the plant that is responsible for maintenance of the Requesting Plant.
Parameters:  none
Notes:
   OperationID: ValidateMaintPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMaintPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMaintPlant(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/ValidateMaintPlant", {
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
   Summary: Invoke method GetNewMaintReq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMaintReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMaintReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMaintReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMaintReq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/GetNewMaintReq", {
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
   Summary: Invoke method GetNewMaintReqAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMaintReqAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMaintReqAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMaintReqAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMaintReqAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/GetNewMaintReqAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MaintReqAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MaintReqListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MaintReqRow[],
}

export interface Erp_Tablesets_MaintReqAttchRow{
   "Company":string,
   "Plant":string,
   "ReqID":string,
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

export interface Erp_Tablesets_MaintReqListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  */  
   "ReqID":string,
      /**  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  */  
   "EquipID":string,
      /**  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  */  
   "OpenReq":boolean,
      /**   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  */  
   "ReqStatus":string,
      /**  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  */  
   "RequiredDate":string,
      /**  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  */  
   "Priority":string,
      /**  Describes the issue with the equipment that is prompting this request for maintenance.  */  
   "IssueDesc":string,
      /**  User ID that made the Request.  */  
   "Requestor":string,
      /**  User ID that reviewed the request.  */  
   "Reviewer":string,
      /**  Date the request was created  */  
   "RequestDt":string,
      /**  Time the Request was made. Expressed as seconds since midnight.  */  
   "RequestTime":number,
      /**  Date when the response was received.  */  
   "ResponseDate":string,
      /**  Time the Response was made. Expressed as seconds since midnight.  */  
   "ResponseTime":number,
      /**  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  */  
   "JobNum":string,
      /**  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  */  
   "ResDesc":string,
      /**  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   "IssueTopicID2":string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   "IssueTopicID3":string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   "IssueTopicID4":string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   "IssueTopicID5":string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   "IssueTopicID6":string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   "IssueTopicID7":string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   "IssueTopicID8":string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   "IssueTopicID9":string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   "IssueTopicID10":string,
      /**  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   "ResTopicID1":string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  */  
   "ResTopicID2":string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   "ResTopicID3":string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   "ResTopicID4":string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   "ResTopicID5":string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   "ResTopicID6":string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   "ResTopicID7":string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   "ResTopicID8":string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   "ResTopicID9":string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   "ResTopicID10":string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   "HDCaseNum":number,
      /**  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  */  
   "MaintPlant":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "JCDeptDesc":string,
      /**  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  */  
   "IssueTopics":string,
      /**  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  */  
   "ResTopics":string,
      /**  Full description of Equipment. Cannot be blank.  */  
   "EquipIDDescription":string,
      /**  Date that equipment was first put into service. Required field.  */  
   "EquipIDInServiceDate":string,
      /**  Model Number  */  
   "EquipIDModel":string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   "EquipIDTypeID":string,
      /**  OEM Number  */  
   "EquipIDOEM":string,
      /**  Warrenty Expiration Date  */  
   "EquipIDWarrantyExpDate":string,
      /**  Serial Number of equipment  */  
   "EquipIDSerialNum":string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   "EquipIDLocID":string,
      /**  Plant in which the equipment is currently located.  */  
   "EquipIDPlant":string,
      /**  Brand of equipment  */  
   "EquipIDBrand":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID1Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID10Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID2Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID3Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID4Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID5Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID6Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID7Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID8Description":string,
      /**  Full description of the Help Desk topic.  */  
   "IssueTopicID9Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID1Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID10Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID2Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID3Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID4Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID5Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID6Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID7Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID8Description":string,
      /**  Full description of the Help Desk topic.  */  
   "ResTopicID9Description":string,
      /**  Description of the priority.  */  
   "SchedPriDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MaintReqRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  */  
   "ReqID":string,
      /**  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  */  
   "EquipID":string,
      /**  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  */  
   "OpenReq":boolean,
      /**   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  */  
   "ReqStatus":string,
      /**  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  */  
   "RequiredDate":string,
      /**  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  */  
   "Priority":string,
      /**  Describes the issue with the equipment that is prompting this request for maintenance.  */  
   "IssueDesc":string,
      /**  User ID that made the Request.  */  
   "Requestor":string,
      /**  User ID that reviewed the request.  */  
   "Reviewer":string,
      /**  Date the request was created  */  
   "RequestDt":string,
      /**  Time the Request was made. Expressed as seconds since midnight.  */  
   "RequestTime":number,
      /**  Date when the response was received.  */  
   "ResponseDate":string,
      /**  Time the Response was made. Expressed as seconds since midnight.  */  
   "ResponseTime":number,
      /**  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  */  
   "JobNum":string,
      /**  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  */  
   "ResDesc":string,
      /**  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   "IssueTopicID2":string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   "IssueTopicID3":string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   "IssueTopicID4":string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   "IssueTopicID5":string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   "IssueTopicID6":string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   "IssueTopicID7":string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   "IssueTopicID8":string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   "IssueTopicID9":string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   "IssueTopicID10":string,
      /**  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   "ResTopicID1":string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  */  
   "ResTopicID2":string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   "ResTopicID3":string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   "ResTopicID4":string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   "ResTopicID5":string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   "ResTopicID6":string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   "ResTopicID7":string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   "ResTopicID8":string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   "ResTopicID9":string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   "ResTopicID10":string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   "HDCaseNum":number,
      /**  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  */  
   "MaintPlant":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "JCDeptDesc":string,
      /**  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  */  
   "IssueTopics":string,
      /**  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  */  
   "ResTopics":string,
   "BitFlag":number,
   "EquipIDBrand":string,
   "EquipIDOEM":string,
   "EquipIDLocID":string,
   "EquipIDTypeID":string,
   "EquipIDModel":string,
   "EquipIDInServiceDate":string,
   "EquipIDSerialNum":string,
   "EquipIDDescription":string,
   "EquipIDPlant":string,
   "EquipIDWarrantyExpDate":string,
   "IssueTopicID1Description":string,
   "IssueTopicID10Description":string,
   "IssueTopicID2Description":string,
   "IssueTopicID3Description":string,
   "IssueTopicID4Description":string,
   "IssueTopicID5Description":string,
   "IssueTopicID6Description":string,
   "IssueTopicID7Description":string,
   "IssueTopicID8Description":string,
   "IssueTopicID9Description":string,
   "ResTopicID1Description":string,
   "ResTopicID10Description":string,
   "ResTopicID2Description":string,
   "ResTopicID3Description":string,
   "ResTopicID4Description":string,
   "ResTopicID5Description":string,
   "ResTopicID6Description":string,
   "ResTopicID7Description":string,
   "ResTopicID8Description":string,
   "ResTopicID9Description":string,
   "SchedPriDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param plant
      @param reqID
   */  
export interface DeleteByID_input{
   plant:string,
   reqID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MaintReqAttchRow{
   Company:string,
   Plant:string,
   ReqID:string,
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

export interface Erp_Tablesets_MaintReqListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  */  
   ReqID:string,
      /**  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  */  
   EquipID:string,
      /**  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  */  
   OpenReq:boolean,
      /**   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  */  
   ReqStatus:string,
      /**  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  */  
   RequiredDate:string,
      /**  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  */  
   Priority:string,
      /**  Describes the issue with the equipment that is prompting this request for maintenance.  */  
   IssueDesc:string,
      /**  User ID that made the Request.  */  
   Requestor:string,
      /**  User ID that reviewed the request.  */  
   Reviewer:string,
      /**  Date the request was created  */  
   RequestDt:string,
      /**  Time the Request was made. Expressed as seconds since midnight.  */  
   RequestTime:number,
      /**  Date when the response was received.  */  
   ResponseDate:string,
      /**  Time the Response was made. Expressed as seconds since midnight.  */  
   ResponseTime:number,
      /**  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  */  
   JobNum:string,
      /**  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  */  
   ResDesc:string,
      /**  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   IssueTopicID2:string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   IssueTopicID3:string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   IssueTopicID4:string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   IssueTopicID5:string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   IssueTopicID6:string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   IssueTopicID7:string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   IssueTopicID8:string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   IssueTopicID9:string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   IssueTopicID10:string,
      /**  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   ResTopicID1:string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  */  
   ResTopicID2:string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   ResTopicID3:string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   ResTopicID4:string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   ResTopicID5:string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   ResTopicID6:string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   ResTopicID7:string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   ResTopicID8:string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   ResTopicID9:string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   ResTopicID10:string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   HDCaseNum:number,
      /**  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  */  
   MaintPlant:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   JCDeptDesc:string,
      /**  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  */  
   IssueTopics:string,
      /**  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  */  
   ResTopics:string,
      /**  Full description of Equipment. Cannot be blank.  */  
   EquipIDDescription:string,
      /**  Date that equipment was first put into service. Required field.  */  
   EquipIDInServiceDate:string,
      /**  Model Number  */  
   EquipIDModel:string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   EquipIDTypeID:string,
      /**  OEM Number  */  
   EquipIDOEM:string,
      /**  Warrenty Expiration Date  */  
   EquipIDWarrantyExpDate:string,
      /**  Serial Number of equipment  */  
   EquipIDSerialNum:string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   EquipIDLocID:string,
      /**  Plant in which the equipment is currently located.  */  
   EquipIDPlant:string,
      /**  Brand of equipment  */  
   EquipIDBrand:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID1Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID10Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID2Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID3Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID4Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID5Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID6Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID7Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID8Description:string,
      /**  Full description of the Help Desk topic.  */  
   IssueTopicID9Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID1Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID10Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID2Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID3Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID4Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID5Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID6Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID7Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID8Description:string,
      /**  Full description of the Help Desk topic.  */  
   ResTopicID9Description:string,
      /**  Description of the priority.  */  
   SchedPriDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MaintReqListTableset{
   MaintReqList:Erp_Tablesets_MaintReqListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MaintReqRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  */  
   ReqID:string,
      /**  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  */  
   EquipID:string,
      /**  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  */  
   OpenReq:boolean,
      /**   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  */  
   ReqStatus:string,
      /**  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  */  
   RequiredDate:string,
      /**  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  */  
   Priority:string,
      /**  Describes the issue with the equipment that is prompting this request for maintenance.  */  
   IssueDesc:string,
      /**  User ID that made the Request.  */  
   Requestor:string,
      /**  User ID that reviewed the request.  */  
   Reviewer:string,
      /**  Date the request was created  */  
   RequestDt:string,
      /**  Time the Request was made. Expressed as seconds since midnight.  */  
   RequestTime:number,
      /**  Date when the response was received.  */  
   ResponseDate:string,
      /**  Time the Response was made. Expressed as seconds since midnight.  */  
   ResponseTime:number,
      /**  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  */  
   JobNum:string,
      /**  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  */  
   ResDesc:string,
      /**  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   IssueTopicID2:string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   IssueTopicID3:string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   IssueTopicID4:string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   IssueTopicID5:string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   IssueTopicID6:string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   IssueTopicID7:string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   IssueTopicID8:string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   IssueTopicID9:string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   IssueTopicID10:string,
      /**  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   ResTopicID1:string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  */  
   ResTopicID2:string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   ResTopicID3:string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   ResTopicID4:string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   ResTopicID5:string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   ResTopicID6:string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   ResTopicID7:string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   ResTopicID8:string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   ResTopicID9:string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   ResTopicID10:string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   HDCaseNum:number,
      /**  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  */  
   MaintPlant:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   JCDeptDesc:string,
      /**  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  */  
   IssueTopics:string,
      /**  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  */  
   ResTopics:string,
   BitFlag:number,
   EquipIDBrand:string,
   EquipIDOEM:string,
   EquipIDLocID:string,
   EquipIDTypeID:string,
   EquipIDModel:string,
   EquipIDInServiceDate:string,
   EquipIDSerialNum:string,
   EquipIDDescription:string,
   EquipIDPlant:string,
   EquipIDWarrantyExpDate:string,
   IssueTopicID1Description:string,
   IssueTopicID10Description:string,
   IssueTopicID2Description:string,
   IssueTopicID3Description:string,
   IssueTopicID4Description:string,
   IssueTopicID5Description:string,
   IssueTopicID6Description:string,
   IssueTopicID7Description:string,
   IssueTopicID8Description:string,
   IssueTopicID9Description:string,
   ResTopicID1Description:string,
   ResTopicID10Description:string,
   ResTopicID2Description:string,
   ResTopicID3Description:string,
   ResTopicID4Description:string,
   ResTopicID5Description:string,
   ResTopicID6Description:string,
   ResTopicID7Description:string,
   ResTopicID8Description:string,
   ResTopicID9Description:string,
   SchedPriDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MaintReqTableset{
   MaintReq:Erp_Tablesets_MaintReqRow[],
   MaintReqAttch:Erp_Tablesets_MaintReqAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtMaintReqTableset{
   MaintReq:Erp_Tablesets_MaintReqRow[],
   MaintReqAttch:Erp_Tablesets_MaintReqAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param reqID
   */  
export interface GetByID_input{
   plant:string,
   reqID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MaintReqTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MaintReqTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MaintReqTableset[],
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
   returnObj:Erp_Tablesets_MaintReqListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param reqID
   */  
export interface GetNewMaintReqAttch_input{
   ds:Erp_Tablesets_MaintReqTableset[],
   plant:string,
   reqID:string,
}

export interface GetNewMaintReqAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewMaintReq_input{
   ds:Erp_Tablesets_MaintReqTableset[],
   plant:string,
}

export interface GetNewMaintReq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

   /** Required : 
      @param whereClauseMaintReq
      @param whereClauseMaintReqAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMaintReq:string,
   whereClauseMaintReqAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MaintReqTableset[],
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
      @param plant
      @param reqID
      @param onHold
      @param ds
   */  
export interface OnApproveJob_input{
      /**  plant  */  
   plant:string,
      /**  reqID  */  
   reqID:string,
      /**  onHold  */  
   onHold:boolean,
   ds:Erp_Tablesets_MaintReqTableset[],
}

export interface OnApproveJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

   /** Required : 
      @param equipID
      @param ds
   */  
export interface OnChangeEquipID_input{
      /**  equipID  */  
   equipID:string,
   ds:Erp_Tablesets_MaintReqTableset[],
}

export interface OnChangeEquipID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

   /** Required : 
      @param topics
      @param ds
   */  
export interface OnChangeIssueTopics_input{
      /**  Proposed topics string id  */  
   topics:string,
   ds:Erp_Tablesets_MaintReqTableset[],
}

export interface OnChangeIssueTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

   /** Required : 
      @param topics
      @param ds
   */  
export interface OnChangeResTopics_input{
      /**  Proposed topics string id  */  
   topics:string,
   ds:Erp_Tablesets_MaintReqTableset[],
}

export interface OnChangeResTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

   /** Required : 
      @param ipReqID
      @param ipPlant
      @param ipStatus
      @param ds
   */  
export interface StatusRequest_input{
      /**  RequestID  */  
   ipReqID:string,
      /**  Plant  */  
   ipPlant:string,
      /**  StatusRequest  */  
   ipStatus:string,
   ds:Erp_Tablesets_MaintReqTableset[],
}

export interface StatusRequest_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMaintReqTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMaintReqTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MaintReqTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaintReqTableset[],
}
}

export interface ValidateMaintPlant_output{
}

