import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CCScheduleSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/$metadata", {
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
   Description: Get CCSchedules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCSchedules
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCWhsCtrlRow
   */  
export function get_CCSchedules(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCWhsCtrlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCWhsCtrlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCSchedules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules", {
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
   Summary: Calls GetByID to retrieve the CCSchedule item
   Description: Calls GetByID to retrieve the CCSchedule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCWhsCtrlRow
   */  
export function get_CCSchedules_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCWhsCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCWhsCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCSchedule for the service
   Description: Calls UpdateExt to update CCSchedule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCWhsCtrlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCSchedules_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + ")", {
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
   Summary: Call UpdateExt to delete CCSchedule item
   Description: Call UpdateExt to delete CCSchedule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCSchedules_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + ")", {
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
   Description: Get CCHdrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCHdrs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrRow
   */  
export function get_CCSchedules_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CCHdrs(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + ")/CCHdrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CCHdr item
   Description: Calls GetByID to retrieve the CCHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCHdr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   */  
export function get_CCSchedules_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + ")/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CCWhsABCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCWhsABCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCWhsABCRow
   */  
export function get_CCSchedules_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CCWhsABCs(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + ")/CCWhsABCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CCWhsABC item
   Description: Calls GetByID to retrieve the CCWhsABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCWhsABC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCWhsABCRow
   */  
export function get_CCSchedules_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CCWhsABCs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_ABCCode(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, ABCCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCWhsABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCSchedules(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + ")/CCWhsABCs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + ABCCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCWhsABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CCHdrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCHdrs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrRow
   */  
export function get_CCHdrs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCHdrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCHdrs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs", {
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
   Summary: Calls GetByID to retrieve the CCHdr item
   Description: Calls GetByID to retrieve the CCHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCHdr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   */  
export function get_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCHdr for the service
   Description: Calls UpdateExt to update CCHdr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCHdr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
   Summary: Call UpdateExt to delete CCHdr item
   Description: Call UpdateExt to delete CCHdr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCHdr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
   Description: Get CCDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlRow
   */  
export function get_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CCDtl item
   Description: Calls GetByID to retrieve the CCDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   */  
export function get_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CCPCIDs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CCPCIDs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDRow
   */  
export function get_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CCPCID item
   Description: Calls GetByID to retrieve the CCPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCID1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   */  
export function get_CCHdrs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCHdrs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CCDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlRow
   */  
export function get_CCDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCDtls", {
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
   Summary: Calls GetByID to retrieve the CCDtl item
   Description: Calls GetByID to retrieve the CCDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   */  
export function get_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCDtl for the service
   Description: Calls UpdateExt to update CCDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
   Summary: Call UpdateExt to delete CCDtl item
   Description: Call UpdateExt to delete CCDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCDtls_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCDtls(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
   Description: Get CCPCIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCPCIDs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCPCIDRow
   */  
export function get_CCPCIDs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCPCIDs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCPCIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCPCIDs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCPCIDs", {
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
   Summary: Calls GetByID to retrieve the CCPCID item
   Description: Calls GetByID to retrieve the CCPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   */  
export function get_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCPCIDRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCPCIDRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCPCID for the service
   Description: Calls UpdateExt to update CCPCID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCPCIDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
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
   Summary: Call UpdateExt to delete CCPCID item
   Description: Call UpdateExt to delete CCPCID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCPCID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCPCIDs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PCID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PCID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCPCIDs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PCID + ")", {
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
   Description: Get CCWhsABCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCWhsABCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCWhsABCRow
   */  
export function get_CCWhsABCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCWhsABCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCWhsABCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCWhsABCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCWhsABCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCWhsABCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCWhsABCs", {
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
   Summary: Calls GetByID to retrieve the CCWhsABC item
   Description: Calls GetByID to retrieve the CCWhsABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCWhsABC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCWhsABCRow
   */  
export function get_CCWhsABCs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_ABCCode(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, ABCCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCWhsABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCWhsABCs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + ABCCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCWhsABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCWhsABC for the service
   Description: Calls UpdateExt to update CCWhsABC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCWhsABC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCWhsABCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCWhsABCs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_ABCCode(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, ABCCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCWhsABCs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + ABCCode + ")", {
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
   Summary: Call UpdateExt to delete CCWhsABC item
   Description: Call UpdateExt to delete CCWhsABC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCWhsABC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCWhsABCs_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_ABCCode(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, ABCCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/CCWhsABCs(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + ABCCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCWhsCtrlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsCtrlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsCtrlListRow)
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
export function get_GetRows(whereClauseCCWhsCtrl:string, whereClauseCCHdr:string, whereClauseCCDtl:string, whereClauseCCPCID:string, whereClauseCCWhsABC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCCWhsCtrl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCWhsCtrl=" + whereClauseCCWhsCtrl
   }
   if(typeof whereClauseCCHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCHdr=" + whereClauseCCHdr
   }
   if(typeof whereClauseCCDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCDtl=" + whereClauseCCDtl
   }
   if(typeof whereClauseCCPCID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCPCID=" + whereClauseCCPCID
   }
   if(typeof whereClauseCCWhsABC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCWhsABC=" + whereClauseCCWhsABC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetRows" + params, {
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
   Required: True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, warehouseCode:string, ccYear:string, ccMonth:string, fullPhysical:string, epicorHeaders?:Headers){
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
   if(typeof warehouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warehouseCode=" + warehouseCode
   }
   if(typeof ccYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ccYear=" + ccYear
   }
   if(typeof ccMonth!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ccMonth=" + ccMonth
   }
   if(typeof fullPhysical!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fullPhysical=" + fullPhysical
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetList" + params, {
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
   Summary: Invoke method GetCCDtlUOMSum
   Description: Purpose:
Parameters:  none
Notes:
<param name="vWarehouseCode">Warehouse </param><param name="vCCYear"> Year </param><param name="vCCMonth">Month </param><param name="vFullPhysical">Full Physical </param><param name="vCycleSeq"> cycle Seq </param><param name="vPartNum"> Part Number </param><param name="vAttributeSetID">Attribute Set ID </param><returns>CCDtlUOM data set</returns>
   OperationID: GetCCDtlUOMSum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCCDtlUOMSum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCCDtlUOMSum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCCDtlUOMSum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetCCDtlUOMSum", {
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
   Summary: Invoke method OnChangeOfCCMonth
   Description: This method validates CCProdCal
   OperationID: OnChangeOfCCMonth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfCCMonth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCCMonth_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfCCMonth(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/OnChangeOfCCMonth", {
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
   Summary: Invoke method OnChangeOfCCProdCal
   Description: This method validates CCProdCal
   OperationID: OnChangeOfCCProdCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfCCProdCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCCProdCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfCCProdCal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/OnChangeOfCCProdCal", {
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
   Summary: Invoke method OnChangeOfCCYear
   Description: This method validates CCProdCal
   OperationID: OnChangeOfCCYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfCCYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCCYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfCCYear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/OnChangeOfCCYear", {
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
   Summary: Invoke method OnChangeWhseCode
   Description: Purpose:
Parameters:  none
Notes:
///<param name="ipWhseCode">ipWhseCode</param>
/// <param name="ds">CCSchedule dataset</param>
   OperationID: OnChangeWhseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/OnChangeWhseCode", {
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
   Summary: Invoke method SelectParts
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ds">CCSchedule dataset</param>
   OperationID: SelectParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/SelectParts", {
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
   Summary: Invoke method UndoPartSelection
   Description: Purpose:  Reverses the database updates made by SelectParts for a particular cycle schedule (CCWhsCtrl).
Parameters:  none
Notes:
/// <param name="ds">CCSchedule dataset</param>
   OperationID: UndoPartSelection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoPartSelection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoPartSelection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UndoPartSelection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/UndoPartSelection", {
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
   Summary: Invoke method DeleteCycleSequences
   Description: Purpose:  Deletes all cycles (CCHdr, CCDtl) with CycleStatus = 0 for a given cycle count schedule (CCWhsCtrl)
Parameters:  none
Notes:
/// <param name="ds">CCSchedule dataset</param>
   OperationID: DeleteCycleSequences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCycleSequences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCycleSequences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCycleSequences(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/DeleteCycleSequences", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetCodeDescList", {
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
   Summary: Invoke method GetNewCCWhsCtrl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCWhsCtrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCWhsCtrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCWhsCtrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCWhsCtrl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetNewCCWhsCtrl", {
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
   Summary: Invoke method GetNewCCHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCHdr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetNewCCHdr", {
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
   Summary: Invoke method GetNewCCDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetNewCCDtl", {
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
   Summary: Invoke method GetNewCCPCID
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetNewCCPCID", {
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
   Summary: Invoke method GetNewCCWhsABC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCWhsABC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCWhsABC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCWhsABC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCWhsABC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetNewCCWhsABC", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCScheduleSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCHdrRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCPCIDRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCPCIDRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsABCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCWhsABCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsCtrlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCWhsCtrlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCWhsCtrlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCWhsCtrlRow[],
}

export interface Erp_Tablesets_CCDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   "AllocationVariance":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  Part Number selected for counting.  */  
   "PartNum":string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   "TotFrozenVal":number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   "TotFrozenQOH":number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   "PostStatus":number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   "CDRCode":string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   "TotCountVal":number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   "TotCountQOH":number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   "DateRemoved":string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   "RemovedBy":string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   "MoveToCycle":string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "PcntTolerance":number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCCode":string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyToleranceUsed":boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   "PcntToleranceUsed":boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   "ValToleranceUsed":boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   "QtyAdjTolerance":number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   "VarToleranceStat":number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   "PostAdjustment":number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyTolerance":number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   "ValueTolerance":number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "BaseUOM":string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   "TotActivityBeforeCount":number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   "TotActivityBeforeVal":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   "AddedByBlankTag":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCSeq":number,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   "EnableCDRCode":boolean,
      /**  Moved To Cycle Seq  */  
   "MovedToCycleSeq":number,
      /**  Moved to Month  */  
   "MovedToMonth":number,
      /**  Moved to Year  */  
   "MovedToYear":number,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   "MovePart":boolean,
      /**  Month name of MonthToMonth field  */  
   "MoveToMonthName":string,
      /**  Post Status Description  */  
   "PostStatusDesc":string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   "QtyAdjustmentStatus":string,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   "QtyVariance":number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   "ValueVariance":number,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   "VarToleranceStatDesc":string,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   "VoidPartTags":boolean,
      /**  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  */  
   "AddAllAttributeSets":boolean,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "EnableAttributeSetSearch":boolean,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
   "BitFlag":number,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodEnd":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "ReasonDescription":string,
   "WarehseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCHdrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   "CycleDate":string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   "CycleStatus":number,
      /**  This is the date the tags were generated  */  
   "TagGenDate":string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   "SeqStartDate":string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   "TimeSeqStarted":number,
      /**  This is the date the cycle was completed or cancelled.  */  
   "CompleteDate":string,
      /**  This is the time the cycle was completed or cancelled.  */  
   "CompleteTime":number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   "AdjustPosted":boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   "SheetOrTag":number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   "TotalParts":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IncludeNonNettable  */  
   "IncludeNonNettable":boolean,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   "TotalPCIDSelected":number,
      /**  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  */  
   "NestedPCID":boolean,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   "CancelPI":boolean,
   "CycleDateString":string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   "CycleStatusDesc":string,
   "EnablePrintTags":boolean,
   "EnableReprintTags":boolean,
   "EnableStartCountSeq":boolean,
   "EnableVoidBlankTags":boolean,
   "EnableVoidTagsByPart":boolean,
      /**  External field used to hold the Post Counts log filename.  */  
   "LogFileName":string,
      /**  Month Name  */  
   "MonthName":string,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   "NumOfBlankTags":number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   "PostTransDate":string,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   "RemoveAllParts":boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   "TagSortOption":number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   "BlankTagsOnly":boolean,
      /**  field used by GenerateTags to indicate how many blank PCID tags should be generated  */  
   "NumOfBlankPCIDTags":number,
   "PartPostedExists":boolean,
   "TrackedNumberSerialPart":boolean,
      /**  Indicates that any PartNumTrackSerialNum = true exist in details  */  
   "PartNumTrackSerialNum":boolean,
   "BitFlag":number,
   "CCHdrWarehseDescription":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodEnd":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCPCIDRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Site Identifier  */  
   "Plant":string,
      /**  Warehouse identifier  */  
   "WarehouseCode":string,
      /**  Calendar year that this cycle count is for  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  True = full physical inventory count cycle, false = cycle count cycle  */  
   "FullPhysical":boolean,
      /**  Cycle Sequence  */  
   "CycleSeq":number,
      /**  Equates to a PkgControlHeader PCID. It could be top level or a nested PCID.  */  
   "PCID":string,
      /**  The Parent PCID defined for this CCPCID.PCID  */  
   "ParentPCID":string,
      /**  The outermost PCID that contains this CCPCID.PCID  */  
   "TopLevelPCID":string,
      /**  True indicates this PCID was added to the cycle during count entry using a blank tag.  */  
   "AddedByBlankTag":boolean,
      /**  If any ItemPartNum count of this PCID has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE. For consistency with CCDtl, not currently used  */  
   "AllocationVariance":boolean,
      /**  Bin number defaulted from PkgControlHeader or entered on a blank tag  */  
   "BinNum":string,
      /**  There will be data here only if PostStatus =3 and the PCID was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   "MoveToCycle":string,
      /**  The date the PCID was removed from  the cycle. (PostStatus=3)  */  
   "DateRemoved":string,
      /**  This is the user id of the person that removed the PCID from the cycle (PostStatus=3)  */  
   "RemovedBy":string,
      /**  This data is created by the cycle count variance report process.  Used by the posting process to determine whether to post adjustments to inventory.  Code Desc: 0`Not Yet Evaluated~1`Adjustment Will Not Post~2`Adjustment Will Post  */  
   "PostAdjustment":number,
      /**  The posting status of the PCID. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made. 2= the count for this PCID has been processed by the post final counts process and inventory adjustments were not made 3= PCID was removed from the cycle after tags were generated, no posting required Code Desc: 0`Not Posted~1`Adjustment Posted~2`No Adjustment  Required~3`Voided  */  
   "PostStatus":number,
      /**  Reserved for development use.  */  
   "CCPCIDBoolean01":boolean,
      /**  Reserved for development use.  */  
   "CCPCIDBoolean02":boolean,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter01":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter02":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter03":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter04":string,
      /**  Reserved for development use.  */  
   "CCPCIDCharacter05":string,
      /**  Reserved for development use.  */  
   "CCPCIDDate01":string,
      /**  Reserved for development use.  */  
   "CCPCIDDate02":string,
      /**  Reserved for development use.  */  
   "CCPCIDDecimal01":number,
      /**  Reserved for development use.  */  
   "CCPCIDDecimal02":number,
      /**  Used for indicating the level at which this PCIDis nested below the top level it is associated to  */  
   "CCPCIDInteger01":number,
      /**  Reserved for development use.  */  
   "CCPCIDInteger02":number,
      /**  The warehouse to which the PCID should be moved during posting.  */  
   "MoveToWarehouseCode":string,
      /**  The warehouse bin to which the PCID should be moved during posting.  */  
   "MoveToBinNum":string,
      /**  The PCID to which this PCID should be added during posting.  */  
   "AddToPCID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Indicates if the CCPCID was selected for move or delete in Cycle Count Part / PCID Selection Update.  */  
   "MovePCID":boolean,
      /**  Needed if the user will be able to move PCID from one cycle to another in Part Selection Update  */  
   "MovetoMonthName":string,
      /**  Used to indicate that the VoidTagsByPCID processing should be done for this PCID.  */  
   "VoidPCIDTags":boolean,
      /**  The Month that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodSeq.  */  
   "MovedToMonth":number,
      /**  The Year that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodYear.  */  
   "MovedToYear":number,
      /**  The Cycle that this PCID was moved to during posting.  Format consistent with CCHdr.CycleSeq.  */  
   "MovedToCycleSeq":number,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   "QtyAdjustmentStatus":string,
   "BitFlag":number,
   "CCPeriodDefnPeriodEnd":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodDesc":string,
   "WarehseDescription":string,
   "WhseBinDescription":string,
   "WhseBinAisle":string,
   "WhseBinZoneID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCWhsABCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   "ABCCode":string,
      /**  For the random selection method, this is the number of parts to be selected for this ABC code for this month by the monthly selection process. Not used by the repetitive selection method.  */  
   "QtyToSelect":number,
      /**  Total number of parts with this ABC code that have been selected to be counted for the month. This data is initialized during the monthly selection process.  */  
   "TotalSelected":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  field used only by the random methiod during part selection  */  
   "ManuallyAdded":boolean,
   "BitFlag":number,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodEnd":string,
   "CCPeriodDefnPeriodStart":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCWhsCtrlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  This flag will indicate if the user chose to exclude inactive parts when doing the monthly selection.  */  
   "ExcludeInactive":boolean,
      /**  This flag will indicate if the user chose to exclude parts on hold when doing the monthly selection.  */  
   "ExcludeOnHold":boolean,
      /**  This flag will indicate if the user chose to exclude parts with negative QOH when doing the monthly selection.  */  
   "ExcludeNegQOH":boolean,
      /**  This flag will indicate if the user chose to exclude items with no activity since the last count. Used by the random selection method only.  */  
   "ExcludeNoActivity":boolean,
      /**  Indicates whether the part selection has been run for this month. Set by the cycle count item selection process.  */  
   "PartsSelected":boolean,
      /**  This flag will indicate if the user chose to exclude parts with zero QOH when doing the monthly selection.  */  
   "ExcludeZeroQOH":boolean,
      /**  Indicates the production calendar to use for creating the default cycles when a new CCWhsCtrl is saved.  */  
   "CCProdCal":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Field to indicate if PlantConfGtrl.CCSelectMethod for the CCWhsCtrl.Plant = 2.which indicates that the plant uses the cycle count random selection method to select part.  */  
   "UseRandomSelect":boolean,
      /**  warehouse description  */  
   "WhseDesc":string,
      /**  Month Name  */  
   "MonthName":string,
      /**  Defines the end date of the period  */  
   "CCPeriodDefnPeriodEnd":string,
      /**  Defines the start date of the count period  */  
   "CCPeriodDefnPeriodStart":string,
      /**  Unique period description assigned by the user.  */  
   "CCPeriodDefnPeriodDesc":string,
      /**  Calendar description.  */  
   "ProdCalDescription":string,
      /**  Description.  */  
   "WarehseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCWhsCtrlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  This flag will indicate if the user chose to exclude inactive parts when doing the monthly selection.  */  
   "ExcludeInactive":boolean,
      /**  This flag will indicate if the user chose to exclude parts on hold when doing the monthly selection.  */  
   "ExcludeOnHold":boolean,
      /**  This flag will indicate if the user chose to exclude parts with negative QOH when doing the monthly selection.  */  
   "ExcludeNegQOH":boolean,
      /**  This flag will indicate if the user chose to exclude items with no activity since the last count. Used by the random selection method only.  */  
   "ExcludeNoActivity":boolean,
      /**  Indicates whether the part selection has been run for this month. Set by the cycle count item selection process.  */  
   "PartsSelected":boolean,
      /**  This flag will indicate if the user chose to exclude parts with zero QOH when doing the monthly selection.  */  
   "ExcludeZeroQOH":boolean,
      /**  Indicates the production calendar to use for creating the default cycles when a new CCWhsCtrl is saved.  */  
   "CCProdCal":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This flag will indicate if the user chose to include non stock parts when doing the monthly selection.  */  
   "IncludeNonStock":boolean,
      /**  True = do not select PCID for the count. False = CCPCID records will automatically be generated for each top level PCID in the selected warehouses. Applies to Physical Inventory only.  */  
   "ExcludePCID":boolean,
      /**  This flag will indicate if the user chose to exclude inventory attribute tracked parts doing the part selection.  */  
   "ExcludeInvAttributeParts":boolean,
      /**  This flag will indicate if the user chose to exclude Inventory by Revision tracked parts when doing the part selection.  */  
   "ExcludeInvByRevisionParts":boolean,
      /**  Month Name  */  
   "MonthName":string,
      /**  Field to indicate if PlantConfGtrl.CCSelectMethod for the CCWhsCtrl.Plant = 2.which indicates that the plant uses the cycle count random selection method to select part.  */  
   "UseRandomSelect":boolean,
      /**  warehouse description  */  
   "WhseDesc":string,
   "BitFlag":number,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodEnd":string,
   "ProdCalDescription":string,
   "WarehseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
   */  
export interface DeleteByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
   */  
export interface DeleteCycleSequences_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface DeleteCycleSequences_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

export interface Erp_Tablesets_CCDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   AllocationVariance:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  Part Number selected for counting.  */  
   PartNum:string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   TotFrozenVal:number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   TotFrozenQOH:number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   PostStatus:number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   CDRCode:string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   TotCountVal:number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   TotCountQOH:number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   DateRemoved:string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   RemovedBy:string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   MoveToCycle:string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   PcntTolerance:number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCCode:string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyToleranceUsed:boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   PcntToleranceUsed:boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   ValToleranceUsed:boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   QtyAdjTolerance:number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   VarToleranceStat:number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   PostAdjustment:number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyTolerance:number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   ValueTolerance:number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   BaseUOM:string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   TotActivityBeforeCount:number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   TotActivityBeforeVal:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   AddedByBlankTag:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCSeq:number,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   EnableCDRCode:boolean,
      /**  Moved To Cycle Seq  */  
   MovedToCycleSeq:number,
      /**  Moved to Month  */  
   MovedToMonth:number,
      /**  Moved to Year  */  
   MovedToYear:number,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   MovePart:boolean,
      /**  Month name of MonthToMonth field  */  
   MoveToMonthName:string,
      /**  Post Status Description  */  
   PostStatusDesc:string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   QtyAdjustmentStatus:string,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   QtyVariance:number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   ValueVariance:number,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   VarToleranceStatDesc:string,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   VoidPartTags:boolean,
      /**  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  */  
   AddAllAttributeSets:boolean,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   EnableAttributeSetSearch:boolean,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   BitFlag:number,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodEnd:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   ReasonDescription:string,
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCDtlUOMSumRow{
      /**  Company  */  
   Company:string,
      /**  Plant  */  
   Plant:string,
   WarehouseCode:string,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  True = physical inventory  */  
   FullPhysical:boolean,
      /**  Part Number selected for counting.  */  
   PartNum:string,
      /**  The UOM that is summarized for this part for this record. Those CCTag with this part/UOM for this cycle whs/month/year/cycleSeq are summarized into this record.  */  
   UOM:string,
      /**  Total quantity on hand in the warehouse for this part.UOM at the time the inventory was frozen. This quantity is expressed in the UOM in  this summary record.  */  
   TotFrozenQOH:number,
      /**  New on hand in the warehouse based on the count qty entered on the tag. This quantity is expressed in the UOM in this summary record.  */  
   TotCountQOH:number,
      /**  Total ActivityBeforeCount for related CCTag records. This quantity is expressed in the UOM of this summary record.  */  
   TotActivityBeforeCount:number,
   CCMonth:number,
   CCYear:number,
      /**  CCPeriodDefn.PeriodDesc  */  
   PeriodDesc:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   PartNumAttrClassID:string,
      /**  Revision Number associated with the part.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCDtlUOMSumTableset{
   CCDtlUOMSum:Erp_Tablesets_CCDtlUOMSumRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CCHdrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   CycleDate:string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   CycleStatus:number,
      /**  This is the date the tags were generated  */  
   TagGenDate:string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   SeqStartDate:string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   TimeSeqStarted:number,
      /**  This is the date the cycle was completed or cancelled.  */  
   CompleteDate:string,
      /**  This is the time the cycle was completed or cancelled.  */  
   CompleteTime:number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   AdjustPosted:boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   SheetOrTag:number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   TotalParts:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IncludeNonNettable  */  
   IncludeNonNettable:boolean,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   TotalPCIDSelected:number,
      /**  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  */  
   NestedPCID:boolean,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   CancelPI:boolean,
   CycleDateString:string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   CycleStatusDesc:string,
   EnablePrintTags:boolean,
   EnableReprintTags:boolean,
   EnableStartCountSeq:boolean,
   EnableVoidBlankTags:boolean,
   EnableVoidTagsByPart:boolean,
      /**  External field used to hold the Post Counts log filename.  */  
   LogFileName:string,
      /**  Month Name  */  
   MonthName:string,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   NumOfBlankTags:number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   PostTransDate:string,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   RemoveAllParts:boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   TagSortOption:number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   BlankTagsOnly:boolean,
      /**  field used by GenerateTags to indicate how many blank PCID tags should be generated  */  
   NumOfBlankPCIDTags:number,
   PartPostedExists:boolean,
   TrackedNumberSerialPart:boolean,
      /**  Indicates that any PartNumTrackSerialNum = true exist in details  */  
   PartNumTrackSerialNum:boolean,
   BitFlag:number,
   CCHdrWarehseDescription:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodEnd:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCPCIDRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Site Identifier  */  
   Plant:string,
      /**  Warehouse identifier  */  
   WarehouseCode:string,
      /**  Calendar year that this cycle count is for  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  True = full physical inventory count cycle, false = cycle count cycle  */  
   FullPhysical:boolean,
      /**  Cycle Sequence  */  
   CycleSeq:number,
      /**  Equates to a PkgControlHeader PCID. It could be top level or a nested PCID.  */  
   PCID:string,
      /**  The Parent PCID defined for this CCPCID.PCID  */  
   ParentPCID:string,
      /**  The outermost PCID that contains this CCPCID.PCID  */  
   TopLevelPCID:string,
      /**  True indicates this PCID was added to the cycle during count entry using a blank tag.  */  
   AddedByBlankTag:boolean,
      /**  If any ItemPartNum count of this PCID has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE. For consistency with CCDtl, not currently used  */  
   AllocationVariance:boolean,
      /**  Bin number defaulted from PkgControlHeader or entered on a blank tag  */  
   BinNum:string,
      /**  There will be data here only if PostStatus =3 and the PCID was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   MoveToCycle:string,
      /**  The date the PCID was removed from  the cycle. (PostStatus=3)  */  
   DateRemoved:string,
      /**  This is the user id of the person that removed the PCID from the cycle (PostStatus=3)  */  
   RemovedBy:string,
      /**  This data is created by the cycle count variance report process.  Used by the posting process to determine whether to post adjustments to inventory.  Code Desc: 0`Not Yet Evaluated~1`Adjustment Will Not Post~2`Adjustment Will Post  */  
   PostAdjustment:number,
      /**  The posting status of the PCID. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made. 2= the count for this PCID has been processed by the post final counts process and inventory adjustments were not made 3= PCID was removed from the cycle after tags were generated, no posting required Code Desc: 0`Not Posted~1`Adjustment Posted~2`No Adjustment  Required~3`Voided  */  
   PostStatus:number,
      /**  Reserved for development use.  */  
   CCPCIDBoolean01:boolean,
      /**  Reserved for development use.  */  
   CCPCIDBoolean02:boolean,
      /**  Reserved for development use.  */  
   CCPCIDCharacter01:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter02:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter03:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter04:string,
      /**  Reserved for development use.  */  
   CCPCIDCharacter05:string,
      /**  Reserved for development use.  */  
   CCPCIDDate01:string,
      /**  Reserved for development use.  */  
   CCPCIDDate02:string,
      /**  Reserved for development use.  */  
   CCPCIDDecimal01:number,
      /**  Reserved for development use.  */  
   CCPCIDDecimal02:number,
      /**  Used for indicating the level at which this PCIDis nested below the top level it is associated to  */  
   CCPCIDInteger01:number,
      /**  Reserved for development use.  */  
   CCPCIDInteger02:number,
      /**  The warehouse to which the PCID should be moved during posting.  */  
   MoveToWarehouseCode:string,
      /**  The warehouse bin to which the PCID should be moved during posting.  */  
   MoveToBinNum:string,
      /**  The PCID to which this PCID should be added during posting.  */  
   AddToPCID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates if the CCPCID was selected for move or delete in Cycle Count Part / PCID Selection Update.  */  
   MovePCID:boolean,
      /**  Needed if the user will be able to move PCID from one cycle to another in Part Selection Update  */  
   MovetoMonthName:string,
      /**  Used to indicate that the VoidTagsByPCID processing should be done for this PCID.  */  
   VoidPCIDTags:boolean,
      /**  The Month that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodSeq.  */  
   MovedToMonth:number,
      /**  The Year that this PCID was moved to during posting.  Format consistent with CCPeriodDefn.PeriodYear.  */  
   MovedToYear:number,
      /**  The Cycle that this PCID was moved to during posting.  Format consistent with CCHdr.CycleSeq.  */  
   MovedToCycleSeq:number,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   QtyAdjustmentStatus:string,
   BitFlag:number,
   CCPeriodDefnPeriodEnd:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodDesc:string,
   WarehseDescription:string,
   WhseBinDescription:string,
   WhseBinAisle:string,
   WhseBinZoneID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCScheduleTableset{
   CCWhsCtrl:Erp_Tablesets_CCWhsCtrlRow[],
   CCHdr:Erp_Tablesets_CCHdrRow[],
   CCDtl:Erp_Tablesets_CCDtlRow[],
   CCPCID:Erp_Tablesets_CCPCIDRow[],
   CCWhsABC:Erp_Tablesets_CCWhsABCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CCWhsABCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   ABCCode:string,
      /**  For the random selection method, this is the number of parts to be selected for this ABC code for this month by the monthly selection process. Not used by the repetitive selection method.  */  
   QtyToSelect:number,
      /**  Total number of parts with this ABC code that have been selected to be counted for the month. This data is initialized during the monthly selection process.  */  
   TotalSelected:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  field used only by the random methiod during part selection  */  
   ManuallyAdded:boolean,
   BitFlag:number,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodEnd:string,
   CCPeriodDefnPeriodStart:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCWhsCtrlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  This flag will indicate if the user chose to exclude inactive parts when doing the monthly selection.  */  
   ExcludeInactive:boolean,
      /**  This flag will indicate if the user chose to exclude parts on hold when doing the monthly selection.  */  
   ExcludeOnHold:boolean,
      /**  This flag will indicate if the user chose to exclude parts with negative QOH when doing the monthly selection.  */  
   ExcludeNegQOH:boolean,
      /**  This flag will indicate if the user chose to exclude items with no activity since the last count. Used by the random selection method only.  */  
   ExcludeNoActivity:boolean,
      /**  Indicates whether the part selection has been run for this month. Set by the cycle count item selection process.  */  
   PartsSelected:boolean,
      /**  This flag will indicate if the user chose to exclude parts with zero QOH when doing the monthly selection.  */  
   ExcludeZeroQOH:boolean,
      /**  Indicates the production calendar to use for creating the default cycles when a new CCWhsCtrl is saved.  */  
   CCProdCal:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Field to indicate if PlantConfGtrl.CCSelectMethod for the CCWhsCtrl.Plant = 2.which indicates that the plant uses the cycle count random selection method to select part.  */  
   UseRandomSelect:boolean,
      /**  warehouse description  */  
   WhseDesc:string,
      /**  Month Name  */  
   MonthName:string,
      /**  Defines the end date of the period  */  
   CCPeriodDefnPeriodEnd:string,
      /**  Defines the start date of the count period  */  
   CCPeriodDefnPeriodStart:string,
      /**  Unique period description assigned by the user.  */  
   CCPeriodDefnPeriodDesc:string,
      /**  Calendar description.  */  
   ProdCalDescription:string,
      /**  Description.  */  
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCWhsCtrlListTableset{
   CCWhsCtrlList:Erp_Tablesets_CCWhsCtrlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CCWhsCtrlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  This flag will indicate if the user chose to exclude inactive parts when doing the monthly selection.  */  
   ExcludeInactive:boolean,
      /**  This flag will indicate if the user chose to exclude parts on hold when doing the monthly selection.  */  
   ExcludeOnHold:boolean,
      /**  This flag will indicate if the user chose to exclude parts with negative QOH when doing the monthly selection.  */  
   ExcludeNegQOH:boolean,
      /**  This flag will indicate if the user chose to exclude items with no activity since the last count. Used by the random selection method only.  */  
   ExcludeNoActivity:boolean,
      /**  Indicates whether the part selection has been run for this month. Set by the cycle count item selection process.  */  
   PartsSelected:boolean,
      /**  This flag will indicate if the user chose to exclude parts with zero QOH when doing the monthly selection.  */  
   ExcludeZeroQOH:boolean,
      /**  Indicates the production calendar to use for creating the default cycles when a new CCWhsCtrl is saved.  */  
   CCProdCal:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This flag will indicate if the user chose to include non stock parts when doing the monthly selection.  */  
   IncludeNonStock:boolean,
      /**  True = do not select PCID for the count. False = CCPCID records will automatically be generated for each top level PCID in the selected warehouses. Applies to Physical Inventory only.  */  
   ExcludePCID:boolean,
      /**  This flag will indicate if the user chose to exclude inventory attribute tracked parts doing the part selection.  */  
   ExcludeInvAttributeParts:boolean,
      /**  This flag will indicate if the user chose to exclude Inventory by Revision tracked parts when doing the part selection.  */  
   ExcludeInvByRevisionParts:boolean,
      /**  Month Name  */  
   MonthName:string,
      /**  Field to indicate if PlantConfGtrl.CCSelectMethod for the CCWhsCtrl.Plant = 2.which indicates that the plant uses the cycle count random selection method to select part.  */  
   UseRandomSelect:boolean,
      /**  warehouse description  */  
   WhseDesc:string,
   BitFlag:number,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodEnd:string,
   ProdCalDescription:string,
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCCScheduleTableset{
   CCWhsCtrl:Erp_Tablesets_CCWhsCtrlRow[],
   CCHdr:Erp_Tablesets_CCHdrRow[],
   CCDtl:Erp_Tablesets_CCDtlRow[],
   CCPCID:Erp_Tablesets_CCPCIDRow[],
   CCWhsABC:Erp_Tablesets_CCWhsABCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
   */  
export interface GetByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CCScheduleTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CCScheduleTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CCScheduleTableset[],
}

   /** Required : 
      @param vWarehouseCode
      @param vCCYear
      @param vCCMonth
      @param vFullPhysical
      @param vCycleSeq
      @param vPartNum
      @param vAttributeSetID
   */  
export interface GetCCDtlUOMSum_input{
   vWarehouseCode:string,
   vCCYear:number,
   vCCMonth:number,
   vFullPhysical:boolean,
   vCycleSeq:number,
   vPartNum:string,
   vAttributeSetID:number,
}

export interface GetCCDtlUOMSum_output{
   returnObj:Erp_Tablesets_CCDtlUOMSumTableset[],
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
   returnObj:Erp_Tablesets_CCWhsCtrlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
      @param partNum
   */  
export interface GetNewCCDtl_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
   partNum:string,
}

export interface GetNewCCDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
   */  
export interface GetNewCCHdr_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
}

export interface GetNewCCHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
   */  
export interface GetNewCCPCID_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
}

export interface GetNewCCPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
   */  
export interface GetNewCCWhsABC_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
}

export interface GetNewCCWhsABC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
   */  
export interface GetNewCCWhsCtrl_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
}

export interface GetNewCCWhsCtrl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param whereClauseCCWhsCtrl
      @param whereClauseCCHdr
      @param whereClauseCCDtl
      @param whereClauseCCPCID
      @param whereClauseCCWhsABC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCCWhsCtrl:string,
   whereClauseCCHdr:string,
   whereClauseCCDtl:string,
   whereClauseCCPCID:string,
   whereClauseCCWhsABC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CCScheduleTableset[],
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
      @param periodSeq
      @param ds
   */  
export interface OnChangeOfCCMonth_input{
      /**  Proposed Cycle Count Period Defintion PeriodSeq  */  
   periodSeq:number,
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface OnChangeOfCCMonth_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param calendarID
      @param ds
   */  
export interface OnChangeOfCCProdCal_input{
      /**  Proposed Cycle Count Calendar ID field  */  
   calendarID:string,
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface OnChangeOfCCProdCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ccYear
      @param ds
   */  
export interface OnChangeOfCCYear_input{
      /**  Proposed Cycle Count Year  */  
   ccYear:number,
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface OnChangeOfCCYear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ipWhseCode
      @param ds
   */  
export interface OnChangeWhseCode_input{
   ipWhseCode:string,
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface OnChangeWhseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface SelectParts_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface SelectParts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface UndoPartSelection_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface UndoPartSelection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCCScheduleTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCCScheduleTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CCScheduleTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCScheduleTableset[],
}
}

