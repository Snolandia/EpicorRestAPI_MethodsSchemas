import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.WHTPaymentSubmitSvc
// Description: Withholding Tax Payment Submit Report BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/$metadata", {
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
   Description: Get WHTPaymentSubmits items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WHTPaymentSubmits
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentSubmitRow
   */  
export function get_WHTPaymentSubmits(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmits", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WHTPaymentSubmits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WHTPaymentSubmits(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmits", {
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
   Summary: Calls GetByID to retrieve the WHTPaymentSubmit item
   Description: Calls GetByID to retrieve the WHTPaymentSubmit item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPaymentSubmit
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitRow
   */  
export function get_WHTPaymentSubmits_Company_SubmitReportID(Company:string, SubmitReportID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WHTPaymentSubmitRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmits(" + Company + "," + SubmitReportID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WHTPaymentSubmitRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WHTPaymentSubmit for the service
   Description: Calls UpdateExt to update WHTPaymentSubmit. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WHTPaymentSubmit
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WHTPaymentSubmits_Company_SubmitReportID(Company:string, SubmitReportID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmits(" + Company + "," + SubmitReportID + ")", {
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
   Summary: Call UpdateExt to delete WHTPaymentSubmit item
   Description: Call UpdateExt to delete WHTPaymentSubmit item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WHTPaymentSubmit
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WHTPaymentSubmits_Company_SubmitReportID(Company:string, SubmitReportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmits(" + Company + "," + SubmitReportID + ")", {
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
   Description: Get WHTPaymentSubmitAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WHTPaymentSubmitAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentSubmitAttchRow
   */  
export function get_WHTPaymentSubmits_Company_SubmitReportID_WHTPaymentSubmitAttches(Company:string, SubmitReportID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmits(" + Company + "," + SubmitReportID + ")/WHTPaymentSubmitAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WHTPaymentSubmitAttch item
   Description: Calls GetByID to retrieve the WHTPaymentSubmitAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPaymentSubmitAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitAttchRow
   */  
export function get_WHTPaymentSubmits_Company_SubmitReportID_WHTPaymentSubmitAttches_Company_SubmitReportID_DrawingSeq(Company:string, SubmitReportID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WHTPaymentSubmitAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmits(" + Company + "," + SubmitReportID + ")/WHTPaymentSubmitAttches(" + Company + "," + SubmitReportID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WHTPaymentSubmitAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get WHTPaymentSubmitAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WHTPaymentSubmitAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentSubmitAttchRow
   */  
export function get_WHTPaymentSubmitAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmitAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WHTPaymentSubmitAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WHTPaymentSubmitAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmitAttches", {
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
   Summary: Calls GetByID to retrieve the WHTPaymentSubmitAttch item
   Description: Calls GetByID to retrieve the WHTPaymentSubmitAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPaymentSubmitAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitAttchRow
   */  
export function get_WHTPaymentSubmitAttches_Company_SubmitReportID_DrawingSeq(Company:string, SubmitReportID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WHTPaymentSubmitAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmitAttches(" + Company + "," + SubmitReportID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WHTPaymentSubmitAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WHTPaymentSubmitAttch for the service
   Description: Calls UpdateExt to update WHTPaymentSubmitAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WHTPaymentSubmitAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WHTPaymentSubmitAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WHTPaymentSubmitAttches_Company_SubmitReportID_DrawingSeq(Company:string, SubmitReportID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmitAttches(" + Company + "," + SubmitReportID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete WHTPaymentSubmitAttch item
   Description: Call UpdateExt to delete WHTPaymentSubmitAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WHTPaymentSubmitAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SubmitReportID Desc: SubmitReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WHTPaymentSubmitAttches_Company_SubmitReportID_DrawingSeq(Company:string, SubmitReportID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/WHTPaymentSubmitAttches(" + Company + "," + SubmitReportID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentSubmitListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitListRow)
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
export function get_GetRows(whereClauseWHTPaymentSubmit:string, whereClauseWHTPaymentSubmitAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseWHTPaymentSubmit!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWHTPaymentSubmit=" + whereClauseWHTPaymentSubmit
   }
   if(typeof whereClauseWHTPaymentSubmitAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWHTPaymentSubmitAttch=" + whereClauseWHTPaymentSubmitAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetRows" + params, {
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
export function get_GetByID(submitReportID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof submitReportID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "submitReportID=" + submitReportID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetList" + params, {
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
   Summary: Invoke method SetDatePeriod
   Description: Call this method to set date period.
   OperationID: SetDatePeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDatePeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDatePeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetDatePeriod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/SetDatePeriod", {
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
   Summary: Invoke method GetWHTaxReports
   Description: This method get Withholding Tax Reports for specific period
   OperationID: GetWHTaxReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWHTaxReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWHTaxReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWHTaxReports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetWHTaxReports", {
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
   Summary: Invoke method ExcludeWHTaxReport
   Description: This method exclude Withholding Tax Report from current export
   OperationID: ExcludeWHTaxReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExcludeWHTaxReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExcludeWHTaxReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExcludeWHTaxReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/ExcludeWHTaxReport", {
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
   Description: Export Withholding Tax Payments to file.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GenExportFile", {
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
   Summary: Invoke method SetSubmitted
   Description: This method set status to Submitted
   OperationID: SetSubmitted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSubmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSubmitted(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/SetSubmitted", {
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
   Summary: Invoke method ResetStatus
   Description: This method reset status from Submitted
   OperationID: ResetStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/ResetStatus", {
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
   Summary: Invoke method PostReport
   Description: This method set status to Closed
   OperationID: PostReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/PostReport", {
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
   Summary: Invoke method GetNewWHTPaymentSubmit
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWHTPaymentSubmit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWHTPaymentSubmit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWHTPaymentSubmit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWHTPaymentSubmit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetNewWHTPaymentSubmit", {
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
   Summary: Invoke method GetNewWHTPaymentSubmitAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWHTPaymentSubmitAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWHTPaymentSubmitAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWHTPaymentSubmitAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWHTPaymentSubmitAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetNewWHTPaymentSubmitAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSubmitSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WHTPaymentSubmitAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WHTPaymentSubmitListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentSubmitRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WHTPaymentSubmitRow[],
}

export interface Erp_Tablesets_WHTPaymentSubmitAttchRow{
   "Company":string,
   "SubmitReportID":string,
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

export interface Erp_Tablesets_WHTPaymentSubmitListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Submit Report ID.  */  
   "SubmitReportID":string,
      /**  Report Description.  */  
   "Description":string,
      /**  Module AR or AP.  */  
   "Module":string,
      /**  Report date.  */  
   "ReportDate":string,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Quarter of fiscal year.  */  
   "Quarter":string,
      /**  Tax Report Category.  */  
   "RptCatCode":string,
      /**  Start date of the report period.  */  
   "StartDate":string,
      /**  End date of the report period.  */  
   "EndDate":string,
      /**  The user who submitted the report.  */  
   "SubmittedBy":string,
      /**  The date and time of submitting.  */  
   "SubmittedOn":string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   "ReportStatus":number,
      /**  The unique report sequence.  */  
   "ReportSequence":number,
      /**  Electronic Interface Unique Identifier.  */  
   "EFTHeadUID":number,
      /**  Output file path.  */  
   "OutputFile":string,
      /**  Export in test mode.  */  
   "TestMode":boolean,
      /**  The user who created the report.  */  
   "CreatedBy":string,
      /**  The date and time of creating.  */  
   "CreatedOn":string,
      /**  The last user who changed the report.  */  
   "ChangedBy":string,
      /**  The date and time of last changing.  */  
   "ChangedOn":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WHTPaymentSubmitRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Submit Report ID.  */  
   "SubmitReportID":string,
      /**  Report Description.  */  
   "Description":string,
      /**  Module AR or AP.  */  
   "Module":string,
      /**  Report date.  */  
   "ReportDate":string,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Quarter of fiscal year.  */  
   "Quarter":string,
      /**  Tax Report Category.  */  
   "RptCatCode":string,
      /**  Start date of the report period.  */  
   "StartDate":string,
      /**  End date of the report period.  */  
   "EndDate":string,
      /**  The user who submitted the report.  */  
   "SubmittedBy":string,
      /**  The date and time of submitting.  */  
   "SubmittedOn":string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   "ReportStatus":number,
      /**  Report comment.  */  
   "Notes":string,
      /**  The unique report sequence.  */  
   "ReportSequence":number,
      /**  Electronic Interface Unique Identifier.  */  
   "EFTHeadUID":number,
      /**  Output file path.  */  
   "OutputFile":string,
      /**  Export in test mode.  */  
   "TestMode":boolean,
      /**  Token number for previous period.  */  
   "TokenForPreviousQuarter":string,
      /**  The user who created the report.  */  
   "CreatedBy":string,
      /**  The date and time of creating.  */  
   "CreatedOn":string,
      /**  The last user who changed the report.  */  
   "ChangedBy":string,
      /**  The date and time of last changing.  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Period  */  
   "Period":number,
      /**  DateSelection  */  
   "DateSelection":string,
      /**  Fiscal calendar description  */  
   "FiscalCalendarDescription":string,
      /**  Report is closed for changing or not.  */  
   "IsClosed":boolean,
      /**  Report was submitted or not.  */  
   "IsSubmitted":boolean,
   "HasWHTPaymentReports":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param submitReportID
   */  
export interface DeleteByID_input{
   submitReportID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtWHTPaymentSubmitTableset{
   WHTPaymentSubmit:Erp_Tablesets_WHTPaymentSubmitRow[],
   WHTPaymentSubmitAttch:Erp_Tablesets_WHTPaymentSubmitAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WHTPaymentSubmitAttchRow{
   Company:string,
   SubmitReportID:string,
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

export interface Erp_Tablesets_WHTPaymentSubmitListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Submit Report ID.  */  
   SubmitReportID:string,
      /**  Report Description.  */  
   Description:string,
      /**  Module AR or AP.  */  
   Module:string,
      /**  Report date.  */  
   ReportDate:string,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Fiscal year.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Quarter of fiscal year.  */  
   Quarter:string,
      /**  Tax Report Category.  */  
   RptCatCode:string,
      /**  Start date of the report period.  */  
   StartDate:string,
      /**  End date of the report period.  */  
   EndDate:string,
      /**  The user who submitted the report.  */  
   SubmittedBy:string,
      /**  The date and time of submitting.  */  
   SubmittedOn:string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   ReportStatus:number,
      /**  The unique report sequence.  */  
   ReportSequence:number,
      /**  Electronic Interface Unique Identifier.  */  
   EFTHeadUID:number,
      /**  Output file path.  */  
   OutputFile:string,
      /**  Export in test mode.  */  
   TestMode:boolean,
      /**  The user who created the report.  */  
   CreatedBy:string,
      /**  The date and time of creating.  */  
   CreatedOn:string,
      /**  The last user who changed the report.  */  
   ChangedBy:string,
      /**  The date and time of last changing.  */  
   ChangedOn:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WHTPaymentSubmitListTableset{
   WHTPaymentSubmitList:Erp_Tablesets_WHTPaymentSubmitListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WHTPaymentSubmitRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Submit Report ID.  */  
   SubmitReportID:string,
      /**  Report Description.  */  
   Description:string,
      /**  Module AR or AP.  */  
   Module:string,
      /**  Report date.  */  
   ReportDate:string,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Fiscal year.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Quarter of fiscal year.  */  
   Quarter:string,
      /**  Tax Report Category.  */  
   RptCatCode:string,
      /**  Start date of the report period.  */  
   StartDate:string,
      /**  End date of the report period.  */  
   EndDate:string,
      /**  The user who submitted the report.  */  
   SubmittedBy:string,
      /**  The date and time of submitting.  */  
   SubmittedOn:string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   ReportStatus:number,
      /**  Report comment.  */  
   Notes:string,
      /**  The unique report sequence.  */  
   ReportSequence:number,
      /**  Electronic Interface Unique Identifier.  */  
   EFTHeadUID:number,
      /**  Output file path.  */  
   OutputFile:string,
      /**  Export in test mode.  */  
   TestMode:boolean,
      /**  Token number for previous period.  */  
   TokenForPreviousQuarter:string,
      /**  The user who created the report.  */  
   CreatedBy:string,
      /**  The date and time of creating.  */  
   CreatedOn:string,
      /**  The last user who changed the report.  */  
   ChangedBy:string,
      /**  The date and time of last changing.  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Period  */  
   Period:number,
      /**  DateSelection  */  
   DateSelection:string,
      /**  Fiscal calendar description  */  
   FiscalCalendarDescription:string,
      /**  Report is closed for changing or not.  */  
   IsClosed:boolean,
      /**  Report was submitted or not.  */  
   IsSubmitted:boolean,
   HasWHTPaymentReports:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WHTPaymentSubmitTableset{
   WHTPaymentSubmit:Erp_Tablesets_WHTPaymentSubmitRow[],
   WHTPaymentSubmitAttch:Erp_Tablesets_WHTPaymentSubmitAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param reportID
      @param submitReportID
   */  
export interface ExcludeWHTaxReport_input{
      /**  WHT Report ID  */  
   reportID:string,
      /**  WHT Payment Submit Report ID  */  
   submitReportID:string,
}

export interface ExcludeWHTaxReport_output{
   returnObj:boolean,
}

   /** Required : 
      @param submitReportID
      @param eftHeadUID
      @param exportFileName
   */  
export interface GenExportFile_input{
      /**  WHT Payment Submit Report ID  */  
   submitReportID:string,
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
}
}

   /** Required : 
      @param submitReportID
   */  
export interface GetByID_input{
   submitReportID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_WHTPaymentSubmitTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_WHTPaymentSubmitTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_WHTPaymentSubmitTableset[],
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
   returnObj:Erp_Tablesets_WHTPaymentSubmitListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param submitReportID
   */  
export interface GetNewWHTPaymentSubmitAttch_input{
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
   submitReportID:string,
}

export interface GetNewWHTPaymentSubmitAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewWHTPaymentSubmit_input{
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
}

export interface GetNewWHTPaymentSubmit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
}
}

   /** Required : 
      @param whereClauseWHTPaymentSubmit
      @param whereClauseWHTPaymentSubmitAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseWHTPaymentSubmit:string,
   whereClauseWHTPaymentSubmitAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_WHTPaymentSubmitTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param submitReportID
   */  
export interface GetWHTaxReports_input{
      /**  WHT Report ID  */  
   submitReportID:string,
}

export interface GetWHTaxReports_output{
   returnObj:boolean,
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
      @param submitReportID
   */  
export interface PostReport_input{
      /**  WHT Payment Submit Report ID  */  
   submitReportID:string,
}

export interface PostReport_output{
}

   /** Required : 
      @param submitReportID
   */  
export interface ResetStatus_input{
      /**  WHT Payment Submit Report ID  */  
   submitReportID:string,
}

export interface ResetStatus_output{
}

   /** Required : 
      @param ds
   */  
export interface SetDatePeriod_input{
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
}

export interface SetDatePeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
}
}

   /** Required : 
      @param submitReportID
   */  
export interface SetSubmitted_input{
      /**  WHT Payment Submit Report ID  */  
   submitReportID:string,
}

export interface SetSubmitted_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtWHTPaymentSubmitTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtWHTPaymentSubmitTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentSubmitTableset[],
}
}

