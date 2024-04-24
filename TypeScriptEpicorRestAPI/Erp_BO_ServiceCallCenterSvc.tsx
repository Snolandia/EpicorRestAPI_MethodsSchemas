import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ServiceCallCenterSvc
// Description: Field Service Call Center Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/$metadata", {
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
   Description: Get ServiceCallCenters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceCallCenters
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdRow
   */  
export function get_ServiceCallCenters(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceCallCenters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ServiceCallCenters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters", {
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
   Summary: Calls GetByID to retrieve the ServiceCallCenter item
   Description: Calls GetByID to retrieve the ServiceCallCenter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceCallCenter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
   */  
export function get_ServiceCallCenters_Company_CallNum(Company:string, CallNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallhdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallhdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ServiceCallCenter for the service
   Description: Calls UpdateExt to update ServiceCallCenter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceCallCenter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ServiceCallCenters_Company_CallNum(Company:string, CallNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")", {
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
   Summary: Call UpdateExt to delete ServiceCallCenter item
   Description: Call UpdateExt to delete ServiceCallCenter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceCallCenter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ServiceCallCenters_Company_CallNum(Company:string, CallNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")", {
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
   Description: Get FSCallDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSCallDts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtRow
   */  
export function get_ServiceCallCenters_Company_CallNum_FSCallDts(Company:string, CallNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallDts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSCallDt item
   Description: Calls GetByID to retrieve the FSCallDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   */  
export function get_ServiceCallCenters_Company_CallNum_FSCallDts_Company_CallNum_CallLine(Company:string, CallNum:string, CallLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FsTeches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FsTeches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsTechRow
   */  
export function get_ServiceCallCenters_Company_CallNum_FsTeches(Company:string, CallNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsTechRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FsTeches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsTechRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FsTech item
   Description: Calls GetByID to retrieve the FsTech item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsTech1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FsTechRow
   */  
export function get_ServiceCallCenters_Company_CallNum_FsTeches_Company_CallNum_SeqNum(Company:string, CallNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FsTechRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FsTechRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FSCallhdAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSCallhdAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdAttchRow
   */  
export function get_ServiceCallCenters_Company_CallNum_FSCallhdAttches(Company:string, CallNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallhdAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSCallhdAttch item
   Description: Calls GetByID to retrieve the FSCallhdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallhdAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   */  
export function get_ServiceCallCenters_Company_CallNum_FSCallhdAttches_Company_CallNum_DrawingSeq(Company:string, CallNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallhdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallhdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FSCallDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallDts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtRow
   */  
export function get_FSCallDts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallDts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSCallDts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts", {
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
   Summary: Calls GetByID to retrieve the FSCallDt item
   Description: Calls GetByID to retrieve the FSCallDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   */  
export function get_FSCallDts_Company_CallNum_CallLine(Company:string, CallNum:string, CallLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSCallDt for the service
   Description: Calls UpdateExt to update FSCallDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSCallDts_Company_CallNum_CallLine(Company:string, CallNum:string, CallLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")", {
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
   Summary: Call UpdateExt to delete FSCallDt item
   Description: Call UpdateExt to delete FSCallDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSCallDts_Company_CallNum_CallLine(Company:string, CallNum:string, CallLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")", {
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
   Description: Get FSCallDtAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSCallDtAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtAttchRow
   */  
export function get_FSCallDts_Company_CallNum_CallLine_FSCallDtAttches(Company:string, CallNum:string, CallLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")/FSCallDtAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSCallDtAttch item
   Description: Calls GetByID to retrieve the FSCallDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDtAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   */  
export function get_FSCallDts_Company_CallNum_CallLine_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company:string, CallNum:string, CallLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FSCallDtAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallDtAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtAttchRow
   */  
export function get_FSCallDtAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallDtAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSCallDtAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches", {
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
   Summary: Calls GetByID to retrieve the FSCallDtAttch item
   Description: Calls GetByID to retrieve the FSCallDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   */  
export function get_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company:string, CallNum:string, CallLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSCallDtAttch for the service
   Description: Calls UpdateExt to update FSCallDtAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallDtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company:string, CallNum:string, CallLine:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FSCallDtAttch item
   Description: Call UpdateExt to delete FSCallDtAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallDtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company:string, CallNum:string, CallLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")", {
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
   Description: Get FsTeches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FsTeches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsTechRow
   */  
export function get_FsTeches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsTechRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsTechRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FsTeches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FsTechRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FsTechRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FsTeches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches", {
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
   Summary: Calls GetByID to retrieve the FsTech item
   Description: Calls GetByID to retrieve the FsTech item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsTech
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FsTechRow
   */  
export function get_FsTeches_Company_CallNum_SeqNum(Company:string, CallNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FsTechRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FsTechRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FsTech for the service
   Description: Calls UpdateExt to update FsTech. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FsTech
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FsTechRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FsTeches_Company_CallNum_SeqNum(Company:string, CallNum:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete FsTech item
   Description: Call UpdateExt to delete FsTech item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FsTech
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FsTeches_Company_CallNum_SeqNum(Company:string, CallNum:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")", {
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
   Description: Get FSCallhdAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallhdAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdAttchRow
   */  
export function get_FSCallhdAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallhdAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSCallhdAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches", {
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
   Summary: Calls GetByID to retrieve the FSCallhdAttch item
   Description: Calls GetByID to retrieve the FSCallhdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallhdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   */  
export function get_FSCallhdAttches_Company_CallNum_DrawingSeq(Company:string, CallNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallhdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallhdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSCallhdAttch for the service
   Description: Calls UpdateExt to update FSCallhdAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallhdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSCallhdAttches_Company_CallNum_DrawingSeq(Company:string, CallNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FSCallhdAttch item
   Description: Call UpdateExt to delete FSCallhdAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallhdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSCallhdAttches_Company_CallNum_DrawingSeq(Company:string, CallNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdListRow)
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
export function get_GetRows(whereClauseFSCallhd:string, whereClauseFSCallhdAttch:string, whereClauseFSCallDt:string, whereClauseFSCallDtAttch:string, whereClauseFsTech:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFSCallhd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSCallhd=" + whereClauseFSCallhd
   }
   if(typeof whereClauseFSCallhdAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSCallhdAttch=" + whereClauseFSCallhdAttch
   }
   if(typeof whereClauseFSCallDt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSCallDt=" + whereClauseFSCallDt
   }
   if(typeof whereClauseFSCallDtAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSCallDtAttch=" + whereClauseFSCallDtAttch
   }
   if(typeof whereClauseFsTech!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFsTech=" + whereClauseFsTech
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetRows" + params, {
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
export function get_GetByID(callNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof callNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "callNum=" + callNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetList" + params, {
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
   Summary: Invoke method ExpireDate
   Description: Expire Date
   OperationID: ExpireDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpireDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ExpireDate", {
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
   Summary: Invoke method ActivateServiceCall
   Description: This method activates the Service Call.
   OperationID: ActivateServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ActivateServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ActivateServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ActivateServiceCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ActivateServiceCall", {
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
   Summary: Invoke method AssignTechnician
   Description: This method assigns a Service Technician to a service call.
   OperationID: AssignTechnician
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignTechnician_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignTechnician_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignTechnician(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/AssignTechnician", {
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
   Summary: Invoke method ChangeDtlContractLine
   Description: Update Service Call Line Contract information when the Contract Line Number field changes.
   OperationID: ChangeDtlContractLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlContractLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlContractLine", {
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
   Summary: Invoke method ChangeDtlContractNum
   Description: Update Service Call Line Contract information when the Contract Number field changes.
   OperationID: ChangeDtlContractNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlContractNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlContractNum", {
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
   Summary: Invoke method ChangeDtlDropShipPackLine
   Description: Update Service Call Line Warranty information when the Drop Shipment PackLine Number field changes.
   OperationID: ChangeDtlDropShipPackLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlDropShipPackLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlDropShipPackLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlDropShipPackLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlDropShipPackLine", {
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
   Summary: Invoke method ChangeDtlDropShipPackSlip
   Description: Update Service Call Line Warranty information when the Drop Shipment PackSlip field changes.
   OperationID: ChangeDtlDropShipPackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlDropShipPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlDropShipPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlDropShipPackSlip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlDropShipPackSlip", {
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
   Summary: Invoke method ChangeDtlPackLine
   Description: Update Service Call Line Warranty information when the Pack Line Number field changes.
   OperationID: ChangeDtlPackLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlPackLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlPackLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlPackLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlPackLine", {
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
   Summary: Invoke method ChangeDtlPackNum
   Description: Update Service Call Line Warranty information when the Pack ID field changes.
   OperationID: ChangeDtlPackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlPackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlPackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlPackNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlPackNum", {
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
   Summary: Invoke method ChangeDtlPartNum
   Description: Update Service Call Line information when the Part Number field changes.
   OperationID: ChangeDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlPartNum", {
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
   Summary: Invoke method ChangeDtlRevisionNum
   Description: Update Service Call Line information when the Revision Number field changes.
   OperationID: ChangeDtlRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlRevisionNum", {
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
   Summary: Invoke method ChangeDtlSerialNum
   Description: Update Service Call Line Serial Number/Contract information when the Serial Number field changes.
   OperationID: ChangeDtlSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlSerialNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlSerialNum", {
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
   Summary: Invoke method ChangeDtlXPartNum
   Description: Update Service Call Line information when the Customer Part Number field changes.
   OperationID: ChangeDtlXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlXPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeDtlXPartNum", {
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
   Summary: Invoke method ChangeFSCallDtProjectID
   Description: Method to call when changing the project id on the service call detail record.
Validates the id and updates FSCallDt with values from the project.
   OperationID: ChangeFSCallDtProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSCallDtProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSCallDtProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSCallDtProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeFSCallDtProjectID", {
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
   Summary: Invoke method ChangeHdrBillToContact
   Description: This method updates the related Customer Contact information when the Customer
Bill To Contact field (FSCallHd.PrcConNum) changes.
   OperationID: ChangeHdrBillToContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrBillToContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrBillToContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrBillToContact(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrBillToContact", {
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
   Summary: Invoke method ChangeHdrCallCode
   Description: This method gets the default Tax Category and Call Comment when the Service
Call Type field (FSCallHd.CallCode) changes.
   OperationID: ChangeHdrCallCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrCallCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCallCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrCallCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrCallCode", {
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
   Summary: Invoke method ChangeHdrCurrencyCode
   Description: This method gets the appropriate exchange rate for the new currency.  Call this
method when the field FSCallHd.CurrencyCode changes.
   OperationID: ChangeHdrCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrCurrencyCode", {
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
   Summary: Invoke method ChangeHdrCustID
   Description: This method updates the related Customer and ShipTo information when the Customer ID
field (FSCallHd.CustNumCustID) changes.
   OperationID: ChangeHdrCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrCustID", {
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
   Summary: Invoke method ChangeHdrRequestTime
   Description: Validates the entered RequestTime.
   OperationID: ChangeHdrRequestTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrRequestTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrRequestTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrRequestTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrRequestTime", {
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
   Summary: Invoke method ChangeHdrSchedTime
   Description: This method validates the entered Scheduled Time.  Call this method when the
field FSCallHd.DispSchedTime changes.
   OperationID: ChangeHdrSchedTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrSchedTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrSchedTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrSchedTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrSchedTime", {
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
   Summary: Invoke method ChangeHdrShipToContact
   Description: This method updates the related Customer Ship To Contact information when the Customer
Ship To Contact field (FSCallHd.ShpConNum) changes.
   OperationID: ChangeHdrShipToContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrShipToContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrShipToContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrShipToContact(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrShipToContact", {
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
   Summary: Invoke method ChangeHdrShipToCustID
   Description: This method updates the ShipTo information when the ShipToCustID
field (Link) changes.
   OperationID: ChangeHdrShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrShipToCustID", {
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
   Summary: Invoke method ChangeHdrShipToNum
   Description: This method updates the related ShipTo information when the Customer ShipTo Number
field (FSCallHd.ShipToNum) changes.
   OperationID: ChangeHdrShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrShipToNum", {
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
   Summary: Invoke method ChangeHdrUseOTS
   Description: Method to call when changing the UseOTS field.
Refreshes the address list and contact info
   OperationID: ChangeHdrUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrUseOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrUseOTS", {
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
   Summary: Invoke method ChangeHdrHDCaseNum
   Description: This method validates the proposed Case Number.
   OperationID: ChangeHdrHDCaseNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrHDCaseNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrHDCaseNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHdrHDCaseNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeHdrHDCaseNum", {
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
   Summary: Invoke method CheckDtlSerialNum
   Description: Check the serial number field and return messages about the serial number to
the user.  The method will check the following:
The serial number exists
The customer and ship to matches
The part number on the line matches the serial part number
The contract number and line matches (if applicable)
The pack id matches (if appicable)
If any of these conditions are met where the data in the service contract doesn
not match the data for the serial number, the user is prompted with this information
and asked if they would like to continue with the save.
   OperationID: CheckDtlSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlSerialNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/CheckDtlSerialNum", {
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
   Summary: Invoke method CheckPrePartInfo
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, a part number and if any substitutes exist.  Call this method
first before calling the ChangeDtlPartNum method when the field FSCallDt.PartNum changes.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPrePartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/CheckPrePartInfo", {
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
   Summary: Invoke method CheckRateGrpCode
   Description: Update Service Call information when the currency is changed.
   OperationID: CheckRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRateGrpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/CheckRateGrpCode", {
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
   Summary: Invoke method CloseServiceCall
   Description: This method closes the Service Call.  Run this method after calling PreCloseServiceCall.
   OperationID: CloseServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseServiceCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/CloseServiceCall", {
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
   Summary: Invoke method CreateServiceCallJob
   Description: This method creates the Service Call Job for the service call line.  A warning message
is returned by this method if the service call plant and the current plant is not the
same.  Do not call the JobEntry object if the opMessage is not blank.
   OperationID: CreateServiceCallJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateServiceCallJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateServiceCallJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateServiceCallJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/CreateServiceCallJob", {
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
   Summary: Invoke method GetXPartByPartNum
   Description: This method gets the first CustXPart found by using customer number and part number to find it.
   OperationID: GetXPartByPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetXPartByPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetXPartByPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetXPartByPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetXPartByPartNum", {
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
   Summary: Invoke method FindPart
   Description: FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FindPart", {
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
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID.
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetPartFromRowID", {
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
   Description: Method to call to get a Code Description list.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetCodeDescList", {
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
   Summary: Invoke method GetFSCallhdReadyForInvoice
   Description: Returns list of FSCallHd ready to be invoiced.
The standard GetList will not work anymore because need to only return rows where Job is open
   OperationID: GetFSCallhdReadyForInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFSCallhdReadyForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFSCallhdReadyForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFSCallhdReadyForInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetFSCallhdReadyForInvoice", {
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
   Summary: Invoke method GetListRemoveInvoiced
   Description: Returns a list of FSCallhd rows that satisfy the where clause and remove invoiced detail lines
   OperationID: GetListRemoveInvoiced
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListRemoveInvoiced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListRemoveInvoiced_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListRemoveInvoiced(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetListRemoveInvoiced", {
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
   Summary: Invoke method GetNewFSCallHd1
   Description: This method is to be used in place of GetNewFSCallHd.  This method asks for
customer number and shipto number to default the fields based on the customer/shipto.
   OperationID: GetNewFSCallHd1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallHd1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallHd1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSCallHd1(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetNewFSCallHd1", {
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
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetPartXRefInfo", {
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
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetRowsContactTracker", {
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
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetRowsCustomerTracker", {
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
   Summary: Invoke method PreCloseServiceCall
   Description: Checks to see if the service call can be closed and gives a warning message
to let the user decide to continue closing or not.  This method should be called
prior to calling the CloseServiceCall method which does the actual closing logic.
If a warning message returns with this method and the user chooses to continue
or NO warning message then call CloseServiceCall method else cancel close request.
   OperationID: PreCloseServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCloseServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCloseServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCloseServiceCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/PreCloseServiceCall", {
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
   Summary: Invoke method ReopenServiceCall
   Description: This method reopens the Service Call.
   OperationID: ReopenServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReopenServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReopenServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReopenServiceCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ReopenServiceCall", {
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
   Summary: Invoke method VoidServiceCall
   Description: This method voids the Service Call.
   OperationID: VoidServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidServiceCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/VoidServiceCall", {
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
   Summary: Invoke method ChangeIssueTopics
   Description: This method should be invoked when the IssueTopics changes.
Validates and sets the individual IssueTopic fields.
   OperationID: ChangeIssueTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeIssueTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIssueTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeIssueTopics(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeIssueTopics", {
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
   Summary: Invoke method ChangeResTopics
   Description: This method should be invoked when the ResTopics changes.
Validates and sets the individual ResTopic fields.
   OperationID: ChangeResTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeResTopics(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeResTopics", {
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
   Summary: Invoke method ChangeBTCustID
   Description: This method updates the Bill To customer info.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ChangeBTCustID", {
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
   Summary: Invoke method ValidateOTSTaxID
   Description: ValidateOTSTaxID
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOTSTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ValidateOTSTaxID", {
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
   Summary: Invoke method GetNewFSCallhd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSCallhd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetNewFSCallhd", {
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
   Summary: Invoke method GetNewFSCallhdAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallhdAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallhdAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallhdAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSCallhdAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetNewFSCallhdAttch", {
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
   Summary: Invoke method GetNewFSCallDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSCallDt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetNewFSCallDt", {
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
   Summary: Invoke method GetNewFSCallDtAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallDtAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallDtAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallDtAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSCallDtAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetNewFSCallDtAttch", {
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
   Summary: Invoke method GetNewFsTech
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFsTech
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFsTech_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFsTech_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFsTech(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetNewFsTech", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSCallDtAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSCallDtRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSCallhdAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSCallhdListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSCallhdRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsTechRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FsTechRow[],
}

export interface Erp_Tablesets_FSCallDtAttchRow{
   "Company":string,
   "CallNum":number,
   "CallLine":number,
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

export interface Erp_Tablesets_FSCallDtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   "CallNum":number,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   "CallLine":number,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Serial number of the part being repaired.  */  
   "SerialNumber":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  TotalCall Quantity for the line item.  */  
   "CallQty":number,
      /**  Packing slip number that this Service call is linked with.  */  
   "PackNum":number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   "PackLine":number,
      /**  Unique code for the Warranty  */  
   "WarrantyCode":string,
      /**  Contract Number if this item is under a contract  */  
   "ContractNum":number,
      /**  This is the contract line the relates to the item on the service call.  */  
   "ContractLine":number,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  */  
   "CallComment":string,
      /**  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Problem reason code from the reason master table. type problem.  */  
   "ProbReasonCode":string,
      /**  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  total Labor Amount.  */  
   "TotLabor":number,
      /**  total Labor Amount. In customers currency  */  
   "DocTotLabor":number,
      /**  total Billable Labor Amount.  */  
   "TotBillLabor":number,
      /**  total Billable Labor Amount. In Customers currency.  */  
   "DocTotBillLabor":number,
      /**  total Material Amount.  */  
   "TotMaterial":number,
      /**  total Material Amount. In Customers currency  */  
   "DocTotMaterial":number,
      /**  total Billable Material Amount.  */  
   "TotBillMaterial":number,
      /**  total Billable Material Amount. In Customers Currency.  */  
   "DocTotBillMaterial":number,
      /**  total Misc. Amount.  */  
   "TotMisc":number,
      /**  total Misc. Amount. In customers currency.  */  
   "DocTotMisc":number,
      /**  total Billable Misc. Amount.  */  
   "TotBillableMisc":number,
      /**  total Billable Misc. Amount. In customer's currency.  */  
   "DocTotBillableMisc":number,
      /**  total Material Cost.  */  
   "TotMaterialCost":number,
      /**  total Misc. Cost.  */  
   "TotMiscCost":number,
      /**  Project ID of the Project table record that this FSCallDt record. Can be blank.  */  
   "ProjectID":string,
      /**  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Total Subcontract Amount.  */  
   "TotSubCont":number,
      /**  total Subcontract Amount. In customers currency  */  
   "DocTotSubCont":number,
      /**  total Billable Subcontract Amount.  */  
   "TotBillSubCont":number,
      /**  total Billable Subcontract Amount. In Customers currency.  */  
   "DocTotBillSubCont":number,
      /**  total Estimated Labor Amount.  */  
   "TotEstLabor":number,
      /**  total estimated Labor Amount. In customers currency  */  
   "DocTotEstLabor":number,
      /**  total Estimated Material Amount.  */  
   "TotEstMaterial":number,
      /**  total Estimated Material Amount. In Customers currency  */  
   "DocTotEstMaterial":number,
      /**  total Estimated Misc. Amount.  Future Use.  */  
   "TotEstMisc":number,
      /**  total Est. Misc. Amount. In customers currency. Future use  */  
   "DocTotEstMisc":number,
      /**  Total estimated Subcontract Amount.  */  
   "TotEstSubCont":number,
      /**  total Estimated Subcontract Amount. In customers currency  */  
   "DocTotEstSubCont":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotSubCont":number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   "DropShipPackSlip":string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   "DropShipPackLine":number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   "VendorNum":number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   "PurPoint":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  POLine  */  
   "POLine":string,
      /**  IssueTopicID1  */  
   "IssueTopicID1":string,
      /**  IssueTopicID2  */  
   "IssueTopicID2":string,
      /**  IssueTopicID3  */  
   "IssueTopicID3":string,
      /**  IssueTopicID4  */  
   "IssueTopicID4":string,
      /**  IssueTopicID5  */  
   "IssueTopicID5":string,
      /**  IssueTopicID6  */  
   "IssueTopicID6":string,
      /**  IssueTopicID7  */  
   "IssueTopicID7":string,
      /**  IssueTopicID8  */  
   "IssueTopicID8":string,
      /**  IssueTopicID9  */  
   "IssueTopicID9":string,
      /**  IssueTopicID10  */  
   "IssueTopicID10":string,
      /**  IssueTopics  */  
   "IssueTopics":string,
      /**  ResTopicID1  */  
   "ResTopicID1":string,
      /**  ResTopicID2  */  
   "ResTopicID2":string,
      /**  ResTopicID3  */  
   "ResTopicID3":string,
      /**  ResTopicID4  */  
   "ResTopicID4":string,
      /**  ResTopicID5  */  
   "ResTopicID5":string,
      /**  ResTopicID6  */  
   "ResTopicID6":string,
      /**  ResTopicID7  */  
   "ResTopicID7":string,
      /**  ResTopicID8  */  
   "ResTopicID8":string,
      /**  ResTopicID9  */  
   "ResTopicID9":string,
      /**  ResTopicID10  */  
   "ResTopicID10":string,
      /**  ResTopics  */  
   "ResTopics":string,
      /**  PartDescription  */  
   "PartDescription":string,
      /**  CommentText  */  
   "CommentText":string,
      /**  Indicates the invoice processing has been done for this call line.  */  
   "Invoiced":boolean,
      /**  Indicates that the call line can be invoiced.  */  
   "ReadyToInvoice":boolean,
      /**  Currency.CurrSymbol of the "BASE" currency  */  
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DisplayContractType":string,
      /**  Currency.CurrSymbol of the customer's currency  */  
   "DocCurrSymbol":string,
      /**  Total Billable Call Amount for the line in customer's currency  */  
   "DocTotLineBillCall":number,
      /**  Total Actual Call Amount for the line in customer's currency  */  
   "DocTotLineCall":number,
      /**  Total Estimated Call AMount for the line in customer's currency  */  
   "DocTotLineEstCall":number,
      /**  Indicates if Contract entry should be enabled.  */  
   "EnableContract":boolean,
      /**  Indicates if Warranty entry should be enabled.  */  
   "EnableWarranty":boolean,
      /**  Unit of Measure Description  */  
   "IUMDesc":string,
      /**  Reson Code Description  */  
   "ProbReasonDesc":string,
   "Rpt1TotLineBillCall":number,
   "Rpt1TotLineCall":number,
   "Rpt1TotLineEstCall":number,
   "Rpt2TotLineBillCall":number,
   "Rpt2TotLineCall":number,
   "Rpt2TotLineEstCall":number,
   "Rpt3TotLineBillCall":number,
   "Rpt3TotLineCall":number,
   "Rpt3TotLineEstCall":number,
      /**  Total Billable Call Amount for the line  */  
   "TotLineBillCall":number,
      /**  Total Actual Call Amount for the line  */  
   "TotLineCall":number,
      /**  Total Estimated Call Amount for the line  */  
   "TotLineEstCall":number,
   "JobClosed":boolean,
   "BitFlag":number,
   "ContractCodeContractDescription":string,
   "ContractLineLineDesc":string,
   "DropShipDtlLineDesc":string,
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
   "JobNumPartDescription":string,
   "PackLineLineDesc":string,
   "PackNumShipStatus":string,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
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
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSCallhdAttchRow{
   "Company":string,
   "CallNum":number,
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

export interface Erp_Tablesets_FSCallhdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   "CallNum":number,
      /**  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  defaults to TODAY  */  
   "EntryDate":string,
      /**  Time in second past midnight  */  
   "EntryTime":number,
      /**  The date that the service is requested for.  */  
   "RequestDate":string,
      /**  Time in second past midnight  */  
   "RequestTime":number,
      /**  The date that the service is scheduled for.  */  
   "SchedDate":string,
      /**  Time in second past midnight  */  
   "SchedTime":number,
      /**  The date that the service was performed on.  */  
   "ActualDate":string,
      /**  Time in second past midnight  */  
   "ActualTime":number,
      /**  Contains comments about the overall Call. These will be printed on the Service Call.  */  
   "CallComment":string,
      /**  Contains comments about the overall Call. These will be printed on the Service Call invoice.  */  
   "InvoiceComment":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Indicate that the call is open.  */  
   "OpenCall":boolean,
      /**  Indicates that the call is closed and can be invoiced.  */  
   "ReadyToInvoice":boolean,
      /**  Indicated the invoice processing has been done for this call.  */  
   "Invoiced":boolean,
      /**  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  */  
   "VoidCall":boolean,
      /**  Can have 3 values High, normal and, Low  */  
   "CallPriority":string,
      /**   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  A unique code that identifies the type of service call  */  
   "CallCode":string,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  */  
   "LaborComplete":boolean,
      /**  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  */  
   "MaterialComplete":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The estimated duration of the service call in days.  */  
   "Duration":number,
      /**  The Clientele call number that is related to this call.  */  
   "CLCallNum":string,
      /**  The help desk case that created this service call.  */  
   "HDCaseNum":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping country number  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Customer Contact Name  */  
   "CustConName":string,
      /**  Customer Phone Number  */  
   "CustPhoneNum":string,
      /**  Customer Fax Number  */  
   "CustFaxNum":string,
      /**  ShipTo Contact Name  */  
   "ShipConName":string,
      /**  ShipTo Phone Number  */  
   "ShipPhoneNum":string,
      /**  ShipTo Fax Number  */  
   "ShipFaxNum":string,
      /**  Currency Switch  */  
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   "BaseCurrSymbol":string,
      /**  Exchange Rate Label  */  
   "XRateLabel":string,
      /**  Total Estimated Material Amount  */  
   "TotEstMaterial":number,
      /**  Total Estimated Mateiral Amount in customer's currency  */  
   "DocTotEstMaterial":number,
      /**  Total Estimated Subcontract Amount  */  
   "TotEstSubContract":number,
      /**  Total Estimated Subcontract Amount in customer's currency  */  
   "DocTotEstSubcontract":number,
      /**  Total Estimated Miscellaneous Amount  */  
   "TotEstMisc":number,
      /**  Total Estimated Miscellaneous Amount in customer's currency  */  
   "DocTotEstMisc":number,
      /**  Total Estimated Call Amount  */  
   "TotEstCall":number,
      /**  Total Estimated Call Amount in customer's currency  */  
   "DocTotEstCall":number,
      /**  Total Actual Material Amount  */  
   "TotActMaterial":number,
      /**  Total Actual Material Amount in customer's currency  */  
   "DocTotActMaterial":number,
      /**  Total Actual Subcontract Amount  */  
   "TotActSubcontract":number,
      /**  Total Actual Subcontract Amount in  customer's currency  */  
   "DocTotActSubcontract":number,
      /**  Total Actual Miscellaneous Amount  */  
   "TotActMisc":number,
      /**  Total Actual Miscellaneous Amount in customer's currency  */  
   "DocTotActMisc":number,
      /**  Total Actual Call Amount  */  
   "TotActCall":number,
      /**  Total Actual Call Amount in customer's curreny  */  
   "DocTotActCall":number,
      /**  Total Billable Material Amount  */  
   "TotBillMaterial":number,
      /**  Total Billable Material Amount in customer's currency  */  
   "DocTotBillMaterial":number,
      /**  Total Billable Subcontract Amount  */  
   "TotBillSubcontract":number,
      /**  Total Billable Subcontract Amount in customer's currency  */  
   "DocTotBillSubcontract":number,
      /**  Total Billable Miscellaneous Amount  */  
   "TotBillMisc":number,
      /**  Total Billable Miscellaneous Amount  */  
   "DocTotBillMisc":number,
      /**  Total Billable Call Amount  */  
   "TotBillCall":number,
      /**  Total Billable Call Amount in customer's currency  */  
   "DocTotBillCall":number,
   "DispEntryTime":string,
   "DispRequestTime":string,
   "DispSchedTime":string,
   "DispActualTime":string,
      /**  Total Estimated Labor (Service) Amount  */  
   "TotEstLabor":number,
      /**  Total Estimated Labor (Service) Amount in customer's currency  */  
   "DocTotEstLabor":number,
      /**  Total Actual Labor (Service) Amount  */  
   "TotActLabor":number,
      /**  Total Actual Labor (Service) Amount in customer's currency  */  
   "DocTotActLabor":number,
      /**  Total Billable Labor (Service) Amount  */  
   "TotBillLabor":number,
      /**  Total Billable Labor (Service) Amount in customer's currency  */  
   "DocTotBillLabor":number,
      /**  Indicates if the Call Type Code field needs to be enabled.  */  
   "EnableCallType":boolean,
      /**  Indicates if the user can maintain a service call header/line.  */  
   "EnableServiceCall":boolean,
      /**  Indicates if the user can view customer tracker.  */  
   "EnableCustTracker":boolean,
      /**  Indicates if the user can create/update a service call job.  */  
   "EnableJobEntry":boolean,
      /**  Indicates if the user can access labor entry screen.  */  
   "EnableLaborEntry":boolean,
      /**  Indicates if the user can access the Miscellaneous Shipment screen.  */  
   "EnableMiscShip":boolean,
      /**  Indicates if the user can access Issue Material screen.  */  
   "EnableIssueMtl":boolean,
      /**  Indicates if the user can access Issue Return screen.  */  
   "EnableIssueReturn":boolean,
      /**  Indicates if the Reopen Service Call option should be enabled.  */  
   "EnableReopenCall":boolean,
      /**  Indicates if the customer on credit hold.  */  
   "CustOnCreditHold":boolean,
   "ShipEMailAddress":string,
   "CustEMailAddress":string,
   "Rpt1TotActCall":number,
   "Rpt2TotActCall":number,
   "Rpt3TotActCall":number,
   "Rpt1TotActLabor":number,
   "Rpt2TotActLabor":number,
   "Rpt3TotActLabor":number,
   "Rpt1TotActMaterial":number,
   "Rpt2TotActMaterial":number,
   "Rpt3TotActMaterial":number,
   "Rpt1TotActMisc":number,
   "Rpt2TotActMisc":number,
   "Rpt3TotActMisc":number,
   "Rpt1TotActSubcontract":number,
   "Rpt2TotActSubcontract":number,
   "Rpt3TotActSubcontract":number,
   "Rpt1TotBillCall":number,
   "Rpt2TotBillCall":number,
   "Rpt3TotBillCall":number,
   "Rpt1TotBillLabor":number,
   "Rpt2TotBillLabor":number,
   "Rpt3TotBillLabor":number,
   "Rpt1TotBillMaterial":number,
   "Rpt2TotBillMaterial":number,
   "Rpt3TotBillMaterial":number,
   "Rpt1TotBillMisc":number,
   "Rpt2TotBillMisc":number,
   "Rpt3TotBillMisc":number,
   "Rpt1TotBillSubcontract":number,
   "Rpt2TotBillSubcontract":number,
   "Rpt3TotBillSubcontract":number,
   "Rpt1TotEstCall":number,
   "Rpt2TotEstCall":number,
   "Rpt3TotEstCall":number,
   "Rpt1TotEstLabor":number,
   "Rpt2TotEstLabor":number,
   "Rpt3TotEstLabor":number,
   "Rpt1TotEstMaterial":number,
   "Rpt2TotEstMaterial":number,
   "Rpt3TotEstMaterial":number,
   "Rpt1TotEstMisc":number,
   "Rpt2TotEstMisc":number,
   "Rpt3TotEstMisc":number,
   "Rpt1TotEstSubcontract":number,
   "Rpt2TotEstSubcontract":number,
   "Rpt3TotEstSubcontract":number,
   "CustAllowOTS":boolean,
   "ShipToAddrList":string,
   "SoldToAddrList":string,
      /**  Bill To Customer Name  */  
   "BTCustName":string,
      /**  Delimited list of available bill to customers.  */  
   "AvailBTCustList":string,
   "BaseCurrencyID":string,
      /**  Description of the Call Type Code.  */  
   "CallCodeCallDescription":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**  Description  */  
   "CurrRateGrpDescription":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  */  
   "CustNumAllowShipTo3":boolean,
      /**  Country name  */  
   "OTSCountryNumDescription":string,
      /**  Full description for the Tax Region.  */  
   "OTSTaxRegionCodeDescription":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  The full name of the customer.  */  
   "ShipToName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustID":string,
      /**  Full description for the Sales Tax category.  */  
   "TaxCatIDDescription":string,
      /**  Boolean for selection of FSCallhdList  */  
   "Selected":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSCallhdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   "CallNum":number,
      /**  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  defaults to TODAY  */  
   "EntryDate":string,
      /**  Time in second past midnight  */  
   "EntryTime":number,
      /**  The date that the service is requested for.  */  
   "RequestDate":string,
      /**  Time in second past midnight  */  
   "RequestTime":number,
      /**  The date that the service is scheduled for.  */  
   "SchedDate":string,
      /**  Time in second past midnight  */  
   "SchedTime":number,
      /**  The date that the service was performed on.  */  
   "ActualDate":string,
      /**  Time in second past midnight  */  
   "ActualTime":number,
      /**  Contains comments about the overall Call. These will be printed on the Service Call.  */  
   "CallComment":string,
      /**  Contains comments about the overall Call. These will be printed on the Service Call invoice.  */  
   "InvoiceComment":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Indicate that the call is open.  */  
   "OpenCall":boolean,
      /**  Indicates that the call is closed and can be invoiced.  */  
   "ReadyToInvoice":boolean,
      /**  Indicated the invoice processing has been done for this call.  */  
   "Invoiced":boolean,
      /**  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  */  
   "VoidCall":boolean,
      /**  Can have 3 values High, normal and, Low  */  
   "CallPriority":string,
      /**   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  A unique code that identifies the type of service call  */  
   "CallCode":string,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  */  
   "LaborComplete":boolean,
      /**  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  */  
   "MaterialComplete":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The estimated duration of the service call in days.  */  
   "Duration":number,
      /**  The Clientele call number that is related to this call.  */  
   "CLCallNum":string,
      /**  The help desk case that created this service call.  */  
   "HDCaseNum":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping country number  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PONum  */  
   "PONum":string,
      /**  Determines if the service call has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  Delimited list of available bill to customers.  */  
   "AvailBTCustList":string,
   "BaseCurrencyID":string,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   "BaseCurrSymbol":string,
      /**  Bill To Customer Name  */  
   "BTCustName":string,
      /**  Currency Switch  */  
   "CurrencySwitch":boolean,
   "CustAllowOTS":boolean,
      /**  Customer Contact Name  */  
   "CustConName":string,
   "CustEMailAddress":string,
      /**  Customer Fax Number  */  
   "CustFaxNum":string,
      /**  Indicates if the customer on credit hold.  */  
   "CustOnCreditHold":boolean,
      /**  Customer Phone Number  */  
   "CustPhoneNum":string,
   "DispActualTime":string,
   "DispEntryTime":string,
   "DispRequestTime":string,
   "DispSchedTime":string,
      /**  Total Actual Call Amount in customer's curreny  */  
   "DocTotActCall":number,
      /**  Total Actual Labor (Service) Amount in customer's currency  */  
   "DocTotActLabor":number,
      /**  Total Actual Material Amount in customer's currency  */  
   "DocTotActMaterial":number,
      /**  Total Actual Miscellaneous Amount in customer's currency  */  
   "DocTotActMisc":number,
      /**  Total Actual Subcontract Amount in  customer's currency  */  
   "DocTotActSubcontract":number,
      /**  Total Billable Call Amount in customer's currency  */  
   "DocTotBillCall":number,
      /**  Total Billable Labor (Service) Amount in customer's currency  */  
   "DocTotBillLabor":number,
      /**  Total Billable Material Amount in customer's currency  */  
   "DocTotBillMaterial":number,
      /**  Total Billable Miscellaneous Amount  */  
   "DocTotBillMisc":number,
      /**  Total Billable Subcontract Amount in customer's currency  */  
   "DocTotBillSubcontract":number,
      /**  Total Estimated Call Amount in customer's currency  */  
   "DocTotEstCall":number,
      /**  Total Estimated Labor (Service) Amount in customer's currency  */  
   "DocTotEstLabor":number,
      /**  Total Estimated Mateiral Amount in customer's currency  */  
   "DocTotEstMaterial":number,
      /**  Total Estimated Miscellaneous Amount in customer's currency  */  
   "DocTotEstMisc":number,
      /**  Total Estimated Subcontract Amount in customer's currency  */  
   "DocTotEstSubcontract":number,
      /**  Indicates if the Call Type Code field needs to be enabled.  */  
   "EnableCallType":boolean,
      /**  Indicates if the user can view customer tracker.  */  
   "EnableCustTracker":boolean,
      /**  Indicates if the user can access Issue Material screen.  */  
   "EnableIssueMtl":boolean,
      /**  Indicates if the user can access Issue Return screen.  */  
   "EnableIssueReturn":boolean,
      /**  Indicates if the user can create/update a service call job.  */  
   "EnableJobEntry":boolean,
      /**  Indicates if the user can access labor entry screen.  */  
   "EnableLaborEntry":boolean,
      /**  Indicates if the user can access the Miscellaneous Shipment screen.  */  
   "EnableMiscShip":boolean,
      /**  Indicates if the Reopen Service Call option should be enabled.  */  
   "EnableReopenCall":boolean,
      /**  Indicates if the user can maintain a service call header/line.  */  
   "EnableServiceCall":boolean,
   "Rpt1TotActCall":number,
   "Rpt1TotActLabor":number,
   "Rpt1TotActMaterial":number,
   "Rpt1TotActMisc":number,
   "Rpt1TotActSubcontract":number,
   "Rpt1TotBillCall":number,
   "Rpt1TotBillLabor":number,
   "Rpt1TotBillMaterial":number,
   "Rpt1TotBillMisc":number,
   "Rpt1TotBillSubcontract":number,
   "Rpt1TotEstCall":number,
   "Rpt1TotEstLabor":number,
   "Rpt1TotEstMaterial":number,
   "Rpt1TotEstMisc":number,
   "Rpt1TotEstSubcontract":number,
   "Rpt2TotActCall":number,
   "Rpt2TotActLabor":number,
   "Rpt2TotActMaterial":number,
   "Rpt2TotActMisc":number,
   "Rpt2TotActSubcontract":number,
   "Rpt2TotBillCall":number,
   "Rpt2TotBillLabor":number,
   "Rpt2TotBillMaterial":number,
   "Rpt2TotBillMisc":number,
   "Rpt2TotBillSubcontract":number,
   "Rpt2TotEstCall":number,
   "Rpt2TotEstLabor":number,
   "Rpt2TotEstMaterial":number,
   "Rpt2TotEstMisc":number,
   "Rpt2TotEstSubcontract":number,
   "Rpt3TotActCall":number,
   "Rpt3TotActLabor":number,
   "Rpt3TotActMaterial":number,
   "Rpt3TotActMisc":number,
   "Rpt3TotActSubcontract":number,
   "Rpt3TotBillCall":number,
   "Rpt3TotBillLabor":number,
   "Rpt3TotBillMaterial":number,
   "Rpt3TotBillMisc":number,
   "Rpt3TotBillSubcontract":number,
   "Rpt3TotEstCall":number,
   "Rpt3TotEstLabor":number,
   "Rpt3TotEstMaterial":number,
   "Rpt3TotEstMisc":number,
   "Rpt3TotEstSubcontract":number,
      /**  ShipTo Contact Name  */  
   "ShipConName":string,
   "ShipEMailAddress":string,
      /**  ShipTo Fax Number  */  
   "ShipFaxNum":string,
      /**  ShipTo Phone Number  */  
   "ShipPhoneNum":string,
   "ShipToAddrList":string,
   "SoldToAddrList":string,
      /**  Total Actual Call Amount  */  
   "TotActCall":number,
      /**  Total Actual Labor (Service) Amount  */  
   "TotActLabor":number,
      /**  Total Actual Material Amount  */  
   "TotActMaterial":number,
      /**  Total Actual Miscellaneous Amount  */  
   "TotActMisc":number,
      /**  Total Actual Subcontract Amount  */  
   "TotActSubcontract":number,
      /**  Total Billable Call Amount  */  
   "TotBillCall":number,
      /**  Total Billable Labor (Service) Amount  */  
   "TotBillLabor":number,
      /**  Total Billable Material Amount  */  
   "TotBillMaterial":number,
      /**  Total Billable Miscellaneous Amount  */  
   "TotBillMisc":number,
      /**  Total Billable Subcontract Amount  */  
   "TotBillSubcontract":number,
      /**  Total Estimated Call Amount  */  
   "TotEstCall":number,
      /**  Total Estimated Labor (Service) Amount  */  
   "TotEstLabor":number,
      /**  Total Estimated Material Amount  */  
   "TotEstMaterial":number,
      /**  Total Estimated Miscellaneous Amount  */  
   "TotEstMisc":number,
      /**  Total Estimated Subcontract Amount  */  
   "TotEstSubContract":number,
      /**  Exchange Rate Label  */  
   "XRateLabel":string,
      /**  Boolean for selection of FSCallhd  */  
   "Selected":boolean,
   "BitFlag":number,
   "BTCustNumInactive":boolean,
   "CallCodeCallDescription":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrRateGrpDescription":string,
   "CustNumInactive":boolean,
   "CustNumCustID":string,
   "CustNumAllowShipTo3":boolean,
   "CustNumBTName":string,
   "CustNumName":string,
   "HDCaseDescription":string,
   "OTSCountryNumEUMember":boolean,
   "OTSCountryNumDescription":string,
   "OTSCountryNumISOCode":string,
   "OTSTaxRegionCodeDescription":string,
   "PlantName":string,
   "ShipToCustID":string,
   "ShipToBTName":string,
   "ShipToName":string,
   "ShipToInactive":boolean,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FsTechRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The call number that the technician is assigned to.  */  
   "CallNum":number,
      /**  Part of the unique for this table.  */  
   "SeqNum":number,
      /**  Employee ID.  */  
   "EmpID":string,
      /**  the name of the employee assigned to the service call.  */  
   "Name":string,
      /**  Indicate that the call is open.  Not directly maintainable.  This is a mirror image of FSCallHd.OpenCall and is maintained by the WRITE trigger of FSCallHd.  */  
   "OpenCall":boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "CnvEmpID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Call Priority  */  
   "CallPriority":string,
   "CustID":string,
   "ShipName":string,
   "Address1":string,
   "City":string,
   "State":string,
   "RequestDate":string,
      /**  Request Time in HH:MM display format  */  
   "RequestTime":string,
   "SchedDate":string,
      /**  Scheduled Time in HH:MM display format  */  
   "SchedTime":string,
   "Duration":number,
      /**  Indicates if this record is to be displayed as open service call.  */  
   "ShowOpenCall":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipCallNum
   */  
export interface ActivateServiceCall_input{
      /**  The Service Call Number to close  */  
   ipCallNum:number,
}

export interface ActivateServiceCall_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
}

   /** Required : 
      @param ipCallNum
      @param ipEmpID
      @param ds
   */  
export interface AssignTechnician_input{
      /**  The Service Call Number  */  
   ipCallNum:number,
      /**  The Employee ID of the service technician  */  
   ipEmpID:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface AssignTechnician_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param billToCustNum
      @param ds
   */  
export interface ChangeBTCustID_input{
      /**  Proposed bill to custid  */  
   billToCustNum:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeBTCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipContractLine
      @param ds
   */  
export interface ChangeDtlContractLine_input{
      /**  The proposed service contract line number  */  
   ipContractLine:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlContractLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipContractNum
      @param ds
   */  
export interface ChangeDtlContractNum_input{
      /**  The proposed service contract number  */  
   ipContractNum:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlContractNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipDropShipPackLine
      @param ds
   */  
export interface ChangeDtlDropShipPackLine_input{
      /**  The proposed drop shipment pack line number  */  
   ipDropShipPackLine:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlDropShipPackLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipDropShipPackSlip
      @param ds
   */  
export interface ChangeDtlDropShipPackSlip_input{
      /**  The proposed drop shipment pack slip  */  
   ipDropShipPackSlip:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlDropShipPackSlip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipPackLine
      @param ds
   */  
export interface ChangeDtlPackLine_input{
      /**  The proposed pack line number  */  
   ipPackLine:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlPackLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface ChangeDtlPackNum_input{
      /**  The proposed pack ID  */  
   ipPackNum:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlPackNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
      @param uomCode
   */  
export interface ChangeDtlPartNum_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface ChangeDtlPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipRevNum
      @param ds
   */  
export interface ChangeDtlRevisionNum_input{
      /**  The proposed Revision Number  */  
   ipRevNum:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ipSerialNum
      @param ds
   */  
export interface ChangeDtlSerialNum_input{
      /**  The part number for the proposed serial number  */  
   ipPartNum:string,
      /**  The proposed serial number  */  
   ipSerialNum:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlSerialNum_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDtlXPartNum_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeDtlXPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param proposedProjectID
      @param ds
   */  
export interface ChangeFSCallDtProjectID_input{
      /**  The proposed project id  */  
   proposedProjectID:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeFSCallDtProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipPrcConNum
      @param ds
   */  
export interface ChangeHdrBillToContact_input{
      /**  The proposed Customer Contact  */  
   ipPrcConNum:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrBillToContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipCallCode
      @param ds
   */  
export interface ChangeHdrCallCode_input{
      /**  The proposed Service Call Type Code  */  
   ipCallCode:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrCallCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipCurrencyCode
      @param ds
   */  
export interface ChangeHdrCurrencyCode_input{
      /**  The proposed Currency Code  */  
   ipCurrencyCode:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipCustID
      @param ds
   */  
export interface ChangeHdrCustID_input{
      /**  The proposed Customer ID  */  
   ipCustID:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipHDCaseNum
      @param ds
   */  
export interface ChangeHdrHDCaseNum_input{
      /**  The proposed Case Number  */  
   ipHDCaseNum:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrHDCaseNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipRequestTime
      @param ds
   */  
export interface ChangeHdrRequestTime_input{
      /**  The proposed Request Time as integer (number of minutes past midnight)  */  
   ipRequestTime:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrRequestTime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipSchedTime
      @param ds
   */  
export interface ChangeHdrSchedTime_input{
      /**  The proposed Request Time as integer (number of seconds past midnight)  */  
   ipSchedTime:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrSchedTime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipShpConNum
      @param ds
   */  
export interface ChangeHdrShipToContact_input{
      /**  The proposed ShipTo Contact  */  
   ipShpConNum:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrShipToContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipShipToCustID
      @param ds
   */  
export interface ChangeHdrShipToCustID_input{
      /**  The proposed Ship To Customer ID  */  
   ipShipToCustID:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipShipToNum
      @param ds
   */  
export interface ChangeHdrShipToNum_input{
      /**  The proposed Customer ShipTo Number  */  
   ipShipToNum:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeHdrUseOTS_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeHdrUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param topics
      @param ds
   */  
export interface ChangeIssueTopics_input{
      /**  Proposed topics string id  */  
   topics:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeIssueTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param topics
      @param ds
   */  
export interface ChangeResTopics_input{
      /**  Proposed topics string id  */  
   topics:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface ChangeResTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CheckDtlSerialNum_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface CheckDtlSerialNum_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param vPartNum
      @param vContractNum
      @param vPackNum
   */  
export interface CheckPrePartInfo_input{
      /**  The input-output part number to validate and it gets returned  */  
   vPartNum:string,
      /**  The current Service Contract number associated with the call  */  
   vContractNum:number,
      /**  The current Pack id associated with the call  */  
   vPackNum:number,
}

export interface CheckPrePartInfo_output{
parameters : {
      /**  output parameters  */  
   vPartNum:string,
   vContractMsg:string,
   vWarrantyMsg:string,
   vSubPartMsg:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param ipRateGrpCode
      @param ds
   */  
export interface CheckRateGrpCode_input{
      /**  Currency Rate Group Code  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface CheckRateGrpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipCallNum
   */  
export interface CloseServiceCall_input{
      /**  The Service Call Number to close  */  
   ipCallNum:number,
}

export interface CloseServiceCall_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
}

   /** Required : 
      @param ipCallNum
      @param ipCallLine
      @param ds
   */  
export interface CreateServiceCallJob_input{
      /**  The Service Call Number to create the job for.  */  
   ipCallNum:number,
      /**  The Service Call Line Number to create the job for.  */  
   ipCallLine:number,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface CreateServiceCallJob_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param callNum
   */  
export interface DeleteByID_input{
   callNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FSCallCustTrkRow{
      /**  From FSCallhd.Company  */  
   Company:string,
      /**  From FSCallhd.CallNum  */  
   CallNum:number,
      /**  From FSCallhd.OpenCall  */  
   OpenCall:boolean,
      /**  From FSCallhd.CallPriority  */  
   CallPriority:string,
      /**  From FSCallhd.RequestDate  */  
   RequestDate:string,
      /**  From FSCallhd.SchedDate  */  
   SchedDate:string,
      /**  From FSCallhd.ActualDate  */  
   ActualDate:string,
      /**  From FSCallhd.ReadyToInvoice  */  
   ReadyToInvoice:boolean,
      /**  From FSCallhd.Invoiced  */  
   Invoiced:boolean,
      /**  From FSCallhd.VoidCall  */  
   VoidCall:boolean,
      /**  From FSCallhd.CallCode  */  
   CallCode:string,
      /**  From FSCallhd.CustNum  */  
   CustNum:number,
      /**  From FSCallhd.ShipToNum  */  
   ShipToNum:string,
      /**  From FSCallhd.ShpConNum  */  
   ShpConNum:number,
      /**  From FSCallDt.CallLine  */  
   CallLine:number,
      /**  From FSCallDt.PartNum  */  
   PartNum:string,
      /**  From FSCallDt.LineDesc  */  
   LineDesc:string,
      /**  From FSCallDt.CallQty  */  
   CallQty:number,
      /**  From FSCallDt.ContractCode  */  
   ContractCode:string,
      /**  from FSCallhd.CallCodeCallDescription  */  
   CallCodeCallDescription:string,
      /**  from FSCallDt.RevisionNum  */  
   RevisionNum:string,
      /**  from FSCallDt.XPartNum  */  
   XPartNum:string,
      /**  from FSCallDt.XRevisionNum  */  
   XRevisionNum:string,
      /**  The full customer's name.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
      /**  The customer ID.  */  
   CustID:string,
   IUM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSCallCustTrkTableset{
   FSCallCustTrk:Erp_Tablesets_FSCallCustTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FSCallDtAttchRow{
   Company:string,
   CallNum:number,
   CallLine:number,
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

export interface Erp_Tablesets_FSCallDtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   CallLine:number,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Serial number of the part being repaired.  */  
   SerialNumber:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  TotalCall Quantity for the line item.  */  
   CallQty:number,
      /**  Packing slip number that this Service call is linked with.  */  
   PackNum:number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   PackLine:number,
      /**  Unique code for the Warranty  */  
   WarrantyCode:string,
      /**  Contract Number if this item is under a contract  */  
   ContractNum:number,
      /**  This is the contract line the relates to the item on the service call.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  */  
   CallComment:string,
      /**  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Problem reason code from the reason master table. type problem.  */  
   ProbReasonCode:string,
      /**  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  total Labor Amount.  */  
   TotLabor:number,
      /**  total Labor Amount. In customers currency  */  
   DocTotLabor:number,
      /**  total Billable Labor Amount.  */  
   TotBillLabor:number,
      /**  total Billable Labor Amount. In Customers currency.  */  
   DocTotBillLabor:number,
      /**  total Material Amount.  */  
   TotMaterial:number,
      /**  total Material Amount. In Customers currency  */  
   DocTotMaterial:number,
      /**  total Billable Material Amount.  */  
   TotBillMaterial:number,
      /**  total Billable Material Amount. In Customers Currency.  */  
   DocTotBillMaterial:number,
      /**  total Misc. Amount.  */  
   TotMisc:number,
      /**  total Misc. Amount. In customers currency.  */  
   DocTotMisc:number,
      /**  total Billable Misc. Amount.  */  
   TotBillableMisc:number,
      /**  total Billable Misc. Amount. In customer's currency.  */  
   DocTotBillableMisc:number,
      /**  total Material Cost.  */  
   TotMaterialCost:number,
      /**  total Misc. Cost.  */  
   TotMiscCost:number,
      /**  Project ID of the Project table record that this FSCallDt record. Can be blank.  */  
   ProjectID:string,
      /**  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total Subcontract Amount.  */  
   TotSubCont:number,
      /**  total Subcontract Amount. In customers currency  */  
   DocTotSubCont:number,
      /**  total Billable Subcontract Amount.  */  
   TotBillSubCont:number,
      /**  total Billable Subcontract Amount. In Customers currency.  */  
   DocTotBillSubCont:number,
      /**  total Estimated Labor Amount.  */  
   TotEstLabor:number,
      /**  total estimated Labor Amount. In customers currency  */  
   DocTotEstLabor:number,
      /**  total Estimated Material Amount.  */  
   TotEstMaterial:number,
      /**  total Estimated Material Amount. In Customers currency  */  
   DocTotEstMaterial:number,
      /**  total Estimated Misc. Amount.  Future Use.  */  
   TotEstMisc:number,
      /**  total Est. Misc. Amount. In customers currency. Future use  */  
   DocTotEstMisc:number,
      /**  Total estimated Subcontract Amount.  */  
   TotEstSubCont:number,
      /**  total Estimated Subcontract Amount. In customers currency  */  
   DocTotEstSubCont:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotSubCont:number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   DropShipPackSlip:string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   DropShipPackLine:number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   VendorNum:number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   PurPoint:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  POLine  */  
   POLine:string,
      /**  IssueTopicID1  */  
   IssueTopicID1:string,
      /**  IssueTopicID2  */  
   IssueTopicID2:string,
      /**  IssueTopicID3  */  
   IssueTopicID3:string,
      /**  IssueTopicID4  */  
   IssueTopicID4:string,
      /**  IssueTopicID5  */  
   IssueTopicID5:string,
      /**  IssueTopicID6  */  
   IssueTopicID6:string,
      /**  IssueTopicID7  */  
   IssueTopicID7:string,
      /**  IssueTopicID8  */  
   IssueTopicID8:string,
      /**  IssueTopicID9  */  
   IssueTopicID9:string,
      /**  IssueTopicID10  */  
   IssueTopicID10:string,
      /**  IssueTopics  */  
   IssueTopics:string,
      /**  ResTopicID1  */  
   ResTopicID1:string,
      /**  ResTopicID2  */  
   ResTopicID2:string,
      /**  ResTopicID3  */  
   ResTopicID3:string,
      /**  ResTopicID4  */  
   ResTopicID4:string,
      /**  ResTopicID5  */  
   ResTopicID5:string,
      /**  ResTopicID6  */  
   ResTopicID6:string,
      /**  ResTopicID7  */  
   ResTopicID7:string,
      /**  ResTopicID8  */  
   ResTopicID8:string,
      /**  ResTopicID9  */  
   ResTopicID9:string,
      /**  ResTopicID10  */  
   ResTopicID10:string,
      /**  ResTopics  */  
   ResTopics:string,
      /**  PartDescription  */  
   PartDescription:string,
      /**  CommentText  */  
   CommentText:string,
      /**  Indicates the invoice processing has been done for this call line.  */  
   Invoiced:boolean,
      /**  Indicates that the call line can be invoiced.  */  
   ReadyToInvoice:boolean,
      /**  Currency.CurrSymbol of the "BASE" currency  */  
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DisplayContractType:string,
      /**  Currency.CurrSymbol of the customer's currency  */  
   DocCurrSymbol:string,
      /**  Total Billable Call Amount for the line in customer's currency  */  
   DocTotLineBillCall:number,
      /**  Total Actual Call Amount for the line in customer's currency  */  
   DocTotLineCall:number,
      /**  Total Estimated Call AMount for the line in customer's currency  */  
   DocTotLineEstCall:number,
      /**  Indicates if Contract entry should be enabled.  */  
   EnableContract:boolean,
      /**  Indicates if Warranty entry should be enabled.  */  
   EnableWarranty:boolean,
      /**  Unit of Measure Description  */  
   IUMDesc:string,
      /**  Reson Code Description  */  
   ProbReasonDesc:string,
   Rpt1TotLineBillCall:number,
   Rpt1TotLineCall:number,
   Rpt1TotLineEstCall:number,
   Rpt2TotLineBillCall:number,
   Rpt2TotLineCall:number,
   Rpt2TotLineEstCall:number,
   Rpt3TotLineBillCall:number,
   Rpt3TotLineCall:number,
   Rpt3TotLineEstCall:number,
      /**  Total Billable Call Amount for the line  */  
   TotLineBillCall:number,
      /**  Total Actual Call Amount for the line  */  
   TotLineCall:number,
      /**  Total Estimated Call Amount for the line  */  
   TotLineEstCall:number,
   JobClosed:boolean,
   BitFlag:number,
   ContractCodeContractDescription:string,
   ContractLineLineDesc:string,
   DropShipDtlLineDesc:string,
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
   JobNumPartDescription:string,
   PackLineLineDesc:string,
   PackNumShipStatus:string,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
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
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSCallhdAttchRow{
   Company:string,
   CallNum:number,
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

export interface Erp_Tablesets_FSCallhdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  defaults to TODAY  */  
   EntryDate:string,
      /**  Time in second past midnight  */  
   EntryTime:number,
      /**  The date that the service is requested for.  */  
   RequestDate:string,
      /**  Time in second past midnight  */  
   RequestTime:number,
      /**  The date that the service is scheduled for.  */  
   SchedDate:string,
      /**  Time in second past midnight  */  
   SchedTime:number,
      /**  The date that the service was performed on.  */  
   ActualDate:string,
      /**  Time in second past midnight  */  
   ActualTime:number,
      /**  Contains comments about the overall Call. These will be printed on the Service Call.  */  
   CallComment:string,
      /**  Contains comments about the overall Call. These will be printed on the Service Call invoice.  */  
   InvoiceComment:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Indicate that the call is open.  */  
   OpenCall:boolean,
      /**  Indicates that the call is closed and can be invoiced.  */  
   ReadyToInvoice:boolean,
      /**  Indicated the invoice processing has been done for this call.  */  
   Invoiced:boolean,
      /**  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  */  
   VoidCall:boolean,
      /**  Can have 3 values High, normal and, Low  */  
   CallPriority:string,
      /**   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  A unique code that identifies the type of service call  */  
   CallCode:string,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  */  
   LaborComplete:boolean,
      /**  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  */  
   MaterialComplete:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The estimated duration of the service call in days.  */  
   Duration:number,
      /**  The Clientele call number that is related to this call.  */  
   CLCallNum:string,
      /**  The help desk case that created this service call.  */  
   HDCaseNum:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping country number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Customer Contact Name  */  
   CustConName:string,
      /**  Customer Phone Number  */  
   CustPhoneNum:string,
      /**  Customer Fax Number  */  
   CustFaxNum:string,
      /**  ShipTo Contact Name  */  
   ShipConName:string,
      /**  ShipTo Phone Number  */  
   ShipPhoneNum:string,
      /**  ShipTo Fax Number  */  
   ShipFaxNum:string,
      /**  Currency Switch  */  
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   BaseCurrSymbol:string,
      /**  Exchange Rate Label  */  
   XRateLabel:string,
      /**  Total Estimated Material Amount  */  
   TotEstMaterial:number,
      /**  Total Estimated Mateiral Amount in customer's currency  */  
   DocTotEstMaterial:number,
      /**  Total Estimated Subcontract Amount  */  
   TotEstSubContract:number,
      /**  Total Estimated Subcontract Amount in customer's currency  */  
   DocTotEstSubcontract:number,
      /**  Total Estimated Miscellaneous Amount  */  
   TotEstMisc:number,
      /**  Total Estimated Miscellaneous Amount in customer's currency  */  
   DocTotEstMisc:number,
      /**  Total Estimated Call Amount  */  
   TotEstCall:number,
      /**  Total Estimated Call Amount in customer's currency  */  
   DocTotEstCall:number,
      /**  Total Actual Material Amount  */  
   TotActMaterial:number,
      /**  Total Actual Material Amount in customer's currency  */  
   DocTotActMaterial:number,
      /**  Total Actual Subcontract Amount  */  
   TotActSubcontract:number,
      /**  Total Actual Subcontract Amount in  customer's currency  */  
   DocTotActSubcontract:number,
      /**  Total Actual Miscellaneous Amount  */  
   TotActMisc:number,
      /**  Total Actual Miscellaneous Amount in customer's currency  */  
   DocTotActMisc:number,
      /**  Total Actual Call Amount  */  
   TotActCall:number,
      /**  Total Actual Call Amount in customer's curreny  */  
   DocTotActCall:number,
      /**  Total Billable Material Amount  */  
   TotBillMaterial:number,
      /**  Total Billable Material Amount in customer's currency  */  
   DocTotBillMaterial:number,
      /**  Total Billable Subcontract Amount  */  
   TotBillSubcontract:number,
      /**  Total Billable Subcontract Amount in customer's currency  */  
   DocTotBillSubcontract:number,
      /**  Total Billable Miscellaneous Amount  */  
   TotBillMisc:number,
      /**  Total Billable Miscellaneous Amount  */  
   DocTotBillMisc:number,
      /**  Total Billable Call Amount  */  
   TotBillCall:number,
      /**  Total Billable Call Amount in customer's currency  */  
   DocTotBillCall:number,
   DispEntryTime:string,
   DispRequestTime:string,
   DispSchedTime:string,
   DispActualTime:string,
      /**  Total Estimated Labor (Service) Amount  */  
   TotEstLabor:number,
      /**  Total Estimated Labor (Service) Amount in customer's currency  */  
   DocTotEstLabor:number,
      /**  Total Actual Labor (Service) Amount  */  
   TotActLabor:number,
      /**  Total Actual Labor (Service) Amount in customer's currency  */  
   DocTotActLabor:number,
      /**  Total Billable Labor (Service) Amount  */  
   TotBillLabor:number,
      /**  Total Billable Labor (Service) Amount in customer's currency  */  
   DocTotBillLabor:number,
      /**  Indicates if the Call Type Code field needs to be enabled.  */  
   EnableCallType:boolean,
      /**  Indicates if the user can maintain a service call header/line.  */  
   EnableServiceCall:boolean,
      /**  Indicates if the user can view customer tracker.  */  
   EnableCustTracker:boolean,
      /**  Indicates if the user can create/update a service call job.  */  
   EnableJobEntry:boolean,
      /**  Indicates if the user can access labor entry screen.  */  
   EnableLaborEntry:boolean,
      /**  Indicates if the user can access the Miscellaneous Shipment screen.  */  
   EnableMiscShip:boolean,
      /**  Indicates if the user can access Issue Material screen.  */  
   EnableIssueMtl:boolean,
      /**  Indicates if the user can access Issue Return screen.  */  
   EnableIssueReturn:boolean,
      /**  Indicates if the Reopen Service Call option should be enabled.  */  
   EnableReopenCall:boolean,
      /**  Indicates if the customer on credit hold.  */  
   CustOnCreditHold:boolean,
   ShipEMailAddress:string,
   CustEMailAddress:string,
   Rpt1TotActCall:number,
   Rpt2TotActCall:number,
   Rpt3TotActCall:number,
   Rpt1TotActLabor:number,
   Rpt2TotActLabor:number,
   Rpt3TotActLabor:number,
   Rpt1TotActMaterial:number,
   Rpt2TotActMaterial:number,
   Rpt3TotActMaterial:number,
   Rpt1TotActMisc:number,
   Rpt2TotActMisc:number,
   Rpt3TotActMisc:number,
   Rpt1TotActSubcontract:number,
   Rpt2TotActSubcontract:number,
   Rpt3TotActSubcontract:number,
   Rpt1TotBillCall:number,
   Rpt2TotBillCall:number,
   Rpt3TotBillCall:number,
   Rpt1TotBillLabor:number,
   Rpt2TotBillLabor:number,
   Rpt3TotBillLabor:number,
   Rpt1TotBillMaterial:number,
   Rpt2TotBillMaterial:number,
   Rpt3TotBillMaterial:number,
   Rpt1TotBillMisc:number,
   Rpt2TotBillMisc:number,
   Rpt3TotBillMisc:number,
   Rpt1TotBillSubcontract:number,
   Rpt2TotBillSubcontract:number,
   Rpt3TotBillSubcontract:number,
   Rpt1TotEstCall:number,
   Rpt2TotEstCall:number,
   Rpt3TotEstCall:number,
   Rpt1TotEstLabor:number,
   Rpt2TotEstLabor:number,
   Rpt3TotEstLabor:number,
   Rpt1TotEstMaterial:number,
   Rpt2TotEstMaterial:number,
   Rpt3TotEstMaterial:number,
   Rpt1TotEstMisc:number,
   Rpt2TotEstMisc:number,
   Rpt3TotEstMisc:number,
   Rpt1TotEstSubcontract:number,
   Rpt2TotEstSubcontract:number,
   Rpt3TotEstSubcontract:number,
   CustAllowOTS:boolean,
   ShipToAddrList:string,
   SoldToAddrList:string,
      /**  Bill To Customer Name  */  
   BTCustName:string,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
   BaseCurrencyID:string,
      /**  Description of the Call Type Code.  */  
   CallCodeCallDescription:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**  Description  */  
   CurrRateGrpDescription:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  */  
   CustNumAllowShipTo3:boolean,
      /**  Country name  */  
   OTSCountryNumDescription:string,
      /**  Full description for the Tax Region.  */  
   OTSTaxRegionCodeDescription:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  The full name of the customer.  */  
   ShipToName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustID:string,
      /**  Full description for the Sales Tax category.  */  
   TaxCatIDDescription:string,
      /**  Boolean for selection of FSCallhdList  */  
   Selected:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSCallhdListTableset{
   FSCallhdList:Erp_Tablesets_FSCallhdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FSCallhdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  defaults to TODAY  */  
   EntryDate:string,
      /**  Time in second past midnight  */  
   EntryTime:number,
      /**  The date that the service is requested for.  */  
   RequestDate:string,
      /**  Time in second past midnight  */  
   RequestTime:number,
      /**  The date that the service is scheduled for.  */  
   SchedDate:string,
      /**  Time in second past midnight  */  
   SchedTime:number,
      /**  The date that the service was performed on.  */  
   ActualDate:string,
      /**  Time in second past midnight  */  
   ActualTime:number,
      /**  Contains comments about the overall Call. These will be printed on the Service Call.  */  
   CallComment:string,
      /**  Contains comments about the overall Call. These will be printed on the Service Call invoice.  */  
   InvoiceComment:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Indicate that the call is open.  */  
   OpenCall:boolean,
      /**  Indicates that the call is closed and can be invoiced.  */  
   ReadyToInvoice:boolean,
      /**  Indicated the invoice processing has been done for this call.  */  
   Invoiced:boolean,
      /**  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  */  
   VoidCall:boolean,
      /**  Can have 3 values High, normal and, Low  */  
   CallPriority:string,
      /**   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  A unique code that identifies the type of service call  */  
   CallCode:string,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  */  
   LaborComplete:boolean,
      /**  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  */  
   MaterialComplete:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The estimated duration of the service call in days.  */  
   Duration:number,
      /**  The Clientele call number that is related to this call.  */  
   CLCallNum:string,
      /**  The help desk case that created this service call.  */  
   HDCaseNum:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping country number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PONum  */  
   PONum:string,
      /**  Determines if the service call has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
   BaseCurrencyID:string,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   BaseCurrSymbol:string,
      /**  Bill To Customer Name  */  
   BTCustName:string,
      /**  Currency Switch  */  
   CurrencySwitch:boolean,
   CustAllowOTS:boolean,
      /**  Customer Contact Name  */  
   CustConName:string,
   CustEMailAddress:string,
      /**  Customer Fax Number  */  
   CustFaxNum:string,
      /**  Indicates if the customer on credit hold.  */  
   CustOnCreditHold:boolean,
      /**  Customer Phone Number  */  
   CustPhoneNum:string,
   DispActualTime:string,
   DispEntryTime:string,
   DispRequestTime:string,
   DispSchedTime:string,
      /**  Total Actual Call Amount in customer's curreny  */  
   DocTotActCall:number,
      /**  Total Actual Labor (Service) Amount in customer's currency  */  
   DocTotActLabor:number,
      /**  Total Actual Material Amount in customer's currency  */  
   DocTotActMaterial:number,
      /**  Total Actual Miscellaneous Amount in customer's currency  */  
   DocTotActMisc:number,
      /**  Total Actual Subcontract Amount in  customer's currency  */  
   DocTotActSubcontract:number,
      /**  Total Billable Call Amount in customer's currency  */  
   DocTotBillCall:number,
      /**  Total Billable Labor (Service) Amount in customer's currency  */  
   DocTotBillLabor:number,
      /**  Total Billable Material Amount in customer's currency  */  
   DocTotBillMaterial:number,
      /**  Total Billable Miscellaneous Amount  */  
   DocTotBillMisc:number,
      /**  Total Billable Subcontract Amount in customer's currency  */  
   DocTotBillSubcontract:number,
      /**  Total Estimated Call Amount in customer's currency  */  
   DocTotEstCall:number,
      /**  Total Estimated Labor (Service) Amount in customer's currency  */  
   DocTotEstLabor:number,
      /**  Total Estimated Mateiral Amount in customer's currency  */  
   DocTotEstMaterial:number,
      /**  Total Estimated Miscellaneous Amount in customer's currency  */  
   DocTotEstMisc:number,
      /**  Total Estimated Subcontract Amount in customer's currency  */  
   DocTotEstSubcontract:number,
      /**  Indicates if the Call Type Code field needs to be enabled.  */  
   EnableCallType:boolean,
      /**  Indicates if the user can view customer tracker.  */  
   EnableCustTracker:boolean,
      /**  Indicates if the user can access Issue Material screen.  */  
   EnableIssueMtl:boolean,
      /**  Indicates if the user can access Issue Return screen.  */  
   EnableIssueReturn:boolean,
      /**  Indicates if the user can create/update a service call job.  */  
   EnableJobEntry:boolean,
      /**  Indicates if the user can access labor entry screen.  */  
   EnableLaborEntry:boolean,
      /**  Indicates if the user can access the Miscellaneous Shipment screen.  */  
   EnableMiscShip:boolean,
      /**  Indicates if the Reopen Service Call option should be enabled.  */  
   EnableReopenCall:boolean,
      /**  Indicates if the user can maintain a service call header/line.  */  
   EnableServiceCall:boolean,
   Rpt1TotActCall:number,
   Rpt1TotActLabor:number,
   Rpt1TotActMaterial:number,
   Rpt1TotActMisc:number,
   Rpt1TotActSubcontract:number,
   Rpt1TotBillCall:number,
   Rpt1TotBillLabor:number,
   Rpt1TotBillMaterial:number,
   Rpt1TotBillMisc:number,
   Rpt1TotBillSubcontract:number,
   Rpt1TotEstCall:number,
   Rpt1TotEstLabor:number,
   Rpt1TotEstMaterial:number,
   Rpt1TotEstMisc:number,
   Rpt1TotEstSubcontract:number,
   Rpt2TotActCall:number,
   Rpt2TotActLabor:number,
   Rpt2TotActMaterial:number,
   Rpt2TotActMisc:number,
   Rpt2TotActSubcontract:number,
   Rpt2TotBillCall:number,
   Rpt2TotBillLabor:number,
   Rpt2TotBillMaterial:number,
   Rpt2TotBillMisc:number,
   Rpt2TotBillSubcontract:number,
   Rpt2TotEstCall:number,
   Rpt2TotEstLabor:number,
   Rpt2TotEstMaterial:number,
   Rpt2TotEstMisc:number,
   Rpt2TotEstSubcontract:number,
   Rpt3TotActCall:number,
   Rpt3TotActLabor:number,
   Rpt3TotActMaterial:number,
   Rpt3TotActMisc:number,
   Rpt3TotActSubcontract:number,
   Rpt3TotBillCall:number,
   Rpt3TotBillLabor:number,
   Rpt3TotBillMaterial:number,
   Rpt3TotBillMisc:number,
   Rpt3TotBillSubcontract:number,
   Rpt3TotEstCall:number,
   Rpt3TotEstLabor:number,
   Rpt3TotEstMaterial:number,
   Rpt3TotEstMisc:number,
   Rpt3TotEstSubcontract:number,
      /**  ShipTo Contact Name  */  
   ShipConName:string,
   ShipEMailAddress:string,
      /**  ShipTo Fax Number  */  
   ShipFaxNum:string,
      /**  ShipTo Phone Number  */  
   ShipPhoneNum:string,
   ShipToAddrList:string,
   SoldToAddrList:string,
      /**  Total Actual Call Amount  */  
   TotActCall:number,
      /**  Total Actual Labor (Service) Amount  */  
   TotActLabor:number,
      /**  Total Actual Material Amount  */  
   TotActMaterial:number,
      /**  Total Actual Miscellaneous Amount  */  
   TotActMisc:number,
      /**  Total Actual Subcontract Amount  */  
   TotActSubcontract:number,
      /**  Total Billable Call Amount  */  
   TotBillCall:number,
      /**  Total Billable Labor (Service) Amount  */  
   TotBillLabor:number,
      /**  Total Billable Material Amount  */  
   TotBillMaterial:number,
      /**  Total Billable Miscellaneous Amount  */  
   TotBillMisc:number,
      /**  Total Billable Subcontract Amount  */  
   TotBillSubcontract:number,
      /**  Total Estimated Call Amount  */  
   TotEstCall:number,
      /**  Total Estimated Labor (Service) Amount  */  
   TotEstLabor:number,
      /**  Total Estimated Material Amount  */  
   TotEstMaterial:number,
      /**  Total Estimated Miscellaneous Amount  */  
   TotEstMisc:number,
      /**  Total Estimated Subcontract Amount  */  
   TotEstSubContract:number,
      /**  Exchange Rate Label  */  
   XRateLabel:string,
      /**  Boolean for selection of FSCallhd  */  
   Selected:boolean,
   BitFlag:number,
   BTCustNumInactive:boolean,
   CallCodeCallDescription:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrRateGrpDescription:string,
   CustNumInactive:boolean,
   CustNumCustID:string,
   CustNumAllowShipTo3:boolean,
   CustNumBTName:string,
   CustNumName:string,
   HDCaseDescription:string,
   OTSCountryNumEUMember:boolean,
   OTSCountryNumDescription:string,
   OTSCountryNumISOCode:string,
   OTSTaxRegionCodeDescription:string,
   PlantName:string,
   ShipToCustID:string,
   ShipToBTName:string,
   ShipToName:string,
   ShipToInactive:boolean,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FsTechRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The call number that the technician is assigned to.  */  
   CallNum:number,
      /**  Part of the unique for this table.  */  
   SeqNum:number,
      /**  Employee ID.  */  
   EmpID:string,
      /**  the name of the employee assigned to the service call.  */  
   Name:string,
      /**  Indicate that the call is open.  Not directly maintainable.  This is a mirror image of FSCallHd.OpenCall and is maintained by the WRITE trigger of FSCallHd.  */  
   OpenCall:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   CnvEmpID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Call Priority  */  
   CallPriority:string,
   CustID:string,
   ShipName:string,
   Address1:string,
   City:string,
   State:string,
   RequestDate:string,
      /**  Request Time in HH:MM display format  */  
   RequestTime:string,
   SchedDate:string,
      /**  Scheduled Time in HH:MM display format  */  
   SchedTime:string,
   Duration:number,
      /**  Indicates if this record is to be displayed as open service call.  */  
   ShowOpenCall:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ServiceCallCenterTableset{
   FSCallhd:Erp_Tablesets_FSCallhdRow[],
   FSCallhdAttch:Erp_Tablesets_FSCallhdAttchRow[],
   FSCallDt:Erp_Tablesets_FSCallDtRow[],
   FSCallDtAttch:Erp_Tablesets_FSCallDtAttchRow[],
   FsTech:Erp_Tablesets_FsTechRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtServiceCallCenterTableset{
   FSCallhd:Erp_Tablesets_FSCallhdRow[],
   FSCallhdAttch:Erp_Tablesets_FSCallhdAttchRow[],
   FSCallDt:Erp_Tablesets_FSCallDtRow[],
   FSCallDtAttch:Erp_Tablesets_FSCallDtAttchRow[],
   FsTech:Erp_Tablesets_FsTechRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ExpirationDate
      @param EffectiveDAte
      @param Duration
      @param modifier
   */  
export interface ExpireDate_input{
   ExpirationDate:string,
   EffectiveDAte:string,
   Duration:number,
   modifier:string,
}

export interface ExpireDate_output{
   returnObj:string,
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
      /**  PartNum  */  
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param callNum
   */  
export interface GetByID_input{
   callNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name  */  
   tableName:string,
      /**  The field name.  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param custNums
      @param callCodes
   */  
export interface GetFSCallhdReadyForInvoice_input{
   custNums:string,
   callCodes:string,
}

export interface GetFSCallhdReadyForInvoice_output{
   returnObj:Erp_Tablesets_FSCallhdListTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListRemoveInvoiced_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetListRemoveInvoiced_output{
   returnObj:Erp_Tablesets_FSCallhdListTableset[],
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
   returnObj:Erp_Tablesets_FSCallhdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param callNum
      @param callLine
   */  
export interface GetNewFSCallDtAttch_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
   callNum:number,
   callLine:number,
}

export interface GetNewFSCallDtAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
      @param callNum
   */  
export interface GetNewFSCallDt_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
   callNum:number,
}

export interface GetNewFSCallDt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
      @param ipCustNum
      @param ipShipToNum
   */  
export interface GetNewFSCallHd1_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
      /**  The Customer Number for this Service Call  */  
   ipCustNum:number,
      /**  The Customer ShipTo Number for this Service Call  */  
   ipShipToNum:string,
}

export interface GetNewFSCallHd1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
      @param callNum
   */  
export interface GetNewFSCallhdAttch_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
   callNum:number,
}

export interface GetNewFSCallhdAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFSCallhd_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface GetNewFSCallhd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
      @param callNum
   */  
export interface GetNewFsTech_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
   callNum:number,
}

export interface GetNewFsTech_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
      /**  Row Type  */  
   ipRowType:string,
      /**  Row ID  */  
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param partNum
      @param custNum
      @param uomCode
      @param SysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  Customer number  */  
   custNum:number,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param whereClauseFSCallhd
      @param whereClauseFSCallhdAttch
      @param whereClauseFSCallDt
      @param whereClauseFSCallDtAttch
      @param whereClauseFsTech
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for FSCallhd table.  */  
   whereClauseFSCallhd:string,
      /**  Whereclause for FSCallhdAttch table.  */  
   whereClauseFSCallhdAttch:string,
      /**  Whereclause for FSCallDt table.  */  
   whereClauseFSCallDt:string,
      /**  Whereclause for FSCallDtAttch table.  */  
   whereClauseFSCallDtAttch:string,
      /**  Whereclause for FsTech table.  */  
   whereClauseFsTech:string,
      /**  Contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_FSCallCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseFSCallhd
      @param whereClauseFSCallhdAttch
      @param whereClauseFSCallDt
      @param whereClauseFSCallDtAttch
      @param whereClauseFsTech
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for FSCallhd table.  */  
   whereClauseFSCallhd:string,
      /**  Whereclause for FSCallhdAttch table.  */  
   whereClauseFSCallhdAttch:string,
      /**  Whereclause for FSCallDt table.  */  
   whereClauseFSCallDt:string,
      /**  Whereclause for FSCallDtAttch table.  */  
   whereClauseFSCallDtAttch:string,
      /**  Whereclause for FsTech table.  */  
   whereClauseFsTech:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_FSCallCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseFSCallhd
      @param whereClauseFSCallhdAttch
      @param whereClauseFSCallDt
      @param whereClauseFSCallDtAttch
      @param whereClauseFsTech
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFSCallhd:string,
   whereClauseFSCallhdAttch:string,
   whereClauseFSCallDt:string,
   whereClauseFSCallDtAttch:string,
   whereClauseFsTech:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param custNum
      @param partNum
   */  
export interface GetXPartByPartNum_input{
      /**  Customer Number  */  
   custNum:number,
      /**  Part Number  */  
   partNum:string,
}

export interface GetXPartByPartNum_output{
   returnObj:string,
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
      @param ipCallNum
   */  
export interface PreCloseServiceCall_input{
      /**  The Service Call Number to close  */  
   ipCallNum:number,
}

export interface PreCloseServiceCall_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipCallNum
   */  
export interface ReopenServiceCall_input{
      /**  The Service Call Number to close  */  
   ipCallNum:number,
}

export interface ReopenServiceCall_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtServiceCallCenterTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtServiceCallCenterTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
}
}

   /** Required : 
      @param ds
      @param manualValidation
      @param hmrcFraudPrevHeader
   */  
export interface ValidateOTSTaxID_input{
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
      /**  bool  */  
   manualValidation:boolean,
      /**  string  */  
   hmrcFraudPrevHeader:string,
}

export interface ValidateOTSTaxID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceCallCenterTableset[],
   opMessage:string,
}
}

   /** Required : 
      @param ipCallNum
   */  
export interface VoidServiceCall_input{
      /**  The Service Call Number to close  */  
   ipCallNum:number,
}

export interface VoidServiceCall_output{
   returnObj:Erp_Tablesets_ServiceCallCenterTableset[],
}

