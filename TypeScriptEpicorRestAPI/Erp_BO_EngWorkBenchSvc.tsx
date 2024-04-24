import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.EngWorkBenchSvc
// Description: Engineering Workbench Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/$metadata", {
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
   Description: Get EngWorkBenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EngWorkBenches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupRow
   */  
export function get_EngWorkBenches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EngWorkBenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EngWorkBenches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches", {
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
   Summary: Calls GetByID to retrieve the EngWorkBench item
   Description: Calls GetByID to retrieve the EngWorkBench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EngWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
   */  
export function get_EngWorkBenches_Company_GroupID(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EngWorkBench for the service
   Description: Calls UpdateExt to update EngWorkBench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EngWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EngWorkBenches_Company_GroupID(Company:string, GroupID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete EngWorkBench item
   Description: Call UpdateExt to delete EngWorkBench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EngWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EngWorkBenches_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")", {
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
   Description: Get ECORevs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECORevs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevRow
   */  
export function get_EngWorkBenches_Company_GroupID_ECORevs(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECORevs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECORev item
   Description: Calls GetByID to retrieve the ECORev item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORev1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevRow
   */  
export function get_EngWorkBenches_Company_GroupID_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECORevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECORevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOGroupAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOGroupAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupAttchRow
   */  
export function get_EngWorkBenches_Company_GroupID_ECOGroupAttches(Company:string, GroupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECOGroupAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOGroupAttch item
   Description: Calls GetByID to retrieve the ECOGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOGroupAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   */  
export function get_EngWorkBenches_Company_GroupID_ECOGroupAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECORevs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECORevs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevRow
   */  
export function get_ECORevs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECORevs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECORevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECORevs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs", {
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
   Summary: Calls GetByID to retrieve the ECORev item
   Description: Calls GetByID to retrieve the ECORev item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORev
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECORevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECORevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECORev for the service
   Description: Calls UpdateExt to update ECORev. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECORev
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
   Summary: Call UpdateExt to delete ECORev item
   Description: Call UpdateExt to delete ECORev item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECORev
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
   Description: Get ECOCOParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOCOParts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOCOPartRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOCOParts(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOCOPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOCOParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOCOPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOCOPart item
   Description: Calls GetByID to retrieve the ECOCOPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOCOPart1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, CoPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOCOPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOCOPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOMtls(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOMtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOMtl item
   Description: Calls GetByID to retrieve the ECOMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOOprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOOprs(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOOprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOpr item
   Description: Calls GetByID to retrieve the ECOOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECORevAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECORevAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevAttchRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECORevAttches(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECORevAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECORevAttch item
   Description: Calls GetByID to retrieve the ECORevAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORevAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   */  
export function get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECORevAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECORevAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECOCOParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOCOParts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOCOPartRow
   */  
export function get_ECOCOParts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOCOPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOCOPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOCOParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOCOParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts", {
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
   Summary: Calls GetByID to retrieve the ECOCOPart item
   Description: Calls GetByID to retrieve the ECOCOPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOCOPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   */  
export function get_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, CoPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOCOPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOCOPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOCOPart for the service
   Description: Calls UpdateExt to update ECOCOPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOCOPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, CoPartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")", {
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
   Summary: Call UpdateExt to delete ECOCOPart item
   Description: Call UpdateExt to delete ECOCOPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOCOPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, CoPartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")", {
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
   Description: Get ECOMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRow
   */  
export function get_ECOMtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOMtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls", {
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
   Summary: Calls GetByID to retrieve the ECOMtl item
   Description: Calls GetByID to retrieve the ECOMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOMtl for the service
   Description: Calls UpdateExt to update ECOMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOMtl item
   Description: Call UpdateExt to delete ECOMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")", {
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
   Description: Get ECOMtlInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlInsps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlInspRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlInsps(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOMtlInsp item
   Description: Calls GetByID to retrieve the ECOMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlInsp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlRefDes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlRefDes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRefDesRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRefDes(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRefDes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOMtlRefDe item
   Description: Calls GetByID to retrieve the ECOMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRefDe1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RefDesSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlRestrictions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictionRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRestrictions(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRestrictions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOMtlRestriction item
   Description: Calls GetByID to retrieve the ECOMtlRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestriction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlAttchRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlAttches(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOMtlAttch item
   Description: Calls GetByID to retrieve the ECOMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   */  
export function get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECOMtlInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlInsps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlInspRow
   */  
export function get_ECOMtlInsps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOMtlInsps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps", {
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
   Summary: Calls GetByID to retrieve the ECOMtlInsp item
   Description: Calls GetByID to retrieve the ECOMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   */  
export function get_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOMtlInsp for the service
   Description: Calls UpdateExt to update ECOMtlInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, PlanSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOMtlInsp item
   Description: Call UpdateExt to delete ECOMtlInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, PlanSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")", {
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
   Description: Get ECOMtlRefDes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlRefDes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRefDesRow
   */  
export function get_ECOMtlRefDes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOMtlRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes", {
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
   Summary: Calls GetByID to retrieve the ECOMtlRefDe item
   Description: Calls GetByID to retrieve the ECOMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   */  
export function get_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RefDesSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRefDesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRefDesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOMtlRefDe for the service
   Description: Calls UpdateExt to update ECOMtlRefDe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RefDesSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOMtlRefDe item
   Description: Call UpdateExt to delete ECOMtlRefDe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlRefDe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RefDesSeq Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RefDesSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")", {
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
   Description: Get ECOMtlRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlRestrictions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictionRow
   */  
export function get_ECOMtlRestrictions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOMtlRestrictions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions", {
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
   Summary: Calls GetByID to retrieve the ECOMtlRestriction item
   Description: Calls GetByID to retrieve the ECOMtlRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   */  
export function get_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOMtlRestriction for the service
   Description: Calls UpdateExt to update ECOMtlRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")", {
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
   Summary: Call UpdateExt to delete ECOMtlRestriction item
   Description: Call UpdateExt to delete ECOMtlRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")", {
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
   Description: Get ECOMtlRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlRestrictSubsts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictSubstRow
   */  
export function get_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_ECOMtlRestrictSubsts(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")/ECOMtlRestrictSubsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOMtlRestrictSubst item
   Description: Calls GetByID to retrieve the ECOMtlRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestrictSubst1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   */  
export function get_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECOMtlRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlRestrictSubsts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictSubstRow
   */  
export function get_ECOMtlRestrictSubsts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlRestrictSubsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOMtlRestrictSubsts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts", {
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
   Summary: Calls GetByID to retrieve the ECOMtlRestrictSubst item
   Description: Calls GetByID to retrieve the ECOMtlRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   */  
export function get_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOMtlRestrictSubst for the service
   Description: Calls UpdateExt to update ECOMtlRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, SubstanceID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
   Summary: Call UpdateExt to delete ECOMtlRestrictSubst item
   Description: Call UpdateExt to delete ECOMtlRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, RestrictionTypeID:string, SubstanceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
   Description: Get ECOMtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlAttchRow
   */  
export function get_ECOMtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOMtlAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches", {
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
   Summary: Calls GetByID to retrieve the ECOMtlAttch item
   Description: Calls GetByID to retrieve the ECOMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   */  
export function get_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOMtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOMtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOMtlAttch for the service
   Description: Calls UpdateExt to update ECOMtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOMtlAttch item
   Description: Call UpdateExt to delete ECOMtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, MtlSeq:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")", {
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
   Description: Get ECOOprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRow
   */  
export function get_ECOOprs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs", {
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
   Summary: Calls GetByID to retrieve the ECOOpr item
   Description: Calls GetByID to retrieve the ECOOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOpr for the service
   Description: Calls UpdateExt to update ECOOpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOOpr item
   Description: Call UpdateExt to delete ECOOpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", {
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
   Description: Get ECOOprActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprActions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprActions(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprAction item
   Description: Calls GetByID to retrieve the ECOOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOOprInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprInsps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprInspRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprInsps(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprInsp item
   Description: Calls GetByID to retrieve the ECOOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprInsp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOOprMachParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprMachParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprMachParamRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprMachParams(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprMachParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprMachParam item
   Description: Calls GetByID to retrieve the ECOOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprMachParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, MachParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOOpDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOpDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOpDtlRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOpDtls(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOpDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOpDtl item
   Description: Calls GetByID to retrieve the ECOOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, OpDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOOprRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprRestrictions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictionRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprRestrictions(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprRestrictions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprRestriction item
   Description: Calls GetByID to retrieve the ECOOprRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestriction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECOOprAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprAttchRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprAttches(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprAttch item
   Description: Calls GetByID to retrieve the ECOOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   */  
export function get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECOOprActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprActions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionRow
   */  
export function get_ECOOprActions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprActions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions", {
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
   Summary: Calls GetByID to retrieve the ECOOprAction item
   Description: Calls GetByID to retrieve the ECOOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   */  
export function get_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprAction for the service
   Description: Calls UpdateExt to update ECOOprAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOOprAction item
   Description: Call UpdateExt to delete ECOOprAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")", {
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
   Description: Get ECOOprActionParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprActionParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionParamRow
   */  
export function get_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ECOOprActionParams(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")/ECOOprActionParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprActionParam item
   Description: Calls GetByID to retrieve the ECOOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprActionParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   */  
export function get_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECOOprActionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprActionParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionParamRow
   */  
export function get_ECOOprActionParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprActionParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprActionParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams", {
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
   Summary: Calls GetByID to retrieve the ECOOprActionParam item
   Description: Calls GetByID to retrieve the ECOOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   */  
export function get_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprActionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprActionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprActionParam for the service
   Description: Calls UpdateExt to update ECOOprActionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOOprActionParam item
   Description: Call UpdateExt to delete ECOOprActionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprActionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param ActionSeq Desc: ActionSeq   Required: True
      @param ActionParamSeq Desc: ActionParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, ActionSeq:string, ActionParamSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", {
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
   Description: Get ECOOprInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprInsps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprInspRow
   */  
export function get_ECOOprInsps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprInsps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps", {
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
   Summary: Calls GetByID to retrieve the ECOOprInsp item
   Description: Calls GetByID to retrieve the ECOOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   */  
export function get_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprInsp for the service
   Description: Calls UpdateExt to update ECOOprInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, PlanSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOOprInsp item
   Description: Call UpdateExt to delete ECOOprInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, PlanSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")", {
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
   Description: Get ECOOprMachParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprMachParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprMachParamRow
   */  
export function get_ECOOprMachParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprMachParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprMachParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams", {
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
   Summary: Calls GetByID to retrieve the ECOOprMachParam item
   Description: Calls GetByID to retrieve the ECOOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprMachParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   */  
export function get_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, MachParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprMachParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprMachParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprMachParam for the service
   Description: Calls UpdateExt to update ECOOprMachParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprMachParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, MachParamSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOOprMachParam item
   Description: Call UpdateExt to delete ECOOprMachParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprMachParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param MachParamSeq Desc: MachParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, MachParamSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")", {
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
   Description: Get ECOOpDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOpDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOpDtlRow
   */  
export function get_ECOOpDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOpDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOpDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls", {
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
   Summary: Calls GetByID to retrieve the ECOOpDtl item
   Description: Calls GetByID to retrieve the ECOOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   */  
export function get_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, OpDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOpDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOpDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOpDtl for the service
   Description: Calls UpdateExt to update ECOOpDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOpDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, OpDtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOOpDtl item
   Description: Call UpdateExt to delete ECOOpDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOpDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param OpDtlSeq Desc: OpDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, OpDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")", {
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
   Description: Get ECOOprRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprRestrictions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictionRow
   */  
export function get_ECOOprRestrictions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprRestrictions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions", {
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
   Summary: Calls GetByID to retrieve the ECOOprRestriction item
   Description: Calls GetByID to retrieve the ECOOprRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   */  
export function get_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprRestrictionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprRestrictionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprRestriction for the service
   Description: Calls UpdateExt to update ECOOprRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")", {
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
   Summary: Call UpdateExt to delete ECOOprRestriction item
   Description: Call UpdateExt to delete ECOOprRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprRestriction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")", {
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
   Description: Get ECOOprRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprRestrictSubsts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictSubstRow
   */  
export function get_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_ECOOprRestrictSubsts(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")/ECOOprRestrictSubsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprRestrictSubst item
   Description: Calls GetByID to retrieve the ECOOprRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestrictSubst1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   */  
export function get_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECOOprRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprRestrictSubsts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictSubstRow
   */  
export function get_ECOOprRestrictSubsts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprRestrictSubsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprRestrictSubsts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts", {
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
   Summary: Calls GetByID to retrieve the ECOOprRestrictSubst item
   Description: Calls GetByID to retrieve the ECOOprRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   */  
export function get_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, SubstanceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprRestrictSubstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprRestrictSubstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprRestrictSubst for the service
   Description: Calls UpdateExt to update ECOOprRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, SubstanceID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
   Summary: Call UpdateExt to delete ECOOprRestrictSubst item
   Description: Call UpdateExt to delete ECOOprRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprRestrictSubst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param RestrictionTypeID Desc: RestrictionTypeID   Required: True   Allow empty value : True
      @param SubstanceID Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, RestrictionTypeID:string, SubstanceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", {
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
   Description: Get ECOOprAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprAttchRow
   */  
export function get_ECOOprAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches", {
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
   Summary: Calls GetByID to retrieve the ECOOprAttch item
   Description: Calls GetByID to retrieve the ECOOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   */  
export function get_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprAttch for the service
   Description: Calls UpdateExt to update ECOOprAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOOprAttch item
   Description: Call UpdateExt to delete ECOOprAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")", {
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
   Description: Get ECORevAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECORevAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevAttchRow
   */  
export function get_ECORevAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECORevAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECORevAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches", {
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
   Summary: Calls GetByID to retrieve the ECORevAttch item
   Description: Calls GetByID to retrieve the ECORevAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORevAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   */  
export function get_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECORevAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECORevAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECORevAttch for the service
   Description: Calls UpdateExt to update ECORevAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECORevAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ECORevAttch item
   Description: Call UpdateExt to delete ECORevAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECORevAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")", {
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
   Description: Get ECOGroupAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOGroupAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupAttchRow
   */  
export function get_ECOGroupAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOGroupAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOGroupAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches", {
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
   Summary: Calls GetByID to retrieve the ECOGroupAttch item
   Description: Calls GetByID to retrieve the ECOGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOGroupAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   */  
export function get_ECOGroupAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOGroupAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOGroupAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOGroupAttch for the service
   Description: Calls UpdateExt to update ECOGroupAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOGroupAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOGroupAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOGroupAttch item
   Description: Call UpdateExt to delete ECOGroupAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOGroupAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOGroupAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
   Description: Get ECOImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOImportRow
   */  
export function get_ECOImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports", {
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
   Summary: Calls GetByID to retrieve the ECOImport item
   Description: Calls GetByID to retrieve the ECOImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOImport
      @param PartNum Desc: PartNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOImportRow
   */  
export function get_ECOImports_PartNum(PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports(" + PartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOImport for the service
   Description: Calls UpdateExt to update ECOImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOImport
      @param PartNum Desc: PartNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOImports_PartNum(PartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports(" + PartNum + ")", {
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
   Summary: Call UpdateExt to delete ECOImport item
   Description: Call UpdateExt to delete ECOImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOImport
      @param PartNum Desc: PartNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOImports_PartNum(PartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports(" + PartNum + ")", {
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
   Description: Get ECOStages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOStages
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOStageRow
   */  
export function get_ECOStages(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOStageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOStageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOStages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOStageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOStageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOStages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages", {
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
   Summary: Calls GetByID to retrieve the ECOStage item
   Description: Calls GetByID to retrieve the ECOStage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOStage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param StageSeq Desc: StageSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOStageRow
   */  
export function get_ECOStages_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_StageSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, StageSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOStageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + StageSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOStageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOStage for the service
   Description: Calls UpdateExt to update ECOStage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOStage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param StageSeq Desc: StageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOStageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOStages_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_StageSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, StageSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + StageSeq + ")", {
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
   Summary: Call UpdateExt to delete ECOStage item
   Description: Call UpdateExt to delete ECOStage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOStage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param StageSeq Desc: StageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOStages_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_StageSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, StageSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + StageSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClauseECOGroup:string, whereClauseECOGroupAttch:string, whereClauseECORev:string, whereClauseECORevAttch:string, whereClauseECOCOPart:string, whereClauseECOMtl:string, whereClauseECOMtlAttch:string, whereClauseECOMtlInsp:string, whereClauseECOMtlRefDes:string, whereClauseECOMtlRestriction:string, whereClauseECOMtlRestrictSubst:string, whereClauseECOOpr:string, whereClauseECOOprAttch:string, whereClauseECOOprAction:string, whereClauseECOOprActionParam:string, whereClauseECOOprInsp:string, whereClauseECOOprMachParam:string, whereClauseECOOpDtl:string, whereClauseECOOprRestriction:string, whereClauseECOOprRestrictSubst:string, whereClauseECOImport:string, whereClauseECOStage:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseECOGroup!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOGroup=" + whereClauseECOGroup
   }
   if(typeof whereClauseECOGroupAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOGroupAttch=" + whereClauseECOGroupAttch
   }
   if(typeof whereClauseECORev!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECORev=" + whereClauseECORev
   }
   if(typeof whereClauseECORevAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECORevAttch=" + whereClauseECORevAttch
   }
   if(typeof whereClauseECOCOPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOCOPart=" + whereClauseECOCOPart
   }
   if(typeof whereClauseECOMtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOMtl=" + whereClauseECOMtl
   }
   if(typeof whereClauseECOMtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOMtlAttch=" + whereClauseECOMtlAttch
   }
   if(typeof whereClauseECOMtlInsp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOMtlInsp=" + whereClauseECOMtlInsp
   }
   if(typeof whereClauseECOMtlRefDes!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOMtlRefDes=" + whereClauseECOMtlRefDes
   }
   if(typeof whereClauseECOMtlRestriction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOMtlRestriction=" + whereClauseECOMtlRestriction
   }
   if(typeof whereClauseECOMtlRestrictSubst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOMtlRestrictSubst=" + whereClauseECOMtlRestrictSubst
   }
   if(typeof whereClauseECOOpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOpr=" + whereClauseECOOpr
   }
   if(typeof whereClauseECOOprAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOprAttch=" + whereClauseECOOprAttch
   }
   if(typeof whereClauseECOOprAction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOprAction=" + whereClauseECOOprAction
   }
   if(typeof whereClauseECOOprActionParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOprActionParam=" + whereClauseECOOprActionParam
   }
   if(typeof whereClauseECOOprInsp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOprInsp=" + whereClauseECOOprInsp
   }
   if(typeof whereClauseECOOprMachParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOprMachParam=" + whereClauseECOOprMachParam
   }
   if(typeof whereClauseECOOpDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOpDtl=" + whereClauseECOOpDtl
   }
   if(typeof whereClauseECOOprRestriction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOprRestriction=" + whereClauseECOOprRestriction
   }
   if(typeof whereClauseECOOprRestrictSubst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOprRestrictSubst=" + whereClauseECOOprRestrictSubst
   }
   if(typeof whereClauseECOImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOImport=" + whereClauseECOImport
   }
   if(typeof whereClauseECOStage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOStage=" + whereClauseECOStage
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetRows" + params, {
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
export function get_GetByID(groupID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetList" + params, {
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
   Summary: Invoke method UnLockAll
   Description: This method unlocks all the revisions in a group.
This method runs the logic behind the old Vantage 6.1 Group>Lock All menu option.
   OperationID: UnLockAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLockAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLockAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnLockAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UnLockAll", {
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
   Summary: Invoke method UnLockAllAndRefresh
   Description: This Invokes UnLockAll() to lock all revisions followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: UnLockAllAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLockAllAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLockAllAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnLockAllAndRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UnLockAllAndRefresh", {
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
   Summary: Invoke method ValidateBill
   Description: This method validate the bill for the revision.
This method runs the logic behind the old Vantage 6.1 Revision>Validate Bill menu option.
   OperationID: ValidateBill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBill(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ValidateBill", {
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
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInspection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ValidateInspection", {
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
   Summary: Invoke method ValidateRefDes
   Description: Verify that there are no other ECOMtlRefDes records in the revision having the
same RefDes value if the ECORev.ValRefDes = true. Check the number of reference
designators are equal to the Required Ref Designators defined on ECOMtl.
   OperationID: ValidateRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ValidateRefDes", {
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
   Summary: Invoke method ViewCosts
   Description: This method will return the data need to display Part Rev costs.
   OperationID: ViewCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ViewCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ViewCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ViewCosts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ViewCosts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetCodeDescList", {
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
   Summary: Invoke method UpdateECORev
   OperationID: UpdateECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateECORev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UpdateECORev", {
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
   Summary: Invoke method UpdateCurrentECORev
   OperationID: UpdateCurrentECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCurrentECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCurrentECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCurrentECORev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UpdateCurrentECORev", {
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
   Summary: Invoke method UpdatePartECORev
   Description: UpdatePartECORev method used for PLM REST workflow
   OperationID: UpdatePartECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePartECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePartECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePartECORev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UpdatePartECORev", {
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
   Summary: Invoke method UpdateCurrentPartECORev
   Description: UpdateCurrentPartECORev method used for PLM REST workflow
   OperationID: UpdateCurrentPartECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCurrentPartECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCurrentPartECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCurrentPartECORev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UpdateCurrentPartECORev", {
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
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfCurrentSiteHasExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIfCurrentSiteHasExternalMES(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetIfCurrentSiteHasExternalMES", {
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
   Summary: Invoke method RequestApproveExternalMESValidation
   Description: MES Approval Validation
   OperationID: RequestApproveExternalMESValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RequestApproveExternalMESValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestApproveExternalMESValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RequestApproveExternalMESValidation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/RequestApproveExternalMESValidation", {
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
   Summary: Invoke method IsTopPartSalesKit
   Description: Checks if the top part is a Sales Kit
   OperationID: IsTopPartSalesKit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsTopPartSalesKit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTopPartSalesKit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsTopPartSalesKit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/IsTopPartSalesKit", {
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
   Summary: Invoke method CheckRulesBeforeDelete
   Description: Validate if exists rules to display a warning that rules may be deleted
   OperationID: CheckRulesBeforeDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRulesBeforeDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRulesBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRulesBeforeDelete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckRulesBeforeDelete", {
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
   Summary: Invoke method GetRowsWithCustomsBOM
   Description: Returns a Rows Dataset, which contains ECORev table filtered with PartRev.CNCustomsBOM=1 And not linked to CNCustomsHandbookHeader
   OperationID: GetRowsWithCustomsBOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWithCustomsBOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithCustomsBOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsWithCustomsBOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetRowsWithCustomsBOM", {
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
   Summary: Invoke method OnChangingProcessMfgType
   Description: Logic for when the recipe type is changing
   OperationID: OnChangingProcessMfgType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingProcessMfgType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingProcessMfgType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingProcessMfgType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingProcessMfgType", {
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
   Summary: Invoke method ChangeEcoMtlMtlAttributeSetID
   OperationID: ChangeEcoMtlMtlAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoMtlMtlAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoMtlMtlAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEcoMtlMtlAttributeSetID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeEcoMtlMtlAttributeSetID", {
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
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Logic for when the number of pieces is changing
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingNumberOfPieces", {
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
   Summary: Invoke method OnChangingSalvageNumberOfPieces
   Description: Logic for when the salvage number of pieces is changing
   OperationID: OnChangingSalvageNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSalvageNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSalvageNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSalvageNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingSalvageNumberOfPieces", {
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
   Summary: Invoke method GetEcoRevPartTypeCode
   Description: Returns the part's Type Code
   OperationID: GetEcoRevPartTypeCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEcoRevPartTypeCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEcoRevPartTypeCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEcoRevPartTypeCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetEcoRevPartTypeCode", {
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
   Summary: Invoke method GetTreeStructure
   Description: Returns TreeStructure for recipe
   OperationID: GetTreeStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTreeStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTreeStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTreeStructure(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetTreeStructure", {
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
   Summary: Invoke method ChangeEcoMtlSalvageAttributeSetID
   OperationID: ChangeEcoMtlSalvageAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoMtlSalvageAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoMtlSalvageAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEcoMtlSalvageAttributeSetID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeEcoMtlSalvageAttributeSetID", {
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
   Summary: Invoke method ChangeEcoOprAttributeSetID
   OperationID: ChangeEcoOprAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoOprAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoOprAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEcoOprAttributeSetID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeEcoOprAttributeSetID", {
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
   Summary: Invoke method ProcessMassCheckout
   Description: Process MassCheckout - loop to possibly create new revisions and
checkout for multiple parts
   OperationID: ProcessMassCheckout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMassCheckout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMassCheckout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessMassCheckout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ProcessMassCheckout", {
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
   Summary: Invoke method GetMassCheckout
   Description: Gets the default values for the MassCheck data table based on the part
number entered.
   OperationID: GetMassCheckout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMassCheckout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassCheckout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMassCheckout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetMassCheckout", {
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
   Summary: Invoke method OnChangingMassCheckoutCreateNewRev
   Description: Call this method when the CreateNewRev changes in MassCheckout
   OperationID: OnChangingMassCheckoutCreateNewRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMassCheckoutCreateNewRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMassCheckoutCreateNewRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingMassCheckoutCreateNewRev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingMassCheckoutCreateNewRev", {
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
   Summary: Invoke method OnChangingMassCheckoutRevisionNum
   Description: Call this method when either Revision changes in MassCheckout
   OperationID: OnChangingMassCheckoutRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMassCheckoutRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMassCheckoutRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingMassCheckoutRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingMassCheckoutRevisionNum", {
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
   Summary: Invoke method OnChangingMtlRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingMtlRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMtlRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMtlRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingMtlRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingMtlRevisionNum", {
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
   Summary: Invoke method OnChangingSalvageRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingSalvageRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSalvageRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSalvageRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSalvageRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingSalvageRevisionNum", {
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
   Summary: Invoke method OnChangingSubRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingSubRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSubRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSubRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSubRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/OnChangingSubRevisionNum", {
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
   Summary: Invoke method GetNewECOGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOGroup", {
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
   Summary: Invoke method GetNewECOGroupAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOGroupAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOGroupAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOGroupAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOGroupAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOGroupAttch", {
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
   Summary: Invoke method GetNewECORev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECORev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECORev", {
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
   Summary: Invoke method GetNewECORevAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECORevAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECORevAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORevAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECORevAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECORevAttch", {
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
   Summary: Invoke method GetNewECOCOPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOCOPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOCOPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOCOPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOCOPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOCOPart", {
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
   Summary: Invoke method GetNewECOMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOMtl", {
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
   Summary: Invoke method GetNewECOMtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOMtlAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOMtlAttch", {
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
   Summary: Invoke method GetNewECOMtlInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOMtlInsp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOMtlInsp", {
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
   Summary: Invoke method GetNewECOMtlRefDes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOMtlRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOMtlRefDes", {
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
   Summary: Invoke method GetNewECOMtlRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOMtlRestriction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOMtlRestriction", {
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
   Summary: Invoke method GetNewECOMtlRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlRestrictSubst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOMtlRestrictSubst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOMtlRestrictSubst", {
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
   Summary: Invoke method GetNewECOOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOpr", {
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
   Summary: Invoke method GetNewECOOprAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprAttch", {
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
   Summary: Invoke method GetNewECOOprAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprAction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprAction", {
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
   Summary: Invoke method GetNewECOOprActionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprActionParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprActionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprActionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprActionParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprActionParam", {
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
   Summary: Invoke method GetNewECOOprInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprInsp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprInsp", {
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
   Summary: Invoke method GetNewECOOprMachParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprMachParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprMachParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprMachParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprMachParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprMachParam", {
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
   Summary: Invoke method GetNewECOOpDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOpDtl", {
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
   Summary: Invoke method GetNewECOOprRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprRestriction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprRestriction", {
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
   Summary: Invoke method GetNewECOOprRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprRestrictSubst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprRestrictSubst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprRestrictSubst", {
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
   Summary: Invoke method GetNewECOStage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOStage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOStage", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UpdateExt", {
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
   Summary: Invoke method GetSchedulingBlocks
   OperationID: GetSchedulingBlocks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSchedulingBlocks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedulingBlocks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSchedulingBlocks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetSchedulingBlocks", {
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
   Summary: Invoke method getNextOpDtlSeq
   OperationID: getNextOpDtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getNextOpDtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getNextOpDtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getNextOpDtlSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/getNextOpDtlSeq", {
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
   Summary: Invoke method GetNewECOOprByStageNumber
   Description: Inserts a new ECOOpr row in the DataSet with defaults populated, based on Stage Number.
   OperationID: GetNewECOOprByStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprByStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprByStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOprByStageNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOOprByStageNumber", {
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
   Summary: Invoke method GetNewECOMtlByStageNumber
   Description: Inserts a new ECOMtl row in the DataSet with defaults populated, based on Stage Number.
   OperationID: GetNewECOMtlByStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlByStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlByStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOMtlByStageNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECOMtlByStageNumber", {
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
   Summary: Invoke method AddRefDesRange
   Description: Creates new ECOMtlRefDes records based on the ECOMtl dataset fields.
   OperationID: AddRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRefDesRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/AddRefDesRange", {
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
   Summary: Invoke method AllowApproveMethod
   Description: This method exists soley for the purpose of allowing security for
approving a method to be defined
   OperationID: AllowApproveMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowApproveMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowApproveMethod(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/AllowApproveMethod", {
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
   Summary: Invoke method AllowUnapproveMethod
   Description: This method exists soley for the purpose of allowing security for
unapproving a method to be defined
   OperationID: AllowUnapproveMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowUnapproveMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowUnapproveMethod(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/AllowUnapproveMethod", {
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
   Summary: Invoke method ApproveAll
   Description: This methods approves all revisions within an ECOGroup and returns a results string
and returns an updated dataset if the user chooses to.
This method runs the logic behind the Vantage 6.1 Group>Approve All menu option.
   OperationID: ApproveAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ApproveAll", {
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
   Summary: Invoke method ApproveAllAndRefresh
   Description: Invokes ApproveAll() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: ApproveAllAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAllAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAllAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveAllAndRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ApproveAllAndRefresh", {
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
   Summary: Invoke method ApproveAndCheckInAll
   Description: This methods approves and checks in all revisions within an ECOGroup and returns a results string
and returns an updated dataset if the user chooses to.
This method runs the logic behind the Group>Approve and Check In All menu option.
   OperationID: ApproveAndCheckInAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAndCheckInAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAndCheckInAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveAndCheckInAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ApproveAndCheckInAll", {
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
   Summary: Invoke method ChangeECOCoPartPartNum
   Description: This method validates the ECOCoPart.CoPartNum and defaults fields associated with the partnum.
This method should run when the ECOCoPart.CoPartNum field changes.
   OperationID: ChangeECOCoPartPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOCoPartPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOCoPartPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOCoPartPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOCoPartPartNum", {
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
   Summary: Invoke method ChangeECOGroupGroupClosed
   Description: This methods assigns fields associated with ECOGroup.GroupClosed changing.
If ECOGroup.GroupClosed changes to true, ClosedBy, ClosedDate, and ClosedTime gets populated.
This method should run before/at the time ECOGroup.GroupClosed field changes.
   OperationID: ChangeECOGroupGroupClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOGroupGroupClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOGroupGroupClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOGroupGroupClosed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOGroupGroupClosed", {
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
   Summary: Invoke method ChangeECOGroupWorkflowGroup
   Description: This methods assigns fields associated with ECOGroup.WFGroupID changing.
If ECOGroup.WFGroupID changes, verify and check if there is a default TaskSetID
associated with the WFGroupID and if so, populate ECOGroup.TaskSetID.
This method should run before/at the time ECOGroup.WFGroupID field changes.
   OperationID: ChangeECOGroupWorkflowGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOGroupWorkflowGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOGroupWorkflowGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOGroupWorkflowGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOGroupWorkflowGroup", {
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
   Summary: Invoke method ChangeECOMtlFixedQty
   Description: This methods assigns ECOMtl.EstScrap field when ECOMtl.FixedQty changes.
This method should run when the ECOMtl.FixedQty changes.
   OperationID: ChangeECOMtlFixedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlFixedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlFixedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlFixedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlFixedQty", {
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
   Summary: Invoke method ChangeEcoMtlInspPlan
   OperationID: ChangeEcoMtlInspPlan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoMtlInspPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoMtlInspPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEcoMtlInspPlan(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeEcoMtlInspPlan", {
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
   Summary: Invoke method ChangeECOMtlMtlPartNum
   Description: This method assigns the associated fields when the ECOMtl.MtlPartNum field changes.
This method should run when changing the ECOMtl.MtlPartNum.
   OperationID: ChangeECOMtlMtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlMtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlMtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlMtlPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlMtlPartNum", {
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
   Summary: Invoke method ChangeECOMtlMtlSeq
   Description: This method create a new ttECOMtl record and delete the existing one when changing
this component of the primary unique index and update the ecomtl.qq.
This method should run before changing the ECOMtl.MtlSeq.
   OperationID: ChangeECOMtlMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlMtlSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlMtlSeq", {
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
   Summary: Invoke method ChangeECOMtlPlanAsAsm
   Description: This method assigns the associated fields when the ECOMtl.MtlPartNum field changes.
This method should run when changing the ECOMtl.MtlPartNum.
   OperationID: ChangeECOMtlPlanAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlPlanAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlPlanAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlPlanAsAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlPlanAsAsm", {
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
   Summary: Invoke method ChangeECOMtlPullAsAsm
   Description: This method assigns the associated fields when the ECOMtl.MtlPartNum field changes.
This method should run when changing the ECOMtl.MtlPartNum.
   OperationID: ChangeECOMtlPullAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlPullAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlPullAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlPullAsAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlPullAsAsm", {
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
   Summary: Invoke method ChangeECOMtlQtyPer
   Description: This methods assigns ECOMtl.ReqRefDes and ECOMtl.RDEndNum fields
when ECOMtl.QtyPer changes. This method should run when the ECOMtl.QtyPer changes.
   OperationID: ChangeECOMtlQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlQtyPer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlQtyPer", {
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
   Summary: Invoke method ChangeECOMtlSalvageQtyPer
   Description: This methods updates ECOMtl Salvage Number of Pieces when ECOMtl.SalvageQtyPer changes.
This method should run when the ECOMtl.SalvageQtyPer changes.
   OperationID: ChangeECOMtlSalvageQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlSalvageQtyPer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlSalvageQtyPer", {
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
   Summary: Invoke method ChangeECOMtlSalvageUM
   Description: This methods updates ECOMtl Salvage Number of Pieces when ECOMtl.SalvageUM changes.
This method should run when the ECOMtl.SalvageUM changes.
   OperationID: ChangeECOMtlSalvageUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlSalvageUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlSalvageUM", {
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
   Summary: Invoke method ChangeECOMtlReassignSNAsm
   Description: Validates that there is no other material with ReassignSNAsm field to TRUE
   OperationID: ChangeECOMtlReassignSNAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlReassignSNAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlReassignSNAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlReassignSNAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlReassignSNAsm", {
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
   Summary: Invoke method ChangeECOMtlRelatedOperation
   Description: This methods assigns associated fields when ECOMtl.RelatedOperation changes.
This method should run when the ECOMtl.RelatedOperation changes.
   OperationID: ChangeECOMtlRelatedOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRelatedOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRelatedOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlRelatedOperation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlRelatedOperation", {
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
   Summary: Invoke method ChangeECOMtlRelatedStage
   Description: This methods assigns associated fields when ECOMtl.RelatedStage changes.
This method should run when the ECOMtl.RelatedStage changes.
   OperationID: ChangeECOMtlRelatedStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRelatedStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRelatedStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlRelatedStage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlRelatedStage", {
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
   Summary: Invoke method ChangeECOMtlReqRefDes
   Description: This methods assigns ECOMtl.RDEndNum field when ECOMtl.ReqRefDes changes.
This method should run when the ECOMtl.ReqRefDes changes.
   OperationID: ChangeECOMtlReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlReqRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlReqRefDes", {
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
   Summary: Invoke method ChangeECOMtlRestriction
   Description: This methods assigns associated fields when ECOMtlRestriction.RestrictionTypeID changes.
   OperationID: ChangeECOMtlRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlRestriction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlRestriction", {
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
   Summary: Invoke method ChangeECOMtlRFQNeeded
   Description: This methods assigns ECOMtl.RFQVendQuotes field when ECOMtl.RFQNeeded changes.
This method should run when the ECOMtl.RFQNeeded changes.
   OperationID: ChangeECOMtlRFQNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRFQNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRFQNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlRFQNeeded(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlRFQNeeded", {
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
   Summary: Invoke method ChangeECOMtlSalvageMtlBurRate
   Description: This methods assigns ECOMtl.SalvageEstMtlBurUnitCredit field when ECOMtl.SalvageMtlBurRate changes.
This method should run when the ECOMtl.SalvageMtlBurRate changes.
   OperationID: ChangeECOMtlSalvageMtlBurRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageMtlBurRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageMtlBurRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlSalvageMtlBurRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlSalvageMtlBurRate", {
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
   Summary: Invoke method ChangeECOMtlSalvagePartNum
   Description: This methods assigns associated fields when ECOMtl.SalvagePartNum changes.
This method should run when the ECOMtl.SalvagePartNum changes.
   OperationID: ChangeECOMtlSalvagePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvagePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvagePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlSalvagePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlSalvagePartNum", {
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
   Summary: Invoke method ChangeECOMtlSalvageUnitCredit
   Description: This methods assigns ECOMtl.SalvageEstMtlBurUnitCredit field when ECOMtl.SalvageUnitCredit changes.
This method should run when the ECOMtl.SalvageMtlBurRate changes.
   OperationID: ChangeECOMtlSalvageUnitCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageUnitCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageUnitCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlSalvageUnitCredit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlSalvageUnitCredit", {
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
   Summary: Invoke method ChangeECOMtlSubstance
   Description: This methods assigns associated fields when ECOMtlRestrictSubst.SubstanceID changes.
   OperationID: ChangeECOMtlSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOMtlSubstance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOMtlSubstance", {
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
   Summary: Invoke method ChangeECOOpDtlCapability
   Description: Method to call when changing the Capability ID.  This method will update ECOOpDtl
to see if the labor and burden rates need to be reset.  Blank is a valid entry for
Capability ID.
   OperationID: ChangeECOOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOpDtlCapability(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOpDtlCapability", {
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
   Summary: Invoke method ChangeECOOpDtlResourceGrpID
   Description: Method to call when changing the Resource Group ID.  Blank is a valid
entry for Resource Group ID.
   OperationID: ChangeECOOpDtlResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOpDtlResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOpDtlResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOpDtlResourceGrpID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOpDtlResourceGrpID", {
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
   Summary: Invoke method ChangeECOOpDtlResourceID
   Description: Method to call when changing the Resource ID.  Blank is a valid entry for Resource ID.
   OperationID: ChangeECOOpDtlResourceID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOpDtlResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOpDtlResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOpDtlResourceID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOpDtlResourceID", {
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
   Summary: Invoke method ChangeECOOprAutoReceive
   Description: This method also returns a list of values/descriptions for the LaborEntryMethod dropdown
based on the value of the ECOOpr.AutoReceive field.  This does not change the actual
value of the ECOOpr.LaborEntryMethod field, just returns values for its dropdown list.
This method should run before/at the time ECOGroup.GroupClosed field changes.
   OperationID: ChangeECOOprAutoReceive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprAutoReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprAutoReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprAutoReceive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprAutoReceive", {
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
   Summary: Invoke method ChangeECOOprLaborEntryMethod
   Description: Verification when changing the LaborEntryMethod field
   OperationID: ChangeECOOprLaborEntryMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprLaborEntryMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprLaborEntryMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprLaborEntryMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprLaborEntryMethod", {
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
   Summary: Invoke method ChangeECOOprOpCode
   Description: This method defaults/resets specific fields related to the new operation code.
This method should run when the ECOOpr.OpCode field changes.
   OperationID: ChangeECOOprOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprOpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprOpCode", {
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
   Summary: Invoke method ChangeECOOprOprSeq
   Description: This method will update all of the associated records to the ECOOpr if the
OprSeq field is changing.
This method should run before changing the ECOOpr.OprSeq.
   OperationID: ChangeECOOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprOprSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprOprSeq", {
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
   Summary: Invoke method ChangeECOOprOpStdID
   Description: This method defaults/resets the production standards when selecting an
Operation Standard
This method should run when the ECOOpr.OpStdID field changes.
   OperationID: ChangeECOOprOpStdID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprOpStdID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprOpStdID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprOpStdID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprOpStdID", {
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
   Summary: Invoke method ChangeECOOprPrimaryProdOpDtl
   Description: This method defaults/resets the production standards when selecting Primary
Production Operation Detail.
This method should run when the ECOOpr.PrimaryProdOpDtl field changes.
   OperationID: ChangeECOOprPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprPrimaryProdOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprPrimaryProdOpDtl", {
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
   Summary: Invoke method ChangeECOOprPrimarySetupOpDtl
   Description: This method defaults/resets the setup values when selecting Primary
Setup Operation Detail.
This method should run when the ECOOpr.PrimarySetupOpDtl field changes.
   OperationID: ChangeECOOprPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprPrimarySetupOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprPrimarySetupOpDtl", {
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
   Summary: Invoke method ChangeECOOprRestriction
   Description: This methods assigns associated fields when ECOOprRestriction.RestrictionTypeID changes.
   OperationID: ChangeECOOprRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprRestriction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprRestriction", {
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
   Summary: Invoke method ChangeECOOprRFQNeeded
   Description: This methods assigns ECOOpr.RFQVendQuotes field when ECOOpr.RFQNeeded changes.
This method should run when the ECOOpr.RFQNeeded changes.
   OperationID: ChangeECOOprRFQNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprRFQNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprRFQNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprRFQNeeded(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprRFQNeeded", {
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
   Summary: Invoke method ChangeECOOprSNRequiredOpr
   Description: Validates SNRequiredOpr flag to avoid to set it false if the prior operation has the flag set to true
The flag cannot be set to true if the part is not serial tracked also.
   OperationID: ChangeECOOprSNRequiredOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprSNRequiredOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprSNRequiredOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprSNRequiredOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprSNRequiredOpr", {
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
   Summary: Invoke method ChangeECOOprStdFormat
   Description: This methods assigns ECOOpr.OpsPerPart a default value based on the StdFormat value.
   OperationID: ChangeECOOprStdFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprStdFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprStdFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprStdFormat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprStdFormat", {
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
   Summary: Invoke method ChangeECOOprSubPartNum
   Description: This methods assigns associated fields when ECOOpr.SubPartNum changes.
This method should run when the ECOOpr.SubPartNum changes.
   OperationID: ChangeECOOprSubPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprSubPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprSubPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprSubPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprSubPartNum", {
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
   Summary: Invoke method ChangeECOOprSubstance
   Description: This methods assigns associated fields when ECOOprRestrictSubst.SubstanceID changes.
   OperationID: ChangeECOOprSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprSubstance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprSubstance", {
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
   Summary: Invoke method ChangeECOOprVendorNumVendorID
   Description: This methods assigns associated fields when ECOOpr.VendorNumVendorID changes.
This method should run when the ECOOpr.VendorNumVendorID changes.
   OperationID: ChangeECOOprVendorNumVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprVendorNumVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprVendorNumVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOOprVendorNumVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOOprVendorNumVendorID", {
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
   Summary: Invoke method ChangeECORevApproved
   Description: This methods assigns fields associated with ECORev.Approved changing.
This method should run before ECOGroup.Approved field changes.
   OperationID: ChangeECORevApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECORevApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECORevApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECORevApproved(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECORevApproved", {
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
   Summary: Invoke method ChangingECOOprAutoReceive
   Description: Verification when changing the AutoReceive field
   OperationID: ChangingECOOprAutoReceive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingECOOprAutoReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingECOOprAutoReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangingECOOprAutoReceive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangingECOOprAutoReceive", {
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
   Summary: Invoke method CheckECOMtlMtlPartNum
   Description: This methods checks the ECOMtl.MtlPartNum when it changes to see if any messages when
validating it arise.  Messages could be from the analysis code or if the user is trying to
use the parent part as a component of itself.
This method should run before changing the ECOMtl.MtlPartNum.
   OperationID: CheckECOMtlMtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlMtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlMtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOMtlMtlPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOMtlMtlPartNum", {
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
   Description: The method is to be run on drag/drop of a part.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckPrePartInfo", {
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
   Summary: Invoke method CheckChangeECOMtlMtlSeq
   Description: This method is called when ECOMtl MtlSeq is changed. It will validate the MtlSeq and, if this is not an added row,
it will delete and recreate the ECOMtl record and associated child records
   OperationID: CheckChangeECOMtlMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECOMtlMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECOMtlMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckChangeECOMtlMtlSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckChangeECOMtlMtlSeq", {
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
   Summary: Invoke method CheckChangeECOOprOprSeq
   Description: This method is called when ECOOpr OprSeq is changed. It will validate the OprSeq and, if this is not an added row,
it will delete and recreate the ECOOpr record and associated child records
   OperationID: CheckChangeECOOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECOOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECOOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckChangeECOOprOprSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckChangeECOOprOprSeq", {
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
   Summary: Invoke method ChangeECOStageStageSeq
   Description: This method is called when ECOStage StageSeq is changed. It will validate the Stage and, if this is not an added row,
it will delete and recreate the Stage record and associated child records
   OperationID: ChangeECOStageStageSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOStageStageSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOStageStageSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeECOStageStageSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ChangeECOStageStageSeq", {
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
   Summary: Invoke method CheckECOMtlMtlSeqRelatedOperation
   Description: This methods checks to see if the ECOMtl.MtlSeq has changed from the original ECOMtl.MtlSeq or
if the ECOMtl.RelatedOperation has changed from the original ECOMtl.RelatedOperation or
the ECOMtl.RelatedStage has changed from the original ECOMMtl.RelatedStage
and provides a message asking the user if they would like to set the current configuration
to unapproved if the MtlSeq, RelatedOperation or RelatedStage did change.  This method does not actually validate the
ECOMtl.MtlSeq, ECOMtl.RelatedOperation or ECOMtl.RelatedStage.
For RelatedOperation and RelatedStage, it is one or the other, i.e. both a RelatedOperation
and a RelatedStage should not be passed in.  The value to pass in is based on ECORev.UseStaging.
If this value is true, RelatedStage is used, otherwise RelatedOperation is used.
Actual validation is handle in the beforeupdate logic in a private method.
This method should run before changing the ECOMtl.MtlSeq or ECOMtl.RelatedOperation
   OperationID: CheckECOMtlMtlSeqRelatedOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlMtlSeqRelatedOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlMtlSeqRelatedOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOMtlMtlSeqRelatedOperation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOMtlMtlSeqRelatedOperation", {
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
   Summary: Invoke method CheckECOMtlPlanAsAsm
   Description: This methods checks the ECOMtl.PlanAsAsm when it changes to see if any messages when
validating it arise.  Messages could be from the analysis code
This method should run before changing the ECOMtl.PlanAsAsm.
   OperationID: CheckECOMtlPlanAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlPlanAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlPlanAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOMtlPlanAsAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOMtlPlanAsAsm", {
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
   Summary: Invoke method CheckECOMtlPullAsAsm
   Description: This methods checks the ECOMtl.PullAsAsm when it changes to see if any messages when
validating it arise.  Messages could be from the analysis code
This method should run before changing the ECOMtl.PullAsAsm.
   OperationID: CheckECOMtlPullAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlPullAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlPullAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOMtlPullAsAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOMtlPullAsAsm", {
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
   Summary: Invoke method CheckECOMtlViewAsAsm
   Description: This methods checks the ECOMtl.ViewAsAsm when it changes to see if any messages when
validating it arise. This method should run before changing the ECOMtl.ViewAsAsm.
   OperationID: CheckECOMtlViewAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlViewAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlViewAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOMtlViewAsAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOMtlViewAsAsm", {
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
   Summary: Invoke method CheckECOOprOprSeq
   Description: This methods checks to see if the ECOOpr.OprSeq has changed from the original ECOOpr.OprSeq
and provides a message asking the user if they would like to set the current configuration
to unapproved if the OprSeq did change.  This method does not actually validate the ECOOpr.OprSeq.
Actual validation is handle in the beforeupdate logic in a private method.
This method should run before changing the ECOOpr.OprSeq.
   OperationID: CheckECOOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOOprOprSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOOprOprSeq", {
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
   Summary: Invoke method CheckECOOprPrimaryProdOpDtl
   Description: This method validated the value of Primary Production Operation Detail.
This method should run when the ECOOpr.PrimaryProdOpDtl field changes.
   OperationID: CheckECOOprPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOOprPrimaryProdOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOOprPrimaryProdOpDtl", {
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
   Summary: Invoke method CheckECOOprPrimarySetupOpDtl
   Description: This method validated the value of Primary Setup Operation Detail.
This method should run when the ECOOpr.PrimarySetupOpDtl field changes.
   OperationID: CheckECOOprPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOOprPrimarySetupOpDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOOprPrimarySetupOpDtl", {
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
   Summary: Invoke method CheckECOOprPurPoint
   Description: This methods checks to see if the new ECOOpr.PurPoint has changed from the original
ECOOpr.PurPoint and validates the value.
This method should run before changing the ECOOpr.PurPoint.
   OperationID: CheckECOOprPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOOprPurPoint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOOprPurPoint", {
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
   Summary: Invoke method CheckECOOprVendorNumVendorID
   Description: This methods checks to see if the new ECOOpr.VendorNumVendorID has changed from the original
ECOOpr.VendorNumVendorID and validates the value.
This method should run before changing the ECOOpr.VendorNumVendorID.
   OperationID: CheckECOOprVendorNumVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprVendorNumVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprVendorNumVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECOOprVendorNumVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECOOprVendorNumVendorID", {
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
   Summary: Invoke method CheckECORevApproved
   Description: This methods checks if the BMSyst.VerifyPassword flag is set, and verifies a password
before the user is able to approve this revision.
This method should run before the ECORev.Approved field changes (ChangeECORevApproved).
   OperationID: CheckECORevApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECORevApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECORevApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECORevApproved(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECORevApproved", {
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
   Summary: Invoke method CheckChangeECORevApproved
   Description: This method is called when ECORev Approved flag is changed.  It will run the following methods:
CheckECORevApprovedChanging, CheckECORevApproved, ChangeECORevApproved
   OperationID: CheckChangeECORevApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECORevApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECORevApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckChangeECORevApproved(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckChangeECORevApproved", {
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
   Summary: Invoke method CheckECORevValRefDes
   Description: Verify that there are no other ECOMtlRefDes records in the revision having
the same RefDes value if the ECORev.ValRefDes = true. This method should
run before changing the ECORev.ValRefDes.
   OperationID: CheckECORevValRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECORevValRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECORevValRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECORevValRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECORevValRefDes", {
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
   Summary: Invoke method CheckECORevApprovedChanging
   Description: Verify that there are no other EcoMtl or EcoOpr records in the revision with  missing or invalid attributes
This method should run before changing the ECORev.Approved.
   OperationID: CheckECORevApprovedChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECORevApprovedChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECORevApprovedChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckECORevApprovedChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckECORevApprovedChanging", {
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
   Summary: Invoke method CheckIn
   Description: This method checks in a single revision.
This method runs the logic behind the old Vantage 6.1 Revision>Check In menu option.
   OperationID: CheckIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckIn", {
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
   Summary: Invoke method CheckInAndRefresh
   Description: Invokes CheckIn() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data.
   OperationID: CheckInAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckInAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckInAndRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckInAndRefresh", {
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
   Summary: Invoke method CheckInAll
   Description: This methods checks in all revisions within an ECOGroup and returns a results string
and returns an updated dataset if the user chooses to.
This method runs the logic behind the Vantage 6.1 Group>Check In All menu option.
   OperationID: CheckInAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckInAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckInAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckInAll", {
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
   Summary: Invoke method CheckOut
   Description: This method checks out a single revision
This method runs the logic behind the old Vantage 6.1 Revision>Check Out menu option.
   OperationID: CheckOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOut(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckOut", {
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
   Summary: Invoke method CheckOutAndRefresh
   Description: Invokes CheckOut() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data.
   OperationID: CheckOutAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOutAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOutAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOutAndRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckOutAndRefresh", {
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
   Summary: Invoke method CheckChangeECOCoPartNum
   Description: The method is called when ECOCOPart CoPartNum is changed.   It will run methods CheckPreECOCoPartInfo and ChangeECOCoPartPartNum
   OperationID: CheckChangeECOCoPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECOCoPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECOCoPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckChangeECOCoPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckChangeECOCoPartNum", {
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
   Summary: Invoke method CheckPreECOCoPartInfo
   Description: This method validates the ECOCoPart.CoPartNum is not serial tracked or a configured part.
   OperationID: CheckPreECOCoPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPreECOCoPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPreECOCoPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPreECOCoPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/CheckPreECOCoPartInfo", {
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
   Summary: Invoke method ClearAll
   Description: This method will delete all ECOMtl, ECOOpr and ECOOpDtl associated with the ECORev to clear all for.
When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: ClearAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ClearAll", {
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
   Summary: Invoke method DeleteRefDesRange
   Description: Deletes ECOMtlRefDes records based on the ECOMtl dataset fields.
   OperationID: DeleteRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRefDesRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/DeleteRefDesRange", {
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
   Summary: Invoke method ECOGroupExists
   Description: This method accepts a ECOGroup.ECOGroupID and determines if the ECOGroupID exists
as a valid record in the database.
   OperationID: ECOGroupExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECOGroupExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECOGroupExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOGroupExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupExists", {
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
   Summary: Invoke method EcoOprInitSNReqSubConShip
   Description: Method required to set the initial value of ECOOpr.SNRequiredSubConShip
   OperationID: EcoOprInitSNReqSubConShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EcoOprInitSNReqSubConShip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EcoOprInitSNReqSubConShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EcoOprInitSNReqSubConShip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EcoOprInitSNReqSubConShip", {
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
   Summary: Invoke method GetNewECORevForProcessMfg
   Description: Inserts a new ECORev row in the DataSet
   OperationID: GetNewECORevForProcessMfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECORevForProcessMfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORevForProcessMfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECORevForProcessMfg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetNewECORevForProcessMfg", {
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
   Summary: Invoke method ExportToPLM
   Description: This method accepts a ECOGroup.ECOGroupID and sends a xml message describing the ECO to PLM
   OperationID: ExportToPLM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToPLM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToPLM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportToPLM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ExportToPLM", {
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
   Summary: Invoke method ExpressPartCheckOut
   Description: This method will generate an ECOGroup for the user to check out the part to if
an ECOGroup doesn't already exist for the user.  Once the ECOGroup is properly
created, the inputted part information will be checked out to the ECOGroup that was
created or to the one that already exists for the user.
   OperationID: ExpressPartCheckOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpressPartCheckOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpressPartCheckOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpressPartCheckOut(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ExpressPartCheckOut", {
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
   Summary: Invoke method GetAvailTaskSets
   Description: This method gets the available TaskSets for the TaskSet combo in the
EngineeringWorkbenchEntry.
   OperationID: GetAvailTaskSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTaskSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTaskSets(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetAvailTaskSets", {
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
   Summary: Invoke method GetDatasetForTreeByRef
   Description: Same as GetDataSetForTree but expects ref EngWorkbenchTableset to improve performance within kinetic when merging large volumes of data.
            
This methods will return a dataset that will include PartRev, PartOpr, PartMtl and PartOpDtl if those
records exist for a ECOMtl and there is no ECORev, ECOOpr, ECOMtl and ECOOpDtl associated with it.
These added "Part" records will be able to be determined by the associated tables "IsPartRev",
"IsPartOpr", "IsPartMtl" or "IsPartOpDtl" field.  If this field is checked then the record in the dataset
was copied from the associated "part" table.  These "part" records will not be maintable as they
will not be "real" database records, just a picture of the "part" record for display purposes.
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
This method is different from the "GetRows" or "GetById" methods.  Those methods only return
maintainable "ECO" records.
   OperationID: GetDatasetForTreeByRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeByRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeByRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTreeByRef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetDatasetForTreeByRef", {
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
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartMtl and PartOpDtl if those
records exist for a ECOMtl and there is no ECORev, ECOOpr, ECOMtl and ECOOpDtl associated with it.
These added "Part" records will be able to be determined by the associated tables "IsPartRev",
"IsPartOpr", "IsPartMtl" or "IsPartOpDtl" field.  If this field is checked then the record in the dataset
was copied from the associated "part" table.  These "part" records will not be maintable as they
will not be "real" database records, just a picture of the "part" record for display purposes.
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
This method is different from the "GetRows" or "GetById" methods.  Those methods only return
maintainable "ECO" records.
   OperationID: GetDatasetForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTree(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetDatasetForTree", {
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
   Summary: Invoke method GetDetailsFromImport
   Description: This method gets the details from an import file
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>Import menu option
   OperationID: GetDetailsFromImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetailsFromImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetDetailsFromImport", {
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
   Summary: Invoke method GetDetailsFromJob
   Description: This method gets the details from a job assembly.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get From Job menu option.
   OperationID: GetDetailsFromJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetailsFromJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetDetailsFromJob", {
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
   Summary: Invoke method GetDetailsFromMethods
   Description: This method gets the details from a method.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get From Methods menu option.
   OperationID: GetDetailsFromMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromMethods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromMethods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetailsFromMethods(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetDetailsFromMethods", {
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
   Summary: Invoke method GetDetailsFromQuotes
   Description: This method gets the details from a quote assembly.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get From Quote menu option.
   OperationID: GetDetailsFromQuotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromQuotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromQuotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetailsFromQuotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetDetailsFromQuotes", {
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
   Summary: Invoke method GetDetailsOperations
   Description: This method gets the details from operations for a revision.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get Operations Details menu option.
   OperationID: GetDetailsOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetailsOperations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetDetailsOperations", {
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
   Summary: Invoke method GetECORevData
   Description: This method returns the ECOGroup record and all associated ECORev records
based on the inputted GroupID and ipCheckOutStatus (yes = checked out, no = not checked out).
In some UI cases, this method will be used to replace the base GetByID.  This method
should improve the performance because it will not be bringing back a complete
dataset.
   OperationID: GetECORevData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetECORevData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECORevData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetECORevData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetECORevData", {
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
   Summary: Invoke method GetECOGroupAndECORev
   Description: This method returns the ECOGroup record and all associated ECORev records
based on the inputted GroupID and ipCheckOutStatus (yes = checked out, no = not checked out).
In some UI cases, this method will be used to replace the base GetByID.  This method
should improve the performance because it will not be bringing back a complete
dataset.
   OperationID: GetECOGroupAndECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetECOGroupAndECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECOGroupAndECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetECOGroupAndECORev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetECOGroupAndECORev", {
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
   Summary: Invoke method GetProjectRoles
   OperationID: GetProjectRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectRoles_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProjectRoles(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GetProjectRoles", {
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
   Summary: Invoke method GroupLock
   Description: This method checks if a group doesn't have a lock and locks a group
   OperationID: GroupLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GroupLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GroupLock", {
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
   Summary: Invoke method GroupUnLock
   Description: This method deletes a lock on the group and revisions within a group.
   OperationID: GroupUnLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupUnLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupUnLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GroupUnLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/GroupUnLock", {
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
   Summary: Invoke method InsertBOMMtl
   Description: This methods allows for the insertion of an engineering material for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertBOMMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertBOMMtl", {
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
   Summary: Invoke method InsertBOMMtlWithStageNumber
   Description: This methods allows for the insertion of an engineering material for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMMtlWithStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMMtlWithStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMMtlWithStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertBOMMtlWithStageNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertBOMMtlWithStageNumber", {
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
   Summary: Invoke method InsertBOMOpr
   Description: This methods allows for the insertion of an engineering operation for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertBOMOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertBOMOpr", {
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
   Summary: Invoke method InsertBOMOprWithStageNumber
   Description: This methods allows for the insertion of an engineering operation with stage number for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMOprWithStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMOprWithStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMOprWithStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertBOMOprWithStageNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertBOMOprWithStageNumber", {
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
   Summary: Invoke method InsertMaterialDemilitedList
   Description: Method processes list of parts for drag/drop functionality,
method inserts parts which don't need a dialog and outputs list of the parts for UI dialog
   OperationID: InsertMaterialDemilitedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterialDemilitedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterialDemilitedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertMaterialDemilitedList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertMaterialDemilitedList", {
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
   Summary: Invoke method InsertMaterialWithStageNumberDemilitedList
   Description: Method processes list of parts for drag/drop functionality,
method inserts parts which don't need a dialog and outputs list of the parts for UI dialog
   OperationID: InsertMaterialWithStageNumberDemilitedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterialWithStageNumberDemilitedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterialWithStageNumberDemilitedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertMaterialWithStageNumberDemilitedList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertMaterialWithStageNumberDemilitedList", {
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
   Summary: Invoke method InsertMaterialList
   OperationID: InsertMaterialList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterialList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterialList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertMaterialList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertMaterialList", {
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
   Summary: Invoke method InsertMaterial
   Description: This methods allows for the insertion on a part for drag/drop functionality,
validates a ECORev record exists and the part is valid.
   OperationID: InsertMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertMaterial(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertMaterial", {
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
   Summary: Invoke method InsertOpDtlCapability
   Description: This method allows for the insertion of Capability on an operation to create
ECOOpDtl for drag/drop functionality.
   OperationID: InsertOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOpDtlCapability(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOpDtlCapability", {
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
   Summary: Invoke method InsertOpDtlResGroup
   Description: This method allows for the insertion of Resource Group on an operation to create
ECOOpDtl for drag/drop functionality.
   OperationID: InsertOpDtlResGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOpDtlResGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOpDtlResGroup", {
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
   Summary: Invoke method InsertOpDtlResource
   Description: This method allows for the insertion of Resource on an operation to create
ECOOpDtl for drag/drop functionality.
   OperationID: InsertOpDtlResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOpDtlResource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOpDtlResource", {
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
   Summary: Invoke method InsertOperationOP
   Description: This methods allows for the insertion on an operation for drag/drop functionality
   OperationID: InsertOperationOP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperationOP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperationOP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOperationOP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOperationOP", {
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
   Summary: Invoke method InsertOperationOPWithStageNumber
   Description: This methods allows for the insertion on an operation for drag/drop functionality
   OperationID: InsertOperationOPWithStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperationOPWithStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperationOPWithStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOperationOPWithStageNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOperationOPWithStageNumber", {
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
   Summary: Invoke method InsertOprCapability
   Description: This method allows for the insertion of Capability on a revision to create
ECOOpr/ECOOpDtl for drag/drop functionality.
   OperationID: InsertOprCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOprCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOprCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOprCapability(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOprCapability", {
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
   Summary: Invoke method InsertOprResGroup
   Description: This method allows for the insertion of ResourceGroup on a revision to create
ECOOpr/ECOOpDtl for drag/drop functionality.
   OperationID: InsertOprResGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOprResGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOprResGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOprResGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOprResGroup", {
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
   Summary: Invoke method InsertOprResource
   Description: This method allows for the insertion of Resource on a revision to create
ECOOpr/ECOOpDtl for drag/drop functionality.
   OperationID: InsertOprResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOprResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOprResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InsertOprResource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/InsertOprResource", {
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
   Summary: Invoke method LoadFileAndGetDetailsFromImport
   Description: This method loads the imported CSV and invokes GetDetailsFromImport()
   OperationID: LoadFileAndGetDetailsFromImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadFileAndGetDetailsFromImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadFileAndGetDetailsFromImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadFileAndGetDetailsFromImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/LoadFileAndGetDetailsFromImport", {
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
   Summary: Invoke method LockAll
   Description: This method locks all the revisions in a group.
This method runs the logic behind the old Vantage 6.1 Group>Lock All menu option.
   OperationID: LockAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/LockAll", {
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
   Summary: Invoke method LockAllAndRefresh
   Description: This Invokes LockAll() to lock all revisions followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: LockAllAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockAllAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockAllAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockAllAndRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/LockAllAndRefresh", {
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
   Summary: Invoke method MassAssign
   Description: This method will mass assign ECOGroup.Description, ECOGroup.ECO, and ECOGRoup.EffectiveDate
to associated ECORev records and their ECORev.RevShortDesc, ECORev.ECO, and ECORev.EffectiveDate
fields respectively.
This method will assign values based on external fields in the ECOGroup dataset.
This method should run from the menu/task "Group>Mass Assign as it was in the old
Vantage 6.1.  When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: MassAssign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAssign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAssign_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassAssign(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/MassAssign", {
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
   Summary: Invoke method MassAssignAndRefresh
   Description: Invokes MassAssign() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: MassAssignAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAssignAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAssignAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassAssignAndRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/MassAssignAndRefresh", {
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
   Summary: Invoke method PreGetDetails
   Description: This method should be called right before the GetDetailsFromMethod method.  If a configured
part is entered, and the Prompt to Get Details from Resulting Configuration is checked
in the product configurator designer, a question should be displayed to the user asking
if they want to configure the part
   OperationID: PreGetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGetDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/PreGetDetails", {
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
   Summary: Invoke method PreGetDetailsAndReturnConfigType
   Description: This method should be called right before the GetDetailsFromMethod method when you need the config type returned.  If a configured
part is entered, and the Prompt to Get Details from Resulting Configuration is checked
in the product configurator designer, a question should be displayed to the user asking
if they want to configure the part
   OperationID: PreGetDetailsAndReturnConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetailsAndReturnConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetailsAndReturnConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGetDetailsAndReturnConfigType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/PreGetDetailsAndReturnConfigType", {
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
   Summary: Invoke method PromptForPassword
   Description: This method checks the BMSyst record to see if a password should prompted for and then
validated by the ValidatePassword method in UserFile BO.  Run this before ApproveAll,
CheckECORevApproved, CheckIn, CheckInAll, and CheckOut.
   OperationID: PromptForPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptForPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PromptForPassword(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/PromptForPassword", {
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
   Summary: Invoke method ResequenceMaterials
   Description: This method will resequence the operations, update theECOMtl records.
This method should run from the menu/task "Material>Resequence" as it was in the old
Vantage 6.1.  When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: ResequenceMaterials
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceMaterials_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceMaterials_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResequenceMaterials(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ResequenceMaterials", {
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
   Summary: Invoke method ResequenceOperations
   Description: This method will resequence the operations, update the ECORev and ECOMtl records.
This method should run from the menu/task "Operation>Resequence" as it was in the old
Vantage 6.1.  When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: ResequenceOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResequenceOperations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ResequenceOperations", {
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
   Summary: Invoke method RevisionLock
   Description: This method locks a single revision
This method runs the logic behind the old Vantage 6.1 Revision>Lock Revision menu option.
   OperationID: RevisionLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RevisionLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RevisionLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/RevisionLock", {
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
   Summary: Invoke method RevisionUnLock
   Description: This method unlocks a single revision
This method runs the logic behind the old Vantage 6.1 Revision>Unlock Revision menu option.
   OperationID: RevisionUnLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RevisionUnLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionUnLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RevisionUnLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/RevisionUnLock", {
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
   Summary: Invoke method UndoCheckOut
   Description: This method undoes the check out of a revision
This method runs the logic behind the old Vantage 6.1 Revision>Undo Check Out menu option.
   OperationID: UndoCheckOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoCheckOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoCheckOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UndoCheckOut(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/UndoCheckOut", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOCOPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOCOPartRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOGroupAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOGroupListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOGroupRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOMtlAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlInspRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOMtlInspRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRefDesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOMtlRefDesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictSubstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOMtlRestrictSubstRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOMtlRestrictionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOMtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOpDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOpDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprActionParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprActionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprInspRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprInspRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprMachParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprMachParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictSubstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprRestrictSubstRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprRestrictionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECORevAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECORevRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOStageRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOStageRow[],
}

export interface Erp_Tablesets_ECOCOPartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  */  
   "CoPartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  */  
   "CoRevisionNum":string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   "PartsPerOp":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "LbrCostBase":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "MtlCostBase":number,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   "IUM":string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  If true, MRP will not generate change suggestions for the co-part  */  
   "PreventSugg":boolean,
      /**  Indicates if the parent Part should be used as the primary costing method for the co-part  */  
   "PrimaryCost":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
   "PartMasterPart":boolean,
   "ProcessMode":string,
   "EnablePreventSugg":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOGroupAttchRow{
   "Company":string,
   "GroupID":string,
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

export interface Erp_Tablesets_ECOGroupListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The text description of the ECO Group  */  
   "Description":string,
      /**  Determines if the ECO group is closed or open.  */  
   "GroupClosed":boolean,
      /**  ECO Group comments.  */  
   "CommentText":string,
      /**  Date at which this ECO Group will become effective.  */  
   "EffectiveDate":string,
      /**  Date which this ECO Group was completed.  */  
   "CompletionDate":string,
      /**  Date which this ECO group is due to be completed.  */  
   "DueDate":string,
      /**  Date which this ECO group was created.  Not maintainable by the user.  */  
   "CreatedDate":string,
      /**  UserID who created the ECO group.  Not maintainable by the user.  */  
   "CreatedBy":string,
      /**  The time (in milliseconds) that the ECO group was created.  */  
   "CreatedTime":number,
      /**  Date which this ECO group was closed.  Not maintainable by the user.  */  
   "ClosedDate":string,
      /**  UserID who closed the ECO group.  Not maintainable by the user.  */  
   "ClosedBy":string,
      /**  The time (in milliseconds) that the ECO group was closed.  */  
   "ClosedTime":number,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   "ECO":string,
      /**  Unique identifier of the task set.  */  
   "TaskSetID":string,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The Currently active milestone task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  If FALSE then revisions in this group may not be checked in.  */  
   "CheckInAllowed":boolean,
      /**  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  */  
   "PrimeSalesRepCode":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  */  
   "CheckOutAllowed":boolean,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  */  
   "SingleUser":boolean,
      /**  Indicates if this ECO Group is locked.  */  
   "GrpLocked":boolean,
      /**  UserID that has the ECOGroup record locked  */  
   "GrpLockedBy":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical to mass assign description to ecorevs  */  
   "MassAssignDesc":boolean,
      /**  Flag to mass assign ECO to ecorevs  */  
   "MassAssignECO":boolean,
      /**  Flag to mass assign effective date across ecorevs  */  
   "MassAssignEffectiveDate":boolean,
      /**  Flag if Approve All is allowed for this group.  */  
   "CanApproveAll":boolean,
      /**  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  */  
   "MultiBOMAllowed":boolean,
      /**  Flag if Check In All is allowed for this group  */  
   "CanCheckInAll":boolean,
      /**  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  */  
   "WFGroupIDDesc":string,
      /**  If true use method for all parts in tree, otherwise use the part's default method  */  
   "UseMethodForPartsInTree":boolean,
   "CurrentWFStageDesc":string,
      /**  Used for enable/disable the check in all option.  */  
   "EnableCheckInAll":boolean,
      /**  Description of the task set.  */  
   "TaskSetIDTaskSetDescription":string,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   "TaskSetIDWorkflowType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOGroupRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The text description of the ECO Group  */  
   "Description":string,
      /**  Determines if the ECO group is closed or open.  */  
   "GroupClosed":boolean,
      /**  ECO Group comments.  */  
   "CommentText":string,
      /**  Date at which this ECO Group will become effective.  */  
   "EffectiveDate":string,
      /**  Date which this ECO Group was completed.  */  
   "CompletionDate":string,
      /**  Date which this ECO group is due to be completed.  */  
   "DueDate":string,
      /**  Date which this ECO group was created.  Not maintainable by the user.  */  
   "CreatedDate":string,
      /**  UserID who created the ECO group.  Not maintainable by the user.  */  
   "CreatedBy":string,
      /**  The time (in milliseconds) that the ECO group was created.  */  
   "CreatedTime":number,
      /**  Date which this ECO group was closed.  Not maintainable by the user.  */  
   "ClosedDate":string,
      /**  UserID who closed the ECO group.  Not maintainable by the user.  */  
   "ClosedBy":string,
      /**  The time (in milliseconds) that the ECO group was closed.  */  
   "ClosedTime":number,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   "ECO":string,
      /**  Unique identifier of the task set.  */  
   "TaskSetID":string,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The Currently active milestone task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  If FALSE then revisions in this group may not be checked in.  */  
   "CheckInAllowed":boolean,
      /**  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  */  
   "PrimeSalesRepCode":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  */  
   "CheckOutAllowed":boolean,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  */  
   "SingleUser":boolean,
      /**  Indicates if this ECO Group is locked.  */  
   "GrpLocked":boolean,
      /**  UserID that has the ECOGroup record locked  */  
   "GrpLockedBy":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical to mass assign description to ecorevs  */  
   "MassAssignDesc":boolean,
      /**  Flag to mass assign ECO to ecorevs  */  
   "MassAssignECO":boolean,
      /**  Flag to mass assign effective date across ecorevs  */  
   "MassAssignEffectiveDate":boolean,
      /**  Flag if Approve All is allowed for this group.  */  
   "CanApproveAll":boolean,
      /**  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  */  
   "MultiBOMAllowed":boolean,
      /**  Flag if Check In All is allowed for this group  */  
   "CanCheckInAll":boolean,
      /**  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  */  
   "WFGroupIDDesc":string,
      /**  If true use method for all parts in tree, otherwise use the part's default method  */  
   "UseMethodForPartsInTree":boolean,
   "CurrentWFStageDesc":string,
      /**  Used for enable/disable the check in all option.  */  
   "EnableCheckInAll":boolean,
   "BitFlag":number,
   "TaskSetIDWorkflowType":string,
   "TaskSetIDTaskSetDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOImportRow{
      /**  The part number.  */  
   "PartNum":string,
      /**  The description of the part number.  */  
   "PartDescription":string,
      /**  The type code.  */  
   "TypeCode":string,
      /**  The quantity per.  */  
   "QtyPer":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOMtlAttchRow{
   "Company":string,
   "GroupID":string,
   "PartNum":string,
   "RevisionNum":string,
   "AltMethod":string,
   "ProcessMfgID":string,
   "MtlSeq":number,
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

export interface Erp_Tablesets_ECOMtlInspRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  Parent Part number to which this material item is a component of  */  
   "PartNum":string,
      /**  Revision number of the part that this material item is a component of.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  */  
   "MtlSeq":number,
      /**  A sequence number that uniquely identifies the ECOMtlInsp record within the ECO material  */  
   "PlanSeq":number,
      /**  The inspection plan part number (configurator part number).  */  
   "InspPlanPartNum":string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   "SpecID":string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   "OrigMtlSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
   "SpecHedDescription":string,
   "BitFlag":number,
   "InspPlanDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOMtlRefDesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  Identifier of Reference Designator  */  
   "RefDes":string,
      /**  Unique identifies the reference designator with the material sequence.  */  
   "RefDesSeq":number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   "MtlPartNum":string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   "OrigMtlSeq":number,
      /**  Free form side location. (Top, Bottom, Both, Level, etc)  */  
   "Side":string,
      /**  X Coordinate of the reference designator  */  
   "XLocation":number,
      /**  Y Coordinate of the reference designator  */  
   "YLocation":number,
      /**  Z Coordinate of the reference designator  */  
   "ZLocation":number,
      /**  Rotation of the reference designator. Max value = 360.000  */  
   "Rotation":number,
      /**  Designator Description  */  
   "Description":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOMtlRestrictSubstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  Substance identification.  */  
   "SubstanceID":string,
      /**  Default weight of the substance per primary part of UOM  */  
   "Weight":number,
      /**  By default the primary UOM of the part.  */  
   "WeightUOM":string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   "OrigMtlSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
   "Exempt":boolean,
   "ExemptDate":string,
   "ExemptCertificate":string,
   "Manual":boolean,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   "MtlPartNum":string,
   "BitFlag":number,
   "GroupIDDescription":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "RestrictionDescription":string,
   "RevisionNumRevDescription":string,
   "RevisionNumPartDescription":string,
   "RevisionNumRevShortDesc":string,
   "SubstanceDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOMtlRestrictionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   "MtlPartNum":string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   "OrigMtlSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Yes to display when the part has no net weight or when one or more of the selected has no weight.  */  
   "Weight":boolean,
   "Manual":boolean,
   "ComplianceDate":string,
   "LastRollUp":string,
   "RollUpType":string,
   "BitFlag":number,
   "GroupIDDescription":string,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumIUM":string,
   "RestrictionDescription":string,
   "RevisionNumRevShortDesc":string,
   "RevisionNumPartDescription":string,
   "RevisionNumRevDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOMtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Parent Part number to which this material item is a component of  */  
   "PartNum":string,
      /**  Revision number of the part that this material item is a component of.  */  
   "RevisionNum":string,
      /**  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  */  
   "MtlSeq":number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   "MtlPartNum":string,
      /**  Quantity Per Parent  */  
   "QtyPer":number,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   "FixedQty":boolean,
      /**   A material record can be related to a specific operation. This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job. The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   "RelatedOperation":number,
      /**  Part number for Salvageable scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  */  
   "SalvagePartNum":string,
      /**  Description of Salvageable material. Use Part.Description for a default.  */  
   "SalvageDescription":string,
      /**  A factor that multiplied by the QtyPer results in the expected total salvage quantity.  */  
   "SalvageQtyPer":number,
      /**  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  */  
   "SalvageUM":string,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   "SalvageUnitCredit":number,
      /**  Material comments specific to this manufacturing process. These comments copied to Jobs/Quotes when pulled from BOM.  */  
   "MfgComment":string,
      /**  Indicates if these comments should override the comments defined in the part master. It controls how the MfgComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.MfgComments will be appended on to the Part.MfgComments when written to the Job/Quote material record.  */  
   "OverRideMfgComments":boolean,
      /**   Material comments specific to a manufacturing process. These comments (and optionally the comments from Part Master) are  copied to Jobs/Quotes when the BOM is pulled.
( See OverRidePurComments )  */  
   "PurComment":string,
      /**  Indicates if these comments should override the comments defined in the part master. It controls how the PurComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.PurComments will be appended on to the Part.PurComments when written to the Job/Quote material record.  */  
   "OverRidePurComments":boolean,
      /**  Estimated Scrap  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   "EstScrapType":string,
      /**  This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly should be pulled from stock or manufactured as part of the job it is pulled into. If PullAsAsm = No only the assembly record will be pulled into the job/quote (as a material), the related material and operations will not be pulled over.  */  
   "PullAsAsm":boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   "FindNum":string,
      /**   This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly when shown in ABOM indented views or on reports it should be shown either as a subassembly or material requirement.  If Yes then the assemblies components will be shown else it is shown as a single material requirement line. Similar to the PullAsAsm flag however this is used to control how subassemblies appear in the ABOM module.
NOTE: AS OF 2.70.400 this function is not implemented.  Pending further analysis. It has been added to the schema to make it easier to implement when decision has been reached.  */  
   "ViewAsAsm":boolean,
      /**  Indicates which APS Scheduler module the assembly is scheduled in.  */  
   "APSSchedulerName":string,
      /**  APS Start Limit date.  Prevents APS from scheduling before this date.  */  
   "APSSLDate":string,
      /**  APS Start Limit time.  Time, in decimal hours, that APS will not schedule before.  Only valid if APSSLDate is valid.  */  
   "APSSLTime":number,
      /**  Schedule direction.  Valid options are: F=Forward, B=Backward, C=dynamic Constraint based, W=minimum WIP, E=End of work, S=Split longest duration, X=use the direction specified in task entry in APS.  */  
   "APSInsertDirection":string,
      /**  Method of insertion into schedule.  Valid values are: T=best Time, G=same Group, N=uNscheduled, F=Force Insert, I=without resource assignment.  */  
   "APSInsertCriteria":string,
      /**  Used to calculated setup time during optimization.  */  
   "APSAttrib1":number,
      /**  Used to calculated setup time during optimization.  */  
   "APSAttrib2":number,
      /**  Used to calculated setup time during optimization.  */  
   "APSAttrib3":number,
      /**  Used to calculated setup time during optimization.  */  
   "APSAttrib4":number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   "APSAddResType":string,
      /**  The salvage material burden rate for this Part Material.  */  
   "SalvageMtlBurRate":number,
      /**  Estimated salvage Mtl Burden Unit Credit.  */  
   "SalvageEstMtlBurUnitCredit":number,
      /**  The material burden rate for this Part Material.  */  
   "MtlBurRate":number,
      /**  Estimated Mtl Burden Unit Cost.  */  
   "EstMtlBurUnitCost":number,
      /**  A flag to indicate that this part material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this part material.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The original material sequence number from the PartMtl record at the time of check out. If this record was not created during check out this should remain 0.  */  
   "OrigMtlSeq":number,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  A material record can be related to a specific operation by stage. This field contains the StageNumber of the operation that it is related to.  */  
   "RelatedStage":string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   "BaseMethodOverridden":boolean,
      /**  Parent Alternate Routing method for the part material.  */  
   "ParentAltMethod":string,
      /**  Indicates the parent material sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   "ParentMtlSeq":number,
      /**   Unit of Measure code of the Material requirement.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "UOMCode":string,
      /**  Material Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Rule Tag. Used in the configurator.  */  
   "RuleTag":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  This is relevant for assemblies (Part.Method = Yes). Indicates if the sub-assemby can be spawned off to a different job.  Can be true only if PullAsAsm = true.  */  
   "PlanAsAsm":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   "ReassignSNAsm":boolean,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   "LocationView":boolean,
      /**  Weight Measurement  */  
   "CNWeightMeasurement":boolean,
      /**  Required Quantity  */  
   "CNRequiredQty":number,
      /**  Consumed Quantity  */  
   "CNConsumedQty":number,
      /**  UOM  */  
   "CNUOM":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "MtlAttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvageAttributeSetID":number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   "SalvagePlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvagePlanningAttributeSetID":number,
      /**  Planning Percent  */  
   "PlanningPct":number,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "MtlRevisionNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "SalvageRevisionNum":string,
      /**  The user's response to potential question for analysis code on mtlpartnum validation.  */  
   "AnswerMtlPartNumQuestion":boolean,
      /**  Attrition Rate  */  
   "CNAttritionRate":number,
      /**  Used to Enable Part Inspection fields on UI  */  
   "EnablePartInsp":boolean,
      /**  Should pullasasm be enabled on the UI?  */  
   "EnablePullAsAsm":boolean,
      /**  Should viewasasm be enabled on the UI?  */  
   "EnableViewAsAsm":boolean,
   "ExpandTree":boolean,
      /**  Is this a PartMtl record?  Used for build of tree to display PartMtl as ECOMtl.  */  
   "IsPartMtl":boolean,
      /**  A boolean value to determine if the Material is the Top part sales kit  */  
   "IsTopPartSalesKit":boolean,
      /**  Used to enter comments for manufacturing when this part is referenced on a job.  */  
   "MtlPartNumMfgComment":string,
      /**  Part Comments that will be used as a default for purchasing.  */  
   "MtlPartNumPurComment":string,
      /**  Is there a revision for the MtlPartNum component of the parent partnum?  */  
   "MtlRevExists":boolean,
      /**  The related operation description  */  
   "OpDesc":string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
   "RelatedECOOprOprSeq":number,
      /**  Salvage Base Unit of Measure  */  
   "SalvageBaseUOM":string,
      /**  Salvage Part Number Track Multi UOM  */  
   "SalvagePartTrackMulti":boolean,
      /**  The value of ecorev.usestaging for UI purposes.  */  
   "UseStaging":boolean,
      /**  The user's response to potential question for analysis code on planasasm validation.  */  
   "AnswerPlanAsAsmQuestion":boolean,
      /**  The user's response to potential question for analysis code on pullasasm validation.  */  
   "AnswerPullAsAsmQuestion":boolean,
      /**  The display unit of measure for the qty/parent field.  */  
   "DspUnitMeasure":string,
      /**  External field used to control the flag over the FixedQty field on UI screens.  */  
   "EnableFixedQty":boolean,
   "EnableAttributeSetSearch":boolean,
   "SalvEnableAttSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "PlanningNumberOfPiecesDisp":number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "SalvagePlanningNumberOfPiecesDisp":number,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "APSSchedulerNameAPSSchedulerName":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "GroupIDDescription":string,
   "MtlPartNumTrackInventoryByRevision":boolean,
   "MtlPartNumAttrClassID":string,
   "MtlPartNumTrackInventoryAttributes":boolean,
   "MtlPartNumTrackLots":boolean,
   "MtlPartNumTrackDimension":boolean,
   "MtlPartNumSellingFactor":number,
   "MtlPartNumIUM":string,
   "MtlPartNumPricePerCode":string,
   "MtlPartNumTrackSerialNum":boolean,
   "MtlPartNumPartDescription":string,
   "MtlPartNumSalesUM":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "RevisionNumPartDescription":string,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "SalvagePartNumTrackInventoryByRevision":boolean,
   "SalvagePartNumPricePerCode":string,
   "SalvagePartNumSalesUM":string,
   "SalvagePartNumTrackDimension":boolean,
   "SalvagePartNumPartDescription":string,
   "SalvagePartNumTrackLots":boolean,
   "SalvagePartNumIUM":string,
   "SalvagePartNumSellingFactor":number,
   "SalvagePartNumAttrClassID":string,
   "SalvagePartNumTrackInventoryAttributes":boolean,
   "SalvagePartNumTrackSerialNum":boolean,
   "SalvDynAttrValueSetShortDescription":string,
   "SalvDynAttrValueSetDescription":string,
   "StageNoDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOpDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   "OpDtlSeq":number,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   "CapabilityID":string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  */  
   "ResourceID":string,
      /**  The standard setup hours for the operation.   This is the setup time required for each machine.  */  
   "SetupHours":number,
      /**  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  */  
   "ProdHours":number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   "NumResources":number,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   "SetupOrProd":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  Description is initially created when the ECOOpDtl is created.   If the ECOOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "OpDtlDesc":string,
      /**  Parent Alternate Routing method of this part operation.  */  
   "ParentAltMethod":string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   "ParentOprSeq":number,
      /**  Indicates the parent operation detail sequence.  */  
   "ParentOpDtlSeq":number,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   "BaseMethodOverridden":boolean,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOpDtlSeq":number,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOprSeq":number,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   "ConcurrentCapacity":number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   "DailyProdRate":number,
      /**  Duplicated from ECOOpr.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  Duplicated from ECOOpr.SetupCrewSize. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Indicates if primary production operation.  */  
   "PrimaryProd":boolean,
      /**  Indicates if primary setup operation.  */  
   "PrimarySetup":boolean,
      /**  Capability description  */  
   "CapabilityDesc":string,
      /**  Resource description  */  
   "ResourceDesc":string,
      /**  Resource Group description  */  
   "ResourceGrpDesc":string,
      /**  Is this a PartOpDtl?  Used when building the tree to show PartOpDtl as ECOOpDtl.  */  
   "IsPartOpDtl":boolean,
      /**  Flag for sub contract  */  
   "SubContract":boolean,
   "BitFlag":number,
   "CapabilityIDDescription":string,
   "GroupIDDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "RevisionNumRevShortDesc":string,
   "RevisionNumRevDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprActionParamRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   "GroupID":string,
      /**  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part or process manufacture.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  The ID of Process Manufacturing revision.  */  
   "ProcessMfgID":string,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   "OprSeq":number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  A sequence number which uniquely identifies parameter within the Operation/Action set.  */  
   "ActionParamSeq":number,
      /**  Data type of Action Parameter  */  
   "ActionParamFieldDataType":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueCharacter":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueDate":string,
      /**  Value of Action Parameter.  */  
   "ActionParamValueDecimal":number,
      /**  Value of Action Parameter.  */  
   "ActionParamValueInteger":number,
      /**  Value of Action Parameter.  */  
   "ActionParamValueLogical":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprActionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   "GroupID":string,
      /**  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part or process manufacture.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  The ID of Process Manufacturing revision.  */  
   "ProcessMfgID":string,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   "OprSeq":number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  Description of Action.  */  
   "ActionDesc":string,
      /**  Indicated if this action must be completed before Operation can be completed.  */  
   "Required":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprAttchRow{
   "Company":string,
   "GroupID":string,
   "PartNum":string,
   "RevisionNum":string,
   "AltMethod":string,
   "ProcessMfgID":string,
   "OprSeq":number,
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

export interface Erp_Tablesets_ECOOprInspRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  Parent Part number to which this material item is a component of  */  
   "PartNum":string,
      /**  Revision number of the part that this material item is a component of.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  A sequence number that uniquely identifies the ECOOprInsp ecord within the ECO operation  */  
   "PlanSeq":number,
      /**  The inspection plan part number (configurator part number).  */  
   "InspPlanPartNum":string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   "SpecID":string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOprSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
   "SpecHedDescription":string,
   "BitFlag":number,
   "InspPlanDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprMachParamRow{
      /**  Company  */  
   "Company":string,
      /**  GroupID  */  
   "GroupID":string,
      /**  PartNum  */  
   "PartNum":string,
      /**  RevisionNum  */  
   "RevisionNum":string,
      /**  AltMethod  */  
   "AltMethod":string,
      /**  OprSeq  */  
   "OprSeq":number,
      /**  MachParamSeq  */  
   "MachParamSeq":number,
      /**  RequestCode  */  
   "RequestCode":string,
      /**  MachineNum  */  
   "MachineNum":string,
      /**  ToolNum  */  
   "ToolNum":string,
      /**  ParamNum  */  
   "ParamNum":number,
      /**  ParamUpperLimit  */  
   "ParamUpperLimit":number,
      /**  ParamNominalValue  */  
   "ParamNominalValue":number,
      /**  ParamLowerLimit  */  
   "ParamLowerLimit":number,
      /**  ParamDelayValue  */  
   "ParamDelayValue":number,
      /**  SpecEnable  */  
   "SpecEnable":boolean,
      /**  SpecControlAlarm  */  
   "SpecControlAlarm":boolean,
      /**  SpecRunAlarm  */  
   "SpecRunAlarm":boolean,
      /**  ProcSpecAlarm  */  
   "ProcSpecAlarm":boolean,
      /**  ProcControlAlarm  */  
   "ProcControlAlarm":boolean,
      /**  PartQualSpecEnable  */  
   "PartQualSpecEnable":boolean,
      /**  PartQualControlEnable  */  
   "PartQualControlEnable":boolean,
      /**  OrigOprSeq  */  
   "OrigOprSeq":number,
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
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprRestrictSubstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "OprSeq":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  Substance identification.  */  
   "SubstanceID":string,
      /**  Defaulted from Operation Master Substances.  */  
   "Weight":number,
      /**  Defaulted from Operation Master Substances.  */  
   "WeightUOM":string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOprSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
   "Exempt":boolean,
   "ExemptDate":string,
   "ExemptCertificate":string,
   "Manual":boolean,
   "BitFlag":number,
   "GroupIDDescription":string,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "RestrictionDescription":string,
   "RevisionNumRevShortDesc":string,
   "RevisionNumRevDescription":string,
   "RevisionNumPartDescription":string,
   "SubstanceDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprRestrictionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  Restriction Type identification.  */  
   "RestrictionTypeID":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "OpCode":string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOprSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Yes to display when the part has no net weight or when one or more of the selected has no weight.  */  
   "Weight":boolean,
   "Manual":boolean,
   "ComplianceDate":string,
   "BitFlag":number,
   "GroupIDDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "RestrictionDescription":string,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "RevisionNumPartDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   "OpStdID":string,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   "EstSetHours":number,
      /**   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  */  
   "EstProdHours":number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  Production Quantity per one of the Parent Item.  */  
   "QtyPer":number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   "Machines":number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  Estimated Scrap  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Inventory UOM  */  
   "IUM":string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  Hours required is calculated as days * 8.  */  
   "DaysOut":number,
      /**  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  */  
   "SubPartNum":string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Editor widget for Job operation comments.  */  
   "CommentText":string,
      /**   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   "SchedRelation":string,
      /**  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   "RunQty":number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  */  
   "AddlSetupHours":number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   "AddlSetUpQty":number,
      /**  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  */  
   "APSPrepOp":number,
      /**  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  */  
   "APSNextOp":number,
      /**  Specifies the operation for which this is an alternate.  */  
   "APSAltOp":number,
      /**  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  */  
   "APSSpecificResource":string,
      /**   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  */  
   "APSCycleTime":number,
      /**   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  */  
   "APSConstantTime":number,
      /**  Used to group operations to save on setups.  */  
   "APSSetupGroup":number,
      /**  Quantity of Part per cycle.  */  
   "APSMakeFactor":number,
      /**  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  */  
   "APSContainerSize":number,
      /**  Name of the APS Scheduler Module in which to schedule this operation.  */  
   "APSSchedulerName":string,
      /**  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  */  
   "APSMaxLength":number,
      /**  Time between the end of this operation and the start time of the successor operation.  */  
   "APSTransferTime":number,
      /**  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  */  
   "APSEffectiveness":number,
      /**  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  */  
   "APSOperationClass":string,
      /**  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  */  
   "APSAuxResource":string,
      /**  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  */  
   "APSAddResource":string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  The quantity requested for first article inspection.  */  
   "FAQty":number,
      /**  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOprSeq":number,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  */  
   "PrimarySetupOpDtl":number,
      /**   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  */  
   "PrimaryProdOpDtl":number,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  Operation Description.  */  
   "OpDesc":string,
      /**  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  */  
   "StageNumber":string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   "BaseMethodOverridden":boolean,
      /**  Parent Alternate Routing method of this part operation.  */  
   "ParentAltMethod":string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   "ParentOprSeq":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty01":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty02":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty03":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty04":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty05":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty06":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty07":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty08":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty09":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty10":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost01":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost02":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost03":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost04":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost05":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost06":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost07":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost08":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost09":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost10":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate01":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate02":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate03":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate04":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate05":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate06":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate07":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate08":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate09":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate10":number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   "SNRequiredOpr":boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   "SNRequiredSubConShip":boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   "SendAheadType":string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   "SendAheadOffset":number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   "PrjRoleList":string,
      /**  Allow use all Roles  */  
   "UseAllRoles":boolean,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  PctReg  */  
   "PctReg":number,
      /**  SetupMaterial  */  
   "SetupMaterial":number,
      /**  MaterialColorRating  */  
   "MaterialColorRating":number,
      /**  MiscInfo1  */  
   "MiscInfo1":string,
      /**  MiscInfo2  */  
   "MiscInfo2":string,
      /**  SetupURL  */  
   "SetupURL":string,
      /**  ExpPctUp  */  
   "ExpPctUp":number,
      /**  ExpCycTm  */  
   "ExpCycTm":number,
      /**  ExpGood  */  
   "ExpGood":number,
      /**  NonProdLimit  */  
   "NonProdLimit":number,
      /**  AutoSpcEnable  */  
   "AutoSpcEnable":boolean,
      /**  AutoSpcPeriod  */  
   "AutoSpcPeriod":number,
      /**  PartQualEnable  */  
   "PartQualEnable":boolean,
      /**  AutoSpcSubgroup  */  
   "AutoSpcSubgroup":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PulsesPerCycle  */  
   "PulsesPerCycle":number,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  TemplateID  */  
   "TemplateID":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "SubRevisionNum":string,
      /**  The vendor's name and bill to address  */  
   "DspBillAddr":string,
      /**  Field used to control the flag on SNRequiredSubConShip field on UI screens.  */  
   "EnableSNReqSubConShip":boolean,
      /**  Used as a flag to enable controls on UI screens  */  
   "EnableSNRequiredOpr":boolean,
      /**  The final operation field  */  
   "FinalOpr":boolean,
      /**  Flag to let you know if you have price breaks.  */  
   "HasPriceBreaks":boolean,
      /**  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  */  
   "IsPartOpr":boolean,
      /**  The original or old OprSeq.  Used when changing the OprSeq.  */  
   "OldOprSeq":number,
   "OpStdDescription":string,
      /**  PML ID  */  
   "PLMChar03":string,
      /**  Primary Resource Group description  */  
   "PrimaryResourceGrpDesc":string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   "PrimaryResourceGrpID":string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   "RefreshResources":boolean,
      /**  The setup hours per machines.  */  
   "SetHoursPerMach":number,
      /**  The standard format description.  */  
   "StdFrmtDesc":string,
      /**  The value of the ecorev.usestaging field for UI purposes  */  
   "UseStaging":boolean,
      /**  The auto receive field  */  
   "AutoReceive":boolean,
   "EnableAttributeSetSearch":boolean,
   "PrimaryProdOpDtlDesc":string,
   "PrimarySetupOpDtlDesc":string,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "APSSchedulerNameAPSSchedulerName":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "GroupIDDescription":string,
   "OpCodeOpDesc":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PrimaryProdOpDtlOpDtlDesc":string,
   "PrimarySetupOpDtlOpDtlDesc":string,
   "RevisionNumRevShortDesc":string,
   "RevisionNumRevDescription":string,
   "RevisionNumPartDescription":string,
   "SetupGroupDescription":string,
   "StageNoDescription":string,
   "SubPartNumTrackInventoryAttributes":boolean,
   "SubPartNumPricePerCode":string,
   "SubPartNumTrackDimension":boolean,
   "SubPartNumTrackSerialNum":boolean,
   "SubPartNumSellingFactor":number,
   "SubPartNumTrackLots":boolean,
   "SubPartNumSalesUM":string,
   "SubPartNumPartDescription":string,
   "SubPartNumIUM":string,
   "SubPartNumAttrClassID":string,
   "SubPartNumTrackInventoryByRevision":boolean,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumName":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumCountry":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECORevAttchRow{
   "Company":string,
   "GroupID":string,
   "PartNum":string,
   "RevisionNum":string,
   "AltMethod":string,
   "ProcessMfgID":string,
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

export interface Erp_Tablesets_ECORevRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   "RevShortDesc":string,
      /**  Used to enter a full description of the revision.  */  
   "RevDescription":string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   "Approved":boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   "EffectiveDate":string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRSetupBurdenCost":number,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   "ECO":string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  */  
   "CheckInRevisionNum":string,
      /**  The date that the revision is checked in.  */  
   "CheckInDate":string,
      /**  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  */  
   "CheckedOut":boolean,
      /**  The date that the Part-Rev was last checked out to the group.  */  
   "CheckOutDate":string,
      /**  UserID who checked out the revision.  Not maintainable by the user.  */  
   "CheckedOutBy":string,
      /**  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   "SearchWord":string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   "PartDescription":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  Indicates if this ECO Revision is locked.  */  
   "RevLocked":boolean,
      /**  UserID that has the ECORev record locked.  */  
   "RevLockedBy":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The alternate method of the parent this method inherits from.  */  
   "ParentAltMethod":string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   "UseStaging":boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   "UseAltRevForParts":boolean,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  */  
   "ProcessMode":string,
      /**  AltMethodDesc  */  
   "AltMethodDesc":string,
      /**  Customs Item Number  */  
   "CNCustomsItemNum":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  */  
   "ProcessMfgType":string,
      /**  Description of Process Manufacturing revision.  */  
   "ProcessMfgDescription":string,
      /**  ID of Revision Image.  */  
   "ImageID":string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   "UseAdvancedStaging":boolean,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   "ECPCEnabled":boolean,
   "Configured":boolean,
      /**  Should the GetDetails menu options be enabled?  */  
   "EnableGetDetails":boolean,
      /**  Should the UnLock menu option be enabled?  */  
   "EnableUnLock":boolean,
      /**  Is the revision updateable?  Used for menu options.  */  
   "EnableUpdateable":boolean,
   "HasCoParts":boolean,
      /**  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  */  
   "IsPartRev":boolean,
      /**  Should the Lock menu option be enabled?  */  
   "EnableLock":boolean,
      /**  Handbook Line  */  
   "CNHandbookLine":string,
   "CNHandbookCode":string,
   "CNCustomsBOM":boolean,
   "isFromPartRevision":boolean,
      /**  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  */  
   "AltMethodDisplay":string,
   "BitFlag":number,
   "GroupIDDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumTypeCode":string,
   "PartRevCreatedBy":string,
   "PartRevCreatedOn":string,
   "PartRevApproved":boolean,
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOStageRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   "GroupID":string,
      /**  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part or process manufacture.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  The ID of Process Manufacturing revision.  */  
   "ProcessMfgID":string,
      /**  A sequence number which uniquely identifies stage record within the stage set.  */  
   "StageSeq":number,
      /**  The identification of related StageNo.  */  
   "StageNumber":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  High-level descriptions of General Requirements for Stage.  */  
   "GeneralRequirements":string,
   "BitFlag":number,
   "StageNumberDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipMtlSeq
      @param ipPrefix
      @param ipStartNum
      @param ipEndNum
      @param ipSuffix
      @param ds
   */  
export interface AddRefDesRange_input{
      /**  The Group ID of ECO revision  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision  */  
   ipPartNum:string,
      /**  The ECO Revision Number  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID  */  
   ipProcessMfgID:string,
      /**  The ECO Material Seq  */  
   ipMtlSeq:number,
      /**  The Prefix to be used to create Reference Designators  */  
   ipPrefix:string,
      /**  The Starting Number to create Reference Designators  */  
   ipStartNum:number,
      /**  The Ending Number to create Reference Designators  */  
   ipEndNum:number,
      /**  The Suffix to be used to create Reference Designators  */  
   ipSuffix:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface AddRefDesRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

export interface AllowApproveMethod_output{
}

export interface AllowUnapproveMethod_output{
}

   /** Required : 
      @param ipGroupID
      @param ipValidPassword
   */  
export interface ApproveAllAndRefresh_input{
      /**  The ECOGroup.GroupID to approve all for  */  
   ipGroupID:string,
      /**  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  */  
   ipValidPassword:boolean,
}

export interface ApproveAllAndRefresh_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opResultString:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ipValidPassword
   */  
export interface ApproveAll_input{
      /**  The ECOGroup.GroupID to approve all for  */  
   ipGroupID:string,
      /**  Used for GetDatasetForTree, The Part Number to return data for.  */  
   ipPartNum:string,
      /**  Used for GetDatasetForTree, The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  Used for GetDatasetForTree, The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
      /**  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  */  
   ipValidPassword:boolean,
}

export interface ApproveAll_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opResultString:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ipValidPassword
      @param ipAuditText
   */  
export interface ApproveAndCheckInAll_input{
      /**  The ECOGroup.GroupID to approve all for  */  
   ipGroupID:string,
      /**  Used for GetDatasetForTree, The Part Number to return data for.  */  
   ipPartNum:string,
      /**  Used for GetDatasetForTree, The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  Used for GetDatasetForTree, The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false use the part's default method.  */  
   ipUseMethodForParts:boolean,
      /**  Did the user supply a valid password to run this functionality?  The value for this parameter should come from running the ValidatePassword method in the UserFile BO.  */  
   ipValidPassword:boolean,
      /**  The text to write to the audit record(s).  */  
   ipAuditText:string,
}

export interface ApproveAndCheckInAll_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opResultString:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOCoPartPartNum_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOCoPartPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedGroupClosed
      @param ds
   */  
export interface ChangeECOGroupGroupClosed_input{
      /**  The new proposed ECOGroup.GroupClosed value  */  
   ipProposedGroupClosed:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOGroupGroupClosed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedWFGroupID
      @param ds
   */  
export interface ChangeECOGroupWorkflowGroup_input{
      /**  The new proposed ECOGroup.WFGroupID value  */  
   ipProposedWFGroupID:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOGroupWorkflowGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedFixedQty
      @param ds
   */  
export interface ChangeECOMtlFixedQty_input{
      /**  The new proposed ECOMtl.FixedQty value  */  
   ipProposedFixedQty:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlFixedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlMtlPartNum_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlMtlPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedMtlSeq
      @param ds
   */  
export interface ChangeECOMtlMtlSeq_input{
      /**  The new proposed ECOMtl.MtlSeq value  */  
   ipProposedMtlSeq:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlMtlSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlPlanAsAsm_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlPlanAsAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlPullAsAsm_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlPullAsAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlQtyPer_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlQtyPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedRFQNeeded
      @param ds
   */  
export interface ChangeECOMtlRFQNeeded_input{
      /**  The new proposed ECOMtl.RFQNeeded value  */  
   ipProposedRFQNeeded:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlRFQNeeded_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param proposedReassignSNAsm
      @param ds
   */  
export interface ChangeECOMtlReassignSNAsm_input{
      /**  Proposed value for Reassign SN Asm  */  
   proposedReassignSNAsm:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlReassignSNAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedRelatedOperation
      @param ds
   */  
export interface ChangeECOMtlRelatedOperation_input{
      /**  The new proposed ECOMtl.RFQNeeded value  */  
   ipProposedRelatedOperation:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlRelatedOperation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedRelatedStage
      @param ds
   */  
export interface ChangeECOMtlRelatedStage_input{
      /**  The new proposed ECOMtl.RFQNeeded value  */  
   ipProposedRelatedStage:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlRelatedStage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlReqRefDes_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlReqRefDes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlRestriction_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedSalvageMtlBurRate
      @param ds
   */  
export interface ChangeECOMtlSalvageMtlBurRate_input{
      /**  The new proposed ECOMtl.SalvageMtlBurRate value  */  
   ipProposedSalvageMtlBurRate:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlSalvageMtlBurRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedSalvagePartNum
      @param ds
   */  
export interface ChangeECOMtlSalvagePartNum_input{
      /**  The new proposed ECOMtl.SalvagePartNum value  */  
   ipProposedSalvagePartNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlSalvagePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlSalvageQtyPer_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlSalvageQtyPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlSalvageUM_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlSalvageUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedSalvageUnitCredit
      @param ds
   */  
export interface ChangeECOMtlSalvageUnitCredit_input{
      /**  The new proposed ECOMtl.SalvageUnitCredit value  */  
   ipProposedSalvageUnitCredit:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlSalvageUnitCredit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOMtlSubstance_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOMtlSubstance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param proposedCapID
      @param ds
   */  
export interface ChangeECOOpDtlCapability_input{
      /**  The proposed Capability ID  */  
   proposedCapID:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOpDtlCapability_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param proposedResGrpID
      @param ds
   */  
export interface ChangeECOOpDtlResourceGrpID_input{
      /**  The proposed Resource Group ID  */  
   proposedResGrpID:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOpDtlResourceGrpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param proposedResourceID
      @param ds
   */  
export interface ChangeECOOpDtlResourceID_input{
      /**  The proposed Resource ID  */  
   proposedResourceID:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOpDtlResourceID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOOprAutoReceive_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprAutoReceive_output{
parameters : {
      /**  output parameters  */  
   opLaborEntryMethodList:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param iLaborEntryMethod
      @param ds
   */  
export interface ChangeECOOprLaborEntryMethod_input{
      /**  Proposed value for LaborEntryMethod field  */  
   iLaborEntryMethod:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprLaborEntryMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param proposedOpCode
      @param ds
   */  
export interface ChangeECOOprOpCode_input{
      /**  The proposed Operation Code  */  
   proposedOpCode:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprOpCode_output{
parameters : {
      /**  output parameters  */  
   refreshMessage:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOOprOpStdID_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprOpStdID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedOprSeq
      @param ds
   */  
export interface ChangeECOOprOprSeq_input{
      /**  The new proposed ECOOpr.OprSeq value  */  
   ipProposedOprSeq:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOOprPrimaryProdOpDtl_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprPrimaryProdOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOOprPrimarySetupOpDtl_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprPrimarySetupOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedRFQNeeded
      @param ds
   */  
export interface ChangeECOOprRFQNeeded_input{
      /**  The new proposed ECOGroup.RFQNeeded value  */  
   ipProposedRFQNeeded:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprRFQNeeded_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOOprRestriction_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedSNRequired
      @param ds
   */  
export interface ChangeECOOprSNRequiredOpr_input{
      /**  The new proposed ECOGroup.SNRequiredOpr value  */  
   ipProposedSNRequired:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprSNRequiredOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedStdFormat
      @param ds
   */  
export interface ChangeECOOprStdFormat_input{
      /**  The new proposed ECOOpr.StdFormat value  */  
   ipProposedStdFormat:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprStdFormat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedSubPartNum
      @param ds
   */  
export interface ChangeECOOprSubPartNum_input{
      /**  The new proposed ECOGroup.SubPartNum value  */  
   ipProposedSubPartNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprSubPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOOprSubstance_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprSubstance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeECOOprVendorNumVendorID_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOOprVendorNumVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedApproved
      @param ds
   */  
export interface ChangeECORevApproved_input{
      /**  The new proposed ipProposedApproved value  */  
   ipProposedApproved:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECORevApproved_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedStageSeq
      @param ds
   */  
export interface ChangeECOStageStageSeq_input{
      /**  Proposed OprSeq  */  
   ipProposedStageSeq:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeECOStageStageSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedInspPlan
      @param ipProposedSpecId
   */  
export interface ChangeEcoMtlInspPlan_input{
      /**  The new proposed ECOMtl.InspPlanPartNum value  */  
   ipProposedInspPlan:string,
      /**  The new proposed ECOMtl.SpecID value  */  
   ipProposedSpecId:string,
}

export interface ChangeEcoMtlInspPlan_output{
}

   /** Required : 
      @param mtlAttributeSetID
      @param ds
   */  
export interface ChangeEcoMtlMtlAttributeSetID_input{
   mtlAttributeSetID:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeEcoMtlMtlAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param salvAttributeSetID
      @param ds
   */  
export interface ChangeEcoMtlSalvageAttributeSetID_input{
   salvAttributeSetID:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeEcoMtlSalvageAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface ChangeEcoOprAttributeSetID_input{
   attributeSetID:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangeEcoOprAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param iAutoReceive
      @param ds
   */  
export interface ChangingECOOprAutoReceive_input{
      /**  Proposed value for AutoReceive field  */  
   iAutoReceive:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ChangingECOOprAutoReceive_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedPartNum
      @param ds
   */  
export interface CheckChangeECOCoPartNum_input{
   ipProposedPartNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckChangeECOCoPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedMtlSeq
      @param doCheck
      @param ds
   */  
export interface CheckChangeECOMtlMtlSeq_input{
      /**  Proposed MtlSeq  */  
   ipProposedMtlSeq:number,
      /**  True to perform validation, false if the user has accepted the validation message  */  
   doCheck:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckChangeECOMtlMtlSeq_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opMsgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedOprSeq
      @param doCheck
      @param ds
   */  
export interface CheckChangeECOOprOprSeq_input{
      /**  Proposed OprSeq  */  
   ipProposedOprSeq:number,
      /**  True to perform validation, false if the user has accepted the validation message  */  
   doCheck:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckChangeECOOprOprSeq_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opMsgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedApproved
      @param ipValidPassword
      @param ds
   */  
export interface CheckChangeECORevApproved_input{
      /**  The proposed Approved value  */  
   ipProposedApproved:boolean,
      /**  A valid password has been sent  */  
   ipValidPassword:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckChangeECORevApproved_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedMtlPartNum
      @param ds
   */  
export interface CheckECOMtlMtlPartNum_input{
      /**  The new proposed ttECOMtl.PartNum value  */  
   ipProposedMtlPartNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOMtlMtlPartNum_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opMsgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedMtlSeq
      @param ipProposedRelatedOperation
      @param ipProposedRelatedStage
      @param ds
   */  
export interface CheckECOMtlMtlSeqRelatedOperation_input{
      /**  The new proposed ECOMtl.MtlSeq value  */  
   ipProposedMtlSeq:number,
      /**  The new proposed ECOMtl.RelatedOperation value  */  
   ipProposedRelatedOperation:number,
      /**  The new proposed ECOMtl.RelatedStage value  */  
   ipProposedRelatedStage:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOMtlMtlSeqRelatedOperation_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opMsgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedPlanAsAsm
      @param ds
   */  
export interface CheckECOMtlPlanAsAsm_input{
      /**  The new proposed ECOMtl.PlanAsAsm value  */  
   ipProposedPlanAsAsm:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOMtlPlanAsAsm_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opMsgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedPullAsAsm
      @param ds
   */  
export interface CheckECOMtlPullAsAsm_input{
      /**  The new proposed ECOMtl.PullAsAsm value  */  
   ipProposedPullAsAsm:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOMtlPullAsAsm_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opMsgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedViewAsAsm
      @param ds
   */  
export interface CheckECOMtlViewAsAsm_input{
      /**  The new proposed ECOMtl.ViewAsAsm value  */  
   ipProposedViewAsAsm:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOMtlViewAsAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedOprSeq
      @param ds
   */  
export interface CheckECOOprOprSeq_input{
      /**  The new proposed ECOOpr.OprSeq value  */  
   ipProposedOprSeq:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOOprOprSeq_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opMsgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPrimaryProdOpDtl
   */  
export interface CheckECOOprPrimaryProdOpDtl_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
      /**  The new PrimaryProdOpDtl value to change to  */  
   ipPrimaryProdOpDtl:number,
}

export interface CheckECOOprPrimaryProdOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPrimarySetupOpDtl
   */  
export interface CheckECOOprPrimarySetupOpDtl_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
      /**  The new PrimarySetupOpDtl value to change to  */  
   ipPrimarySetupOpDtl:number,
}

export interface CheckECOOprPrimarySetupOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedPurPoint
      @param ds
   */  
export interface CheckECOOprPurPoint_input{
      /**  The new proposed ECOOpr.PurPoint value  */  
   ipProposedPurPoint:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOOprPurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedVendorNumVendorID
      @param ds
   */  
export interface CheckECOOprVendorNumVendorID_input{
      /**  The new proposed ECOOpr.VendorNumVendorID value  */  
   ipProposedVendorNumVendorID:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECOOprVendorNumVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedApproved
      @param ds
   */  
export interface CheckECORevApprovedChanging_input{
      /**  The new proposed ECORev.Approved value  */  
   ipProposedApproved:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECORevApprovedChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedApproved
      @param ipValidPassword
      @param ds
   */  
export interface CheckECORevApproved_input{
      /**  The new proposed ECOGroup.Approved value  */  
   ipProposedApproved:boolean,
      /**  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method in the
            UserFile BO.  */  
   ipValidPassword:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECORevApproved_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipProposedValResDes
      @param ds
   */  
export interface CheckECORevValRefDes_input{
      /**  The new proposed ECORev.ValRefDes value  */  
   ipProposedValResDes:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckECORevValRefDes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ipValidPassword
      @param ipAuditText
   */  
export interface CheckInAll_input{
      /**  The ECOGroup.GroupID to check in all for  */  
   ipGroupID:string,
      /**  Used for GetDatasetForTree, The Part Number to return data for.  */  
   ipPartNum:string,
      /**  Used for GetDatasetForTree, The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  Used for GetDatasetForTree, The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
      /**  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  */  
   ipValidPassword:boolean,
      /**  The text to write to the audit record(s).  */  
   ipAuditText:string,
}

export interface CheckInAll_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opResultString:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipValidPassword
      @param ipAuditText
   */  
export interface CheckInAndRefresh_input{
      /**  The Group ID to return costs for.  */  
   ipGroupID:string,
      /**  The Part Number to return costs for.  */  
   ipPartNum:string,
      /**  The Revision Number to return costs for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return costs for.  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID  */  
   ipProcessMfgID:string,
      /**  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  */  
   ipValidPassword:boolean,
      /**  The text to write to the audit record.  */  
   ipAuditText:string,
}

export interface CheckInAndRefresh_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipValidPassword
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ipAuditText
   */  
export interface CheckIn_input{
      /**  The Group ID to return costs for.  */  
   ipGroupID:string,
      /**  The Part Number to return costs for.  */  
   ipPartNum:string,
      /**  The Revision Number to return costs for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return costs for.  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  */  
   ipValidPassword:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
      /**  The text to write to the audit record.  */  
   ipAuditText:string,
}

export interface CheckIn_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipValidPassword
      @param ipCalledFromRecipe
   */  
export interface CheckOutAndRefresh_input{
      /**  The Group ID to check out for.  */  
   ipGroupID:string,
      /**  The Part Number to check out for.  */  
   ipPartNum:string,
      /**  The Revision Number to check out for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to check out for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to check out for.  */  
   ipProcessMfgID:string,
      /**  The As Of Date to check out for.  */  
   ipAsOfDate:string,
      /**  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method in the
            UserFile BO.  */  
   ipValidPassword:boolean,
      /**  Parameter to be used to know if the method is called from Engineering Workbench or Recipe Entry.  */  
   ipCalledFromRecipe:boolean,
}

export interface CheckOutAndRefresh_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opECORevSysRowID:string,
   altMethodMsg:string,
   altMethodFlg:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipValidPassword
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface CheckOut_input{
      /**  The Group ID to check out for.  */  
   ipGroupID:string,
      /**  The Part Number to check out for.  */  
   ipPartNum:string,
      /**  The Revision Number to check out for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to check out for.  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to check out for.  */  
   ipProcessMfgID:string,
      /**  The As Of Date to check out for.  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  */  
   ipValidPassword:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface CheckOut_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opCheckedOutRevisionNum:string,
   altMethodMsg:string,
   altMethodFlg:boolean,
}
}

   /** Required : 
      @param ipProposedPartNum
      @param ds
   */  
export interface CheckPreECOCoPartInfo_input{
      /**  The new proposed ECOCoPart.CoPartNum value  */  
   ipProposedPartNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface CheckPreECOCoPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param partNum
   */  
export interface CheckPrePartInfo_input{
      /**  The new PartNum if a substitute part is found, partNum will be the substitute part  */  
   partNum:string,
}

export interface CheckPrePartInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   vMessage:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param altMethod
      @param opSeq
      @param mtlSeq
      @param opDtlSeq
   */  
export interface CheckRulesBeforeDelete_input{
   partNum:string,
   revisionNum:string,
   altMethod:string,
   opSeq:number,
   mtlSeq:number,
   opDtlSeq:number,
}

export interface CheckRulesBeforeDelete_output{
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface ClearAll_input{
      /**  The Group ID to clear all for  */  
   ipGroupID:string,
      /**  The Part Number to clear all for.  */  
   ipPartNum:string,
      /**  The Revision Number to clear all for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to clear all for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to clear all for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface ClearAll_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipMtlSeq
      @param ipPrefix
      @param ipStartNum
      @param ipEndNum
      @param ipSuffix
      @param ds
   */  
export interface DeleteRefDesRange_input{
      /**  The Group ID of ECO revision  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision  */  
   ipPartNum:string,
      /**  The ECO Revision Number  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID  */  
   ipProcessMfgID:string,
      /**  The ECO Material Seq  */  
   ipMtlSeq:number,
      /**  The Prefix to be used to delete Reference Designators  */  
   ipPrefix:string,
      /**  The Starting Number to delete Reference Designators  */  
   ipStartNum:number,
      /**  The Ending Number to delete Reference Designators  */  
   ipEndNum:number,
      /**  The Suffix to be used to delete Reference Designators  */  
   ipSuffix:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface DeleteRefDesRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface ECOGroupExists_input{
      /**  The Group ID to check if it exists in the database.  */  
   ipGroupID:string,
}

export interface ECOGroupExists_output{
parameters : {
      /**  output parameters  */  
   opECOGroupExists:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface EcoOprInitSNReqSubConShip_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface EcoOprInitSNReqSubConShip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

export interface Erp_Tablesets_ECOCOPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  */  
   CoPartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  */  
   CoRevisionNum:string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   PartsPerOp:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   LbrCostBase:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   MtlCostBase:number,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   IUM:string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  If true, MRP will not generate change suggestions for the co-part  */  
   PreventSugg:boolean,
      /**  Indicates if the parent Part should be used as the primary costing method for the co-part  */  
   PrimaryCost:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   PartMasterPart:boolean,
   ProcessMode:string,
   EnablePreventSugg:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOGroupAttchRow{
   Company:string,
   GroupID:string,
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

export interface Erp_Tablesets_ECOGroupListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The text description of the ECO Group  */  
   Description:string,
      /**  Determines if the ECO group is closed or open.  */  
   GroupClosed:boolean,
      /**  ECO Group comments.  */  
   CommentText:string,
      /**  Date at which this ECO Group will become effective.  */  
   EffectiveDate:string,
      /**  Date which this ECO Group was completed.  */  
   CompletionDate:string,
      /**  Date which this ECO group is due to be completed.  */  
   DueDate:string,
      /**  Date which this ECO group was created.  Not maintainable by the user.  */  
   CreatedDate:string,
      /**  UserID who created the ECO group.  Not maintainable by the user.  */  
   CreatedBy:string,
      /**  The time (in milliseconds) that the ECO group was created.  */  
   CreatedTime:number,
      /**  Date which this ECO group was closed.  Not maintainable by the user.  */  
   ClosedDate:string,
      /**  UserID who closed the ECO group.  Not maintainable by the user.  */  
   ClosedBy:string,
      /**  The time (in milliseconds) that the ECO group was closed.  */  
   ClosedTime:number,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   ECO:string,
      /**  Unique identifier of the task set.  */  
   TaskSetID:string,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The Currently active milestone task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  If FALSE then revisions in this group may not be checked in.  */  
   CheckInAllowed:boolean,
      /**  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  */  
   PrimeSalesRepCode:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  */  
   CheckOutAllowed:boolean,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  */  
   SingleUser:boolean,
      /**  Indicates if this ECO Group is locked.  */  
   GrpLocked:boolean,
      /**  UserID that has the ECOGroup record locked  */  
   GrpLockedBy:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical to mass assign description to ecorevs  */  
   MassAssignDesc:boolean,
      /**  Flag to mass assign ECO to ecorevs  */  
   MassAssignECO:boolean,
      /**  Flag to mass assign effective date across ecorevs  */  
   MassAssignEffectiveDate:boolean,
      /**  Flag if Approve All is allowed for this group.  */  
   CanApproveAll:boolean,
      /**  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  */  
   MultiBOMAllowed:boolean,
      /**  Flag if Check In All is allowed for this group  */  
   CanCheckInAll:boolean,
      /**  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  */  
   WFGroupIDDesc:string,
      /**  If true use method for all parts in tree, otherwise use the part's default method  */  
   UseMethodForPartsInTree:boolean,
   CurrentWFStageDesc:string,
      /**  Used for enable/disable the check in all option.  */  
   EnableCheckInAll:boolean,
      /**  Description of the task set.  */  
   TaskSetIDTaskSetDescription:string,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   TaskSetIDWorkflowType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOGroupListTableset{
   ECOGroupList:Erp_Tablesets_ECOGroupListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ECOGroupRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The text description of the ECO Group  */  
   Description:string,
      /**  Determines if the ECO group is closed or open.  */  
   GroupClosed:boolean,
      /**  ECO Group comments.  */  
   CommentText:string,
      /**  Date at which this ECO Group will become effective.  */  
   EffectiveDate:string,
      /**  Date which this ECO Group was completed.  */  
   CompletionDate:string,
      /**  Date which this ECO group is due to be completed.  */  
   DueDate:string,
      /**  Date which this ECO group was created.  Not maintainable by the user.  */  
   CreatedDate:string,
      /**  UserID who created the ECO group.  Not maintainable by the user.  */  
   CreatedBy:string,
      /**  The time (in milliseconds) that the ECO group was created.  */  
   CreatedTime:number,
      /**  Date which this ECO group was closed.  Not maintainable by the user.  */  
   ClosedDate:string,
      /**  UserID who closed the ECO group.  Not maintainable by the user.  */  
   ClosedBy:string,
      /**  The time (in milliseconds) that the ECO group was closed.  */  
   ClosedTime:number,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   ECO:string,
      /**  Unique identifier of the task set.  */  
   TaskSetID:string,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The Currently active milestone task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  If FALSE then revisions in this group may not be checked in.  */  
   CheckInAllowed:boolean,
      /**  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  */  
   PrimeSalesRepCode:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  */  
   CheckOutAllowed:boolean,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  */  
   SingleUser:boolean,
      /**  Indicates if this ECO Group is locked.  */  
   GrpLocked:boolean,
      /**  UserID that has the ECOGroup record locked  */  
   GrpLockedBy:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical to mass assign description to ecorevs  */  
   MassAssignDesc:boolean,
      /**  Flag to mass assign ECO to ecorevs  */  
   MassAssignECO:boolean,
      /**  Flag to mass assign effective date across ecorevs  */  
   MassAssignEffectiveDate:boolean,
      /**  Flag if Approve All is allowed for this group.  */  
   CanApproveAll:boolean,
      /**  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  */  
   MultiBOMAllowed:boolean,
      /**  Flag if Check In All is allowed for this group  */  
   CanCheckInAll:boolean,
      /**  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  */  
   WFGroupIDDesc:string,
      /**  If true use method for all parts in tree, otherwise use the part's default method  */  
   UseMethodForPartsInTree:boolean,
   CurrentWFStageDesc:string,
      /**  Used for enable/disable the check in all option.  */  
   EnableCheckInAll:boolean,
   BitFlag:number,
   TaskSetIDWorkflowType:string,
   TaskSetIDTaskSetDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOImportRow{
      /**  The part number.  */  
   PartNum:string,
      /**  The description of the part number.  */  
   PartDescription:string,
      /**  The type code.  */  
   TypeCode:string,
      /**  The quantity per.  */  
   QtyPer:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOMtlAttchRow{
   Company:string,
   GroupID:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   ProcessMfgID:string,
   MtlSeq:number,
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

export interface Erp_Tablesets_ECOMtlInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  Parent Part number to which this material item is a component of  */  
   PartNum:string,
      /**  Revision number of the part that this material item is a component of.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  A sequence number that uniquely identifies the ECOMtlInsp record within the ECO material  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   OrigMtlSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOMtlRefDesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Identifier of Reference Designator  */  
   RefDes:string,
      /**  Unique identifies the reference designator with the material sequence.  */  
   RefDesSeq:number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   OrigMtlSeq:number,
      /**  Free form side location. (Top, Bottom, Both, Level, etc)  */  
   Side:string,
      /**  X Coordinate of the reference designator  */  
   XLocation:number,
      /**  Y Coordinate of the reference designator  */  
   YLocation:number,
      /**  Z Coordinate of the reference designator  */  
   ZLocation:number,
      /**  Rotation of the reference designator. Max value = 360.000  */  
   Rotation:number,
      /**  Designator Description  */  
   Description:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOMtlRestrictSubstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  Substance identification.  */  
   SubstanceID:string,
      /**  Default weight of the substance per primary part of UOM  */  
   Weight:number,
      /**  By default the primary UOM of the part.  */  
   WeightUOM:string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   OrigMtlSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   Exempt:boolean,
   ExemptDate:string,
   ExemptCertificate:string,
   Manual:boolean,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
   BitFlag:number,
   GroupIDDescription:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   RestrictionDescription:string,
   RevisionNumRevDescription:string,
   RevisionNumPartDescription:string,
   RevisionNumRevShortDesc:string,
   SubstanceDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOMtlRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  */  
   OrigMtlSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Yes to display when the part has no net weight or when one or more of the selected has no weight.  */  
   Weight:boolean,
   Manual:boolean,
   ComplianceDate:string,
   LastRollUp:string,
   RollUpType:string,
   BitFlag:number,
   GroupIDDescription:string,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   RestrictionDescription:string,
   RevisionNumRevShortDesc:string,
   RevisionNumPartDescription:string,
   RevisionNumRevDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Parent Part number to which this material item is a component of  */  
   PartNum:string,
      /**  Revision number of the part that this material item is a component of.  */  
   RevisionNum:string,
      /**  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  Quantity Per Parent  */  
   QtyPer:number,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**   A material record can be related to a specific operation. This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job. The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   RelatedOperation:number,
      /**  Part number for Salvageable scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvageable material. Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the QtyPer results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  Material comments specific to this manufacturing process. These comments copied to Jobs/Quotes when pulled from BOM.  */  
   MfgComment:string,
      /**  Indicates if these comments should override the comments defined in the part master. It controls how the MfgComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.MfgComments will be appended on to the Part.MfgComments when written to the Job/Quote material record.  */  
   OverRideMfgComments:boolean,
      /**   Material comments specific to a manufacturing process. These comments (and optionally the comments from Part Master) are  copied to Jobs/Quotes when the BOM is pulled.
( See OverRidePurComments )  */  
   PurComment:string,
      /**  Indicates if these comments should override the comments defined in the part master. It controls how the PurComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.PurComments will be appended on to the Part.PurComments when written to the Job/Quote material record.  */  
   OverRidePurComments:boolean,
      /**  Estimated Scrap  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   EstScrapType:string,
      /**  This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly should be pulled from stock or manufactured as part of the job it is pulled into. If PullAsAsm = No only the assembly record will be pulled into the job/quote (as a material), the related material and operations will not be pulled over.  */  
   PullAsAsm:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**   This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly when shown in ABOM indented views or on reports it should be shown either as a subassembly or material requirement.  If Yes then the assemblies components will be shown else it is shown as a single material requirement line. Similar to the PullAsAsm flag however this is used to control how subassemblies appear in the ABOM module.
NOTE: AS OF 2.70.400 this function is not implemented.  Pending further analysis. It has been added to the schema to make it easier to implement when decision has been reached.  */  
   ViewAsAsm:boolean,
      /**  Indicates which APS Scheduler module the assembly is scheduled in.  */  
   APSSchedulerName:string,
      /**  APS Start Limit date.  Prevents APS from scheduling before this date.  */  
   APSSLDate:string,
      /**  APS Start Limit time.  Time, in decimal hours, that APS will not schedule before.  Only valid if APSSLDate is valid.  */  
   APSSLTime:number,
      /**  Schedule direction.  Valid options are: F=Forward, B=Backward, C=dynamic Constraint based, W=minimum WIP, E=End of work, S=Split longest duration, X=use the direction specified in task entry in APS.  */  
   APSInsertDirection:string,
      /**  Method of insertion into schedule.  Valid values are: T=best Time, G=same Group, N=uNscheduled, F=Force Insert, I=without resource assignment.  */  
   APSInsertCriteria:string,
      /**  Used to calculated setup time during optimization.  */  
   APSAttrib1:number,
      /**  Used to calculated setup time during optimization.  */  
   APSAttrib2:number,
      /**  Used to calculated setup time during optimization.  */  
   APSAttrib3:number,
      /**  Used to calculated setup time during optimization.  */  
   APSAttrib4:number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  The salvage material burden rate for this Part Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated salvage Mtl Burden Unit Credit.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**  The material burden rate for this Part Material.  */  
   MtlBurRate:number,
      /**  Estimated Mtl Burden Unit Cost.  */  
   EstMtlBurUnitCost:number,
      /**  A flag to indicate that this part material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this part material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The original material sequence number from the PartMtl record at the time of check out. If this record was not created during check out this should remain 0.  */  
   OrigMtlSeq:number,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  A material record can be related to a specific operation by stage. This field contains the StageNumber of the operation that it is related to.  */  
   RelatedStage:string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  Parent Alternate Routing method for the part material.  */  
   ParentAltMethod:string,
      /**  Indicates the parent material sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   ParentMtlSeq:number,
      /**   Unit of Measure code of the Material requirement.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Material Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Rule Tag. Used in the configurator.  */  
   RuleTag:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  This is relevant for assemblies (Part.Method = Yes). Indicates if the sub-assemby can be spawned off to a different job.  Can be true only if PullAsAsm = true.  */  
   PlanAsAsm:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   ReassignSNAsm:boolean,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  Weight Measurement  */  
   CNWeightMeasurement:boolean,
      /**  Required Quantity  */  
   CNRequiredQty:number,
      /**  Consumed Quantity  */  
   CNConsumedQty:number,
      /**  UOM  */  
   CNUOM:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   MtlAttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  Planning Percent  */  
   PlanningPct:number,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   MtlRevisionNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
      /**  The user's response to potential question for analysis code on mtlpartnum validation.  */  
   AnswerMtlPartNumQuestion:boolean,
      /**  Attrition Rate  */  
   CNAttritionRate:number,
      /**  Used to Enable Part Inspection fields on UI  */  
   EnablePartInsp:boolean,
      /**  Should pullasasm be enabled on the UI?  */  
   EnablePullAsAsm:boolean,
      /**  Should viewasasm be enabled on the UI?  */  
   EnableViewAsAsm:boolean,
   ExpandTree:boolean,
      /**  Is this a PartMtl record?  Used for build of tree to display PartMtl as ECOMtl.  */  
   IsPartMtl:boolean,
      /**  A boolean value to determine if the Material is the Top part sales kit  */  
   IsTopPartSalesKit:boolean,
      /**  Used to enter comments for manufacturing when this part is referenced on a job.  */  
   MtlPartNumMfgComment:string,
      /**  Part Comments that will be used as a default for purchasing.  */  
   MtlPartNumPurComment:string,
      /**  Is there a revision for the MtlPartNum component of the parent partnum?  */  
   MtlRevExists:boolean,
      /**  The related operation description  */  
   OpDesc:string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
   RelatedECOOprOprSeq:number,
      /**  Salvage Base Unit of Measure  */  
   SalvageBaseUOM:string,
      /**  Salvage Part Number Track Multi UOM  */  
   SalvagePartTrackMulti:boolean,
      /**  The value of ecorev.usestaging for UI purposes.  */  
   UseStaging:boolean,
      /**  The user's response to potential question for analysis code on planasasm validation.  */  
   AnswerPlanAsAsmQuestion:boolean,
      /**  The user's response to potential question for analysis code on pullasasm validation.  */  
   AnswerPullAsAsmQuestion:boolean,
      /**  The display unit of measure for the qty/parent field.  */  
   DspUnitMeasure:string,
      /**  External field used to control the flag over the FixedQty field on UI screens.  */  
   EnableFixedQty:boolean,
   EnableAttributeSetSearch:boolean,
   SalvEnableAttSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   PlanningNumberOfPiecesDisp:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   SalvagePlanningNumberOfPiecesDisp:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   APSSchedulerNameAPSSchedulerName:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   GroupIDDescription:string,
   MtlPartNumTrackInventoryByRevision:boolean,
   MtlPartNumAttrClassID:string,
   MtlPartNumTrackInventoryAttributes:boolean,
   MtlPartNumTrackLots:boolean,
   MtlPartNumTrackDimension:boolean,
   MtlPartNumSellingFactor:number,
   MtlPartNumIUM:string,
   MtlPartNumPricePerCode:string,
   MtlPartNumTrackSerialNum:boolean,
   MtlPartNumPartDescription:string,
   MtlPartNumSalesUM:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   RevisionNumPartDescription:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   SalvagePartNumTrackInventoryByRevision:boolean,
   SalvagePartNumPricePerCode:string,
   SalvagePartNumSalesUM:string,
   SalvagePartNumTrackDimension:boolean,
   SalvagePartNumPartDescription:string,
   SalvagePartNumTrackLots:boolean,
   SalvagePartNumIUM:string,
   SalvagePartNumSellingFactor:number,
   SalvagePartNumAttrClassID:string,
   SalvagePartNumTrackInventoryAttributes:boolean,
   SalvagePartNumTrackSerialNum:boolean,
   SalvDynAttrValueSetShortDescription:string,
   SalvDynAttrValueSetDescription:string,
   StageNoDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOpDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   CapabilityID:string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  */  
   ResourceID:string,
      /**  The standard setup hours for the operation.   This is the setup time required for each machine.  */  
   SetupHours:number,
      /**  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  */  
   ProdHours:number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   NumResources:number,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   SetupOrProd:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Description is initially created when the ECOOpDtl is created.   If the ECOOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   OpDtlDesc:string,
      /**  Parent Alternate Routing method of this part operation.  */  
   ParentAltMethod:string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   ParentOprSeq:number,
      /**  Indicates the parent operation detail sequence.  */  
   ParentOpDtlSeq:number,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOpDtlSeq:number,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOprSeq:number,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Duplicated from ECOOpr.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  Duplicated from ECOOpr.SetupCrewSize. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Indicates if primary production operation.  */  
   PrimaryProd:boolean,
      /**  Indicates if primary setup operation.  */  
   PrimarySetup:boolean,
      /**  Capability description  */  
   CapabilityDesc:string,
      /**  Resource description  */  
   ResourceDesc:string,
      /**  Resource Group description  */  
   ResourceGrpDesc:string,
      /**  Is this a PartOpDtl?  Used when building the tree to show PartOpDtl as ECOOpDtl.  */  
   IsPartOpDtl:boolean,
      /**  Flag for sub contract  */  
   SubContract:boolean,
   BitFlag:number,
   CapabilityIDDescription:string,
   GroupIDDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   RevisionNumRevShortDesc:string,
   RevisionNumRevDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprActionParamRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   GroupID:string,
      /**  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part or process manufacture.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  The ID of Process Manufacturing revision.  */  
   ProcessMfgID:string,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   OprSeq:number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  A sequence number which uniquely identifies parameter within the Operation/Action set.  */  
   ActionParamSeq:number,
      /**  Data type of Action Parameter  */  
   ActionParamFieldDataType:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueCharacter:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDate:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDecimal:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueInteger:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueLogical:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprActionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   GroupID:string,
      /**  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part or process manufacture.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  The ID of Process Manufacturing revision.  */  
   ProcessMfgID:string,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   OprSeq:number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  Description of Action.  */  
   ActionDesc:string,
      /**  Indicated if this action must be completed before Operation can be completed.  */  
   Required:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprAttchRow{
   Company:string,
   GroupID:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   ProcessMfgID:string,
   OprSeq:number,
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

export interface Erp_Tablesets_ECOOprInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  Parent Part number to which this material item is a component of  */  
   PartNum:string,
      /**  Revision number of the part that this material item is a component of.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  A sequence number that uniquely identifies the ECOOprInsp ecord within the ECO operation  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOprSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprMachParamRow{
      /**  Company  */  
   Company:string,
      /**  GroupID  */  
   GroupID:string,
      /**  PartNum  */  
   PartNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  AltMethod  */  
   AltMethod:string,
      /**  OprSeq  */  
   OprSeq:number,
      /**  MachParamSeq  */  
   MachParamSeq:number,
      /**  RequestCode  */  
   RequestCode:string,
      /**  MachineNum  */  
   MachineNum:string,
      /**  ToolNum  */  
   ToolNum:string,
      /**  ParamNum  */  
   ParamNum:number,
      /**  ParamUpperLimit  */  
   ParamUpperLimit:number,
      /**  ParamNominalValue  */  
   ParamNominalValue:number,
      /**  ParamLowerLimit  */  
   ParamLowerLimit:number,
      /**  ParamDelayValue  */  
   ParamDelayValue:number,
      /**  SpecEnable  */  
   SpecEnable:boolean,
      /**  SpecControlAlarm  */  
   SpecControlAlarm:boolean,
      /**  SpecRunAlarm  */  
   SpecRunAlarm:boolean,
      /**  ProcSpecAlarm  */  
   ProcSpecAlarm:boolean,
      /**  ProcControlAlarm  */  
   ProcControlAlarm:boolean,
      /**  PartQualSpecEnable  */  
   PartQualSpecEnable:boolean,
      /**  PartQualControlEnable  */  
   PartQualControlEnable:boolean,
      /**  OrigOprSeq  */  
   OrigOprSeq:number,
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
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprRestrictSubstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   OprSeq:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  Substance identification.  */  
   SubstanceID:string,
      /**  Defaulted from Operation Master Substances.  */  
   Weight:number,
      /**  Defaulted from Operation Master Substances.  */  
   WeightUOM:string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOprSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
   Exempt:boolean,
   ExemptDate:string,
   ExemptCertificate:string,
   Manual:boolean,
   BitFlag:number,
   GroupIDDescription:string,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   RestrictionDescription:string,
   RevisionNumRevShortDesc:string,
   RevisionNumRevDescription:string,
   RevisionNumPartDescription:string,
   SubstanceDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  Restriction Type identification.  */  
   RestrictionTypeID:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOprSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Yes to display when the part has no net weight or when one or more of the selected has no weight.  */  
   Weight:boolean,
   Manual:boolean,
   ComplianceDate:string,
   BitFlag:number,
   GroupIDDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   RestrictionDescription:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   RevisionNumPartDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  Estimated Scrap  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Inventory UOM  */  
   IUM:string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  Hours required is calculated as days * 8.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  */  
   SubPartNum:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  */  
   AddlSetupHours:number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   AddlSetUpQty:number,
      /**  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  */  
   APSPrepOp:number,
      /**  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  */  
   APSNextOp:number,
      /**  Specifies the operation for which this is an alternate.  */  
   APSAltOp:number,
      /**  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  */  
   APSSpecificResource:string,
      /**   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  */  
   APSCycleTime:number,
      /**   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  */  
   APSConstantTime:number,
      /**  Used to group operations to save on setups.  */  
   APSSetupGroup:number,
      /**  Quantity of Part per cycle.  */  
   APSMakeFactor:number,
      /**  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  */  
   APSContainerSize:number,
      /**  Name of the APS Scheduler Module in which to schedule this operation.  */  
   APSSchedulerName:string,
      /**  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  */  
   APSMaxLength:number,
      /**  Time between the end of this operation and the start time of the successor operation.  */  
   APSTransferTime:number,
      /**  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  */  
   APSEffectiveness:number,
      /**  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  */  
   APSOperationClass:string,
      /**  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  */  
   APSAuxResource:string,
      /**  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  */  
   APSAddResource:string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOprSeq:number,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  */  
   StageNumber:string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  Parent Alternate Routing method of this part operation.  */  
   ParentAltMethod:string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   ParentOprSeq:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty01:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty02:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty03:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty04:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty05:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty06:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty07:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty08:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty09:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty10:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost01:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost02:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost03:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost04:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost05:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost06:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost07:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost08:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost09:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost10:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate01:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate02:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate03:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate04:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate05:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate06:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate07:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate08:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate09:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate10:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Allow use all Roles  */  
   UseAllRoles:boolean,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PctReg  */  
   PctReg:number,
      /**  SetupMaterial  */  
   SetupMaterial:number,
      /**  MaterialColorRating  */  
   MaterialColorRating:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  SetupURL  */  
   SetupURL:string,
      /**  ExpPctUp  */  
   ExpPctUp:number,
      /**  ExpCycTm  */  
   ExpCycTm:number,
      /**  ExpGood  */  
   ExpGood:number,
      /**  NonProdLimit  */  
   NonProdLimit:number,
      /**  AutoSpcEnable  */  
   AutoSpcEnable:boolean,
      /**  AutoSpcPeriod  */  
   AutoSpcPeriod:number,
      /**  PartQualEnable  */  
   PartQualEnable:boolean,
      /**  AutoSpcSubgroup  */  
   AutoSpcSubgroup:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PulsesPerCycle  */  
   PulsesPerCycle:number,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  TemplateID  */  
   TemplateID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SubRevisionNum:string,
      /**  The vendor's name and bill to address  */  
   DspBillAddr:string,
      /**  Field used to control the flag on SNRequiredSubConShip field on UI screens.  */  
   EnableSNReqSubConShip:boolean,
      /**  Used as a flag to enable controls on UI screens  */  
   EnableSNRequiredOpr:boolean,
      /**  The final operation field  */  
   FinalOpr:boolean,
      /**  Flag to let you know if you have price breaks.  */  
   HasPriceBreaks:boolean,
      /**  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  */  
   IsPartOpr:boolean,
      /**  The original or old OprSeq.  Used when changing the OprSeq.  */  
   OldOprSeq:number,
   OpStdDescription:string,
      /**  PML ID  */  
   PLMChar03:string,
      /**  Primary Resource Group description  */  
   PrimaryResourceGrpDesc:string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   PrimaryResourceGrpID:string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   RefreshResources:boolean,
      /**  The setup hours per machines.  */  
   SetHoursPerMach:number,
      /**  The standard format description.  */  
   StdFrmtDesc:string,
      /**  The value of the ecorev.usestaging field for UI purposes  */  
   UseStaging:boolean,
      /**  The auto receive field  */  
   AutoReceive:boolean,
   EnableAttributeSetSearch:boolean,
   PrimaryProdOpDtlDesc:string,
   PrimarySetupOpDtlDesc:string,
   BitFlag:number,
   AnalysisCdDescription:string,
   APSSchedulerNameAPSSchedulerName:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   GroupIDDescription:string,
   OpCodeOpDesc:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PrimaryProdOpDtlOpDtlDesc:string,
   PrimarySetupOpDtlOpDtlDesc:string,
   RevisionNumRevShortDesc:string,
   RevisionNumRevDescription:string,
   RevisionNumPartDescription:string,
   SetupGroupDescription:string,
   StageNoDescription:string,
   SubPartNumTrackInventoryAttributes:boolean,
   SubPartNumPricePerCode:string,
   SubPartNumTrackDimension:boolean,
   SubPartNumTrackSerialNum:boolean,
   SubPartNumSellingFactor:number,
   SubPartNumTrackLots:boolean,
   SubPartNumSalesUM:string,
   SubPartNumPartDescription:string,
   SubPartNumIUM:string,
   SubPartNumAttrClassID:string,
   SubPartNumTrackInventoryByRevision:boolean,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumName:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECORevAttchRow{
   Company:string,
   GroupID:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   ProcessMfgID:string,
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

export interface Erp_Tablesets_ECORevRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   RevShortDesc:string,
      /**  Used to enter a full description of the revision.  */  
   RevDescription:string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   Approved:boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   EffectiveDate:string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRSetupBurdenCost:number,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   ECO:string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  */  
   CheckInRevisionNum:string,
      /**  The date that the revision is checked in.  */  
   CheckInDate:string,
      /**  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  */  
   CheckedOut:boolean,
      /**  The date that the Part-Rev was last checked out to the group.  */  
   CheckOutDate:string,
      /**  UserID who checked out the revision.  Not maintainable by the user.  */  
   CheckedOutBy:string,
      /**  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   SearchWord:string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   PartDescription:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  Indicates if this ECO Revision is locked.  */  
   RevLocked:boolean,
      /**  UserID that has the ECORev record locked.  */  
   RevLockedBy:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  ConfigID  */  
   ConfigID:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  */  
   ProcessMode:string,
      /**  AltMethodDesc  */  
   AltMethodDesc:string,
      /**  Customs Item Number  */  
   CNCustomsItemNum:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  */  
   ProcessMfgType:string,
      /**  Description of Process Manufacturing revision.  */  
   ProcessMfgDescription:string,
      /**  ID of Revision Image.  */  
   ImageID:string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   ECPCEnabled:boolean,
   Configured:boolean,
      /**  Should the GetDetails menu options be enabled?  */  
   EnableGetDetails:boolean,
      /**  Should the UnLock menu option be enabled?  */  
   EnableUnLock:boolean,
      /**  Is the revision updateable?  Used for menu options.  */  
   EnableUpdateable:boolean,
   HasCoParts:boolean,
      /**  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  */  
   IsPartRev:boolean,
      /**  Should the Lock menu option be enabled?  */  
   EnableLock:boolean,
      /**  Handbook Line  */  
   CNHandbookLine:string,
   CNHandbookCode:string,
   CNCustomsBOM:boolean,
   isFromPartRevision:boolean,
      /**  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  */  
   AltMethodDisplay:string,
   BitFlag:number,
   GroupIDDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumTypeCode:string,
   PartRevCreatedBy:string,
   PartRevCreatedOn:string,
   PartRevApproved:boolean,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOStageRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   GroupID:string,
      /**  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part or process manufacture.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  The ID of Process Manufacturing revision.  */  
   ProcessMfgID:string,
      /**  A sequence number which uniquely identifies stage record within the stage set.  */  
   StageSeq:number,
      /**  The identification of related StageNo.  */  
   StageNumber:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  High-level descriptions of General Requirements for Stage.  */  
   GeneralRequirements:string,
   BitFlag:number,
   StageNumberDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EngWorkBenchCostsTableset{
   PartRevCosts:Erp_Tablesets_PartRevCostsRow[],
   PartRevCostsDetail:Erp_Tablesets_PartRevCostsDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EngWorkBenchTableset{
   ECOGroup:Erp_Tablesets_ECOGroupRow[],
   ECOGroupAttch:Erp_Tablesets_ECOGroupAttchRow[],
   ECORev:Erp_Tablesets_ECORevRow[],
   ECORevAttch:Erp_Tablesets_ECORevAttchRow[],
   ECOCOPart:Erp_Tablesets_ECOCOPartRow[],
   ECOMtl:Erp_Tablesets_ECOMtlRow[],
   ECOMtlAttch:Erp_Tablesets_ECOMtlAttchRow[],
   ECOMtlInsp:Erp_Tablesets_ECOMtlInspRow[],
   ECOMtlRefDes:Erp_Tablesets_ECOMtlRefDesRow[],
   ECOMtlRestriction:Erp_Tablesets_ECOMtlRestrictionRow[],
   ECOMtlRestrictSubst:Erp_Tablesets_ECOMtlRestrictSubstRow[],
   ECOOpr:Erp_Tablesets_ECOOprRow[],
   ECOOprAttch:Erp_Tablesets_ECOOprAttchRow[],
   ECOOprAction:Erp_Tablesets_ECOOprActionRow[],
   ECOOprActionParam:Erp_Tablesets_ECOOprActionParamRow[],
   ECOOprInsp:Erp_Tablesets_ECOOprInspRow[],
   ECOOprMachParam:Erp_Tablesets_ECOOprMachParamRow[],
   ECOOpDtl:Erp_Tablesets_ECOOpDtlRow[],
   ECOOprRestriction:Erp_Tablesets_ECOOprRestrictionRow[],
   ECOOprRestrictSubst:Erp_Tablesets_ECOOprRestrictSubstRow[],
   ECOImport:Erp_Tablesets_ECOImportRow[],
   ECOStage:Erp_Tablesets_ECOStageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MassCheckoutRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Yes - create new revision     
No - do not create new revision  */  
   CreateNewRev:boolean,
      /**  Part to checkout and/or create new revision for.  */  
   PartNum:string,
      /**  The Revision number to checkout or create.  */  
   RevisionNum:string,
      /**  The part number to get details from.  */  
   SourcePartNum:string,
      /**  The revision to get details from.  */  
   SourceRevisionNum:string,
   GroupID:string,
   RevShortDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MassCheckoutTableset{
   MassCheckout:Erp_Tablesets_MassCheckoutRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartRevCostsDetailRow{
      /**  The part number.  */  
   PartNum:string,
      /**  The revision number  */  
   RevisionNum:string,
      /**  The quantity  */  
   Quantity:number,
      /**  Is this approved?  */  
   Approved:boolean,
      /**  The BOM type  */  
   BOMType:string,
      /**  The BOM Level  */  
   BOMLevel:number,
      /**  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  */  
   MtlRevision:string,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  The material cost  */  
   MaterialCost:number,
      /**  The labor cost  */  
   LaborCost:number,
      /**  The burden cost  */  
   BurdenCost:number,
      /**  The subcontract cost  */  
   SubcontractCost:number,
      /**  The material burden cost  */  
   MaterialBurdenCost:number,
      /**  The total cost  */  
   TotalCost:number,
      /**  The material unit cost  */  
   MaterialUnitCost:number,
      /**  The labor unit cost  */  
   LaborUnitCost:number,
      /**  The burden unit cost  */  
   BurdenUnitCost:number,
      /**  The subcontract unit cost  */  
   SubcontractUnitCost:number,
      /**  The material burden unit cost  */  
   MaterialBurdenUnitCost:number,
      /**  The total unit cost  */  
   TotalUnitCost:number,
      /**  The quantity per parent  */  
   QtyPer:number,
      /**  The required quantity  */  
   RequiredQty:number,
      /**  The description of the part  */  
   PartDescription:string,
      /**  The effective date  */  
   EffectiveDate:string,
      /**  The BOM Sequence  */  
   BomSequence:number,
      /**  The company id.  */  
   Company:string,
      /**  The Alternate Method  */  
   AltMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRevCostsRow{
      /**  The company id.  */  
   Company:string,
      /**  The part number  */  
   PartNum:string,
      /**  The effective date  */  
   EffectiveDate:string,
      /**  The maximum level  */  
   MaxLevel:number,
      /**  Assemblies Only flag  */  
   AssembliesOnly:boolean,
      /**  The quantity  */  
   Quantity:number,
      /**  The material total cost.  */  
   MaterialTotalCost:number,
      /**  The material unit cost  */  
   MaterialUnitCost:number,
      /**  The material part cost  */  
   MaterialPartCost:number,
      /**  The labor total cost  */  
   LaborTotalCost:number,
      /**  The unit cost of labor  */  
   LaborUnitCost:number,
      /**  The part cost of labor  */  
   LaborPartCost:number,
      /**  The burden total cost  */  
   BurdenTotalCost:number,
      /**  The burden unit cost  */  
   BurdenUnitCost:number,
      /**  The burden part cost  */  
   BurdenPartCost:number,
      /**  The subcontract total cost  */  
   SubcontractTotalCost:number,
      /**  The subcontract unit cost  */  
   SubcontractUnitCost:number,
      /**  The subcontract part cost  */  
   SubcontractPartCost:number,
      /**  The material burden total cost  */  
   MtlBurdenTotalCost:number,
      /**  The material burden unit cost  */  
   MtlBurdenUnitCost:number,
      /**  The material burden part cost  */  
   MtlBurdenPartCost:number,
      /**  The cost method label  */  
   CostMethodLabel:string,
      /**  The revision number.  */  
   RevisionNum:string,
      /**  The alternate method  */  
   AltMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtEngWorkBenchTableset{
   ECOGroup:Erp_Tablesets_ECOGroupRow[],
   ECOGroupAttch:Erp_Tablesets_ECOGroupAttchRow[],
   ECORev:Erp_Tablesets_ECORevRow[],
   ECORevAttch:Erp_Tablesets_ECORevAttchRow[],
   ECOCOPart:Erp_Tablesets_ECOCOPartRow[],
   ECOMtl:Erp_Tablesets_ECOMtlRow[],
   ECOMtlAttch:Erp_Tablesets_ECOMtlAttchRow[],
   ECOMtlInsp:Erp_Tablesets_ECOMtlInspRow[],
   ECOMtlRefDes:Erp_Tablesets_ECOMtlRefDesRow[],
   ECOMtlRestriction:Erp_Tablesets_ECOMtlRestrictionRow[],
   ECOMtlRestrictSubst:Erp_Tablesets_ECOMtlRestrictSubstRow[],
   ECOOpr:Erp_Tablesets_ECOOprRow[],
   ECOOprAttch:Erp_Tablesets_ECOOprAttchRow[],
   ECOOprAction:Erp_Tablesets_ECOOprActionRow[],
   ECOOprActionParam:Erp_Tablesets_ECOOprActionParamRow[],
   ECOOprInsp:Erp_Tablesets_ECOOprInspRow[],
   ECOOprMachParam:Erp_Tablesets_ECOOprMachParamRow[],
   ECOOpDtl:Erp_Tablesets_ECOOpDtlRow[],
   ECOOprRestriction:Erp_Tablesets_ECOOprRestrictionRow[],
   ECOOprRestrictSubst:Erp_Tablesets_ECOOprRestrictSubstRow[],
   ECOImport:Erp_Tablesets_ECOImportRow[],
   ECOStage:Erp_Tablesets_ECOStageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipGroupID
   */  
export interface ExportToPLM_input{
      /**  The GroupID of the ECOGroup to export.  */  
   ipGroupID:string,
}

export interface ExportToPLM_output{
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipValidPassword
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface ExpressPartCheckOut_input{
      /**  The Part Number to check out for.  */  
   ipPartNum:string,
      /**  The Revision Number to check out for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to check out for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to check out for.  */  
   ipProcessMfgID:string,
      /**  The As Of Date to check out for.  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  */  
   ipValidPassword:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface ExpressPartCheckOut_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opCheckedOutRevisionNum:string,
   opGroupID:string,
   altMethodMsg:string,
   altMethodFlg:boolean,
}
}

export interface GetAvailTaskSets_output{
parameters : {
      /**  output parameters  */  
   newList:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
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
      @param ds
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipUseMethodForParts
   */  
export interface GetDatasetForTreeByRef_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
      /**  The Group Id to return data for.  */  
   ipGroupID:string,
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface GetDatasetForTreeByRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipUseMethodForParts
   */  
export interface GetDatasetForTree_input{
      /**  The Group Id to return data for.  */  
   ipGroupID:string,
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface GetDatasetForTree_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipFileName
      @param ds
   */  
export interface GetDetailsFromImport_input{
      /**  The Group ID of revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of revision to get details for  */  
   ipPartNum:string,
      /**  The Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to get details for.  */  
   ipProcessMfgID:string,
      /**  The filename to import from. This file should reside on the client side.  Used for messages.  */  
   ipFileName:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface GetDetailsFromImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   altMethodMsg:string,
   altMethodFlg:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipJobNum
      @param ipAssemblySeq
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface GetDetailsFromJob_input{
      /**  The Group ID of revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of revision to get details for  */  
   ipPartNum:string,
      /**  The Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to get details for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The job number to get details from  */  
   ipJobNum:string,
      /**  The assembly sequence to get details from  */  
   ipAssemblySeq:number,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface GetDetailsFromJob_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipPartRevPartNum
      @param ipPartRevRevisionNum
      @param ipPartRevAltMethod
      @param ipPartRevProcessMfgID
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ipCopyConfiguration
      @param ipGetFromConfig
   */  
export interface GetDetailsFromMethods_input{
      /**  The Group ID of ECO revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to get details for  */  
   ipPartNum:string,
      /**  The ECO Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to get details for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Part Number of part revision to get details from  */  
   ipPartRevPartNum:string,
      /**  The Part Revision Number to get details from  */  
   ipPartRevRevisionNum:string,
      /**  The Part Alternate method to get details from  */  
   ipPartRevAltMethod:string,
      /**  The Part Process Manufacturing ID to get details from  */  
   ipPartRevProcessMfgID:string,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
            refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  */  
   ipUseMethodForParts:boolean,
      /**  Logical to specify to copy the configuration  */  
   ipCopyConfiguration:boolean,
      /**  Logical to specify to copy the methods from resulting configuration  */  
   ipGetFromConfig:boolean,
}

export interface GetDetailsFromMethods_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipAssemblySeq
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface GetDetailsFromQuotes_input{
      /**  The Group ID of ECO revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to get details for  */  
   ipPartNum:string,
      /**  The ECO Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to get details for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The quote number of the QuoteAsm to get details from  */  
   ipQuoteNum:number,
      /**  The quote line of the QuoteAsm to get details from  */  
   ipQuoteLine:number,
      /**  The assemblyseq of the QuoteAsm to get details from  */  
   ipAssemblySeq:number,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface GetDetailsFromQuotes_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipPartRevPartNum
      @param ipPartRevRevisionNum
      @param ipPartRevAltMethod
      @param ipPartRevProcessMfgID
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface GetDetailsOperations_input{
      /**  The Group ID of ECO revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to get details for  */  
   ipPartNum:string,
      /**  The ECO Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to get details for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Part Number of part revision to get details from  */  
   ipPartRevPartNum:string,
      /**  The Part Revision Number to get details from  */  
   ipPartRevRevisionNum:string,
      /**  The Part Alternate method to get details from  */  
   ipPartRevAltMethod:string,
      /**  The Part Process Manufacturing ID to get details from  */  
   ipPartRevProcessMfgID:string,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
            refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface GetDetailsOperations_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipCheckOutStatus
      @param CheckUpdateLock
   */  
export interface GetECOGroupAndECORev_input{
      /**  The Group ID to return data for.  */  
   ipGroupID:string,
      /**  Return Checked Out ECORev?  */  
   ipCheckOutStatus:boolean,
      /**  Check and Update Lock?  */  
   CheckUpdateLock:boolean,
}

export interface GetECOGroupAndECORev_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   LockedMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipCheckOutStatus
   */  
export interface GetECORevData_input{
      /**  The Group ID to return data for.  */  
   ipGroupID:string,
      /**  Return Checked Out ECORev?  */  
   ipCheckOutStatus:boolean,
}

export interface GetECORevData_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param PartNum
   */  
export interface GetEcoRevPartTypeCode_input{
   PartNum:string,
}

export interface GetEcoRevPartTypeCode_output{
   returnObj:string,
}

export interface GetIfCurrentSiteHasExternalMES_output{
   returnObj:boolean,
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
   returnObj:Erp_Tablesets_ECOGroupListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
   */  
export interface GetMassCheckout_input{
   ds:Erp_Tablesets_MassCheckoutTableset[],
      /**  Group ID  */  
   groupID:string,
      /**  Part number to checkout.  */  
   partNum:string,
}

export interface GetMassCheckout_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassCheckoutTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetNewECOCOPart_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetNewECOCOPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewECOGroupAttch_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
}

export interface GetNewECOGroupAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewECOGroup_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface GetNewECOGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param mtlSeq
   */  
export interface GetNewECOMtlAttch_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   mtlSeq:number,
}

export interface GetNewECOMtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param stageNumber
   */  
export interface GetNewECOMtlByStageNumber_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   stageNumber:string,
}

export interface GetNewECOMtlByStageNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param mtlSeq
   */  
export interface GetNewECOMtlInsp_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   mtlSeq:number,
}

export interface GetNewECOMtlInsp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param mtlSeq
   */  
export interface GetNewECOMtlRefDes_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   mtlSeq:number,
}

export interface GetNewECOMtlRefDes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param mtlSeq
      @param restrictionTypeID
   */  
export interface GetNewECOMtlRestrictSubst_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   mtlSeq:number,
   restrictionTypeID:string,
}

export interface GetNewECOMtlRestrictSubst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param mtlSeq
   */  
export interface GetNewECOMtlRestriction_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   mtlSeq:number,
}

export interface GetNewECOMtlRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetNewECOMtl_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetNewECOMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface GetNewECOOpDtl_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface GetNewECOOpDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
      @param actionSeq
   */  
export interface GetNewECOOprActionParam_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
   actionSeq:number,
}

export interface GetNewECOOprActionParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface GetNewECOOprAction_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface GetNewECOOprAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface GetNewECOOprAttch_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface GetNewECOOprAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param stageNumber
   */  
export interface GetNewECOOprByStageNumber_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   stageNumber:string,
}

export interface GetNewECOOprByStageNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface GetNewECOOprInsp_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface GetNewECOOprInsp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface GetNewECOOprMachParam_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface GetNewECOOprMachParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
      @param restrictionTypeID
   */  
export interface GetNewECOOprRestrictSubst_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
   restrictionTypeID:string,
}

export interface GetNewECOOprRestrictSubst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface GetNewECOOprRestriction_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface GetNewECOOprRestriction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetNewECOOpr_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetNewECOOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetNewECORevAttch_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetNewECORevAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param processType
      @param plant
      @param recipeDesc
      @param revShortDesc
      @param revNotes
      @param effectiveDate
   */  
export interface GetNewECORevForProcessMfg_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   processType:string,
   plant:string,
   recipeDesc:string,
   revShortDesc:string,
   revNotes:string,
   effectiveDate:string,
}

export interface GetNewECORevForProcessMfg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface GetNewECORev_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
}

export interface GetNewECORev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetNewECOStage_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetNewECOStage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

export interface GetProjectRoles_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param whereClauseECOGroup
      @param whereClauseECORev
      @param whereClauseECOMtl
      @param cnHandbookCode
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsWithCustomsBOM_input{
   whereClauseECOGroup:string,
   whereClauseECORev:string,
   whereClauseECOMtl:string,
      /**  current CNHandbookCode, the corresponding ECORevs will be excluded from search result  */  
   cnHandbookCode:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsWithCustomsBOM_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseECOGroup
      @param whereClauseECOGroupAttch
      @param whereClauseECORev
      @param whereClauseECORevAttch
      @param whereClauseECOCOPart
      @param whereClauseECOMtl
      @param whereClauseECOMtlAttch
      @param whereClauseECOMtlInsp
      @param whereClauseECOMtlRefDes
      @param whereClauseECOMtlRestriction
      @param whereClauseECOMtlRestrictSubst
      @param whereClauseECOOpr
      @param whereClauseECOOprAttch
      @param whereClauseECOOprAction
      @param whereClauseECOOprActionParam
      @param whereClauseECOOprInsp
      @param whereClauseECOOprMachParam
      @param whereClauseECOOpDtl
      @param whereClauseECOOprRestriction
      @param whereClauseECOOprRestrictSubst
      @param whereClauseECOImport
      @param whereClauseECOStage
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseECOGroup:string,
   whereClauseECOGroupAttch:string,
   whereClauseECORev:string,
   whereClauseECORevAttch:string,
   whereClauseECOCOPart:string,
   whereClauseECOMtl:string,
   whereClauseECOMtlAttch:string,
   whereClauseECOMtlInsp:string,
   whereClauseECOMtlRefDes:string,
   whereClauseECOMtlRestriction:string,
   whereClauseECOMtlRestrictSubst:string,
   whereClauseECOOpr:string,
   whereClauseECOOprAttch:string,
   whereClauseECOOprAction:string,
   whereClauseECOOprActionParam:string,
   whereClauseECOOprInsp:string,
   whereClauseECOOprMachParam:string,
   whereClauseECOOpDtl:string,
   whereClauseECOOprRestriction:string,
   whereClauseECOOprRestrictSubst:string,
   whereClauseECOImport:string,
   whereClauseECOStage:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param OpCode
      @param iPlant
   */  
export interface GetSchedulingBlocks_input{
   OpCode:string,
   iPlant:string,
}

export interface GetSchedulingBlocks_output{
   returnObj:number,
}

   /** Required : 
      @param ProcessMfgType
   */  
export interface GetTreeStructure_input{
   ProcessMfgType:string,
}

export interface GetTreeStructure_output{
   returnObj:string,
}

   /** Required : 
      @param ipGroupID
   */  
export interface GroupLock_input{
      /**  The Group ID of ecogroup to lock  */  
   ipGroupID:string,
}

export interface GroupLock_output{
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ds
   */  
export interface GroupUnLock_input{
      /**  The Group ID of ecogroup to lock  */  
   ipGroupID:string,
      /**  Used for GetDatasetForTree, The Part Number to return data for.  */  
   ipPartNum:string,
      /**  Used for GetDatasetForTree, The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  Used for GetDatasetForTree, The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface GroupUnLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
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
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipSourceRowid
      @param ipOperSeq
      @param ipMtlSeq
      @param ipBeforeMtlRowid
      @param ipDroppedAs
      @param ipStageNumber
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertBOMMtlWithStageNumber_input{
      /**  The Group ID of ECO revision to drop materials to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop materials to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop materials to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop materials to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop materials for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The rowid of source record could be jobasmbl, jobmtl, or quotemtl, partmtl to be added to the parent ECORev  */  
   ipSourceRowid:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The material seq to use  */  
   ipMtlSeq:number,
      /**  The material rowid to insert material before  */  
   ipBeforeMtlRowid:string,
      /**  The character value to determine where to drop and to drop as what.
             valid values: PartMtl, JobMtl, JobAsmbl, QuoteMtl, QuoteAsm  */  
   ipDroppedAs:string,
      /**  The related stage number  */  
   ipStageNumber:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertBOMMtlWithStageNumber_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipSourceRowid
      @param ipOperSeq
      @param ipMtlSeq
      @param ipBeforeMtlRowid
      @param ipDroppedAs
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertBOMMtl_input{
      /**  The Group ID of ECO revision to drop materials to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop materials to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop materials to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop materials to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop materials for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The rowid of source record could be jobasmbl, jobmtl, or quotemtl, partmtl to be added to the parent ECORev  */  
   ipSourceRowid:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The material seq to use  */  
   ipMtlSeq:number,
      /**  The material rowid to insert material before  */  
   ipBeforeMtlRowid:string,
      /**  The character value to determine where to drop and to drop as what.
             valid values: PartMtl, JobMtl, JobAsmbl, QuoteMtl, QuoteAsm  */  
   ipDroppedAs:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertBOMMtl_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipSourceRowid
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipDroppedAs
      @param ipStageNumber
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertBOMOprWithStageNumber_input{
      /**  The Group ID of ECO revision to drop operations to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operations to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operations to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operations to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operations to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The rowid of source record could be partopr, joboper, or
             quoteopr to be added to the parent ECORev  */  
   ipSourceRowid:string,
      /**  The new operation sequence  */  
   ipNewOperSeq:number,
      /**  The material rowid to insert material before  */  
   ipBeforeOperRowid:string,
      /**  The character value to determine where to drop and to drop as what.
             valid values: PartOpr, JobOper, QuoteOpr  */  
   ipDroppedAs:string,
      /**  The stage number the operation is associated to  */  
   ipStageNumber:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertBOMOprWithStageNumber_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipSourceRowid
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipDroppedAs
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertBOMOpr_input{
      /**  The Group ID of ECO revision to drop operations to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operations to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operations to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operations to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operations to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The rowid of source record could be partopr, joboper, or
             quoteopr to be added to the parent ECORev  */  
   ipSourceRowid:string,
      /**  The new operation sequence  */  
   ipNewOperSeq:number,
      /**  The material rowid to insert material before  */  
   ipBeforeOperRowid:string,
      /**  The character value to determine where to drop and to drop as what.
             valid values: PartOpr, JobOper, QuoteOpr  */  
   ipDroppedAs:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertBOMOpr_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipPartNumMtlDelimList
      @param ipOperSeq
      @param ipBeforeMtlRowid
      @param ipReturn
      @param ipUseMethodForParts
   */  
export interface InsertMaterialDemilitedList_input{
      /**  The Group ID of ECO revision to drop part to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop part to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop part to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop part to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop part to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The delimited list of part numbers being added from the part table  */  
   ipPartNumMtlDelimList:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The material rowid to insert part before  */  
   ipBeforeMtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If true use the method passed in for all parts in the tree, if false  */  
   ipUseMethodForParts:boolean,
}

export interface InsertMaterialDemilitedList_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   ipPartNumAskDelimList:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipPartNumMtlList
      @param ipOperSeq
      @param ipBeforeMtlRowid
      @param ipReturn
      @param ipUseMethodForParts
   */  
export interface InsertMaterialList_input{
   ipGroupID:string,
   ipPartNum:string,
   ipRevisionNum:string,
   ipAltMethod:string,
   ipProcessMfgID:string,
   ipAsOfDate:string,
   ipCompleteTree:boolean,
   ipPartNumMtlList:string,
   ipOperSeq:number,
   ipBeforeMtlRowid:string,
   ipReturn:boolean,
   ipUseMethodForParts:boolean,
}

export interface InsertMaterialList_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   ipPartNumAskList:any[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipPartNumMtlDelimList
      @param ipOperSeq
      @param ipBeforeMtlRowid
      @param ipReturn
      @param ipUseMethodForParts
      @param ipStageNumber
   */  
export interface InsertMaterialWithStageNumberDemilitedList_input{
      /**  The Group ID of ECO revision to drop part to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop part to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop part to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop part to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop part to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The delimited list of part numbers being added from the part table  */  
   ipPartNumMtlDelimList:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The material rowid to insert part before  */  
   ipBeforeMtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If true use the method passed in for all parts in the tree, if false  */  
   ipUseMethodForParts:boolean,
      /**  The related stage for recipe  */  
   ipStageNumber:string,
}

export interface InsertMaterialWithStageNumberDemilitedList_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   ipPartNumAskDelimList:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipPartPartNum
      @param ipOperSeq
      @param ipMtlSeq
      @param ipBeforeMtlRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertMaterial_input{
      /**  The Group ID of ECO revision to drop part to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop part to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop part to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop part to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop part to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The part number being added from the part table  */  
   ipPartPartNum:string,
      /**  The related operation seq (or 0 if unrelated)  */  
   ipOperSeq:number,
      /**  The material seq to use  */  
   ipMtlSeq:number,
      /**  The material rowid to insert part before  */  
   ipBeforeMtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertMaterial_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipOprSeq
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipCapabilityID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertOpDtlCapability_input{
      /**  The Group ID of ECO revision to drop operation detail to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operation detail to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operation detail to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operation detail to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operation detail to  */  
   ipProcessMfgID:string,
      /**  The ECO Operation Sequence to drop operation detail to  */  
   ipOprSeq:number,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Capability ID being added  */  
   ipCapabilityID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertOpDtlCapability_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipOprSeq
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipResourceGrpID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertOpDtlResGroup_input{
      /**  The Group ID of ECO revision to drop operation detail to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operation detail to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operation detail to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operation detail to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operation detail to  */  
   ipProcessMfgID:string,
      /**  The ECO Operation Sequence to drop operation detail to  */  
   ipOprSeq:number,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Resource Group ID being added  */  
   ipResourceGrpID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertOpDtlResGroup_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipOprSeq
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipResourceID
      @param ipNewOpDtlSeq
      @param ipBeforeOpDtlRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertOpDtlResource_input{
      /**  The Group ID of ECO revision to drop operation detail to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operation detail to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operation detail to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operation detail to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operation to  */  
   ipProcessMfgID:string,
      /**  The ECO Operation Sequence to drop operation detail to  */  
   ipOprSeq:number,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Resource ID being added  */  
   ipResourceID:string,
      /**  The new operation detail seq  */  
   ipNewOpDtlSeq:number,
      /**  The operation detail rowid to insert operation detail before  */  
   ipBeforeOpDtlRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertOpDtlResource_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipOpCode
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ipStageNumber
   */  
export interface InsertOperationOPWithStageNumber_input{
      /**  The Group ID of ECO revision to drop operations to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operations to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operations to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operations to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operations to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
   ipOpCode:string,
      /**  The new operation seq  */  
   ipNewOperSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOperRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
            refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ipStageNumber:string,
}

export interface InsertOperationOPWithStageNumber_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipOpCode
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertOperationOP_input{
      /**  The Group ID of ECO revision to drop operations to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operations to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operations to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operations to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operations to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
   ipOpCode:string,
      /**  The new operation seq  */  
   ipNewOperSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOperRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertOperationOP_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipCapabilityID
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertOprCapability_input{
      /**  The Group ID of ECO revision to drop operations to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operations to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operations to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operations to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operations to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Capability ID being added  */  
   ipCapabilityID:string,
      /**  The new operation seq  */  
   ipNewOperSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOperRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertOprCapability_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipResourceGrpID
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertOprResGroup_input{
      /**  The Group ID of ECO revision to drop operations to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operations to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operations to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operations to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operations to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Resource Group ID being added  */  
   ipResourceGrpID:string,
      /**  The new operation seq  */  
   ipNewOperSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOperRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertOprResGroup_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipResourceID
      @param ipNewOperSeq
      @param ipBeforeOperRowid
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface InsertOprResource_input{
      /**  The Group ID of ECO revision to drop operations to  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to drop operations to  */  
   ipPartNum:string,
      /**  The ECO Revision Number to drop operations to  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to drop operations to  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to drop operations to  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The Resource ID being added  */  
   ipResourceID:string,
      /**  The new operation seq  */  
   ipNewOperSeq:number,
      /**  The operation rowid to insert operation before  */  
   ipBeforeOperRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface InsertOprResource_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param partNum
   */  
export interface IsTopPartSalesKit_input{
      /**  PartNum will be searched in PartMtl.MtlPartNum  */  
   partNum:string,
}

export interface IsTopPartSalesKit_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipUseMethodForParts
      @param ipFileName
      @param ds
   */  
export interface LoadFileAndGetDetailsFromImport_input{
      /**  The Group ID of revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of revision to get details for  */  
   ipPartNum:string,
      /**  The Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to get details for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  If true use the method passed in for all parts in the tree, if false use the part's default method.  */  
   ipUseMethodForParts:boolean,
      /**  The filename to import from. This file should have been uploaded to server  */  
   ipFileName:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface LoadFileAndGetDetailsFromImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface LockAllAndRefresh_input{
      /**  The Group ID to lock for.  */  
   ipGroupID:string,
}

export interface LockAllAndRefresh_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opResultString:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ds
   */  
export interface LockAll_input{
      /**  The Group ID to lock for.  */  
   ipGroupID:string,
      /**  Used for GetDatasetForTree, The Part Number to return data for.  */  
   ipPartNum:string,
      /**  Used for GetDatasetForTree, The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  Used for GetDatasetForTree, The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface LockAll_output{
parameters : {
      /**  output parameters  */  
   opResultString:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipMassAssignDesc
      @param ipMassAssignECO
      @param ipMassAssignEffectiveDate
      @param ipMADescription
      @param ipMAECO
      @param ipMAEffectiveDate
   */  
export interface MassAssignAndRefresh_input{
      /**  The Group ID to mass assign for.  */  
   ipGroupID:string,
      /**  Do you want to mass assign Description? Value comes from external ECOGroup.MassAssignDesc  */  
   ipMassAssignDesc:boolean,
      /**  Do you want to mass assign ECO?  Value comes from external ECOGroup.MassAssignECO.  */  
   ipMassAssignECO:boolean,
      /**  Do you want to mass assign Effective Date? Value comes from external ECOGroup.MassAssignEffectiveDate.  */  
   ipMassAssignEffectiveDate:boolean,
      /**  The value of the new description to be mass assigned.  */  
   ipMADescription:string,
      /**  The value of the new ECO to be mass assigned.  */  
   ipMAECO:string,
      /**  The value of the new Effective Date to be mass assigned.  */  
   ipMAEffectiveDate:string,
}

export interface MassAssignAndRefresh_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipMassAssignDesc
      @param ipMassAssignECO
      @param ipMassAssignEffectiveDate
      @param ipMADescription
      @param ipMAECO
      @param ipMAEffectiveDate
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ds
   */  
export interface MassAssign_input{
      /**  The Group ID to mass assign for.  */  
   ipGroupID:string,
      /**  Used for GetDatasetForTree, The Part Number to return data for.  */  
   ipPartNum:string,
      /**  Used for GetDatasetForTree, The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  Used for GetDatasetForTree, The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Do you want to mass assign Description? Value comes from external ECOGroup.MassAssignDesc  */  
   ipMassAssignDesc:boolean,
      /**  Do you want to mass assign ECO?  Value comes from external ECOGroup.MassAssignECO.  */  
   ipMassAssignECO:boolean,
      /**  Do you want to mass assign Effective Date? Value comes from external ECOGroup.MassAssignEffectiveDate.  */  
   ipMassAssignEffectiveDate:boolean,
      /**  The value of the new description to be mass assigned.  */  
   ipMADescription:string,
      /**  The value of the new ECO to be mass assigned.  */  
   ipMAECO:string,
      /**  The value fo the new Effective Date to be mass assigned.  */  
   ipMAEffectiveDate:string,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface MassAssign_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param sysRowID
      @param ipCreateNewRev
      @param ds
   */  
export interface OnChangingMassCheckoutCreateNewRev_input{
      /**  current row  */  
   sysRowID:string,
      /**  create new rev yes or no  */  
   ipCreateNewRev:boolean,
   ds:Erp_Tablesets_MassCheckoutTableset[],
}

export interface OnChangingMassCheckoutCreateNewRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassCheckoutTableset[],
}
}

   /** Required : 
      @param sysRowID
      @param checkoutRev
      @param ipProposedRevisionNum
      @param ds
   */  
export interface OnChangingMassCheckoutRevisionNum_input{
      /**  current row  */  
   sysRowID:string,
      /**  True = checkout part revision, false = details revision  */  
   checkoutRev:boolean,
   ipProposedRevisionNum:string,
   ds:Erp_Tablesets_MassCheckoutTableset[],
}

export interface OnChangingMassCheckoutRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassCheckoutTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingMtlRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface OnChangingMtlRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param processMfgType
      @param ds
   */  
export interface OnChangingProcessMfgType_input{
   processMfgType:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface OnChangingProcessMfgType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param salvageNumberOfPieces
      @param ds
   */  
export interface OnChangingSalvageNumberOfPieces_input{
   salvageNumberOfPieces:number,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface OnChangingSalvageNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingSalvageRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface OnChangingSalvageRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingSubRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface OnChangingSubRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipPartRevPartNum
      @param ipPartRevRevisionNum
      @param ipPartRevAltMethod
      @param ipPartRevProcessMfgID
   */  
export interface PreGetDetailsAndReturnConfigType_input{
      /**  The Group ID of ECO revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to get details for  */  
   ipPartNum:string,
      /**  The ECO Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to get details for  */  
   ipProcessMfgID:string,
      /**  The Part Number of part revision to get details from  */  
   ipPartRevPartNum:string,
      /**  The Part Revision Number to get details from  */  
   ipPartRevRevisionNum:string,
      /**  The Part Alternate method to get details from  */  
   ipPartRevAltMethod:string,
      /**  The Part Process Manufacturing ID to get details from  */  
   ipPartRevProcessMfgID:string,
}

export interface PreGetDetailsAndReturnConfigType_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
   configType:string,
   configURL:string,
   configID:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipPartRevPartNum
      @param ipPartRevRevisionNum
      @param ipPartRevAltMethod
      @param ipPartRevProcessMfgID
   */  
export interface PreGetDetails_input{
      /**  The Group ID of ECO revision to get details for  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision to get details for  */  
   ipPartNum:string,
      /**  The ECO Revision Number to get details for  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method to get details for  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID to get details for  */  
   ipProcessMfgID:string,
      /**  The Part Number of part revision to get details from  */  
   ipPartRevPartNum:string,
      /**  The Part Revision Number to get details from  */  
   ipPartRevRevisionNum:string,
      /**  The Part Alternate method to get details from  */  
   ipPartRevAltMethod:string,
      /**  The Part Process Manufacturing ID to get details from  */  
   ipPartRevProcessMfgID:string,
}

export interface PreGetDetails_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessMassCheckout_input{
   ds:Erp_Tablesets_MassCheckoutTableset[],
}

export interface ProcessMassCheckout_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassCheckoutTableset[],
}
}

export interface PromptForPassword_output{
parameters : {
      /**  output parameters  */  
   opPromptForPassword:boolean,
}
}

   /** Required : 
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface RequestApproveExternalMESValidation_input{
      /**  The Group ID of ECO revision  */  
   groupID:string,
      /**  The Part Number of ECO revision  */  
   partNum:string,
      /**  The ECO Revision Number  */  
   revisionNum:string,
      /**  The ECO Alternate Method  */  
   altMethod:string,
      /**  The ECO Process Manufacturing ID  */  
   processMfgID:string,
}

export interface RequestApproveExternalMESValidation_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipResequenceBy
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface ResequenceMaterials_input{
      /**  The Group ID to resequence for.  */  
   ipGroupID:string,
      /**  The Part Number to resequence for.  */  
   ipPartNum:string,
      /**  The Revision Number to resequence for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to resequence for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to resequence for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  The way the user wants the material resequenced by.
             Valid Values: Material, Part, Item  */  
   ipResequenceBy:string,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface ResequenceMaterials_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface ResequenceOperations_input{
      /**  The Group ID to resequence for.  */  
   ipGroupID:string,
      /**  The Part Number to resequence for.  */  
   ipPartNum:string,
      /**  The Revision Number to resequence for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to resequence for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to resequence for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface ResequenceOperations_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ds
   */  
export interface RevisionLock_input{
      /**  The Group ID of revision to lock  */  
   ipGroupID:string,
      /**  The Part Number of revision to lock  */  
   ipPartNum:string,
      /**  The Revision Number to lock  */  
   ipRevisionNum:string,
      /**  The Alternate Method to lock  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to lock for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface RevisionLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ds
   */  
export interface RevisionUnLock_input{
      /**  The Group ID of revision to unlock  */  
   ipGroupID:string,
      /**  The Part Number of revision to unlock  */  
   ipPartNum:string,
      /**  The Revision Number to unlock  */  
   ipRevisionNum:string,
      /**  The Alternate Method to unlock  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to unlock  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface RevisionUnLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface UnLockAllAndRefresh_input{
      /**  The Group ID to unlock for.  */  
   ipGroupID:string,
}

export interface UnLockAllAndRefresh_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opResultString:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ds
   */  
export interface UnLockAll_input{
      /**  The Group ID to unlock for.  */  
   ipGroupID:string,
      /**  Used for GetDatasetForTree, The Part Number to return data for.  */  
   ipPartNum:string,
      /**  Used for GetDatasetForTree, The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  Used for GetDatasetForTree, The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface UnLockAll_output{
parameters : {
      /**  output parameters  */  
   opResultString:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
      @param ds
   */  
export interface UndoCheckOut_input{
      /**  The Group ID to check out for.  */  
   ipGroupID:string,
      /**  The Part Number to check out for.  */  
   ipPartNum:string,
      /**  The Revision Number to check out for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to check out for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to check out for.  */  
   ipProcessMfgID:string,
      /**  The As Of Date to check out for.  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface UndoCheckOut_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param EngWorkBenchData
   */  
export interface UpdateCurrentECORev_input{
   EngWorkBenchData:any,      //schema had no properties on an object.
}

export interface UpdateCurrentECORev_output{
parameters : {
      /**  output parameters  */  
   EngWorkBenchData: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateCurrentPartECORev_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface UpdateCurrentPartECORev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param EngWorkBenchData
   */  
export interface UpdateECORev_input{
   EngWorkBenchData:any,      //schema had no properties on an object.
}

export interface UpdateECORev_output{
parameters : {
      /**  output parameters  */  
   EngWorkBenchData: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtEngWorkBenchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtEngWorkBenchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdatePartECORev_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface UpdatePartECORev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipCompleteTree
      @param ipReturn
      @param ipGetDatasetForTree
      @param ipUseMethodForParts
   */  
export interface ValidateBill_input{
      /**  The Group ID to return costs for.  */  
   ipGroupID:string,
      /**  The Part Number to return costs for.  */  
   ipPartNum:string,
      /**  The Revision Number to return costs for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return costs for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to return costs for  */  
   ipProcessMfgID:string,
      /**  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
      /**  Logical to determine if you would like the dataset refreshed and brought back  */  
   ipReturn:boolean,
      /**  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  */  
   ipGetDatasetForTree:boolean,
      /**  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  */  
   ipUseMethodForParts:boolean,
}

export interface ValidateBill_output{
   returnObj:Erp_Tablesets_EngWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipProposedInspPlan
      @param ipProposedSpecId
      @param iptable
      @param ds
   */  
export interface ValidateInspection_input{
      /**  The new proposed InspPlanPartNum value  */  
   ipProposedInspPlan:string,
      /**  The new proposed SpecID value  */  
   ipProposedSpecId:string,
      /**  table name  */  
   iptable:string,
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}

export interface ValidateInspection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EngWorkBenchTableset[],
}
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
   */  
export interface ValidateRefDes_input{
      /**  The Group ID of ECO revision  */  
   ipGroupID:string,
      /**  The Part Number of ECO revision  */  
   ipPartNum:string,
      /**  The ECO Revision Number  */  
   ipRevisionNum:string,
      /**  The ECO Alternate Method  */  
   ipAltMethod:string,
      /**  The ECO Process Manufacturing ID  */  
   ipProcessMfgID:string,
}

export interface ValidateRefDes_output{
}

   /** Required : 
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipAsOfDate
      @param ipQuantity
      @param ipMaxLevel
      @param ipAssembliesOnly
   */  
export interface ViewCosts_input{
      /**  The Group ID to return costs for.  */  
   ipGroupID:string,
      /**  The Part Number to return costs for.  */  
   ipPartNum:string,
      /**  The Revision Number to return costs for.  */  
   ipRevisionNum:string,
      /**  The Alternate method to return costs for.  */  
   ipAltMethod:string,
      /**  The Process Manufacturing ID to return costs for.  */  
   ipProcessMfgID:string,
      /**  The As of Date to return costs for.  */  
   ipAsOfDate:string,
      /**  The Quantity to return costs for.  */  
   ipQuantity:number,
      /**  The Max Level to return costs for.  */  
   ipMaxLevel:number,
      /**  Assemblies only?  */  
   ipAssembliesOnly:boolean,
}

export interface ViewCosts_output{
   returnObj:Erp_Tablesets_EngWorkBenchCostsTableset[],
}

   /** Required : 
      @param ipCompany
      @param ipGroupID
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipOprSeq
   */  
export interface getNextOpDtlSeq_input{
   ipCompany:string,
   ipGroupID:string,
   ipPartNum:string,
   ipRevisionNum:string,
   ipAltMethod:string,
   ipProcessMfgID:string,
   ipOprSeq:number,
}

export interface getNextOpDtlSeq_output{
   returnObj:number,
}

